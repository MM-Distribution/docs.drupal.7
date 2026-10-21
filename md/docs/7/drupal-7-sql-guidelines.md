---
title: "Drupal 7 SQL guidelines"
source_url: "https://www.drupal.org/docs/7/drupal-7-sql-guidelines"
page_type: guide
published: "2016-09-08T14:44:01+00:00"
modified: "2026-02-24T12:54:42+00:00"
breadcrumb: ["Drupal 7"]
fetched: "2026-10-21T07:13:40Z"
raw: "raw/docs/7/drupal-7-sql-guidelines.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Drupal 7 SQL guidelines

These guidelines provide some tips for writing efficient SQL code for Drupal 7. Guidelines apply to MySQL and PostgreSQL.

## [Install tools to measure performance of SQL queries](/docs/7/guidelines-for-sql/install-tools-to-measure-performance-of-sql-queries)

In this guide, the following set-up is needed:

## [Logging slow SQL queries server-side in PostgreSQL](/docs/7/guidelines-for-sql/logging-slow-sql-queries-server-side-in-postgresql)

A first solution is to modify PostgreSQL postgresql.conf configuration file:

## [The Benefits of Indexing Large MySQL Tables](/docs/7/guidelines-for-sql/the-benefits-of-indexing-large-mysql-tables)

The use of indexes to assist with large blocks of tables, data may have considerable impact on reducing MySQL query execution and, thus,

## [Run EXPLAIN on slow queries to find sequential scans](/docs/7/guidelines-for-sql/run-explain-on-slow-queries-to-find-sequential-scans)

A database system executes each query in one or several steps.

## [Using MySQL EXPLAIN](/docs/7/guidelines-for-sql/using-mysql-explain)

To display the query plan, run EXPLAIN my_query using an SQL client like PhpMyAdmin or any other MySQL client.

## [Using PostgreSQL EXPLAIN](/docs/7/guidelines-for-sql/using-postgresql-explain)

To display the query plan, run EXPLAIN my_query using an SQL client like pgAdmin3 or any other PostgreSQL client.

## [Understanding the logic behind EXPLAIN ANALYSE](/docs/7/guidelines-for-sql/understanding-the-logic-behind-explain-analyse)

When processing queries, the database has two possibilities:

## [Indexes are not symmetric](/docs/7/guidelines-for-sql/indexes-are-not-symmetric)

Multi-column indexes can be rather tricky to understand. An index on several columns is not symmetric and doesn't work equally on every

## [Make sure that JOIN columns both carry indexes of the same type](/docs/7/guidelines-for-sql/make-sure-that-join-columns-both-carry-indexes-of-the-same-type)

Running a JOIN on two columns of different data types may force a sequential scan.

## [Conclusion and summary of the guidelines](/docs/7/guidelines-for-sql/conclusion-and-summary-of-the-guidelines)

## [Writing code compliant with both MySQL and PostgreSQL](/docs/7/guidelines-for-sql/writing-code-compliant-with-both-mysql-and-postgresql)

Writing code compliant with both MySQL and PostgreSQL

- [MySQLism and PostgreSQLism: DELETE on JOINS requires the USING syntax](/docs/7/guidelines-for-sql/writing-code-compliant-with-both-mysql-and-postgresql/mysqlism-and-0)
- [MySQLism and PostgreSQLism: avoid deleting data in several tables in one query](/docs/7/guidelines-for-sql/writing-code-compliant-with-both-mysql-and-postgresql/mysqlism-and)
- [MySQLism: MySQL considers INT and BOOLEAN the same](/docs/7/guidelines-for-sql/writing-code-compliant-with-both-mysql-and-postgresql/mysqlism-mysql)
- [MySQLism: MySQL will automatically cast INT into VARCHAR/CHAR](/docs/7/guidelines-for-sql/writing-code-compliant-with-both-mysql-and-postgresql/mysqlism-mysql-will)
- [MySQLism: Use CASE instead of IF().](/docs/7/guidelines-for-sql/writing-code-compliant-with-both-mysql-and-postgresql/mysqlism-use-case)
- [MySQLism: Use SELECT(DISTINCT ) only for one field, use SELECT COUNT(\*) FROM (SELECT DISTINCT ... ) ... for multiple](/docs/7/guidelines-for-sql/writing-code-compliant-with-both-mysql-and-postgresql/mysqlism-use)
- [MySQLism: avoid UPDATE on duplicate](/docs/7/guidelines-for-sql/writing-code-compliant-with-both-mysql-and-postgresql/mysqlism-avoid-0)
- [MySQLism: avoid ambiguous queries](/docs/7/guidelines-for-sql/writing-code-compliant-with-both-mysql-and-postgresql/mysqlism-avoid)
- [MySQLism: avoid nested ORDER BY, use nested queries](/docs/7/guidelines-for-sql/writing-code-compliant-with-both-mysql-and-postgresql/mysqlism-avoid-4)
- [MySQLism: avoid using IF() in SELECT use CASE()](/docs/7/guidelines-for-sql/writing-code-compliant-with-both-mysql-and-postgresql/mysqlism-avoid-using)
- [MySQLism: avoid using MySQL IGNORE syntax](/docs/7/guidelines-for-sql/writing-code-compliant-with-both-mysql-and-postgresql/mysqlism-avoid-1)
- [MySQLism: avoid using MySQL REPLACE syntax](/docs/7/guidelines-for-sql/writing-code-compliant-with-both-mysql-and-postgresql/mysqlism-avoid-2)
- [MySQLism: avoid using double quotes for alphanumerical values](/docs/7/guidelines-for-sql/writing-code-compliant-with-both-mysql-and-postgresql/mysqlism-avoid-3)
- [MySQLism: use TEXT values and not VARCHAR(255)](/docs/7/guidelines-for-sql/writing-code-compliant-with-both-mysql-and-postgresql/mysqlism-use-text)
- [Oracleism: Don't use AS for table aliases](/docs/7/guidelines-for-sql/writing-code-compliant-with-both-mysql-and-postgresql/oracleism-dont-use)
- [PostgreSQLism: CONCAT() can only take two arguments (D6 only, fixed in D7)](/docs/7/guidelines-for-sql/writing-code-compliant-with-both-mysql-and-postgresql/postgresqlism-concat)
- [PostgreSQLism: all non-aggregated fields to be present in the GROUP BY clause](/docs/7/guidelines-for-sql/writing-code-compliant-with-both-mysql-and-postgresql/postgresqlism-all)
- [PostgreSQLism: avoid mutiple ROW inserts (PostgreSQL \< 8.2 only)](/docs/7/guidelines-for-sql/writing-code-compliant-with-both-mysql-and-postgresql/postgresqlism-avoid)
- [Testing SQL 99 compliance](/docs/7/guidelines-for-sql/writing-code-compliant-with-both-mysql-and-postgresql/testing-sql-99)
- [Writing code compliant with both MySQL and PostgreSQL](/docs/7/guidelines-for-sql/writing-code-compliant-with-both-mysql-and-postgresql/writing-code)
