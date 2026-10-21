---
title: "Clean URLs with Apache 2 for performance"
source_url: "https://www.drupal.org/docs/7/configuring-clean-urls/clean-urls-with-apache-2-for-performance"
page_type: page
last_updated: "Last updated on 22 November 2017"
published: "2006-01-08T02:15:18+00:00"
modified: "2017-11-22T17:06:41+00:00"
breadcrumb: ["Drupal 7", "Configuring clean URLs in Drupal 7"]
fetched: "2026-10-21T06:49:23Z"
raw: "raw/docs/7/configuring-clean-urls/clean-urls-with-apache-2-for-performance.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Clean URLs with Apache 2 for performance

**Note the following directions do not adequately cover everything that needs to be included in a site's Apache configuration file to make sure the site is secure. The files directory needs a SetHandler directive per** <http://drupal.org/files/sa-2006-006/advisory.txt>

Enabling .htaccess in Apache requires more work on the part of the server. A full explanation can be found here:  
<http://www.serverwatch.com/tutorials/article.php/3436911>  
Suffice it to say that it is in your interest to not use .htaccess files and even disable them if you are concerned about squeezing more performance out of apache.

I moved the rewrite rules (all of the sample .htaccess file really) to /etc/httpd/conf/drupal.conf. Then for each virtual host, one can add the line:

``` php
Include conf/drupal.conf
```

The rewrite rules change slightly:

``` php
  # Rewrite current-style URLs of the form 'index.php?q=x'.
  RewriteCond %{DOCUMENT_ROOT}%{REQUEST_FILENAME} !-f
  RewriteCond %{DOCUMENT_ROOT}%{REQUEST_FILENAME} !-d
  RewriteRule ^(.*)$ /index.php?q=$1 [L,QSA]
```

Note that I added %{DOCUMENT_ROOT} and a leading slash in front of index.php -- because I have index.php installed in my document root. If you install it in another directory, you will want to give the relative path to it from document root with the leading slash.

Important: If you forget the leading slash (more specifically, forget to give the relative path with leading slash), Apache will give you a "400 Bad Request" error.

This is better. But we still have a problem where every request will check for the existence of a file and a directory before we apply the rewrite rule. The OS may be able to cache some of that information, but it would still be better to avoid the two file-system checks in the first place.

There are some directories that we should not rewrite. And there are certain extensions that we should not rewrite. Using this information, we can update the rewrite rule to send everything to index.php that does not fall into this category. The first rule excludes the directories "files", "misc", and "uploads". The second rule excludes the extensions you see. Add more if you have other extensions in your directory that should not get passed to index.php.

``` php
  RewriteCond  %{REQUEST_FILENAME} !^/$
  RewriteCond  %{REQUEST_FILENAME} !^/(files|misc|uploads)(/.*)?
  RewriteCond  %{REQUEST_FILENAME} !\.(php|ico|png|jpg|gif|css|js|html?)(\W.*)?
  RewriteRule ^(.*)$ /index.php?q=$1 [L,QSA]
```

**Note:** This sort of directive will disable ImageCache and any other modules that depend on passing requests for files that are not found to index.php.

### Compliance with SA-2006-006

#### Multisite + files

Add this to your http.conf file; be sure to change the webroot path `/var/www/html/` so it matches your webroot path. Also be aware that if your running drupal in multiple sub directories then you need to add this in for each one. (/var/www/html/sitea, /var/www/html/siteb, /var/www/html/sitec, ...etc) or you can use the directives in the following section. This is compatible with multisite due to the `*` in `sites/*/files`.

``` php
<Directory /var/www/html/sites/*/files>
  SetHandler Drupal_Security_Do_Not_Remove_See_SA_2006_006
  Options None
  Options +FollowSymLinks
</Directory>
```

#### Multisite + Sub Directories + files + tmp

The below directives will handle files directories for each site and for any sub directory site. This example also shows how to secure site tmp directories wh any other site specific directory to safeguard. Again, replace `/var/www/html/` to match your webroot.

``` php
  # handles root (/var/www/html/sites) and sub dirs (/var/html/www/sub/sites)
  <Directory ~ "^/var/www/html/(.+/)*sites/.+/(files|tmp)/">
    SetHandler Drupal_Security_Do_Not_Remove_See_SA_2006_006
    Options None
    Options +FollowSymLinks
  </Directory>
```

See [Directory Directive](http://httpd.apache.org/docs/trunk/mod/core.html#directory) for the \* syntax and other tips.
