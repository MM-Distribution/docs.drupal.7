---
title: "Upgrade process to Drupal 7"
source_url: "https://www.drupal.org/docs/7/upgrade-to-drupal-7/upgrade-process-to-drupal-7"
page_type: page
last_updated: "Last updated on 11 October 2017"
published: "2009-09-06T23:08:24+00:00"
modified: "2017-10-11T17:43:59+00:00"
breadcrumb: ["Drupal 7", "Upgrade to Drupal 7"]
fetched: "2026-10-21T06:20:03Z"
raw: "raw/docs/7/upgrade-to-drupal-7/upgrade-process-to-drupal-7.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Upgrade process to Drupal 7

## Automated Drush Upgrade

You can use the `drush sup` command to perform an automated site upgrade to Drupal 7. Consult [this page](https://dev.acquia.com/blog/use-drush-upgrade-drupal-6-drupal-7) for more information.

## Manual Upgrade Steps

**Note:** DO NOT run install.php at any time during an upgrade. It will empty your content from the database.

1.  **Backup your existing site and database**.

2.  **Update Drupal core, modules and themes to the latest releases for your existing Drupal version.**

3.  **Log in as user ID 1** (the site maintenance user).  
    This is the user name that you created during the installation process for your site.

4.  **Put your site in maintenance mode**  
    Go to the site maintenance page, select "Off-line" and save the configuration. If you have defined a custom maintenance theme in your settings.php file, comment it out before proceeding.

5.  **Change all themes to Garland**  
    Go to the Themes page, enable "Garland" and select it as the default theme. If you have been using a separate theme for administration, select "Garland" for your administration theme as well. If you are using a custom maintenance theme, comment out `'maintenance_theme' => 'your theme name'` in settings.php.

6.  **Disable non-core modules**  
    Go to the Modules page and disable all modules that are not listed under "Core - required" or "Core - optional". It is possible that some modules cannot be disabled, because others depend on them. Repeat this step until all non-core modules are disabled.

    If you know that you will not re-enable some modules for the target Drupal version and you no longer need their data, then you should uninstall them under the Uninstall tab after disabling them.

    You can also use Drush to disable all non-core modules (first save a list of all enabled modules):

    ``` php
    drush pml --no-core --type=module --status=enabled --pipe > modules.txt
    cat modules.txt | xargs drush -y dis
    cat modules.txt | xargs drush -y en
    ```

7.  **Remove default settings file**  
    On the command line or in your FTP client, remove the file `sites/default/default.settings.php`

8.  **Remove all old core files and directories**  
    Remove all old core files and directories, except for the 'sites' directory and any custom files you added elsewhere. If you made modifications to files like `.htaccess` or `robots.txt`, you will need to re-apply them from your backup, after the new files are in place.

9.  **Remove uninstalled modules**  
    If you uninstalled any modules, remove them from the `sites/all/modules` and other `sites/*/modules` directories. Leave other modules in place, even though they are incompatible with Drupal 7.x.

10. **Download Drupal 7**  
    Download the latest Drupal release of the target version to a directory outside of your web root. Extract the archive and copy the files into your Drupal directory.

    On a typical Unix/Linux command line, use the following commands to download  
    and extract:

    `wget http://drupal.org/files/projects/drupal-x.y.tar.gz`

    `tar -zxvf drupal-x.y.tar.gz`

    This creates a new directory `drupal-x.y/` containing all Drupal files and directories. Copy the files into your Drupal installation directory:

    `cp -R drupal-x.y/* drupal-x.y/.htaccess /path/to/your/installation`

    If you do not have command line access to your server, download the archive using your web browser, extract it, and then use an FTP client to upload the files to your web root.

11. **Re-apply modifications to core files**  
    Re-apply any modifications to files such as `.htaccess` or `robots.txt`.

12. **Make your `settings.php` file writeable**  
    Make your `settings.php` file writeable, so that the update process can convert it to the new format.

13. **Run the update script**  
    Run `update.php` by visiting `http://www.example.com/update.php` (replace `www.example.com` with your domain name). This will update the core database tables.

    If you are unable to access `update.php` do the following:

    - Open `settings.php` with a text editor.

    - Find the line that says:

      `$update_free_access = FALSE;`

    - Change it into:

      `$update_free_access = TRUE;`

    - Once the upgrade is done, `$update_free_access` must be reverted to `FALSE`.

    If your update script runs without errors and you can view the home page of your upgraded website but none of your links are working (page not founds when clicking on menus etc) AND you were using clean URLs, go to /?q=admin/config/search/clean-urls and turn off clean URLs.

14. **Backup your database**  
    Backup your database after the core upgrade has run.

15. **Upgrade fields**  
    If you are upgrading from Drupal 6 to 7 and were using CCK (and perhaps additional modules) to create fields for your content types, you will need to upgrade the data in those fields as a separate step.  
    If you have CCK text fields that have no maximum length value, you need to consult <https://drupal.org/node/1117028> . Long story short: give them maximum lengths \<= 255 before running Migrate Content.  
    Download the Drupal 7 [CCK](http://drupal.org/project/cck) module, and turn on Content Migration. Go to *Structure \> Migrate Fields* or `http://www.example.com/admin/structure/content_migrate` for a page to walk you through the migration process. There are now several types of fields in core, but not every type. You might need to download Drupal 7 versions of contributed modules to support other types of fields (such as the [References](http://drupal.org/project/references) module for nodereference fields and/or userreference fields). [Learn more about migrating content from CCK to Core Fields.](http://drupal.org/node/1144136)

16. **Update contrib modules and themes**  
    Replace and update your non-core modules and themes, following the procedures at <http://drupal.org/node/948216>

17. **Check the Status Report**  
    Go to the Status Report page and verify that everything is working as expected.

18. **Make sure settings.php is secure**  
    Ensure that `$update_free_access` is `FALSE` in settings.php.  
    Remove write permissions.

19. **Check Drupal Core Modules**  
    Make sure that standard modules from a typical fresh install are engaged. In a Drupal 6 to 7 upgrade, some modules that may not be engaged are: 'Dashboard', 'Contextual Links', 'Overlay', 'Field', 'File', 'Image' and 'Shortcut'.

20. **Remove your site from Maintenance Mode**  
    Go to the Maintenance Mode page and disable the "Put site into maintenance mode" checkbox and save the configuration.
