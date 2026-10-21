---
title: "Clearing or rebuilding Drupal's cache"
source_url: "https://www.drupal.org/docs/7/administering-drupal-7-site/clearing-or-rebuilding-drupals-cache"
page_type: page
last_updated: "Last updated on 19 August 2022"
published: "2005-12-22T08:04:12+00:00"
modified: "2022-08-19T18:38:55+00:00"
breadcrumb: ["Drupal 7", "Administering Drupal 7 site"]
fetched: "2026-10-21T06:00:25Z"
raw: "raw/docs/7/administering-drupal-7-site/clearing-or-rebuilding-drupals-cache.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Clearing or rebuilding Drupal's cache

To create a page Drupal needs to make several database queries. This can slow down websites with a lot of traffic. To make websites faster Drupal stores web pages in a cache.

It is a good practice to clear or rebuild caches when moving a site from one host to another. Clearing the caches can also be useful when installing new modules or themes, and as a first step in troubleshooting. During development it is necessary to clear the cache very frequently.

Clearing caches is relatively harmless. Sites might slow down for a bit afterwards while the cache fills back up.

Note that there are sometimes caches other than the Drupal cache that can affect website performance. For example, some hosting services use a cache called "Varnish" to improve performance. Also, individual web browsers maintain their own caches on a user's computer or device.

The procedure below is for clearing Drupal's internal cache. To clear a non-Drupal cache, please refer to the procedures for those caches.

[About clearing the theme cache](/node/337176).

## Clearing the cache

1.  The easiest way to clear the Drupal cache is to go to **Administration \> Configuration \> Development \> Performance** (<http://example.com/admin/config/development/performance>)
2.  Click the button "Clear all caches"

## Other ways of clearing the cache

### Drush

The most convenient way to rebuild Drupal's cache is by using [Drush](/node/477684).

Drupal 9:

``` php
drush cache-rebuild
```

Drupal 7 and earlier:  
`drush cache-clear all` or alternately,

``` php
drush cc all
```

### Run update.php

Running update.php (<http://example.com/update.php>) is another way of clearing the cache. If you cannot login or have no user 1 rights you will need to set \$update_free_access = TRUE; first in /sites/default/settings.php. Do not forget to set this back to FALSE afterwards.

### A PHP snippet

Use the following code to clear specific cache type from within a module. If you want to clear all the caches similar to the functionality of the button on the "Performance" page, call this snippet for all tables beginning with the word "cache".

``` php
<?php
db_query("DELETE FROM {cache};");
?>
```

### In the database

Important: Do not work directly on databases of sites that are "live" unless you know exactly what you are doing. For production sites, either use the "clear all caches" button or drush, as described above. For the following instructions on working directly in the database, thoroughly test your intended changes on a copy of your production site.

To remove the contents of cache\_ tables, use phpMyAdmin or another tool to access the desired tables and TRUNCATE (empty, **not** remove) them. All tables that start with cache\_ can safely be truncated EXCEPT the cache_form table.

Note the exception: don't TRUNCATE the cache_form table on a site with active users. Doing so may cause in-progress form submissions to break. The cache_form table is also not cleared by [the core cache clearing methods](https://api.drupal.org/api/drupal/includes!common.inc/function/drupal_flush_all_caches/7.x); see `function drupal_flush_all_caches()`. In order to manage the size of cache_form on high traffic sites, please see the [Safe cache_form Clear](https://www.drupal.org/project/safe_cache_form_clear) contrib module.

In phpMyAdmin, if you would like to clear cache\_\* tables, select the desired tables and choose "Truncate" from the "with selected" drop-down menu at the bottom of the page. For the command line, see here:  
<http://dev.mysql.com/doc/refman/5.1/en/truncate-table.html>

#### Drupal 9 - MySQL Snippet :

``` php
TRUNCATE cache_config;
TRUNCATE cache_container;
TRUNCATE cache_data;
TRUNCATE cache_default;
TRUNCATE cache_discovery;
TRUNCATE cache_dynamic_page_cache;
TRUNCATE cache_entity;
TRUNCATE cache_menu;
TRUNCATE cache_render;
TRUNCATE cache_toolbar;
```

### Drupal 7 - MySQL Snippet :

``` php
TRUNCATE TABLE cache;
TRUNCATE TABLE cache_block;
TRUNCATE TABLE cache_bootstrap;
TRUNCATE TABLE cache_field;
TRUNCATE TABLE cache_filter;
TRUNCATE TABLE cache_form;
TRUNCATE TABLE cache_image;
TRUNCATE TABLE cache_menu;
TRUNCATE TABLE cache_page;
TRUNCATE TABLE cache_path;
TRUNCATE TABLE cache_token;
TRUNCATE TABLE cache_update;
```

### Devel module

The [module Devel](/project/devel) makes it easy to clear Drupal's cache. Just install this module and enable the "Developer/Development Block" for easy access to cache clearing. Note that "Devel" is a module designed to make development easier and should generally not be enabled on a production site.

### Admin_menu module

The [Administration menu (admin_menu) module](/project/admin_menu) has several cache clearing options for menu, page requisites, theme registry, cache tables and administration menu. It also has cron and update.php links too.

### A PHP file to clear caches and rebuild the routing tables

Be careful not to leave this on the server as anyone can clear caches if they know the file name. Create a file named clear.php with the code below. Place the file in the Drupal base directory and run it by browsing to `http://example.com/clear.php`.

#### Drupal 6

``` php
<?php
include_once './includes/bootstrap.inc';
drupal_bootstrap(DRUPAL_BOOTSTRAP_FULL);
drupal_flush_all_caches();
?>
```

#### Drupal 7 version

``` php
<?php
// Define static var.
define('DRUPAL_ROOT', getcwd());
// Include bootstrap.
include_once('./includes/bootstrap.inc');
// Initialize stuff.
drupal_bootstrap(DRUPAL_BOOTSTRAP_FULL);
// Clear cache.
drupal_flush_all_caches();
?>
```

## Clearing specific entries in cache tables\<\>

The [Drupal cache API](https://www.drupal.org/docs/7/api/cache-api) can be used to clear specific items. Caching back ends can be switched (to memcache, to flat files, etc.) without having to rewrite any code.

``` php
cache_clear_all('content:' . $MYNID, 'cache_content', TRUE);
```

The example above clears all items from cache that *start* with 'content:\$MYNID\*'. To only remove one specific row, drop the \$wildcard parameter (the "TRUE" statement in the function call) and change the format of the first parameter to omit the asterisk, which functions as a wildcard.

``` php
<?php
cache_clear_all('content:' . $MYNID . ':' . $MYNID, 'cache_content');
?>
```
