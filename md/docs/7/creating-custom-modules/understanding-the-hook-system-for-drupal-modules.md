---
title: "Understanding the hook system for Drupal modules"
source_url: "https://www.drupal.org/docs/7/creating-custom-modules/understanding-the-hook-system-for-drupal-modules"
page_type: page
last_updated: "Last updated on 23 December 2016"
published: "2001-10-25T14:18:20+00:00"
modified: "2016-12-23T08:07:22+00:00"
breadcrumb: ["Drupal 7", "Creating custom modules in Drupal 7"]
fetched: "2026-10-21T07:49:24Z"
raw: "raw/docs/7/creating-custom-modules/understanding-the-hook-system-for-drupal-modules.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Understanding the hook system for Drupal modules

A Drupal module is a collection of files containing some functionality and is written in PHP. Because the module code executes within the context of the site, it can use all the functions and access all variables and structures of Drupal core. In fact, a module is no different from a regular PHP file that can be independently created and tested and then used to drive multiple functionalities.

This approach allows Drupal core to call at specific places certain functions defined in modules and enhance the functionality of core. The places where code can be executed are called "hooks" and are defined by a fixed interface.

## About hooks

Hooks are how modules can interact with the core code of Drupal. They make it possible for a module to define new urls and pages within the site (hook_menu), to add content to pages (hook_block, hook_footer, etc.), to set up custom database tables (hook_schema) and more. [This page](http://api.drupal.org/api/group/hooks "Drupal API reference - Hooks") lists the hooks provided in the core, but modules can define hooks of their own. For example, the cck module defines hook_field_info, which can be used by modules that want to define a new type of content field. Most modules that define hooks will also provide documentation about them.

Hooks occur at various points in the thread of execution, where Drupal seeks contributions from all the enabled modules. For example, when a user visits a help page on a Drupal site, as Drupal builds the help page it will give each module a chance to contribute documentation about itself. It does this by scanning all the module code for functions that have the name mymodule_help(\$path, \$arg), where "mymodule" is the module's name, e.g., the block module's help hook is called block_help and the node module's help hook is called node_help. The hook may provide parameters; hook_help's parameters \$path and \$arg allow the developer to determine what page or pages the help messages will appear on.

A hook can be thought of as an event listener in the sense that an event triggers an action. The event in Drupal, such as deleting a node, would trigger the hook "hook_delete". If your module implemented hook_delete, that function would run when a node deletion occurred. As an example, your function might be to decrease the count of the total number of nodes, so when a node was deleted, your function would be called and lower the count by 1.

See also [the overview of module hooks](http://api.drupal.org/api/group/hooks "Drupal API reference - Hooks"), in the Drupal API Reference. You might want to check out also this [good article discussing how Drupal module/hook system works](http://alanstorm.com/drupal_module_hooks), using simple PHP constructs/snippets.
