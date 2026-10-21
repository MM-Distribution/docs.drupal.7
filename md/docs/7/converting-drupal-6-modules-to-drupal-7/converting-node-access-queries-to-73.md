---
title: "Converting node access queries to 7.3"
source_url: "https://www.drupal.org/docs/7/converting-drupal-6-modules-to-drupal-7/converting-node-access-queries-to-73"
page_type: page
last_updated: "Last updated on 15 October 2016"
published: "2011-06-30T00:08:06+00:00"
modified: "2016-10-15T22:13:12+00:00"
breadcrumb: ["Drupal 7", "Converting Drupal 6 modules to Drupal 7"]
fetched: "2026-10-21T07:50:42Z"
raw: "raw/docs/7/converting-drupal-6-modules-to-drupal-7/converting-node-access-queries-to-73.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Converting node access queries to 7.3

Previously, for every node listing query, you only needed to add `$query->addTag('node_access');` Now, you also need to add `$query->addMetaData('base_table', $name_of_table_holding_the_nid);`. For example:

``` php
   $query = db_select('taxonomy_index', 't');
+  $query->addMetaData('base_table', 'taxonomy_index');
   $query->addTag('node_access');
   $query->condition('tid', $tid);
```

As of 7.3, core is able to discover the base table and so this change is optional. However, there's a slight performance hit if the `base_table` metadata is not defined explicitly, and in later versions it might become required to specify the base table this way. If your code is doing `db_select('node')` then the performance hit is negligible and there are no plans to mandate an `$query->addMetaData('base_table', 'node');` for these queries.
