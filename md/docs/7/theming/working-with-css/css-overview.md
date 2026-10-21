---
title: "CSS overview"
source_url: "https://www.drupal.org/docs/7/theming/working-with-css/css-overview"
page_type: page
last_updated: "Last updated on 11 March 2021"
published: "2008-12-01T17:27:24+00:00"
modified: "2021-03-11T21:35:31+00:00"
breadcrumb: ["Drupal 7", "Theming Drupal 7", "Working with CSS"]
fetched: "2026-10-21T08:13:56Z"
raw: "raw/docs/7/theming/working-with-css/css-overview.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# CSS overview

Most modern web pages use external style sheets to control the presentation of a page. In a traditional static HTML page, a pointer to a style sheet must be manually placed within the HTML code (usually within the page header).

Here's an example:

`<link rel="stylesheet" type="text/css" href="/mytheme.css" />`

This code simply tells the browser where to find one of the style sheets (mytheme.css) that control the appearance of the page.

To the browser, a page from a Drupal site might look exactly the same: the HTML header has the same kind of pointers to external style sheets. The key difference is that behind the scene, those pointers are added to the HTML automatically. Some styles might come from the theme itself and others might be supplied by various Drupal modules (to provide default styling for the module output).

## Adding stylesheets in Drupal

You can add new style sheets to a theme or module, and you can override a default style sheet from Drupal core, contributed modules, or even another theme. There are two main ways to do this.

You can include the stylesheet using the .info file of a theme or module. This only works when the CSS file is bundled as part of that theme or module. It will cause the stylesheet to be included on every page. Here is an example (from the Zen theme):

``` php
stylesheets[all][] = system.base.css
```

Alternatively, you can inject CSS using the drupal_add_css() function, which will allow you to limit the pages where CSS appears, or to use an external stylesheet (for instance, one hosted on a CDN). To do this, call it from an appropriate function in a .module file or in your theme's template.php file.

Here is an example that adds a google font:

``` php
function mytheme_preprocess_html(&$variables) {
  drupal_add_css('http://fonts.googleapis.com/css?family=News+Cycle', array('type' => 'external')); } 
```
