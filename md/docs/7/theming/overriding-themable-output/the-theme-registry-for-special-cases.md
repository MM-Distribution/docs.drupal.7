---
title: "The theme registry for special cases"
source_url: "https://www.drupal.org/docs/7/theming/overriding-themable-output/the-theme-registry-for-special-cases"
page_type: page
last_updated: "Last updated on 6 February 2021"
published: "2008-02-18T21:25:06+00:00"
modified: "2021-02-06T16:20:00+00:00"
breadcrumb: ["Drupal 7", "Theming Drupal 7", "Overriding themable output"]
fetched: "2026-10-21T08:22:13Z"
raw: "raw/docs/7/theming/overriding-themable-output/the-theme-registry-for-special-cases.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# The theme registry for special cases

You should be familiar with the [purpose](/node/173880#theme-registry) of the theme registry before continuing on this page. The instructions here will cover how to manually register a theming hook and explain how it can be [manipulated](#manipulate-registry).

The most common case for manually registering hooks is in forms. Form elements are themable but there is another dimension to how they are processed. There are the generic elements such as checkboxes, radio selects, submit button, drop down menus, etc. Each element is themable on its own and overriding it does not require manually registering the hooks associated with it. The extra dimension comes in with custom forms where each element is arranged in very specific ways. In some forms, they are already arranged, themed and registered. For these forms, manually registering is not required. The forms that are not explicitly themed will default to how [form API renders](http://api.drupal.org/api/file/developer/topics/forms_api.html/6) them.

Registered form example:  
Here's an example for two of the search forms registered by search.module, the search box and search block. Every form has a unique ID associated with it. Registering the IDs also serves as the theming hook. In this case, it is "search_theme_form" and "search_block_form".

``` php
function search_theme() {
  return array(
    'search_theme_form' => array(
      'arguments' => array('form' => NULL),
      'template' => 'search-theme-form',
    ),
    'search_block_form' => array(
      'arguments' => array('form' => NULL),
      'template' => 'search-block-form',
    ),
    ...
  );
}
```

The Form API passes control of its presentation along to the handler of the registered hook. In this example, it is registered with the type of template with its default arguments. The output can be altered easily from the theme since it was already registered as a [template](/node/190815#search-tpl). Auto discovery of the hook only happens with existing theming hooks registered below the theming layer. *([see image](/node/173880#theming-overrides))*

Registering an unregistered form:  
There is another search form that is not registered. It is the form with the ID of "search_form" used on the main search page. The data for the form is [constructed in a function](http://api.drupal.org/api/function/search_form/6) just like any other form but it leaves it up to the Form API to deal with the presentation based on its data structure.

To extend this so it can be overridden, you have to register it from your theme with [hook_theme](http://api.drupal.org/api/function/hook_theme/6). Place the following inside your template.php file replacing the "drop" prefix with the name of your theme. The theming hook is the ID of the form:

``` php
function drop_theme() {
  return array(
    'search_form' => array(
      'arguments' => array('form' => NULL),
    ),
  );
}
```

Themed forms always have an argument of "form". Since the template was not specified, the hook will be seen as a theme function, not a template. *The theme function has to have a matching prefix of the theme that registered it.* *phptemplate\_\* will not work.* So, with the above entry, the theme function would look like this:

``` php
function drop_search_form($form) {
  $advanced = '';
  $simple = '';
  foreach (element_children($form) as $element) {
    if ($element == 'advanced') {
      $advanced .= drupal_render($form[$element]);
    }
    else {
      $simple .= drupal_render($form[$element]);
    }
  }
  return $advanced . $simple;
}
```

The only thing changed here is the positioning of the advanced search form.

- *Sub-themes overriding a form that was registered in its base theme does not have to manually re-register the form. Remember, the registering allows auto discovery for the layers above it and sub-themes are just another layer on top of base themes.*
- *This may be more automated in future versions. The developers are aware of the burden it places on themers.*

**Manual manipulating**

Manual manipulation of the theme registry is an advanced feature. You can read about it by clicking the "Theme registry" in the block provided by devel module. It can also be returned with [theme_get_registry](http://api.drupal.org/api/function/theme_get_registry/7).

To be continued...
