---
title: "How to Make a Simple Module with a Form and Menu Link"
source_url: "https://www.drupal.org/docs/7/howtos/how-to-make-a-simple-module-with-a-form-and-menu-link"
page_type: page
last_updated: "Last updated on 6 April 2018"
published: "2012-01-27T23:49:58+00:00"
modified: "2018-04-06T16:28:49+00:00"
breadcrumb: ["Drupal 7", "Site building and development HowTos for Drupal 7"]
fetched: "2026-10-21T08:05:25Z"
raw: "raw/docs/7/howtos/how-to-make-a-simple-module-with-a-form-and-menu-link.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# How to Make a Simple Module with a Form and Menu Link

This guide will show you how to add a form to your website that is accessed through its own URL. This guide will go over module creation, form creation, and the menu hook function.

**Creating the module structure**  
The first step in creating the module is to create a folder for the module. You should put this in "sites/all/modules/{name of your module}." Keep in mind that whenever I say "{name of your module}," you should insert the name of your module. For example, we will use the module directory "sites/all/modules/form_example."

Now, create two empty text files called "{name of your module}.module" and "{name of your module}.info."

These two files are required by your module. The .info file contains information about what your module does, while the .module file contains the actual code including hooks. Hooks are functions with special names that will be called by Drupal when actions occur. For example "form_example_menu()" is called when menu information is gathered. In many examples, you will see names such as "hook_menu()" or "my_theme_menu()" and in these cases "my_theme" and "hook" should be replaced by the name of your module or theme.

**Build the basic module files**

Here is what we will put into the form_example.info file. This tells Drupal and users about your module.

``` php
core = "7.x"
description = "An example module used to learn module development and forms creation."
name = "Form Example Module"
```

There are more options that you can put in the .info file, but the ones above should be added.

Here is the start of our form_example.module file. This will create a very basic form that only has one field, a submit button.

``` php
<?php
function form_example_form($form, &$form_state) {
  
  $form['submit_button'] = array(
    '#type' => 'submit',
    '#value' => t('Click Here!'),
  );
  
  return $form;
}
?>
```

Note: Do not include the last "?\>" part of the PHP code and leave a trailing blank line at the end of the file. This is the Drupal standard.

The module right now contains one function that will create a form. It is important to note that the function takes the inputs \$form and a reference &\$form_state. This function will be called when Drupal tries to build the form "form_example_form."

The process for creating a form is mainly two steps. The first is to build an associative array \$form that contains all the fields. The second step is to return that \$form variable.

To add a field, you set the variable \$form\[{name of your field}\] = array(); Each field can then have a number of attributes, such as "#type" and "#value." Most of these attributes are named with a preceding "#" sign.

The field we added above is a submit button with the text "Click Here!" on the button. Note that t() will output text and is a Drupal function that plays nice with translation.

Now that we have a form, we need to add two more functions: form_example_form_validate, and form_example_form_submit. These two functions are hook functions that will be called when Drupal validates the form and when it submits the form (assuming it validated).

form_example.module:

``` php
<?php
function form_example_form($form, &$form_state) {
  
  $form['submit_button'] = array(
    '#type' => 'submit',
    '#value' => t('Click Here!'),
  );
  
  return $form;
}

function form_example_form_validate($form, &$form_state) {
}

function form_example_form_submit($form, &$form_state) {
}
?>
```

You will note that these three functions take the same variables. \$form is the original form information and can be seen as the original structure of the form. \$form_state holds all of the submitted values as well as other information, some of which you can add yourself. These two functions need to named similar to the other form, but with "validate" and "submit" at the end.

We want to see the form!!! We will add a menu link to this form.

form.example.module

