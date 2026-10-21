---
title: "Default baseline variables"
source_url: "https://www.drupal.org/docs/7/theming/overriding-themable-output/default-baseline-variables"
page_type: page
last_updated: "Last updated on 31 August 2016"
published: "2008-02-26T02:38:51+00:00"
modified: "2016-08-31T14:15:55+00:00"
breadcrumb: ["Drupal 7", "Theming Drupal 7", "Overriding themable output"]
fetched: "2026-10-21T08:18:51Z"
raw: "raw/docs/7/theming/overriding-themable-output/default-baseline-variables.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Default baseline variables

The following are the baseline variables available to all [template files](/node/190815). They are generated through the [preprocessor function](/node/223430), [template_preprocess Drupal 6](http://api.drupal.org/api/function/template_preprocess/6) or [template_preprocess Drupal 7](http://api.drupal.org/api/function/template_preprocess/7). Variables specific to the template are documented inside the file.

## New Variables available in D7

`$attributes_array`

`$title_attributes_array`

`$content_attributes_array`

`$classes_array`

Array of html class attribute values. It is flattened into a string within the variable \$classes.

`$title_prefix`

An array containing additional output populated by modules, intended to be displayed in front of the main title tag that appears in the template.

`$title_suffix`

An array containing additional output populated by modules, intended to be displayed after the main title tag that appears in the template.

## Variables available in both D6 and D7

`$id`  
*The placement of the template. Each time the template is used, it is incremented by one.*

`$zebra`  
*Either "odd" or "even". Alternate each time the template is used.*

`$directory`  
*The theme path relative to the base install. example: "sites/all/themes/myTheme"*

`$is_admin`  
*Boolean returns TRUE when the visitor is a site administrator.*

`$is_front`  
*Boolean returns TRUE when viewing the front page of the site.*

`$logged_in`  
*Boolean returns TRUE when the visitor is a member of the site, logged in and authenticated.*

`$db_is_active`  
*Boolean returns TRUE when the database is active and running. This is only useful for [theming in maintenance mode](/node/195435) where the site may run into database problems.*

`$user`  
*The user object containing data for the current visitor. Some of the data contained here may not be safe. Be sure to pass potentially dangerous strings through [check_plain](http://api.drupal.org/api/function/check_plain/6).*
