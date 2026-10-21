---
title: "Overriding style sheets from modules and base themes"
source_url: "https://www.drupal.org/docs/7/theming/working-with-css/overriding-style-sheets-from-modules-and-base-themes"
page_type: page
last_updated: "Last updated on 16 September 2016"
published: "2008-05-29T00:42:48+00:00"
modified: "2016-09-16T00:01:59+00:00"
breadcrumb: ["Drupal 7", "Theming Drupal 7", "Working with CSS"]
fetched: "2026-10-21T08:14:12Z"
raw: "raw/docs/7/theming/working-with-css/overriding-style-sheets-from-modules-and-base-themes.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Overriding style sheets from modules and base themes

You can override the style sheet provided by Drupal core, contributed modules or even other themes.

Most modules provide defaults for the presentation of its output. This includes the markup itself and an associated style sheet. *(see the explanation on the [overriding behavior](/node/173880#theming-overrides) for the markup.)* These default styles can be overridden by making changes within your theme.

## Overriding core and contributed module style sheets

To override a core or contributed module style sheet, it must be specified in your theme's .info file. Drupal overrides are cascading and your theme's stylesheets override any that were previously declared. For example, system-menus.css is located at "modules/system/system-menus.css". If you place a file with the same name in your theme's folder and add the following entry to the .info file, the original system-menus.css file will be ignored and your version will be loaded in its place.

`stylesheets[all][] = system-menus.css`

*A few notes:*

- *Overriding core CSS files will prevent the default "style.css" file from loading. Remember to explicitly define any [defaults](/node/171206) when needed. In Drupal 7, style.css does not load unless it is specified in the .info file.*
- *The themes override must have a matching media type of the original style.*
- *URLs within the replacement style sheet may need to be corrected. Check the file for any '`url()`' properties or '`@import`' rules to make sure they are pointing to the right resource.*
- *The order of style sheets listed in the head of the page will change. This may cause some cascading rules to change with it.*
- *Some core and module style sheets are loaded conditionally. Overriding through .info files will force the file to always be used.*
- *If only minor changes are required, consider using CSS selectors to override the styles instead of overriding the whole file.*
- *In Drupal 7, if you would like to override some css files please use [hook_css_alter](http://api.drupal.org/api/function/hook_css_alter/7) in template.php (see example in seven theme).*

Remember to [clear your cache](/node/337176) after making this change!

## Overriding or omitting a base theme style sheet

The following applies to [sub-themes](/node/225125). To prevent a style sheet from a base theme from being carried over to a sub-theme, you can redefine the style sheet inside the .info file. This works the same way as overriding module or core style sheets.

The base theme and the sub-theme must have the same entry:  
`stylesheets[all][] = masterStyle.css`

If the file exists inside the sub-theme, it will be used. Remove the file in the sub-theme to prevent the file from loading altogether.
