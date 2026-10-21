---
title: "Changing PHP memory limits"
source_url: "https://www.drupal.org/docs/7/managing-site-performance-and-scalability/changing-php-memory-limits"
page_type: page
last_updated: "Last updated on 25 May 2022"
published: "2016-08-16T20:16:55+00:00"
modified: "2022-05-25T09:42:37+00:00"
breadcrumb: ["Drupal 7", "Managing Drupal 7 site performance and scalability"]
fetched: "2026-10-21T06:59:28Z"
raw: "raw/docs/7/managing-site-performance-and-scalability/changing-php-memory-limits.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Changing PHP memory limits

*Note: Increasing 'Php-Memory limit' is different from increasing 'PHP-upload' size limit. You can learn to increase upload size [here](http://drupal.org/node/97193).*

The standard [PHP memory requirements for Drupal core](https://www.drupal.org/requirements/php#memory) are a bare minimum. Sites that run many contrib modules, or particularly memory-intensive ones, will need more. There are several techniques to increase the PHP memory limit and you only need to use one of them. The right one for you depends on your system configuration.

A typical appropriate memory limit for PHP running Drupal is 128MB per process; for sites with a lot of contributed modules or with high-memory pages, 256MB or even 512MB may be more appropriate.

It's often the case that the admin section of a site, or a particular page, uses much more memory than other pages. If that is the case, you can [conditionally increase memory limits](https://support-acquia.force.com/s/article/360004542293-Conditionally-increasing-memory-limits) based on the URL of the page.

### Relationship between memory limit and scalability

It's important to understand that increasing the amount of memory *each* PHP process can use decreases the number of *concurrent* processes that can run. Concurrent processes are key to the maximum number of page requests you can serve at any given time.

For example, let's assume a server with 2 GB of memory free for PHP after accounting for other processes running on it (the OS, Apache, and so on).

|                                        |       |       |       |
|----------------------------------------|-------|-------|-------|
| **PHP memory limit**                   | 128MB | 256MB | 512MB |
| **Max number of concurrent processes** | 16    | 8     | 4     |

*Memory limit/concurrency relationship with 2GB RAM*

## How to change memory limits

### php.ini

This is the recommended approach if you have access to the server's php.ini. This will not be possible in some shared hosting environments, though your host may be able to adjust it for you. Note that this change will affect all websites and PHP scripts on the server.

1.  Locate the php.ini file used by your web server. You can click the "more information" link on Drupal's status page's PHP section. which shows the phpinfo() page. Locate the *Configuration File (php.ini) Path* row on that page. During installation Drupal checks the PHP Memory Limit, and if it is less than 64M, an error message also provides the path to the php.ini file.

2.  Edit the memory_limit parameter in the php.ini file (usually in a section called Resource Limits). Make sure you use M to specify the number of megabytes (not `MB`).

    `memory_limit = 256M ; Maximum amount of memory a script may consume (256MB)`  
    If there is no section already for this, place the above line at the end of the file.

3.  Restart Apache.

### php.ini in the Drupal root folder

Add the following line to a php.ini file in your Drupal root folder:  
`memory_limit = 256M`  
This will only work if PHP is running as CGI/FastCGI.

### .user.ini in public_html folder (for PHP 5.3 and up)

PHP 5.3+ allows you to change the memory limit by placing a **.user.ini** file in the public_html folder.  
Simply create the above file and type the following line in it:  
`memory_limit = 256M`  
Some cPanel hosts only accept this method.

*The next two solutions are more restricted in scope and, in some cases, may be more appropriate choices than affecting all sites.*

### .htaccess

Edit the .htaccess file in the Drupal root directory. Look for the section:

``` php
# Override PHP settings. More in sites/default/settings.php # but the following cannot be changed at runtime. 
```

and immediately after this add the following line:  
`php_value memory_limit 256M`

This method will only work if PHP is running as an Apache module.

### settings.php

If Drupal is already installed, you can edit sites/default/settings.php. This method will affect only the site using this file.  
Locate the PHP settings section and add the following line at the end of that section:  
`ini_set('memory_limit', '256M');`

### Shared Hosting

In some shared hosting environments, access to the PHP memory limit setting is restricted. If you cannot make the change yourself, please ask your hosting provider to adjust it for you, or look for a new host that allows more flexibility.

For some hosts renaming php.ini to php5.ini may be necessary.

Some hosting services require the following line in .htaccess to enable a php.ini file.  
`suPHP_ConfigPath ~/public_html`

For some hosts (CrazyDomains) you may need to add the following lines to the php.ini file (if they are not there already):

``` php
extension=pdo.so extension=pdo_sqlite.so extension=sqlite.so extension=pdo_mysql.so 
```

### Modifying php.ini in local server environments

For MAMP see <http://drupal.org/node/66187> particularly the "Optional: Adjust PHP's memory limit for scripts" section (note the difference for MAMP Pro).

If you are using XAMPP/WAMP, there may be two PHP.ini files (one under the PHP directory and the other under Apache/bin). To change your memory limit, edit the file in the XAMPP/Apache/bin directory.

### Check your change has taken effect

In all cases, it pays to ensure that your change is actually working. Check Drupal's *status report* to verify that your memory actually is what you want it to be. If your change doesn't seem to be working, *double-check the location of php.ini*. Some systems have multiple copies of that file in different places. Only one is used and the others are red herrings.

### Tools

XHprof is a good solution to find high memory consumption. See this page for more instructions on how to install and use it: <http://groups.drupal.org/node/82889>
