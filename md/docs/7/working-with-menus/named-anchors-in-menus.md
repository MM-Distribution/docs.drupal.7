---
title: "Named anchors in menus"
source_url: "https://www.drupal.org/docs/7/working-with-menus/named-anchors-in-menus"
page_type: page
last_updated: "Last updated on 23 December 2016"
published: "2007-01-04T15:23:51+00:00"
modified: "2016-12-23T08:21:28+00:00"
breadcrumb: ["Drupal 7", "Working with menus in Drupal 7"]
fetched: "2026-10-21T07:20:23Z"
raw: "raw/docs/7/working-with-menus/named-anchors-in-menus.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Named anchors in menus

In Drupal 7, a link to a named anchor or named region on the page can be created in the Menu system. Go to admin/structure/menu/manage/navigation/add. To link to an anchor on just one of your site's pages, set the path to the full url of the page and include the anchor reference, for example:

`http://example.com/node/5#anchor`

For a link to an anchor on the current page (that is, a link that works on every page the menu link is displayed on), you can use the [Menu token](https://drupal.org/project/menu_token) module. Once that is installed together with the modules that it requires, you will be able to set the link path to:

`[current-page:url]#anchor`  
or  
`node/[node:nid]#anchor`

In earlier versions of Drupal, users who have tried using “named anchors,” also known as “jump links,” in the menu system can run into problems with them not working. A named anchor will look like this:  
`<a name="anchor"></a>`

The expected behavior is that when a link that points to this named anchor is clicked, the user’s browser should jump to the anchor tag on the html page, making it appear at the top of the user’s browser window.

This desired behavior can be accomplished by adding the following function to your theme’s template.php file:

``` php
function phptemplate_menu_item_link($item, $link_item) {
  // Convert anchors in path to proper fragment
  $path = explode('#', $link_item['path'], 2);
  $fragment = !empty($path[1]) ? $path[1] : NULL;
  $path = $path[0];
  return l(
            $item['title'],
            $path,
            !empty($item['description']) ? array('title' => $item['description']) : array(),
            !empty($item['query']) ? $item['query'] : NULL,
            $fragment,
            FALSE,
            FALSE
          );
}
```
