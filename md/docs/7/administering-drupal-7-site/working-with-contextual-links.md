---
title: "Working with contextual links"
source_url: "https://www.drupal.org/docs/7/administering-drupal-7-site/working-with-contextual-links"
page_type: page
last_updated: "Last updated on 9 December 2017"
published: "2009-12-10T23:49:19+00:00"
modified: "2017-12-09T00:11:29+00:00"
breadcrumb: ["Drupal 7", "Administering Drupal 7 site"]
fetched: "2026-10-21T05:59:07Z"
raw: "raw/docs/7/administering-drupal-7-site/working-with-contextual-links.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Working with contextual links

In Drupal 7, some modules supply contextual links that allow privileged users to quickly perform tasks that are related to regions of the page without navigating to the Admin Dashboard. For example, when you hover your mouse over a block or node, links are displayed that allow you to make changes to the block or node.

![](/files/contextuallinks.jpg)

## Uses

You can enable and disable contextual links and you can specify the user roles that have permission to view and use contextual links.

### Enabling contextual links

To enable the Contextual links module:

1.  Navigate to the modules administration page (*Administer \> Modules*).
2.  In the *Core* section of the *Modules* page, enable the *Contextual Links* module
3.  Click *Save Configuration*.

### Configuring contextual links permissions

To set permissions for different user roles to access the contextual links:

1.  Navigate to the Permissions page (*People \> Permissions tab*).
2.  For each role you can enable or disable the *Use contextual links* permission.
3.  Click *Save Permissions*.

Note that contextual links are not displayed if the user does not have permission to perform the specific action represented by the link.

### Displaying contextual links

When using default rendering, the normal *teaser view* will embed the contextual links on nodes for you.

If using a customized theme, *your node template should include the normal renderable elements* found in core's node.tpl.php. Specifically, the contextual links are provided by the line  
` print render($title_suffix); `  
`$title_suffix` is where these functions are usually inserted. The same should apply to blocks and other places contextual links are available.

In order for the contextual links to be positioned correctly, you must ensure the "`contextual-links-region`" class is present on a containing element. The theme system will usually provide this class in the `$classes` variable in your node template, but if you are overriding classes or specifying them directly in the template, you will have to add this class explicitly.

Contextual links are not available by default to views with "field" based rows.

## Adding new contextual links

This page contains a rough guide for adding new contextual links in a custom module of your own.

Contextual links are basically added in two steps:

1.  Declaring menu items using [hook_menu](http://api.drupal.org/api/drupal/modules--system--system.api.php/function/hook_menu/7) or [hook_menu_alter](http://api.drupal.org/api/drupal/modules--system--system.api.php/function/hook_menu_alter/7).
2.  Adding the contextual links render element to render arrays.

### Declaring contextual link menu items

Contextual links are implemented as [local tasks](http://api.drupal.org/api/drupal/includes--menu.inc/constant/MENU_LOCAL_TASK/7) in the menu system. Additionally, the parameter *context* is set to [MENU_CONTEXT_INLINE](http://api.drupal.org/api/drupal/includes--menu.inc/constant/MENU_CONTEXT_INLINE/7).

Menu items for contextual links could look like this:

``` php
  // An example contextual link menu item.
  $items['contextual/%/information'] = array(
    'title' => 'Block information',
    'type' => MENU_LOCAL_ACTION,
    'context' => MENU_CONTEXT_INLINE,
    'page callback' => 'contextual_example_page',
    'page arguments' => array(1),
    'access callback' => TRUE,
  );
  // To use local task menu items, there must be a parent page.
  $items['contextual'] = array(
    'title' => 'The contextual example page',
    'page callback' => 'contextual_example_page',
    'page arguments' => array(1),
    'access callback' => TRUE,
  );
```

### Adding the contextual link render element

The contextual link render element is added by using any function that can alter a renderable array. An example follows:

``` php
/**
 * Implements hook_block_view_alter().
 */
function contextual_example_block_view_alter(&$data, $block) {
  // Contextual links can be added as a renderable element to the content of
  // a render array. We check if the block has content, and if so add a
  // contextual link to it.
  if (isset($data['content']) && is_array($data['content'])) {
    $contextual_links = array(
      'contextual',
      array($block->module),
    );

    $data['content']['#contextual_links']['contextual_example'] = $contextual_links;
  }

}
```

The contextual link render element has an array keyed with the module providing the contextual links. This array has two values, the first being the path examined for local task menu items, the second containing any callback arguments for that menu item (placed in yet another array).

Please note that this element *will be changed* by the contextual_preprocess function, moving it to any title suffix element in that part of the render array. If there is no title suffix element, the contextual links will not be displayed (unless you change the preprocessing).
