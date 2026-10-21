---
title: "Specifying a custom permission for a new page"
source_url: "https://www.drupal.org/docs/7/creating-custom-modules/specifying-a-custom-permission-for-a-new-page"
page_type: page
last_updated: "Last updated on 20 December 2017"
published: "2011-04-06T14:17:07+00:00"
modified: "2017-12-20T15:06:23+00:00"
breadcrumb: ["Drupal 7", "Creating custom modules in Drupal 7"]
fetched: "2026-10-21T07:24:16Z"
raw: "raw/docs/7/creating-custom-modules/specifying-a-custom-permission-for-a-new-page.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Specifying a custom permission for a new page

**Drupal hooks described: *hook_permission(), hook_menu()***

So far we have our working block and a settings form. The block displays a maximum number of links. However, there may be more links than the maximum we show. So we'll create a page that lists all the content that was created in the last week.

### Custom permission

First, we'll create a custom permission, using [hook_permission()](https://api.drupal.org/api/drupal/modules%21system%21system.api.php/function/hook_permission/7). The permissions this hook defines can be configured at *People \> Permissions (tab)*, or `http://example.com/admin/people/permissions`. Only user roles with this permission granted will have access to the page we will create.

Add this to your `.module` file:

``` php
/**
 * Implements hook_permission().
 */
function current_posts_permission() {
  return array(
    'access current_posts content' => array(
      'title' => t('Access content for the Current posts module'),
    )
  );
}
```

This hook follows the typical Drupal pattern of attributes defined in arrays. The main key is the machine readable name of the permission, which we will use in our [hook_menu()](https://api.drupal.org/api/drupal/modules%21system%21system.api.php/function/hook_menu/7) implementation. `'title'` provides the human-readable name of the permission, to be shown on the permission administration page. This should be wrapped in the t() function for translation.

See [hook_permission()](http://api.drupal.org/api/drupal/modules--system--system.api.php/function/hook_permission/7) for all the available options.

### Registering the URL and naming the page function

We'll need to edit `current_posts_menu()` to establish a path and name for the new page. A quick note on function naming conventions in Drupal:

- If you are implementing a Drupal hook, you must always name the function "your_module_name_hookname".
- If your function is not a Drupal hook but is otherwise public (i.e. it would be okay for another module to call it, and you don't intend to change its argument signature or behavior often), start the function name with "your_module_name\_". Make sure you have not accidentally picked a function name matching a Drupal hook
- If you are creating a strictly private function (i.e. no other module should rely on it being a stable function or call it), start the function name with an underscore: "\_your_module_name\_".

Page callbacks are good candidates for strictly private functions, so we will start with an underscore, then the module name, and finally the word, 'page'. Add the following code to your `current_posts_menu()` function as the second item in the `$items` array. Be sure the code, `return $items;` is the final line of the function.

``` php
/**
* Implements hook_menu().
*/
function current_posts_menu() {
    $items = array();    
    $items['current_posts'] = array(
        'title' => 'Current posts',
        'page callback' => '_current_posts_page',
        'access arguments' => array('access current_posts content'),
        'type' => MENU_NORMAL_ITEM, // Will appear in Navigation menu.
      );
    return $items;
}
```

This listing mirrors the previous menu item with a couple of exceptions. The first needed a description for the *Configuration* page. That's less important here, and we are not including it. Because we are creating a page function and not calling `drupal_get_form`, we have no page arguments to pass. The new permission becomes the access argument. Since we are not using the `admin/config` path, our item will appear in the Navigation menu.

### Check

Enable your module again and check the *Navigation* menu. You should see a listing for *Current posts*. If it's not there, try clearing the caches. You may also need to add the new permission to your role. (Find this link beside your module listing on the *Modules* page, or access the list of permissions at `http://example.com/admin/people/permissions`.)

![Admin People Permissions](/files/admin_people_permissions.png)  
 

Now this **current_posts** page is only accessible to users who have this permissions checked, currently in screenshot this permission is assigned to Administrator only, it means Anonymous user and Authenticated users can't access this page. If they will try to access this, will get Access Denied.

Please note, you will see only a blank page when you follow the menu link. That's as it should be, because we have not yet written the page function. You may even get an error message. Remember to disable your module before continuing.

### Clear caches

If you are not able to see your changes that you did either in hook_menu or hook_permission function, then [clear cache](https://drupal.org/node/42055) to make your changes active.

### See also

- [hook_permission()](http://api.drupal.org/api/drupal/modules--system--system.api.php/function/hook_permission/7)
- [hook_menu()](http://api.drupal.org/api/drupal/modules--system--system.api.php/function/hook_menu/7)