``` php
<?php

function form_example_menu() {
  $items = array();

  $items['examples/form-example'] = array( //this creates a URL that will call this form at "examples/form-example"
    'title' => 'Example Form', //page title
    'description' => 'A form to mess around with.',
    'page callback' => 'drupal_get_form', //this is the function that will be called when the page is accessed.  for a form, use drupal_get_form
    'page arguments' => array('form_example_form'), //put the name of the form here
    'access callback' => TRUE
  );

  return $items;
}

function form_example_form($form, &$form_state) {
  
  $form['submit_button'] = array(
    '#type' => 'submit',
    '#value' => t('Click Here!'),
  );
  
  return $form;
}

function form_example_form_validate($form, &$form_state) {
}

function form_example_form_submit($form, &$form_state) {
}
?>
```

Now enable your module and try to access the link. You will probably need to clear the cache.

**Add more functionality to the form.**

Now we will add one more field to the form.

form_example.module

``` php
<?php

function form_example_menu() {
  $items = array();

  $items['examples/form-example'] = array( //this creates a URL that will call this form at "examples/form-example"
    'title' => 'Example Form', //page title
    'description' => 'A form to mess around with.',
    'page callback' => 'drupal_get_form', //this is the function that will be called when the page is accessed.  for a form, use drupal_get_form
    'page arguments' => array('form_example_form'), //put the name of the form here
    'access callback' => TRUE
  );

  return $items;
}

function form_example_form($form, &$form_state) {
  
 $form['price'] = array(
    '#type' => 'textfield', //you can find a list of available types in the form api
    '#title' => 'What is Your Price?',
    '#size' => 10,
    '#maxlength' => 10,
    '#required' => TRUE, //make this field required 
  );

  $form['submit_button'] = array(
    '#type' => 'submit',
    '#value' => t('Click Here!'),
  );
  
  return $form;
}

function form_example_form_validate($form, &$form_state) {
}

function form_example_form_submit($form, &$form_state) {
}
?>
```

Here we have added a new text field and made it required. We have also set the maximum length. You'll see if you try to submit the form, that Drupal will automatically produce an error for the user if they don't fill in the required fields. We will add some more validation in the next step.

**Add validation**

form_example.module

``` php
<?php

function form_example_menu() {
  $items = array();

  $items['examples/form-example'] = array( //this creates a URL that will call this form at "examples/form-example"
    'title' => 'Example Form', //page title
    'description' => 'A form to mess around with.',
    'page callback' => 'drupal_get_form', //this is the function that will be called when the page is accessed.  for a form, use drupal_get_form
    'page arguments' => array('form_example_form'), //put the name of the form here
    'access callback' => TRUE
  );

  return $items;
}

function form_example_form($form, &$form_state) {
  
 $form['price'] = array(
    '#type' => 'textfield', //you can find a list of available types in the form api
    '#title' => 'What is Your Price?',
    '#size' => 10,
    '#maxlength' => 10,
    '#required' => TRUE, //make this field required 
  );

  $form['submit_button'] = array(
    '#type' => 'submit',
    '#value' => t('Click Here!'),
  );
  
  return $form;
}

function form_example_form_validate($form, &$form_state) {
  if (!($form_state['values']['price'] > 0)){
    form_set_error('price', t('Price must be a positive number.'));
  }
}

function form_example_form_submit($form, &$form_state) {
}
?>
```

You will now see that the form will not submit unless the price is a positive number. We do this by checking the value of price, in \$form_state\['values'\]\[{name of your field}\]. There are similar variables for all of your fields.

We then set an error with form_set_error. Adding this error will alert Drupal that the form did not pass validation.

**What to do when your form is submitted?**  
From this point, you will want to either save the form data, send an email, or display some information. That is beyond the scope of this How-To at this point.

I have built some module "tools" or "calculators" using the above method and included the calculation steps in the submit function. You can set the variable "\$form_state\['rebuild'\] = TRUE;" in the submit function so that Drupal does not clear the form. You can, therefore, edit the \$form_state to change a "markup" field type to have your output.

This can also be done with AJAX so that the form displays the calculated values without a page load. That gets a little more complicated and may be added as a separate How To.

**Conclusions**  
Hopefully, this is helpful for people interested in writing a module or adding a form to a module.
