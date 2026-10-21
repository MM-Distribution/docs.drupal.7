---
title: "Backing up your site (GUI)"
source_url: "https://www.drupal.org/docs/7/backing-up-and-migrating-a-site/backing-up-your-site-gui"
page_type: page
last_updated: "Last updated on 23 May 2018"
published: "2006-05-03T23:07:19+00:00"
modified: "2018-05-23T13:28:52+00:00"
breadcrumb: ["Drupal 7", "Backing up and migrating a Drupal 7 site"]
fetched: "2026-10-21T06:57:39Z"
raw: "raw/docs/7/backing-up-and-migrating-a-site/backing-up-your-site-gui.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Backing up your site (GUI)

**Backup your Drupal files**  
Using your FTP client, download all your existing Drupal files to your hard drive and put the files in a folder called 'backup'.

**Backup your database with phpMyAdmin**

- Log in to PHPMyAdmin.
- Select your database from the dropdown box on the left.  
  If you are upgrading a test site, choose your test site database. (to find the database name goto drupal_folder/sites/default/settings.php, search for database.)
- Click the "Export" tab
- Click "select all"
- Make sure to check the "structure" and "data" checkboxes
- Check "Save as File" desktop
- Click the "Go" button and save the .sql file to your desktop. Let's put it in the same 'backup' folder where you backed up your Drupal files.

This page is much a much more verbose/detailed how-to:

- <http://drupal.org/node/120627>

And it links to this visual phpMyAdmin how-to:

- <http://codex.wordpress.org/Backing_Up_Your_Database>

Another useful page:

- <https://www.siteground.com/tutorials/phpmyadmin/administration/>
