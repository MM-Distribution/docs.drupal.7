---
title: "Update core (option 1)"
source_url: "https://www.drupal.org/docs/7/update/core-option-1"
page_type: page
last_updated: "Last updated on 24 March 2021"
published: "2011-07-19T07:37:37+00:00"
modified: "2021-03-24T18:44:25+00:00"
breadcrumb: ["Drupal 7", "Updating Drupal 7"]
fetched: "2026-10-21T05:57:03Z"
raw: "raw/docs/7/update/core-option-1.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Update core (option 1)

## Before you begin

If not already done, it is suggested to read this [Introduction](/docs/7/update/introduction#before-you-begin). Which summarized all your options to choose from when updating your Drupal 7.

## First steps and definitions

- If you are upgrading to Drupal version x.y.z, then x is known as the major version number, y is known as the minor version number, and z is known as the patch version number. The download file will be named `drupal-x.y.z.tar.gz` (or `drupal-x.y.z.zip`). Drupal 7 uses only x.y (MAJOR.MINOR) to designate versions.
- All directories mentioned in these documents are relative to the directory of your Drupal installation.
- Make a full backup of all files, directories, and your database(s) before starting, and save it outside your Drupal installation directory. Instructions may be found at <http://drupal.org/upgrade/backing-up-the-db>
- It is wise to try an update or upgrade on a test copy of your site before applying it to your live site. Even minor updates can cause your site's behavior to change.
- Each new release of Drupal has release notes, which explain the changes made since the previous version and any special instructions needed to update or upgrade to the new version. You can find a link to the release notes for the version you are upgrading or updating to on the Drupal project page (<https://www.drupal.org/project/drupal>).

## Update problems

If you encounter errors during this process:

- Note any error messages you see.
- Restore your site to its previous state, using the file and database backups you created before you started the update process. Do not attempt to do further updates on a site that had update problems.
- Consult one of the support options listed on <http://drupal.org/support>

## Update process

The standard process of updating is as follows:

1.  Take backups of all files and database

2.  Put site in Maintenance Mode (under Configuration / Development)

3.  Find your web root folder if it is called `www` rename it to `www_old`.

4.  Download the latest version of [Drupal 7 core](https://www.drupal.org/project/drupal). Unzip the files and delete the sites folder locally.

5.  Upload all the files to the server into a new directory `www`. (Make sure this `www` folder has the same permissions as the previous folder `www_old`)

6.  Move the `sites` folder from `www_old/sites` to `www/sites`. (This assumes any contributed modules, custom themes etc. that you use are in the `sites` directory)

7.  If changes have been made to `robots.txt` or `.htaccess` in the new version ensure these are incorporated into your version. The release notes should tell you whether this is required. Otherwise copy your previous versions from `www_old` to `www`.

8.  Run Update.php by visiting yourdomain.com/update.php

9.  While Update.php runs if you got any errors like below use the [Module missing message fixer](https://www.drupal.org/project/module_missing_message_fixer) to overcome these errors.(For 7.5x versions only)  

    ``` php
    The following module is missing from the file system: MODULE NAME. In order to fix this, put the module back in its original location. For more information, see the documentation page.
    ```

    OR

    ``` php
    User warning: The following module is missing from the file system: MODULE NAME. In order to fix this, put the module back in its original location. For more information, see the the documentation page. in _drupal_trigger_error_with_delayed_logging()
    ```

10. Switch off maintenance mode by reversing step 2

11. Take some time to test the site is functioning as expected.

12. Remove the `www_old` folder if all is working correctly.

More in-depth information on updating and upgrading can be found at <http://drupal.org/upgrade>
