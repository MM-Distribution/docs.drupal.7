---
title: "Menu path changes from 6.x to 7.x"
source_url: "https://www.drupal.org/docs/7/converting-drupal-6-modules-to-drupal-7/menu-path-changes-from-6x-to-7x"
page_type: page
last_updated: "Last updated on 15 October 2016"
published: "2010-02-19T18:12:08+00:00"
modified: "2016-10-15T22:13:12+00:00"
breadcrumb: ["Drupal 7", "Converting Drupal 6 modules to Drupal 7"]
fetched: "2026-10-21T07:51:12Z"
raw: "raw/docs/7/converting-drupal-6-modules-to-drupal-7/menu-path-changes-from-6x-to-7x.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Menu path changes from 6.x to 7.x

This page is a list of changes to the menu path from D6 to D7.

See [Information Architecture Drupal 7](/node/549094) for more information.

### Many paths to admin screens have changed

Paths to many administrative screens have changed between Drupal 6 and Drupal 7, as part of the information architecture and usability improvement effort. Here is a list **(possibly incomplete)**:

- Most items in admin/settings/\* moved to admin/config/\* (see exceptions below)
- Some items in admin/build/\* moved to admin/structure/\* (see exceptions below)
- Media-related items are now in admin/config/media [(issue)](http://drupal.org/node/550228)
- admin/build/modules -\> admin/modules
- admin/build/themes -\> admin/appearance
- admin/build/path -\> admin/config/search/path
- admin/build/block -\> admin/structure/block
- admin/build/menu -\> admin/structure/menu
- admin/content/types -\> admin/structure/types
- admin/content/taxonomy -\> admin/structure/taxonomy
- admin/content/forum -\> admin/structure/forum
- admin/build/testing -\> admin/config/development/testing
- admin/settings/site-maintenance -\> admin/config/development/maintenance
- admin/settings/performance -\> admin/config/development/performance
- [(Issue)](http://drupal.org/node/564576) admin/settings/contact removed
- admin/settings/filters -\> admin/config/content/formats
- admin/user/user -\> admin/people
- admin/user/permissions -\> admin/people/permissions
- admin/user/roles -\> admin/people/permissions/roles

### Changed log out path from 'logout' to 'user/logout' for consistency

[(issue)](http://drupal.org/node/337820) The menu path to log out the current user is now 'user/logout' and fits in line with all the other user-related paths like user/login, user/register, etc.

Drupal 6.x:

``` php
drupal_goto('logout');
l(t('Log out'), 'logout');
```

Drupal 7.x:

``` php
drupal_goto('user/logout');
l(t('Log out'), 'user/logout');
```

### Changed Clean URLs and Search settings page path

[(issue)](http://drupal.org/node/557890) Clean URLs and Search settings pages have been grouped in a "Search and metadata" category.

Path for search settings page has been changed from **"admin/settings/search"** to **"admin/config/search/settings"**  
Path for clean URLs settings page has been changed from **"admin/settings/clean-urls"** to **"/admin/config/search/clean-urls/"**

Example - Drupal 6:

``` php
<?php
function customsearch_menu() {
  $items = array();

  $items['admin/settings/customsearch'] = array(
    'title' => t('Custom search settings'),
    'description' => t('Administer custom search.'),
    'page callback' => 'drupal_get_form',
    'page arguments' => array('customsearch_settings'),
    'access callback' => 'user_access',
    'access arguments' => array('administer site configuration'),
    'type' => MENU_NORMAL_ITEM,
  );
  return $items;
}
?>
```

Drupal 7:

``` php
<?php
function customsearch_menu() {
  $items = array();

  $items['admin/config/search/customsearch'] = array(
    'title' => t('Custom search settings'),
    'description' => t('Administer custom search.'),
    'page callback' => 'drupal_get_form',
    'page arguments' => array('customsearch_settings'),
    'access callback' => 'user_access',
    'access arguments' => array('administer site configuration'),
    'type' => MENU_NORMAL_ITEM,
  );
  return $items;
}
?>
```
