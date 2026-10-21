---
title: "Declaring the block"
source_url: "https://www.drupal.org/docs/7/creating-custom-modules/declaring-the-block"
page_type: page
last_updated: "Last updated on 14 August 2017"
published: "2011-03-24T19:13:55+00:00"
modified: "2017-08-14T19:27:40+00:00"
breadcrumb: ["Drupal 7", "Creating custom modules in Drupal 7"]
fetched: "2026-10-21T07:22:27Z"
raw: "raw/docs/7/creating-custom-modules/declaring-the-block.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Declaring the block

**Drupal hook described: *hook_block_info()***

Modules are created to do all sorts of things: create blocks (abbreviated content that often appears on the right or left side of multiple pages), create special content types (for full page content - such as the content you are reading right now), track back-end information, and more. You may hear the term 'block modules' used to describe modules that primarily create block content (such as the menu module), or 'node modules' used to describe modules that primarily generate full page content (such as the blog and forum modules). At this stage, this module is a 'block module', because it generates a block.

In Drupal 7, there are at least eight block hooks. For the purposes of this module, we will use two of them. The first is `hook_block_info()`. As you might suspect, this hook tells Drupal what block(s) your module creates. We will use this hook to define a block that will eventually display the most recent posts. You can use a given hook exactly once in any module, so this hook must declare all blocks the module needs. For this module, a single block is all we need.

To use this hook to define our block, go to your `current_posts.module` file and create the function `current_posts_block_info()` as follows:

``` php
/**
 * Implements hook_block_info().
 */
function current_posts_block_info() {
  $blocks['current_posts'] = array(
    // The name that will appear in the block list.
    'info' => t('Current posts'),
    // Default setting.
    'cache' => DRUPAL_CACHE_PER_ROLE,
  );
  return $blocks;
}
```

(Remember not to include the closing `?>` in your code.)

The doc block simply identifies the hook. For such a straightforward implementation, that is sufficient. Anyone reading the code can easily go to the API and call up the hook for further information.

The return value takes the form of an associative array. Pay special attention to this array structure, as it is Drupal's preferred programming structure. Arrays in PHP are well supported and very fast, and Drupal makes extensive use of them.

The only required value is 'info'. `hook_block_info` can also specify configuration settings. Here we set the cache to the default. See [hook_block_info](http://api.drupal.org/api/drupal/modules--block--block.api.php/function/hook_block_info/7) for a complete list of settings available.

Don't forget the final return statement.

### Check

At this point, go to *Modules*, click the checkbox to enable *Current Posts*, and save your configuration. Next, navigate to *Structure \> Blocks*. Scroll down to the bottom of the list. Among the disabled blocks, you should find the name, 'Current posts'. Return to *Modules*, disable your module and save. **Important**: Be sure you disable your module and save, or new partial code in your module could break your site.

### Visibility

To change the visibility of the block, use 'visibility' and 'pages'.

This example enable the block "Example : empty block" on a listed pages (BLOCK_VISIBILITY_LISTED) with the path "node/\*" :

``` php
$blocks['example_empty'] = array(
    'info' => t('Example: empty block'),
    'status' => TRUE,
    'region' => 'Content',
    'visibility' => BLOCK_VISIBILITY_LISTED,
    'pages' => 'node/*',
);
```

### 

On admin, go to "structure/block/manage/block_example/example_empty/configure", there is "node/\*" in the visibility settings :

![](/files/Capture%20d%E2%80%99e%CC%81cran%202017-08-14%20a%CC%80%2020.00.48.png)

### See Also

- [hook_block_info](http://api.drupal.org/api/drupal/modules--block--block.api.php/function/hook_block_info/7)
