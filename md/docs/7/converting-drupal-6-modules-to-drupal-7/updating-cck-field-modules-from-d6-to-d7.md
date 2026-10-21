---
title: "Updating CCK Field Modules from D6 to D7"
source_url: "https://www.drupal.org/docs/7/converting-drupal-6-modules-to-drupal-7/updating-cck-field-modules-from-d6-to-d7"
page_type: page
last_updated: "Last updated on 22 December 2016"
published: "2010-03-01T02:32:33+00:00"
modified: "2016-12-22T06:01:51+00:00"
breadcrumb: ["Drupal 7", "Converting Drupal 6 modules to Drupal 7"]
fetched: "2026-10-21T07:51:44Z"
raw: "raw/docs/7/converting-drupal-6-modules-to-drupal-7/updating-cck-field-modules-from-d6-to-d7.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Updating CCK Field Modules from D6 to D7

This page includes instructions about how to update CCK field modules from D6 to D7. Start by using the [Coder](http://drupal.org/project/coder "coder") module and other documentation to apply basic D6 to D7 changes, then focus on the changes in the Field API. See the [Field API Book Page](http://drupal.org/community-initiatives/drupal-core/fields) or the embedded [Field API documentation](http://drupalcode.org/viewvc/drupal/drupal/modules/field/field.api.php?revision=1.65&content-type=text%2Fplain&view=co&pathrev=MAIN), or look at the way core fields are defined for more information.

## Miscellaneous Changes

- Remove **content_notify()** calls. They were in the module_enable(), module_disable(), module_install() and module_uninstall() hooks. There is a [new method in core](http://drupal.org/node/224333#hook_modules_action) to allow modules to be notified when other modules are enabled and disabled, so this is no longer needed.
- Change **hook_content_is_empty()** to **hook_field_is_empty()**, this is just a change in the hook name.
- Functions like **content_fields()** need to be replaced with their new equivalents, like **field_info_fields()**. Replace **content_types()** with **field_info_instances()**. The information from **content_database_info()** is now available in **\$field\['storage'\]** (keep in mind that the field might not use database storage). See [field.info.inc](http://drupalcode.org/project/drupal.git/blob_plain/refs/heads/7.x:/modules/field/field.info.inc) for some of the new functions. The fingerprint of the function and the structure of the values returned may be slightly different, so you'll need to test that.
- Note that the field data structure has changed slightly. The language (or a variable that indicates that the field has no translation) lives at the top level of the field array, i.e. The field value looks like \$field\['field_name'\]\[unc\]\[0\]\['value'\] instead of \$field\['field_name'\]\[0\]\['value'\]

## New! Fields Everywhere

In Drupal 7, fields can be on any object that declares it is 'fieldable', including nodes and users. Other modules can create their own entities that can have fields attached to them by declaring hook_entity_info().

``` php
/**
 * Implements hook_entity_info().
 */
function node_entity_info() {
  $return =  array(
    'example' => array(
      'label' => t('Node'),
      'controller class' => 'NodeController',
      'base table' => 'node',
      'revision_table' => 'node_revision',
      'fieldable' => TRUE,
      'uri callback' => 'node_uri',
      'entity keys' => array(
        'id' => 'nid',
        'revision' => 'vid',
        'bundle' => 'type',
      ),
      'bundle keys' => array(
        'bundle' => 'node',
       ),
      'bundles' => array(),
      'view modes' => array(
        'full' => array(
          'label' => t('Full content'),
        ),
        'teaser' => array(
          'label' => t('Teaser'),
        ),
        'rss' => array(
          'label' => t('RSS'),
        ),
      ),
    ),
  );
  return $return;
}
```

## New! Instance Array

There is a new array called an \$instance. It has the same basic structure as the \$field array used in Drupal 6, but contains the settings that apply to a specific instance of a field. The widget definition is a sub-array of the instance. The \$field array is a separate, smaller, array that contains only values that apply to all instances of a field.

Note that there are numerous 'settings' arrays. The field has settings, the instance has settings, the widget has settings, and the display has settings.

Several things that were field values in Drupal 6 are now instance values: required, label, description, widget. There are now separate weights for the widget, and the display. Settings values are now in 'settings' sub-arrays, for instance \$field\['min'\] is now \$field\['settings'\]\['min'\].

The display settings correspond to the view modes declared by hook_entity_info() for the type of entity used in this instance.

``` php
$instance = array(
  'entity_type' => 'node',
  'label' => 'Example',
  'required' => 0,
  'description' => 'My description',
  'default_value' => '',
  'id' => 9,
  'field_id' => 5,
  'field_name' => 'field_example',
  'bundle' => 'article',
  'deleted' => 0,
  'settings' => array(
    'min' => 5,
    'max' => 10,
  ),
  'widget' => array(
    'weight' => 0,
    'type' => 'number',
    'module' => 'number',
    'active' => 1,
    'settings' => array(),
  ),
  'display' => array(
    'full' => array(
      'label' => 'above',
      'type' => 'number_decimal',
      'settings' => array(
        'scale' => 2,
      ),
      'weight' => 0,
      'module' => 'number',
    ),
  ),
);
```

## Changed! Field Array

The field array now contains only values that are the same across all instances. 'Bundle' is the new name for what we called a 'Content Type' in Drupal 6, to recognize that fields can go on objects other than nodes. 'Cardinality' is the new name for what we called 'Multiple' in Drupal 6. The field storage is now pluggable, defaulting to sql storage.

A simplified example of a \$field array (with some details left out) is below:

``` php
$field = array(
  'translatable' => 1,
  'id' => 5,
  'field_name' => 'field_example',
  'type' => 'number_decimal',
  'module' => 'number',
  'active' => 1,
  'locked' => 0,
  'cardinality' => 1,
  'deleted' => 0,
  'settings' => array(
    'scale' => 2,
  ),
  'storage' => array(
    'type' => 'field_sql_storage',
    'settings' => array(),
    'module' => 'field_sql_storage',
    'active' => 1,
    'details' => array(),
  ),
  'entity_types' => array(...),
  'indexes' => array(...),
  'columns' => array(
    'value' => array(...),
  ),
  'bundles' => array(
    'node' => array(...),
  ),
);  
```

## Changed! Hook Widget Info

The name of the widget info hook has changed from hook_widget_info() to hook_field_widget_info(). Special behaviors for multiple values and default values are defined slightly differently. New in Drupal 7, you declare all the widget settings in the info hook and set default values for the settings.

### In Drupal 6

``` php
function number_widget_info() {
  return array(
    'number' => array(
      'label' => t('Text field'),
      'field types' => array('number_integer', 'number_decimal', 'number_float'),
      'multiple values' => CONTENT_HANDLE_CORE,
      'callbacks' => array(
        'default value' => CONTENT_CALLBACK_DEFAULT,
      ),
    ),
  );
}
```

### In Drupal 7

``` php
/**
 * Implements hook_field_widget_info().
 */
function number_field_widget_info() {
  return array(
    'number' => array(
      'label' => t('Text field'),
      'field types' => array('number_integer', 'number_decimal', 'number_float'),
      'behaviors' => array(
        'multiple values' => FIELD_BEHAVIOR_DEFAULT,
        'default value' => FIELD_BEHAVIOR_DEFAULT,
      ),
      'settings' => array(
        'size' => 60,
      ),
    ),
  );
}
```

## Changed! Hook Widget

You still add \#element_validate and name a function to do the widget validation, just as was done in Drupal 6. In Drupal 6 we had \$element\['\_error_element'\] which is gone in Drupal 7, replaced by new function hook_field_widget_error(). The hook_widget() function has been renamed to hook_field_widget_form(), and it has several new parameters passed to it.

### In Drupal 6

``` php
function number_widget(&$form, &$form_state, $field, $items, $delta = 0) {
  $element['value'] = array(
    // Fill in $element.
  );

  // Used so that hook_field('validate') knows where to flag an error.
  $element['_error_element'] = array(
    '#type' => 'value',
    '#value' => implode('][', array_merge($element['#parents'], array($field_key))),
  );

  return $element;
}
```

### In Drupal 7

``` php
/**
 * Implements hook_field_widget_form().
 */
function number_field_widget_form(&$form, &$form_state, $field, $instance, $langcode, $items, $delta, $element) {
  // use += to avoid overwriting incoming $element
  $element['value'] += array(
    // Fill in $element.
  );

  return $element;
}

/**
 * Implements hook_field_widget_error().
 */
function number_field_widget_error($element, $error, $form, &$form_state) {
  form_error($element['value'], $error['message']);
}
```

The following values are available in the \$element for widget processing. Don't try to use the values of \$form\['#fields'\] in element processing, that doesn't exist in Drupal 7. Use \$element\['#field_name'\] to get the field array from the \$form_state, like **\$field = \$form_state\['field'\]\[\$element\['#field_name'\]\]\[\$element\['#language'\]\]\['field'\]**. Note that you should get it from \$form_state instead of field_info_field() during form processing to be sure you are not getting a cached, out of date, version of the field.

``` php
$element['#entity_type']
$element['#bundle']
$element['#field_name']
$element['#language']
$element['#columns']
$element['#title']
$element['#description']
$element['#required']
$element['#delta']
$element['#language']
```

## Changed! Hook Field Info

New in Drupal 7, you declare all the field and instance settings in the info hook and set default values for the settings. You also identify a default widget and a default formatter for this field.

### In Drupal 6

``` php
/**
 * Implementation of hook_field_info().
 */
function number_field_info() {
  return array(
    'number_integer' => array(
      'label' => t('Integer'),
      'description' => t('Store a number in the database as an integer.'),
    ),
  );
}
```

### In Drupal 7

``` php
/**
 * Implements hook_field_info().
 */
function number_field_info() {
  return array(
    'number_integer' => array(
      'label' => t('Integer'),
      'description' => t('This field stores a number in the database as an integer.'),
      'settings' => array('size' => 255),
      'instance_settings' => array('min' => '', 'max' => '', 'prefix' => '', 'suffix' => ''),
      'default_widget' => 'number',
      'default_formatter' => 'number_integer',
    ),
  );
}
```

## Changed! Hook Field Settings

In Drupal 7 hook_field_settings() is broken out into hook_field_settings_form() and hook_field_schema(). The 'save' operation was used to instruct CCK what settings need to be saved and is no longer needed since the settings are defined in hook_field_info().

### Drupal 6

``` php
/**
 * Implementation of hook_field_settings().
 */
function number_field_settings($op, $field) {
  switch ($op) {
    case 'form':
      $form = array();
      $form['min'] = array(
        '#type' => 'textfield',
        '#title' => t('Minimum'),
        '#element_validate' => array('_element_validate_number'),
        '#default_value' => is_numeric($field['min']) ? $field['min'] : '',
      );
      return $form;

    case 'validate':
      // Any additional validation for the field could be done here.
      break;

    case 'save':
      $values = array('prefix', 'suffix', 'min', 'max', 'allowed_values', 'allowed_values_php');
      if ($field['type'] == 'number_decimal') {
        $values = array_merge($values, array('precision', 'scale', 'decimal'));
      }
      return $values;

    case 'database columns':
      return array(
        'value' => array('type' => 'int', 'not null' => FALSE, 'sortable' => TRUE),
      );
  }
}
```

### Drupal 7

``` php
/**
 * Implements hook_field_settings_form().
 */
function number_field_settings_form($field, $instance, $has_data) {
  $settings = $field['settings'];
  $form = array();
  if ($field['type'] == 'number_decimal' || $field['type'] == 'number_float') {
    $form['decimal_separator'] = array(
      '#type' => 'select',
      '#title' => t('Decimal marker'),
      '#options' => array(
        '.' => 'decimal point',
        ',' => 'comma',
        ' ' => 'space',
      ),
      '#default_value' => $settings['decimal_separator'],
      '#description' => t('The character users will input to mark the decimal point in forms.'),
    );
  }
  return $form;
}

/**
 * Implements hook_field_schema().
 */
function number_field_schema($field) {
  switch ($field['type']) {
    case 'number_integer' :
      $columns = array(
        'value' => array(
          'type' => 'int',
          'not null' => FALSE
        ),
      );
      break;
  }
  return array(
    'columns' => $columns,
  );
}
```

### Replacing \$op == 'validate' with \#element_validate

The custom CCK validation hooks have been removed in D7. You can still validate more complicated forms by using the FAPI \#element_validate on the entire sub-form.

``` php
/**
 * Implements hook_field_settings_form().
 */
function myfield_field_settings_form($field, $instance, $has_data) {
  $form = array();
  $form['decimal_separator'] = array(
    ...
    '#element_validate' => array('myfield_field_settings_form_validate'),
  );
  return $form;
}

/**
 * Implements the #element_validate callback for myfield_field_settings_form().
 */
function myfield_field_settings_form_validate($element, &$form_state) {
  // Do any custom validation here.
  if ($has_error) {
    form_error($element['decimal_separator'], t('%label has an error.', array('%label' => t('Decimal marker'))));
  }
  else {
    // You can update the values of the settings here too.
    form_set_value($element['decimal_separator'], $new_value, $form_state);
  }
}
```

### Replacing \$op == 'views data' for views relationships, etc.

If your D6 hook_field_settings() supported \$op == 'views data' then that logic will have to be moved. To add support for relationships your module should implement hook_field_views_data() or hook_field_views_data_alter() to add the necessary information. [Related issue](http://drupal.org/node/761372).

## Changed! Hook Field

Each of the operations in hook_field is now a separate hook, hook_field_validate, hook_field_insert, hook_field_update, etc. Note that a couple operations, load and prepare_view, operate on multiple entities at once, so are passed an array of \$entities instead of a single \$entity.

In Drupal 6 we had \$element\['\_error_element'\] which is gone in Drupal 7, replaced with a \$error array that is passed by reference to the validator.

### Drupal 6

``` php
/**
 * Implementation of hook_field().
 */
function number_field($op, &$node, $field, &$items, $teaser, $page) {
  switch ($op) {
    case 'validate':
      $allowed_values = content_allowed_values($field);
      if (is_array($items)) {
        foreach ($items as $delta => $item) {
          $error_element = isset($item['_error_element']) ? $item['_error_element'] : '';
          if (is_array($item) && isset($item['_error_element'])) unset($item['_error_element']);
          if ($item['value'] != '') {
            if (is_numeric($field['min']) && $item['value'] < $field['min']) {
              form_set_error($error_element, t('%name: the value may be no smaller than %min.', array('%name' => t($field['widget']['label']), '%min' => $field['min'])));
            }
            if (is_numeric($field['max']) && $item['value'] > $field['max']) {
              form_set_error($error_element, t('%name: the value may be no larger than %max.', array('%name' => t($field['widget']['label']), '%max' => $field['max'])));
            }
            if (count($allowed_values)) {
              // We cannot use array_key_exists() because allowed values are
              // stored as strings, and we need to compare numeric equality.
              $valid = FALSE;
              foreach ($allowed_values as $kay => $value) {
                if ((float) $item['value'] == (float) $kay) {
                  $valid = TRUE;
                  break;
                }
              }
              if (!$valid) {
                form_set_error($error_element, t('%name: illegal value.', array('%name' => t($field['widget']['label']))));
              }
            }
          }
        }
      }
      return $items;
  }
}
```

### Drupal 7

``` php
/**
 * Implements hook_field_validate().
 *
 * Possible error codes:
 * - 'number_min': The value is smaller than the allowed minimum value.
 * - 'number_max': The value is larger than the allowed maximum value.
 */
function number_field_validate($entity_type, $entity, $field, $instance, $langcode, $items, &$errors) {
  foreach ($items as $delta => $item) {
    if ($item['value'] != '') {
      if (is_numeric($instance['settings']['min']) && $item['value'] < $instance['settings']['min']) {
        $errors[$field['field_name']][$langcode][$delta][] = array(
          'error' => 'number_min',
          'message' => t('%name: the value may be no smaller than %min.', array('%name' => t($instance['label']), '%min' => $instance['settings']['min'])),
        );
      }
      if (is_numeric($instance['settings']['max']) && $item['value'] > $instance['settings']['max']) {
        $errors[$field['field_name']][$langcode][$delta][] = array(
          'error' => 'number_max',
          'message' => t('%name: the value may be no larger than %max.', array('%name' => t($instance['label']), '%max' => $instance['settings']['max'])),
        );
      }
    }
  }
}
```

## Changed! Hook Formatter Info

In Drupal 6, a formatter could provide the default behavior of formatting a single field value or alternatively could be used to format all field values of a multiple value field in a single formatter, in Drupal 7, all formatters receive all field values to format as they wish.

New feature in Drupal 7: formatters can declare settings and default values for those settings.

New constraint in Drupal 7: two formatters cannot have the same machine name (this was already the case for field type and widget names in Drupal 6). It is therefore recommended to prefix formatter machine names by the name of the module that implements them. This also means that, unlike Drupal 6, Drupal 7 doesn't require each field type to have a formatter named 'default'.

### In Drupal 6

``` php
/**
 * Implementation of hook_field_formatter_info().
 */
function number_field_formatter_info() {
  return array(
    'default' => array(
      'label' => '9999', 
      'multiple values' => CONTENT_HANDLE_CORE, 
      'field types' => array('number_integer', 'number_decimal', 'number_float')),
  );
}

```

### In Drupal 7

``` php
/**
 * Implements hook_field_formatter_info().
 */
function number_field_formatter_info() {
  return array(
    'number_integer' => array(
      'label' => t('Default'),
      'field types' => array('number_integer', 'number_decimal', 'number_float'),
      'settings' =>  array(
        'thousand_separator' => ' ',
        'decimal_separator' => '.',
        'scale' => 0,
        'prefix_suffix' => TRUE,
      ),
    ),
  );
}
```

## Changed! Hook Formatter

In Drupal 6, you had to create a theme function for each formatter and declare each of them in hook_theme. In Drupal 7 you implement hook_field_formatter_view(), no need to implement hook_theme().

### In Drupal 6

``` php
/**
 * Implementation of hook_theme().
 */
function number_theme() {
  return array(
    'number_formatter_unformatted' => array('arguments' => array('element' => NULL)),
  );
}

function theme_number_formatter_unformatted($element) {
  return $element['#item']['value'];
}
```

### In Drupal 7

``` php
/**
 * Implements hook_field_formatter_view().
 */
function number_field_formatter_view($entity_type, $entity, $field, $instance, $langcode, $items, $display) {
  $element = array();
  $settings = $display['settings'];
  $formatter = $display['type'];
  foreach ($items as $delta => $item) {
    $element[$delta] = array('#markup' => $item['value']);
  }

  return $element;
}
```
