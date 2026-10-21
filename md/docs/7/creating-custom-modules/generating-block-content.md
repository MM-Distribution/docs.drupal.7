---
title: "Generating block content"
source_url: "https://www.drupal.org/docs/7/creating-custom-modules/generating-block-content"
page_type: page
last_updated: "Last updated on 29 March 2017"
published: "2011-03-24T19:44:59+00:00"
modified: "2017-03-29T19:55:08+00:00"
breadcrumb: ["Drupal 7", "Creating custom modules in Drupal 7"]
fetched: "2026-10-21T07:22:58Z"
raw: "raw/docs/7/creating-custom-modules/generating-block-content.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Generating block content

**Drupal hook described: *hook_block_view()***  
**Main functions described: *user_access(), l(), theme()***

The next step in this tutorial is to take the data we generated in our custom function and turn it into content for the block. We will do this using `hook_block_view`. This function returns two values, 'subject', which is the title of the block, and 'content', which is self-documenting. Once again, we will use a switch structure. This structure allows for additional blocks to be added in the future if needed. The \$delta parameter tells the function which block is being requested.

### Access check

Here's the first part of the code:

``` php
function current_posts_block_view($delta = '') {
  switch ($delta) {
    case 'current_posts':
      $block['subject'] = t('Current posts');
      if (user_access('access content')) {
      // Retrieve and process data here.
   }
```

Best practice dictates that information displayed to the user be assessed against that user's permissions. Here we implement the most basic of checks, 'access content'. You can use any permission here that Drupal supplies, or even create your own. For a list of permission names, go to *People \> List (tab)* (or `http://example.com/admin/people`). In the permission dropdown there, you will find a list of the machine readable names that you can use in your code. This list will include all permissions active on your site, including those created by contrib modules. The names in the *Permissions* tab (`http://example.com/admin/people/permissions`) are not the machine readable names.

Another way to find permissions set in core modules is through the [API reference](http://api.drupal.org/api/drupal). Enter the module name followed by `_permission`, for example, `node_permission`. You'll get a list of all the permissions that node defines. Knowing which one to use might be a bit tricky. For example, the `access content` permission we use here is actually defined in the node module, not the block module.

### Coding the data as links

Here's the next bit of code:

``` php
       // Use our custom function to retrieve data.
        $result = current_posts_contents();
        // Array to contain items for the block to render.
        $items = array();
        // Iterate over the result set and format as links.
        foreach ($result as $node) {
          $items[] = array(
            'data' => l($node->title, 'node/' . $node->nid),
          );
        }
```

First, we use our custom function to save the data into the `$result` variable. The `$items` variable gives us a place to store the processed data. We then iterate over the result set, processing each item and formatting it as a link.

Notice the actual link is created by the [l()](http://api.drupal.org/api/drupal/includes--common.inc/function/l/7) function. (That's a lower case 'L'.) The first parameter sets the link text, in this case the node's title. The second parameter is the actual link path. The path to any node is always "node/#", where \# is the ID number of the node. `l()` uses this path to generate appropriate links, adjusting the URL to the installation's URL configuration.

### Theming the data

Drupal's presentation layer is a pluggable system known as the theme layer. Each theme can take control of most of Drupal's output, and has complete control over the CSS. Theming in Drupal is a vast subject with entire books devoted to the subject. Here we will merely touch the surface with a theme function. Later in the tutorial, we will delve into render arrays.

Here's the last section of code for `current_posts_block_view`:

``` php
        // No content in the last week.
        if (empty($items)) {
          $block['content'] = t('No posts available.');  
        }
        else {
          //Pass data through theme function.
          $block['content'] = theme('item_list', array(
            'items' => $items));
        }
      }
    return $block;
  }
 
}
```

First, we allow for the possibility of no content that fits our criteria. Your module's block should appear whether or not new content from the last week exists on your site.

If the `$items` variable contains data, it goes to the `theme()` function. The first argument of this function is the theme hook. Drupal includes many default theme hooks you can use with this function; see [Default theme implementations](http://api.drupal.org/api/drupal/modules--system--theme.api.php/group/themeable/7) for the complete list. We have chosen to theme our data as an unordered list, the [theme_item_list](http://api.drupal.org/api/drupal/includes--theme.inc/function/theme_item_list/7) theme hook. The second argument passes the content to be themed.

You may wonder why the code takes this form if the function is `theme_item_list`. `theme()` looks for a theme function called `theme_hookname`, where 'hookname' is the first argument, in this case, `item_list`. In other words, the second part of the hook name becomes the first argument when the function is called, telling the theme function which of its default versions to use.

### The whole function

``` php
/**
 * Implements hook_block_view().
 * 
 * Prepares the contents of the block.
 */
function current_posts_block_view($delta = '') {
  switch ($delta) {
    case 'current_posts':
      $block['subject'] = t('Current posts');
      if (user_access('access content')) {
        // Use our custom function to retrieve data.
        $result = current_posts_contents();
        // Array to contain items for the block to render.
        $items = array();
        // Iterate over the resultset and format as links.
        foreach ($result as $node) {
          $items[] = array(
            'data' => l($node->title, 'node/' . $node->nid),
          ); 
        }
       // No content in the last week.
        if (empty($items)) {
          $block['content'] = t('No posts available.');  
        } 
        else {
          // Pass data through theme function.
          $block['content'] = theme('item_list', array(
            'items' => $items));
        }
      }
    return $block;
  }
  
}
```

(Remember not to include the opening or closing PHP tags when you add this section.)

### See also

- [user_access()](http://api.drupal.org/api/drupal/modules--user--user.module/function/user_access/7)
- [hook_block_view()](http://api.drupal.org/api/drupal/modules--block--block.api.php/function/hook_block_view/7)
- [API reference](http://api.drupal.org/api/drupal)
- [l()](http://api.drupal.org/api/drupal/includes--common.inc/function/l/7)
- [theme()](http://api.drupal.org/api/drupal/includes--theme.inc/function/theme/7)
- [Default theme implementations](http://api.drupal.org/api/drupal/modules--system--theme.api.php/group/themeable/7)
