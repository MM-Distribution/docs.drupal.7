---
title: "Modernizr.load() and Drupal: Basics"
source_url: "https://www.drupal.org/docs/7/theming/tools-and-best-practices/modernizrload-and-drupal-basics"
page_type: page
last_updated: "Last updated on 8 September 2016"
published: "2013-02-11T03:50:28+00:00"
modified: "2016-09-08T13:41:29+00:00"
breadcrumb: ["Drupal 7", "Theming Drupal 7", "Tools and best practices"]
fetched: "2026-10-21T08:56:08Z"
raw: "raw/docs/7/theming/tools-and-best-practices/modernizrload-and-drupal-basics.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Modernizr.load() and Drupal: Basics

Modernizr can also be a [conditional resource loader](http://modernizr.com/docs/#load), which means it can load different CSS or JS files based on the outcome of Modernizr tests. This capability is only present when you have selected **Modernizr.load** on the [download builder](http://modernizr.com/download/). The Drupal module automatically requires that this script loader be present in your build, so that the following API calls work no matter what.

Once you have Modernizr.load() available, the [Modernizr module](http://drupal.org/project/modernizr) offers multiple ways to create Modernizr.load() commands. No matter how you create them, the `Modernizr.load` objects will all print out on your page in the exact spot they should be, coming after the Modernizr `<script>` tag but before most of the page markup, meaning they begin to be fetched as soon as possible.

The Modernizr module collects calls to this API from three places:

- [theme `.info` files](http://drupal.org/node/1913830#info)
- [modules using `hook_modernizr_load()`](http://drupal.org/node/1913830#hook-load)
- [modules/themes that implement `hook_modernizr_load_alter()`](http://drupal.org/node/1913830#hook-load-alter)

## From within a theme's `.info` file

For people most familiar with theming, adding lines to an `.info` file might be the most comfortable method. It is easier to understand conditional loading if you consider that it already happens in every `.info` file you already create:

``` php
stylesheets[all][] = my/styles.css
```

This stylesheet declaration contains the word `all`, which defines the `media` attribute when the stylesheet is printed. You could easily change the output to be something like this:

``` php
stylesheets[screen and (min-width: 960px)][] = my/desktop.css
```

And now the condition is much less permissive than "all." In much the same way, the Modernizr module can accept instructions for Modernizr.load() commands using a similar syntax:

``` php
modernizr[Modernizr.boxshadow][yep][] = css/boxshadow.css
modernizr[Modernizr.boxshadow][nope][] = css/no-boxshadow.css
```

...becomes...

``` php
Modernizr.load({
  'test' => Modernizr.boxshadow,
   'yep' => 'css/boxshadow.css',
  'nope' => 'css/no-boxshadow.css'
});
```

## `hook_modernizr_load()`

Modules can implement a hook to create `Modernizr.load()` commands:

``` php
/**
 * Implements hook_modernizr_load().
 */
function MYMODULE_modernizr_load() {
  $load[] = array(
    'test' => 'Modernizr.boxshadow',
     'yep' => array('css/boxshadow.css'),
    'nope' => array('css/no-boxshadow.css'),
  );
  return $load;
}
```

...becomes the exact same Modernizr.load() command printed above.

## `hook_modernizr_load_alter()` (for template.php)

Using a hook inside template.php is identical to using a module hook. The minor difference is that themes cannot use regular hooks, and can only implement "alter" hooks. Modernizr module includes `drupal_alter()` hooks for both of its APIs, meaning template.php has access to the same options as modules:

``` php
/**
 * Implements hook_modernizr_load_alter().
 */
function MYTHEME_modernizr_load_alter(&$load) {
  $load[] = array(
    'test' => 'Modernizr.boxshadow',
     'yep' => array('css/boxshadow.css'),
    'nope' => array('css/no-boxshadow.css'),
  );
  return $load;
}
```

## Why would I do this?

There is a big performance gain by **not** downloading things on certain devices. For a more detailed explanation, read about how you can use `Modernizr.load` to download [one less jpeg](http://fourword.fourkitchens.com/article/one-less-jpg) and cut your bandwidth usage in half on mobile devices.
