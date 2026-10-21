---
title: "Overview"
source_url: "https://www.drupal.org/docs/7/system-requirements/overview"
page_type: page
last_updated: "Last updated on 18 August 2023"
published: "2003-02-02T16:25:17+00:00"
modified: "2023-08-18T14:28:44+00:00"
breadcrumb: ["Drupal 7", "Drupal 7 system requirements"]
fetched: "2026-10-21T05:51:53Z"
raw: "raw/docs/7/system-requirements/overview.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Overview

**Note: this page should not be edited without first discussing the changes in a [Drupal Core issue](/node/add/project-issue/drupal) as the requirements for each version of Drupal are decided upon by the Drupal Core developers.**

To install and run Drupal your web server must meet certain minimum requirements. Most web hosting companies meet these requirements. However, a few stand out by also actively supporting the Drupal community. If you need hosting, consider selecting one of [these web hosts](http://drupal.org/hosting).

## Disclaimer

Note that the minimum requirements of Drupal core can be subject to change, given an important enough reason. Where such a change is likely to have broad impact on Drupal's user base, every effort will be made to communicate these decisions ahead of time.

## Disk space

A minimum installation requires 15 Megabytes. 60 MB is needed for a website with many contributed modules and themes installed. Keep in mind you need much more for the database, files uploaded by the users, media, backups and other files.

## Web server

Apache, Nginx, Microsoft IIS or any other web server with proper PHP support.  
[More details about web server requirements.](/requirements/webserver)

## Database

- MySQL 5.0.15/MariaDB 5.1.44/Percona Server 5.1.70 or higher with PDO,
- PostgreSQL 8.3 or higher with PDO,
- SQLite 3.3.7 or higher

[Microsoft SQL Server](/project/sqlsrv) and [Oracle](/project/oracle) are supported by additional modules.  
[More details about database requirements.](/requirements/database)

## PHP

PHP 5.6 or higher (**8.x or higher strongly recommended**).

[More details about PHP requirements,](/requirements/php) including [PHP memory](https://www.drupal.org/requirements/php#memory).

See also the [Site Performance section](http://drupal.org/node/627252) of the Administration Guide and the [webhosting troubleshooting FAQ](/node/34022).
