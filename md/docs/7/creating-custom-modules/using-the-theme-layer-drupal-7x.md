---
title: "Using the theme layer (Drupal 7.x)"
source_url: "https://www.drupal.org/docs/7/creating-custom-modules/using-the-theme-layer-drupal-7x"
page_type: page
last_updated: "Last updated on 23 December 2016"
published: "2010-10-06T21:45:20+00:00"
modified: "2016-12-23T07:08:31+00:00"
breadcrumb: ["Drupal 7", "Creating custom modules in Drupal 7"]
fetched: "2026-10-21T07:27:25Z"
raw: "raw/docs/7/creating-custom-modules/using-the-theme-layer-drupal-7x.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Using the theme layer (Drupal 7.x)

A well-made Drupal module allows all elements of its presentation to be overridden by the theme of the site on which it is used. In order for this theme layer to be usable, a module must be written to take advantage of it.

The first step is that *logic* must be separated as much as possible from *presentation*. To accomplish this, modules do as much of the work on the data as possible, and hand that data off to the presentation layer. Modules then provide **default theme implementations** that provide the basic presentation and serve as a basis for themes that wish to provide an alternate presentation. This is handled through the `theme()` function. Every chunk of output that is themed through the `theme()` function is called a *theme hook*. There are two ways to provide a default implementation. The easier way is to provide a *function*, and the recommended way is to provide a *template* and a corresponding preprocessor function. We'll expand on this in a little bit.

Ideally, your module won't produce a single line of HTML output that is not in a theme implementation. In reality, administrative pages and very small items may not necessarily be processed through a theme function \[`theme()`\], but a sign of a well written module includes easily modified presentation that in all places processes through the `theme()` function.

## Registering theme hooks

In order to utilize a theme hook, your module first has to register that this exists. (This is a change starting in Drupal 6; this registration is necessary due to the amount of time automatic discovery of alternate implementations takes; by registering, this discovery can be done only when needed, and then is always available.)

Your module's `hook_theme()` (see [the hook API documentation](http://api.drupal.org/api/group/hooks/7) for details on hooks) will return a list of all theme hooks that your module implements. A simple `hook_theme` implementation might look like this:

``` php
function forum_theme() {
  return array(
    'forums' => array(
      'template' => 'forums',
      'variables' => array('forums' => NULL, 'topics' => NULL, 'parents' => NULL, 'tid' => NULL, 'sortby' => NULL, 'forum_per_page' => NULL),
    ),
//...
  );
}
```

This registration tells us that a theme hook named `forums` is implemented. The default implementation is a template. Because there are different kinds of template engines, this registration does not include the extension used by the engine, though Drupal core only supports PHPTemplate templates for modules. These template files have the extension '.tpl.php'.

It also tells us that the `forums` theme function takes 6 variables (or arguments), and they all default to NULL. (All arguments must be given defaults as we have no way to assure that a `theme('forums', ...)` call will provide the proper information. If in doubt, make the default NULL). These arguments are translated into the named variables for the template. When calling this theme hook, an author might write:

``` php
  $output = theme('forums', array('forums' => $forums, 'topics' => $topics, 'parents' => $parents, 'tid' => 17, 'sortby' => 'ASC', 'forums_per_page' => 25));
```

If the 'template' had been left off of the hook_theme() definition, the theme hook's default implementation would be assumed to be a function named 'theme_forums'.

