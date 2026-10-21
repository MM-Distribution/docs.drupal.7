---
title: "Implementing the Modernizr Test API within a module or theme"
source_url: "https://www.drupal.org/docs/7/theming/tools-and-best-practices/implementing-the-modernizr-test-api-within-a-module-or-theme"
page_type: page
last_updated: "Last updated on 8 September 2016"
published: "2014-09-03T16:28:50+00:00"
modified: "2016-09-08T13:40:47+00:00"
breadcrumb: ["Drupal 7", "Theming Drupal 7", "Tools and best practices"]
fetched: "2026-10-21T08:56:24Z"
raw: "raw/docs/7/theming/tools-and-best-practices/implementing-the-modernizr-test-api-within-a-module-or-theme.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Implementing the Modernizr Test API within a module or theme

The Modernizr Drupal module provides a Test API which allows site admins to generate a custom build which contains all the features needed by modules and themes enabled within a Drupal site. This API is very simple, and implementing it means you'll be making life easier for any user who uses both your module/theme and the Modernizr module.

You can read the full docs within the [official modernizr.api.php file](http://cgit.drupalcode.org/modernizr/tree/modernizr.api.php), but here are a few samples:

## How to implement within a module

Implement `hook_modernizr_info()` in your module:

``` php
/**
 * Implements hook_modernizr_info().
 */
function mymodule_modernizr_info() {
  $tests = array();

  // My Module relies on media queries.
  $tests[] = 'mq';

  return $tests;
}
```

## How to implement within a theme

Themes should implement the dependencies within the `.info` file:

``` php
modernizr[tests][] = flexbox
```

Alternatively, you can implement `hook_modernizr_info_alter()` but we feel that the `.info` method more closely aligns with normal themer workflow and domain knowledge.

## List of modules/themes that support Test API

Once you implement this API, feel free to update this issue: [\#1914478: \[meta\] Provide Modernizr integration for other contrib modules](/project/modernizr/issues/1914478 "Status: Active")
