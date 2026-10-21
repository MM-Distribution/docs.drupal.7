---
title: "Yin/Yang Multisite Staging"
source_url: "https://www.drupal.org/docs/7/howtos/yinyang-multisite-staging"
page_type: page
last_updated: "Last updated on 26 January 2018"
published: "2010-10-15T13:34:34+00:00"
modified: "2018-01-26T00:15:21+00:00"
breadcrumb: ["Drupal 7", "Site building and development HowTos for Drupal 7"]
fetched: "2026-10-21T08:07:45Z"
raw: "raw/docs/7/howtos/yinyang-multisite-staging.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Yin/Yang Multisite Staging

## Overview

A key challenge in using a content management system is providing a facility for staging: for large changes to the system to be tested in a sandbox and then seamlessly deployed to a production site with a minimum of downtime. The situation becomes more complex when using a drupal-multisite install where multiple independent sites are dependent on a single Drupal install with some themes or modules managed separately and where the settings directories require correct DNS resolution to work properly. This document describes a system for using virtual hosts to provide a sandbox running on an alternate portnumber for development and scripts to migrate data between the two installations (yin and yang) where either can be production or sandbox. In this system, one script migrates such that data always flows from production to development (but also backs up the previous production environment) and another simply switches which environment is production and which is development.

## Uses

You can use the system in a variety of ways. In the simplest case, you populate the development site with a copy of the current production site for testing, for example, installing new modules. Once you've confirmed that the modules don't cause a problem in the testing environment, you can install them on the production site with the knowledge that they're unlikely to cause a problem. When you need to make a major update, you can warn your content managers to not add new content while you repopulate the development space and then apply your changes. Once you've checked that the development space appears to be functioning correctly, you can run the second script (swdev.sh), which exchanges the development site for the production one (by switching the symbolic links). You can then ask your user community to check all of the sites to ensure there are no serious problems. Until you repopulate the development space, your old production environment is preserved there, which enables you to switch back immediately, if any serious problems are discovered.

It is not a panacea: it does not allow people to continue adding content while updates are happening. Anything added to the production site after you populate the development space will be lost when you switch. But it does provide a sandbox for multisite testing and development and allows your production site to continue to be available while you perform large updates and testing and to switch to the new site with zero downtime.

## How to Set up Yin/Yang Staging

First, create two directories that will be your document roots: htdocs-yin and htdocs-yang. These are the actual directories that will ultimately each contain a copy of your single Drupal install used for Drupal multisite. Create symbolic links in the same place htdocs pointing at htdocs-yin and htdocs-dev pointing at htdocs-yang.

Second, create a virtual host entry for htdocs-dev running on an alternate port (e.g. 8080). If you plan to use the Securepages module, you should craft this virtual host to use https (and set securepages to not fall back to HTTP). Otherwise, when you try to authenticate, you will be directed away from your sandbox to the secure version of your production site on port 443.

Third, untar and place Drupal source folders re-named "drupal6", "drupal7", etc, in htdocs, and create symbolic links that point to each of the elements in the source folder. Install Drupal as usual in htdocs-yin/sites/default. Instead of one database, create two databases: dbname-yin and dbname-yang. Under some circumstances MySQL will complain about database names that have hyphens -- enclose the name in backticks. Set up settings.php as usual, and refer to dbname-yin. Additional subsites can be created in the multisite by creating additional directories with symlinks referencing the correct version of Drupal. In this way, you can support a mix of Drupal 6, 7, and 8 sites.

Fourth, install the two scripts below and configure them appropriately for your environment.

**mkdev.php**

``` php
#! /usr/bin/php
<?
# database stem => settings directory
$sites = array(
  "example" => "default",
  #"sitetwo" => "www.example.com.sitetwo",
  );
$apachepath = "/var/www";
$sed = "/bin/sed";
$tar = "/bin/tar";
$mysqlpath = "/usr/local/bin";
$htdocs = "htdocs";
$mroot = "xxxxxxx";
$admin = "root";
$agrp = "wwwadmin";
$mysock = "/tmp/mysqld.sock";

list($htdocs,$yinyang) = split("-", readlink("${apachepath}/${htdocs}"));

if($yinyang == "yin") {
  $dev = "yang";
}
elseif($yinyang == "yang")  {
  $dev = "yin";
}
else {
  die("Couldn't get yin/yang.\n");
}

if($dev) {
  $now = date("YmdHis");
  system("mv ${apachepath}/${htdocs}-${dev} ${apachepath}/${htdocs}-dev-${now};
          mkdir -m 775 ${apachepath}/${htdocs}-${dev};
          chown ${admin} ${apachepath}/${htdocs}-${dev};
          chgrp ${agrp} ${apachepath}/${htdocs}-${dev};
          cd ${apachepath}/${htdocs}; ${tar} cf - . | (cd ${apachepath}/${htdocs}-${dev}; ${tar} xfBp -)");
  foreach($sites as $db => $settings) {
    system("${mysqlpath}/mysqldump -S ${mysock} -f -uroot -p${mroot} --extended-insert=false $db-${dev} >${apachepath}/${htdocs}-dev-${now}/sites/${settings}/${db}.sql");
    system("${mysqlpath}/mysqladmin -S ${mysock} -f -uroot -p${mroot} drop ${db}-${dev}");
    system("${mysqlpath}/mysqladmin -S ${mysock} -f -uroot -p${mroot} create ${db}-${dev}");
    system("${mysqlpath}/mysqldump -S ${mysock} -uroot -p${mroot} ${db}-${yinyang} | ${mysqlpath}/mysql  -S ${mysock} -uroot -p${mroot} ${db}-${dev}");
    system("${sed} s/-${yinyang}/-${dev}/ <${apachepath}/${htdocs}/sites/${settings}/settings.php >${apachepath}/${htdocs}-${dev}/sites/${settings}/settings.php");
  }
}

?>
```

**swdev.sh**

``` php
#! /bin/sh

# script to switch between production and development web spaces
# test presence of symbolic links, then move devel to temp,
# move current to devel, and move temp to current
# sbrewer and george 20100416

APACHEPATH=/var/www
HTDOCS=htdocs
DEV=htdocs-dev
TEMP=htdocs-swdevtmp
if [ -L ${APACHEPATH}/${HTDOCS} -a -L ${APACHEPATH}/${DEV} ] ;
then 
mv ${APACHEPATH}/${DEV} ${APACHEPATH}/${TEMP};
mv ${APACHEPATH}/${HTDOCS} ${APACHEPATH}/${DEV};
mv ${APACHEPATH}/${TEMP} ${APACHEPATH}/${HTDOCS};
fi
```

Once you have populated your production site, run mkdev.php, which should (1) backup your (empty) htdocs-dev (in actuality htdocs-yang) directory, (2) copy htdocs into a new htdocs-dev directory, (3) dump the empty dbname-yang database (which will generate a warning), (4) copy dbname-yin into dbname-yang, and (5) rewrite the settings.php in default to to use dbname-yang. You should now be able to visit your production site on port 8080 and confirm that the sandbox has been populated.

For each additional site you add, add an additional line to mkdev.php.

Rerun mkdev.php any time to repopulate the development space

Run swdev.sh to switch which (yin or yang) is production and which is development.

## Acknowledgments

Special thanks to George Drake for many suggestions and help with Bourne shell script.
