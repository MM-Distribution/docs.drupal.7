---
title: "Update core using Drush"
source_url: "https://www.drupal.org/docs/7/update/updating-drupal-using-drush"
page_type: page
last_updated: "Last updated on 16 February 2022"
published: "2015-08-13T13:28:38+00:00"
modified: "2022-02-16T18:08:06+00:00"
breadcrumb: ["Drupal 7", "Updating Drupal 7"]
fetched: "2026-10-21T05:57:50Z"
raw: "raw/docs/7/update/updating-drupal-using-drush.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Update core using Drush

## Before you begin

If not already done, it is suggested to read this [Introduction](/docs/7/update/introduction#before-you-begin). Which summarized all your options to choose from when updating your Drupal 7.

## Update Drupal 7 core using Drush

Steps to update Drupal 7 core using [Drush](http://docs.drush.org/en/7.x/) version 8 or earlier. Drush is the Drupal Shell.

### 1. Backup everything

Drush backs up the Drupal 7 core installation for you when updating, but you might want to back-up the sites directory just in case something goes wrong. You also want to take a backup of the database. Use the command below to back up everything:

``` php
drush archive-dump
```

### 2. Put your site in maintenance mode

``` php
drush variable-set --exact maintenance_mode 1
drush cache-clear all
```

### 3. Update Drupal with drush

``` php
drush pm-update drupal
```

Drush will also update your database if necessary.

### 4. Check that everything works

Go around your site and test everything! If you had modified robots.txt or .htaccess, make sure the modifications are reapplied. (Sometimes you can just copy the old files back.) If you used a custom installation profile, you might have to copy that back too. If the configuration file has changed, make sure your file has the latest and correct information - compare `sites/default/settings.php` and `sites/default/default.settings.php`.

### 5. Put your site online again

``` php
drush variable-set --exact maintenance_mode 0
drush cache-clear all
```

## Alternative Drush commands

Alternatively, you might be interested in those other Drush commands:

- `drush pm-update` is the same as running `drush pm-updatecode` and then `drush updatedb`, so you can optionally run the latter two commands to break up the process.
- `drush pm-updatecode` has a number of options you can use with `drush pm-update`, including `--security-only`. Learn more [here](http://drushcommands.com/drush-7x/pm/pm-updatecode/). You can run update commands with `-n` to prevent it from automatically answering 'y' to every 'y/n' request for user input.

## Troubleshooting

- *No code updates available* for "drush pm-update drupal"  
  Run following code which will refresh the available releases*.*  
   

  ``` php
  drush pm-refresh
  ```

  and rerun

  ``` php
  drush pm-update drupal
  ```
