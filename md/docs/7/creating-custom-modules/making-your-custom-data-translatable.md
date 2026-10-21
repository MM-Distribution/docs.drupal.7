---
title: "Making your custom data translatable"
source_url: "https://www.drupal.org/docs/7/creating-custom-modules/making-your-custom-data-translatable"
page_type: page
last_updated: "Last updated on 19 March 2018"
published: "2008-09-04T15:39:01+00:00"
modified: "2018-03-19T18:35:00+00:00"
breadcrumb: ["Drupal 7", "Creating custom modules in Drupal 7"]
fetched: "2026-10-21T07:48:25Z"
raw: "raw/docs/7/creating-custom-modules/making-your-custom-data-translatable.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Making your custom data translatable

When developing a module, you should give some consideration to making the text your module displays translatable into other languages. An overview of this process is given on the [Multilingual Support](/node/303984) page.

This page concerns one step in that process: making user-entered text in your module translatable. Note that if all of the user-entered text in your module is stored in nodes, probably the core Locale and Content Translation module will take care of translations for you. But if your module lets the user enter data other than nodes, and that data will be displayed to users, then continue reading to find out how to make it translatable.

The core Locale module supports enabling of languages, designation of a default language, and import/export of language files (.pot, .po) to be used and edited with external software. See its handbook page: <http://drupal.org/handbook/modules/locale>.

### Drupal 7

Starting with Drupal 7, user-entered/configurable strings that are stored in the database may be translated by a contributed module that alters the database queries. To prepare the storage of your module for this translatable strings handling, follow these steps:

- Translation works by rewriting database queries. Therefore, translatable strings have to be stored in dedicated database columns and not in a serialized array or similar.

- In your implementation of hook_schema(), set the field to:  

  ``` php
  'translatable' => TRUE, 
  ```

  An example from block.install:

  ``` php
  function block_schema() {
   $schema['block'] = array(
   // ... 'title' => array(
   'type' => 'varchar',
   'length' => 64,
   'not null' => TRUE,
   'default' => '',
   'description' => 'Custom title for the block. (Empty string will use block default title, <none> will remove the title, text will cause block to use specified title.)',
   'translatable' => TRUE,
   ), 
  ```

