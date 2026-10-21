---
title: "How to Write a Drupal 7 Installation Profile"
source_url: "https://www.drupal.org/docs/7/creating-distributions/how-to-write-a-drupal-7-installation-profile"
page_type: page
last_updated: "Last updated on 17 October 2016"
published: "2011-01-10T21:42:11+00:00"
modified: "2016-10-17T21:51:05+00:00"
breadcrumb: ["Drupal 7", "Creating Drupal 7 distributions"]
fetched: "2026-10-21T07:52:30Z"
raw: "raw/docs/7/creating-distributions/how-to-write-a-drupal-7-installation-profile.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# How to Write a Drupal 7 Installation Profile

Based on [this article](http://www.isaacsukin.com/news/2011/01/10/how-write-drupal-7-installation-profile).

## Installation profiles are like modules

All installation profiles must have *profilename*.info and *profilename*.profile files, and they can also have a *profilename*.install file. The *profilename*.profile file has access to almost everything a normal Drupal *modulename*.module file does because Drupal is fully bootstrapped before almost anything in the profile runs.

The primary exception is that [st()](http://api.drupal.org/api/drupal/includes--install.inc/function/st/7) should generally be used to translate strings instead of the usual [t()](http://api.drupal.org/api/drupal/includes--bootstrap.inc/function/t/7) because the localization hasn't been set up until the installation process completes. Profile files should reside in their own directory within the /profiles directory to be loaded.

Also, [Drush make](https://www.drupal.org/node/625094) is a powerful command line tool for automating parts of the distribution process, which may be easier than the traditional profile method outlined below.

## .info file

The *profilename*.info file should look similar to this:

``` php
name = Profile Name
description = Description of what the profile does.
core = 7.x

; Optional: Mark your installation profile as exclusive, so that the installer
; will auto-select it.
exclusive = true

dependencies[] = block
dependencies[] = color
dependencies[] = comment
dependencies[] = contextual
dependencies[] = dashboard
dependencies[] = help
dependencies[] = image
dependencies[] = list
dependencies[] = menu
dependencies[] = number
dependencies[] = options
dependencies[] = path
dependencies[] = taxonomy
dependencies[] = dblog
dependencies[] = search
dependencies[] = shortcut
dependencies[] = toolbar
dependencies[] = overlay
dependencies[] = field_ui
dependencies[] = file
dependencies[] = rdf
```

The contents of the *profilename*.info file are as follows:

- The `name`, `description`, and `core` assignments are all required.
- The `dependencies` list includes all modules that will be enabled when this profile is installed (the ones above are the defaults from the *Standard* install profile).
- You can optionally include [other declarations](https://drupal.org/node/542202) that can also appear in module .info files.

You can include custom modules with your install profile or have Drupal.org [automatically include other projects](/node/642116) in your profile's package, and you can list those as dependencies as well.

## .install file

In many cases, your *profilename*.install file will look like this:

``` php
/**
 * Implement hook_install().
 *
 * Perform actions to set up the site for this profile.
 */
function profilename_install() {
  include_once DRUPAL_ROOT . '/profiles/minimal/minimal.install';
  minimal_install();
}
```

Use [hook_install()](http://api.drupal.org/api/drupal/modules--system--system.api.php/function/hook_install/7) to insert content into your database during the installation process. This example uses the [minimal default setup](http://api.drupal.org/api/drupal/profiles--minimal--minimal.install/function/minimal_install/7) given by the Minimal install profile in Drupal core. You may want to use the [Standard profile defaults](http://api.drupal.org/api/drupal/profiles--standard--standard.install/function/standard_install/7) instead, which provides various node types, user roles, blocks, input formats, taxonomies, settings, etc. that you might expect to find in a Drupal installation. If you don't use the Standard installation, it's still worth taking a look at it as an example.

### Updating installation profiles

Just like modules, installation profiles can have [hook_update_N()](http://api.drupal.org/api/drupal/modules--system--system.api.php/function/hook_update_N/7) functions in their .install file so that they can be updated to the latest version. For example, if you release version 1.0 of your install profile that installs one content type, and then you release version 2.0 that installs two content types, version 2.0 could have an update function that installed the second content type for sites that had originally used the 1.0 version.

## .profile file

The rest of this page explains what you can do in *profilename*.profile.

### Adding steps to the install process

New steps added to the installation process can either run invisibly in the background (normally to save data or include code needed in later steps) or display something on the screen. New steps are added in [`hook_install_tasks()`](http://api.drupal.org/api/drupal/modules--system--system.api.php/function/hook_install_tasks/7) by returning an associative array. Here's what each task array looks like (all elements are optional):

``` php
<?php
$task['machine_name'] = array(
  'display_name' => st('Human-readable task name'),
  'display' => TRUE,
  'type' => 'normal',
  'run' => INSTALL_TASK_RUN_IF_REACHED,
  'function' => 'function_to_execute',
);
?>
```

Let's break it down.

machine_name  
The internal name of the task.

display_name  
The human-readable name of the task.

display  
Determines whether to show this task in the list of installation tasks on the side of the installation screens. If `display_name` is not given or `display` is FALSE, the task does not appear in the list of installation tasks on the side of the installation screens. `display` is useful if you want to conditionally display a task; for example, you might want to display a configuration form for a module that the user chose to enable in a previous step, but skip that form if the module was not enabled.

type  
One of "normal," "batch," or "form."

- "Normal" tasks can return HTML that will be displayed as a page in the installer or `NULL` to indicate that the task is completed. This is the default. Remember to provide some way to continue to the next step, such as a "continue" button.
- "Batch" tasks return a [batch array](http://api.drupal.org/api/drupal/includes--form.inc/function/batch_set/7) to be processed by the [Batch API](http://api.drupal.org/api/drupal/includes--form.inc/group/batch/7), which is useful for example if you want to import something that could take awhile. The task will be considered complete when the batch finishes processing.
- "Form" tasks return a [Form API structured array](http://api.drupal.org/api/drupal/developer--topics--forms_api_reference.html) which will be displayed as a form on a page in the installer. The installer will take care of moving the user to the next task when the form is submitted.

You can see more specifically what happens for each type in [`install_run_task()`](http://api.drupal.org/api/drupal/includes--install.core.inc/function/install_run_task/7).  

run  
One of [`INSTALL_TASK_RUN_IF_REACHED`](http://api.drupal.org/api/drupal/includes--install.core.inc/constant/INSTALL_TASK_RUN_IF_REACHED/7), [`INSTALL_TASK_RUN_IF_NOT_COMPLETED`](http://api.drupal.org/api/drupal/includes--install.core.inc/constant/INSTALL_TASK_RUN_IF_NOT_COMPLETED/7), or [`INSTALL_TASK_SKIP`](http://api.drupal.org/api/drupal/includes--install.core.inc/constant/INSTALL_TASK_SKIP/7).

- `INSTALL_TASK_RUN_IF_REACHED` means the task will run at each stage of the installation that reaches it. This is mainly used by core to include important resources on each page of the installer.
- `INSTALL_TASK_RUN_IF_NOT_COMPLETED` means the task will run once during the installation process. This is the default, and it is useful for things like displaying instructions and configuration forms, or for inserting content into the database.
- `INSTALL_TASK_SKIP` means the task will not be run. This is usually set conditionally, since you may want to skip tasks depending on the options the user chose in previous steps. It is often the case that a task will be skipped when `display` is set to `FALSE`, but it is possible to display a task in the list without executing it.

function  
This is the function that will be run when the task is executed. If not set, this is the same as the machine_name of the task. You may want to set it to something else if you want to use the same function for multiple tasks, or if you want to conditionally choose a function depending on the options the user chose in previous steps.

As an example, let's say we're writing an installation profile called *geo* for a geographically-focused website, so we want the installer to ask what geographic area the website covers. We'll start by adding a page that asks for the relevant country. If the country is "United States," we'll add another page that asks for the relevant state, or if the country is "Canada," we'll add another page that asks for the relevant province.

``` php
/**
 * Implements hook_install_tasks().
 */
function geo_install_tasks($install_state) {
  $country_is_us = !empty($install_state['parameters']['country']) && $install_state['parameters']['country'] == 'US'; 
  $country_is_ca = !empty($install_state['parameters']['country']) && $install_state['parameters']['country'] == 'CA';
  $tasks = array(
    'geo_country' => array(
      'display_name' => st('Choose a country'),
    ),
    'geo_state' => array(
      'display_name' => st('Choose a state or province'),
      'display' => $country_is_us || $country_is_ca,
      'type' => 'form',
      'run' => $country_is_us || $country_is_ca ? INSTALL_TASK_RUN_IF_NOT_COMPLETED : INSTALL_TASK_SKIP,
      'function' => $country_is_us ? 'geo_state_form' : 'geo_province_form',
    ),
  );
  return $tasks;
}
```

For the `geo_country` task above, "Choose a country" is displayed in the list of tasks in the installer, and the function `geo_country()` is run when the installer reaches that task. Since it has type "normal," it must do its own processing, calling a form using [`drupal_get_form()`](http://api.drupal.org/api/drupal/includes--form.inc/function/drupal_get_form/7) and then rendering it by returning the results of [`drupal_render()`](http://api.drupal.org/api/drupal/includes--common.inc/function/drupal_render/7). (See [`install_select_locale()`](http://api.drupal.org/api/drupal/includes--install.core.inc/function/install_select_locale/7) for an example of this.) The form's submit function would set `$install_state['parameters']['country']` appropriately. Then, if the country chosen is the U.S. or Canada, "Choose a state or province" is displayed in the installer, and either `geo_state_form()` or `geo_province_form()` is used to generate the state- or province-selection form.

All tasks added in `hook_install_tasks()` are run after all dependencies are installed and loaded, so you have access to pretty much everything you would in a normal Drupal module.

### Changing and removing steps from the install process

[`hook_install_tasks_alter()`](http://api.drupal.org/api/drupal/modules--system--system.api.php/function/hook_install_tasks_alter/7) allows changing or removing steps from the install process. For example, if you are building an install profile specifically for sites using a certain language, you might want to remove the localization steps and simply configure the language settings yourself.

`hook_install_tasks_alter()` takes two parameters: `&$tasks` and `$install_state`. The \$tasks variable contains a structured array of all installation tasks like the one you returned in `hook_install_tasks()`. Here are the default tasks, in order, as defined by [`install_tasks()`](http://api.drupal.org/api/drupal/includes--install.core.inc/function/install_tasks/7):

[`install_select_profile`](http://api.drupal.org/api/drupal/includes--install.core.inc/function/install_select_profile/7)  
A configuration page to select which profile to install. It doesn't make any sense to change this, because by the time your profile gets control, it will have already been chosen.

[`install_select_locale`](http://api.drupal.org/api/drupal/includes--install.core.inc/function/install_select_locale/7)  
Allows choosing the language to use in the installer.

[`install_load_profile`](http://api.drupal.org/api/drupal/includes--install.core.inc/function/install_load_profile/7)  
Loads the selected profile into memory.

[`install_verify_requirements`](http://api.drupal.org/api/drupal/includes--install.core.inc/function/install_verify_requirements/7)  
Checks whether the current server meets the correct requirements for installing Drupal.

[`install_settings_form`](http://api.drupal.org/api/drupal/includes--install.core.inc/function/install_settings_form/7)  
The form used to configure and rewrite settings.php.

[`install_system_module`](http://api.drupal.org/api/drupal/includes--install.core.inc/function/install_system_module/7)  
Installs the system module so that the system can be bootstrapped, and installs the user module so that sessions can be recorded during bootstrap.

[`install_bootstrap_full`](http://api.drupal.org/api/drupal/includes--install.core.inc/function/install_bootstrap_full/7)  
Does a full bootstrap of Drupal, loading all core functions and resources.

[`install_profile_modules`](http://api.drupal.org/api/drupal/includes--install.core.inc/function/install_profile_modules/7)  
Installs and enables all modules on which the profile depends (as defined in the `.info` file), and then runs `profilename_install()` if it exists (as defined in the `.install` file).

[`install_import_locales`](http://api.drupal.org/api/drupal/includes--install.core.inc/function/install_import_locales/7)  
Import available languages into the system.

[`install_configure_form`](http://api.drupal.org/api/drupal/includes--install.core.inc/function/install_configure_form/7)  
A form to configure site information and settings.

Profile tasks  
Now any tasks defined by the current installation profile are run. Drupal has already been fully bootstrapped, all required modules are already installed and enabled, and the profile itself has also been "installed," so each task should have access to anything a normal Drupal module would be able to access.

[`install_import_locales_remaining`](http://api.drupal.org/api/drupal/includes--install.core.inc/function/install_import_locales_remaining/7)  
Imports additional languages into the system if any have not yet been imported.

[`install_finished`](http://api.drupal.org/api/drupal/includes--install.core.inc/function/install_finished/7)  
Performs final installation tasks (like clearing caches) and informs the user that the installation process is complete.

### Altering forms

You can also alter forms displayed by the installer using [`hook_form_alter()`](http://api.drupal.org/api/drupal/modules--system--system.api.php/function/hook_form_alter/7) and [`hook_form_FORM_ID_alter()`](http://api.drupal.org/api/drupal/modules--system--system.api.php/function/hook_form_FORM_ID_alter/7) just like you would alter forms in a normal module. The form IDs are the machine names of the tasks by default. You may want to do this to add additional fields to the install_configure_form step, for example. Most installation profiles will also want to include this snippet, which sets the default site name to the name of the server:

``` php
<?php
/**
 * Implements hook_form_FORM_ID_alter().
 */
function standard_form_install_configure_form_alter(&$form, $form_state) {
  // Pre-populate the site name with the server name.
  $form['site_information']['site_name']['#default_value'] = $_SERVER['SERVER_NAME'];
}
?>
```

### Inserting content into the database, and other useful functions

- [`variable_set()`](http://api.drupal.org/api/drupal/includes--bootstrap.inc/function/variable_set/7) and [`variable_get()`](http://api.drupal.org/api/drupal/includes--bootstrap.inc/function/variable_get/7) are particularly useful to remember what your install tasks have already done. Just remember to use [`variable_del()`](http://api.drupal.org/api/drupal/includes--bootstrap.inc/function/variable_del/7) to delete any temporary variables you've created when you're done.
- If you need more fine-grained control than the `dependencies[]` in the `.info` file can give you, you may want to use [`module_enable()`](http://api.drupal.org/api/drupal/includes--module.inc/function/module_enable/7) to enable a specific module during the install process. [Enabling themes](http://api.drupal.org/api/drupal/includes--theme.inc/function/theme_enable/7) is similar, but [setting the default, admin, and maintenance themes](http://www.computerminds.co.uk/articles/setting-default-theme-during-installation) requires a little extra work.
- [`drupal_set_title()`](http://api.drupal.org/api/drupal/includes--bootstrap.inc/function/drupal_set_title/7) allows you to set the title of the page as it appears at the top of the browser window.
- Check the [`standard_install()`](http://api.drupal.org/api/drupal/profiles--standard--standard.install/function/standard_install/7) function for examples of how to save various kinds of content in the database, including content types, taxonomies, user roles and permissions, input formats, fields, menu links, and [RDF](https://secure.wikimedia.org/wikipedia/en/wiki/Resource_Description_Framework) mappings.

## Final notes

Be sure to check out [how to create a drupal-org.make file](http://drupal.org/node/642116) if you want to distribute your profile on Drupal.org.
