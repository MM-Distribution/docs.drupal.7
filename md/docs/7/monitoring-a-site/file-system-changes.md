---
title: "File system changes"
source_url: "https://www.drupal.org/docs/7/monitoring-a-site/file-system-changes"
page_type: page
last_updated: "Last updated on 2 December 2018"
published: "2014-11-05T11:40:58+00:00"
modified: "2018-12-02T18:46:29+00:00"
breadcrumb: ["Drupal 7", "Monitoring a Drupal 7 site"]
fetched: "2026-10-21T07:04:53Z"
raw: "raw/docs/7/monitoring-a-site/file-system-changes.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# File system changes

## Purpose

This document outlines several methods to track changes to a website at the file or directory level; file system monitoring should be applied alongside regular file and database backups.

## Goals

The goals of file system tracking include:

- Monitor changed and added files
- Log changes and additions
- Ability to revert granular changes
- Automated alerts

## General approaches

Administrators can monitor file system via general technologies such as:

- System utilities
- Revision control
- OS/kernel level monitoring

## Specific tools

Options for file system monitoring include:

- [diff](en.wikipedia.org/wiki/Diff_utility "Wikipedia article on Diff utility") and [drush make](https://www.drupal.org/node/625094 "Drush Make documentation") - build clean test copy of your site and compare against production
- [Git](http://git-scm.com/ "Git homepage") - source code management
- [inotify](https://en.wikipedia.org/wiki/Inotify "Wikipedia article on inotify") and [incron](http://inotify.aiken.cz/?section=incron&page=doc&lang=en "incron documentation") - OS kernel level file monitoring service that can run commands on filesystem events
- [Watcher](https://github.com/gregghz/Watcher/blob/master/jobs.yml "Watcher, Python library for inotify"), Python inotify library
- [OSSEC](http://ossec.net "OSSEC website") - Open Source Host-based Intrusion Detection System that performs log analysis, file integrity checking, policy monitoring, rootkit detection, real-time alerting and active response.

## Considerations

When configuring a file-based monitoring strategy, there are many considerations, including the following:

### Run the monitoring script/service as root

This would make it hard for attackers to disable or modify your file system monitoring solution.

### Disable monitoring during scheduled maintenance/upgrades

This would prevent unnecessary notifications when you are performing regular maintenance on the site.

### Monitor only executable filetypes

It may be reasonably safe to monitor only executable file types, such as .php files, etc. Unnecessary log entries and alerts may be reduced through the use of specific filtering.

### Use strict file system permissions

Read about [securing file permissions and ownership](https://www.drupal.org/node/244924 "securing file permissions and ownership"). In general, avoid allowing *execute* and *write* permissions when possible.
