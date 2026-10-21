---
title: "Adding style sheets from .info files"
source_url: "https://www.drupal.org/docs/7/theming/working-with-css/adding-style-sheets-from-info-files"
page_type: page
last_updated: "Last updated on 22 December 2016"
published: "2007-08-28T16:15:09+00:00"
modified: "2016-12-22T07:40:01+00:00"
breadcrumb: ["Drupal 7", "Theming Drupal 7", "Working with CSS"]
fetched: "2026-10-21T08:14:28Z"
raw: "raw/docs/7/theming/working-with-css/adding-style-sheets-from-info-files.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Adding style sheets from .info files

This page explains how to add a style sheet using the [.info file](/node/171205) of a theme. To add a style sheet programmatically, see the [API functions](/node/225868) page. Styling themes purely through CSS is possible with the information provided here.

*Notes:*

- *When working with style sheets, make sure that CSS Optimization is disabled. *CSS Optimization aggregates all of the style sheets for a site in order to improve performance. When CSS Optimization is enabled, no changes to your style sheets will be reflected on your site until the aggregated styles are cleared.* You can enable CSS Optimization again when you're done modifying your style sheets*. *For Drupal 7 it is located in "Administer \> Configuration \> Development \> Performance".*
- *The .info file is cached. Adding or removing any styles will not be detected until the cache is cleared and the revised .info is read. *(Do not confuse this with the [theme registry](/node/173880#theme-registry).) You must [clear the cache](http://drupal.org/node/337176) to see the changes.**

Adding style sheets:  
In Drupal 6, by default, a "style.css" file will be used from your theme when no other styles are defined inside the .info file. In Drupal 7, the style.css file will be used only if it is specified in the .info file. Adding other styles is as simple as defining a new '`stylesheets`' key with its [media property](http://www.w3.org/TR/CSS21/media.html) and the name of the style sheet. Keep in mind that defining custom styles will prevent the default "style.css" from loading. Remember to explicitly define the default style sheet if your theme uses it.

``` php
; Add a style sheet for all media
stylesheets[all][] = theStyle.css

; Add a style sheet for screen and projection media
stylesheets[screen, projection][] = theScreenProjectionStyle.css

; Add a style sheet for print media
stylesheets[print][] = thePrintStyle.css

; Add a style sheet with media query
stylesheets[screen and (max-width: 600px)][] = theStyle600.css
    
```

*A few notes:*

- *Note the empty square brackets between the `[media]` and `= styleName.css`.* These are always empty and denote that each stylesheet is appended to an array, as in php.
- *The order in which the styles are listed in the .info file will reflect the order it is displayed on head of the page.*
- *The style sheets can be placed in sub-directories, i.e., `stylesheets[all][] = stylesheets/styleName.css`. Useful for organizing style sheets.*
- *However, it is recommended that sub-directories be kept to one level, i.e.,`stylesheets[all][] = css/foo/styleName.css` may cause a problem with some templates. Safer is `stylesheets[all][] = css/styleName.css` or `stylesheets[all][] = foo/styleName.css`.*
- The word "style" can not be used in the name, like "myown_style.css". It will conflict with the default style.css. Anyhow, myownstyle.css will work.

Adding external stylesheets  
To use a stylesheet external to your theme, such as one hosted on a CDN, you cannot use the themes .info file. Instead you can add this in `template.php`. In Drupal 7 do this as follows:

``` php
function mytheme_preprocess_html(&$variables) {
  drupal_add_css('http://fonts.googleapis.com/css?family=News+Cycle', array('type' => 'external'));
}
```