There are more options that can be set here, but these two are by far the most important. For more information, see the [hook_theme](http://api.drupal.org/api/function/hook_theme/7) documentation.

## Implementing default templates

When implemented as a template, the .tpl.php file is required. It should be in the same directory as the .module file (though the 'path' directive can be used to place these templates in another directory or a sub-directory).

Templates should be as much pure HTML as possible, but there are a few functions that are explicitly encouraged in your templates:

- [t()](http://api.drupal.org/api/function/t/7): modules should always provide proper translatability, and templates are no exception. Themers need to have the direct text to work with and translators need all of the text to be passed through `t()`.
- [format_date()](http://api.drupal.org/api/function/format_date/7): since this function is, really, a presentation function, the presentation layer is the appropriate place for it.

For other functions, consider whether or not they really are needed at the presentation layer. If they are not, they can be used in the preprocessor layer. All templates may have an optional preprocess function, named `template_preprocess_HOOK`. For example, for our `forums` theme hook above, its preprocess function will be named [template_preprocess_forums()](http://api.drupal.org/api/function/template_preprocess_forums/7).

The purpose of the preprocess function is to perform any logic that needs to be performed to make data presentable, and to sanitize any data so that it is safe to output. It is **critically important** that your output be [secure](http://drupal.org/writing-secure-code) and not contain XSS (Cross Site Scripting) vulnerabilities. And since data that is output often comes from users, this data **must** be sanitized before it is output. Since we assume that themers are not necessarily developers, we must assume that they are not going to fully understand how to do this; but that's ok, because we can sanitize data in the preprocess function by running it through [check_plain](http://api.drupal.org/api/function/check_plain/7), [check_markup](http://api.drupal.org/api/function/check_markup/7), [filter_xss_admin](http://api.drupal.org/api/function/filter_xss_admin/7) or other output sanitizing functions.

Here is a simple example [from Poll module](http://api.drupal.org/api/function/template_preprocess_poll_bar/7):

``` php
function template_preprocess_poll_bar(&$variables) {
  if ($variables['block']) {
    $variables['theme_hook_suggestions'][] = 'poll_bar__block';
  }
  $variables['title'] = check_plain($variables['title']);
  $variables['percentage'] = round($variables['votes'] * 100 / max($variables['total_votes'], 1));
}
```

First, note that the preprocessor function takes a reference to an array of variables. This array will be seeded with the arguments that were sent via the `theme()` and named by the 'arguments' section of the hook registration. Since this is a reference, simply modifying this array is enough to transport those changes to the template that accompanies it.

This example illustrates three important concepts:

1.  The 'title' field is unsafe, because it comes from user input. It is run through check_plain so that the template may safely output it.
2.  The theme hook receives the total number of votes and the number of votes for just that item, but the template wants to display a percentage. That kind of work shouldn't be done in a template; instead, the math is performed here. The variables still exist, though; a themer overriding this could easily choose to display something other than a percentage.
3.  The special variable 'theme_hook_suggestions' can be used to provide alternative template files to use. This is an array of hook names, and it is *last in, first out*, which means the last item added to the array will be the first one used. If a template doesn't exist, it will use the next one in the list. The special double underscore in this example is a shorthand way of indicating this– it does not look for a hook name with two underscores or a template with two dashes, rather, it will look for (in this template file case) first poll-bar-block.tpl.php, and failing to find that it will drop the part after the double underscores and it will look for poll-bar.tpl.php.

[Theme Developer module](/project/devel_themer), which is part of the devel project, includes a *template log* feature which outputs at bottom of page all the template files which could have been used to theme the current page. This may be handy while building your module, but even more so when themeing a site. Also, don't miss its Themer information popup.

**Note**: Template files should be named with hyphens instead of underscores. If the theme hook is 'forum_list', the template file should be named 'forum-list.tpl.php'. Also if you are planning to use preprocess functions, do not use hyphens in your theme hook name.

## Implementing theme functions

Drupal allows you to use functions for your default theme implementations. This is somewhat faster performance than loading template files. New in Drupal 7, theme functions can have preprocess functions just like templates. Copying and modifying template files are still considered more friendly for themers than overriding theme functions in template.php.

Theme functions are named by prepending 'theme\_' to the name of the hook. The arguments given to theme('hook') will be passed straight through, unaltered. The defaults specified in the hook registration will not be provided here; they must be provided as normal PHP argument defaults.

``` php
/**
 * Implements hook_theme().
 */
function dashboard_theme() {
  return array(
    'dashboard' => array(
      'render element' => 'element',
    ),
// ...
  );
}
```

And the function:

``` php
/**
 * Returns HTML for the entire dashboard.
 *
 * @param $variables
 *   An associative array containing:
 *   - element: A render element containing the properties of the dashboard
 *     region element, #dashboard_region and #children.
 *
 * @ingroup themeable
 */
function theme_dashboard($variables) {
  extract($variables);
  drupal_add_css(drupal_get_path('module', 'dashboard') . '/dashboard.css');
  return '
```

`' . $element['#children'] . '`

`'; } `

Themers can override this function by creating a function named `themename_dashboard()`.

## Dynamic theming

In addition to being able to specify alternate templates in a preprocess function, you may also create dynamic theming implementations using wildcards. There are two steps in this process.

First, in `hook_theme`, you can specify a pattern. Patterns are simple regular expressions. ^ (beginning of line) is assumed, but \$ (end of line) is not. To signify the dynamic portion of the pattern, a double underscore is the general convention; this is not required but it is highly recommended.

Second, when calling the theme() function, instead of a string for the first argument you may pass an array. This array is much like theme_hook_suggestions above, but this one is *first in, first out* so the first one seen will be used.

For a practical example, the module Views likes to let each view be themed by name. Upon registration, the hook 'views_view' would register with the pattern 'views_view\_\_'. When theming that view, Views would call:

``` php
  $output = theme(array("views_view__$view->name", 'views_view'), $view);
```

Views will implement a default view for views_view; if a theme registers 'views_view\_\_foo' and Views themes a view named 'foo', the specific override will activate and be used instead. Unlike the 'theme_hook_suggestions' variable in the preprocessor function, this works for both theme functions as well as templates.

More on [preprocess functions](/node/223430).

## theme('table') and theme('item_list')

Drupal provides a few helpers to build complex HTML constructs easily. These are very useful features, and by using them it is easy to create a consistent look on tables and lists. The downside is that they are not readily accessible to a themer. Instead, they place code that should be at the presentation layer into the logic layer, and only advanced themers are able to do anything with it.

These functions are more acceptable for administration pages.

When creating output that is likely to be changed, it is best to avoid the use of these constructs and create the tables and lists with real HTML code. The forum themes are perfect examples of how to accomplish this and still create HTML code that is consistent.

## Function name suggestions with double underscores

An even bigger problem with using common provided theme functions such as theme('item_list') is that a theme probably does not want to override every [theme_item_list()](http://api.drupal.org/api/function/theme_item_list/7) for every list output by Drupal anywhere, but only the one in our module. Therefore, instead of simply `theme('item_list')`, we can use `theme('item_list__mymodule__main', $items)` which would make it possible for a theme to implement `themename_item_list__mymodule__main()` or `themename_item_list__mymodule() to override item_list()` only for that specific instance.

An alternative to the double underscore convention is to explicitly name each hook that could be used, in the order of our preference, in an array:

``` php
  theme(array('somemodule_itemlist_alternative', 'item_list'), $items);
```

## Having changes to code take effect

When new theming functions are added, we must clear the [theme registry](/node/173880#theme-registry) to see them.

## See also

- [Theme handbook](/theme-guide)
- [Drupal API documentation for hook_theme()](http://api.drupal.org/api/function/hook_theme/7)
- [Drupal API documentation for theme()](http://api.drupal.org/api/function/theme/7)
