---
title: "Adding browser-specific style sheets"
source_url: "https://www.drupal.org/docs/7/theming/advanced/adding-browser-specific-style-sheets"
page_type: page
last_updated: "Last updated on 31 August 2016"
published: "2010-03-16T21:25:43+00:00"
modified: "2016-08-31T14:09:42+00:00"
breadcrumb: ["Drupal 7", "Theming Drupal 7", "Advanced theming"]
fetched: "2026-10-21T08:17:18Z"
raw: "raw/docs/7/theming/advanced/adding-browser-specific-style-sheets.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Adding browser-specific style sheets

You can add a browser-specific style sheet.

## Drupal 6

Below is a Drupal 6 theme example for including IE6\< targeted CSS files. (Examples are taken from the Garland theme found in the Drupal core installation.)

`page.tpl.php:`

``` php
<?php
...
<?php print $styles ?>
<!--[if lt IE 7]>
  <?php print phptemplate_get_ie_styles(); ?>
<![endif]-->
...
?>
```

`template.php:`

``` php
<?php
...
function phptemplate_get_ie_styles() {
  global $language;

  $iecss = '<link type="text/css" rel="stylesheet" media="all" href="'. base_path() . path_to_theme() .'/fix-ie.css" />';
  if ($language->direction == LANGUAGE_RTL) {
    $iecss .= '<style type="text/css" media="all">@import "'. base_path() . path_to_theme() .'/fix-ie-rtl.css";</style>';
  }

  return $iecss;
}
...
?>
```

## Drupal 7

Drupal 7 adds the ability to specify a 'browsers' key when calling drupal_add_css().

`template.php:`

``` php
<?php
...
function yourthemename_preprocess_html(&$vars) {
  ...
  drupal_add_css(path_to_theme() . '/fix-ie.css', array('weight' => CSS_THEME, 'browsers' => array('IE' => 'lt IE 7', '!IE' => FALSE), 'preprocess' => FALSE));
}
...
?>
```

See the API documentation for [drupal_pre_render_conditional_comments()](http://api.drupal.org/api/drupal/includes--common.inc/function/drupal_pre_render_conditional_comments/7) for details on the 'IE' and '!IE' keys.

It is recommended for themes to always use drupal_add_css() for adding a CSS file, so that Drupal code knows the exact total number of CSS files being added. This is information that might be needed for working around Internet Explorer's limitation of only being able to load the first 31 LINK/STYLE tags.
