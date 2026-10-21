---
title: "Secure multi-site setup using shared code-base"
source_url: "https://www.drupal.org/docs/7/multisite-drupal/secure-multi-site-setup-using-shared-code-base"
page_type: page
last_updated: "Last updated on 15 September 2016"
published: "2009-05-29T14:14:00+00:00"
modified: "2016-09-15T15:31:37+00:00"
breadcrumb: ["Drupal 7", "Multisite Drupal 7"]
fetched: "2026-10-21T06:13:35Z"
raw: "raw/docs/7/multisite-drupal/secure-multi-site-setup-using-shared-code-base.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Secure multi-site setup using shared code-base

Building on comments from [this forum topic](http://drupal.org/node/39807), I've implemented a shared code-base system which has the following features:

- keeps user data separate - no user can see the files of another user, no browser client can access information from another site
- contributed modules/themes can be shared or single-site - commonly used modules can be shared across all sites, but custom themes or unusual modules can be installed for a single site
- core updates can be applied selectively - one site can be updated to a new core version, another can wait (e.g. for a contributed module to to be upgraded) and upgrade later (or even revert completely using database snapshots). Multiple code-base versions can run concurrently, shared by an arbitrary number of sites as required.
- works with PHP user_base security - this needs php.ini or httpd.conf modification to whitelist the shared code-base directory
- prevents users modifying shared code or symlinks - all shared files and links are not owned by the site user, they have read-only access
- works with user control panels like cPanel - installs into a user's public_html or www directory (or a sub-directory)
- works with any file transfer method - users have full control of their own files, but no-one elses

The examples below use Drupal 6, but the setup is known to work for Drupal 7 too.

Each Drupal core version is owned by a system user ('cms' in my case) and installed in a sub-directory of:

``` php
/usr/local/drupal/
```

So for example 6.12 would be downloaded and extracted to:

``` php
/usr/local/drupal/drupal-6.12
```

Each site is deployed with 2 sets of symlinks:

``` php
/home/[username]/drupal_home
```

which contains the reference to the version of drupal to be used:

``` php
/home/[username]/drupal_home/current -> /usr/local/drupal/drupal-6.12
```

And the site content, which is usually in a sub-directory of the user's home directory:

``` php
/home/[username]/public_html
```

Symlinks in here reference the drupal_home symlink above:

``` php
.htaccess -> ../drupal_home/current/.htaccess
cron.php -> ../drupal_home/current/cron.php
includes/ -> ../drupal_home/current/includes
index.php -> ../drupal_home/current/index.php
misc/ -> ../drupal_home/current/misc
modules -> ../drupal_home/current/modules
profiles/ -> ../drupal_home/current/profiles
scripts/ -> ../drupal_home/current/scripts
themes-> ../drupal_home/current/themes
update.php -> ../drupal_home/current/update.php
xmlrpc.php -> ../drupal_home/current/xmlrpc.php
```

Shared contributed modules and themes are placed in the sites/all directory of the shared code-base, then linked from each site:

``` php
sites/all-> ../drupal_home/current/sites/all
```

All other files and sub-directories are unique to the site:

``` php
sites/default/...
sites/[sitename]/...
files/...
robots.txt
```

So the 'settings.php' file and 'files' directory particularly are only accessible by the site's user. If an unusual .htaccess file is required this can replace the symlink to the shared one. Themes and modules unique to one site can be placed in the sites/default directory, or the sites/\[sitename\] if using multiple domains with one installation.

To update this site to a new version of drupal, download the new core files and extract as above. Shared modules need to be copied from the previous version's sites/all directory, and tested to confirm compatibility using a sandpit site. This may seem like an unnecessary duplication of code, but it allows different versions of modules to be used with different version of the core. Once you're ready simply change the drupal_home link for each site:

``` php
/home/[username]/drupal_home/current -> /usr/local/drupal/drupal-6.13
```

All the public_html linked files/sub-directories (listed above) will be instantly updated to point to the updated files. Themes and modules unique to each site are preserved across updates.

To simplify the setup of each site I've written (or modified from Geary's contributions in the forum thread) scripts to automate each stage of the process:

