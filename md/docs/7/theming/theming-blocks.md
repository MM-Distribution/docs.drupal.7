---
title: "Theming blocks"
source_url: "https://www.drupal.org/docs/7/theming/theming-blocks"
page_type: page
last_updated: "Last updated on 12 June 2018"
published: "2006-12-20T00:04:49+00:00"
modified: "2018-06-12T16:43:36+00:00"
breadcrumb: ["Drupal 7", "Theming Drupal 7"]
fetched: "2026-10-21T06:05:19Z"
raw: "raw/docs/7/theming/theming-blocks.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Theming blocks

Designers can create multiple tpl.php files for blocks based on the specific block, the module that created the block, or the region that the block appears in.

## Template suggestions

### Drupal 7

In Drupal 7 template files are searched in the following order:

- block--block--\[block-id\].tpl.php
- block--\[module\]--\[delta\].tpl.php
- block--\[module\].tpl.php
- block--\[region\].tpl.php
- block.tpl.php

If the block delta key uses a hyphen, (-), replace this with an underscore (\_).

Adding some custom code you may even use the block description as a template suggestion: [Add meaningful template suggestions for blocks (D7)](#snippet)

[Drupal 7 Template (Theme Hook) Suggestions](/node/1089656)

## Finding module and delta

You can find the block's module and delta by looking at the html source of a page: each block's main DIV has the following classes and IDs:

``` php
<div class="block block-{module}" id="block-{module}-{delta}"> 
```

Note that custom blocks created in the admin UI count as coming from block.module, so their template is 'block-block-\[delta\]'.

## Styling with CSS

The classes and IDs also let you apply CSS rules to blocks selectively: all blocks, all blocks from a particular module, or just one block. (To style blocks by region, use the DIV that wraps an entire region in your selector.)

Note that the delta is usually a number: each module numbers the blocks it provides, starting at 0. In some cases, the delta can also be a name: eg to style blocks created with the Views module, use block-views-\[name of your block\].tpl.php.

### CSS styling in Drupal 7 & Ajax

Targeting a block purely by its ID is not always reliable in Drupal 7. If Ajax is used to reload portions of your page that include blocks, the IDs of the loaded blocks will get a counter appended to them. For example, an ID of 'block-masquerade-masquerade' will become 'block-masquerade-masquerade--2', which will break your theming. See [drupal_html_id()](http://api.drupal.org/api/drupal/includes!common.inc/function/drupal_html_id/7) for details.

## <span id="snippet">Add meaningful template suggestions for blocks (D7)</span>

Add this snippet to your theme's template.php file. Really useful for theming, particularly the block description one. The available templates for any block will be:

- block--REGION.tpl.php
- block--MODULE.tpl.php
- block--DELTA.tpl.php
- block--DESCRIPTION.tpl.php

<!-- -->

``` php
function MYTHEME_preprocess_block(&$variables) {
  $variables['theme_hook_suggestions'][] = 'block__' . $variables['block']->region;
  $variables['theme_hook_suggestions'][] = 'block__' . $variables['block']->module; 
  $variables['theme_hook_suggestions'][] = 'block__' . $variables['block']->delta;

  // Add block description as template suggestion
  $block = block_custom_block_get($variables['block']->delta);

  // Transform block description to a valid machine name
  if (!empty($block['info'])) { 
    setlocale(LC_ALL, 'en_US');

    // required for iconv()
    $variables['theme_hook_suggestions'][] = 'block__' . str_replace(' ', '_', strtolower(iconv('UTF-8', 'ASCII//TRANSLIT', $block['info'])));
  }
} 
```
