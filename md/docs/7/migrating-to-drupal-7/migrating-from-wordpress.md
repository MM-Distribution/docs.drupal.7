---
title: "Migrating from Wordpress"
source_url: "https://www.drupal.org/docs/7/migrating-to-drupal-7/migrating-from-wordpress"
page_type: page
last_updated: "Last updated on 4 November 2021"
published: "2006-01-03T17:49:27+00:00"
modified: "2021-11-04T14:16:09+00:00"
breadcrumb: ["Drupal 7", "Migrating to Drupal 7"]
fetched: "2026-10-21T06:54:33Z"
raw: "raw/docs/7/migrating-to-drupal-7/migrating-from-wordpress.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Migrating from Wordpress

Migrating to Drupal from Wordpress should be a fairly straightforward process for a solid basic transition (complex custom additions to Wordpress may need to be re-engineered into Drupal, but your content, comments taxonomies, etc. should come across just fine).

Essentially, the Wordpress import takes a feed of your existing Wordpress site and generates [nodes](http://drupal.org/node/21947) and [vocabularies](http://drupal.org/node/22272) from that data in your Drupal site.

## Suggested steps

- Setup a base Drupal site (see our beginning with Drupal articles).
- Configure it to your new site as much as you can (you could [install an existing theme](http://drupal.org/project/Themes) or modify an existing theme to your preference).
- New sites should be built on Drupal 7 or Drupal 9, and use the [WordPress Migrate](https://drupal.org/project/wordpress_migrate) module. Here is the [documentation for WordPress Migrate](/node/1593370).
- For Drupal 6, the [Wordpress Import](http://drupal.org/project/wordpress_import) module could be used. Follow the instructions in the [Wordpress Import](http://drupal.org/project/wordpress_import) module (read the project page and any text files that come with the tarball) and execute the import.

## Some things to consider

- The visual layout/structure may not be the same, you need to think about if you need custom [content types](/node/21947) or you want to migrate using the default 'page' content type.
- You may need to [theme](http://drupal.org/theme-guide/6) the created nodes from your Wordpress import that are generated from your Wordpress import.
- Wordpress uses the concept of "categories" but in Drupal they are called "vocabularies", terms form a taxonomy which belong to a vocabulary, but in the end, they are all the same thing.

**Note:**  
One additional note, if your WordPress install has multiple user accounts creating content and you create accounts with the same username in your Drupal site before the migration, that information will be retained in the migration.

Note that once you've done the migration and if you do a rollback, the Drupal accounts will still exist, so you don't have to create them again.

## Drupal 9 and later

This page is about migrating to Drupal 7. There is not yet a corresponding Drupal 9 and later page. However, there is a contributed [**Wordpress Migrate**](/project/wordpress_migrate) project available for Drupal 9. Making use of it and its documentation is a good place to start.

You may also want to read: [AgileDrop.com: Migrate WordPress to Drupal](https://www.agiledrop.com/blog/migrate-wordpress-drupal).
