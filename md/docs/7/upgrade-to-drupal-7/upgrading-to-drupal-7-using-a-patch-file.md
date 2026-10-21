---
title: "Upgrading to Drupal 7 using a patch file"
source_url: "https://www.drupal.org/docs/7/upgrade-to-drupal-7/upgrading-to-drupal-7-using-a-patch-file"
page_type: page
last_updated: "Last updated on 11 October 2017"
published: "2009-01-15T12:51:07+00:00"
modified: "2017-10-11T17:48:44+00:00"
breadcrumb: ["Drupal 7", "Upgrade to Drupal 7"]
fetched: "2026-10-21T06:21:51Z"
raw: "raw/docs/7/upgrade-to-drupal-7/upgrading-to-drupal-7-using-a-patch-file.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Upgrading to Drupal 7 using a patch file

The standard procedure to upgrade to Drupal 7 is to download it from drupal.org and follow the included UPGRADE.txt.

For administrators using the UNIX shell it may be easier by using a patch file instead. To follow the procedure described below you need the `diff` and `patch` commands which are available at most LINUX distributions.

## Backup everything (as instructed in [UPGRADE.txt](http://api.drupal.org/api/drupal/UPGRADE.txt/7 "Drupal 7 text for Upgrade file"))

If applying the patch fails, you want it to be easy to restore your site. Aside from the VERY IMPORTANT database, you also need to back up the following, if you have customized them:

- .htaccess file
- robots.txt file
- settings.php file (sites/all/default or sites/all/example.com)
- custom profiles (profiles)
- custom themes (sites/all/themes)
- custom modules (sites/all/modules/custom)
- contributed modules (sites/all/modules/contrib)
- custom features (sites/all/modules/features)

## Create the patch file

Instead of creating the patch file by yourself you may download patch files for the 5.x, 6.x, and 7.x Drupal series from <http://fuerstnet.de/en/drupal-upgrade-easier>.

1.  Download the latest Drupal release from the Drupal Download page (like version 6.9, called *latest* below)
2.  Download the Drupal release matching your installation by modifying the download URL for the latest release (like version 6.4, called *current* below). Get version information about your current Drupal installation from the CHANGELOG.txt inside your Drupal root.
3.  Untar both tar files and run the shell command `diff -Naur drupal-current drupal-latest > drupal-current-to-drupal-latest.patch`
4.  Move the created patch file into the root of your current Drupal installation

To prepare the upgrade follow UPGRADING.txt up to "5. Remove all of the old files and directories from the Drupal installation directory." After that, continue using the **Patching** commands listed below.

## Patching

1.  `cd` to your current Drupal installation directory

2.  Test drive the patch by running the shell command `patch -p1 --dry-run < drupal-current-to-drupal-latest.patch`. You will see a lot of lines like *patching file includes/bootstrap.inc* telling you which files will be patched.

    WARNING: Don't proceed if you see error messages like *Reversed (or previously applied) patch detected* or *1 out of 2 hunks FAILED*. Your Drupal installation probably is modified somehow and the patch file will not apply completely. You now better switch to the standard upgrade procedure described in UPGRADE.txt.

3.  Finally apply the patch file by running `patch -p1 < drupal-current-to-drupal-latest.patch`

Proceed with UPGRADING.txt from "8. Verify the new configuration file to make sure it has the latest and correct information" (`sites/default/settings.php`) and run `update.php`.

## Faster procedure but may be dangerous

On my Drupal installations I usually only apply the patch file after doing a backup of the complete Drupal directory and it's database(s) and run update.php for every site afterwards. This never put me in trouble but your mileage may vary.
