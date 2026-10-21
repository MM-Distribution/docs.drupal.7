---
title: "Using MySQL EXPLAIN"
source_url: "https://www.drupal.org/docs/7/guidelines-for-sql/using-mysql-explain"
page_type: page
last_updated: "Last updated on 8 September 2016"
published: "2009-08-26T08:26:24+00:00"
modified: "2016-09-08T14:47:50+00:00"
breadcrumb: ["Drupal 7", "Drupal 7 SQL guidelines"]
fetched: "2026-10-21T07:14:57Z"
raw: "raw/docs/7/guidelines-for-sql/using-mysql-explain.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Using MySQL EXPLAIN

To display the query plan, run `EXPLAIN my_query` using an SQL client like [PhpMyAdmin](http://www.phpmyadmin.org) or any other MySQL client.

Example: the following query

``` php
EXPLAIN SELECT tt.TicketNumber, tt.TimeIn,
               tt.ProjectReference, tt.EstimatedShipDate,
               tt.ActualShipDate, tt.ClientID,
               tt.ServiceCodes, tt.RepetitiveID,
               tt.CurrentProcess, tt.CurrentDPPerson,
               tt.RecordVolume, tt.DPPrinted, et.COUNTRY,
               et_1.COUNTRY, do.CUSTNAME
        FROM tt, et, et AS et_1, do
        WHERE tt.SubmitTime IS NULL
          AND tt.ActualPC = et.EMPLOYID
          AND tt.AssignedPC = et_1.EMPLOYID
          AND tt.ClientID = do.CUSTNMBR;
```

Results in:  
  
`table type possible_keys key key_len ref rows Extra`  
`et ALL PRIMARY NULL NULL NULL 74`  
`do ALL PRIMARY NULL NULL NULL 2135`  
`et_1 ALL PRIMARY NULL NULL NULL 74`  
`tt ALL AssignedPC, NULL NULL NULL 3872`  
`ClientID,`  
`ActualPC`  
`Range checked for each record (index map: 0x23)`  

Because type is ALL for each table, this output indicates that MySQL is generating a Cartesian product of all the tables; that is, every combination of rows. This takes quite a long time, because the product of the number of rows in each table must be examined.

The row processing of data is called a **sequential scan**.

Now jump to [Understanding the logic behind EXPLAIN ANALYSE](/node/559772) to continue.

Reference:  
[MySQL EXPLAIN syntax](http://dev.mysql.com/doc/refman/5.0/en/using-explain.html)
