---
title: "Backup your database and files"
source_url: "https://www.drupal.org/docs/7/site-building-best-practices/backup-your-database-and-files"
page_type: page
last_updated: "Last updated on 4 November 2019"
published: "2010-06-28T16:38:14+00:00"
modified: "2019-11-04T13:50:35+00:00"
breadcrumb: ["Drupal 7", "Drupal 7 site building best practices"]
fetched: "2026-10-21T07:10:18Z"
raw: "raw/docs/7/site-building-best-practices/backup-your-database-and-files.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Backup your database and files

Creating and storing website backups is not just an element of website best practices, it is the most important step to ensure website stability and a requirement for all forms of development!

**Basic advantages of a backup strategy**

1.  If for any reason your website goes awry restoring it from a recent backup is sometimes the only option available.
2.  New development environments can be created and refreshed very easily.
3.  Upgrades and patches can be tested singly or in groups with high confidence when using a recent backup of your production site.

To create a complete copy of the website both the database and the custom files will need to be backed up. An automatic backup strategy is easy to implement using the Backup & Migrate module, and a manual backup can be created before major updates or new implementations, providing a convenient restore point taken immediately prior to the changes going in.

### Backup & Migrate

The [Backup & Migrate](http://drupal.org/project/backup_migrate) module facilitates emergency recovery and site migration. You can configure it for automatic backups saved to the filesystem - with more frequent backups during development.

You can also create a manual backup before undertaking any complex configuration changes or major updates. That way, you have a "restore point" in case of disaster.

While there may be some issues of security when you save the database and content as a file (you could exclude certain tables, perhaps), the benefits of having a rollback in case of a disaster are significant.

The module also facilitates the migration of the site. I just moved a complex site with Views, APK, CiviCRM, etc., about 12,000 files. I moved the files, created a new database, edited settings.php and civicrm.settings.php for the new database, exported the database from the existing site and imported it in the new site's database with phpMyAdmin and VOILA - site moved! (sometimes I copy the files, make a default installation, enable the Backup & Migrate module, and import the database in the module interface - that works too).

### Drush

[Drush](/project/drush) (Drupal Shell) is a command-line utility written in PHP. To use Drush you need to have shell (SSH) terminal access to your server and be able to [install and configure the Drush utility code.](http://docs.drush.org/en/master/install/)

Drush also integrates with the Backup & Migrate module.

#### Drush archive-dump

Drush archive-dump creates an archive of your files and database with the [archive-dump command.](http://drushcommands.com/drush-8x/core/archive-dump/)

#### Drush sql-dump

Drush [sql-dump](http://drushcommands.com/drush-8x/sql/sql-dump/) uses mysqldump to back up your database. It is particularly effective when combined with [Drush aliases](https://raw.githubusercontent.com/drush-ops/drush/8.x/examples/example.aliases.drushrc.php) so you do not have to be in your site directory, and you can backup a remote server DB if you have SSH access on it.  
*Example sql-dump command (without alias) adding timestamp to filename:*  
`` drush sql-dump --result-file=PATH/TO/BACKUP/DIR/DBNAME_`date +"%m_%d_%Y-%H:%M"`.sql ``

### Command line interface

If your web host gives you access to the command-line: You can perform a database dump with the `mysqldump` command.

### Using a Git hook

See [A development automation example using Git hooks \| Develop guide on Drupal.org](https://www.drupal.org/docs/develop/local-server-setup/linux-development-environments/set-up-a-local-development-drupal-0/a). The method there uses the commit hash inside the dump file name to know which state of the codebase it goes with.
