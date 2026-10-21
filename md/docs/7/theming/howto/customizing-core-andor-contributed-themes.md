---
title: "Customizing core and/or contributed themes"
source_url: "https://www.drupal.org/docs/7/theming/howto/customizing-core-andor-contributed-themes"
page_type: page
last_updated: "Last updated on 13 November 2022"
published: "2014-08-20T04:00:55+00:00"
modified: "2022-11-13T20:38:34+00:00"
breadcrumb: ["Drupal 7", "Theming Drupal 7", "Theming HowTos"]
fetched: "2026-10-21T08:50:11Z"
raw: "raw/docs/7/theming/howto/customizing-core-andor-contributed-themes.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Customizing core and/or contributed themes

Core and contrib themes are nice as they provide a site theme with no coding at all. However, it's rare that these themes are exactly what we want, and we often need to add our own modifications to match the specifics of our site.

Editing the files included in contrib and core themes is a big no-no, as these changes will be overwritten when the theme is updated. We can get around this by creating a sub-theme of whichever theme we are using, and make our own site specific themes.

To do this, you should do the following:

1.  [Create a sub-theme](https://www.drupal.org/node/225125) of the theme you want to customize.
2.  Include at least one stylesheet in the .info file for this theme (as described in the above link). Make sure that this file does not have the same name as any of the stylesheets in the parent theme. If you use the same name, your stylesheet will be used and the parent stylesheet will not.
3.  Make any CSS changes specific to your site within this stylesheet.

By using this method, any and all CSS changes you make to your site will be in files external to the theme you are adapting, and therefore when the theme is updated, you will not lose your changes. And since sub-theme CSS files will always be included after the parent theme stylesheets, the CSS in the sub-theme stylesheet will take priority over the parent theme's CSS.
