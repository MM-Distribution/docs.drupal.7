---
title: "Configuring a basic multi-site development environment in Linux"
source_url: "https://www.drupal.org/docs/7/multisite/configuring-a-basic-multi-site-development-environment-in-linux"
page_type: page
last_updated: "Last updated on 28 April 2020"
published: "2010-06-10T15:27:13+00:00"
modified: "2020-04-28T20:47:21+00:00"
breadcrumb: ["Drupal 7", "Multisite Drupal 7"]
fetched: "2026-10-21T06:10:45Z"
raw: "raw/docs/7/multisite/configuring-a-basic-multi-site-development-environment-in-linux.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Configuring a basic multi-site development environment in Linux

This page describes the minimum required steps for configuring a multi-site development environment on a Linux machine. The steps go through how to set up two development sites with the names `testsite` and `testsite2`. By replacing these names with ones of your choice, you can set up your personalized multi-site testing environment in Linux. The sites will share the same Drupal installation, but will use different databases. These instructions assume that you have the necessary [system requirements](http://drupal.org/requirements) for Drupal and know how to use a Linux command prompt.

## Step 1: Download and uncompress Drupal

It is not recommended to install Drupal through your package manager, as the available Drupal package is usually outdated. You can download and uncompress Drupal by following the steps on the [Download and uncompress Drupal](http://drupal.org/documentation/install/download) page of the Installation guide, as this step does not differ from a normal installation.

## Step 2: Set up your hosts file

Add the following lines to `/etc/hosts`:

``` php
127.0.0.1    testsite.localhost
127.0.0.1    testsite2.localhost
```

## Step 3: Set up Virtual Hosts

Add the following code to `/etc/apache2/httpd.conf`:

``` php
<VirtualHost *:80>
   DocumentRoot /var/www/html
   ServerName localhost
</VirtualHost>
<VirtualHost *:80>
    DocumentRoot /var/www/drupal
    ServerName testsite.localhost
</VirtualHost>
<VirtualHost *:80>
    DocumentRoot /var/www/drupal
    ServerName testsite2.localhost
</VirtualHost>
```

The stanza (paragraph) about `/var/www/html` is there to preserve the possibility to put non-Drupal sites in that directory. If you want only Drupal sites to be served, you can ignore it. You should also change the directory `/var/www/drupal` to the location you uncompressed Drupal in step 1.  
After this, restart Apache:  
`sudo /etc/init.d/apache2 restart`

## Step 4: Set up your databases

Create two databases using the instructions found on the [Create the database](http://drupal.org/documentation/install/create-database) page of the Installation guide. Name one of them `testsite` and the other `testsite2`.

## Step 5: Set up your sites folders

1.  From the command prompt, navigate to `/var/www/drupal/sites/` or wherever you have your sites folder installed.
2.  Copy the default.settings.php to `testsite.localhost/settings.php` and `testsite2.localhost/settings.php`

The resulting directory structure should contain a folder for each domain name (like `testsite.localhost` or `yourdomain.com`) with a settings.php file in each folder.

For Drupal 8: Activate the multi-site feature by copying (and renaming) the file `sites/example.sites.php` to `sites/sites.php`. There is no need to edit the file unless you need site aliases.  
For Drupal7: There is no need for sites.php file unless you need [site aliasing feature](https://api.drupal.org/api/drupal/sites%21example.sites.php/7.x). The normal [site selection rules](https://api.drupal.org/api/drupal/sites%21default%21default.settings.php/7.x) applies. 

## Step 6: Configure your sites to use the appropriate databases

1.  In the `/var/www/drupal/sites/testsite.localhost/` directory, edit the `settings.php` file as follows (assuming you are using MySQL):  

    ``` php
    $databases = array (
      'default' =>
      array (
        'default' =>
        array (
          'database' => 'testsite', 
          'username' => 'testuser', 
          'password' => 'password', 
          'host' => 'localhost', 
          'port' => '', 
          'driver' => 'mysql', 
          'prefix' => '', 
        ), 
      ), 
    );
    ```

2.  Repeat for `/var/www/drupal/sites/testsite2.localhost/`, except replace `testsite` with `testsite2`.

## Step 7: Run the installation script for your sites

In a web browser, visit `http://testsite.localhost/install.php` and follow the instructions found on the [Run the installation script](http://drupal.org/documentation/install/run-script) page of the Installation guide. Repeat for `http://testsite2.localhost/install.php`.

## Step 8: Remove write permissions from your sites' settings.php files

You don't really need to do this, since this is only a development environment, so we're not really concerned about security. Nevertheless, it's a good habit to get into:  
From the command prompt, navigate to `/var/www/drupal/sites`and remove the write permissions for the `settings.php` files:  
`sudo chmod a-w testsite.localhost/settings.php`  
`sudo chmod a-w testsite2.localhost/settings.php`

## Step 9: You're done!

You can visit your sites at:  
`http://testsite.localhost/index.php`  
`http://testsite2.localhost/index.php`

## Other resources

[Local multi-site installation of Drupal 7 on Linux](http://drupal.org/node/1114158)
