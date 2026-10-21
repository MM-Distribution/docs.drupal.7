---
title: "Installing Modernizr module and JavaScript library"
source_url: "https://www.drupal.org/docs/7/theming/tools-and-best-practices/installing-modernizr-module-and-javascript-library"
page_type: page
last_updated: "Last updated on 8 September 2016"
published: "2013-02-10T23:56:17+00:00"
modified: "2016-09-08T13:41:17+00:00"
breadcrumb: ["Drupal 7", "Theming Drupal 7", "Tools and best practices"]
fetched: "2026-10-21T08:55:37Z"
raw: "raw/docs/7/theming/tools-and-best-practices/installing-modernizr-module-and-javascript-library.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Installing Modernizr module and JavaScript library

[Modernizr is not GPLv2](http://modernizr.com/license/), and therefore cannot ship within Drupal modules. Since the [Modernizr module](http://drupal.org/project/modernizr) depends on the upstream JavaScript library, you cannot simply enable the module and expect it to work. Just like a WYSIWYG module or jQuery Update, you must upload your own copy of the JS file after uploading the module to your server.

## Drush (easiest)

The best and easiest way to install Modernizr is to use [drush](http://drupal.org/project/drush), the command-line tool for Drupal.

``` php
drush en modernizr -y
```

This will enable the Modernizr module and automatically download a development copy of modernizr.js. If you'd like to replace your current file, delete it and run the following command:

``` php
drush mdl
```

Drush can detect whether or not you're using the [Libraries API](http://drupal.org/project/libraries) and place the file in the correct location within your Drupal codebase: `sites/all/libraries/modernizr`

## Without Drush

If you are unable or unwilling to use Drush, you'll have to go to [modernizr.com](http://modernizr.com), get the file from the site, and upload it to `sites/all/libraries/modernizr`
