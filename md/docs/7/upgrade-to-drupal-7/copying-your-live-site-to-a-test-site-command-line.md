---
title: "Copying your live site to a test site (command line)"
source_url: "https://www.drupal.org/docs/7/upgrade-to-drupal-7/copying-your-live-site-to-a-test-site-command-line"
page_type: page
last_updated: "Last updated on 11 January 2020"
published: "2005-11-09T19:41:01+00:00"
modified: "2020-01-11T19:35:20+00:00"
breadcrumb: ["Drupal 7", "Upgrade to Drupal 7"]
fetched: "2026-10-21T06:18:29Z"
raw: "raw/docs/7/upgrade-to-drupal-7/copying-your-live-site-to-a-test-site-command-line.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Copying your live site to a test site (command line)

Before you begin, decide where the new installation will be located. Usually you can just install Drupal to a subdirectory: <http://www.example.com/test_site/>.

Make sure you have already completed the [steps for backing up your database](/upgrade/backing-up-the-db).

Use Drush(Drupal specific command line terminal): Drush is a program that you can install on your computer and/or on your web-hosting server, which allows you to easily build and maintain all aspects of your Drupal installation, whether that be a 'Local' site on your computer, or an online site. [Drush](https://www.drupal.org/project/drush "Drush")

### Note:

In order to have clean urls in your test_site directory you have to edit the mod_rewrite settings in test_site/.htaccess, uncomment and modify:  
RewriteBase /test_site

## I. Copy your live site files to a test site directory

Copy the contents of your live site directory to a new directory called "test_site", or whatever name you would like to use:

`cp -R /path/to/drupal/ path/to/new/drupal/site`

Make sure the .htaccess file gets copied to the new directory as well.

**You can also use the sftp login/pass for the destination account to copy files with rsync**

For example, this will sync the www directory from the source account to the destination account, copying new files and replacing existing files.

`rsync -av /var/home/user1/domain.com/www/ user2@domain2.com:/var/home/user2/domain2.com/www/`

## II. Setup a blank test-site database with MySQL

a\) Create a new, blank MySQL database (login to MySQL) and give permissions for a user to access it:

`mysqladmin -u dba_user -p create test_site_database `

(Where 'dba_user' is an example MySQL user which has the CREATE and GRANT privileges. Use the appropriate user name for your system.)

b\) MySQL will prompt for the 'dba_user' database password and then create a blank test_site database. Next you must login and set the access database permissions:

`mysql -u dba_user -p `

c\) Again, you will be asked for the 'dba_user' database password. At the MySQL prompt, enter following command:

`GRANT ALL PRIVILEGES ON test_site_database.* TO nobody@localhost IDENTIFIED BY 'password'; `

where 'test_site_database' is the name of your database 'nobody@localhost' is the username of your webserver MySQL account 'password' is the password required to log in as the MySQL user.

d\) To activate the new permissions you must enter the command:

`flush privileges; `

and then enter '\q' to exit MySQL.

## III. Change settings.php (or includes/conf.php) in your test_site directory

a\) Open and edit the file located under sites/default/settings.php (or includes/conf.php) with an editor. Look for the following block of code:

``` php
$databases = array (
  'default' =>
  array (
    'default' =>
    array (
      'database' => 'yourdatabasename',
      'username' => 'databaseusername',
      'password' => 'databasepassword',
      'host' => 'localhost',
      'port' => '',
      'driver' => 'mysql',
      'prefix' => '',
    ),
  ),
);
```

*Note: There will be two blocks of code that are similar to the one above. Be sure to edit the one that **does not** have an asterisk "\*" at the beginning of each line. The asterisk means the line is commented out, so PHP is ignoring the line.*

- Replace 'yourdatabasename' with the name of your database
- Replace 'databaseusername' with your database username (sometimes this is 'root')
- Replace 'databasepassword' with your database username's password

Save your changes.

## IV. Import your database backup into the test_site database

Now that you have a new blank test_site database, you must take the backup.sql file you created in the backup step and import it into your new database. This will create a copy of the live site database on the new test site database. There are several methods for doing this.

### IV method 1: Use the contributed database insertion script

Deprecated.

### IV method 2: Use mysqldump directly

You can also copy the database directly from the old database to the new database, by issuing this command:

``` php
mysqldump --opt --user=<user> --password=<password> <original database> | mysql --user=<user> --password=<password> <new database>
```

This way you do not need to make a dump, which greatly improves speed.

### IV method 3: Using the mysql console

You can also use the MySQL console to import your database, by issuing the following commands. This assumes you already created the new MySQL database, following the instructions above.

``` php
mysql -u {user name you are using for the new database} -p
Enter password: {enter new database password}
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is xxxxx
Server version: 5.0.44
```

Type 'help;' or '\h' for help. Type '\c' to clear the buffer.

``` php
mysql> use {new database name};

mysql> source /path/to/your/backup/file/such/as/backup.sql;

mysql>\q
```

## V. Check if your test site works

Navigate to <http://www.example.com/test_site> and you should see a working copy of your live site.

### Don't forget to edit .htaccess and settings.php

In settings.php, use a text editor to change (or uncomment) the line

``` php
$db_url = 'mysql://user:pass@localhost/test_site_db';
```

and fill in your correct username and password for the test_site database that you created above.  
Also change the line

``` php
$base_url = 'http://www.example.com/test_site';
```

In .htacccess, change RewriteBase /your_live_site/ to RewriteBase /test_site/

Then you should be ready to test your new test_site.
