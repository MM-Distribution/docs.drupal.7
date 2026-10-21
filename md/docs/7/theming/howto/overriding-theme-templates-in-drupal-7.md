---
title: "Overriding Theme Templates in Drupal 7"
source_url: "https://www.drupal.org/docs/7/theming/howto/overriding-theme-templates-in-drupal-7"
page_type: page
last_updated: "Last updated on 16 September 2016"
published: "2008-11-20T19:11:47+00:00"
modified: "2016-09-16T00:52:59+00:00"
breadcrumb: ["Drupal 7", "Theming Drupal 7", "Theming HowTos"]
fetched: "2026-10-21T08:50:58Z"
raw: "raw/docs/7/theming/howto/overriding-theme-templates-in-drupal-7.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Overriding Theme Templates in Drupal 7

### Adding additional preprocess functions inside existing preprocess functions

You may want to add additional preprocess functions inside your theme's preprocess function or preprocess_hook function to create different variable in different situations. For instance, if you wanted to have a node-type template (node-story.tpl.php) you could create a function called MYTHEME_preprocess_node_story(), where you would set story specific variables. The title of the function is not called through the theme API, so you could call it whatever you like, but this would allow you to setup your own API for calling all node-type templates with only a few lines of code.

**Drupal 7**

``` php
function THEME_preprocess_node(&$variables) {
  $node = $variables['node'];

  // Create preprocess functions per content type.
  $function = __FUNCTION__ . '_' . $node->type;
    if (function_exists($function)) { 
      $function($variables);
    } 
}
```

You can then have a preprocess function depending per content type in your template.php like so:

``` php
function THEME_preprocess_node_MY_CONTENT_TYPE(& $variables) {
  // Code that is specific to this content type
} 
```
