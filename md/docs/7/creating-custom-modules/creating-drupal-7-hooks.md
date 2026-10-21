---
title: "Creating Drupal 7 hooks"
source_url: "https://www.drupal.org/docs/7/creating-custom-modules/creating-drupal-7-hooks"
page_type: page
last_updated: "Last updated on 12 November 2017"
published: "2014-07-14T14:05:19+00:00"
modified: "2017-11-12T04:06:09+00:00"
breadcrumb: ["Drupal 7", "Creating custom modules in Drupal 7"]
fetched: "2026-10-21T07:21:41Z"
raw: "raw/docs/7/creating-custom-modules/creating-drupal-7-hooks.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Creating Drupal 7 hooks

## The Drupal 7 Hook Concept

Drupal’s [hook system](http://api.drupal.org/api/drupal/includes!module.inc/group/hooks/7) allows modules to interact with and alter data of other modules, or even Drupal core itself.

To use a hook system you must create the hook and call their implementations.

After reading this page you will have a solid understanding of the concept of hook, and will have seen a few basic examples.

### Creating a Drupal 7 hook (and calling their implementations)

Creating a hook and calling their implementations can be done by using one of the following functions (not all included): [drupal_alter()](https://api.drupal.org/api/drupal/includes%21module.inc/function/drupal_alter/7), [module_invoke_all()](https://api.drupal.org/api/drupal/includes%21module.inc/function/module_invoke_all/7) and [module_invoke()](https://api.drupal.org/api/drupal/includes%21module.inc/function/module_invoke/7)

### Implementing a Drupal 7 hook

To be able to call it you need to implement a drupal 7 hook.

When calling a hook, "hook" is always replaced with the name of your module. For example, in test.module, hook_help() would be defined as test_help().

### Drupal 7 Hook Types:

In common practice, there are two types of hooks that you can create:

1.  **Alter hooks**:  
    a common way to edit the contents of a particular object or variable by getting variables in the hook by reference, typically by using [drupal_alter()](https://api.drupal.org/api/drupal/includes%21module.inc/function/drupal_alter/7)
2.  **Intercepting hooks**:  
    allowing external modules to perform actions during the execution, can not get variables by reference, typically by using [module_invoke_all()](https://api.drupal.org/api/drupal/includes%21module.inc/function/module_invoke_all/7) and [module_invoke()](https://api.drupal.org/api/drupal/includes%21module.inc/function/module_invoke/7)

## Examples:

#### Example \#1 (Simple Invoking)

``` php
  // Calling all modules implementing 'hook_name':
  module_invoke_all('hook_name');
```

#### Example \#2 (Invoking a Particular one)

``` php
  // Calling a particular module's 'hook_name' implementation:
  module_invoke('module_name', 'hook_name');
  // @note: module_name comes without '.module'
  // @note: hook_name is the specific hook defined in that module 
```

#### Example \#3 (Collecting results in an array)

``` php
  $result = array();
  foreach (module_implements('hook_name') as $module) {
    // Calling all modules implementing hook_hook_name and 
    // Returning results than pushing them into the $result array:
    $result[] = module_invoke($module, 'hook_name');
  }
```

#### Example \#4 (Altering data using drupal_alter())

``` php
  $data = array(
    'key1' => 'value1',
    'key2' => 'value2',
  );
  // Calling all modules implementing hook_my_data_alter():
  drupal_alter('my_data', $data);
  // You should implement hook_my_data_alter() in all other modules in which you want to alter $data
```

#### Example \#5 (passing by reference: cannot use module_invoke())

``` php
  // @see user_module_invoke()
  foreach (module_implements('hook_name') as $module) {
    $function = $module . '_hook_name';
    // will call all modules implementing hook_hook_name
    // and can pass each argument as reference determined
    // by the function declaration
    $function($arg1, $arg2);
  }
```
