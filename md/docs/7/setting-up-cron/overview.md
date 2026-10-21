---
title: "Overview"
source_url: "https://www.drupal.org/docs/7/setting-up-cron/overview"
page_type: page
last_updated: "Last updated on 12 September 2016"
published: "2008-04-25T05:49:12+00:00"
modified: "2016-09-12T08:38:36+00:00"
breadcrumb: ["Drupal 7", "Setting up cron for Drupal 7"]
fetched: "2026-10-21T06:23:08Z"
raw: "raw/docs/7/setting-up-cron/overview.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Overview

Setting up cron is an important step in the installation of the website and assists in the maintenance of the site's assets for search results, checking for updates to Drupal core and modules, and removing temporary files.

A properly configured cron job can manage a variety of tasks:

- The Search module that indexes the website's content.
- The Aggregator module's that retrieves feeds.
- The Ping module that notifies other sites of updates.
- The System module that performs routine maintenance tasks, such as pruning of logs.

## What is cron?

Cron is a daemon that executes commands at specified intervals. These commands are called "cron jobs". Cron is available on Unix, Linux and Mac servers. Windows servers use a [Scheduled Task](http://drupal.org/node/31506) to execute commands. The actual "cron job" is a time-triggered action that is usually (and most efficiently) performed by your website's hosting server, but can also be configured by a remote service or even from your own desktop.

What actually happens is that the cron job visits the cron.php file in your website at a URL like `http://www.example.com/cron.php?cron_key=0MgWtfB33FYbbQ5UAC3L0LL3RC0PT3RNUBZILLA0Nf1Re`. You can find the exact address of the cron.php file in the Status report at Administration \> Reports \> Status report (admin/reports/status) in the section Cron maintenance tasks.

## Enabling cron

From Drupal 7 onwards there are two separate ways to run Drupal's cron tasks. The easiest way is to let Drupal do it for you (which it does by default) using its built-in "automated cron" system (which is similar to the "Poor man's cron" contrib module for Drupal 6).

The automated cron system is compatible with all systems because it doesn't actually involve the system's cron daemon. It works by checking at the end of each Drupal request to see when cron last ran and, if it has been too long, processing the cron tasks as part of that request. The two down-sides are (1) cron tasks will only run when Drupal is processing requests; and (2) the 'weight' (processing and memory) of running the cron tasks will be added to some arbitrary unknown page request, which may slow down those requests, and has the potential to exceed memory limits on a complex site.

The second way (which is applicable to any version of Drupal) is to [create a cron job](/node/23714), or use some other external (to Drupal) method of triggering its cron tasks, such as an external cron job service like [EasyCron](https://www.easycron.com) or [Cronless](http://cronless.com). This is the more reliable of the two methods (because it will always run on schedule), and it uses fewer resources (because the cron processing is not added to a page request). Therefore this is generally the preferred way to run cron, when you have the choice. Note that if you create a cron job, you may want to disable the "automated cron" system entirely.

In *Drupal 7* you can manage the "automated cron" via the Administration \> Configuration \> System \> Cron (admin/config/system/cron).

## Disabling "automated cron"

For performance reasons, or if you want to ensure that cron can only ever run from an external trigger, it may be desirable to disable the automated cron system.

You can disable it by setting the "Run cron every" value to "Never" (e.g., at Administration \> Configuration \> System \> Cron (admin/config/system/cron).

Alternatively, in *Drupal 7*, you can set the 'cron_safe_threshold' variable in the {variable} table to 0. (Note that drush will assume this variable is 0 if you have left the "Run cron every" value at the default, so you will need to set it explicitly, either at admin/config/system/cron, or via `drush -y vset cron_safe_threshold 0`)

Another way to disable cron in *Drupal 7* is to add the following line to your settings.php:  
`$conf['cron_safe_threshold'] = 0;`

Note that this fixes the setting at admin/config/system/cron to "Never", and administrative users cannot override it.

## Resources

[*Got Drupal* video about cron Drupal 6](http://gotdrupal.com/videos/setting-up-drupal-cron) that talks about cron, shows various ways of configuring it and helps troubleshooting.
