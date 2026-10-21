---
title: "Update core (option 2)"
source_url: "https://www.drupal.org/docs/7/update/core-option-2"
page_type: page
last_updated: "Last updated on 6 August 2019"
published: "2016-04-06T10:02:09+00:00"
modified: "2019-08-06T07:21:16+00:00"
breadcrumb: ["Drupal 7", "Updating Drupal 7"]
fetched: "2026-10-21T05:57:19Z"
raw: "raw/docs/7/update/core-option-2.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Update core (option 2)

## Before you begin

If not already done, it is suggested to read this [Introduction](/docs/7/update/introduction#before-you-begin). Which summarized all your options to choose from when updating your Drupal 7.

## Update Drupal 7 core

To update from one minor 7.x version of Drupal to any later 7.x version, after following the instructions in the *First steps and definitions* section at the top of this file:

1.  Log in as a user with the permission "Administer software updates".

2.  If you are updating a live, production site, go to Administration \> Configuration \> Development \> Maintenance mode. Enable the "Put site into maintenance mode" checkbox and save the configuration.

3.  Remove all old core files and directories, except for the 'sites' directory, the original install profile in the 'profiles' directory and any custom files you added elsewhere.
    - To be more specific, in your Drupal root folder, delete all files and the following folders: includes, misc, modules, scripts, and themes. If you used a normal installation, then also delete the profiles folder, but if you used a custom profile, then in the profiles folder, delete the subfolders minimal, standard, and testing.
    - If you made modifications to files like .htaccess or robots.txt, you will need to re-apply them from your backup, after the new files are in place.
    - Sometimes an update includes changes to settings.php (this will be noted in the release announcement). If that's the case, replace your old settings.php with the new "default.settings.php", and copy the site-specific entries (especially the lines giving the database name, user, and password) from the old settings.php to the new settings.php.
    - If you had added any custom templates or other custom files outside the "sites" folder (note that this is generally not recommended), then you will need to restore them from your backup because they have been deleted.

4.  Download the latest Drupal 7.x release from <http://drupal.org/project/drupal> to a directory outside of your web root. Extract the archive and copy the files into your Drupal directory.

    - On a typical Unix/Linux command line, use the following commands to download and extract:  

      ``` php
      wget http://drupal.org/files/projects/drupal-x.y.tar.gz
      tar -zxvf drupal-x.y.tar.gz
      ```

    - This creates a new directory drupal-x.y/ containing all Drupal files and directories. Copy the files into your Drupal installation directory:  

      ``` php
      cp -R drupal-x.y/* drupal-x.y/.htaccess /path/to/your/installation
      ```

    - If you do not have command line access to your server, download the archive from <http://drupal.org> using your web browser, extract it, and then use an FTP client to upload the files to your web root.

    This will (a) install fresh copies of the files and subfolders deleted in step 3, (b) overwrite any files in the "sites" folder that are part of core, e.g., "sites/all/README.txt" and "sites/default/default.settings.php", and (c) leave alone any file in the "sites" folder whose path and name is different from any file in core. As an alternative, you could (a) copy all the files and folders except "sites" from the new core you downloaded into your Drupal root, (b) if the release notes indicate there have been changes to "settings.php", then replace your "default.settings.php" with the new version in your download, replace your current "settings.php" with a copy of the new "default.settings.php", and insert any site-specific content from current "settings.php" into the new one, and (c) repeat step (b) for all additional sites in a multi-site installation.

5.  Re-apply any modifications to files such as .htaccess or robots.txt and restore any deleted templates or other custom files you had in core folders.

6.  Run update.php by visiting <http://www.example.com/update.php> (replace [www.example.com](http://www.example.com) with your domain name). This will update the core database tables.

    If you are unable to access update.php do the following:

    - Open settings.php with a text editor.

    - Find the line that says:  

      ``` php
      $update_free_access = FALSE;
      ```

    - Change it into:  

      ``` php
      $update_free_access = TRUE;
      ```

    - Try again to run update.php.

    - Once the update is done, \$update_free_access must be reverted to FALSE.

    In a multi-site installation, run update.php again for each site.

7.  Navigate to Administration \> Configuration \> Development \> Performance and "clear all cache". So that the cache is rebuilt.

8.  Go to Administration \> Reports \> Status report. Verify that everything is working as expected.

9.  Ensure that \$update_free_access is FALSE in settings.php.

10. Go to Administration \> Configuration \> Development \> Maintenance mode. Disable the "Put site into maintenance mode" checkbox and save the configuration.
