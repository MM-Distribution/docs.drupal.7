---
title: "Creating advanced theme settings"
source_url: "https://www.drupal.org/docs/7/theming/advanced/creating-advanced-theme-settings"
page_type: page
last_updated: "Last updated on 15 May 2018"
published: "2007-09-23T04:58:45+00:00"
modified: "2018-05-15T14:21:11+00:00"
breadcrumb: ["Drupal 7", "Theming Drupal 7", "Advanced theming"]
fetched: "2026-10-21T08:16:32Z"
raw: "raw/docs/7/theming/advanced/creating-advanced-theme-settings.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Creating advanced theme settings

In Drupal 6 and beyond, theme authors can now customize this page by adding additional settings to the form. In Drupal 5, theme authors and theme users will have to install the [Theme Settings API](/project/themesettingsapi) module (5.x-2.1 or later) before being able to use the method described below.

**Drupal 7**  
Drupal 7 uses admin/appearance/settings/themeName.

**Drupal 6**  
In the Drupal administration section, each theme has its own settings page at **admin/build/themes/settings/themeName**. And this page has a form with standard settings like “Logo image settings” and “Shortcut icon settings.”

## Drupal 7

In Drupal 7, themes can modify the entire theme settings form. In a theme’s `theme-settings.php`, themes should now use [THEMENAME_form_system_theme_settings_alter(&\$form, \$form_state)](http://api.drupal.org/api/function/hook_form_system_theme_settings_alter/7) hook function. This gives the same power to themes that modules have if they use [hook_form_system_theme_settings_alter()](https://api.drupal.org/api/drupal/modules%21system%21theme.api.php/function/hook_form_system_theme_settings_alter/7). See the “Forms API Quickstart Guide” and “Forms API Reference” on <http://api.drupal.org/api/7>, as well as the [hook_form_FORM_ID_alter() docs](http://api.drupal.org/api/function/hook_form_FORM_ID_alter/7) to learn the full flexibility of Forms API. Note that themes can no longer use the phptemplate\_ prefix to the function; you’ll need to use the actual name of your theme as the prefix.

Here’s an example if you had a “foo” theme and wanted to add a textfield whose default value was “blue bikeshed”:

``` php
function foo_form_system_theme_settings_alter(&$form, $form_state) {
  $form['foo_example'] = array(
    '#type'          => 'textfield',
    '#title'         => t('Widget'),
    '#default_value' => theme_get_setting('foo_example'),
    '#description'   => t("Place this text in the widget spot on your site."),
  );
}
```

In order to set the default value for any form element you add, you’ll need to add a simple line to your .info file: `settings[SETTING_NAME] = DEFAULT_VALUE`. For our foo theme, you’d need to edit the foo.info file and add this line:

``` php
settings[foo_example] = blue bikeshed
```

In any of your theme’s PHP files, you can retrieve the value the user set by calling:

``` php
$foo_example = theme_get_setting('foo_example');
```

## Drupal 6

First, create a theme-settings.php file in your theme directory and add a `themeName_settings()` or `themeEngineName_settings()` function. The `themeEngineName_settings()` form is discouraged since it can lead to fatal errors when two functions with the same name are defined in your Drupal installation. The function should use the Forms API to create the additional form widgets.

For example: to add settings to the Garland theme, a `garland_settings()` or `phptemplate_settings()` function would be placed in the theme’s **theme-settings.php** file.

*Directly modifying Garland or Minnelli is strongly discouraged, since they are used for the install and upgrade process.*

If a user has previously saved the theme settings form, the saved values will be passed to this function in the \$saved_settings parameter. The widgets to add to the form should be returned as a Forms API array.

The comments in the following example explain the details:

``` php
<?php
// An example themes/garland/theme-settings.php file.

/**
 * Implementation of THEMEHOOK_settings() function.
 *
 * @param $saved_settings
 *   array An array of saved settings for this theme.
 * @return
 *   array A form array.
 */
function garland_settings($saved_settings) {
  /*
   * The default values for the theme variables. Make sure $defaults exactly
   * matches the $defaults in the template.php file.
   */
  $defaults = array(
    'garland_happy' => 1,
    'garland_shoes' => 0,
  );

  // Merge the saved variables and their default values
  $settings = array_merge($defaults, $saved_settings);

  // Create the form widgets using Forms API
  $form['garland_happy'] = array(
    '#type' => 'checkbox',
    '#title' => t('Get happy'),
    '#default_value' => $settings['garland_happy'],
  );
  $form['garland_shoes'] = array(
    '#type' => 'checkbox',
    '#title' => t('Use ruby red slippers'),
    '#default_value' => $settings['garland_shoes'],
  );

  // Return the additional form widgets
  return $form;
}
?>
```

Note that theme authors can create complex, dynamic forms using advanced Forms API (auto-completion, collapsible fieldsets) and the JavaScript library, jQuery.

## Getting the settings’ values in your theme files

In order to retrieve the settings in the theme’s **template.php** or **.tpl.php** files, simply use `theme_get_setting('varname')`. See the Drupal API for details: <http://api.drupal.org/api/6/function/theme_get_setting>

For example: ` $happy = theme_get_setting('garland_happy'); `

## Initializing the default values

Since we can’t guarantee that a user will ever go to the **admin/build/themes/settings/themeName** page, we have to ensure that the default values for our custom settings get initialized.

The theme settings variables aren’t set until we submit the **admin/build/themes/settings/themeName** form for the first time, so in our **template.php** file we need to check whether the variables are set or not. If they aren’t set, we need to set them to the default values. We accomplish that by retrieving one of the variables and seeing if it is null. If it is null, we save the defaults using `variable_set()` and then force the refresh of the settings in Drupal’s internals using `theme_get_setting('', TRUE)`.

Add the following code near the top of your **template.php** file:

``` php
/*
 * Initialize theme settings
 */
if (is_null(theme_get_setting('garland_happy'))) {  // <-- change this line
  global $theme_key;

  /*
   * The default values for the theme variables. Make sure $defaults exactly
   * matches the $defaults in the theme-settings.php file.
   */
  $defaults = array(             // <-- change this array
    'garland_happy' => 1,
    'garland_shoes' => 0,
  );

  // Get default theme settings.
  $settings = theme_get_settings($theme_key);
  // Don't save the toggle_node_info_ variables.
  if (module_exists('node')) {
    // NOTE: node_get_types() is renamed to node_type_get_types() in Drupal 7
    foreach (node_type_get_types() as $type => $name) {    
      unset($settings['toggle_node_info_' . $type]);
    }
  }
  // Save default theme settings.
  variable_set(
    str_replace('/', '_', 'theme_'. $theme_key .'_settings'),
    array_merge($defaults, $settings)
  );
  // Force refresh of Drupal internals.
  theme_get_setting('', TRUE);
}
```

Note that the variable name “garland_happy” in the first line of the above code would be replaced with a variable name from your custom theme settings and the \$defaults array would need to be copied from your **theme-settings.php** file.

## Adding additional settings to a new version of your theme

After you have released a 1.0 version of your theme, you will eventually want to add some additional custom settings to the 2.0 version. The process is mostly straight-forward. But pay close attention to the initialization code in the third step:

1.  In your **theme-settings.php** file, add the new settings to the `$defaults` and `$form` variables.
2.  In your **template.php** file, add the settings to the `$defaults` variable in the *Initialize theme settings* code.
3.  In your **template.php** file, update the initialization code to check for the existence of one of your *new* settings. For example, if you added several settings, including a `garland_slippers` setting, you would change the first line of the *Initialize theme settings* code to read:  
    `if (is_null(theme_get_setting('garland_slippers'))) {`

This will ensure that the defaults for your newly-added custom settings get added to the saved values of the old custom settings.
