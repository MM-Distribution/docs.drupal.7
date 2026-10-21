---
title: "Working with template suggestions"
source_url: "https://www.drupal.org/docs/7/theming/overriding-themable-output/working-with-template-suggestions"
page_type: page
last_updated: "Last updated on 4 February 2025"
published: "2008-02-18T20:37:32+00:00"
modified: "2025-02-04T10:01:06+00:00"
breadcrumb: ["Drupal 7", "Theming Drupal 7", "Overriding themable output"]
fetched: "2026-10-21T08:22:28Z"
raw: "raw/docs/7/theming/overriding-themable-output/working-with-template-suggestions.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Working with template suggestions

See new documentation for Drupal 8+ : <https://www.drupal.org/node/2358785>

Template suggestions are alternate templates based on existing .tpl.php files. These suggestions can be used when a specified condition is met and the suggested template exists. All layers from core, modules, theme engines and themes can provide the suggestions. You can think of the suggestions as *naming hints* telling the system to pick and choose based on the right circumstances. The idea is simple but it is a powerful feature, providing another layer of customization.

*[Theme Developer](/project/devel_themer) module showing template suggestions for the [possible "page" templates.](/node/190815#page-suggestion) The image shows Drupal 6 template suggestions.*  
![devel showing Drupal 6 template suggestions](/files/devel_suggestions.png)

These naming suggestions are set of [preprocess functions](/node/223430). There are plenty already provided by core. If you need to extend it further, add a preprocessor for the theming hook into your template.php file. The examples below add suggestions on the *"node"* and *"page"* theming hooks. It can be added to any hook implemented as a template.

### Theme debug mode

As of [Drupal 7.33](https://www.drupal.org/drupal-7.33-release-notes), Drupal core has a theme debug mode that can be enabled and disabled via the `theme_debug` variable. Theme debug mode can be used to see possible template suggestions and the locations of template files right in your HTML markup (as HTML comments). To enable it, add this line to your settings.php:

``` php
$conf['theme_debug'] = TRUE;
```

You can enable it with drush using:

``` php
drush vset theme_debug 1
```

And disable using

``` php
drush vset theme_debug 0
```

**You'll then see output like this when you inspect or view source:**

``` php
<!-- THEME DEBUG -->
<!-- CALL: theme('page') -->
<!-- FILE NAME SUGGESTIONS:
   * page--front.tpl.php
   * page--node.tpl.php
   x page.tpl.php
-->
<!-- BEGIN OUTPUT from 'modules/system/page.tpl.php' -->
…
<!-- END OUTPUT from 'modules/system/page.tpl.php' -->
```

------------------------------------------------------------------------

A listing of all the suggestions for Drupal 7 core can be found in [Drupal 7 Template Suggestions](/node/1089656).

To use the examples below, paste the function definitions into a template.php file in your theme directory, ex: "sites/all/themes/drop/template.php". If a template.php file does not exist in your theme, you may create one. The prefix of "drop" should be the name of your theme.

``` php
// Add a single suggestion for nodes that have the "Promoted to front page" box checked.
function drop_preprocess_node(&$variables) {
  if ($variables['promote']) {
    // looks for node--promoted.tpl.php in your theme directory
    $variables['theme_hook_suggestion'] = 'node__promoted';
  }
}

// Add multiple suggestions for pages based on the logged in user's roles.
function drop_preprocess_page(&$variables) {
  global $user;
  
  if (!empty($user->roles)) {
    foreach ($user->roles as $role) {
      $filter = '![^a-z0-9-_]+!s';
      $string_clean = preg_replace($filter, '-', drupal_strtolower($role));

      // looks for page--[role].tpl.php in your theme directory
      // ex: page--administrator.tpl.php
      $variables['theme_hook_suggestions'][] =  'page__' . $string_clean;
    }
  }
}
```

There are two ways to add these suggestions.

1.  The key of '`theme_hook_suggestion`' accepts a single suggestion and it takes precedence. If the condition is met and the file exists, it will be used to ignore all others.
2.  The key of '`theme_hook_suggestions`' *(plural)* can accept an array of suggestions. They are processed in FILO order *(first in ,last out)*. Adding to the array should be done with a general condition first, progressively getting more specific so it cascades based on specificity.

A few notes:

- When adding to '`theme_hook_suggestions`', add to the array. Do not reset it since the variables are passed by reference. All the suggestions set before it in core and modules would be lost.  

  ``` php
  // Do not do this:
  $variables['theme_hook_suggestions'] = array('hook__suggestion');
    
  // Instead do this:
  $variables['theme_hook_suggestions'][] = 'hook__suggestion';
  ```

- Prefix the suggestion with the name of the hook, it is associated with, such as "node" or "page". This keeps it clear and the files grouped together. It also minimizes any chance of Drupal registering the template with a different hook.

- Use two hyphens to separate the hook name from the rest of the suggestion. This is consistent with template naming suggestions in core.

- Use underscores ("\_") instead of hyphens ("-") when adding to the array but use hyphens for your template.  

  ``` php
  // Do not do this:
  $variables['theme_hook_suggestions'] = array('pagemanager-item__' . $style);

  // Instead do this:
  $variables['theme_hook_suggestions'][] = 'pagemanager_item__' . $style;
  // to get to pagemanager-item--style1.tpl.php
  ```
