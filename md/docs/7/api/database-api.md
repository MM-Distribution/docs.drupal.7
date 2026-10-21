---
title: "Database API"
source_url: "https://www.drupal.org/docs/7/api/database-api"
page_type: guide
published: "2016-10-14T21:01:06+00:00"
modified: "2018-02-20T06:59:35+00:00"
breadcrumb: ["Drupal 7", "Drupal 7 APIs"]
fetched: "2026-10-21T07:54:19Z"
raw: "raw/docs/7/api/database-api.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Database API

Documentation for Database API in Drupal 7.

## [Database API overview](/docs/7/api/database-api/database-api-overview)

The Drupal 7 Database API provides a standard, vendor-agnostic abstraction layer for accessing database servers.

## [General concepts](/docs/7/api/database-api/general-concepts)

The Drupal database layer is built on top of the PHP's PDO library. PDO provides a unified, object-oriented API for accessing different

## [Database configuration](/docs/7/api/database-api/database-configuration)

The primary means of defining a database connection is via the \$databases array in settings.php. As its name suggests, \$databases allows

## [Static queries](/docs/7/api/database-api/static-queries)

Use static queries for simple SELECT statements that don't need to be altered at run-time.

## [Fetching into a custom class](/docs/7/api/database-api/fetching-into-a-custom-class)

Queries can be fetched into objects based on custom classes. For example, if we have a class named ExampleClass the following query will

## [Dynamic queries](/docs/7/api/database-api/dynamic-queries)

Dynamic queries in Drupal 7 Database API.

- [Introduction to dynamic queries](/docs/7/api/database-api/dynamic-queries/introduction-to-dynamic-queries)
- [Conditional clauses](/docs/7/api/database-api/dynamic-queries/conditional-clauses)
- [Count queries](/docs/7/api/database-api/dynamic-queries/count-queries)
- [Distinct](/docs/7/api/database-api/dynamic-queries/distinct)
- [Expressions](/docs/7/api/database-api/dynamic-queries/expressions)
- [Extenders](/docs/7/api/database-api/dynamic-queries/extenders)
- [Fields](/docs/7/api/database-api/dynamic-queries/fields)
- [Grouping](/docs/7/api/database-api/dynamic-queries/grouping)
- [Joins](/docs/7/api/database-api/dynamic-queries/joins)
- [Ordering](/docs/7/api/database-api/dynamic-queries/ordering)
- [Query alteration (tagging)](/docs/7/api/database-api/dynamic-queries/query-alteration-tagging)
- [Ranges and limits](/docs/7/api/database-api/dynamic-queries/ranges-and-limits)
- [Table sorting](/docs/7/api/database-api/dynamic-queries/table-sorting)
- [Unions](/docs/7/api/database-api/dynamic-queries/unions)

## [Result sets](/docs/7/api/database-api/result-sets)

A Select query will always return a result set object of zero or more records. There are several ways to then retrieve data from that

## [Insert queries](/docs/7/api/database-api/insert-queries)

Insert queries must always use a query builder object. Certain databases require special handling for LOB (Large OBject, such as TEXT in

## [Update queries](/docs/7/api/database-api/update-queries)

Update queries must always use a query builder object. Certain databases require special handling for LOB (Large OBject, such as TEXT on

## [Delete queries](/docs/7/api/database-api/delete-queries)

Delete queries must always use a query builder object. They are started using the db_delete() function as follows:

## [Merge queries using db_merge](/docs/7/api/database-api/merge-queries-using-db_merge)

Merge queries are a special type of hybrid query. Although a syntax is defined for them in the SQL 2003 specification, virtually no

## [Writing database drivers](/docs/7/api/database-api/writing-database-drivers)

Coming soon, really! webchick insisted I post the documentation as it stands now, and this part isn't done yet. I'll get it added just as

## [Error handling](/docs/7/api/database-api/error-handling)

The Database API throws exceptions on error, which can be picked up by wrapping your database operations in try {} catch() {} blocks, as

## [Transactions](/docs/7/api/database-api/transactions)

Drupal also supports transactions, including a transparent fallback for databases that do not support transactions. However, transactions

## [Chaining](/docs/7/api/database-api/chaining)

There is a lot of talk about chaining database api functions together, for example:

## [Functions and operators](/docs/7/api/database-api/functions-and-operators)

Drupal's database layer does not provide cross-database abstraction of SQL functions. For portability across supported database engines

## [SQL Views](/docs/7/api/database-api/sql-views)

The theory behind SQL Views, and the difference with the Views module.
