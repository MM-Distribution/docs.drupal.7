---
title: "Creating a custom build of Modernizr based on your Drupal setup"
source_url: "https://www.drupal.org/docs/7/theming/tools-and-best-practices/creating-a-custom-build-of-modernizr-based-on-your-drupal"
page_type: page
last_updated: "Last updated on 8 September 2016"
published: "2013-02-11T00:08:09+00:00"
modified: "2016-09-08T13:39:04+00:00"
breadcrumb: ["Drupal 7", "Theming Drupal 7", "Tools and best practices"]
fetched: "2026-10-21T08:55:53Z"
raw: "raw/docs/7/theming/tools-and-best-practices/creating-a-custom-build-of-modernizr-based-on-your-drupal.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Creating a custom build of Modernizr based on your Drupal setup

When your site is ready to go live, you'll want to take inventory of which [feature tests](http://drupal.org/node/1913726) you used, and reduce your Modernizr JS library to include only those tests that you need. This way it is as small as possible, downloading and executing more quickly than it would with unused feature detections present and firing.

The [Modernizr module](http://drupal.org/project/modernizr) has you covered; it keeps track of all the tests being requested by other modules and themes — just visit `admin/config/development/modernizr`. There are three sources: modules, themes, and tests within your current copy of modernizr.js.

There's a link to download the exact custom build described on the config page, pictured here:

------------------------------------------------------------------------

![An image of the Modernizr module's custom build screen.](/files/modernizr-download-custom-build.png)

------------------------------------------------------------------------

The button will link to [modernizr.com/download/](http://modernizr.com/download/), allowing you to customize your copy of Modernizr before downloading the file. Once downloaded or copied to your clipboard, it will need to be placed at `sites/all/libraries/modernizr`.

After placing the library in the correct location, you should be able to reload the Modernizr configuration page and see an updated list reflecting any customizations you made once you were on the Modernizr download page.

## Missing tests/utilities

As of 7.x-3.3, the module will report when it cannot find required tests or utilities within your current custom build of Modernizr. The missing tests are highlighted red and display the word `(missing)` after their name. Here is a sample screenshot of a custom build that is missing `flexbox` and `load`:

![Sample screenshot demonstrating how the admin interface displays missing tests and utilities](/files/modernizr-custom-build-missing-tests.png)
