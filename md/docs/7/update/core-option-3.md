---
title: "Update core (option 3)"
source_url: "https://www.drupal.org/docs/7/update/core-option-3"
page_type: page
last_updated: "Last updated on 17 August 2023"
published: "2012-03-22T13:46:36+00:00"
modified: "2023-08-17T13:22:10+00:00"
breadcrumb: ["Drupal 7", "Updating Drupal 7"]
fetched: "2026-10-21T05:57:34Z"
raw: "raw/docs/7/update/core-option-3.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Update core (option 3)

## Before you begin

If not already done, it is suggested to read this [Introduction](/docs/7/update/introduction#before-you-begin). Which summarized all your options to choose from when updating your Drupal 7.

## Update Drupal 7 core

1.  Make a backup of your Drupal instance (database). (For example: [with MySQL](http://www.thegeekstuff.com/2008/09/backup-and-restore-mysql-database-using-mysqldump/))
2.  Download the latest release of your current Drupal version.
3.  Extract the \[tar ball or zip\] [Drupal package](https://www.drupal.org/project/drupal).
4.  Set your site on maintenance mode (For ex: [How on D7](http://www.ostraining.com/blog/drupal/how-to-put-drupal-7-in-maintenance-mode/))
5.  Delete all the files & folders inside your original Drupal instance except for `sites/` and its sub-folders. This assumes that all of your custom work - including themes - is in the recommended spot: the `sites/` folder tree. If you have made custom changes elsewhere you will need to either preserve them or plan to replace them later. *Warning:* If your Drupal installation is built from a distribution your site will break if you delete the `profiles/` folder. Don't delete the profile folder that corresponds to the distribution you installed, for example `profiles/kickstart/` if you installed Drupal Commerce Kickstart*.*
6.  Copy all the folders and files *except* `sites/` from inside the extracted Drupal package \[tar ball or zip package\] into your original Drupal instance location.
7.  Some updates do not include changes to `setting.php` and some do. If the update release includes changes to `settings.php` you will need to replace your old `settings.php` in `sites/default/` with the new one, and then edit the site-specific entries (e.g. database name, user, and password) in the setting file.
8.  If you have modified files such as `.htaccess` or `robots.txt` re-apply those changes to the new files.
9.  If you have a `favicon.ico` file that was deleted replace it too
10. Login to your site as administrator or as user no 1
11. Run update.php by navigating to *<http://yourdrupalsitename/update.php>* and follow the process to update your Drupal instance
12. Disable maintenance mode

## Troubleshooting

- If you experience problems during your site upgrade, see the [Troubleshooting FAQ](/Troubleshooting-FAQ "visit Drupal Troubleshooting FAQ page").
- Instead of commenting here, please read the module project page and, if necessary, [post an issue](/node/add/project-issue "visit the post an issue page") or post a message in the [forums](/forum "visit Drupal Community & Support page").
