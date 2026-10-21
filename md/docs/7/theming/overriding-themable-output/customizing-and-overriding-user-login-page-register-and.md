---
title: "Customizing and Overriding User Login page, Register, and Password Reset in Drupal 6 and 7"
source_url: "https://www.drupal.org/docs/7/theming/overriding-themable-output/customizing-and-overriding-user-login-page-register-and"
page_type: page
last_updated: "Last updated on 31 August 2016"
published: "2008-12-23T20:10:47+00:00"
modified: "2016-08-31T14:15:55+00:00"
breadcrumb: ["Drupal 7", "Theming Drupal 7", "Overriding themable output"]
fetched: "2026-10-21T08:19:07Z"
raw: "raw/docs/7/theming/overriding-themable-output/customizing-and-overriding-user-login-page-register-and.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Customizing and Overriding User Login page, Register, and Password Reset in Drupal 6 and 7

Customizing the user login, register, and password reset pages is fairly simple, and uses the following concepts:

- preprocessing to set variables
- registration of functions in the theme registry
- creation of one or more theme templates.

**Step 1.**  
In the site theme directory, create or edit your template.php file.

**Step 2.**  
The first step is to implement hook_theme for your theme. In the template.php file for your theme, look for a function named `yourtheme_theme()` and modify it to add these return values. If the function doesn't exist, add the following:

*For D6:*

``` php
/**
 * Registers overrides for various functions.
 *
 * In this case, overrides three user functions
 */
function yourtheme_theme() {
  return array(
    'user_login' => array(
      'template' => 'user-login',
      'arguments' => array('form' => NULL),
    ),
    'user_register' => array(
      'template' => 'user-register',
      'arguments' => array('form' => NULL),
    ),
    'user_pass' => array(
      'template' => 'user-pass',
      'arguments' => array('form' => NULL),
    ),
  );
}
```

Notes about that code:

- Change the function name by replacing "yourtheme" with the name of your theme
- The template can be the same for all three. The example above uses a different template for each case: user-login, user-register, and user-pass
- The template names must use a dash, not an underscore
- Note: It's `user_pass` not `user_password`

*For D7:*

``` php
function yourtheme_theme() {
  $items = array();
    
  $items['user_login'] = array(
    'render element' => 'form',
    'path' => drupal_get_path('theme', 'yourtheme') . '/templates',
    'template' => 'user-login',
    'preprocess functions' => array(
       'yourtheme_preprocess_user_login'
    ),
  );
  $items['user_register_form'] = array(
    'render element' => 'form',
    'path' => drupal_get_path('theme', 'yourtheme') . '/templates',
    'template' => 'user-register-form',
    'preprocess functions' => array(
      'yourtheme_preprocess_user_register_form'
    ),
  );
  $items['user_pass'] = array(
    'render element' => 'form',
    'path' => drupal_get_path('theme', 'yourtheme') . '/templates',
    'template' => 'user-pass',
    'preprocess functions' => array(
      'yourtheme_preprocess_user_pass'
    ),
  );
  return $items;
}
```

Notes about the D7 version:

- The 'path' lines tell Drupal where to find the .tpl.php files. This is optional, and in the code above, 'path' tells Drupal to find the files in the templates subdirectory of the theme's base directory.
- Note the "\_form" added to the user_register element.
- Note: As it is the case for D6, it's `user_pass` not `user_password`

**Step 3.**  
Now you implement three preprocess functions. There may be more concise ways to code this, but this works very well and is easy to read, so here we go!

*For D6:*

``` php
function yourtheme_preprocess_user_login(&$variables) {
  $variables['intro_text'] = t('This is my awesome login form');
  $variables['rendered'] = drupal_render($variables['form']);
}

function yourtheme_preprocess_user_register(&$variables) {
  $variables['intro_text'] = t('This is my super awesome reg form');
  $variables['rendered'] = drupal_render($variables['form']);
}

function yourtheme_preprocess_user_pass(&$variables) {
  $variables['intro_text'] = t('This is my super awesome insane password form');
  $variables['rendered'] = drupal_render($variables['form']);
} 
```

Notes about that code:

- Change the function name by replacing "yourtheme" with the name of your theme
- The line `$variables['intro_text']` adds the text that follows to the `$variables` array, which gets passed to the template as `$intro_text`
- The second line renders the form and adds that code to the `$variables` array, which gets passed to the template as `$rendered`

*For D7:*  
The code is even simpler for D7 because we don't need to pass a variable containing the form content we want rendered. The variable exists already in the \$vars array and can be rendered in the .tpl.php file.

``` php
function yourtheme_preprocess_user_login(&$vars) {
  $vars['intro_text'] = t('This is my awesome login form');
}

function yourtheme_preprocess_user_register_form(&$vars) {
  $vars['intro_text'] = t('This is my super awesome reg form');
}

function yourtheme_preprocess_user_pass(&$vars) {
  $vars['intro_text'] = t('This is my super awesome request new password form');
}
```

The above preprocess functions simply add a variable into the \$vars array that is then displayed in the .tpl.php file. Much more complex manipulation of the content of the render array is possible.

Please note, that the preprocess functions should go into the template.php file.

**Step 4.**  
Create template files to match the `'template'` values defined above.

*For D6*  
We need the following template files (make sure to use a dash, not an underscore) :

- `user-login.tpl.php`
- `user-register.tpl.php`
- `user-pass.tpl.php`

*For D7*  
Same as D6, except using `user-register-form.tpl.php` instead of `user-register.tpl.php`for the register form.

**Step 5.**  
Paste the following into user-login.tpl.php. Modify as necessary for `user-register.tpl.php` (D6) and `user-register-form.tpl.php` (D7):

*For D6:*

``` php
<p><?php print $intro_text; ?></p>

<div class="my-form-wrapper">
  <?php print $rendered; ?>
</div>
```

*For D7:*

``` php
<p><?php print render($intro_text); ?></p>
<div class="yourtheme-user-login-form-wrapper">
  <?php print drupal_render_children($form) ?>
</div>
```

Note the change to the syntax for causing Drupal to render the form. Also, the D7 sample uses a different class for the div, but that's just a matter of preference.

**Step 6.**  
Save your template.php file to the theme's main directory. Save your .tpl.php files in the same place for the D6 examples, or, in the case of the D7 examples, to the directory you specify in the 'path' element of the \$items array.

**Step 7.**  
Rebuild the cache. Go to *Administration \> Performance* and click on "Rebuild Cache" on the bottom of the page.

Now, the user login page will contain the new text from the preprocess function, and the tpl.php file(s) can be modified to suit the site's needs.
