---
title: "Make a test site"
source_url: "https://www.drupal.org/docs/7/upgrade-to-drupal-7/make-a-test-site"
page_type: page
last_updated: "Last updated on 18 August 2016"
published: "2006-05-03T22:43:07+00:00"
modified: "2016-08-18T20:17:40+00:00"
breadcrumb: ["Drupal 7", "Upgrade to Drupal 7"]
fetched: "2026-10-21T06:18:14Z"
raw: "raw/docs/7/upgrade-to-drupal-7/make-a-test-site.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Make a test site

It is recommended that you copy your existing site to a test site and upgrade that one first. Even though you have made backups and can restore your site, you don't want your live site (the one people are actively visiting) to crash and burn if something bad happens during the upgrade.

Copying your Drupal installation to a test site takes a few steps:

- Make a backup of your existing Drupal files and database
- Copy the files to a test-site subfolder on your server
- Copy your old database to a test-site database
- Change some configuration settings, Example: update test-site's settings.php to point to the test-site database.

If you choose not to create a test site, skip forward to [Downloading Drupal and installing the files](/upgrade/downloading-drupal). Otherwise, choose either the GUI or command line method for Copying your live site to a test site.
