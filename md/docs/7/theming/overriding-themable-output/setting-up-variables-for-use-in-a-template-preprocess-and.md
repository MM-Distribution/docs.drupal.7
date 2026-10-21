---
title: "Setting up variables for use in a template (preprocess and process functions)"
source_url: "https://www.drupal.org/docs/7/theming/overriding-themable-output/setting-up-variables-for-use-in-a-template-preprocess-and"
page_type: page
last_updated: "Last updated on 24 April 2017"
published: "2008-02-18T20:24:28+00:00"
modified: "2017-04-24T09:51:20+00:00"
breadcrumb: ["Drupal 7", "Theming Drupal 7", "Overriding themable output"]
fetched: "2026-10-21T08:18:36Z"
raw: "raw/docs/7/theming/overriding-themable-output/setting-up-variables-for-use-in-a-template-preprocess-and.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Setting up variables for use in a template (preprocess and process functions)

The main role of the preprocessors is to set up variables to be placed within the template (.tpl.php) files. In Drupal 7 they apply to both templates and functions.

***Note:** Preprocessors are also used for providing [template suggestions](/node/223440).*

Every layer in Drupal from core, modules, engines and themes can have numerous preprocessors, each progressively building upon the variables before being rendered through template files. This keeps the template markup clean and easy to work with as most of the logic is kept inside these preprocessors.

Here are the preprocessors Drupal uses organized by render sequence:

1.  [template_preprocess Drupal 7](http://api.drupal.org/api/function/template_preprocess/7)  
    This is always added by core. The [variables generated here](/node/226776) are used for every templated hook.
2.  template_preprocess\_*hook *This is supplied by a module or core file that implements a theming hook. The initial generation of all the variables specific to this hook is usually done here.
3.  *moduleName*\_preprocess  
    Do not confuse this with the preprocessor before it. This allows modules that did not originally implement the hook to influence the variables. Applies to all hooks.
4.  *moduleName*\_preprocess\_*hook*  
    Same idea as the previous preprocessor but for specific hooks.
5.  *engineName*\_engine_preprocess  
    *- The preprocessor for theming engines. Applies to all hooks.*
6.  *engineName*\_engine_preprocess\_*hook*  
    Another preprocessor for theming engines but specific to a single hook.
7.  *engineName*\_preprocess  
    NOT RECOMMENDED. This is the first preprocessor that can be used inside the theme. It can be named after the theme engine the theme is running under. Applies to all hooks.
8.  *engineName*\_preprocess\_*hook*  
    NOT RECOMMENDED. Another preprocessor named after the engine but specific to a single hook.
9.  *themeName*\_preprocess  
    This one is named after the theme itself. Applies to all hooks.
10. *themeName*\_preprocess\_*hook*  
    Same as the previous preprocessor but for a specific hook.

There are many possibilities here for modifying the variables. In most cases, it is only the first two preprocessors that exist. The first adds the default baseline variables and the second adds a set specific to the theming hook. Contributed modules taking advantage of the preprocessor slots (3 & 4) should document their behavior. It will not be covered extensively here.

*While it is possible, the default PHPTemplate does not inject itself to this list. (5 & 6)*

Themes can start adding their preprocessors seventh in the list. The preprocess function should be added to the theme's template.php file. However, due to the problems listed below, it is recommended that themes use their own names as the prefix (9 & 10). It is possible to grow this list beyond the ten shown above by having sub-themes add preprocessors strictly through their theme name as it is shown in the last two examples.

*A few notes:*

- *There is an unfortunate design flaw/bug in the theme system when a theme is part of a base theme/sub-theme hierarchy. Any preprocess functions prefixed with engineName_preprocess will be run multiple times (once for each theme in the hierarchy) instead of just once. Not only is this wasting resources, it can also cause difficult-to-debug errors.*
- *The theme name (9 & 10) should **always be used for [themes](/node/225125)**. This minimizes any chance of a sub-theme redeclaring a function with an engineName_preprocess prefix and causing *fatal PHP errors due to duplicate functions*.*

Note that nothing should be [returned](http://us.php.net/return) from these functions and the variables have to be passed by [reference](http://us.php.net/manual/en/language.references.php) indicated by the ampersand before variables, e.g., *&*\$variables.

Since the variables set early on are run through all the latter preprocessors due to references, be careful that you do not inadvertently reset any added before your theme. It is fine to reset them, but doing so accidentally can keep you guessing what went wrong.

*Example set from a module implementing the hook of "foo":*

``` php
function template_preprocess_foo(&$variables) {
  $variables['foo_list'] = array(
    'list item 1',
    'list item 2',
    'list item 3',
  );
}
```

*And the preprocessor created from the theme to add to the variable set above:*

``` php
function drop_preprocess_foo(&$variables) {
  // Do not do this unless you mean to:
  $variables['foo_list'] = array('list item 4');
  
  // Instead do this:
  $variables['foo_list'][] = 'list item 4';
}
```

The variables that end up in the template file are the keys set within `$variables`. So, with the above example, the variable in the template would result in `$foo_list`.

When using a preprocessor not specific to a theming hook, a second parameter can be used which always passes the current hook. Using a more specialized preprocess function like the one shown above is easier to maintain but if there will be shared code for multiple theming hooks, you may want to opt for this instead.

``` php
function drop_preprocess(&$variables, $hook) {

  // Shared between the 'foo' and 'bar' theming hooks.
  if ($hook == 'foo' || $hook == 'bar') {
    $variables['foobar_item'] = 'foobar item';
  }

  // Specific to 'foo'.
  if ($hook == 'foo') {
    $variables['foo_item'] = 'foo item';
  }
  // Specific to 'bar'.
  elseif ($hook == 'bar') {
    $variables['bar_items'] = 'bar item';
  }
}
```

There are two sets of variable process functions. The first is the existing "preprocess" functions. The second is "process" functions which are run after preprocessors. All the various prefixes and suffixes apply to this second phase in the exact same way. This is useful when certain variables need to be worked on in two phases. For example, adding classes into an array for the "preprocess" phase then flattening them into a string in the "process" phase, so it's ready to print within a template.

So effectively they are the same thing but called in different phases. Preprocess functions are called first and changes are made then Process functions are then called at a later phase and allowed for changes to be made.

*Related HowTos and code snippets:*

- *[Additional preprocess functions for node types.](/node/337022)*
