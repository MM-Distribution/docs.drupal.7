---
title: "Using .clearfix"
source_url: "https://www.drupal.org/docs/7/theming/working-with-css/using-clearfix"
page_type: page
last_updated: "Last updated on 19 September 2016"
published: "2010-04-22T19:36:28+00:00"
modified: "2016-09-19T20:50:24+00:00"
breadcrumb: ["Drupal 7", "Theming Drupal 7", "Working with CSS"]
fetched: "2026-10-21T08:16:01Z"
raw: "raw/docs/7/theming/working-with-css/using-clearfix.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Using .clearfix

Drupal 6's “clear-block” class was a Drupalism for functionality which is better known by the CSS Community as “clearfix.” Furthermore, using the “block” term was confusing as it is not dependent on Drupal’s block system. The clear-block class has been renamed to clearfix in Drupal 7.

7.x and 8.x

``` php
<div class="clearfix">
```

Here's what Drupal provides by default from system.base.css:

``` php
/**
 * Markup free clearing.
 *
 * @see http://perishablepress.com/press/2009/12/06/new-clearfix-hack
 */
.clearfix:after {
  content: ".";
  display: block;
  height: 0;
  clear: both;
  visibility: hidden;
}
/* IE6 */
* html .clearfix {
  height: 1%;
}
/* IE7 */
*:first-child + html .clearfix {
  min-height: 1%;
}
```
