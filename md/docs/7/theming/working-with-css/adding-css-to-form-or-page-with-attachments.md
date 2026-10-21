---
title: "Adding CSS to form or page with attachments"
source_url: "https://www.drupal.org/docs/7/theming/working-with-css/adding-css-to-form-or-page-with-attachments"
page_type: page
last_updated: "Last updated on 11 March 2021"
published: "2014-06-03T04:20:07+00:00"
modified: "2021-03-11T21:35:31+00:00"
breadcrumb: ["Drupal 7", "Theming Drupal 7", "Working with CSS"]
fetched: "2026-10-21T08:14:43Z"
raw: "raw/docs/7/theming/working-with-css/adding-css-to-form-or-page-with-attachments.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Adding CSS to form or page with attachments

On the [previous page](https://www.drupal.org/docs/7/theming/working-with-css/adding-style-sheets-from-info-files) we learned how to add css using the [.info](https://drupal.org/node/171205) file and the [drupal_add_css()](https://api.drupal.org/api/drupal/includes!common.inc/function/drupal_add_css/7 "drupal_add_css") function. You will recall that the major advantage to drupal_add_css() is that you can include CSS only on specific pages to reduce your page load. Unfortunately, if you have a lot of conditional rules for CSS inclusion, this can lead to complex logic in your template.php or in a hook_init() implementation. Thankfully, there's an easier way!

## Adding css using \#attached attribute

Drupal 7 introduced render arrays to improve the separation of content and markup. One of the elements of a render array is the [\#attached](https://api.drupal.org/api/drupal/developer%21topics%21forms_api_reference.html/7#attached) attribute. This attribute allows you to declaratively state what CSS needs to be included whenever that array is rendered into HTML.

### Adding CSS to a cached block

If you add css using [drupal_add_css()](https://api.drupal.org/api/drupal/includes!common.inc/function/drupal_add_css/7 "drupal_add_css") inside [hook_block_view()](https://api.drupal.org/api/drupal/modules!block!block.api.php/function/hook_block_view/7 "hook_block_view"), and then enable block cache, you will discover that the css will be included when the block is first rendered, but not if the block is cached. This is because the drupal_add_css() call only happens when the hook_block_view() function is called. Using \#attached guarantees that the needed resource will be included as part of the rendering process even if the block is being pulled from cache. Under the hood, this happens via a call to drupal_process_attached(), which in turn calls drupal_add_css() for you.

**Moving from drupal_add_css() to \#attached**

Initially, the code below will work, but if you enable block caching, or if you have defined your block to be cached in [hook_block_info()](https://api.drupal.org/api/drupal/modules%21block%21block.api.php/function/hook_block_info/7), the `my.css` will fail to be included.

``` php
function foo_block_view($delta = '') {
  if ($delta === 'foo_delta') {
    drupal_add_css('path/to/my.css');
    $block = array(
      'subject' => t('Foo title'),
      'content' => t('Lorem ipsum text.'),
    );
    return $block;
  }
}
```

Changing the code to be cache-friendly is as simple as removing the call to drupal_add_css() and adding the \#attached property with the resource included in the css property of the array you set as its value.

``` php
function foo_block_view($delta = '') {
  if ($delta === 'foo_delta') {
    $block = array(
      'subject' => t('Foo title'),
      'content' => array(
        '#markup' => '<p>' . t('Lorem ipsum text.') . '</p>',
        '#attached' => array(
          'css' => array(
            'path/to/my.css'
          ),
        ),
      ),
    );
    return $block;
  }
} 
```

You can add internal, external and inline css using this attribute.

**We can also add css to the page in a similar way.**

``` php
$content = array();
$content['#attached']['css'] = array(
  'path/to/my.css' => array(
    'group' => CSS_AGGREGATE_THEME,
    'weight' => 999
  ),
);
return $content; 
```
