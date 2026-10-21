---
title: "Default .info values"
source_url: "https://www.drupal.org/docs/7/theming/default-info-values"
page_type: page
last_updated: "Last updated on 31 August 2016"
published: "2007-08-28T16:10:57+00:00"
modified: "2016-08-31T13:54:46+00:00"
breadcrumb: ["Drupal 7", "Theming Drupal 7"]
fetched: "2026-10-21T06:01:27Z"
raw: "raw/docs/7/theming/default-info-values.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Default .info values

The following are the assumed defaults. When they are not defined, the theme will automatically take these values.  
*Default values are defined in [\_system_rebuild_theme_data()](http://api.drupal.org/api/drupal/modules%21system%21system.module/function/_system_rebuild_theme_data/7).*

*Note: These defaults apply as a group. In other words, overriding a region with `regions[sub_header] = Sub-header` will omit the rest of the default regions. To gain them back, they must be redefined. This also applies to stylesheets. Even though it's not technically in a group, defining another stylesheet will prevent "style.css" from being included unless it is redefined.*

regions  
Drupal 7

``` php
regions[sidebar_first]  = Left sidebar
regions[sidebar_second] = Right sidebar
regions[content] = Content
regions[header] = Header
regions[footer] = Footer
regions[highlighted] = Highlighted
regions[help] = Help
regions[page_top] = Page Top
regions[page_bottom] = Page Bottom
```

Drupal 6

``` php
regions[left] = Left sidebar
regions[right] = Right sidebar
regions[content] = Content
regions[header] = Header
regions[footer] = Footer
```

engine  
Drupal 7

``` php
engine = phptemplate
```

features  
Drupal 7

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

Drupal 6

``` php
features[] = logo
features[] = name
features[] = slogan
features[] = mission
features[] = node_user_picture
features[] = comment_user_picture
features[] = search
features[] = favicon
features[] = primary_links
features[] = secondary_links
```

theme settings  
Drupal 7

``` php
settings[toggle_logo] = 1
settings[toggle_name] = 1
settings[toggle_slogan] = 1
settings[toggle_node_user_picture] = 1
settings[toggle_comment_user_picture] = 1
settings[toggle_comment_user_verification] = 1
settings[toggle_favicon] = 1
settings[toggle_main_menu] = 1
settings[toggle_secondary_menu] = 1
```

screenshot  
``` php
screenshot = screenshot.png
```

stylesheets  
``` php
stylesheets[all][] = style.css
```

scripts  
``` php
scripts[] = script.js
```

php *(minimum support)*  
[DRUPAL_MINIMUM_PHP](http://api.drupal.org/api/constant/DRUPAL_MINIMUM_PHP) is a constant. It points to the minimum requirements for Drupal core to run.

``` php
php = DRUPAL_MINIMUM_PHP
```
