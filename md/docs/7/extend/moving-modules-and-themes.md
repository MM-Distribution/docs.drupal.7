---
title: "Moving modules and themes"
source_url: "https://www.drupal.org/docs/7/extend/moving-modules-and-themes"
page_type: page
last_updated: "Last updated on 3 August 2025"
published: "2007-10-15T19:19:52+00:00"
modified: "2025-08-03T12:32:07+00:00"
breadcrumb: ["Drupal 7", "Extending Drupal 7"]
fetched: "2026-10-21T06:08:09Z"
raw: "raw/docs/7/extend/moving-modules-and-themes.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Moving modules and themes

For modern Drupal, see [How to fix "The following module is missing from the file system..." \> You moved the module inside your Drupal installation](https://www.drupal.org/docs/administering-a-drupal-site/troubleshooting-drupal/how-to-fix-the-following-module-is-missing-from-the-file-system-warning-messages#s-you-moved-the-module-inside-your-drupal-installation).

The best practice is to keep all of your contributed modules and themes in the `sites/all/modules` or `sites/all/themes` directory, as appropriate. If you are upgrading from a previous version or have already installed them in the main `modules` or `themes` directories and you wish to move them, it is possible but you just need to make sure Drupal knows you moved them.

1.  Go to **Administer \> Site Building \> Modules** (or Themes) and disable the modules/themes you wish to move.
2.  Move the modules/themes to the new directory you wish them to live in.
3.  Now go back and enable the modules again. Drupal will locate them in the new directory and update the system table as needed.

Typically you'll see a PHP "Fatal error: Call to undefined function myfunction()" error when Drupal doesn't know where your module is. If this is the case you may need to force the System Table to be rebuilt.

## Forcing a System Table rebuild

The system table gets rebuilt when you visit: admin/build/modules. So if your module has moved and you've forgotten to disable it above then just visit the modules page and you should be fine.

However visiting the modules page may still leave some errors. Some contributed modules will not come back online because of paths stored in their settings and may cause various database errors. In these cases, try uninstalling the module completely. Or just leave it where it was before you moved it. It's also possible to modify the database directly to change the path if necessary.

Always remember to make a complete backup first.

## Using Drush

If you are using Drush, you do not have to go through the hassle of disabling them all. There is a [Drush](http://drupal.org/project/drush) utility that can help you, it is called [registry rebuild](http://drupal.org/project/registry_rebuild "registry rebuild"). Registry Rebuild flushes the registry, and thus rewrites the paths to the modules in the database.

If you do not have access to Drush on your server or do not use Drush, you can also run it just with PHP, as described on the project page. Drush usage is preferred, though.

### Using Drush to rebuild the registry

Move your module folders wherever you want. Then run `drush rr` and `drush cc all` and maybe `drush rr` once more, and you are done.

This affects only the System Table so some modules may store paths in other places and still will not work after moving, as described above. However, these modules should be exceptions from the rule and the Registry Rebuild process will work in most cases.

### APC or other opcode caches

If you use a PHP opcode caching tool like [APC](http://pecl.php.net/package/apc) it is possible you need to clear their caches or restart them after following the above procedures.
