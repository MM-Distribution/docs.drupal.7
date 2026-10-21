---
title: "Understanding the logic behind EXPLAIN ANALYSE"
source_url: "https://www.drupal.org/docs/7/guidelines-for-sql/understanding-the-logic-behind-explain-analyse"
page_type: page
last_updated: "Last updated on 8 September 2016"
published: "2009-08-26T08:28:51+00:00"
modified: "2016-09-08T14:47:50+00:00"
breadcrumb: ["Drupal 7", "Drupal 7 SQL guidelines"]
fetched: "2026-10-21T07:15:29Z"
raw: "raw/docs/7/guidelines-for-sql/understanding-the-logic-behind-explain-analyse.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Understanding the logic behind EXPLAIN ANALYSE

When processing queries, the database has two possibilities:

- Access the data directly using indexes.
- Perform sequential scan on disc or in memory.

**Sequential scans** on large tables are considered **evil**, because they eat database memory and CPU time. A sequential scan on 100.000 rows will consume **100.000 CPU cycles** . Even more when scanning from disc.

Therefore, the logic behind debugging queries is to **run EXPLAIN on each slow query** and **hunt for sequential scans**.

When you find a sequential scan, try to rewrite the query.  
Rewriting queries takes both time and effort.

Here are examples for the most simple cases:

- Add an index on columns involded in sequential scans.
- Make sure that JOIN left and right colums have indexes.

``` php
SELECT foo, bar FROM table1 t1
INNER JOIN table2  t2 on t1.a = t2.a
WHERE t2.c=1
```

  
Of course, t1.a and t2.a should carry indexes.

The guide covers detailed techniques for optimizing queries.

Usually, you can always transform a sequential query into a collection of INNER, LEFT and RIGHT JOINs which does not produce a sequential scan or produces it in the very last steps, when minimal information can be loaded in memory and computer fast.
