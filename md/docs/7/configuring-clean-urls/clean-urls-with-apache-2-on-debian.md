---
title: "Clean URLs with Apache 2 on Debian"
source_url: "https://www.drupal.org/docs/7/configuring-clean-urls/clean-urls-with-apache-2-on-debian"
page_type: page
last_updated: "Last updated on 8 August 2016"
published: "2006-01-08T01:52:59+00:00"
modified: "2016-08-08T13:10:26+00:00"
breadcrumb: ["Drupal 7", "Configuring clean URLs in Drupal 7"]
fetched: "2026-10-21T06:49:38Z"
raw: "raw/docs/7/configuring-clean-urls/clean-urls-with-apache-2-on-debian.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Clean URLs with Apache 2 on Debian

### Note: This article needs to be updated for Debian "Etch" and "Lenny" releases. (as of March 2009)

If you're running Apache 2 on Debian stable, in order to install the rewrite module you simply need to:

`# a2enmod rewrite`

then restart the webserver:

`# /etc/init.d/apache2 restart`

then edit either /etc/apache2/sites-enabled/drupal or to your .htaccess and ensure it looks something like this:

``` php
#
# Apache/PHP/site settings:
#

# Protect files and directories from prying eyes:
<Files ~ "(\.(conf|inc|module|pl|sh|sql|theme|engine|xtmpl)|Entries|Repositories|Root|scripts|updates)$">
  order deny,allow
  deny from all
</Files>

# Set some options
Options -Indexes
Options +FollowSymLinks

# Customized server error messages:
ErrorDocument 404 /index.php

# Set the default handler to index.php:
DirectoryIndex index.php

# Overload PHP variables:
<IfModule sapi_apache2.c>
   # If you are using Apache 2, you have to use <IfModule sapi_apache2.c>
   # instead of <IfModule mod_php4.c>.
   php_value register_globals        0
   php_value track_vars              1
   php_value short_open_tag          1
   php_value magic_quotes_gpc        0
   php_value magic_quotes_runtime    0
   php_value magic_quotes_sybase     0
   php_value arg_separator.output    "&amp;"
   php_value session.cache_expire    200000
   php_value session.gc_maxlifetime  200000
   php_value session.cookie_lifetime 2000000
   php_value session.auto_start      0
   php_value session.save_handler    user
   php_value session.cache_limiter   none
   php_value allow_call_time_pass_reference  On
</IfModule>

# Various rewrite rules
<IfModule mod_rewrite.c>
  RewriteEngine on
  Options All

  # Modify the RewriteBase if you are using Drupal in a subdirectory and the
  # rewrite rules are not working properly:
  RewriteBase /drupal

  # Rewrite old-style URLS of the form 'node.php?id=x':
  RewriteCond %{REQUEST_FILENAME} !-f
  RewriteCond %{REQUEST_FILENAME} !-d
  RewriteCond %{QUERY_STRING} ^id=([^&]+)$
  RewriteRule node.php index.php?q=node/view/%1 [L]

  # Rewrite old-style URLs of the form 'module.php?mod=x':
  RewriteCond %{REQUEST_FILENAME} !-f
  RewriteCond %{REQUEST_FILENAME} !-d
  RewriteCond %{QUERY_STRING} ^mod=([^&]+)$
  RewriteRule module.php index.php?q=%1 [L]

  # Rewrite URLs of the form 'index.php?q=x':
  RewriteCond %{REQUEST_FILENAME} !-f
  RewriteCond %{REQUEST_FILENAME} !-d
  RewriteRule ^(.*)$ index.php?q=$1 [L,QSA]
</IfModule>

# $Id: .htaccess,v 1.58 2004/10/09 20:41:49 dries Exp $
```

This is because the debian package installs the drupal "sites-enabled" virtual host, result being that drupal is accessed from <http://example.com/drupal>, hence the need to uncomment RewriteBase. Change it to the base that corresponds to your system.

ref: <http://www.debian-administration.org/articles/136>  
<http://drupal.org/node/14322>

--  
Sean K. O'Brien  
CTO  
Colley Graphics, LLC  
[http://www.colleygraphics.com](http://www.colleygraphics.com/)
