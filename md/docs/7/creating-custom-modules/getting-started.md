---
title: "Getting started"
source_url: "https://www.drupal.org/docs/7/creating-custom-modules/getting-started"
page_type: page
last_updated: "Last updated on 30 October 2019"
published: "2011-02-27T00:56:04+00:00"
modified: "2019-10-30T13:57:51+00:00"
breadcrumb: ["Drupal 7", "Creating custom modules in Drupal 7"]
fetched: "2026-10-21T07:20:54Z"
raw: "raw/docs/7/creating-custom-modules/getting-started.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Getting started

**Main topic described: *module file name and location***

In this tutorial, we'll create a module that displays links to content, such as blog entries or forum discussions, that were created within the last week. This page describes how to create the initial module file and directory.

### Before you begin

If you want PHP to help identify your mistakes on your testing site, try the settings in [Showing all errors while developing](http://drupal.org/node/1056468).

### Name your module

The first step in creating a module is to choose a "short name" for it. This short name will be used in all file and function names in your module; it must start with a letter, and contain only lower-case letters and underscores. For this example, we'll choose "current_posts" as the short name. **Important note:** Be sure you follow these guidelines and do not use upper case letters in your module's short name, since it is used for both the module's file name and as a function prefix. When you implement Drupal "hooks" (see later portions of tutorial), Drupal will only recognize your hook implementation functions if they have the same function name prefix as the name of the module file.

It's also important to make sure your module does not have the same short name as any theme you will be using on the site.

### Create a folder and a module file

Given that our choice of short name is "current_posts" :

1.  **Start the module by creating a folder in your Drupal installation at the path:**
    - `sites/all/modules/current_posts`

      *In Drupal 6.x and 7.x, `sites/all/modules` (or `sites/all/modules/contrib` and `sites/all/modules/custom)` is the preferred place for non-core modules ` with ``sites/all/themes` (or `sites/all/themes/contrib` and `sites/all/themes/custom`) for non-core themes. By placing all site-specific files in the `sites` directory, this allows you to more easily update the core files and modules without erasing your customizations. Alternatively, if you have a multi-site Drupal installation and this module is for only one specific site, you can put it in `sites/your-site-folder/modules`.*
2.  **Create the info file for the module :**
    - Save it as `current_posts.info` in the directory `sites/all/modules/current_posts`

    - At a minimum, this file needs to contain the following...  

      ``` php
      name = Current Posts
      description = Description of what this module does
      core = 7.x
      ```
3.  **Create the PHP file for the module :**
    - Save it as `current_posts.module` in the directory `sites/all/modules/current_posts`
4.  **Add an opening PHP tag to the module :**
    - `<?php`
    - *Module files begin with [the opening PHP tag](http://us3.php.net/manual/en/language.basic-syntax.phpmode.php). Do not place the CVS ID tag in your module. It is no longer needed with drupal.org's conversion to Git. If the coder module gives you error messages about it, then that module has not yet been updated to drupal.org's Git conventions.*

The module is not operational yet: it hasn't been activated. We'll activate the module later in the tutorial.

### Coding standards

As per the [Coding standards](http://drupal.org/node/318), omit the closing `?>` tag. Including the closing tag may cause strange runtime issues on certain server setups. 

All functions in your module that will be used directly by Drupal are "hooks" named {modulename}\_{functionname}, where "functionname" is a pre-defined function name suffix. Drupal will call these functions to get specific data, so having these well-defined names means Drupal knows where to look. We will come to hooks in a while.

### LICENSE.txt

Do not include a LICENSE.txt (or similar) file. The packaging script will add this.

### See also

- [Showing all errors while developing](http://drupal.org/node/1056468)
- [Opening PHP tag](http://us3.php.net/manual/en/language.basic-syntax.phpmode.php)
- [Coding standards](http://drupal.org/node/318)
