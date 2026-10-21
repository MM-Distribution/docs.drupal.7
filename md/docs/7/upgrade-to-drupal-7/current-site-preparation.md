---
title: "Current Site Preparation"
source_url: "https://www.drupal.org/docs/7/upgrade-to-drupal-7/current-site-preparation"
page_type: page
last_updated: "Last updated on 11 October 2017"
published: "2009-08-15T19:38:54+00:00"
modified: "2017-10-11T17:38:51+00:00"
breadcrumb: ["Drupal 7", "Upgrade to Drupal 7"]
fetched: "2026-10-21T06:19:32Z"
raw: "raw/docs/7/upgrade-to-drupal-7/current-site-preparation.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Current Site Preparation

It is always highly recommended to backup your site before any update or upgrade.  
A full backup consists of making copies of:

- All core Drupal files and folders
- All contributed module files and folders
- All contributed theme files and folders
- All other files and assets that have been uploaded via your Drupal site (e.g. /files folder)
- The Drupal database  
  (**Note:** Make sure to 'Clear all cache' using *Admin \> Site Configuration \> Performance \> Clear all cache* button to avoid any issues related to cache.)

For more information about backing up your Drupal site see <http://drupal.org/node/22281>

## Update Your Site to the Latest Stable Release of the Current Release

It is important for your current site to be updated to the latest stable release of the current release prior to upgrade because point releases sometime introduce minor database schema changes. These changes will be expected to be in place when you upgrade to Drupal 7.

## Update Contributed Modules as Required

As part of the [upgrade planning process](http://drupal.org/node/550130) you will have researched whether modules currently installed on your site will be available for Drupal 7.

Each module will have a slightly different upgrade path to Drupal 7. In many cases you will be required to update the modules on your site to their latest versions for the current version.

Visit the project page for each of module installed on your site for instructions on how to update to the latest version. Drupal 5 users who have the [Update Status](/project/update_status) module installed will be provided links to the project page for each installed module, helping to identify if all of the required updates are complete. This module been added to core in Drupal 6 and later and the Available Updates page is now found at admin/reports/updates. Also useful is the [Update status advanced settings](http://drupal.org/project/update_advanced) module which adds some of the functionality present in contrib that was not included in core.

## Test Your Current Site After Updating and Prior to Upgrading

Part of the reason for updating your site prior to upgrade is to ensure that you have a stable foundation on which to upgrade. Test to make sure your site is still working. If everything is working as expected it is a good idea to make another backup of the newly updated site to ensure that if something should go wrong during the actual site upgrade you have a known working restore point.

## Optional: Document Your Experience

If you will be updating and upgrading multiple sites, documenting any hiccups or problems you have during your update will save you time in subsequent updates and upgrades.
