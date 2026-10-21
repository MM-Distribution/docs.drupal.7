---
title: "Adding a 'More' link"
source_url: "https://www.drupal.org/docs/7/creating-custom-modules/adding-a-more-link"
page_type: page
last_updated: "Last updated on 2 March 2017"
published: "2011-04-15T11:58:07+00:00"
modified: "2017-03-02T05:34:16+00:00"
breadcrumb: ["Drupal 7", "Creating custom modules in Drupal 7"]
fetched: "2026-10-21T07:25:37Z"
raw: "raw/docs/7/creating-custom-modules/adding-a-more-link.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Adding a 'More' link

**Main topic described: *Block system, Render arrays, Menu system***  
**Main function described: *drupal_set_title()***

With this last addition to the module, we will pull together what you have learned about the block system, the menu system, and render arrays, and throw in a workaround for a minor bug in a past version of Drupal 7.

It may have occurred to you that access to this page belongs not in the 'Navigation' menu, but through a 'More' link at the bottom of the 'Current posts' block. That was the plan all along, but we started with a menu link to show how it works.

If you looked at the [Default theme implementations](http://api.drupal.org/api/drupal/modules--system--theme.api.php/group/themeable/7) referenced back in [Generating block content](http://drupal.org/node/1104498), you may have noticed the [theme_more_link](http://api.drupal.org/api/drupal/includes--theme.inc/function/theme_more_link/7) theme hook. We'll use that, along with a theme hook suggestion, to theme the 'More' link for our block.

### Child render elements

We'll start by converting the call to `theme_item_list` into a render array as we did in the page function. We'll also make it a child of `block['content']` to allow for the 'More' link as a sibling. Here's the revised code for the last section of `current_posts_block_view`:

``` php
else {
  //Pass data through theme function.
  $block['content']['posts'] = array(
    '#theme' => 'item_list__current_posts__block',
    '#items' => $items,
  ); 
```

Remember not to include the PHP markers in your code.

We move the item list code to `$block['content']['posts']`, making it a child element. You can name the child element whatever you like, as long as it doesn't start with a hash mark (#). We convert the call to `theme_item_list` into a render array, then add the `__current_posts` theme hook suggestion. This we follow with a second suggestion in case a themer wants to render the lists in the block and page differently.

Here's new code for the 'More' link to add directly after the last listing:

``` php
  //Add a link to the page for more entries.
  $block['content']['more'] = array(
    '#theme' => 'more_link__current_posts',
    '#url' => 'current_posts',
    '#title' => t('See the full list of current posts.'),
  );
}
```

Here we make the 'More' link a sibling to the `posts` array and provide the two parameters this theme hook requires, the path and title. The title provides text which will appear as a tooltip when the mouse hovers over the link. We give this theme hook a suggestion as well.

### Edit `current_posts_menu()`

At this point, we have links to the page both in our block and in the 'Navigation' menu. We don't want a link in the menu, so we'll edit `current_posts_menu()` to take it off. All you need to do is change the `type` attribute for the page item. Delete `MENU_NORMAL_ITEM` and replace it with `MENU_CALLBACK`. This type provides a path and attributes only, with no menu link. Should you have your module enabled, you'll need to disable then re-enable it for this change to take effect.

### Page title fix

Enable your module and follow the 'More' link in the block, then note the page title. If it is 'Home', it is likely that you are using an older version of Drupal 7. To ensure our module works on installations of the earlier version of Drupal 7 before this bug was patched, let's implement a workaround.

The workaround is to use the function `drupal_set_title()`. Add the following to the beginning of your `_current_posts_page()` function:

``` php
  drupal_set_title('Current posts');
```

With this addition, you can be sure the correct title will appear on the page, no matter which version of Drupal 7 your module is installed in.

### Check

Check your module functionality one final time. If you have been following along, the last thing to check is the corrected page title, 'Current posts'. If you have problems getting your code additions to appear, try clearing the caches or disabling then re-enabling your module.

### View the code

You can view all the code for the `.module` file here: [current_posts.module](http://drupalcode.org/sandbox/jn2/1117260.git/blob/b2104cb366f462cc62c602c70a1f11585a527c0b:/current_posts.module)

### See also

- [Examples for developers](http://drupal.org/project/examples), the block, menu, and page examples (If you don't see a Drupal 7 release for download, git clone master for the latest versions.)
- [Default theme implementations](http://api.drupal.org/api/drupal/modules--system--theme.api.php/group/themeable/7)
- [theme_more_link](http://api.drupal.org/api/drupal/includes--theme.inc/function/theme_more_link/7)
- [drupal_set_title()](http://api.drupal.org/api/drupal/includes--bootstrap.inc/function/drupal_set_title/7)
