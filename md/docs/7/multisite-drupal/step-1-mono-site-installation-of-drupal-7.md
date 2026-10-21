---
title: "Step 1: mono-site installation of Drupal 7"
source_url: "https://www.drupal.org/docs/7/multisite-drupal/step-1-mono-site-installation-of-drupal-7"
page_type: page
last_updated: "Last updated on 30 August 2016"
published: "2014-03-24T10:47:13+00:00"
modified: "2016-08-30T13:47:16+00:00"
breadcrumb: ["Drupal 7", "Multisite Drupal 7"]
fetched: "2026-10-21T06:14:06Z"
raw: "raw/docs/7/multisite-drupal/step-1-mono-site-installation-of-drupal-7.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Step 1: mono-site installation of Drupal 7

Firstly install Drupal 7 thanks to your distribution or by hand. (Ubuntu 11.04 doesn't include Drupal 7, but Mageia 3 and 4 do.) If you have to install Drupal by hand, follow the 6 steps of the [Installation guide](https://drupal.org/documentation/install). Don't insert any dot in the name of the directory you install Drupal in. We suggest /var/www/drupal7/ and we will suppose below that such is its name. The corresponding database name cannot contain contain spaces, slashes, nor dots. I'll suppose below it is "drupal7".  
Since you install locally, skip the "Set up a Domain and point it to the directory containing Drupal's files" part of the [Quick install for beginners](http://drupal.org/documentation/install/beginners). Instead, you'll setup a virtual host:

## Setting the default site hostname

### In Ubuntu 11

At starting, Apache reads Ubuntu's file /etc/apache2/apache2.conf that file which includes several directives, notably:

``` php
Include ports.conf
Include conf.d/
Include sites-enabled/
```

So all the files in conf.d/ and sites-enabled/ will be read as if they were parts of the main configuration file.

ports.confs says "NameVirtualHost \*:80".  
which means that for all IP (the star means "all") the virtual host will be redirected as indicated. "80" is the number of the port listened to by Apache.

- Create a file called /etc/apache2/sites-available/drupal7 saying:  

  ``` php
  <VirtualHost *:80>
     DocumentRoot /var/www/drupal7
     ServerName drupal7
  </VirtualHost>
  ```

  This means that "drupal7" will point to /var/www/drupal7/ .

- Create a symbolic link from the directory sites-enabled to this file (So if you later want to disable your Drupal sites you will not need to remove them, but just to remove the link.):  
  `sudo ln -s /etc/apache2/sites-available/drupal7 /etc/apache2/sites-enabled/drupal7`

- Create a file called /etc/apache2/conf.d/drupal7.conf saying:  

  ``` php
  Alias drupal7 127.0.0.1

  <Directory /var/www/drupal7>
      Options +FollowSymLinks
      AllowOverride All
      order allow,deny
      allow from all
  </Directory>
  ```

- In Ubuntu 11.04, in order to enable Apache's Rewrite module, necessary for Drupal's "Clean URLs" feature, launch Debian script `sudo a2enmod rewrite`, which will create the symbolic link /etc/apache2/mods-enabled/rewrite.load .

### In Mageia 3 and 4

- Navigate to folder /etc/httpd/conf/sites.d/ (In Magiea 3, it is /etc/httpd/conf/vhosts.d/.)

- Open 00_default_vhosts.conf file. Apache's main configuration file is /etc/httpd/conf/httpd.conf . At starting, Apache reads that file which includes several directives, notably:  

  ``` php
  # Include generic server configuration
  Include conf/conf.d/*.conf
  # Include sites configuration
  Include conf/sites.d/*.conf
  ```

  In Mageia 3, it is:

  ``` php
  Include conf/webapps.d/*.conf
  Include conf/vhosts.d/*.conf
  ```

  So that our file 00_default_vhosts.conf will be read as if it were part of the main configuration file.

- In Mageia 3, at the bottom of the existing list, comment out (adding the character "#" at the beginning of the lines) the examples.

- After the comment lines, enter:  

  ``` php
  NameVirtualHost *:80
  <VirtualHost *:80>
     DocumentRoot /var/www/html
     ServerName localhost
  </VirtualHost>
  <VirtualHost *:80>
     DocumentRoot /var/www/drupal7
     ServerName drupal7
  </VirtualHost>
  ```

  The 1<sup>st</sup> line means that for all IP (the star means "all") the virtual host will be redirected as indicated. "80" is the number of the port listened to by Apache. Then we say that "localhost" will point to /var/www/html/, which is not in the Drupal hierarchy, so that you be still able to have non-Drupal websites there. If all your websites are Drupal websites, don't write these lines. But you still need the 1st one. And the last virtual host is for the default Drupal 7 site.

## Setting the default site database

- Create an empty database with PhpMyAdmin: in your browser: <http://localhost/phpmyadmin%C2%A0>. . To create it, click on “localhost” on the top left, then on the “Databases” tab, name this database “drupal7”, as collation, choose one corresponding to your computer encoding (usually “utf8”) and language. If your language is not mentioned, “utf8_unicode_ci” is usually a good choice. Then click on “Create”. Alternatively, you can use MySQL Workbench to create your database.
- Be aware that some share hosting services require that all your database usernames begin by a fix part (for instance derived from your main site name) followed by an underscore. If you don't want to change your username when putting your Drupal site alive, check your hosting service rules now. Create a user called "company_drupal", where "company" stands for the prefix required by your hosting service provider. To add a new user, in PhpMyAdmin, click on “localhost” on the top left, then on the “Users” tab, then, click on the link "Add user" located below the list of users, and in the field “User name” (“Use text field:”), name it "company_drupal", then in the “Host” rolling list, choose “Local”: the corresponding field will automatically get filled as “localhost”. In the field “Password” (“Use text field:”), type your password (Don't forget it.), and retype it in the “Re-type:” field. Then click on the “Add user” button at the bottom of the sub-window. You will get the “You have added a new user!” message.
- Grant company_drupal@localhost the SELECT, INSERT, UPDATE, DELETE, CREATE, DROP, INDEX, ALTER, CREATE_TMP_TABLE and LOCK_TABLES privileges to this new schema. To do so, in PhpMyAdmin 's “Users” tab, click on the “Edit privileges” on your new user's line (“company_drupal”): a sub-window will open. Scroll it down up to “Database-specific privileges”. In the rolling list “Add privileges on the following database:”, choose your default database “drupal7”. There choose the above mentioned privileges and click on “Go”.

## Don't use the default site

We suggest you don't use the default website, so that you'll always have a virgin site to copy or to compare to your sites. So don't add content to it, don't enable modules or themes, don't configure it. The bulk loops below have to be performed as many times as you want to create sites (other than the default one). Check if the default Drupal web site and the non-Drupal websites, if any, work.
