---
title: "Validating the data"
source_url: "https://www.drupal.org/docs/7/creating-custom-modules/validating-the-data"
page_type: page
last_updated: "Last updated on 21 September 2016"
published: "2011-03-30T22:17:01+00:00"
modified: "2016-09-21T18:04:25+00:00"
breadcrumb: ["Drupal 7", "Creating custom modules in Drupal 7"]
fetched: "2026-10-21T07:24:00Z"
raw: "raw/docs/7/creating-custom-modules/validating-the-data.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Validating the data

**Main topic described: *Form API***  
**Main functions described: *\_validate(), form_set_error()***

The Form API supplies excellent default validation, but it also allows us to create our own validation function. We want to be sure that the value the user enters is a number greater than 0. The validation function works much like a hook, with the form ID taking the place of the module name. Our validate function will be named `current_posts_form_validate($form, &$form_state)`. Don't confuse this with `hook_validate()`, which is part of the main hook system.

Notice the `$form_state` array variable, an argument here and also for our form function. `$form_state` is passed by reference along through each stage of form processing to capture information about the form's workflow and its current state. Incoming `$_POST` data is first sanitized and checked against the structure of the form before being handed off to validate and submit handlers. The array's `values` key is the default key for storing this data. See [drupal_build_form()](http://api.drupal.org/api/drupal/includes--form.inc/function/drupal_build_form/7) for a list of `$form_state` keys.

Add this function to your `current_posts.module` file:

``` php
/**
 * Implements validation from the Form API.
 * 
 * @param $form
 *   A structured array containing the elements and properties of the form.
 * @param $form_state
 *   An array that stores information about the form's current state 
 *   during processing.
 */
function current_posts_form_validate($form, &$form_state){
  $max_num = $form_state['values']['current_posts_max'];
  if (!is_numeric($max_num)){
    form_set_error('current_posts_max', t('You must enter a number for the maximum number of posts to display.'));
  }
  elseif ($max_num <= 0){
    form_set_error('current_posts_max', t('Maximum number of posts to display must be positive.'));
  }
}
```

(Remember not to include the closing `?>` in your code.)

### Testing the data

First we retrieve the configuration setting from `$form_state` and save it into a variable. We then check to be sure it's a number. If not, `form_set_error()` goes into action, setting the element in the first argument with an error CSS class (red by default). It also displays a red box with the error message given in the second argument.

If the data passes the first check, we make sure it's a positive number. If not, we again call `form_set_error()` Notice that both our string literals for error messages are wrapped in `t()`.

### Check

Enable your module again and visit the configuration page. Experiment with entering values to see how the validation works on errors. Be sure to disable your module before you add more code.

### See also

- [Form API Quickstart Guide](http://drupal.org/node/751826)
- [Form generation](http://api.drupal.org/api/drupal/includes--form.inc/group/form_api/7)
- [drupal_build_form()](http://api.drupal.org/api/drupal/includes--form.inc/function/drupal_build_form/7)
- [form_set_error()](http://api.drupal.org/api/drupal/includes--form.inc/function/form_set_error/7)
