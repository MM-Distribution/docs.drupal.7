---
title: "Customize the default user registration form"
source_url: "https://www.drupal.org/docs/7/howtos/customize-the-default-user-registration-form"
page_type: page
last_updated: "Last updated on 14 February 2017"
published: "2012-09-09T09:23:44+00:00"
modified: "2017-02-14T12:45:19+00:00"
breadcrumb: ["Drupal 7", "Site building and development HowTos for Drupal 7"]
fetched: "2026-10-21T08:03:37Z"
raw: "raw/docs/7/howtos/customize-the-default-user-registration-form.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Customize the default user registration form

Firstly, in your theme's root directory add the following to template.php. If the file does not exist, create it.

``` php
function YOURTHEME_theme(&$existing, $type, $theme, $path){
  $hooks = array();
   // Make user-register.tpl.php available
  $hooks['user_register_form'] = array (
     'render element' => 'form',
     'path' => drupal_get_path('theme','YOURTHEME'),
     'template' => 'user-register',
     'preprocess functions' => array('YOURTHEME_preprocess_user_register_form'),
  );
  return $hooks;
}

function YOURTHEME_preprocess_user_register_form(&$vars) {
  $args = func_get_args();
  array_shift($args);
  $form_state['build_info']['args'] = $args; 
  $vars['form'] = drupal_build_form('user_register_form', $form_state['build_info']['args']);
}
```

## Account fields

Account fields are rendered following the pattern of the two required fields, 'name' and 'mail':

``` php
print render($form['account']['name']);
print render($form['account']['mail']);
```

## Profile2 Support

To load Profile2 fields into the user registration form manually, use this pattern:

``` php
print render($form['profile_theprofile_name']['field_thefield_name']);
```

Also, I make use of field group module (here) with Profile2 and noticed that I didn't need to include anything about the field group a Profile2 field is in to render that field.

## CAPTCHA

If you use the CAPTCHA module and need to build your own user-register.tpl.php you'll need this to render it:

``` php
  print render($form['captcha']);
```

This took me longer than it should of to figure it out.

## Submission

Lastly, if you want your form to actually be usable, the following snippet is required to build the form action stuff:

``` php
  print drupal_render($form['actions']);
  print drupal_render_children($form);
```

This page is a reference page spawned from [this](http://drupal.org/node/1211520) support thread in the Theme Development forum.
