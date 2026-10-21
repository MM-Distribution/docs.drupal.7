---
title: "Using PostgreSQL EXPLAIN"
source_url: "https://www.drupal.org/docs/7/guidelines-for-sql/using-postgresql-explain"
page_type: page
last_updated: "Last updated on 8 September 2016"
published: "2009-08-26T08:24:18+00:00"
modified: "2016-09-08T14:47:50+00:00"
breadcrumb: ["Drupal 7", "Drupal 7 SQL guidelines"]
fetched: "2026-10-21T07:15:13Z"
raw: "raw/docs/7/guidelines-for-sql/using-postgresql-explain.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Using PostgreSQL EXPLAIN

To display the query plan, run `EXPLAIN my_query` using an SQL client like [pgAdmin3](http://www.pgadmin.org) or any other PostgreSQL client.

Example:

``` php
EXPLAIN SELECT * FROM tenk1 WHERE unique1 < 100;

                                  QUERY PLAN
------------------------------------------------------------------------------
 Bitmap Heap Scan on tenk1  (cost=2.37..232.35 rows=106 width=244)
   Recheck Cond: (unique1 < 100)
   ->  Bitmap Index Scan on tenk1_unique1  (cost=0.00..2.37 rows=106 width=0)
         Index Cond: (unique1 < 100)
```

The query plan should be read on reverse:

- Bitmap Index Scan on tenk1_unique1 is processed **firstly**.
- Bitmap Heap Scan on tenk1 is processed **secondly**.

The structure of a query plan is a tree of plan nodes. Nodes at the bottom level of the tree are table scan nodes: they return raw rows from a table. There are different types of scan nodes for different table access methods: sequential scans, index scans, and bitmap index scans.

Another example:

``` php
EXPLAIN SELECT *
FROM tenk1 t1, tenk2 t2
WHERE t1.unique1 < 100 AND t1.unique2 = t2.unique2;
```

Results in:

``` php
                                        QUERY PLAN
------------------------------------------------------------------------------------------
 Hash Join  (cost=232.61..741.67 rows=106 width=488)
   Hash Cond: (t2.unique2 = t1.unique2)
   ->  Seq Scan on tenk2 t2  (cost=0.00..458.00 rows=10000 width=244)
   ->  Hash  (cost=232.35..232.35 rows=106 width=244)
         ->  Bitmap Heap Scan on tenk1 t1  (cost=2.37..232.35 rows=106 width=244)
               Recheck Cond: (unique1 < 100)
               ->  Bitmap Index Scan on tenk1_unique1  (cost=0.00..2.37 rows=106 width=0)
                     Index Cond: (unique1 < 100)
```

The line starting with **Seq Scan** indicates that PostgreSQL is processig every row. This takes quite a long time, because the product of the number of rows in each table must be examined.

The row processing of data is called a **sequential scan**.

Now jump to [Understanding the logic behind EXPLAIN ANALYSE](/node/559772) to continue.

Reference:  
[PostgreSQL EXPLAIN syntax](http://www.postgresql.org/docs/current/static/using-explain.html)
