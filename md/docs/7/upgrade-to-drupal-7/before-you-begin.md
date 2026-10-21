---
title: "Before you begin"
source_url: "https://www.drupal.org/docs/7/upgrade-to-drupal-7/before-you-begin"
page_type: page
last_updated: "Last updated on 11 October 2017"
published: "2010-04-13T19:17:07+00:00"
modified: "2017-10-11T14:47:58+00:00"
breadcrumb: ["Drupal 7", "Upgrade to Drupal 7"]
fetched: "2026-10-21T06:17:58Z"
raw: "raw/docs/7/upgrade-to-drupal-7/before-you-begin.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Before you begin

This section addresses steps you should take before beginning the upgrade process to Drupal 7.

## Make backups

**Back up the existing files and database for your site before you begin the rest of the upgrade process to Drupal 7.**

Even if you have determined that you may not need to upgrade the database, it doesn't hurt to make a backup. If the upgrade process fails, you may not be able to resurrect your site without the use of backups.

Choose either the GUI or command-line method for backing up your site.

For more information, see [Backing up your Drupal site](http://drupal.org/node/22281).

## Choose the right method

Before you begin the actual upgrade to Drupal 7, determine which interface methods are available for you to use to update your site. The server you use to host your site may limit you to one of the following options:

- **Command line**. Via SSH terminal access, you can connect to the server, enter commands directly, and complete all the steps in the upgrade. [Drush](/project/drush) also has a site-upgrade command which can do some of the tasks. To do so you must install the [Drush Site Upgrade Module](https://drupal.org/project/drush_sup).
- **GUI**. You can use phpMyAdmin, a browser-based MySql interface, to do anything you need on your database. And you can use any FTP client, such as [FileZilla](http://filezilla-project.org/), to transfer the files to your Drupal site from your desktop to the server.

Once you have determined whether you will use the GUI or command-line version (or a bit of both), you're ready to prepare to upgrade by following the instructions given in this section.
