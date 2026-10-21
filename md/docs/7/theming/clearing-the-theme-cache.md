---
title: "Clearing the theme cache"
source_url: "https://www.drupal.org/docs/7/theming/clearing-the-theme-cache"
page_type: page
last_updated: "Last updated on 19 January 2019"
published: "2008-11-21T02:32:26+00:00"
modified: "2019-01-19T00:09:36+00:00"
breadcrumb: ["Drupal 7", "Theming Drupal 7"]
fetched: "2026-10-21T06:03:15Z"
raw: "raw/docs/7/theming/clearing-the-theme-cache.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Clearing the theme cache

The contents of the .info file are cached in the database, so Drupal will not automatically notice alterations to the .info file. Also, if you add new tpl.php files or override new theme functions, you must clear the theme cache before your changes will be activated.

Do not confuse the cache with the [theme registry](/node/173880#theme-registry). To clear the cache, do one of the following:

- Click the "Clear all caches" button located under Performance. Note that this button clears all caches, not only the theme cache. If you have a site with a lot of pages or a lot of traffic you might prefer to clear only the theme cache with one of the other methods below.
  - **Drupal 7**: ***Administration \> Configuration \> Development \> Performance*** (`admin/config/development/performance`)
- Other methods:
  - [Admin menu](http://drupal.org/project/admin_menu) has clear cache links beneath the home icon.
  - Devel Block module of the [Devel project](http://drupal.org/project/devel) provides an "Empty cache" link.
  - The API function [drupal_theme_rebuild](http://api.drupal.org/api/function/drupal_theme_rebuild/7) (D7)
  - Some themes (Zen, Fusion, ...) provide a checkbox to rebuild the theme cache on every page, with a nice warning so you don't forget to turn this off.
  - [Drush](http://drupal.org/project/drush) has a command line command: drush cc theme-registry.
  - [The Magic module](https://drupal.org/project/magic) has a setting to 'Rebuild Theme Registry on Page Reload' that can be used with any theme.
- Visiting the theme selection page will also clear the .info file cache.
  - **Drupal 7**: *Administration \> Appearance* (`admin/appearance`)

If all of the above fails, you might also try to [clear all caches](http://drupal.org/node/42055)
