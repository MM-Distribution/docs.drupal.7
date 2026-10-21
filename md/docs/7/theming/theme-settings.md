---
title: "Theme settings"
source_url: "https://www.drupal.org/docs/7/theming/theme-settings"
page_type: page
last_updated: "Last updated on 2 December 2018"
published: "2008-02-14T23:41:38+00:00"
modified: "2018-12-02T18:30:06+00:00"
breadcrumb: ["Drupal 7", "Theming Drupal 7"]
fetched: "2026-10-21T06:02:13Z"
raw: "raw/docs/7/theming/theme-settings.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Theme settings

Various page elements can be output by the theme. It can be toggled on and off on the theme's configuration page.

## Drupal 7

You can locate these settings at *"Administer \> Appearance \> Settings \> themeName".* For example, the site's slogan can be suppressed by unchecking the "Site slogan" check box on that page.

![Screenshot of features enabled in Drupal 7](/files/features_enabled_7.png)

These check-boxes show themselves depending on the features enabled inside the [.info file](/node/171205). It must be specified with the key of '`features`' followed by empty brackets then the feature itself, e.g., `features[] = the_feature`. If none is defined, the following values are assumed.

``` php
features[] = logo
features[] = name
features[] = slogan
features[] = node_user_picture
features[] = comment_user_picture
features[] = comment_user_verification
features[] = favicon
features[] = main_menu
features[] = secondary_menu
```

Drupal 7 *removes* the previously available mission and search as theme features (they can be created and controlled as blocks instead) and it adds a toggle for "User verification status in comments".

To disable any features, only add the ones you want into the .info file. The rest will be omitted when defining only the features that are needed for the theme. Some of the features will also enable related form fields. For example, '`logo`' will enable an upload field for the image along with the checkbox.

*Note:*

The contents of the .info file are cached in the database so altering it will not be noticed by Drupal. (Do not confuse this with the [theme registry](/node/173880#theme-registry).) To learn how to clear it, check out the options in [Clearing the theme cache](http://drupal.org/node/337176).
