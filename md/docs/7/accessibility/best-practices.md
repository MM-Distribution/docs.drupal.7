---
title: "Best practices"
source_url: "https://www.drupal.org/docs/7/accessibility/best-practices"
page_type: page
last_updated: "Last updated on 23 April 2023"
published: "2012-06-15T19:38:12+00:00"
modified: "2023-04-23T21:41:32+00:00"
breadcrumb: ["Drupal 7", "Accessibility tools and best practices for Drupal 7"]
fetched: "2026-10-21T07:13:24Z"
raw: "raw/docs/7/accessibility/best-practices.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Best practices

**Please note that this was the Drupal 7 best practice. For current best practices see the [Accessibility Handbook](https://www.drupal.org/docs/accessibility/drupal-accessibility-features).**

This page provides best practices and important considerations for accessibility when developing Drupal modules.

## Use tools to evaluate your module’s pages for accessibility

Use the [Web Accessibility Evaluation Tool (WAVE)](http://wave.webaim.org/) toolbar or another automated tool to check any pages or blocks that your module creates for accessibility issues.

Here is a list of [more accessibility validation tools](http://drupal.org/node/464494). These tools will not detect all accessibility problems, but they are a great start.

## Use the Form API appropriately

If you use the Drupal Form API, it will do a lot of work towards making your forms accessible. Make sure when using hook_form_alter and other techniques to modify forms that you are not reducing the accessibility of forms.

### Use \#title and \#description

Every FAPI element should have the \#title property set. This makes a label for the input field so that screen reader users know what the input field is for. The \#title property should indicate the label associated to the form element. It should **not** be used for formatting other text (to create a heading, for example).

If the form element needs additional description beyond the title, set the \#description property as well.

For example,

``` php
$form['pass'] = array(
  '#type' => 'password', 
  '#description' => t('Passwords must be at least 8 characters and contain a number'), 
  '#title' => t('Password'), 
  '#maxlength' => 64, 
  '#size' => 15,
);
```

### Use fieldsets to group elements that belong together logically

If you are making a date or phone number field, it is best to only use one input field instead of several. However, if you need to use several input boxes (for example, for the month, day, and year), then these should be grouped in a fieldset so that it is clear to screen reader users that they are all part of the same logical input field.

Example:

``` php
$form['start_date'] = array(
  '#type' => 'fieldset',
  '#title' => t('Date'),
);
$form['start_date']['month'] = array(
  '#type' => 'textfield',
  '#title' => t('Month'),
  '#size' => 2,
  '#maxlength' => 2,
);
$form['start_date']['day'] = array(
  '#type' => 'textfield',
  '#title' => t('Day'),
  '#size' => 2,
  '#maxlength' => 2,
);
$form['start_date']['year'] = array(
  '#type' => 'textfield',
  '#title' => t('Year'),
  '#size' => 4,
  '#maxlength' => 4,
);
```

Radio buttons and checkboxes also need to be grouped together inside a fieldset for the same reason.

Example:

``` php
$form['dinner_pref'] = array(
  '#type' => 'fieldset',
  '#title' => t('Dinner Preference'),
);
$form['dinner_pref']['month'] = array(
  '#type' => 'radio',
  '#title' => t('Chinese'),
);
$form['dinner_pref']['day'] = array(
  '#type' => 'radio',
  '#title' => t('Indian'),
);
$form['dinner_pref']['year'] = array(
  '#type' => 'radio',
  '#title' => t('Burgers'),
);
```

### Form field focus

While it can seem convenient to give a form field the initial focus on a page, this should only be done if that form field is or enables the primary purpose of the page. For example, on a 'Search This Site' page, giving focus to a 'Search Keywords' field would probably be appropriate because searching is the primary purpose of the page. But on a 'Modules List' page, giving focus to a 'Filter Keywords' field would be inappropriate because filtering the module list is not the page's primary purpose.

When focus is given to a form field, screen readers will start reading the page at that field, skipping the top of the page. Users of screen readers will therefore miss out on the context provided at the top and may have difficulty understanding what the page is about, since they cannot review the entire page at a glance.

### Useful links

Here are a few links discussing accessibility considerations with the Form API:

- [Drupal 7, two new system classes to improve accessibility](http://zufelt.ca/blog/drupal-7-two-new-system-classes-improve-accessibility)
- [Drupal 7 Form API accessibility: \#title_display](http://zufelt.ca/blog/drupal-7-form-api-accessibility-titledisplay)

## Make accessible JavaScript widgets

JavaScript widgets are very often not fully accessibility. Best practices recommend ensuring the basic functionality of your site and then enhancing this functionality with JavaScript and other widgets (not replace or mask basic functions).

### Autocomplete widgets

You can create autocomplete widgets in Drupal 7 by setting the '#autocomplete_path' property on a form element. These widgets are accessible. If you want to use jQuery UI Autocomplete instead of Drupal's built-in version, it is accessible in version 1.9 but not in version 1.8.

### Other custom Javascript widgets

For information on creating JavaScript widgets, see these WebAIM articles on [Javascript](http://www.webaim.org/techniques/javascript/) and [AJAX](http://www.webaim.org/techniques/ajax/) accessibility.

For general information, see the [Accessibility handbook](https://www.drupal.org/node/394094).

For information on creating accessible themes, see [Creating accessible themes](http://drupal.org/node/464472).
