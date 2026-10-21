---
title: "Web server"
source_url: "https://www.drupal.org/docs/7/system-requirements/web-server"
page_type: page
last_updated: "Last updated on 26 April 2017"
published: "2012-09-13T00:36:16+00:00"
modified: "2017-04-26T07:52:06+00:00"
breadcrumb: ["Drupal 7", "Drupal 7 system requirements"]
fetched: "2026-10-21T05:52:08Z"
raw: "raw/docs/7/system-requirements/web-server.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Web server

#### Contents

- [Apache](#apache)
- [Nginx](#nginx)
- [Hiawatha](#hiawatha)
- [Microsoft IIS](#microsoft-iis)
- [PHP Built-in Web Server (Development Only)](#php-built-in-web-server)

Drupal works on any [web server](http://en.wikipedia.org/wiki/Webserver) with PHP support.

***Security note*:** Some security features are only provided for Apache and (to a lesser extent) IIS through the use of .htaccess and web.config files. You are responsible for recreating these features when not using Apache.

### Apache

[Apache](http://httpd.apache.org/) is the most commonly used web server for Drupal. Drupal will work on Apache 2.x hosted on UNIX/Linux, OS X, or Windows.

The majority of Drupal development and deployment is done on Apache, so there are more community experiences and testings performed on Apache than on other web servers. Drupal 7 and 6 will likely work on Apache 1.3.

You can use the Apache 'mod_rewrite' extension to [allow for clean URLs](/getting-started/clean-urls). Note that with Drupal 8, clean urls are enabled by default and can't be disabled, so mod_rewrite needs to be installed and enabled for Drupal 8 to work.

The Apache Virtualhost configuration must contain the directive `AllowOverride All` to allow Drupal's .htaccess file to be used.

If the Apache server has `Options +MultiViews` enabled by default, then the Apache Virtualhost configuration should also contain `Options -MultiViews` (or have -MultiViews added to the existing Options directive).

SymLinks: Drupal versions prior to 8.0 set +FollowSymLinks option in the .htaccess file. This prevents Drupal running on shared hosts which require +SymLinksIfOwnerMatch instead for security reasons. Drupal 8.0 does not set either option, but this causes installation on at least OpenSuse distributions to fail. The onscreen error messages are unhelpful, but the error logs identify the problem correctly in both cases. If you edit the .htaccess file remember that you have to re-edit after updates which overwrite the file!

### Nginx

[Nginx](http://nginx.org/) is a commonly used web server that focuses on high concurrency, performance and low memory usage.

Drupal will work on Nginx legacy versions (0.7.x, 0.8.x, 1.0.x, 1.2.x), stable 1.8.x versions, and mainline 1.9.x versions hosted on UNIX/Linux, OS X, or Windows. Nginx is a popular alternative to Apache, so there are also significant community experiences and testings performed on Nginx.

For information on enabling clean URLs, see [Clean URLs with NGINX](/node/976392). Note that with Drupal 8, clean urls are enabled by default and can't be disabled, so ngx_http_rewrite_module needs to be installed and enabled for Drupal 8 to work.

### Hiawatha

[Hiawatha](https://www.hiawatha-webserver.org/) is a web server with a strong focus on security. It also aims at being easy to use and being lightweight. Research performed by independent researchers proves that Hiawatha offers a performance comparable to other web servers under [normal conditions](http://www.saltwaterc.ro/wp-download/documents/PHP_web_serving_study.pdf), but much better performances [while under attack](https://www.hiawatha-webserver.org/weblog/64).

Hiawatha is fully compatible with Drupal. For information about the required URL rewriting rules to use Drupal with Hiawatha, read [Clean URLs with Hiawatha](/node/2275833).

### Microsoft IIS

[Microsoft IIS](https://www.iis.net/) is a web server and a set of feature extension modules for use with Microsoft Windows.

Drupal core will work with IIS 5, IIS 6, IIS 7, or IIS 8 if PHP is configured correctly.

To achieve clean URLs you may need to use a third party product. For IIS 7 or IIS 8 you can use the Microsoft URL Rewrite Module or a third party solution.

On IIS 7 Drupal requires [Windows 2008 Server SP2](http://technet.microsoft.com/en-us/windowsserver/dd262148.aspx) or later for fastCGI support.

### PHP Built-in Web Server (Development Only)

[PHP Built-in Web Server](http://php.net/manual/en/features.commandline.webserver.php "PHP Built-in Web Server") is included as a CLI SAPI tool in PHP versions 5.4.0 and above.

PHP web server was designed to aid in application development. It may also be useful for testing purposes or for application demonstrations that are run in controlled environments. It is not intended to be a full-featured web server therefore it should not be used as a production server for public use.

This web server can be started through a Drush command provided by the [PHP Server](/project/php_server "PHP Server") Drupal module.
