---
title: "Assigning content to regions"
source_url: "https://www.drupal.org/docs/7/theming/assigning-content-to-regions"
page_type: page
last_updated: "Last updated on 8 November 2018"
published: "2007-08-28T16:51:53+00:00"
modified: "2018-11-08T06:07:04+00:00"
breadcrumb: ["Drupal 7", "Theming Drupal 7"]
fetched: "2026-10-21T06:01:42Z"
raw: "raw/docs/7/theming/assigning-content-to-regions.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Assigning content to regions

If none is defined, the following values are assumed in Drupal 6.

``` php
regions[left] = Left sidebar
regions[right] = Right sidebar
regions[content] = Content
regions[header] = Header
regions[footer] = Footer
  
```

Drupal 7 adds Highlighted and Help as default regions. By default, the textual content of the Help region is the same as the \$help variable was in page.tpl.php for Drupal 6. The "machine" readable names of the sidebars have also changed names.

``` php
regions[sidebar_first] = Left sidebar
regions[sidebar_second] = Right sidebar
regions[content] = Content
regions[header] = Header
regions[footer] = Footer
regions[highlighted] = Highlighted
regions[help] = Help
```

Drupal 7 Bartik theme has following default regions -

``` php
regions[header] = Header
regions[help] = Help
regions[page_top] = Page top
regions[page_bottom] = Page bottom
regions[highlighted] = Highlighted

regions[featured] = Featured
regions[content] = Content
regions[sidebar_first] = Sidebar first
regions[sidebar_second] = Sidebar second

regions[triptych_first] = Triptych first
regions[triptych_middle] = Triptych middle
regions[triptych_last] = Triptych last

regions[footer_firstcolumn] = Footer first column
regions[footer_secondcolumn] = Footer second column
regions[footer_thirdcolumn] = Footer third column
regions[footer_fourthcolumn] = Footer fourth column
regions[footer] = Footer
```

Keep in mind that the internal names are converted into region variables inside the "page.tpl.php" template automatically. In the above example, the `[header]` region will output all the blocks assigned to it through the `$header` variable in Drupal 6, or `$page['header']` in Drupal 7. There are a few restrictions on naming [variables in PHP](http://us3.php.net/variables), so make sure the internal/machine names conform to the same restrictions. Basically, your internal region names can only contain alphanumeric characters and underscores, and they should start with a letter.

The human readable names outside the square brackets are used for labeling the region in the block administration page located at "Administer \> Site building \> Blocks" and in Drupal 7 the block administration page is located at "Administration \> Structure \> Blocks" .

*Here is the block administration table for Garland:*  
![Garland block configuration example](/files/block_config_garland.png)

*Drupal 7 - Block administration table for Bartik:*  
![Bartik block configuration example](/files/blocks%20in%20D7.png)

*A few notes:*

- *There are [template (.tpl.php) files](/node/190815#block-tpl) available for rendering individual blocks.*
- *Adding a custom region prevents the defaults from being used. If you want to keep the defaults in addition to custom regions, manually add in the defaults.*
- *If you define custom regions, it is important to remember that you need to include the content, help, page_top and page_bottom regions in your set of regions. The page_top and page_bottom regions are hidden, which means they will not show up on the blocks administration interface.*
- *The order in which the regions are defined will be reflected in the block configuration table. Garland, for example, uses the default regions. Notice the order of the regions listed in the image.*
- *The content of the .info file is cached in the database, so altering it will not be noticed by Drupal. (Do not confuse this with the [theme registry](/node/173880#theme-registry).) To learn how to clear it, check out the options in [Clearing the theme cache](http://drupal.org/node/337176).*

*Upgrade notes:*

- *The `$footer_message` region variable has been removed in Drupal 7.*

**The \$content region**  
In Drupal 6 and before the \$content variable in page.tpl.php contained the main page content appended with the blocks positioned into the content region (if you had that region defined).

In Drupal 7, \$content became a full region and is now mandatory in all themes. This new requirement was set up so that when enabling new themes, Drupal knows where to put the main page content by default.

In Drupal 6, it was only possible to put blocks after the main page content in this region. The only way to put blocks before the main page content was to define a specific region for that purpose. Drupal 7 now makes the main page content its own block. This makes it possible to put blocks before or after the main page content in the region without hacking in a new region.

**Manually assigning content to regions:**

Content can be manually assigned to regions with [`drupal_set_content()`](http://api.drupal.org/api/drupal/includes--common.inc/function/drupal_set_content/6) in Drupal 6 or [`drupal_add_region_content`](http://api.drupal.org/api/drupal/includes--common.inc/function/drupal_add_region_content/7) for Drupal 7. For example in Drupal 6, `drupal_set_content('header', 'Welcome!')` would assign the text *'Welcome!'* to the header region.

Here is a more useful example for building a summary of all the comments into the "right" region. *Rename the "drop" prefix with the name of your theme. More information on [preprocessors is available](/node/223430).*

``` php
function drop_preprocess_comment(&$variables) {
  
  // Setup a few variables.
  $comment = $variables['comment'];
  $title = l(
    $comment->subject,
    comment_node_url(),
    array('fragment' => "comment-$comment->cid")
  );
  $new_marker = $comment->new ? t('new') : '';
  $by_line = t('by') .' '. theme('username', $comment);

  // Form the markup.
  $summary = '';
  $summary .= '' . "$title $new_marker"; $summary .= '' . "$by_line"; $summary .= '';

  // Set the comment into the right region.
  drupal_set_content('right', $summary);
}

```

*Note that setting content through this function should happen before the block regions are retrieved and that is done with a call from [template_preprocess_page](http://api.drupal.org/api/function/template_preprocess_page/6) \> [theme_blocks](http://api.drupal.org/api/function/theme_blocks/6) \> [drupal_get_content](http://api.drupal.org/api/function/drupal_get_content/6).*
