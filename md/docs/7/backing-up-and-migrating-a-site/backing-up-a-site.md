---
title: "Backing up a site"
source_url: "https://www.drupal.org/docs/7/backing-up-and-migrating-a-site/backing-up-a-site"
page_type: page
last_updated: "Last updated on 22 May 2025"
published: "2005-05-07T22:30:48+00:00"
modified: "2025-05-22T13:09:53+00:00"
breadcrumb: ["Drupal 7", "Backing up and migrating a Drupal 7 site"]
fetched: "2026-10-21T06:57:24Z"
raw: "raw/docs/7/backing-up-and-migrating-a-site/backing-up-a-site.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Backing up a site

#### Updated guidance:

See also [How to back up your Drupal site](https://www.drupal.org/docs/updating-drupal/how-to-back-up-your-drupal-site) for updated guidance relevant to Drupal core and Drupal CMS.

## General backup best practices

- Always back up the entire site before updating or upgrading. (It is also a good idea before migrating, copying, moving, or replacing.)
- Date your backups. Save each one into a directory or file with a title that includes the date of the backup. You do not want to be guessing which backup is the most recent one when you are trying to recover your failed site. Panic is not conducive to a good recovery process.
- Save a copy of each backup in a different location than your webserver. Remember, if the data doesn't exist in three places, it doesn't exist at all. If your webserver crashes, then all the backup files might be gone too (see earlier reference to panic).
- Inquire about your ISP or web host's backup policies. Most good web hosts have a backup plan that kicks in every 24 hours. If yours does not, it's up to you to back up your site daily, or find a host who will. It cannot be stressed enough that if a site's data does not exist in three places, it doesn't exist at all.
- In addition to your web host's backups, routinely do it yourself. Periodically run a separate backup monthly, weekly, daily or whatever fits your site's needs. Gauge the backup cycle by how much of your user's data you can afford to lose without all the users revolting and starting a riot. Even if you tell yourself, "It's no big deal", it is, and you do not want to lose content.
- Document and test your backup and restore procedure *before* you need it. The forums and IRC chat are full of people who want help recovering from some unforeseen fatal error, and if they knew how to restore their site using the backups, they'd created, they would be in business and making money rather than waiting for help from a Drupal volunteer.
- Restore your backups using the same method as you took the backup.

## Specific backup strategy

Backing up a Drupal site involves backing up both the site's database and its files.

### Backing up the database

The [Backup and Migrate](/project/backup_migrate) module allows you to download backups or save backups on a schedule, though users should stay updated on open, known issues with the Drupal 8 version. The [Backup Database](https://www.drupal.org/project/backup_db) module is an alternative for Drupal 8 but depends upon the [Composer](https://getcomposer.org/doc/00-intro.md) module which requires command line access and cannot be operated in most shared hosting environments. The Backup and Migrate module and the Backup Database module will back up your database, code and user-uploaded files. With advanced features in Backup and Migrate, you can specify how many backups should be kept and how often backups should be taken. Alternatively, the [Database Administration module](/node/8482) for Drupal 7 gives Drupal administrators direct access to their Drupal database tables.

If you prefer the command line, backing up and restoring a MySQL database using the *command line* is covered in the MySQL Reference Manual, in the section on [Backup and Recovery](http://dev.mysql.com/doc/refman/5.1/en/backup-and-recovery.html "Backup And Recovery Guidelines for MySQL 5.0"). Note that the Reference Manual cited is based on MyISAM tables. If you use InnoDB tables in your database, please pay particular attention to [MySQL Reference Manual, section 14.2.6](http://dev.mysql.com/doc/refman/5.0/en/innodb-backup.html). There is also a handbook page about doing a [Backup and restore using bash shell scripts](/node/59369).

Backups can also be performed with a *graphical utility* such as [PHPmyAdmin](http://www.phpmyadmin.net/home_page/index.php "external link to the PHPmyAdmin project"). There's also a FAQ on that site called "[How can I backup my database or table](http://www.phpmyadmin.net/documentation/#faq6_4 "external link to the PHPmyAdmin project FAQ")." You can also take a look at the [phpMyAdminToolkit.Dump](http://www.codeplex.com/phpMyAdminToolkit) program, which according to its home page, is a console application with similar functionality to mysqldump. The program uses the phpMyAdmin API behind the scenes.

If you want to backup a bigger MySQL Database on a hosted webspace with phpMyAdmin you could run into problems because there often is a time limit for php processing. There is a script called [MySQLDumper](http://www.mysqldumper.de/en/) or [Bigdump](http://www.ozerov.de/bigdump.php) that has a workaround for the limit. MySQLDumper can also generate automatic backups.

For backing up MariaDB, see [Backing Up and Restoring](https://mariadb.com/kb/en/mariadb/backing-up-and-restoring/) in the MariaDB documentation.

If you are using a database other than MySQL or MariaDB, that vendor's documentation should have backup information. For a list of even more methods, consult the Handbook pages in the [Upgrade Guide](http://drupal.org/upgrade/backing-up-the-db) as well.

### Backing up the core files

The root directory of your installation contains all the files that make Drupal do its magic. Sure, you \*could\* go get these files from Drupal.org again if you ever needed them, but having your own copies of the core files is so much faster and efficient. If you've edited anything in the core files for your specific website, having a copy of the core files becomes mandatory, since the site's changelog is part of the root directory too.

As a suggestion, everything in the root directory should be backed up monthly, but *always back up the core files before an upgrade*. It's been said before in other sections of the Handbook, but Best Practices mean that backups of the core should be a regular habit. Do this every month as suggested, and when disaster strikes, you won't be wondering whether you've made any changes recently that have been lost forever.

### Backing up the non-core files

Contributed modules and their associated third-party files should be backed up monthly as well. If you are adhering to the Best Practices outlined in the previous section above, your contributed modules will be part of the core files backup by default, since they exist in a directory of the root Drupal installation. If you do not have the bandwidth or storage resources to back up your entire root directory each month, you *must* backup the /sites/all/modules/ (version 5.x - 7.x) or the /sites/example.com/modules/ (version 4.7 and lower). Failure to do this may leave you with no clear example of which modules you had, and what versions they were. Imagine trying to restore your site right now without knowing which versions of modules to download from Drupal.org. Could you do it?

There are also files that are not part of the database, the core, or the contributed modules that are important to your site. The directory you specified in Administer \> Site Configuration \> File System holds uploaded pictures, user's icons, and other stuff that you don't want to lose. If you are running your site in 'private' file transfer mode, chances are good that this /files/ directory is not inside your root Drupal installation, and therefore won't get backed up by the procedure outlined in "Backing Up The Core Files" above.

The /sites/ directory is another one that you should take note of, since it holds lots of things relating to your site such as logos and embedded images. Custom themes are also stored here.

Make sure that you back these two directories up weekly, or any changes made by your users might get lost forever. On high traffic sites, make daily backups of these two, and save the last 8 backups for safekeeping. If something goes wrong by accident, and you can bring your site back to the same way your users left it, you will have garnered their loyalty, increased word-of-mouth traffic for your site, and become their newest idol. You might even make it into their blog. Yes, backups can do this for you.
