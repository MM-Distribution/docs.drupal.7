---
title: "Multi-site on Linux - Configuring multi-site for a local user (UserDir)"
source_url: "https://www.drupal.org/docs/7/multisite-drupal/multi-site-on-linux-configuring-multi-site-for-a-local-user-userdir"
page_type: page
last_updated: "Last updated on 30 August 2016"
published: "2014-06-05T18:09:05+00:00"
modified: "2016-08-30T13:47:16+00:00"
breadcrumb: ["Drupal 7", "Multisite Drupal 7"]
fetched: "2026-10-21T06:11:31Z"
raw: "raw/docs/7/multisite-drupal/multi-site-on-linux-configuring-multi-site-for-a-local-user-userdir.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Multi-site on Linux - Configuring multi-site for a local user (UserDir)

This guide will cover how to deploy multiple sites from within a single Drupal installation for a local user

## The Setup

- Ubuntu 14.04 64-bit
- Apache/2.4.7 with **UserDir module**
- PHP 5.5.9-1ubuntu4
- MySQL 5.5.37-0ubuntu0.14.04.1
- Drupal 7x

## The Sites Directory

- ~/public_html/foo
- ~/public_html/bar
- ~/public_html/foo/bar

## The Sites URLs

- <http://localhost/~%5Buser%5D/foo>
- <http://localhost/~%5Buser%5D/bar>
- <http://localhost/~%5Buser%5D/foo/bar>

## The Foo

- Create database "foo" (<https://drupal.org/documentation/install/create-database>).

- Download and extract Drupal.  

  ``` php
  wget -P ~/ http://drupal.org/files/projects/drupal-x.y.tar.gz
  tar -zxvf ~/drupal-x.y.tar.gz
  mv ~/drupal-x.y ~/public_html/foo
  ```

- Create the settings.php file.  

  ``` php
  cd ~/public_html/foo
  cp sites/default/default.settings.php sites/default/settings.php
  chmod a+w sites/default/settings.php
  chmod a+w sites/default
  ```

- Configure clean URLs.  
  `nano .htaccess`  
  replace `# RewriteBase /drupal` with `RewriteBase /~[user]/foo`

- Run the installation script, point your browser to <http://localhost/~%5Buser%5D/foo>.

- Write permissions after install.  

  ``` php
  chmod go-w sites/default/settings.php
  chmod go-w sites/default
  ```

## The Bar and the Foo/Bar

- Create database "bar" and "foo_bar" (<https://drupal.org/documentation/install/create-database>).

- Create the settings.php file.  

  ``` php
  cd ~/public_html/foo
  mkdir sites/bar
  mkdir sites/foo.bar
  cp sites/default/default.settings.php sites/bar/settings.php
  cp sites/default/default.settings.php sites/foo.bar/settings.php
  chmod -R a+w sites/bar
  chmod -R a+w sites/foo.bar
  ```

- Create the sites.php file.  

  ``` php
  cp sites/example.sites.php sites/sites.php
  nano sites/sites.php
  ```

  Add following lines at the end of file (without syntax).

  ``` php
  $sites = array(
    'localhost.~[user].bar' => 'bar',
    'localhost.~[user].foo.bar' => 'foo.bar',
  ); 
  ```

- Create symbolic link.  

  ``` php
  ln -s . ~/public_html/bar
  ln -s . ~/public_html/foo/bar
  ```

- Configure clean URLs.  
  `nano .htaccess`  
  Add

  ``` php
  RewriteCond %{REQUEST_FILENAME} !-f
  RewriteCond %{REQUEST_FILENAME} !-d
  RewriteCond %{REQUEST_URI} !=/favicon.ico
  RewriteCond %{REQUEST_URI} ^/~[user]/bar/
  RewriteRule ^ /~[user]/bar/index.php [L]
  ```

  and

  ``` php
  RewriteCond %{REQUEST_FILENAME} !-f
  RewriteCond %{REQUEST_FILENAME} !-d
  RewriteCond %{REQUEST_URI} !=/favicon.ico
  RewriteCond %{REQUEST_URI} ^/~[user]/foo/bar/
  RewriteRule ^ /~[user]/foo/bar/index.php [L]
  ```

  right before

  ``` php
  RewriteCond %{REQUEST_FILENAME} !-f
  RewriteCond %{REQUEST_FILENAME} !-d
  RewriteCond %{REQUEST_URI} !=/favicon.ico
  RewriteRule ^ index.php [L]
  ```

- Run the installation script, point your browser to <http://localhost/~%5Buser%5D/bar> and <http://localhost/~%5Buser%5D/foo/bar> in turns.

- Write permissions after install.  

  ``` php
  chmod go-w sites/bar/settings.php
  chmod go-w sites/foo.bar/settings.php
  chmod go-w sites/bar
  chmod go-w sites/foo.bar
  ```

***Notes: replace "\[user\]" with actual username.***
