---
title: "Checking if a region is occupied"
source_url: "https://www.drupal.org/docs/7/theming/checking-if-a-region-is-occupied"
page_type: page
last_updated: "Last updated on 21 May 2023"
published: "2009-07-13T11:50:45+00:00"
modified: "2023-05-21T11:12:37+00:00"
breadcrumb: ["Drupal 7", "Theming Drupal 7"]
fetched: "2026-10-21T06:01:58Z"
raw: "raw/docs/7/theming/checking-if-a-region-is-occupied.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Checking if a region is occupied

While theming page.tpl.php, It's possible to check to see whether a region is empty, by checking the content of the relevant variable which contains the region's contents.

**Example:**

``` php
  if($page['sidebar_first']) {
    // do something
  }
```

**However, region variables haven't been defined for templates at the block, node and view levels.**

To deal with this case, part of the [block.module](http://api.drupal.org/api/file/modules/block/block.module/6) code could be adapted to create a function which can be inserted in your theme `template.php` file.

The function takes one parameter (a region name), and returns 1 if the region is empty or 0 if the region is occupied. The function examines the block visibility setting *for the current path* to work out if the region is occupied.

``` php
function region_empty($test_region) {
  /* Check to see if a region is occupied
   * returns 1 if it's empty
   */

  $test_empty = 1;

  $result = db_query_range('SELECT n.pages, n.visibility FROM {blocks} n WHERE n.region="%s" AND n.theme="%s"', $test_region, $GLOBALS['theme'], 0, 10);
  if (count($result) > 0) {
    while ($node = db_fetch_object($result))
    {

      if ($node->visibility < 2) {
        $path = drupal_get_path_alias($_GET['q']);

        // Compare with the internal and path alias (if any).
        $page_match = drupal_match_path($path, $node->pages);
        if ($path != $_GET['q']) {
          $page_match = $page_match || drupal_match_path($_GET['q'], $node->pages);
        }
        // When $block->visibility has a value of 0, the block is displayed on
        // all pages except those listed in $block->pages. When set to 1, it
        // is displayed only on those pages listed in $block->pages.
        $page_match = !($node->visibility xor $page_match);
      } else {
        $page_match = drupal_eval($block->pages);
      }

      if ($page_match)
        $test_empty = 0;
    }
  }
  return $test_empty;
}
```
