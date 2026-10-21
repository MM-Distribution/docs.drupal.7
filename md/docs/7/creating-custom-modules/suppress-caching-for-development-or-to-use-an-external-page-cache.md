---
title: "Suppress caching (for development) or to use an external page cache"
source_url: "https://www.drupal.org/docs/7/creating-custom-modules/suppress-caching-for-development-or-to-use-an-external-page-cache"
page_type: page
last_updated: "Last updated on 28 May 2023"
published: "2010-05-12T20:46:06+00:00"
modified: "2023-05-28T13:29:15+00:00"
breadcrumb: ["Drupal 7", "Creating custom modules in Drupal 7"]
fetched: "2026-10-21T07:27:10Z"
raw: "raw/docs/7/creating-custom-modules/suppress-caching-for-development-or-to-use-an-external-page-cache.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Suppress caching (for development) or to use an external page cache

This instruction is for Drupal 7 [read about disabling caching in Drupal 8](https://www.drupal.org/node/2598914)

When developing for Drupal you might want to suppress all caching of data to make sure new hooks, theme functions, etc are recognized immediately.

This will have performance detriments, of course, so must not be used in production. To turn on this development mode, add the following to your Drupal 7 settings.php file:

``` php
if (!class_exists('DrupalFakeCache')) {
  $conf['cache_backends'][] = 'includes/cache-install.inc';
}
// Default to throwing away cache data
$conf['cache_default_class'] = 'DrupalFakeCache';

// Rely on the DB cache for form caching - otherwise forms fail.
$conf['cache_class_cache_form'] = 'DrupalDatabaseCache';
```

In <http://drupal.org/node/730046> support for external caches was further enhanced. To use an external page cache (e.g. Varnish) add the following to settings.php:

``` php
if (!class_exists('DrupalFakeCache')) {
  $conf['cache_backends'][] = 'includes/cache-install.inc';
}
// Rely on the external cache for page caching.
$conf['cache_class_cache_page'] = 'DrupalFakeCache';
```

Then navigate to the Performance page at ?q=admin/config/development/performance and enable the page cache and set a non-zero time for "Expiration of cached pages":

![](/files/Performance-drupal-7.png)
