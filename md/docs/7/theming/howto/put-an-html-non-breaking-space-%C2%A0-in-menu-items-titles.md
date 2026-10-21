---
title: "Put an HTML non breaking space (&nbsp;) in menu items titles"
source_url: "https://www.drupal.org/docs/7/theming/howto/put-an-html-non-breaking-space-%C2%A0-in-menu-items-titles"
page_type: page
last_updated: "Last updated on 3 November 2020"
published: "2015-05-30T18:19:16+00:00"
modified: "2020-11-03T20:36:44+00:00"
breadcrumb: ["Drupal 7", "Theming Drupal 7", "Theming HowTos"]
fetched: "2026-10-21T08:51:14Z"
raw: "raw/docs/7/theming/howto/put-an-html-non-breaking-space-%C2%A0-in-menu-items-titles.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Put an HTML non breaking space (&nbsp;) in menu items titles

Adding HTML like &nbsp; to menu titles can be helpful when you want to prevent menu titles which contain spaces from automatically wrapping to another line based on the position of a space character in the title. For example, for a menu title of "Reorder Images", depending on your layout, Drupal may put a line break between the word "Reoder" and the word "Images". Putting the code below into your template.php and changing the title to "Reorder&nbsp;Images", prevents this line break from happening.

Add this to your template.php:

``` php
function YOURTHEMENAME_link($variables) {
$variables['options']['html'] = TRUE;
  return '<a href="' . check_plain(url($variables['path'], $variables['options'])) . '"' . drupal_attributes($variables['options']['attributes']) . '>' . ($variables['options']['html'] ? $variables['text'] : check_plain($variables['text'])) . '</a>';
}
```

replace YOURTHEMENAME with your theme name.  
This is Drupal 7 core function theme_link() and I just added option \$variables\['options'\]\['html'\] = TRUE; and that's it.

Acknowledgement to xalexas comment at <https://www.drupal.org/node/112352#comment-9976285> for this helpful tip.

For Drupal 8 you can write this :

``` php
use Drupal\Core\Render\Markup;

/**
 * Implements hook_preprocess_HOOK()
 */
function YOURTHEME_preprocess_menu(&$variables){
  foreach($variables['items'] as &$link){
    $link['title'] = Markup::create($link['title']);
  }
}
```

Your link title must be a instance of MarkupInterface.