1.  drupal_install.sh - initial deployment of a new site
2.  drupal_update.sh - change or rebuild the links (e.g. when moving Drupal to a different sub-directory)
3.  drupal_link.sh - points the site to a new version

The install script produces a comprehensive starting website including initial module configuration and admin user. It does this by dumping a snapshot of a skeleton installation and using this to create a new database for the user's site. A skeleton file structure is copied to the public_html directory when which contains the basic initial layout for the site's files and sub-directories. The access privileges for the installation directory are then set to allow both the user and drupal (running under Apache as 'nobody' group) to read and write as appropriate.

The update script supports moving the drupal_home directory or the site's installation directory (e.g. promoting it from a sub-directory to the root) while maintaining or rebuilding the links. The versions changer simply updates the current version to a different specified one.

The scripts allow you to install in sub-directories of the public_html directory (or anywhere else), and optionally specify the owning user, drupal_home location, database name, database user (if different) and various other options. Full listings and instructions are detailed below.

The skeleton installation copies a directory containing the following files and sub-directories:

``` php
/usr/local/drupal/skeleton
                   |- public_html
                   |   |- robots.txt
                   |   |- logo.gif
                   |   |- favicon.ico
                   |   |- files
                   |   |   |- images
                   |   |       |- temp
                   |   |- sites
                   |   |   |- default
                   |   |       |- settings.php
                   |   |- uploads
                   |       |- images
                   |- drupal_home
                       |- current -> /usr/local/drupal/drupal-6.12
```

The graphics and images sub-directories are there to allow me to deploy the initial site ready-branded and with image upload support configured, but any shared files you want can be put here and will be copied to each new installation.

## drupal_install.sh

``` php
#!/bin/sh

if [ $# = "0" ]; then
echo "drupal_install: usage: drupal_install username db_pwd [drupal_home] [database] [db_user]"
exit 1;
fi

#default settings
USER=$1
DB_USER=$USER'_'public
DB_PWD=$2
DB=$USER'_'drupal
DIR=../drupal_home

if [ -n "$3" ]; then
DIR=$3
fi

if [ -n "$4" ]; then
DB=$USER'_'$4
fi

if [ -n "$5" ]; then
DB_USER=$USER'_'$5
fi

echo
echo Drupal installation script for $USER

check() {
    test -e $1 && {
        echo
        echo "$PWD/$1 exists, Drupal installation canceled"
        echo
        exit 1
    }
}

backup() {
    test -e $1 && {
        echo
        echo "$PWD/$1 exists, removing."
        echo
        mv $1 $1.bak
    }
}

backup index.html  # not part of Drupal, but suspicious
backup .htaccess

check index.php
check cron.php
check index.php
check xmlrpc.php

check database
check includes
check misc
check modules
check scripts
check themes

echo
echo "Installing Drupal in $PWD"
echo Will create a new database $DB accessed by $DB_USER using password $DB_PWD
echo
echo "Type OK to install:"

read ok
case $ok in
  [Oo][Kk] )
    echo
    echo "Installing now..."
    echo
    ;;
  * )
    echo
    echo "Installation canceled"
    echo
    exit 2
    ;;
esac


echo Creating database and MySQL user...
echo "CREATE DATABASE IF NOT EXISTS $DB;" > /usr/local/drupal/scripts/mysql.tmp
echo "GRANT ALL PRIVILEGES ON $DB.* TO '$DB_USER' IDENTIFIED BY '$DB_PWD';" >> /usr/local/drupal/scripts/mysql.tmp
mysql < /usr/local/drupal/scripts/mysql.tmp
rm -f /usr/local/drupal/scripts/mysql.tmp

echo Populating database with initial settings...
mysqldump cms_drupal > /usr/local/drupal/scripts/cms_content.sql
mysql $DB < /usr/local/drupal/scripts/cms_content.sql

echo Checking drupal_home in $DIR...
test ! -d $DIR && {
  echo Creating drupal_home in $DIR...
  mkdir $DIR
}
cp -rp /usr/local/drupal/skeleton/drupal_home/* $DIR

echo Copying skeleton file structure to $PWD...
cp -rp /usr/local/drupal/skeleton/public_html/* .
chown -R $USER:nobody .
sed -i s#username:password@localhost/databasename#$DB_USER:$DB_PWD@localhost/$DB# sites/default/settings.php
cp -p sites/default/settings.php $DIR/settings.php

echo Creating code-base symlinks in $PWD to $DIR...
ln -sf $DIR/current/.htaccess .htaccess
ln -sf $DIR/current/xmlrpc.php xmlrpc.php
ln -sf $DIR/current/cron.php cron.php
ln -sf $DIR/current/index.php index.php
ln -sf $DIR/current/update.php update.php
ln -sf $DIR/current/includes includes
ln -sf $DIR/current/misc misc
ln -sf $DIR/current/modules modules
ln -sf $DIR/current/profiles profiles
ln -sf $DIR/current/scripts scripts
ln -sf $DIR/current/themes themes
ln -s  ../$DIR/current/sites/all sites/all

echo Done! Log in now to set site information and theme, create users etc.
echo Remember to add a cron job to call cron.php too!
exit 0;
```

