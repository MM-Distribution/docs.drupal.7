---
title: "Clean URLs with Lighttpd"
source_url: "https://www.drupal.org/docs/7/configuring-clean-urls/clean-urls-with-lighttpd"
page_type: page
last_updated: "Last updated on 1 April 2018"
published: "2006-01-08T01:36:48+00:00"
modified: "2018-04-01T22:11:14+00:00"
breadcrumb: ["Drupal 7", "Configuring clean URLs in Drupal 7"]
fetched: "2026-10-21T06:51:12Z"
raw: "raw/docs/7/configuring-clean-urls/clean-urls-with-lighttpd.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Clean URLs with Lighttpd

This document explains how to configure clean URLs for [Lighttpd](http://www.lighttpd.net/). There are two ways to do so:

### Using url rewrites

First you can use the following configuration for Lighty's mod_rewrite module:

``` php
url.rewrite-final = (
  "^/system/test/(.*)$" => "/index.php?q=system/test/$1",
  "^/([^.?]*)\?(.*)$" => "/index.php?q=$1&$2",
  "^/([^.?]*)$" => "/index.php?q=$1",
   "^/rss.xml" => "/index.php?q=rss.xml"
)
```

The first line ensures that Drupal's clean URL check (when saving Settings) succeeds (Drupal makes an HTTP request for a path of the form */system/test/yLgnwqqUu5cWnvPi4Hrz.png*). It's a special case that must be handled separately (read on for the reason).

The two following lines let Drupal handle any URL that **doesn't contain a dot**. This is significant because we can assume, fairly confidently, that addresses like */node/add* are Drupal URLs, but addresses such as */themes/bluemarine/style.css* are physical files. So the above configuration will work for all cases where this assumption holds true; if there are exceptions to the rule, they can be manually added to the rewrite configuration.

The last line handles the important exception of rss.xml, a Drupal URL that contains a dot.

See also the related discussion at <http://drupal.org/node/20766>

### Using mod magnet

Second you can use lighty's mod magnet module together with a simple lua scripts. Have a look at the tutorials  
<https://realize.be/blog/drupal-lighttpd-clean-urls-made-easy> or  
<http://more.zites.net/lighttpd_and_drupal_clean_urls_flexible>

This way has the advantage that there are no problems with dots.
