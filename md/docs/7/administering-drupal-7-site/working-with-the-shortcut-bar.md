---
title: "Working with the shortcut bar"
source_url: "https://www.drupal.org/docs/7/administering-drupal-7-site/working-with-the-shortcut-bar"
page_type: page
last_updated: "Last updated on 10 August 2016"
published: "2009-12-01T04:06:00+00:00"
modified: "2016-08-10T19:28:48+00:00"
breadcrumb: ["Drupal 7", "Administering Drupal 7 site"]
fetched: "2026-10-21T05:59:54Z"
raw: "raw/docs/7/administering-drupal-7-site/working-with-the-shortcut-bar.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Working with the shortcut bar

The Shortcut module provides a toolbar on the top of the page to which you can add links. This toolbar is site-wide, so any links added will be visible to all users who have permissions to see the Shortcut toolbar. This is useful for creating links to commonly-used pages within your site. You can organize these links in multiple sets of shortcuts.

## Uses

### Managing shortcuts

By default, two links are available in your shortcut toolbar: "Add content" and "Find content". To add and edit shortcuts click the "Edit shortcuts" link in the toolbar.

The core Seven administration theme displays a + sign next to administrative page titles that allows you to create a shortcut to that page. (With the overlay module active, the page title appears above the overlay, not under the breadcrumbs as you see here.) If the page is already part of your shortcut set, the link will be a - sign, to remove the shortcut.

![](/files/shortcut-add.jpg)

Once you've added it, you'll see the new link in your shortcut bar:

![](/files/Picture%2021.png)

To manage shortcuts, you must have the *Administer shortcuts* permission.

### Shortcut set limits

By default, you can only have 7 shortcuts displayed (others can be in the list of shortcuts, but disabled). This is governed by the Drupal variable 'shortcut_max_slots'; like any other Drupal variable. You can update it by

- Using the [drush command-line utility](http://drupal.org/project/drush): example drush vset shortcut_max_slots 10
- In the \$conf section of your settings.php file: example: \$conf\['shortcut_max_slots'\] = 10;
- With variable_set('shortcut_max_slots', 10).

Note: you may need to clear the Drupal cache after using either method to update this setting. See also [this issue on the set size limit](http://drupal.org/node/682000).

### Managing shortcut sets

You can organize shortcuts in sets. To add or edit shortcut sets, navigate to your account page (`http://www.example.com/user`) and click the "Shortcuts" tab. Only one shortcut set can be displayed at one time.

![](/files/shortcuts_managing.png)

### Displaying and hiding shortcuts

The core [Toolbar](/handbook/modules/toolbar) module displays the shortcuts near the top of the page, along with an Edit shortcuts link. The shortcuts can be quickly hidden by clicking the arrow sign in the toolbar.

![](/files/shortcuts_toolbar.png)

You can display the shortcuts somewhere else in your site by enabling the Shortcuts block on the Blocks administration page (*Administer \> Structure \> Blocks*).

### Disabling Shortcut module

You can also disable the shortcut feature completely by disabling the module on the modules administration page (*Administer \> Modules*).
