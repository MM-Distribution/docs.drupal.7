---
title: "Indexes are not symmetric"
source_url: "https://www.drupal.org/docs/7/guidelines-for-sql/indexes-are-not-symmetric"
page_type: page
last_updated: "Last updated on 8 September 2016"
published: "2009-08-21T09:12:02+00:00"
modified: "2016-09-08T14:47:50+00:00"
breadcrumb: ["Drupal 7", "Drupal 7 SQL guidelines"]
fetched: "2026-10-21T07:15:44Z"
raw: "raw/docs/7/guidelines-for-sql/indexes-are-not-symmetric.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Indexes are not symmetric

Multi-column indexes can be rather tricky to understand. An index on several columns is not symmetric and doesn't work equally on every field. For example, an index on a dual field:

``` php
CREATE INDEX foo ON table_name (bar1, bar2);
```

is not equal to two indexes on single field:

``` php
CREATE INDEX bar1 ON table_name (bar1);

CREATE INDEX bar2 ON table_name (bar2);
```

A database server can only use this index to optimize conditions that are on the leftmost part of the index. For example, the following query will not use this index:

``` php
SELECT * FROM table_name WHERE bar2 = 'foo'
```

But those two will:

``` php
SELECT * FROM table_name WHERE bar1 = 'foo' AND bar2 = 'bar'
SELECT * FROM table_name WHERE bar1 = 'foo' AND bar2 > 'bar'
```

Some databases claim that a dual index works equally right and left. This is not portable and probably not true, as multi-column indexing may result in a sequential scan in complex queries:

Reference: <http://www.postgresql.org/docs/8.4/static/indexes-multicolumn.html>

> A multicolumn B-tree index can be used with query conditions that involve any subset of the index's columns, but the index is most efficient when there are constraints on the leading (leftmost) columns. The exact rule is that equality constraints on leading columns, plus any inequality constraints on the first column that does not have an equality constraint, will be used to limit the portion of the index that is scanned. Constraints on columns to the right of these columns are checked in the index, so they save visits to the table proper, but they do not reduce the portion of the index that has to be scanned. For example, given an index on (a, b, c) and a query condition WHERE a = 5 AND b \>= 42 AND c \< 77, the index would have to be scanned from the first entry with a = 5 and b = 42 up through the last entry with a = 5. Index entries with c \>= 77 would be skipped, but they'd still have to be scanned through. This index could in principle be used for queries that have constraints on b and/or c with no constraint on a — **but the entire index would have to be scanned, so in most cases the planner would prefer a sequential table scan over using the index**.

According to <http://dev.mysql.com/doc/refman/5.1/en/mysql-indexes.html:>

> MySQL cannot use an index if the columns do not form a leftmost prefix of the index.

A good decision on wether to use multi-column indexes will take into account the cardinality of the data. Sometimes a multi-column index is simply the right answer, particularly if the values in the first column of the index do not limit the rows sufficiently.

Also in where exists clauses the rdbms will not even load the row if the primary key is the composite index, but it will have to.

Indexes are best thought of like caches, you use the right caching mechanism for the job, and you only do it when you can demonstrate performance improvement.

**Therefore the proposed solution to enhance Drupal is to hunt for sequential scans and add single indexes when needed.**
