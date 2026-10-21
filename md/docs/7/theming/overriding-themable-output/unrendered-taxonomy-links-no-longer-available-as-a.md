---
title: "Unrendered taxonomy links no longer available as a separate variable in node.tpl.php files"
source_url: "https://www.drupal.org/docs/7/theming/overriding-themable-output/unrendered-taxonomy-links-no-longer-available-as-a"
page_type: page
last_updated: "Last updated on 10 September 2016"
published: "2010-04-22T18:56:55+00:00"
modified: "2016-09-10T18:36:00+00:00"
breadcrumb: ["Drupal 7", "Theming Drupal 7", "Overriding themable output"]
fetched: "2026-10-21T08:21:27Z"
raw: "raw/docs/7/theming/overriding-themable-output/unrendered-taxonomy-links-no-longer-available-as-a.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Unrendered taxonomy links no longer available as a separate variable in node.tpl.php files

In Drupal 6, node.tpl.php files could use the \$taxonomy variable if they needed access to an array of unrendered taxonomy links associated with the current node.

In Drupal 7, this is no longer the case. Instead, all links have been moved into the \$node object. The array of unrendered taxonomy links can now be found in \$node-\>content\['links'\]\['terms'\]\['#value'\] instead. (Note that this array should be used with caution, since the text contained within it has not been escaped to prevent XSS attacks.)

Rendered taxonomy links are not affected; node.tpl.php files can continue to access these via the \$terms variable, as before. In many cases, the \$terms variable is what you want to use in your theme anyway, and you might be able to replace references to \$taxonomy with it, as in the following example:

### Drupal 6.x

``` php
<?php if ($taxonomy): ?>
  <div class="terms"><?php print $terms ?></div>
<?php endif;?>
```

### Drupal 7.x

``` php
<?php if ($terms): ?>
  <div class="terms"><?php print $terms ?></div>
<?php endif;?>
```