## drupal_update.sh

``` php
#!/bin/sh

if [ $# = "0" ]; then
echo "drupal_update: usage: drupal_update username drupal_home"
exit 1;
fi

#default settings
USER=$1
DIR=../drupal_home

if [ -n "$2" ]; then
DIR=$2
fi

echo
echo "Drupal update script for $USER"
echo "creating Drupal code-base links in $DIR"
echo "And over-writing Drupal in $PWD"
echo
echo "Type OK to proceed:"

read ok
case $ok in
  [Oo][Kk] )
    echo
    echo "Updating now..."
    echo
    ;;
  * )
    echo
    echo "Update canceled"
    echo
    exit 2
    ;;
esac

backup() {
    test -e $1 && {
        echo
        echo "$PWD/$1 exists, renaming."
        echo
        mv $1 $1.bak
    }
}

backup $DIR

cp -rp /usr/local/drupal/skeleton/drupal_home $DIR
DB=$USER'_'drupal
DUMPTO=$DIR/$USER'_'drupal.sql
mysqldump $DB > $DUMPTO
chown -R $USER:nobody $DIR
cp -p sites/default/settings.php $DIR

ln -sf $DIR/current/.htaccess .htaccess
ln -sf $DIR/current/xmlrpc.php xmlrpc.php
ln -sf $DIR/current/cron.php cron.php
ln -sf $DIR/current/index.php index.php
ln -sf $DIR/current/update.php update.php
rm -f includes misc modules profiles scripts themes
ln -sf $DIR/current/includes includes
ln -sf $DIR/current/misc misc
ln -sf $DIR/current/modules modules
ln -sf $DIR/current/profiles profiles
ln -sf $DIR/current/scripts scripts
ln -sf $DIR/current/themes themes
rm -f sites/all
ln -s ../$DIR/current/sites/all sites/all
```

## drupal_link.sh

``` php
#/bin/bash
if [ $# = "0" ]; then
echo "link_update: usage: link_update drupal_version [sub-directory=current]"
exit 1;
fi

OLD=current
NEW=/usr/local/drupal/drupal-$1

if [ -n "$2" ]; then
OLD=$2
fi



echo
echo "Drupal directory update script"
echo "Changing Drupal code-base link to $NEW"
echo "And over-writing $OLD in $PWD/$OLD"
echo
echo "Type OK to proceed:"

read ok
case $ok in
  [Oo][Kk] )
    echo
    echo "Updating now..."
    echo
    ;;
  * )
    echo
    echo "Update canceled"
    echo
    exit 2
    ;;
esac

echo "Current link:"
ls -l $OLD
rm -f $OLD
ln -s $NEW $OLD
echo "New link:"
ls -l $OLD
```

This has been tested and tweaked for several months on a server hosting over 20 Drupal sites, upgrading each site from 6.10 \> 6.11 \> 6.12 without serious issues.

Corrections and suggestions gratefully received!
