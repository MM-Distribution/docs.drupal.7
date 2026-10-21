---
title: "Writing comments and implementing your first hook"
source_url: "https://www.drupal.org/docs/7/creating-custom-modules/writing-comments-and-implementing-your-first-hook"
page_type: page
last_updated: "Last updated on 1 March 2017"
published: "2011-03-17T04:38:13+00:00"
modified: "2017-03-01T08:11:45+00:00"
breadcrumb: ["Drupal 7", "Creating custom modules in Drupal 7"]
fetched: "2026-10-21T07:21:56Z"
raw: "raw/docs/7/creating-custom-modules/writing-comments-and-implementing-your-first-hook.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Writing comments and implementing your first hook

**Drupal hook described: *hook_help()***

### Comments in Drupal modules

It's always a good idea to document how your module works in comments. Drupal uses Doxygen to draw documentation from source code, so contrib modules on drupal.org follow strict comment guidelines. See [Doxygen and comment formatting conventions](http://drupal.org/node/1354) for more details. Following these guidelines is beneficial to anyone looking at your code even if it's not strictly necessary for your situation.

Your first comment in your .module file:

``` php
/**
 * @file
 * A block module that displays recent blog and forum posts.
 */
```

@file signifies that this comment pertains to the entire file. The doc block begins with a slash and two asterisks (/\*\*) and ends with one asterisk and a slash (\*/). Following Drupal guidelines, we will introduce each function in the module with such a comment.

### Implementing your first hook

Hooks are fundamental to Drupal modules. They allow you to integrate your module into the actions of Drupal core. If you missed it, go back and read about hooks in [Introduction to Drupal modules](http://drupal.org/node/292). Drupal's API documentation provides a [list of available module hooks](https://api.drupal.org/api/drupal/includes%21module.inc/group/hooks/7.x).

Your first hook is `hook_help`. This hook is recommended for inclusion in all contrib modules. `hook_help` provides help and additional information about the module to the user. To implement any hook in Drupal, replace "hook" in the hook name with your module's short name, and create a function in the .module file with that name. So, to implement `hook_help()` in our example module, we create a function called `current_posts_help()` in the current_posts.module file:

``` php
function current_posts_help($path, $arg) {

}
```

The `$path` parameter provides context for the help: where in Drupal or the module the user is when they are accessing help. The recommended way to process this variable is with a switch statement. This code pattern is common in Drupal modules. Here is an abbreviated implementation of this function for your module, along with its doc block comment:

``` php
/**
 * Implements hook_help().
 *
 * Displays help and module information.
 *
 * @param path 
 *   Which path of the site we're using to display help
 * @param arg 
 *   Array that holds the current path as returned from arg() function
 */
function current_posts_help($path, $arg) {
  switch ($path) {
    case "admin/help#current_posts":
      return t("Displays links to nodes created on this date"); 
      break; 
  }
}
```

A switch statement is used here because it is typical for the help function to offer more than one page containing help text. The `admin/help#modulename` case is used by Drupal core to link from the main help page (`/admin/help` or `?q=admin/help`). You will eventually want to add more text to provide a better help message to the user; see [Help text standard](http://drupal.org/node/632280) for the complete recommendation. The` t()` function that wraps the text marks it for translation. This function not only allows for translation, it can give your code an added layer of security. See [Localization API](http://drupal.org/node/322729) for more information.

### Check

Look again at the module list by clicking *Modules* on the Toolbar in your Drupal installation. Enable the module and click 'Save configuration'. Close and reopen the *Modules* page, find your module in the list, and you should see a link to 'Help' on the right. (If you don't see this link, make sure the Drupal core 'Help' module is enabled.) Click it to see the help text returned by `current_posts_help`. You can also follow the *Help* link in the toolbar (`http://example.com/admin/help`) and find your help link listed with the others on that page.

Disable your module and save ('Save configuration' button). **Important**: Be sure you follow that last step and disable your module and save, or new partial code in your module could break your site.

### See also

- [Doxygen and comment formatting conventions](http://drupal.org/node/1354)
- [hook_help](http://api.drupal.org/api/function/hook_help)
- [Help text standard](http://drupal.org/node/632280)
- [Localization API](http://drupal.org/node/322729)
