---
title: "Migrating to Drupal"
source_url: "https://www.drupal.org/docs/7/migrating-to-drupal/migrating-to-drupal"
page_type: page
last_updated: "Last updated on 12 August 2016"
published: "2002-02-03T18:41:52+00:00"
modified: "2016-08-12T19:27:56+00:00"
breadcrumb: ["Drupal 7", "Migrating to Drupal 7"]
fetched: "2026-10-21T06:55:35Z"
raw: "raw/docs/7/migrating-to-drupal/migrating-to-drupal.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Migrating to Drupal

This page contains hints and scripts from members of the Drupal community for migrating to Drupal from other content management systems (CMS) weblog, and bulletin board applications. Migrating from other platforms often requires knowledge of PHP and SQL.

Migration involves mapping data fields from the original application's database into Drupal's database. For some applications this can be a simple task, with tools or scripts available to do the migration. Other applications may have complex database schemas, lack documentation, and are uncommon enough that there are no tools available.

The best way to find out if tools or scripts exist for your application is to search on Google. For example a search such as "migrate WordPress Drupal" returns dozens of useful links.

If there are no tools available for migrating from your application to Drupal, you will want to familiarize yourself with Drupal's database schema, as well as the schema of the application you are migrating.

You will need to map all your current users into Drupal's users table. If you have different roles (for example, read-only, author, editor/reviewer, admin), you will need to assign your users to properly set up and configured roles in Drupal. This can mostly be done through Drupal's admin interface, although if you have a large number of users, you may want to find a way to automate the assignment. Editing each user by hand could be time consuming.

If the content being migrated is text, it would likely map into the node and node_revisions tables, with comments in the comments table.

It is usually possible to [import databases](/node/291089) (MySQL, etc.) containing content and users from your previous CMS into Drupal.

This can be done by exporting the databases first to CSV (comma-separated values) or similar files. Tools such as phpMyAdmin for MySQL can make this task easier. You can then import these files with [import/export modules](/project/modules?filters=tid%3A64&solrsort=sis_project_release_usage%20desc) such as [Import HTML](http://drupal.org/project/import_html), [Feeds](http://drupal.org/project/feeds), [Migrate](http://drupal.org/project/migrate), [Node Import](/project/node_import), [User Import](/project/user_import), [CSV Parser](/project/parser_csv), or [Transformations](http://drupal.org/project/transformations) (see a [module comparison](http://groups.drupal.org/node/21338)).

Note that content is often imported as [Content Construction Kit (CCK)](/project/cck) custom content types. If your tables are available in your Drupal database, you can use the [Table Wizard](/project/tw) to expose them to [Views](/project/views), and then use the [Migrate](/project/migrate) module to copy the data from the old columns to the CCK content types. Also, the [Node Convert](/project/node_convert) module can convert imported node types to other node types; it supports, at least, CCK fields, book and forum nodes, and probably others like blog, etc.

In the case that your chosen import module is not yet ready for the Drupal version you wish to use, then there is the [workaround](/node/350707#comment-1170826) of installing a site running on a previous Drupal version just for the import, and then upgrading it.

On the other hand, if you prefer to migrate data into Drupal developing a custom PHP script, see for example [Migration tips](http://acquia.com/category/tags/migration-tips) for some techniques.

Support for migrating can be found on the Drupal.org forum, [Converting to Drupal](/forum/37). See also the Drupal group [Content migration, import, and export](http://groups.drupal.org/content-migration-import-and-export), for discussion of best practices in content migration. Drupal Groups also has [a comparison of modules for importing and exporting data](http://groups.drupal.org/node/21338).

The following pages describe methods people have used to migrate to Drupal in the past. As other CMS software and Drupal evolve, you can use these as a guide to help with your own.
