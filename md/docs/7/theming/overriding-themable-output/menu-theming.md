---
title: "Menu theming"
source_url: "https://www.drupal.org/docs/7/theming/overriding-themable-output/menu-theming"
page_type: page
last_updated: "Last updated on 31 August 2016"
published: "2010-12-04T05:59:32+00:00"
modified: "2016-08-31T14:15:53+00:00"
breadcrumb: ["Drupal 7", "Theming Drupal 7", "Overriding themable output"]
fetched: "2026-10-21T08:21:41Z"
raw: "raw/docs/7/theming/overriding-themable-output/menu-theming.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Menu theming

The new [theme_links(\$variables)](http://api.drupal.org/api/drupal/includes--theme.inc/function/theme_links/7) function in D7 receives only an associative array to build the entire link structure. As you can read in the documentation, your links should be passed through the *links* argument as an associative array, but does not describe where and/or how you get this array.

The following is an example of how to do it with the user menu:

``` php
<?php
$user_menu = menu_navigation_links('user-menu'); 
print theme('links', array(
  'links' => $user_menu,
  'attributes' => array(
    'id' => 'user-menu',
    'class' => array('links', 'clearfix'),
  ),
  'heading' => array(
    'text' => t('User menu'),
    'level' => 'h2',
    'class' => array('element-invisible'),
  ),
));
?>
```

If you are wondering what the `"user-menu"` argument is in the [menu_navigation_links(\$menu_name, \$level = 0)](http://api.drupal.org/api/drupal/includes--menu.inc/function/menu_navigation_links/7) function, it is the name of the menu to be printed. You can find the menu name for this example on the *User menu* administration page (*Administration \> Structure \> Menus \> User menu* or `http://example.com/admin/structure/menu/manage/user-menu/edit`) on your site.

In this example, the *\$user_menu* variable is not mandatory, but doing it this way, you can later use it in a conditional statement that is quite common in the templates.
