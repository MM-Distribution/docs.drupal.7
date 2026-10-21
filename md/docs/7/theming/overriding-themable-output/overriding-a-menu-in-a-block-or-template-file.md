---
title: "Overriding a menu in a block or template file"
source_url: "https://www.drupal.org/docs/7/theming/overriding-themable-output/overriding-a-menu-in-a-block-or-template-file"
page_type: page
last_updated: "Last updated on 29 December 2021"
published: "2010-12-03T22:36:40+00:00"
modified: "2021-12-29T18:39:16+00:00"
breadcrumb: ["Drupal 7", "Theming Drupal 7", "Overriding themable output"]
fetched: "2026-10-21T08:21:57Z"
raw: "raw/docs/7/theming/overriding-themable-output/overriding-a-menu-in-a-block-or-template-file.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Overriding a menu in a block or template file

## Menu Links

For Drupal 7, in almost all themes, menu links are displayed by calling *theme('links\_\_system_main_menu')*. However, if you search for this specific function in Drupal API, you will not find it, and may be confused.

The answer to the confusion is that *links\_\_system_main_menu* is not an actual function, but a pattern. A pattern, like *page\_\_article*. In this pattern, the theming engine will look for this *theme\_...* function, and if not found, it will use the standard *theme('links')* from the [theme.inc](http://api.drupal.org/api/drupal/includes%21theme.inc/7) file. This is what happens in most cases, when this function is called when rendering your menu.

You can create an override for that function from your theme's `template.php` file, like so:

`<?php function themename_links__system_MENUNAME_menu($variables) {} ?>`

MENUNAME is obtainable by editing the menu. It is the machine name of the menu with dashes converted to underscores.

The *\$variables* parameter is passed in, and it contains an index called `'links'`. Each link contains an `'href'` and a `'title'`, among other things.

So inside your override function, loop over the links:

`<?php foreach ($variables['links'] as $link) {}?>`

If we just want to output an `<a>` tag, outside of Drupal we'd normally do:  
`<?php echo "<a href="{$link['href']}">{$link['title']}</a>"; ?>`

However, Drupal has the [l()](http://api.drupal.org/api/drupal/includes--common.inc/function/l/7) function to create links for you. This is preferable because there are some special cases such as the `<front>` link.

So instead, we'd do something like  
`<?php echo l($link['title'], $link['href'], $link); ?>`

The [l()](http://api.drupal.org/api/drupal/includes--common.inc/function/l/7) function will take care of adding an `active` class to a link if that link is to the page currently being viewed.

Your final function might look something like:

``` php
<?php
function THEMENAME_links__system_MENUNAME_menu($variables) {
  $output = '';
  foreach ($variables['links'] as $link) {
    $output .= l($link['title'], $link['href'], $link);
  }
  return $output;
}
?>
```

## Menu itself

In order to theme the *ul* tags of the menu, you need to use the [theme_menu_tree()](https://api.drupal.org/api/drupal/includes%21menu.inc/function/theme_menu_tree/7 "Drupal API") function. An example would be (template.php):

``` php
function THEMENAME_menu_tree__MENUNAME($variables) {
  return '<ul class="MY-CLASS">' . $variables['tree'] . '</ul>';
}
```

The above would append *MY-CLASS* to the classes of all *ul* tags of the MENUNAME. Note that the *machine name* of the menu is prefixed with "menu". For example, if your menu name is **Special Items**, the *machine name* to be added here is `menu_special_items`, NOT `special_items.`

In order to theme the top level tag only, you would:

``` php
function THEMENAME_menu_tree__menu_special_items($variables) {
 return '<ul class="MY-CLASS">' . $variables['tree'] . '</ul>';
}
```
