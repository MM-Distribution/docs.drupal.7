---
title: "Theming Web-Form"
source_url: "https://www.drupal.org/docs/7/theming/howto/theming-web-form"
page_type: page
last_updated: "Last updated on 8 September 2016"
published: "2011-05-14T04:48:08+00:00"
modified: "2016-09-08T14:07:08+00:00"
breadcrumb: ["Drupal 7", "Theming Drupal 7", "Theming HowTos"]
fetched: "2026-10-21T08:52:31Z"
raw: "raw/docs/7/theming/howto/theming-web-form.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Theming Web-Form

This is one of the finest technique I found so far to theme webform form. In fact, it could be used for any form generated through Drupal Form API.

For Example, I needed certain elements of the form to be on one line (horizontally placed), I could do something like below. This is just override function of "template_preprocess_webform_form" provided by webform module. Place this in your theme's template.php file.

``` php
<?php

function garland_preprocess_webform_form(&$vars) {
  drupal_add_css(drupal_get_path('module', 'webform') . '/css/webform.css');
  drupal_add_js(drupal_get_path('module', 'webform') . '/js/webform.js');
  
  $vars['form']['submitted']['name']['#prefix'] = '<table border="0"><tbody style="border: 0px;"><tr><td>';
  $vars['form']['submitted']['name']['#suffix'] = '</td>';
  $vars['form']['submitted']['phone']['#prefix'] = '<td>';
  $vars['form']['submitted']['phone']['#suffix'] = '</td>';
  $vars['form']['submitted']['city']['#prefix'] = '<td>';
  $vars['form']['submitted']['city']['#suffix'] = '</td></tr></tbody></table>';

  if (isset($vars['form']['details']['nid']['#value'])) {
    $vars['nid'] = $vars['form']['details']['nid']['#value'];
  }
  elseif (isset($vars['form']['submission']['#value'])) {
    $vars['nid'] = $vars['form']['submission']['#value']->nid;
  }
}

?>
```

That's it! You could do almost anything you want with this technique!

### Adding custom classes to webform components (form items) for D7.

Webform is implementing it's own theme function for form items. Unfortunately, due to an old decision, there's no way to add css class to item container. You can need this for adding for example bootstrap or foundation classes to make some elements in two or three columns. To do this you should do these simple steps:

#### Step 1.

In your **template.php** file add the following function:

``` php
<?php
/**
 * Replacement for theme_webform_element().
 */
function THEMENAME_webform_element($variables) {
  $variables['element'] += array(
    '#title_display' => 'before',
  );
  $element = $variables['element'];
  if (isset($element['#format']) && $element['#format'] == 'html') {
    $type = 'display';
  }
  else {
    $type = (isset($element['#type']) && !in_array($element['#type'], array('markup', 'textfield', 'webform_email', 'webform_number'))) ? $element['#type'] : $element['#webform_component']['type'];
  }
  $nested_level = $element['#parents'][0] == 'submitted' ? 1 : 0;
  $parents = str_replace('_', '-', implode('--', array_slice($element['#parents'], $nested_level)));
  $wrapper_classes = array(
   'form-item',
   'webform-component',
   'webform-component-' . $type,
  );
  if (isset($element['#container_class'])) {
    $wrapper_classes[] = $element['#container_class'];
  }
  if (isset($element['#title_display']) && strcmp($element['#title_display'], 'inline') === 0) {
    $wrapper_classes[] = 'webform-container-inline';
  }
  $output = '<div class="' . implode(' ', $wrapper_classes) . '" id="webform-component-' . $parents . '">' . "\n";
  if (!isset($element['#title'])) {
    $element['#title_display'] = 'none';
  }
  $prefix = isset($element['#field_prefix']) ? '<span class="field-prefix">' . _webform_filter_xss($element['#field_prefix']) . '</span> ' : '';
  $suffix = isset($element['#field_suffix']) ? ' <span class="field-suffix">' . _webform_filter_xss($element['#field_suffix']) . '</span>' : '';
  switch ($element['#title_display']) {
    case 'inline':
    case 'before':
    case 'invisible':
      $output .= ' ' . theme('form_element_label', $variables);
      $output .= ' ' . $prefix . $element['#children'] . $suffix . "\n";
      break;
    case 'after':
      $output .= ' ' . $prefix . $element['#children'] . $suffix;
      $output .= ' ' . theme('form_element_label', $variables) . "\n";
      break;
    case 'none':
    case 'attribute':
      $output .= ' ' . $prefix . $element['#children'] . $suffix . "\n";
      break;
  }
  if (!empty($element['#description'])) {
    $output .= ' <div class="description">' . $element['#description'] . "</div>\n";
  }
  $output .= "</div>\n";
  return $output;
}
?>
```

This will allow webform element function to get class name for container through **\$element\['#container_class'\]**

#### Step 2.

To make adding classes easy for you without debugging form, you need to get webform and components machine name. To fo this inspect the webform blog with your browser, and find the **\<form\>** element and look at it's last class - that's the webform name. The machine name is the same, only - are converted to \_.

![Getting webform name.](/files/webform-name.png)  
You also need to get machine names for the elements you want to add classes to. Find the *.form-item* you need and copy the element id attribute adter 'webform-component-'. The machine name is the same, only - are converted to \_.

![Getting webform element name](/files/webform-items-name.png)

You can also get this data by printing \$form, but the method above requers no php knowladge.

For the example webform above add this code in your **template.php** file add the following function:

``` php
<?php
/**
 * Implements hook_form_alter()/
 */
function THEMENAME_form_alter(&$form, &$form_state, $form_id) {
    // Your webform id goes here.
    if ($form_id == 'webform_client_form_448') {
    // Add classes to webform fields.
    $form['submitted']['contact_fio']['#container_class'] = 'col-md-6';
    $form['submitted']['contact_email']['#container_class'] = 'col-md-6'.
    $form['submitted']['contact_phone']['#container_class'] = 'col-md-12 clear-both';
    }
}
?>
```

That's it! Hope it helps you fighting for beautifull webforms.
