---
title: "Upgrading contributed modules and themes from Drupal 6 to Drupal 7"
source_url: "https://www.drupal.org/docs/7/upgrade-to-drupal-7/upgrading-contributed-modules-and-themes-from-drupal-6-to-drupal-7"
page_type: page
last_updated: "Last updated on 11 October 2017"
published: "2010-10-21T09:43:18+00:00"
modified: "2017-10-11T17:50:24+00:00"
breadcrumb: ["Drupal 7", "Upgrade to Drupal 7"]
fetched: "2026-10-21T06:22:07Z"
raw: "raw/docs/7/upgrade-to-drupal-7/upgrading-contributed-modules-and-themes-from-drupal-6-to-drupal-7.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Upgrading contributed modules and themes from Drupal 6 to Drupal 7

First perform the core upgrade to Drupal 7 as described in the UPGRADE.txt file. Then you can update and re-enable your non-core modules by following these steps:

1.  Check your notes, and the UPGRADE.txt files inside each module, to see if any special upgrade instructions apply
2.  Fully remove the old module directory inside sites/all/modules/
3.  Download, unpack and move the new module directory to sites/all/modules/
4.  Enable the module
5.  Run update.php again (you should have run it once already when upgrading core) and check for any message output.
6.  Back up your database and files again, between each module update, so that if there is a problem, you can revert to the most recent update.

If you have errors when you run the update.php script:

- Note any error messages you see.
- Restore your site to its previous state, using the file and database backups you created before you started the upgrade or update process. Do not attempt to do further updates or upgrades on a site that had update problems.
- Consult one of the support options listed on <http://drupal.org/support>.

If you have a Drupal 7 version of the theme you were using for Drupal 6, place it in sites/all/themes/ and re-enable it.

For documentation on converting module *code* from Drupal 6 to 7, see the section on [updating your modules](/update/modules).
