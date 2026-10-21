---
title: "Run EXPLAIN on slow queries to find sequential scans"
source_url: "https://www.drupal.org/docs/7/guidelines-for-sql/run-explain-on-slow-queries-to-find-sequential-scans"
page_type: page
last_updated: "Last updated on 8 September 2016"
published: "2009-08-26T07:13:18+00:00"
modified: "2016-09-08T14:47:50+00:00"
breadcrumb: ["Drupal 7", "Drupal 7 SQL guidelines"]
fetched: "2026-10-21T07:14:42Z"
raw: "raw/docs/7/guidelines-for-sql/run-explain-on-slow-queries-to-find-sequential-scans.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Run EXPLAIN on slow queries to find sequential scans

A database system executes each query in one or several steps.  
The **query plan** displays the execution time of each step of query processing.

This short article discusses how to use EXPLAIN ANALYSE to optimize queries.
