---
title: "How to migrate from many different forum systems"
source_url: "https://www.drupal.org/docs/7/migrating-to-drupal/how-to-migrate-from-many-different-forum-systems"
page_type: page
last_updated: "Last updated on 12 August 2016"
published: "2009-10-12T23:25:10+00:00"
modified: "2016-08-12T19:19:01+00:00"
breadcrumb: ["Drupal 7", "Migrating to Drupal 7"]
fetched: "2026-10-21T06:53:31Z"
raw: "raw/docs/7/migrating-to-drupal/how-to-migrate-from-many-different-forum-systems.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# How to migrate from many different forum systems

When there is not yet a Drupal module for direct conversion from your current forum software, migration can often be done in two steps, via popular forums with many converters available. Possible procedures are for example:

- Old forum -\> phpBB -\> Drupal
- Old forum -\> vBulletin -\> Drupal

### Migration to Drupal via phpBB

For the *Old forum -\> phpBB* step, see [phpBB 3.0.x Convertors](http://www.phpbb.com/community/viewforum.php?f=65) and [phpBB 2.0.x Convertors](http://www.phpbb.com/community/viewforum.php?f=10). If you need to install the old phpBB2 version, see [Download legacy release](http://www.phpbb.com/downloads/legacy.php) (phpBB, like Drupal, is open source).

For the *phpBB -\> Drupal* step, see Drupal's [phpBB2Drupal](http://drupal.org/project/phpbb2drupal) module, and the handbook section [Migrating from phpBB](http://drupal.org/node/57197).

### Migration to Drupal via vBulletin

For the *Old forum -\> vBulletin* step, there are modules in vBulletin's [ImpEx Import System](http://www.vbulletin.com/docs/html/impex_module_dump) to import from a large number of forum systems.

For the *vBulletin -\> Drupal* step, see the [vBulletin to Drupal](http://drupal.org/project/vbtodrupal) module, and the handbook page [Migrating from vBulletin](http://drupal.org/node/601784).

### Features and performance

For a Drupal forum with features similar to those of well-known forum systems such as phpBB and vBulletin, see the [Advanced Forum](http://drupal.org/project/advanced_forum) module.

For good [speed and performance](http://drupal.org/node/326504) similar to those of server-friendly static html files used by some forum systems, see Drupal's [Boost](http://drupal.org/project/boost) static cache for anonymous users, and other [performance modules](http://groups.drupal.org/node/21897).

### See also

The [Migrating to Drupal](http://drupal.org/handbook/migrating) handbook section includes general methods, and also sub-sections on migrating from specific software systems, such as forums and CMS.
