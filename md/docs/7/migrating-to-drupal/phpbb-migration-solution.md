---
title: "phpBB migration solution"
source_url: "https://www.drupal.org/docs/7/migrating-to-drupal/phpbb-migration-solution"
page_type: page
last_updated: "Last updated on 10 August 2016"
published: "2006-04-11T05:55:35+00:00"
modified: "2016-08-10T18:03:25+00:00"
breadcrumb: ["Drupal 7", "Migrating to Drupal 7"]
fetched: "2026-10-21T06:56:06Z"
raw: "raw/docs/7/migrating-to-drupal/phpbb-migration-solution.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# phpBB migration solution

## Data Migration

### Drupal 6.x and 5.x

The module to move your phpBB data to a Drupal forum can be [downloaded from the project home page](http://drupal.org/project/phpbb2drupal).

The Drupal 6 module also allows to migrate data from phpBB3, while the Drupal 5 versions are restricted to phpBB2 only.

### Drupal 7

The Drupal 7 version of the module is phpBB3 only. It also supports private messages.

*Instructions below are for the D7 version*

### Pre migration

Make sure that users can post in forums send private messages (if used) and have access to the text format you choose, otherwise the migrate will fail.

**BACKUP YOUR DATA**

You will need to add a migration source, you can do this from the content admin menu, look for phpbb and then add.

The sections of this form are as follows:

#### Name

This is the name of the migration and should be used to identify the phpbb install. If you are only going to be migrating one phpbb instance a name like 'phpbb' will do. Note: If you use too long names, it can cause errors when you navigate to the "Migrate" page.

#### Format for text fields

This is the text format to use. Often [bbcode](http://drupal.org/project/bbcode) format is advised. Your users should have access to this text format.

#### Files location

The migration will try to copy files (Avatars and Attachments) locally and reference them. This setting tells it where to find the files. If the phpbb server is still accessible you can enter the full URL here. If the files are local on the same server as the Drupal box you can enter the root directory.

#### Database Location

This tells the system where the database is and how to connect. If the phpbb tables are in the same DB as the Drupal tables you can just specify a prefix otherwise you need to enter all connection details.

#### Redirection of old paths

If you have the phpbb_redirect module enabled you will see this option. It provides a way for your old URLs to be forwarded to the Drupal nodes. Check the checkbox if you want this to happen. You should also enter a path if the old site wasn't at the root directory. For example if your old site was <http://mysite.com/forum> you would enter forum in this box.

### Migration Process

Navigate to the migrate page and run the migration. In the ideal case this will be as simple as clicking the top checkbox and pressing 'migrate'.

You can then check your data.

## Post migration setup

To make the most of your new Drupal forum, you may want to check out the following:

- [Drupal modules equivalent to phpBB features](http://drupal.org/node/58969)

## Questions? Problems? Comments?

Please use the [phpbb2drupal issue tracker](http://drupal.org/node/add/project_issue/phpbb2drupal) for any of the following:

- You find a bug or experience a problem when using the phpbb2drupal module.
- You are unclear on how to use it and would like assistance (submit a support request issue).
- You find that this documentation is not complete (don't submit the issue to the Drupal Documentation Team but to the phpbb2drupal project).