- When retrieving your data, use db_select() instead of db_query(), and add the 'translatable' query tag:  

  ``` php
  ->addTag('translatable') 
  ```

  This will enable [Query alteration](http://drupal.org/node/310077). An example from block.module:

  ``` php
  $query = db_select('block', 'b')
  ->fields('b')
  ->condition('b.theme', $theme_key)
  ->condition('b.status', 1)
  ->orderBy('b.region')
  ->orderBy('b.weight')
  ->orderBy('b.module')
  ->addTag('block_load')
  ->addTag('translatable')
  ->execute(); 
  ```

By default, Drupal core does not translate these strings. The entire translation handling, storage, and editing are left to contributed modules (most likely [entity_translation](http://drupal.org/project/entity_translation)).

For more information, consult the originating patch:

[\#593746: Prepare Drupal core for dynamic data translation](/project/drupal/issues/593746 "Status: Closed (fixed), Assigned to: sun")

### Drupal 6

As of Drupal 6, the locale module enables multiple types of data to be translated--not just code-based strings. Drupal core includes support for a single type: strings defined at the code level in e.g., .module files. But other modules can register their own types by implementing [hook_locale()](https://api.drupal.org/api/drupal/developer%21hooks%21core.php/function/hook_locale/6.x).

The contrib [Internationalization package](http://drupal.org/project/i18n) (i18n) makes extensive use of `hook_locale()` to make various types of Drupal core data translatable: taxonomies, variables, forums, user profiles, etc. i18n also includes a generic multilingual strings module, which provides a toolset that module authors can use to expose data through the locale system.

The locale system is best suited to data that change relatively infrequently and less suited to longer, more complex strings that may need frequent updating.

A key characteristic of the locale system is that there is only one version of a given item. String substitution happens at run time, e.g., before display. It's distinct in this way from the content translation system, in which there are multiple versions of a given piece of content, one per language.

Module developers wanting to make their data translatable via the locale system have several options including:

1.  Work directly with the locale system
2.  Build on the Internationalization - String Translation module and use its API
3.  Introduce custom handling with multiple versions of a given item, one per language.

Each of these options is described in a section below.

### Some handy methods

Methods useful when working with locale and languages include:

- [hook_locale()](https://api.drupal.org/api/drupal/modules%21locale%21locale.api.php/function/hook_locale/7.x "Allows modules to define their own text groups that can be translated")
- [language_default()](https://api.drupal.org/api/drupal/includes%21bootstrap.inc/function/language_default/7.x "Default language used on the site")
- [language_list()](https://api.drupal.org/api/drupal/includes%21bootstrap.inc/function/language_list/7.x "Get a list of languages set up indexed by the specified key")
- [locale_language_list()](https://api.drupal.org/api/drupal/modules%21locale%21locale.module/function/locale_language_list/7.x "Returns array of language names")

### Working directly with the locale system

To register one or more new "groups" (types of strings) to be recognized by the Locale module, you need to implement `hook_locale()`. However, the Locale module doesn't provide you much help beyond this hook.

The locale system is still focused mainly on the "default" case (strings passed through `t()`, generally in code). The `locale()` function is hard-coded to this use case. While studying the `locale()` function might be useful, it won't directly help you to work with your own custom locale group. The locale system provides a UI for translating strings once they're registered, but, when it comes to registering strings and ensuring they're used when needed, you're on your own. Hence in part the creation of the strings module in i18n to facilitate these tasks.

To work directly with the locale system, you need to:

- Save source strings as they are created to the {locales_source} table.
- Update existing translations when they change.
- Load strings if available from the {locales_target} table for the current language.

### Working with the Internationalization - String Translation module

The basic process for using the String Translation API from the Internationalization module for translating your strings is as follows:

1.  Implement `hook_locale()` to define a translation group for your module; for example, you might choose 'terms_of_use' for the Terms of Use module. See below for completed sample implementation.

2.  Make sure that you only invoke the Strings Translation module if it has been installed, by wrapping all of the calls into its functionality in:  

    ``` php
    if (module_exists('i18nstrings')) { } 
    ```

3.  Locate places in your module where a user can edit a text string that is then displayed on the user interface. Make sure you tell them to enter the text in their site's default language, and perhaps give them some direction on how to translate this text using the Internationalization - Strings Translation module.

4.  Assign each of these strings a behind-the-scenes code name, consisting of your module's translation group name (defined in your hook_locale() implementation), a subgroup code for the section within your module (if desired), and a code specific to the string, separated by colons (e.g. `'terms_of_use:tou:checkbox_label'` could be used as the code name for the label the user enters for a checkbox in the Terms of Use module on the 'tou' screen).

5.  Whenever the user interface text is updated by a user, call the `tt()` function to store the new value for that text. For example:  

    ``` php
    // First store the text in variable_set() or a database table. Then: if (module_exists('i18nstrings')) { $language = language_default('language'); tt('terms_of_use:tou:checkbox_label', $text_user_entered, $language, TRUE); } 
    ```

6.  Whenever you need to display the user interface text, call the `tt()` function to retrieve the current translation of that text. For example:  

    ``` php
    // First retrieve the text from variable_get or a database table. Then: if (module_exists('i18nstrings')) { $text_to_display = tt('terms_of_use:tou:checkbox_label', $text_to_display); } 
    ```

7.  Add a 'refresh' operation to your hook_locale() implementation, which retrieves the untranslated text from the database and calls the `tt()` function on it. Sample hook_locale() implementation:  

    ``` php
    function terms_of_use_locale($op = 'groups', $group = NULL) { switch ($op) { case 'groups': return array('terms_of_use' => t('Terms of Use')); case 'refresh': if(module_exists('i18nstrings')) { // Get the checkbox label from the database or from variable_get first. Then: tt('terms_of_use:tou:checkbox_label', $label_text, NULL, TRUE); } } } 
    ```

For further reading: these two issues are useful references on how other contributed modules added support for translation using the String Translation module:

- [\#79754: Internationalization needed for Legal module](/project/legal/issues/79754 "Status: Closed (fixed), Assigned to: robert castelo")
- [\#299416: translations support](/project/terms_of_use/issues/299416 "Status: Closed (fixed), Assigned to: kars-t")
- [\#471546: Translate relationships (as 'friend')](/project/user_relationships/issues/471546 "Status: Closed (fixed)")

You might also study the code in the Internationalization module itself, as much of its module set is built off of its String Translation module.

### Providing custom multilanguage support

Custom handling may be needed where strings are long, complex, or frequently updated.

1.  Introduce a `language` field in your schema.
2.  On the editing form, present a language selection element. See [locale_form_alter()](https://api.drupal.org/api/drupal/modules%21locale%21locale.module/function/locale_form_alter/7.x) for examples.
3.  On insert and update, save the language field along with other data.
4.  On load, load a version of your data in the appropriate language, if present. (Use the global `$language` variable.)
5.  On view, provide e.g. a 'translate' link, loading a form with a copy of the item ready for translation.
