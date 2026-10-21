---
title: "Upgrading Drupal core to Drupal 7"
source_url: "https://www.drupal.org/docs/7/upgrade-to-drupal-7/upgrading-drupal-core-to-drupal-7"
page_type: page
last_updated: "Last updated on 11 October 2017"
published: "2009-08-14T03:12:55+00:00"
modified: "2017-10-11T14:54:57+00:00"
breadcrumb: ["Drupal 7", "Upgrade to Drupal 7"]
fetched: "2026-10-21T06:18:45Z"
raw: "raw/docs/7/upgrade-to-drupal-7/upgrading-drupal-core-to-drupal-7.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Upgrading Drupal core to Drupal 7

**Before you continue reading, we need to define the difference between upgrading and updating:**

For information on updating your Drupal site see: <http://www.drupal.org/node/1223018>

1.  Upgrading refers to moving from one major release to another, e.g. you are moving from Drupal 6 to Drupal 7.
2.  Updating typically refers to bringing your site up to the latest minor version of Drupal, e.g. such as updating from Drupal 7.12 to Drupal 7.14.

### Upgrading your Drupal installation to Drupal 7

The process of upgrading to Drupal 7 can vary in difficulty depending on the complexity of your current installation. This guide aims to help you plan for and complete a successful upgrade regardless of the size or complexity of your current site.

Any Drupal upgrade has four general steps: Planning, Preparing your current site for upgrade, Upgrading, and Testing.

Before you begin reading this guide, please make note of the following.

### Upgrading Between Versions

You can upgrade from Drupal 6 to Drupal 7.

To move to Drupal 8, use the new migration process. It allows you to migrate from Drupal 6 or Drupal 7 to Drupal 8. See [Upgrading from Drupal 6 or 7 to Drupal 8.](https://www.drupal.org/upgrade/migrate)

### Backing Up Your Existing Site

Regularly backing up your site is considered a best practice. A full backup of your site database, core Drupal files, non-core files (e.g. contributed modules, and file upload folders), and directory/file permissions ([if running on Linux](http://www.concrete5.org/documentation/how-tos/designers/backup-and-restore-file-permissions-in-linux/ "Backup and Restore File Permissions In Linux")) is **strongly recommended** before starting any site upgrade.

You may also wish to familiarize yourself with restoring your site from a backup prior to starting your upgrade. If something should go wrong during your upgrade and you need to restore your site from backup, it is best to be prepared so you can restore your site quickly. See [\[link\]](http://drupal.org/node/22281) for more information on how to back up and restore your site.

You should also review [Copying a live site via command line](http://drupal.org/upgrade/copying-your-live-site-via-command-line).

### Support Resources

- Drupal core issue queue (<http://drupal.org/project/issues/search/drupal>), set component="database update system" and select a version. Current 7.x active issues: [http://drupal.org/project/issues/search/drupal?&status%5B%5D=1&version%5...](http://drupal.org/project/issues/search/drupal?&status%5B%5D=1&version%5B%5D=7.x&component%5B%5D=database+update+system). See also <http://drupal.org/project/examples>
- Contributed modules offer information either on the description page or in the issue queue. Set the 'Version' filter to '7.x' to find related issues (eg. '[Views'](http://drupal.org/project/issues/views?text=&status=All&priorities=All&categories=All&version=7.x&component=All)) and particularly for modules lacking stable D7 versions, search 'Upgrade D7' to maybe find some info and pointers beyond the dead end.
- Drupal theme upgrade : <http://drupal.org/update/themes/6/7>
- Javascript and jquery : <http://drupal.org/node/171213>
