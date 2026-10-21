---
title: "Drupal 7's code registry"
source_url: "https://www.drupal.org/docs/7/creating-custom-modules/drupal-7s-code-registry"
page_type: page
last_updated: "Last updated on 21 September 2021"
published: "2008-12-24T04:35:34+00:00"
modified: "2021-09-21T20:41:43+00:00"
breadcrumb: ["Drupal 7", "Creating custom modules in Drupal 7"]
fetched: "2026-10-21T07:26:39Z"
raw: "raw/docs/7/creating-custom-modules/drupal-7s-code-registry.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Drupal 7's code registry

Drupal 7 introduces a code registry - an inventory of all classes and interfaces for all enabled modules and Drupal's core files. The registry stores the path to the file that a given class or interface is defined in, and loads the file when necessary.

The registry loads classes and interfaces on demand, via php's built in class autoloading mechanism. This will cut down on the amount of code loaded per request, and reduce Drupal's memory footprint.

The only file unconditionally loaded by Drupal for a given module is `module_name.module`. Any code that must always be available without using the registry should be put in this file.

Include classes and interfaces by listing them with the files\[\] property in your .info file. See <https://www.drupal.org/node/542202#files>

All the files listed in .info files of currently enabled modules are parsed when modules are rebuilt (Only changed/new files in that list are added, for performance reasons).

The information is then stored in the {registry} and {registry_file} tables. The registry table in Drupal database holds the important information regarding the name of the Class/Interface or the function along with the name of the module that had implemented and the complete file path within the Drupal set up that contains the Class or Interface or the function name also.

The registry is rebuilt when modules are enabled or disabled in order to incorporate new code or remove the code from disabled modules. If you are developing new code with classes, make sure to rebuild the registry regularly so that new resources are incorporated. (Clearing all caches or calling [registry_rebuild()](http://api.drupal.org/api/drupal/includes--bootstrap.inc/function/registry_rebuild/7) directly both will do this.) Rebuilding an existing registry to incorporate new changes is not that expensive, as the registry will not reparse files that have the same path and modification time as the last build.

Under certain conditions, a stale file registry can lead to errors that block access to a site. The [Registry rebuild](http://drupal.org/project/registry_rebuild) project provides tools to help address this problem.

**Note** Files that do not contain classes and interfaces that might be put into use at any time by your module file do not need to be listed with the files\[\] property in your .info file. Instead, such code can continue to be loaded when you need it, such as through the [hook_menu()](http://api.drupal.org/api/drupal/modules--system--system.api.php/function/hook_menu/7)'s file property. If your module introduces hooks of its own, consider implementing [hook_hook_info()](http://api.drupal.org/api/drupal/modules--system--system.api.php/function/hook_hook_info/7) to allow other modules' hook implementations to be autoloaded.
