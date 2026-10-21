---
title: "Theming the page"
source_url: "https://www.drupal.org/docs/7/creating-custom-modules/theming-the-page"
page_type: page
last_updated: "Last updated on 22 December 2016"
published: "2011-04-06T14:23:50+00:00"
modified: "2016-12-22T06:21:33+00:00"
breadcrumb: ["Drupal 7", "Creating custom modules in Drupal 7"]
fetched: "2026-10-21T07:24:47Z"
raw: "raw/docs/7/creating-custom-modules/theming-the-page.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Theming the page

**Main topic described: *Render API***

Now we will write the page function we established in `current_posts_menu()`. Here's the first part of the code:

``` php
/**
 * Custom page callback function, declared in current_posts_menu().
 */
function _current_posts_page() {
  $result = current_posts_contents('page');
  //Array to contain items for the page to render.
  $items = array();
  //Iterate over the resultset and format as links.
  foreach ($result as $node) {
    $items[] = array(
    'data' => l($node->title, 'node/' . $node->nid),
    ); 
  }
```

Looks familiar, doesn't it? We call the query function, with the 'page' argument, to retrieve all the relevant posts from the database. Then we iterate over the resultset to create links for each post.

### Render array

Now we'll delve a little further into the theming system and format our output as a render array. Whenever possible in Drupal 7, the data used to build a page is kept as structured arrays until the rendering stage in the theming system. This allows your module and other modules to treat the content as data for as long as possible in the page generation process. See [Render Arrays in Drupal 7](http://drupal.org/node/930760) for a full explanation. The next piece of code contains our first render array:

``` php
  if (empty($items)) { //No content in the last week.
    $page_array['current_posts_arguments'] = array(
      //Title serves as page subtitle
      '#title' => t('All posts from the last week'),
      '#markup' => t('No posts available.'),
    );
    return $page_array;  
  } 
```

This code serves the same function as the section of `current_posts_block_view()` that allowed for the absence of data. We create an array variable `$page_array` to hold the render arrays. The name of the variable is irrelevant as long as it doesn't conflict with other variable names. For the key, we follow Drupal naming conventions and begin with the module name.

The subarray is formatted as a render array, with keys preceded by a hash mark (#), using properties established in the Render API. `#title` serves as the title of the render array content. The page title was determined in `current_posts_menu()`, so visually this title functions as a subtitle. `#markup` is the simplest property, providing a simple markup string. We could include HTML if we needed it. Both are wrapped in `t()` for translation.

You may have noticed how similar this looks to the configuration form we created, with keys preceded by hash marks. The Form API has always used Render API properties, but they've traditionally not been documented as such. This changes with Drupal 7, and you can find many of these properties documented in the [Form API Reference](http://api.drupal.org/api/drupal/developer--topics--forms_api_reference.html/7#elements).

### Theme hook suggestion

Here's the last part of the code:

``` php
  else {
    $page_array['current_posts_arguments'] = array(
      '#title' => t('All posts from the last week'),
      '#items' => $items,
      //Theme hook with suggestion.  
      '#theme' => 'item_list__current_posts',
    );
    return $page_array;
  }
}
```

Again, we have the `#title` property. The next two lines are the render array approach to calling `theme_item_list()`, the same function we called in `current_posts_block_view()` with the following code: ` theme('item_list', array('items' => $items));`. The variable `$items`, with its array of links, are assigned to the items property, and the theme property is assigned its item list default theme hook.

There is a notable difference. We have added two underscores and our module name to the item list theme hook call. By doing this, we have given more flexibility to any themer using the module. If we use only the default theme hook, any change a themer makes to that default will appear wherever the hook is used, not just on our item list. With this addition, a theme can specify markup for our output only.

The two underscores tell Drupal that this is a theme hook suggestion, using a pattern that Drupal recognizes. You can write as many suggestions as you like. If you need more, add additional suggestions preceded by double underscores. Drupal will start looking for an implementation of the suggestion on the right, then continue checking right to left until it finds an actual implementation. This module doesn't implement the suggestion, so the look of the output won't change. But the option is now available.

### Check

Time to check your work. Enable your module and follow the link on the 'Navigation' menu. Be sure to log out and view the site as an anonymous user, or a user without the custom permission. The link should not appear on the menu.

### See also

- [Render Arrays in Drupal 7](http://drupal.org/node/930760)
- [Form API Reference](http://api.drupal.org/api/drupal/developer--topics--forms_api_reference.html/7#elements)
- [Using the theme layer](http://drupal.org/node/933976)
