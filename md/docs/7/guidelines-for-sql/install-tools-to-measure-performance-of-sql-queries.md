---
title: "Install tools to measure performance of SQL queries"
source_url: "https://www.drupal.org/docs/7/guidelines-for-sql/install-tools-to-measure-performance-of-sql-queries"
page_type: page
last_updated: "Last updated on 8 September 2016"
published: "2009-08-26T09:28:02+00:00"
modified: "2016-09-08T14:47:50+00:00"
breadcrumb: ["Drupal 7", "Drupal 7 SQL guidelines"]
fetched: "2026-10-21T07:13:56Z"
raw: "raw/docs/7/guidelines-for-sql/install-tools-to-measure-performance-of-sql-queries.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Install tools to measure performance of SQL queries

In this guide, the following set-up is needed:

- Install Drupal [devel](http://drupal.org/project/devel) module and display SQL execution time on each web page.
- Install an SQL client like pgAdmin3 for PostgreSQL or PhpMyAdmin for MySQL to verify query execution time and use debugging techniques like EXPLAIN ANALYSE.
- Enable server-side logging of the SQL slow queries running more than 30 ms.

Depending on your database, read one of the following page:
