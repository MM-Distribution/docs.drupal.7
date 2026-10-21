---
title: "Rounded Corners in Drupal 7 (jquery corner)"
source_url: "https://www.drupal.org/docs/7/theming/howto/rounded-corners-in-drupal-7-jquery-corner"
page_type: page
last_updated: "Last updated on 8 September 2016"
published: "2011-01-17T18:26:35+00:00"
modified: "2016-09-08T14:07:08+00:00"
breadcrumb: ["Drupal 7", "Theming Drupal 7", "Theming HowTos"]
fetched: "2026-10-21T08:51:29Z"
raw: "raw/docs/7/theming/howto/rounded-corners-in-drupal-7-jquery-corner.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Rounded Corners in Drupal 7 (jquery corner)

This is a short and painless intro into generating lovely rounded corners for your divs in Drupal 7.

- Download the latest version of jquery-corner from <http://jquery.malsup.com/corner/>.
- Save it under YOURTHEME/js/jquery.corner.js
- Create an empty file YOURTHEME_corner.js in the same directory
- In your already existing YOURTHEME.info, add scripts\[\] = js/jquery.corner.js and scripts\[\] = js/YOURTHEME_corner.js
- **Flush your cache!!!!!**
- and follow the instructions below

In the YOURTHEME_corner.js, add the following:

``` php
(function ($) {
  Drupal.behaviors.YOUTHEME = {
    attach: function(context, settings) {
      // list every element that you would like to adorn with corners below
      $("#block-user-login h2").corner("tl tr 4px"); // this is just an example, customize as you'd like, tl = top left
    }
  }
})(jQuery);
```

Done! For questions, contact me at [www.ZUROSS.com](http://www.ZUROSS.com).
