---
title: "How to add jQuery UI libraries to a page"
source_url: "https://www.drupal.org/docs/7/howtos/how-to-add-jquery-ui-libraries-to-a-page"
page_type: page
last_updated: "Last updated on 1 November 2016"
published: "2014-03-20T03:05:00+00:00"
modified: "2016-11-01T16:31:17+00:00"
breadcrumb: ["Drupal 7", "Site building and development HowTos for Drupal 7"]
fetched: "2026-10-21T08:06:12Z"
raw: "raw/docs/7/howtos/how-to-add-jquery-ui-libraries-to-a-page.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# How to add jQuery UI libraries to a page

Drupal 7 ships with jQuery UI 1.8.7, so you don't need to add the actual library code unless you wish to use a different version. jQuery UI runs on top of jQuery which also ships with Drupal. jQuery is loaded by default on all pages but jQuery UI libraries must be manually enabled.

A jQuery UI library can be included either with `drupal_add_library()` or `drupal_add_js()` (deprecated) or by adding it to the `#attached` property of renderable arrays (recommended).

**This article demonstrates both approaches, but `drupal_add_library()` and `drupal_add_js()` will not be available in Drupal 8.**

Although a given library may depend on a number of other libraries, you only need to add the library you wish to use. The dependencies are automatically included.

The example below adds the autocomplete library to a new field on the site contact form.

## 1. Using `#attached` in a renderable array (recommended)

``` php
function mymodule_form_contact_site_form_alter(&$form, &$form_state, $form_id) {
  $path = drupal_get_path('module', 'mymodule');
  
  // Adds a form field that the javascript utilizes or modifies.
  $form['location'] = array(
    '#type' => 'textfield',
    '#title' => 'Your Location (Country)',
    '#id' => 'country_autocomplete',
    // Both the library and custom JavaScript code are added to the '#attached'
    // property of a renderable array.
    '#attached' => array(
      'library' => array(
        array('system', 'ui.autocomplete'),
      ),
      'js' => array(
        "$path/mymodule-custom-javascript.js",
      ),
    ),
  ); 
}
```

## 2. Using `drupal_add_library()` (deprecated)

``` php
function mymodule_form_contact_site_form_alter(&$form, &$form_state, $form_id) {
  // Adds a form field that the javascript utilizes or modifies.
  $form['location'] = array(
    '#type' => 'textfield',
    '#title' => t('Your Location (Country)'),
    '#id' => 'country_autocomplete',
  ); 

  // Adds the library making it available for use.
  drupal_add_library('system', 'ui.autocomplete');
  
  // Custom JavaScript code that uses the library.
  $path = drupal_get_path('module', 'mymodule');
  drupal_add_js("$path/mymodule-custom-javascript.js"); 
}
```

## Further Reading

- API documentation: [drupal_add_library](https://api.drupal.org/api/drupal/includes%21common.inc/function/drupal_add_library/7 "https://api.drupal.org/api/drupal/includes%21common.inc/function/drupal_add_library/7") and [drupal_render](https://api.drupal.org/api/drupal/includes%21common.inc/function/drupal_render/7)
- [drupal_add_css(), drupal_add_js() and drupal_add_library() removed in favor of \#attached](https://drupal.org/node/2169605)
- [Render Arrays in Drupal 7](https://drupal.org/node/930760)
- [Managing JavaScript in Drupal 7](https://drupal.org/node/756722)
- [Definitive Guide to Drupal](http://www.amazon.com/The-Definitive-Guide-Drupal-7/dp/1430231351/ref=sr_1_1?ie=UTF8&qid=1395277737 "Purchase at Amazon")
