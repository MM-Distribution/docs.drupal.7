---
title: "Back up your Drupal 7 site using the command line"
source_url: "https://www.drupal.org/docs/7/backing-up-and-migrating-a-site/back-up-your-drupal-7-site-using-the-command-line"
page_type: page
last_updated: "Last updated on 22 December 2024"
published: "2006-05-03T23:05:16+00:00"
modified: "2024-12-22T15:23:58+00:00"
breadcrumb: ["Drupal 7", "Backing up and migrating a Drupal 7 site"]
fetched: "2026-10-21T06:57:08Z"
raw: "raw/docs/7/backing-up-and-migrating-a-site/back-up-your-drupal-7-site-using-the-command-line.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Back up your Drupal 7 site using the command line

When you backup your website you create copies of both the files and the database.

## Back up files

Copy the contents of your Drupal directory to a directory outside your website, for example /tmp/drupalbackup. Below you find a number of possible ways to backup your files.

### Copy all files to a backup directory

Copy all the files (including the .htaccess file) from your Drupal directory to the backup directory:

`cp -rp /path/to/drupal_site /path/to/backup_dir`

The option `-rp` means copy recursive and preserve permissions.

### Put files in compressed archive

Alternatively, you can archive and compress all the files (including the .htaccess file) from your Drupal directory to the backup directory. From your Drupal directory execute:

`tar czf drupalbackup.tgz /path/to/drupal_site/`

If you want to check to make sure this worked use `tar xzpf drupalbackup.tgz` to extract the files into a new directory.

## Back up database

Before making a database backup, it is recommended to turn off [cron jobs](http://drupal.org/node/23714).

### MySQLdump

Mysqldump lets you create a copy of the database:

`mysqldump -u USERNAME -p'PASSWORD' DATABASENAME > /path/to/backup_dir/database-backup.sql`  
(note there should be no space between the `-p` option and the password; the single quotes around the password are needed if the password contains special characters).

### Drush

The [Drush](/project/drush) command sql-dump creates a copy of the database. From your Drupal directory execute:

`drush sql-dump > /path/to/backup_dir/database-backup.sql`

Use `drush help sql-dump` for more information.

Note: Drush 5 introduced [archive-dump](https://drushcommands.com/drush-8x/core/archive-dump/) and [archive-restore](https://drushcommands.com/drush-8x/core/archive-restore/) commands which allow you to backup your code, files, and database into a single file.

If you have installed the module [Backup & Migrate](/project/backup_migrate) you can use the drush command bam-backup. From your Drupal directory execute:

`drush bam-backup`

### Drupal sql dump script (Drupal 6 and earlier)

The Drupal sql dump script will look at your Drupal settings file, automatically connect to the database, and make a backup of it.

- If you are running a version of Drupal that is 4.6 or newer:  
  `./drupalsqldump.sh sites/default/settings.php > /path/to/backup_dir/database-backup.sql`
- If you are running a version of Drupal 4.5 or older:  
  `./drupalsqldump.sh includes/conf.php > /path/to/backup_dir/database-backup.sql`

## PostgreSQL dump

There several ways to do a database backup using PostgreSQL dump . E.g.,  
`pg_dump -U [user] -h [host] [databasename] > dump.sql`  
or  
`pg_dump -U [user] -W -h [host] [databasename] -F c > dump.pg_restore.format`

The former you can restore by running the script with *psql*, the latter by using the pg_restore utility.

For huge databases, the second method is nice because it is automatically compressed. Alternatively, pipe to gzip:

`pg_dump -U [user] -W -h [host] [databasename] | gzip -c > dump.sql.gz`

and to restore: `gunzip -c dump.sql.gz | psql [options]`

## Test backups and Restore database

Backups that can not be restored are not worth too much, so make sure to **test the backups**, at least from time to time.

1.  If you compress the backup, test the compressed archive data (e.g. `unzip -t {archive}`
2.  Verify that the database backup actually can be restored on the database server.

*Example for a corrupted database backup:* There is a bug that allows duplicate entries to be inserted into Drupal's search_index ([\#998474: Duplicate entries in search_index (MySQL error ERROR 1062)](/project/drupal/issues/998474 "Status: Closed (won't fix)")). The workaround for this bug is to truncate the tables `search_dataset`, `search_index`, `search_node_links`, and `search_total` before creating the database backup with `mysqldump`.

When **restoring a database backup**, keep in mind that it does not necessarily suffice to issue `mysql -u {user} -p {database} < {backup.sql}`. This will be the case if you're moving your site to a new server or the databases to a dedicated database host. In those situations, the database has to be created first, then privileges have to be granted (as instructed in the file `INSTALL.mysql.txt` from your Drupal installation's root folder), and finally you'll be able to restore the database backup. Similar steps might be required when using a different database server like PostgreSQL.
