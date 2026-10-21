---
title: "Tuning php.ini for Drupal"
source_url: "https://www.drupal.org/docs/7/managing-site-performance/tuning-phpini-for-drupal"
page_type: page
last_updated: "Last updated on 16 August 2016"
published: "2003-08-24T20:29:57+00:00"
modified: "2016-08-16T20:18:55+00:00"
breadcrumb: ["Drupal 7", "Managing Drupal 7 site performance and scalability"]
fetched: "2026-10-21T07:01:31Z"
raw: "raw/docs/7/managing-site-performance/tuning-phpini-for-drupal.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Tuning php.ini for Drupal

- Finding out current PHP memory limit and php.ini location
- Edit PHP’s realpath-cache-size, and realpath-cache-ttl for Drupal

## Finding out current PHP memory limit and php.ini location

To find out the current value of PHP memory limit, navigate to status report (*Reports \> Status report* or <http://example.com/admin/reports/status>) and scroll down (items are listed alphabetically) to PHP:

![Status report](/files/status_report_0.png)

Two lines above that, you can see PHP version info; '*more information*' link takes you to phpinfo() page, where you can find out the location of php.ini file:

![phpinfo()](/files/phpinfo_1.png)  
(example from a Linux (Ubuntu) system)

To increase PHP memory limit [follow instructions](https://www.drupal.org/docs/7/managing-site-performance/increase-php-memory-limit).

## Edit PHP’s realpath-cache-size, and realpath-cache-ttl for Drupal

Editing the following php.ini directives can noticeably decrease Drupal's initial page generation times.

[**realpath_cache_size**](http://us3.php.net/manual/en/ini.core.php#ini.realpath-cache-size) - Determines the size of the realpath cache to be used by PHP. This value should be increased on systems where PHP opens many files (such as Drupal), to reflect the quantity of the file operations performed. The default value of this declaration is 16k, and should be changed to a value that represents the actual amount of memory used for realpath cache.

In order to find the actual amount of memory that is used by realpath cache, you’ll need to increase the default amount that is being used currently to a larger number than 16k (try 256k) and then use a script to print the actual amount to the screen. I’ve found it helpful to create a PHP block that prints out the actual value and set it to only be visible to my particular role. Then I can check memory intensive areas as well as regular pages. Once I’m done, I’ll disable the block as it’s not needed anymore.

Set realpath cache to 256k in php.ini:

`realpath_cache_size = 256k`

Create a php block or otherwise inject the following php into your site so that you can view it on the screen:

``` php
 
  print_r(realpath_cache_size());  
```

The majority of sites I've checked using this method are using less than 64k. Your values will likely be different.

[**realpath_cache_ttl**](http://us3.php.net/manual/en/ini.core.php#ini.realpath-cache-ttl) - Duration of time (in seconds) for which to cache realpath information for a given file or directory. For systems with rarely changing files (such as Drupal), consider increasing the value. Raise this to 300 or higher.

The following are settings used in a Drupal site for a member’s organization that serves approximately 1500 users and more importantly the site has roughly 30 contributed modules + CiviCRM on the backend which results in quite a number of files requested.

``` php
realpath_cache_size = 64k
realpath_cache_ttl = 3600
```
