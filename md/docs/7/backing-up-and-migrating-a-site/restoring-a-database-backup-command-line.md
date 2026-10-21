---
title: "Restoring a database backup (command line)"
source_url: "https://www.drupal.org/docs/7/backing-up-and-migrating-a-site/restoring-a-database-backup-command-line"
page_type: page
last_updated: "Last updated on 4 January 2018"
published: "2008-12-10T13:31:47+00:00"
modified: "2018-01-04T14:56:31+00:00"
breadcrumb: ["Drupal 7", "Backing up and migrating a Drupal 7 site"]
fetched: "2026-10-21T06:58:26Z"
raw: "raw/docs/7/backing-up-and-migrating-a-site/restoring-a-database-backup-command-line.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Restoring a database backup (command line)

Most of the site updates are happened without incident and when successful, the database dump you made can be discarded or archived. However, occasionally things don't go to plan and when this happens (more often than not) the database backup must be restored. While an investigation is done into what went wrong.

**IMPORTANT:** Before restoring a backup **made before an update**, you must make sure to **completely** empty your database. Drupal updates may rename tables or rearrange table data into new tables, and these tables typically won't be deleted when you restore a database backup. (For example, although mysqldump adds DROP/CREATE TABLE lines to the dump by default, it only does that for tables that it knows about.)

If not deleted, these "new" tables will cause errors the next time you attempt an update and if you ignore those errors because things initially appear to work, you may encounter more problems due to duplicate data, old data or just plain database corruption later on.

### Restoring from a MySQL dump

1 Backup your Drupal sites folder.

### 2 database back up:

*the mysqldump command you do from terminal, not from the mysql commandline*

`mysqldump -u USERNAME -pPASSWORD OLD_DRUPAL_DB_NAME > new_drupal.sql`

### 3 then create the new database or use the truncated same database.

`mysql -u USER -pPASSWORD`

`create database NEW_DRUPAL_DATABASE;`

### 4 Read the document in your drupal core folder

according to the INSTALL.mysql.txt inside the Drupal core folder (see your drupal core folder for INSTALL.pgsql.txt (PostgreSQL) and for sqlite INSTALL.sqlite.txt)  
then follow the next steps  
`use database NEW_DRUPAL_DATABASE;`

### 5 grant privileges

where:

*'databasename' is the name of your database  
'username' is the username of your MySQL account  
'localhost' is the web server host where Drupal is installed  
'password' is the password required for that username*

`GRANT SELECT, INSERT, UPDATE, DELETE, CREATE, DROP, INDEX, ALTER, CREATE TEMPORARY TABLES ON new_drupal_database.* TO 'username'@'localhost' IDENTIFIED BY 'password';`

`exit`

### 6 database restore

`mysql -u USERNAME -pPASSWORD DATABASE_NAME < new_database.sql`

## Some other options

### Emptying a MySQL database

The easiest way to drop all tables is of course to simply drop the entire database and create a new one. If you have CREATE DATABASE privileges at the shell then the simplest way to do this may seem to be to pass mysqldump the --add-drop-database argument when you create your database dumps (you must also use the --databases argument for that to have any effect). However, due to a risk of severe dataloss if not used properly (see the Caution section below), you should probably not do that. Instead, it's safer to do something like this:

``` php
mysql -h HOST -u USERNAME -pPASSWORD
drop database `DB_NAME`;
create database `DB_NAME` charset utf8;
quit
```

Or if you don't have CREATE DATABASE privileges at the shell (perhaps because you're on shared hosting), then you will have to manually delete all the tables before restoring your database dump. You can do that with the following (fill out the first line as appropriate):

``` php
MYSQL="mysql -h HOST -u USERNAME -pPASSWORD -D DB_NAME"
$MYSQL -BNe "show tables" | awk '{print "set foreign_key_checks=0; drop table `" $1 "`;"}' | $MYSQL
unset MYSQL
```

Or if you are sharing a database and have to use a table prefix: WRITE_ME!

### Caution regarding --add-drop-database

One reason not to use --add-drop-database with mysqldump is because you need to use the --databases option for it to have any effect, and the --databases option will insert USE DATABASE lines into the dump, essentially hardcoding the database that the dump applies to. If you are following best practice and have a stage site that you test on before making changes to your live site, then you will probably use two databases with different names (one for each site), and you probably want to be able to use your database dump with either database. Not only would using --databases when creating your dumps prevent that, if you tried to use a dump created with this option to overwrite a database specified on the command line, the database specified at the command line would be ignored and you would likely end up OVERWRITING THE WRONG DATABASE!

**Migrating MySQL database file into new database (Linux/Ubuntu)environment**

This is additional in restoring MySQL file into new MySQL database, after performing \$ mysqldump ..... command via Terminal (outside MySQL terminal)

In the MySQL terminal type this command:

``` php
$ mysql -u USER -pPASSWORD
mysql> use <your database name>;
mysql> source /path/to/your_sql_file.sql;
mysql> exit;
```
