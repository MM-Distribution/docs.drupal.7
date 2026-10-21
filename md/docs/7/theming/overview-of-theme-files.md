---
title: "Overview of theme files"
source_url: "https://www.drupal.org/docs/7/theming/overview-of-theme-files"
page_type: page
last_updated: "Last updated on 23 December 2016"
published: "2007-08-28T15:49:50+00:00"
modified: "2016-12-23T08:25:15+00:00"
breadcrumb: ["Drupal 7", "Theming Drupal 7"]
fetched: "2026-10-21T06:00:56Z"
raw: "raw/docs/7/theming/overview-of-theme-files.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Overview of theme files

A theme is a collection of files that define the presentation layer. You can also create one or more "sub-themes" or variations on a theme. Only the .info file is required, but most themes and sub-themes will use other files as well. The following diagram illustrates the files that are found in a typical theme and sub-theme.

## Drupal 7

![drupal 7 theme templates](/files/7theme_anatomy-fix_1.png)

[.info](/node/171205) *(required)*

All that is required for Drupal to see your theme is a ".info" file. Should the theme require them, meta data, [style sheets](/node/171209), [JavaScripts](/node/171213), [block regions](/node/171224) and more can be defined here. Everything else is optional.

The internal name of the theme is also derived from this file. For example, if it is named "drop.info", then Drupal will see the name of the theme as "drop". *Drupal 5 and below used the name of the enclosing folder of the theme.*

*Info files for themes are new in Drupal 6. In version 5, .info files were used solely for modules.*

[template files](/node/190815) *(.tpl.php)*

These templates are used for the *(x)*HTML markup and PHP variables. In some situations they may output other types of data *--[xml rss](http://api.drupal.org/api/function/theme_aggregator_page_rss) for example*. Each .tpl.php file handles the output of a specific themable chunk of data, and in some situations it can handle multiple .tpl.php files through [suggestions](/node/223440). They are optional, and if none exists in your theme it will fall back to the default output. Refrain from having complex logic in these files. In most cases, it should be straight *(x)*HTML tags and PHP variables. A handful of these templates exists in directories where core and contributed modules exist. Copying them to your theme folder will force Drupal to read your version.

*Note: The [theme registry](/node/173880#theme-registry) caches information about the available theming data. You must reset it when *adding* or *removing* template files or theme functions from your theme.*

template.php

For all the conditional logic and data processing of the output, there is the template.php file. It is not required, but to keep the .tpl.php files tidy it can be used to hold [preprocessors](/node/223430) for generating variables before they are merged with the markup inside .tpl.php files. Custom functions, [overriding theme functions](/node/173880#function-override) or any other customization of the raw output should also be done here. This file must start with a PHP opening tag "\<?php", but the close tag is not needed and it is recommended that you omit it.

[Sub-themes](/node/225125)

On the surface, sub-themes behave just like any other theme. The only difference is that they inherit the resources from their parent themes. To create one, a "base theme" entry inside the .info file is needed. From there it will inherit the resources from its parent theme. There can be multiple levels of inheritance; i.e., a sub-theme can declare another sub-theme as its base. There are no hard set limits to this.

*Drupal 5 and below required sub-themes to be in sub-directories of the parent theme. This is no longer the case.*

Others

- The logo and screen shot are not absolutely necessary for the theme to function, but they are recommended, especially if you are [contributing your theme to the Drupal repository](/node/14208). Screenshots will show inside the theme administration page and the user account settings for selecting themes when the appropriate permissions are set. *See the [screenshot guidelines](/node/11637) for more information.*
- To supply administrative UI settings or "[features](/node/221905)" beyond the logo, search, mission, etc., a "theme-settings.php" file can be used. This is an advanced feature. More information can be found in the [Advanced settings](/node/177868) handbook page.
- For [color module support](/node/108459), a "color" directory with a "color.inc" file is needed along with various support files.

<!-- -->

- *If you want to base your work on a core theme, use [sub-theming](/node/225125) or make a copy and rename the theme. *Directly modifying Bartik, Garland or Minnelli is strongly discouraged, since they are used for the install and upgrade process.**
- *All non-Core or modifications to Core themes should be installed under the "sites/all/themes" directory to keep them separate from core files. If you plan to run multiple sites from a single Drupal code base, you can make a theme available to a specific site rather than all sites; read about how to set this up in [Multi-site installations](/node/43816).*
- *Unlike Drupal 6 where [page.tpl.php](https://api.drupal.org/api/drupal/modules%21system%21page.tpl.php/6) contains whole html structure, in Drupal 7 [html.tpl.php](https://api.drupal.org/api/drupal/modules!system!html.tpl.php/7) has been introduced. By default, these files are kept inside`/modules/system` directory and to override these just copy and paste to your custom theme.*
