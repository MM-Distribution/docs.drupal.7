---
title: "Make sure that JOIN columns both carry indexes of the same type"
source_url: "https://www.drupal.org/docs/7/guidelines-for-sql/make-sure-that-join-columns-both-carry-indexes-of-the-same-type"
page_type: page
last_updated: "Last updated on 8 September 2016"
published: "2009-08-26T11:39:09+00:00"
modified: "2016-09-08T14:47:50+00:00"
breadcrumb: ["Drupal 7", "Drupal 7 SQL guidelines"]
fetched: "2026-10-21T07:16:00Z"
raw: "raw/docs/7/guidelines-for-sql/make-sure-that-join-columns-both-carry-indexes-of-the-same-type.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Make sure that JOIN columns both carry indexes of the same type

Running a JOIN on two columns of different data types may force a sequential scan.

Example:

``` php
SELECT * 
FROM foo
INNER JOIN bar ON foo.a = bar.b
```

If foo.a and bar.b are not of the same data type, the query planner will need to cast the data of each foo.a and bar.b entry. For instance, if foo.a is integer and bar.b is string, it can't use one to lookup in the other unless and until it casts to the right type. This happens using any database, inducing MySQL and PostgreSQL.

Even if the cast happens on memory only, it will consume CPU time, at least one cycle per row and hence will be very slow. On very large tables, this should be avoided.

More examples soon.
