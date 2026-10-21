---
title: "Migrating from Discus"
source_url: "https://www.drupal.org/docs/7/migrating-to-drupal/migrating-from-discus"
page_type: page
last_updated: "Last updated on 12 August 2016"
published: "2009-10-09T09:34:13+00:00"
modified: "2016-08-12T19:15:13+00:00"
breadcrumb: ["Drupal 7", "Migrating to Drupal 7"]
fetched: "2026-10-21T06:53:46Z"
raw: "raw/docs/7/migrating-to-drupal/migrating-from-discus.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Migrating from Discus

Discus is a message board software by [DiscusWare](http://www.discusware.com/). Migration from Discus boards to Drupal forums can be done in two or three steps. Some possible procedures are for example:

- Discus -\> phpBB 2 -\> Drupal
- Discus -\> phpBB 2 -\> phpBB 3 -\> Drupal
- Discus -\> vBulletin -\> Drupal

### Migration to Drupal via phpBB 2 or 3

For the *Discus -\> phpBB 2* step, see markus_freerela's converter on the phpBB discussion [Discus 4 --\> phpBB2 convertor](http://www.phpbb.com/community/viewtopic.php?t=152429), which also includes other converters. Markus' script has several versions that you can try, in order to find the most suitable for your board. Download links are: [2.0](http://www.discusscripts.com/downloads/discus_migr_20.zip), [2.0.1](http://www.discusscripts.com/downloads/discus_migr_201.zip), [2.0.2](http://www.discusscripts.com/downloads/discus_migr_202.zip), [2.1.0](http://www.discusscripts.com/downloads/discus_migr_210.zip), [2.1.1](http://www.discusscripts.com/downloads/discus_migr_211.zip), [2.2.0](http://www.discusscripts.com/downloads/discus_migr_220.zip), [2.2.1](http://www.discusscripts.com/downloads/discus_migr_221.zip), [2.2.3](http://www.discusscripts.com/downloads/discus_migr_223.zip), [2.2.4](http://www.discusscripts.com/downloads/discus_migr.zip). To install the needed old phpBB2 version, see [Download legacy release](http://www.phpbb.com/downloads/legacy.php) (phpBB, like Drupal, is open source).

For the *phpBB 2 or 3 -\> Drupal* steps, see Drupal's [phpBB2Drupal](http://drupal.org/project/phpbb2drupal) module, and the handbook section [Migrating from phpBB](http://drupal.org/node/57197).

### Migration to Drupal via vBulletin

For the *Discus -\> vBulletin* step, there are two modules for DiscusWare in vBulletin's [ImpEx Import System](http://www.vbulletin.com/docs/html/impex_module_dump): the older *discus_file*, and the more recent and probably more complete *DiscusWare4Pro_tabfile*. If Discus was using the optional database, you should export its data (users, etc.) to files with Discus Administration (Database Manager) before the conversion. Also, to export the posts to a tabfile (tab-delimited messages), see the Backup Manager. Two related threads are: [1](http://www.vbulletin.com/forum/showthread.php?t=191441), [2](http://www.vbulletin.com/forum/showthread.php?t=221662). If the Discus auto-archiving of messages was enabled, see this [post](http://www.vbulletin.com/forum/showthread.php?p=1363294#post1363294) for a workaround.

For the *vBulletin -\> Drupal* step, see the [vBulletin to Drupal](http://drupal.org/project/vbtodrupal) module, and the handbook page [Migrating from vBulletin](http://drupal.org/node/601784).

### Features and performance

For a Drupal forum with features similar to those of well-known forum systems such as phpBB and vBulletin, see the [Advanced Forum](http://drupal.org/project/advanced_forum) module.

For good [speed and performance](http://drupal.org/node/326504) similar to those of Discus' static html files, see Drupal's [Boost](http://drupal.org/project/boost) static cache for anonymous users, and other [performance modules](http://groups.drupal.org/node/21897).
