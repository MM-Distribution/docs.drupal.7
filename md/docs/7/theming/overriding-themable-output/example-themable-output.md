---
title: "Example: Themable output"
source_url: "https://www.drupal.org/docs/7/theming/overriding-themable-output/example-themable-output"
page_type: page
last_updated: "Last updated on 27 September 2016"
published: "2009-09-19T00:16:06+00:00"
modified: "2016-09-27T00:32:05+00:00"
breadcrumb: ["Drupal 7", "Theming Drupal 7", "Overriding themable output"]
fetched: "2026-10-21T08:19:53Z"
raw: "raw/docs/7/theming/overriding-themable-output/example-themable-output.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Example: Themable output

## How to customize HTML for the search block

This example explains how to customize the HTML for the default search block. The default search block is created by the search module.

Using the .tpl.php file method:

1.  From your site root, go into the modules/search folder
2.  Copy modules/search/search-block-form.tpl.php to sites/all/themes/yourtheme/search-block-form.tpl.php

You can now edit the version of the file that is in your theme folder.

search-block-form.tpl.php has this code:

### Drupal 7.x:

``` php
<div class="container-inline">
  <?php if (empty($variables['form']['#block']->subject)): ?>
    <h2 class="element-invisible"><?php print t('Search form'); ?></h2>
  <?php endif; ?>
  <?php print $search_form; ?>
</div>
```

This example removes the simple form print statement there, and creates new HTML output, following the documentation at the top of the file:

 

### Drupal 7.x:

``` php
<div class="container-inline">
  <?php if (empty($variables['form']['#block']->subject)): ?>
    <h2 class="element-invisible"><?php print t('Search form'); ?></h2>
  <?php endif; ?>
 <?php $search['search_block_form'] = '
    <div class="form-item" id="edit-search-block-form-1-wrapper">
     <input type="text" maxlength="128" name="search_block_form" id="edit-search-block-form-1" size="15" value="" title="Enter the terms you wish to search for." class="form-text" />
     <br />
     <label for="edit-search-block-form-1">Search posts and comments</label>
    </div>'; 
   print $search['search_block_form'];
   print $search['actions'];
   print $search['hidden']; 
    ?>
</div>
```

The HTML was simply grabbed from the original output by using view source (or Firebug), and then the elements can be re-arranged. You could add in other tags or whatever content you need. Add a little CSS to the mix and just about anything is possible. Don't change the names and IDs of the form elements, otherwise the form won't be processed correctly.

The variables that are being printed in this modified code are explained in the original search-block-form.tpl.php file (located in your_site_root/modules/search/). Here you can see which keys are available in the comments:

Default keys within \$search:

 

### Drupal 7.x:

- \$search\['search_block_form'\]: Text input area wrapped in a div.
- \$search\['actions'\]: Rendered form buttons.
- \$search\['hidden'\]: Hidden form elements. Used to validate forms when submitted.
