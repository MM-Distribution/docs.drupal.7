---
title: "Conclusion and summary of the guidelines"
source_url: "https://www.drupal.org/docs/7/guidelines-for-sql/conclusion-and-summary-of-the-guidelines"
page_type: page
last_updated: "Last updated on 8 September 2016"
published: "2009-08-26T13:05:53+00:00"
modified: "2016-09-08T14:47:50+00:00"
breadcrumb: ["Drupal 7", "Drupal 7 SQL guidelines"]
fetched: "2026-10-21T07:16:15Z"
raw: "raw/docs/7/guidelines-for-sql/conclusion-and-summary-of-the-guidelines.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Conclusion and summary of the guidelines

1.  Use a **collection of SQL performance tools**, including Drupal Devel module, database server-side logging and an SQL client. You will need these three tools, install them and learn to use them.
2.  Log **slow SQL queries** server-side in the database. SQL query should always execute in less than 30 ms in the database. If not, they should be logged.
3.  Use Drupal Devel module for a **first analysis** of these queries.
4.  Run **EXPLAIN** on slow queries in the SQL client to find sequential scans.
5.  Sequential scans are your **enemies**, especially if you plan to run your code on large servers. Try to understand when CPU time is lost. Follow simple rules to write queries which do not imply any sequential scan or very rarely. This will drive down CPU time and improve the quality of your code.
