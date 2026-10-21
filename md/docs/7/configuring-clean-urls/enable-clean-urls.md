---
title: "Enable clean URLs"
source_url: "https://www.drupal.org/docs/7/configuring-clean-urls/enable-clean-urls"
page_type: page
last_updated: "Last updated on 26 October 2020"
published: "2005-01-09T13:27:15+00:00"
modified: "2020-10-26T15:56:46+00:00"
breadcrumb: ["Drupal 7", "Configuring clean URLs in Drupal 7"]
fetched: "2026-10-21T06:48:40Z"
raw: "raw/docs/7/configuring-clean-urls/enable-clean-urls.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Enable clean URLs

This page contains instructions relating to Drupal 7. For Drupal 8 see [troubleshooting-drupal-8/fix-drupal-8-clean-urls-problems](https://www.drupal.org/docs/8/troubleshooting-drupal-8/fix-drupal-8-clean-urls-problems)

On this page:

- [General Information](#general)
- [Clean-Urls Test - False Negatives](#falsenegatives)
- [Enabling Clean URLs in Drupal 7](#enabling)
- [Error Recovery](#recovery)
- [Server Configuration](#serverconfiguration)
  - [Server configuration for Clean URLs on a dedicated server, with httpd.conf](#dedicated)
  - [Server configuration for Clean URLs on a shared server, with .htaccess](#shared)
  - [Clean URLs on Windows servers with IIS](#iis)
- [Fixing problems](#problems)
  - [Check that .htaccess is even being used](#htaccess)
  - [RewriteBase setting](#rewritebase)
  - [\$base_url](#baseurl)
  - [Multi-site](#multisite)
  - [Location of index.php](#location)
- [Create Even Cleaner URLs with the Path Module](#pathmodule)
- [Redirect clean URLs to the human and/or canonical Path](#redirect-to-human-url)

## General Information

By default, Drupal uses and generates URLs for your site's pages that look like "<http://www.example.com/?q=node/83>". With so-called clean URLs this would be displayed without the "?q=" as "<http://www.example.com/node/83>".

The style of URLs using "?q=" can be hard to read, and may even prevent some search engines from indexing all the pages of your site. Research suggests this may not be as big of a problem for major search engines as it once was; however, it is worth noting the recommendation from [Google's webmaster guidelines](http://www.google.com/support/webmasters/bin/answer.py?answer=35769) stating:

> If you decide to use dynamic pages (i.e. the URL contains a "?" character), be aware that not every search engine spider crawls dynamic pages as well as static pages. It helps to keep the parameters short and the number of them few.

If you are unhappy with the default URLs in Drupal, you may be able to tell Drupal to use "clean URLs", eliminating the "?q=" in your site's URLs, and this page explains how to do it. The instructions below are largely applicable only for the most common server setup, which is an Apache web server running on some flavor of Unix/Linux, with the [mod_rewrite Apache module](http://httpd.apache.org/docs/2.4/mod/mod_rewrite.html) (this link is for Apache 2.4) configured and mod_rewrite enabled in **httpd.conf** configuration file. If you are running Drupal on a different type of server, check the links section below (just above the Comments section of this page) to see if there might be something that addresses your server configuration on a different page.

Before enabling clean URLs in the Drupal configuration screens (see below), you may need to prepare your server for clean URLs to work. There are two ways to prepare your server for clean URLs to work in Drupal. If you have complete control of your server, for example: You run your own server; are installing a development site on your personal computer; or you have a dedicated server hosting account, then you should enable clean URLs in the **httpd.conf** file for better performance and security. However, if you have a shared hosting account (at DreamHost, BlueHost, HostGator, GoDaddy, 1and1, et al.), you will not be able to modify the **httpd.conf** file and should use the Drupal **.htaccess** file instead.

## Clean-Urls Test - False Negatives

On some setups the Clean Urls test gives a **false negative** result. If you can visit Clean Url links like `http://example.com/user/login` and Drupal returns the user login page, then .htaccess and mod_rewrite are working. Visiting the Clean Urls admin page directly at `http://example.com/admin/config/search/clean-urls`, should give you a checkbox that lets you enable Clean Urls (note the lack of "?q=" in the URL). See <http://drupal.org/node/1178850>. **Note:** If Clean Urls like `http://example.com/user/login`. stops working (switching hosts) you can visit the same page by changing the URL to look like: `http://www.example.com/?q=user/login`.

## Enabling Clean URLs in Drupal 7

The standard Drupal installation contains a sample .htaccess file that supports Clean URLs, so make sure this file exists before enabling Clean URLs. Before copying this file make sure there is a *dot* , in the .htaccess file's name. It is very important to how Apache works.

In Drupal 7, the installer tests for compatibility with Clean URLs as a part of the installation process. If the environment is tested as compatible with Clean URLs, it will be enabled as part of the installation process and no further action is required to enable Clean URLs.

If you need to enable Clean URLs post installation, Drupal will run the clean URL test automatically when you navigate to the Clean URLs configuration page (*Administer \> Configuration \> Search and metadata \> Clean URLs*), show the results, and allow you to save configuration.

You can enable or disable it at a later time by following these steps:

1.  Navigate to the Clean URLs configuration page (*Administer \> Configuration \> Search and metadata \> Clean URLs*)
2.  Wait for the automated Clean URLs test to run.
3.  Check or uncheck the Enable clean URLs checkbox
4.  Click "Save configuration"

Even if Clean URLs are successfully enabled at install-time, if you have a dedicated server you may still want to follow the steps (below) to enable the more efficient httpd.conf rewrite method for clean URLs. If you choose to do that, you might want to turn off Clean URLs while you are working on the server.

### Error recovery

Enabling "Clean URLs" when your server is not properly configured (i.e. if the Clean URLs tests described above fail) can make it difficult to navigate back to administration pages to undo your mistake, because all the Drupal-generated menus and links will have URLs that do not work. If you find yourself in this situation, you can return to the administrative settings page by typing in the URL in the 'non-clean' form:`http://www.example.com/?q=admin/config/search/clean-urls`. Once there, you should be able to reset to not using Clean URLs.

There are additional instructions for recovering from malfunctioning Clean URLs the Handbook page [Unset clean URLs](/node/5590).

## Server configuration for Clean URLs

You can [read more about other web server requirements](/requirements/webserver)

### Server configuration for Clean URLs on a dedicated server, with httpd.conf

Enabling clean URLs on a dedicated server involves these steps:

1.  Enable mod_rewrite for Apache. You can talk to your web host or consult the [Apache documentation](http://httpd.apache.org/docs/2.4/mod/mod_rewrite.html) for mod_rewrite to get more information on how to do this. At a minimum, this will involve making sure that mod_rewrite is enabled for your installation of Apache.

    To test if mod_rewrite is available in Apache2, you can type the following at a command prompt, to list all installed Apache modules:

    ``` php
    apache2ctl -M 
    ```

    On some systems this command may be:

    ``` php
    apachectl -M 
    ```

    In the output, check to see if the `rewrite_module` is included in the list of modules.

    If the rewrite module is not in the list, it will have to be either compiled-in or made available as a loadable module. Generally speaking, you can tell Apache to load the module by including

    ``` php
    LoadModule rewrite_module modules/mod_rewrite.so AddModule mod_rewrite.c 
    ```

    in your Apache configuration file (see below for information on the configuration file). Be sure to uncomment AddModule mod_rewrite.c, if it is in your configuration file but has been commented out. The following may work to enable the module without editing any files:

    ``` php
    a2enmod rewrite 
    ```

    Note that these approaches may not work for all combinations of operating system and Apache server -- consult the Apache documentation that came with your Apache software for the correct syntax.

    Remember to [restart Apache](http://httpd.apache.org/docs/2.4/stopping.html) for the new configuration to take effect.

2.  The next step is to locate the appropriate Apache configuration file for your site. Depending on your server configuration, the appropriate Apache configuration file could be httpd.conf, a virtual-host-specific file (vhost.conf), a specific site file (e.g. "default"), or apache2.conf. They are usually located in `/etc/httpd/conf`, `/etc/apache2`, `/etc/apache2/apache2.conf`or a sub-directory;

    So, assuming you want to allow access to files on the /var/www/html directory, you should change the following lines from:

    ``` php
    <Directory "/var/www/html">
     AllowOverride None
    </Directory>
    ```

    to

    ``` php
    <Directory "/var/www/html">
     AllowOverride All
    </Directory>
    ```

    if not, try the command:

    ``` php
    find /etc -name httpd* or find /etc -name apache2* 
    ```

    to find the file if it is located elsewhere in your file system.

    > If you do not have write permissions to these files, and Clean URLs are not working out-of-the-box for you, you may have to ask your systems administrator or hosting provider for help. You may still be able to *read* these configuration files to [troubleshoot](http://drupal.org/node/54832) a little however.

3.  The next step is to copy or include the Drupal-specific settings directly into your configuration file. There are instructions here for [how to include the Drupal directives](http://drupal.org/node/43788) in your configuration file. Consult the [.htaccess file in Drupal](http://drupalcode.org/project/drupal.git/blob_plain/HEAD:/.htaccess) for examples of rules, such as the following for Drupal 7  

    ``` php
    RewriteEngine on
    RewriteBase /
    RewriteCond %{REQUEST_FILENAME} !-f
    RewriteCond %{REQUEST_FILENAME} !-d
    RewriteCond %{REQUEST_URI} !=/favicon.ico
    RewriteRule ^ index.php [L] 
    ```

    Or this example on a Debian 8 + Apache2 + ISPConfig, using wildcard to match all sites installed:

    ``` php
    <Directory /var/www/clients/*/*/web/>
      RewriteEngine on
      RewriteBase /
      RewriteCond %{REQUEST_FILENAME} !-f
      RewriteCond %{REQUEST_FILENAME} !-d
      RewriteRule ^(.*)$ index.php?q=$1 [L,QSA]
    </Directory> 
    ```

Note: If you do not want to put the rewrite rules in your Apache configuration file, you can still simply use the Drupal .htaccess file (as you would if you were on shared hosting). You will need to have the Allow Override directive set in your Apache configuration file (this will allow local .htaccess overrides on your site):

``` php
AllowOverride All
AccessFileName .htaccess 
```

Read [Behind the scenes with Apache's .htaccess](http://brainstormsandraves.com/archives/2005/10/09/htaccess/) for a thorough review of .htaccess. You may also find it helpful to view [samples of Apache 2 AllowOverride directives](http://httpd.apache.org/docs/2.4/mod/core.html#allowoverride).

**Note Regarding MultiViews:** Apache supports a feature called "MultiViews" (more generally: "Content Negotiation"), which allows navigation to your pages without the need for file extensions. For instance, if you had a file called "evaluation.txt", a MultiViews-enabled site could access this file with the URL "example.com/evaluation". While MultiViews can be a handy feature when used knowingly, it can cause problems when Drupal's Clean URLs are enabled. Unless you know what you're doing, you should not use MultiViews if you plan to use the Clean URLs feature of Drupal. However, MultiViews is not enabled in a default Apache installation, so it is likely that this note will not apply. [Consult the Apache documentation for further information about MultiViews](http://httpd.apache.org/docs/mod/core.html#options).

### Server configuration for Clean URLs on a shared server, with .htaccess

The standard Drupal installation contains a sample .htaccess file which should be sufficient to get Clean URLs running. It is easy to miss copying this file, because of the leading "dot". So before trying to enable Clean URLs, make sure this file exists in your Drupal installation.

To check for this in terminal, use `ls -a` to make sure the "dot" files are also listed.

If you have this file installed, but Clean URLs still do not work, you can try some of the troubleshooting suggestions below. If you still cannot get Clean URLs to work, contact your hosting provider.

## Clean URLs on Windows servers with IIS

Starting from Drupal 7, the package includes a basic web.config file for use with IIS.  
See [this article](http://drupal.org/node/3854) for more information and setup instructions.

## Fixing problems

### Check if .htaccess is being used

Apache needs to be explicitly told to respect the instructions in your sites .htaccess file. This is off by default, though most hosts will have turned it on. That is what the `AllowOverride All` directive above does - it makes .htaccess start working.

To check if your host is reading the .htaccess file, you can (temporarily) add some garbage string to the file in an attempt to break it. Your site should immediately start returning a "500 Server Error" when you load a page from that directory due to this misconfiguration. (Remove the garbage string immediately.)

If you do this, and your site *does not* break - then .htaccess is being ignored and you will not be able to use clean URLs until you get support from your hosts, or enable it in httpd.conf as described above. Some hosts allow you to enable this option through their site management control panel, so look there first.

### RewriteBase setting

The main configuration option which may need to be changed for your site is the `RewriteBase`. This can be specified in the Drupal .htaccess file or in the httpd.conf file, depending on where you are putting the Drupal rewrite directives (see above). By default, the RewriteBase setting is commented out of the Drupal .htaccess file, and that works well for many configurations.

If you are having trouble getting Clean URLs to work, you may need to change this setting. For example, if your Apache DocumentRoot is `/var/www/` (i.e., /var/www/index.html is what is displayed when you point your browser at `http://www.example.com/`) and your Drupal installation is installed in the subdirectory `/var/www/mysite/`, then the RewriteBase could be set to

``` php
RewriteBase /mysite 
```

and that might help. In some configurations, setting

``` php
RewriteBase / 
```

will allow clean URLs to work.

### \$base_url

You may need to manually set the \$base_url variable in the settings.php file if not already set. It's currently known that servers running FastCGI can run into problems if the \$base_url variable is left commented out (see <http://bugs.php.net/bug.php?id=19656>).

### Multi-site

`RewriteBase` works when your Drupal installation serves only one site, or when all the sites it serves are in the same subdirectory of their domains. For example,

``` php
RewriteBase / 
```

will work for the following sites:

<http://www.example.com/>  
<http://www.example2.com/>  
<http://www.example3.com/>

``` php
RewriteBase /mysite 
```

will work for the following sites:

<http://www.example.com/mysite>  
<http://www.example2.com/mysite>  
<http://www.example3.com/mysite>

However, if your sites are in different subdirectories, `RewriteBase` will not work. You will need to create a special rule for each subdirectory. For example, your Drupal installation may serve the following sites:

<http://www.example.com/>  
<http://www.example.com/mysite>

In order to enable clean URLs for both sites, you will need to add

``` php
RewriteCond %{REQUEST_FILENAME} !-f RewriteCond %{REQUEST_FILENAME} !-d RewriteCond %{REQUEST_URI} ^/mysite/ RewriteRule ^ /mysite/index.php [L] 
```

before the existing rewrite rules.

### Location of index.php

For some server configurations, another change to the Drupal .htaccess file may be necessary. Find a line that looks like this, near the end of your Drupal .htaccess file:

``` php
RewriteRule ^ index.php [L] 
```

You may need to replace `index.php` with the URL path to your Drupal installation's index.php file (only the part after the base URL). For instance, if your site's home page URL is `http://example.com/subdir/`, you might need to use `/subdir/index.php` instead of `index.php`. If your site's home page URL is `http://example.com/`, you might need to use `/index.php` instead of `index.php`. This is necessary on some, but not all server configurations.

## Create Even Cleaner URLs with the Path Module

Using *Clean URLs* will cause Drupal to generate URLs in the form "<http://www.example.com/node/83>." In order to change the 'node/##' portion of the URL to something more like 'news/june-1st-news' a site will need the [Path module](/handbook/modules/path) enabled. See the [Path module handbook page](/handbook/modules/path) for more information on using the path module.

## Redirect clean URLs to the human and/or canonical Path

After you install the Modules Path and Path auto you have for Google two sites "<http://www.example.com/node/123>" and the same at "<http://www.example.com/node/about-us>". For a better SEO and more human readable URLs just install the [Redirect Module](https://www.drupal.org/project/redirect). By default redirect the Redirect Module youer clean URL and by using the [Metatag Module](https://www.drupal.org/project/metatag) the canonical URL to the human URL. This is tested with Drupal 8.3.5 with Commerce 2.x

## Note for Drupal 7

Sometimes, weirdly even after enabling and configuring all the required server configurations on your server, it keeps giving you the "Clean URL test failed" message and the checkbox to enable it, is not shown.

After carefully checking for each of the configuration mentioned in the above doc, if the same error message still persists, try removing the ?q= from the url  
\[your-site-url\]/?q=admin/config/search/clean-urls  
and make it as  
\[your-site-url\]/admin/config/search/clean-urls and hit enter. If all your server configurations were correct, you will be seeing the checkbox to enable Clean URLs again.

### one more condition of failure

I followed [Migrating a site](https://www.drupal.org/docs/7/backing-up-and-migrating-a-site/migrating-a-site) to move a D7 site to another hosting account with the same provider. The advice in the tutorial is to turn off Clean URLs and to put the site into maintenance mode = off-line. I did and moved the site.

I then tried to turn on Clean URLs without success. The test failed time and again. With some reading I came here, but could not resolve the issue. I tested all sort of things and finally found I had to go online first and then turn on clean URLs.

#### **Drupal WARNING : Enable clean URLs(In ubuntu)**

This warning arises when you installing drupal on localhost, Run the below command in the terminal and edit file called 000-default.conf

`sudo nano /etc/apache2/sites-available/000-default.conf`

Add the following code in 000-default.conf and save

`<Directory '/var/www/html'>`

`AllowOverride All`

`</Directory>`
