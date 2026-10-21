---
title: "Multisite Mapping with Drupal"
source_url: "https://www.drupal.org/docs/7/multisite-drupal/multisite-mapping-with-drupal"
page_type: page
last_updated: "Last updated on 27 April 2018"
published: "2016-02-22T13:28:26+00:00"
modified: "2018-04-27T01:31:58+00:00"
breadcrumb: ["Drupal 7", "Multisite Drupal 7"]
fetched: "2026-10-21T06:13:20Z"
raw: "raw/docs/7/multisite-drupal/multisite-mapping-with-drupal.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Multisite Mapping with Drupal

Here I present my recommended settings on Drupal in related to Single Site / Multisite of [Drupal Installation](https://www.drupal.org/documentation/install "Drupal Installation") by mapping *[Subdomains](https://simple.wikipedia.org/wiki/Subdomain "Subdomain")* and *[URL's Paths](https://en.wikipedia.org/wiki/Uniform_Resource_Locator#Syntax "Uniform Resource Locator")*.

To begin this documentation let's take a [domain](https://en.wikipedia.org/wiki/Domain_name "Domain name") written pure html called `www.example.com` and a drupal instance as a subdomain called `dev.example.com`.

The main domain `example.com` is placed directly at the root of `public_html` while the drupal instance is placed at `public_html/drupal`.

## Single Drupal Site (Default)

Figure out the structure of our discussed `public_html` directory along with the domain / subdomain pointing and where the URLs are going as shown below:

``` php
/public_html  <-- where example.com, www.example.com, dev.example.com are pointing
    .htaccess         <-- root's .htaccess
    index.html        <-- http://example.com, http://www.example.com
    /drupal               <-- drupal root folder
        .htaccess         <-- drupal's .htaccess
        index.php         <-- http://dev.example.com
        /sites                <-- drupal's file system folder
            /default          <-- drupal's default subfolder 
            setting.php       <-- drupal's default setting (dev.example.com)
```

### URL-Rewriting on root's .htaccess

If the above configuration is the same as yours then I would like to endorse the most reliable code that I got so far for *[URL-Rewriting](http://httpd.apache.org/docs/current/mod/mod_rewrite.html "Apache Module mod_rewrite")* on `/public_html/.htaccess` as follow:

``` php
RewriteEngine On
RewriteCond %{HTTP_HOST} ^dev
RewriteCond %{REQUEST_URI} !^/drupal/
RewriteRule ^(.*)$ drupal/$1 [L]
```

### Set the absolute URL on setting.php

To remove the trailing slash of `/drupal/` on your URLs, find a line that has the following code:  
`# $base_url = 'http://www.example.com'; // NO trailing slash!`

Remove the leading hash sign and fill in the absolute URL to your Drupal installation as below:  
`$base_url = 'http://dev.example.com'; // NO trailing slash!`

### Public file system path

Open your site on your browser. Once you have login to your drupal sites as the admin, check or set the correct path for *[File system settings](https://www.drupal.org/node/15368 "File system settings")* under the following admin menu:  
`Home » Administration » Configuration » Media » File System`

Verify or correct the value of *Public file system path* to:  
`sites/dev.example.com/files`, for your site `dev.example.com` via access URL:  
`http://dev.example.com/#overlay=%3Fq%3Dadmin%252Fconfig%252Fmedia%252Ffile-system `

## Multi Drupal Sites (By Subdomains)

Consider that you want to publish your site `dev.example.com` under `prod.example.com` and assign `dev.example.com` for the futher development.

Here you may simply install a new site, or copy the *default folder* and duplicate the database follow a guidance on how to *[copy site](#copy-site)* that become like so:

``` php
/public_html  <-- example.com, www.example.com, dev.example.com, prod.example.com
    .htaccess         <-- root's .htaccess
    index.html        <-- http://example.com, http://www.example.com
    /drupal               <-- drupal root folder
        .htaccess         <-- drupal's .htaccess
        index.php         <-- http://dev.example.com, http://prod.example.com
        /sites                <-- drupal's file system folder
            /default              <-- drupal's default subfolder 
                setting.php       <-- drupal's default setting (prod.example.com)
            /dev.example.com      <-- drupal's dev.example.com subfolder
                setting.php       <-- drupal's dev.example.com setting
```

By this configuration, instead of `/public_html/drupal/sites/default` (*default folder*) your site `http://dev.example.com` will now follow to the `setting.php` on folder `dev.example.com`.

### URL-Rewriting on root's .htaccess:

Rewrite the new subdomain of `prod` along with `dev` so its URL goes also to drupal but end up automatically to the `setting.php` on *default folder* since there is no folder by its name.

``` php
RewriteEngine On
RewriteCond %{HTTP_HOST} ^(dev|prod)
RewriteCond %{REQUEST_URI} !^/drupal/
RewriteRule ^(.*)$ drupal/$1 [L]
```

### URL-Rewriting on drupal's .htaccess

Find a line that has the following code:  
`RewriteRule ^ index.php [L]`

Change the code as below:  
`RewriteRule ^(.*)$ /index.php?q=$1 [L,QSA]`

### Set the absolute URL on setting.php

Then on each of `setting.php` remove the leading hash sign `$base_url `and fill in the absolute URL to your Drupal installation.

### Public file system path

Verify or correct the value of *Public file system path* for every subdomains as below:

- sites/dev.example.com/files, for your site dev.example.com via access URL:  
  `http://dev.example.com/#overlay=%3Fq%3Dadmin%252Fconfig%252Fmedia%252Ffile-system `
- sites/prod.example.com/files, for your site prod.example.com via access URL:  
  `http://prod.example.com/#overlay=%3Fq%3Dadmin%252Fconfig%252Fmedia%252Ffile-system`

## Multi Drupal Sites (By Subdomain + URL's Paths)

By *[sharing the same drupal code base](https://www.drupal.org/documentation/install/multi-site "Multi-site - Sharing the same code base")* as above (`/public_html/drupal`) , you may extend the *[Subdomain Mapping](#multisite-drupal-by-subdomains "Multi Drupal Sites (By Subdomains)")* where you can set another drupal sites under URL's Paths like so:

``` php
http://dev.example.com/site1,
http://dev.example.com/site2, etc..
```

### Symbolic Links

First you will need to access your server *[shell](https://en.wikipedia.org/wiki/Shell_(computing) "Shell (computing)")*. Then create the *[symbolic links](https://en.wikipedia.org/wiki/Symbolic_link "Symbolic link")* to the drupal root folder named `site1` and `site2` by following command:

``` php
$ cd /path/to/your/public_html/drupal
$ ln -s . site1
$ ln -s . site2
```

so the directory structure will be as below:

``` php
/public_html  <-- example.com, www.example.com, dev.example.com, prod.example.com
    .htaccess         <-- root's .htaccess
    index.html        <-- http://example.com, http://www.example.com
    /drupal               <-- drupal root folder
        .htaccess         <-- drupal's .htaccess
        index.php         <-- http://dev.example.com, http://prod.example.com
        /site1             <-- http://dev.example.com/site1
        /site2             <-- http://dev.example.com/site2
        /sites                <-- drupal's file system folder
            /default          <-- drupal's default subfolder 
                setting.php   <-- drupal's default setting (prod.example.com)
            /dev.example.com        <-- drupal's dev.example.com subfolder
                setting.php         <-- drupal's dev.example.com setting
            /dev.example.com.drupal.site1  <-- drupal's site1 subfolder
                setting.php                <-- drupal's site1 setting
            /dev.example.com.drupal.site2  <-- drupal's site2 subfolder
                setting.php                <-- drupal's site2 setting
```

### Coding on root's .htaccess & setting.php

The code for the root's .htaccess is the same as above, also the step fill in the absolute URL to `$base_url` in `setting.php`.

### Public file system path

Verify or correct the value of Public file system path for the new sites:

- `sites/dev.example.com.drupal.site1/files`, for `site1` via access URL:  
  `http://dev.example.com/site1/#overlay=%3Fq%3Dadmin%252Fconfig%252Fmedia%252Ffile-system`
- `sites/dev.example.com.drupal.site2/files`, for `site2` via access URL:  
  `http://dev.example.com/site2/#overlay=%3Fq%3Dadmin%252Fconfig%252Fmedia%252Ffile-system`

## Multi Drupal Sites (By Drupal 8)

By [Drupal 8](https://www.drupal.org/8 "Drupal-8") the symbolic links are no more required, there even a flexibility to name the folders under `/public_html/drupal/sites` as long you put them on the file `sites.php` like:

``` php
$sites = array(
   'dev.example.com' => 'dev',
   'dev.example.com.site1' => 'dev.site1',
   'dev.example.com.site2' => 'dev.site2',
);
```

so the directory structure will be as below:

``` php
/public_html  <-- example.com, www.example.com, dev.example.com, prod.example.com
    .htaccess         <-- root's .htaccess
    index.html        <-- http://example.com, http://www.example.com
    /drupal               <-- drupal root folder
        .htaccess         <-- drupal's .htaccess
        index.php         <-- http://dev.example.com, http://prod.example.com
        /sites                <-- drupal's file system folder
            sites.php         <-- drupal's multisite setting
            /default          <-- drupal's default subfolder 
                setting.php   <-- drupal's default setting (prod.example.com)
            /dev                  <-- drupal's dev.example.com subfolder
                setting.php       <-- drupal's dev.example.com setting
            /dev.site1            <-- drupal's dev.example.com.site1 subfolder
                setting.php       <-- drupal's dev.example.com.site1 setting
            /dev.site2            <-- drupal's dev.example.com.site2 subfolder
                setting.php       <-- drupal's dev.example.com.site2 setting
```

## Optional Settings

### Clean URLs

If you like to use URLs like `dev.example.com/user` instead of `dev.example.com/?q=user`, you will need to enable *[Clean URLs](https://www.drupal.org/getting-started/clean-urls "Configure clean URLs")* for your site by accessing the following menu:  
`Home » Administration » Configuration » Search and metadata » Clean URLs`

Incase a trouble with Clean URLs, you may add the following at the end line of setting.php:  
`$GLOBALS['conf']['clean_url'] = 0;`

### SEO URLs

You may also set a *[SEO Friendly URLs](https://moz.com/learn/seo/url "SEO Best Practice")* using *[URL Aliases](https://www.drupal.org/node/120631 "URL aliases")* by accessing the following menu:  
`Home » Administration » Configuration » Search and metadata » URL aliases`

Just remember to avoid the same URL path like the ones listed below when you set your *[Multi-site by Subdomain + URL's Paths](#multisite-drupal-by-subdomains-and-url-path "Multi Drupal Site by Subdomain + URL's Paths")* otherwise it will mix up your Multisite setting.

``` php
http://dev.example.com/site1
http://dev.example.com/site2
```

### Copy Site

You may want to duplicate your site by a Multisite setup for testing or development purposes. Following are documentation you can follow:

- [Create a Test Site](https://www.drupal.org/creating-drupal-test-sites)
- [Making a duplicate of a Drupal website](https://www.drupal.org/node/2063713)
- [Easy method to create duplicate of production site for testing](https://www.drupal.org/node/2365719)

You may also use my method as below. The command is made with an assumption that you have already a backup folder and an existing production site. Please use it with caution.

``` php
#COPY FOLDER (sites/dev » sites/prod)
$ cd /path-to-your/public_html/drupal/sites;
$ sudo rm -rf backup/dev;
$ sudo rsync -aczvAXHS --progress dev backup;
$ sudo mv prod backup/;
$ sudo mv backup/dev prod;
$ find prod -type d -exec sudo chmod 2775 {} \;
$ find prod -type f -exec sudo chmod 0664 {} \;
$ cd prod;
$ find settings.php -type f -exec sudo sed -i 's/db-dev/db-prod/g' {} \;
$ find settings.php -type f -exec sudo sed -i 's/sites\/dev\/files/sites\/prod\/files/g' {} \;

#COPY DATABASE (db-dev » db-prod)
$ sudo rm -rf backup/prod.sql;
$ mysqldump -uUSERNAME -pPASSWORD db-prod > backup/prod.sql;
$ sudo rm -rf backup/dev.sql;
$ mysqldump -uUSERNAME -pPASSWORD db-dev > backup/dev.sql;
$ find backup/dev.sql -type f -exec sed -i 's/db-dev/db-prod/g' {} \;
$ mysql -uADMINNAME -pPASSWORD;
$ mysql> SHOW DATABASES;
$ mysql> DROP DATABASE `db-prod`;
$ mysql> CREATE DATABASE `db-prod` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
$ mysql> GRANT ALL PRIVILEGES ON `db-prod`.* TO "USERNAME"@"localhost";
$ mysql> FLUSH PRIVILEGES;
$ mysql> exit;
$ mysql -uUSERNAME -pPASSWORD db-prod < backup/dev.sql;
$ rm -rf backup/dev.sql;
```

### Cache Clearing

Last but not least, to make sure everything is set properly, it is recommended to do a *[Cache Clearing](https://www.drupal.org/documentation/clearing-rebuilding-cache "Clearing or rebuilding Drupal's cache")* whenever you have put a new setting on your sites by accessing the following menu:  
`Home » Administration » Configuration » Development » Clear all Caches`

Using *[Drush](http://www.drush.org/)* you can even do it for all of your Multisite with *[one time cache command](http://drushcommands.com/drush-8x/cache/cache-rebuild/)*:

``` php
$ cd /path/to/your/public_html/drupal
$ drush @sites cache-rebuild
```

### Recommendation

You may setup *Drupal Multisite* grouped by the followings, hopefully you can find out on how it looks like.

- Sharing Drupal Core Base with Different Theme & Database
- Sharing Drupal Database with Different Layout Themes
- Sharing Drupal Theme with Different Database
