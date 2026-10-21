---
title: "Migrating from phpBB"
source_url: "https://www.drupal.org/docs/7/migrating-to-drupal/migrating-from-phpbb"
page_type: page
last_updated: "Last updated on 10 August 2016"
published: "2006-04-04T03:00:38+00:00"
modified: "2016-08-10T18:03:25+00:00"
breadcrumb: ["Drupal 7", "Migrating to Drupal 7"]
fetched: "2026-10-21T06:54:49Z"
raw: "raw/docs/7/migrating-to-drupal/migrating-from-phpbb.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Migrating from phpBB

For the owners of a phpBB forum, there are two solutions:

- either [migrate the data](/node/58199) of your board to a Drupal forum,

- - Prepare the phpbb3 db by removing any non prefixed (phpbb\_) tables and only retaining the phpbb3 data as long as the phpBB3 forum still works is the main thing.
  - Next export the prefixed phpbb\_ table data (output.sql) and run: `sed -e 's/phpbb_//g' output.sql > fixed.sql` effectively stripping the table prefix.
  - Wipe and import fixed.sql to the phpBB3 db and adjust your config.php file to suite. Now your phpBB data is ready to migrate.
  - Open up a console and issue: `tail -f /var/log/apache2/error.log`or whatever helps you catch the 404's when you attempt the first migration.
  - Then attempt to import the avatars. This will most likely fail.

1.  First I touched every file that didn't exist in /phpBB3/images/avatar/upload/ and set the permissions to.

2.  Then I renamed /phpBB3/.htaccess to /phpBB3/htaccess.bak

3.  Plus rename /phpBB3/images/avatar/upload/.htaccess to /phpBB3/images/avatar/upload/htaccess.bak

4.  Create a dump of the Drupal 7 db now so you can revert back easily if things don't go according to plan.

5.  Attempt \#1: run the migrate on avatars/images again, this time it copied the blank files I touched but complained about integrity constraints because there were duplicate items existing.

6.  So go into the phpbb3 db (via phpmyadmin) for example, and delete the files in question (step 5) from tables: `migrate_map_phpbbavatar`and `users`

7.  Head back to the migrate screen and roll back any changes as well as re-import the clean Drupal 7 db backed up in step 4. Then run another import of avatars.

8.  For each file that kicks up the error about duplicate entries, do a phpmyadmin search from within the original phpBB3 db and remove any reference to those files from the above mentioned tables in Step 6.

9.  After another attempt at migration I got success and was able to proceed with the rest of the import functions.

    The one thing that saved a lot of time in testing was constantly backing up the new Drupal 7 db as I made each successful step so I didn't have to redo all the work previously achieved. I had similar problems when importing the PhpbbAttachment and repeating these steps resolved it.

    Hopefully this helps others as it was a bit of a tricky process.

or [integrate the phpBB board](/node/58200) within the Drupal web site.
