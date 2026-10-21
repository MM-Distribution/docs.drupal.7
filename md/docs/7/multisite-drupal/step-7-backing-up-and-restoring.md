---
title: "Step 7: backing up and restoring"
source_url: "https://www.drupal.org/docs/7/multisite-drupal/step-7-backing-up-and-restoring"
page_type: page
last_updated: "Last updated on 30 August 2016"
published: "2014-03-24T11:19:53+00:00"
modified: "2016-08-30T13:47:16+00:00"
breadcrumb: ["Drupal 7", "Multisite Drupal 7"]
fetched: "2026-10-21T06:15:39Z"
raw: "raw/docs/7/multisite-drupal/step-7-backing-up-and-restoring.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Step 7: backing up and restoring

**Don't forget to include your web sites folders and database schemata in your regular backup scheme.** They are located in /var/www/drupal7/sites/ and /var/lib/mysql/ , respectively.

## Mageia 3 and 4's general backup scheme

- Go to Mageia control center → System → Snapshot.
- Check the box "Enable backups".
- Click on "Advanced".
- Add /var/www/drupal7/sites/ if you want to save this directory and it's not already included in the directories to save. You may prefer to save your all Drupal installation: in this case enter /var/www/drupal7/ instead, but this needs more space. Click on "OK".
- Add the same way /var/lib/mysql/ .
- Click on "Close".

## Database backup

The disadvantages of /var/lib/mysql/ is that it contains human unreadable files, and, if you later want to migrate your website to a 3<sup>rd</sup> party's shared hosting service server, they probably won't allow you to write directly in their /var/lib/mysql/ directory. In order to save your databases in a human readable and "migratable" form:

- In your browser, go to <http://localhost/phpmyadmin>
- Log in. The username (probably "root") and password are MySQL's ones.
- On the left, click on your database name.
- On the horizontal menu, click on "Export".
- If you are in a hurry, just click on "Go". This will create a .sql file you can read, modify if you know SQL and Drupal, and copy to your hosting service provider's server. This file is a list of directives to MySQL.
- If you have a few minutes, before clicking on "Go", click on "Custom - display all possible options". All the tables are selected: this is fine. In the field "File name template", I suggest you enter "%F_localhost\_@DATABASE@". "%F" will insert the date in the file name, while "@DATABASE@" will insert the database name. In "Compression", you can choose a compression, like "gzipped".

## Database restoration

- In your browser, go to <http://localhost/phpmyadmin>
- Log in. The username (probably "root") and password are MySQL's ones.
- In the horizontal menu, click on "Import".
- Then click on the "Browse..." button, choose your .sql file and click on the "Open" button.
- Then click on the "Go" button and wait a bit.
