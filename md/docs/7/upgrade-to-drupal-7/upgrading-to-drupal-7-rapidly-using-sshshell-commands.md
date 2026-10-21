---
title: "Upgrading to Drupal 7 rapidly using SSH/Shell commands"
source_url: "https://www.drupal.org/docs/7/upgrade-to-drupal-7/upgrading-to-drupal-7-rapidly-using-sshshell-commands"
page_type: page
last_updated: "Last updated on 11 October 2017"
published: "2008-08-20T05:42:27+00:00"
modified: "2017-10-11T17:47:33+00:00"
breadcrumb: ["Drupal 7", "Upgrade to Drupal 7"]
fetched: "2026-10-21T06:21:35Z"
raw: "raw/docs/7/upgrade-to-drupal-7/upgrading-to-drupal-7-rapidly-using-sshshell-commands.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Upgrading to Drupal 7 rapidly using SSH/Shell commands

This guide is meant to augment the [official Upgrade guide](http://drupal.org/upgrade/tutorial-introduction). Please read the official upgrade steps in UPGRADE.txt as well as in the Drupal.org Documentation thoroughly to ensure that you understand every aspect of the upgrade process. **This guide is for more-advanced users with SSH/Shell experience,** and you should only follow these steps if you are comfortable working with SSH/Shell and understand the risks (e.g. there is no undo). For simplicity, the term SSH in this guide refers to any kind of remote or local [Unix shell/command line](http://en.wikipedia.org/wiki/Unix_shell).

The goal of this guide is to provide more advanced users with a series of SSH/terminal commands, which can be used to upgrade a Drupal site in as little as one minute (to run the upgrade commands). The time for your backup, which you should do first, will vary.

You can accomplish the same steps using FTP, however using SSH saves a lot of time (SSH speeds things up considerably compared to deleting and uploading files/folders with FTP). Using SSH gets the site upgraded and back online much faster, which is of course a good thing.

*Hint:* Once you are accustomed to the process, to further increase the speed of your upgrades, copy and paste each of the listed commands onto a separate line in a text file to refer to during upgrades. You will then be able to "triple-click" on the line to select it entirely, copy/paste it into your SSH client, and run the command. Use Alt-Tab (Windows) or Cmd-Tab (Mac) to rapidly switch between your text file and SSH client to upgrade Drupal in record time. Note that some Windows editors don't support triple-click (WordPad does though). You can even automate the whole process with a shell script if you'd prefer (though for some this might be relinquishing a bit too much control).

## Prepare your site

1.  If you have a copy of your site running on a local development server such as WAMP, MAMP, etc, it is wise to test the upgrade there first - this will tell you ahead of time whether things are likely to work without causing trouble on your live site.
2.  Switch Drupal into *Off-line* mode so that visitors do not access the site while the upgrade is happening and encounter various errors. You can turn this setting on and off at *Administer \> Site configuration \> Site maintenance (admin/settings/site-maintenance)*.
3.  Ensure that you are logged into the site as the main administrator account (user ID 1). You cannot run the *update.php* file near the end of the process unless you are logged in as the administrator user. If you forget to log in first before running *update.php*, the page will inform you of the step to take to regain access.

## Backup your site

Next back up the full site, both the files as well as the database. **Never upgrade without backing up. Ever.** You can do this through your hosting control panel in most cases, though when you have SSH access it is much faster to backup using a few quick commands. A reference is available on [backing up your Drupal site](http://drupal.org/node/22281). There is also a useful [backup script](http://drupal.org/node/59369) you can use if you'd prefer, or here are the basic commands needed for a quick manual backup:

1.  First make a directory with today's date in your backups folder (create the *backups* folder first if you haven't made one yet). Ensure that this folder is *not* accessible to the web:  
    `mkdir /home/yoursitename/backups/08-17-08`
2.  Now backup the database (customize with your directory paths and info):  
    `mysqldump -u username -p drupal_database > /home/yoursitename/backups/08-17-08/yoursite_db.sql`
3.  Next backup your site's files (again, customize as needed):  
    `tar -czvpf /home/yoursitename/backups/08-17-08/yoursite.tar.gz /home/yoursitename/public_html`

## Upgrade your site to Drupal 7

Assuming you use Drupal as intended and *never hack/edit the core files* (if you did change any of Drupal's core files, your upgrade process will be somewhat or even much more difficult), and you store all of your personal data (e.g. modules, themes, and files) within the **/sites** folder (for Drupal 5 you might also have your **/files** folder in the root directory of your site - with Drupal 6, by default */files* is a sub-folder within the */sites* directory), then you can confidently erase all the rest of Drupal's files and directories besides those, and upload the latest copy of Drupal in their place:

1.  Navigate to your site's root directory (the following commands from this point are to be run while you are in the root directory of your site):  
    `cd /home/yoursitename/public_html`

2.  First make a temporary folder to hold Drupal's old files/folders until you're certain that the upgrade has completed successfully (doing this extra step instead of deleting the old files right off can be helpful in an emergency, since it makes it quick and easy to undo things back to normal if the upgrade fails for some reason, rather than bothering with extracting the whole backup):  
    `mkdir d-backup`

3.  Next paste in the following command which moves all of Drupal's files and folders, besides your personal ones (such as the */sites* and */files* folders), into the temporary *d-backup* folder. The *.htaccess* and *robots.txt* files are not included in the move since it's possible that you've customized them (however if not, feel free to add them to the list):

    **Drupal 5 or 6:**  
    `mv CHANGELOG.txt COPYRIGHT.txt cron.php includes index.php INSTALL.mysql.txt INSTALL.pgsql.txt install.php INSTALL.txt LICENSE.txt MAINTAINERS.txt misc modules profiles scripts themes update.php UPGRADE.txt xmlrpc.php d-backup`

    **Drupal 7:**  
    `mv authorize.php CHANGELOG.txt COPYRIGHT.txt cron.php includes index.php INSTALL.mysql.txt INSTALL.pgsql.txt install.php INSTALL.sqlite.txt INSTALL.txt LICENSE.txt MAINTAINERS.txt misc modules profiles scripts themes update.php UPGRADE.txt web.config xmlrpc.php d-backup`

4.  Check Drupal.org's home page to get the download link for the latest version of Drupal (or simply adjust the number in the command below). Generally you can safely upgrade from your current version of Drupal to any version within the same release (for example 6.1 to 6.4), though reading the UPGRADE.txt files for each version ahead of time is advised, just in case. However extra caution/preparation is required upgrading between major releases (for example 5.x to 6.x). Some web hosts do not support the *wget* command so the alternate *curl* command is also listed (if neither are supported, resort to FTP).

    **Using wget:**  
    `wget http://ftp.drupal.org/files/projects/drupal-6.4.tar.gz`

    **Using curl:**  
    `curl -O http://ftp.drupal.org/files/projects/drupal-6.4.tar.gz`

5.  Extract the downloaded file (it will create its own sub-folder for the files, so don't worry about it getting mixed up with your own files). This command assumes you only have one downloaded copy of Drupal in the directory - if you have others, enter the full name to exact it instead of using the wildcard character:  
    `tar -xzvpf drupal-*`

6.  Go into the newly created sub-directory:  
    `cd drupal-*`

7.  Run the following command to move the new Drupal files out of the folder they were extracted into and into place in the root directory of your site. This moves "only" the same files and folders which you moved into the *d-backup* folder, preserving all of your personal files and folders (e.g. the */sites* and */files* directories) The *../* at the end is what tells the command to move the data up one level in the folder structure, into your site's root directory:  
    **Drupal 5 or 6:**  
    `mv CHANGELOG.txt COPYRIGHT.txt cron.php includes index.php INSTALL.mysql.txt INSTALL.pgsql.txt install.php INSTALL.txt LICENSE.txt MAINTAINERS.txt misc modules profiles scripts themes update.php UPGRADE.txt xmlrpc.php ../`

    **Drupal 7:**  
    `mv authorize.php CHANGELOG.txt COPYRIGHT.txt cron.php includes index.php INSTALL.mysql.txt INSTALL.pgsql.txt install.php INSTALL.sqlite.txt INSTALL.txt LICENSE.txt MAINTAINERS.txt misc modules profiles scripts themes update.php UPGRADE.txt web.config xmlrpc.php ../`

8.  Return to your site's root directory:  
    `cd ..`

9.  If you had any extra files which you placed into Drupal core folders (for instance *jquery.js* into the */misc* folder in the case of having the jQuery Update module installed), you can quickly restore them into place using commands as well. Very few modules ask you to put files outside of the modules directory, so this may never be a step you need to do. Here are several common examples:  
    `cp sites/all/modules/jquery_update/jquery.js misc/jquery.js`  
    `cp sites/all/modules/image/image.imagemagick.inc includes/image.imagemagick.inc`

10. Lastly, go to *example.com/update.php* in your web browser and follow the instructions to update the database within a few clicks. Do *not* adjust any of the drop-down menus under the "Select versions" fieldset; simply run *update.php*. You can go to *Administer \> Logs \> Status report* (Drupal 5) or *Administer \> Reports \> Status report* (Drupal 6 and 7) to confirm your Drupal version.

## Clean up temporary files/folders and restore access to your site

1.  Now that the upgrade has completed successfully, go ahead and delete the temporary *d-backup* folder (remember you still have your "real" backup file in case you need it). Also delete the *tar.gz* copy of Drupal which you downloaded and the *drupal-\** folder it was extracted into. To do this all in one step, run this command (**only** if you do not have any files or folders the name of which begins with *drupal-* that you want to keep, as this will immediately delete them all):  
    `rm -rf d-backup drupal-*`
2.  Many Drupal site admins prefer to delete the various *.txt* files (such as UPGRADE.txt, README.txt, etc) in the root directory of their Drupal sites (often because these files easily reveal the currently-installed version of Drupal to the public). Feel free to delete every .txt file from your Drupal installation directory besides *robots.txt*. If you perform this deletion, adjust the "mv" (move) commands from steps 3 and 7 to no longer include these files during future upgrades.
3.  When done, you can re-enable Drupal for the public again at *Administer \> Site configuration \> Site maintenance (admin/settings/site-maintenance)*. You should [test the site](http://drupal.org/upgrade/testing-the-new-site) to ensure that everything works as expected.
