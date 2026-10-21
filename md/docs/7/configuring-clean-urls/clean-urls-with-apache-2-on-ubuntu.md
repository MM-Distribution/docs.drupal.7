---
title: "Clean URLs with Apache 2 on Ubuntu"
source_url: "https://www.drupal.org/docs/7/configuring-clean-urls/clean-urls-with-apache-2-on-ubuntu"
page_type: page
last_updated: "Last updated on 23 January 2018"
published: "2007-04-07T13:24:36+00:00"
modified: "2018-01-23T23:28:29+00:00"
breadcrumb: ["Drupal 7", "Configuring clean URLs in Drupal 7"]
fetched: "2026-10-21T06:49:54Z"
raw: "raw/docs/7/configuring-clean-urls/clean-urls-with-apache-2-on-ubuntu.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Clean URLs with Apache 2 on Ubuntu

There are two methods for setting up Drupal with Apache on Ubuntu. The first (preferred) method edits the virtual host configuration, which is the default setup on Ubuntu (even for a single-site web server). The second edits the main apache2.conf, which is typical for an older setup.

## Step 1 - Method A: "Virtual Host" Setup

First, from the Linux command line, enable the rewrite module for apache with this command:

`sudo a2enmod rewrite`

You can check to see if this worked by running:

`sudo apache2ctl -M`

and seeing if rewrite_module is on the list.

Next, use an editor (such as `nano`) to edit the appropriate Apache configuration file for your Drupal site in the `/etc/apache2/sites-available/` directory. For a single site, the file is `/etc/apache2/sites-available/000-default.conf`; if you have multiple sites, the file names should reflect the names of the sites to which they refer. Thus, to edit the default site configuration, use `sudo nano /etc/apache2/sites-available/mysite-example.conf`.

Look for the `Directory` section referring to the folder where your Drupal site lives found in the `/etc/apache2/sites-available/000-default.conf` file, typically the line `<Directory /var/www>`, and also change the line: `AllowOverride None` to `AllowOverride All`. This directive permits an .htaccess file, such as Drupal's, to be used to override Apache's default settings, and is necessary to allow the URL rewriting to work. See <https://help.ubuntu.com/community/EnablingUseOfApacheHtaccessFiles> for more information.

Save this file and then reload Apache with `sudo service apache2 reload` or `sudo /etc/init.d/apache2 reload`.

### Subdomain Setup

Instead of creating multiple virtual host files, you can create one virtual host file that uses a wildcard in the ServerAlias. Both a simple multi-site Drupal setup and multiple Drupal versions can run this way if the different subdomains are defined for each site in settings.php.

Consider the following and modify your configuration file to fit your needs.

1.  <http://myproject.dr5.example/>
2.  <http://myproject.dr6.example/>
3.  <http://myproject2.dr6.example/>

Below is an excerpt of a virtual host configuration file that would support the *last two lines in the above example*. This excerpt is not intended to be a *complete* configuration file, but it is here to provide guidance for your development environment.

``` php
<VirtualHost *>
    DocumentRoot "/www/Dr6"
    ServerName example
    ServerAlias *.dr6.example

    <Directory "/www/Dr6">
        AllowOverride All
    </Directory>
```

Edit your config file to suit your development needs, save it; then make sure your site is enabled and finally reload Apache.

## Step 1 - Method B: apache2.conf

In Apache version 2, httpd.conf has been deprecated and the new file location is `/etc/apache2/apache2.conf`.

Thus, the following modification of httpd.conf is no longer necessary to enable the rewrite module (mod_rewrite):

``` php
LoadModule rewrite_module modules/mod_rewrite.so
AddModule mod_rewrite.c
```

Simply run the following from the terminal: `sudo a2enmod rewrite`.

To disable the module run: `sudo a2dismod rewrite`. Remember that this would cause Clean URLs to fail.

Once mod_rewrite is enabled, open apache2.conf in a text editor. The apache2.conf will probably be read-only, so you will need sudo privileges to edit it. Use a command such as: `sudo nano /etc/apache2/apache2.conf`.

Find where the sections are in your apache2.conf and add another one for your Drupal site similar to this:

``` php
<Directory /var/www/your_drupal_site>
    AllowOverride All
</Directory>
```

After you edit apache2.conf as listed above, you need to reload the server with `sudo /etc/init.d/apache2 reload`.

## Step 1 - Method C: Add Rewrite Rules Directly to Virtual Host or apache2.conf

If you do not wish to allow .htaccess overrides, you can add the rewrite rules directly to a virtual host file or apache2.conf. The following should work:

``` php
<Directory /var/www/your_drupal_site>
         RewriteEngine On
         RewriteBase /
         RewriteCond %{REQUEST_FILENAME} !-f
         RewriteCond %{REQUEST_FILENAME} !-d
         RewriteRule ^(.*)$ index.php?q=$1 [L,QSA]
      </Directory>
```

This can provide slightly faster server performance since Apache will not look in every directory for an .htaccess file.

Note that, for proper security, you will need to add in the rules from the Drupal files directory's .htaccess file as well.

## Debugging Rewrite Issues

If you are having problems with getting your rewrite to work you can set Apache to log rewrite errors. Depending on your version of Apache, rewrite logging configuration varies.  

### Rewrite Logging in Apache \< 2.4

In apache prior to version 2.4 you need to add this to the end of `/etc/apache2/apache2.conf`:

``` php
RewriteLog "/var/log/apache2/rewrite.log"
RewriteLogLevel 3
```

Level 0 does no logging. Level 9 logs everything. Choose the level necessary for resolving your issue.

### Rewrite Logging in Apache \>= 2.4

Per [release notes for 2.4](https://httpd.apache.org/docs/2.4/upgrading.html) "The RewriteLog and RewriteLogLevel directives have been removed" and will yield an error "Invalid command 'RewriteLog'".  Logging is now contolled for all modules with a single command "LogLevel" and parameters specific to the module in question (see a [brief tutorial here](https://ctors.net/2015/07/24/apache24_debug_rewrite)).  To enable the log level 3 for mod_rewrite you would put the following at the end of /etc/apache2/apache2.conf:

``` php
LogLevel alert rewrite:trace3
```

**Security Warning:** Make sure to either remove or comment the logging code out when finished, or else put the log file in a directory that can't be read by normal users (such as /var/log/apache2). If this is not done, it can result in a security breach. Keep in mind that enabling rewrite logging adds somewhat to server load, and can easily generate large amounts of output not needed on a production server.

## Step 2: Enable Clean URLs

Now go to `http://yoursite.com/?q=?q=admin/config/search/clean-urls`, and run the test for "Clean URLs" (In Drupal 4.6 - 5.x this is buried in the paragraph explaining what "clean urls" are).

Then, select the radio button to set clean URLs to "enabled" and submit the form. You should now be able to access your site using URLs without the query string in them.

**Note:** In Drupal 7.x, if you are still having issues with Clean URLs, and your site is in maintenance mode, turn off maintenance mode while enabling clean URLs.
