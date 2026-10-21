---
title: "Preparing for a module configuration form"
source_url: "https://www.drupal.org/docs/7/creating-custom-modules/preparing-for-a-module-configuration-form"
page_type: page
last_updated: "Last updated on 6 July 2017"
published: "2011-03-30T21:06:07+00:00"
modified: "2017-07-06T23:34:37+00:00"
breadcrumb: ["Drupal 7", "Creating custom modules in Drupal 7"]
fetched: "2026-10-21T07:23:29Z"
raw: "raw/docs/7/creating-custom-modules/preparing-for-a-module-configuration-form.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Preparing for a module configuration form

**Drupal hook described: *hook_menu()*  
**Main function described: *drupal_get_form()*****

Now that we have a working module, we'd like to make it more flexible. With a busy site, we might not want to display all the links to content created last week. So we'll create a configuration form where the administrator can adjust how many links to display.

### Registering the URL

We will define our form using `hook_menu()`. The name of this hook is a bit misleading, as it does far more than simply assign menu items. Using this hook, modules register paths to define how URL requests are handled. Paths may be registered for URL handling only, or as a link to be placed in a menu (usually the Navigation menu). In this case, we will set a path that will make the form available from the *Configuration* page (`http://example.com/admin/config`).

`hook_menu()` implementations return an associative array whose keys define paths and whose values are an associative array of properties for each path. The definition for each path may include a page callback function, which is invoked when the registered path is requested. After we have set up our form in `hook_menu`, we will create the actual form by writing the page callback function we define here.

### Access check

`hook_menu()` also provides an important part of Drupal's security, as it performs user access checks. We would like only administrators to be able to access this form, and we'll check that permission here in `hook_menu()`. To minimize the number of permissions an administrator has to deal with, we'll use the core administration permission instead of creating a new custom permission.

In Drupal's menu system, 'title' and 'description' attributes are automatically translated. Throughout Drupal, you are encouraged to use the `t()` function on all string literals. This is one place where you must remember not to do that.

Here's the code:

``` php
/**
 * Implements hook_menu().
 */
function current_posts_menu() {
  $items = array();

  $items['admin/config/content/current_posts'] = array(
    'title' => 'Current posts',
    'description' => 'Configuration for Current posts module',
    'page callback' => 'drupal_get_form',
    'page arguments' => array('current_posts_form'),
    'access arguments' => array('access administration pages'),
    'type' => MENU_NORMAL_ITEM,
  );

  return $items;
}
```

### Setting properties

The path set as the array key for `$items` becomes the path to our form. It must take the form of an internal Drupal path with no leading or trailing slashes. We begin the path with `admin/config` to tell Drupal to include a link to this form on the site administration page (*Configuration* or `http://example.com/admin/config`). `content` tells Drupal which section of this page the link belongs to, in this case, *Content authoring*. You can choose to add your form to any one of the default sections (*content, date, development, media, people, regional, search, services, system, user-interface*) by including its path name here.

Next comes the value, the associative array that lists properties of the item. `title` and `description`, as noted previously, are without the `t()` function. We include the administrator permission under `access arguments`, and the value of `type` is the default. This listing will not appear in any menu, only on the *Configuration* page.

### Add configuration button in Modules page

In your current_posts.info file add the following line to create a linked button to your configuration page in the modules page.

``` php
name = Current Posts
description = A block module that lists links to recent posts.
core = 7.x

; NEW LINE
configure = admin/config/content/current_posts
```

### Declaring the form

`page callback` tells Drupal what to call when the link is requested, in this case, `drupal_get_form`, the "key" function in the Form API. (Note that the trailing parentheses are not included in the call to `drupal_get_form`.)

`page arguments` values are passed to that function. By assigning `current_posts_form`, we define that as both the form ID and the name of the function that will create our settings form. As the name of a function, it must follow PHP variable naming conventions, with no spaces or hyphens. To prevent name collision, always start the function name with the name of your module, followed by an underscore.

We'll begin to explore the Form API as we build that function in the next part of the tutorial.

### See also

- [hook_menu()](http://api.drupal.org/api/drupal/modules--system--system.api.php/function/hook_menu/7)
- [drupal_get_form()](http://api.drupal.org/api/drupal/includes--form.inc/function/drupal_get_form/7)
