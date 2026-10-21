---
title: "Theming forms in your theme"
source_url: "https://www.drupal.org/docs/7/theming/advanced/theming-forms-in-your-theme"
page_type: page
last_updated: "Last updated on 31 August 2016"
published: "2011-06-26T04:12:29+00:00"
modified: "2016-08-31T14:09:42+00:00"
breadcrumb: ["Drupal 7", "Theming Drupal 7", "Advanced theming"]
fetched: "2026-10-21T08:16:47Z"
raw: "raw/docs/7/theming/advanced/theming-forms-in-your-theme.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Theming forms in your theme

An example about how to theme Drupal Commerce Check Out form:

### template.php

``` php
/**
 * Implements hook_theme().
 */
function yourtheme_theme($existing, $type, $theme, $path) {
  $base = array(
    'render element' => 'form',
    'path' => drupal_get_path('theme', 'yourtheme') . '/templates/forms',
  );

  return array(
    'commerce_checkout_form_checkout' => $base + array(
      'template' => 'commerce-checkout-form-checkout',
    ),
  );
}

/**
 * Preprocessor for commerce_checkout_form_checkout theme.
 */
function yourtheme_preprocess_commerce_checkout_form_checkout(&$variables) {
  /* Add or modify your variables */
}
```

### \[yourtheme\]/templates/forms/commerce-checkout-form-checkout.tpl.php

``` php
<?php
  // Render or hide parts of $form: var_export($form);
  // Example given:
  hide($form['title']);
  print render($form['first']);
  // Render remaining form elements as usual.
  print drupal_render_children($form);
?>
```

Don't forget clearing the theme registry cache.
