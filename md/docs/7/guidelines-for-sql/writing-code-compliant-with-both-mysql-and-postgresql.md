---
title: "Writing code compliant with both MySQL and PostgreSQL"
source_url: "https://www.drupal.org/docs/7/guidelines-for-sql/writing-code-compliant-with-both-mysql-and-postgresql"
page_type: guide
published: "2016-09-08T14:45:42+00:00"
modified: "2016-09-08T14:45:42+00:00"
breadcrumb: ["Drupal 7", "Drupal 7 SQL guidelines"]
fetched: "2026-10-21T07:16:31Z"
raw: "raw/docs/7/guidelines-for-sql/writing-code-compliant-with-both-mysql-and-postgresql.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Writing code compliant with both MySQL and PostgreSQL

This guide explains how to write compatible SQL code for both MySQL and PostgreSQL and more generally any SQL99 compatible database. It focuses on Drupal 6. Please add the required information about D7.

MySQLism and PostgreSQLism denote features that exist only in one database, cannot be easily ported and therefore should be avoided.

As a trick, when writing code in MySQL, search "MySQLism" in Drupal web site and you will access all tips quickly. When writing code in PostgreSQL, search "PostgreSQLism" in Drupal web site to do the same.

## [MySQLism and PostgreSQLism: DELETE on JOINS requires the USING syntax](/docs/7/guidelines-for-sql/writing-code-compliant-with-both-mysql-and-postgresql/mysqlism-and-0)

SQL-99 does not allow to delete data in a table when using JOINS. The reasons for this are quite obscure. Maybe it was considered too

## [MySQLism and PostgreSQLism: avoid deleting data in several tables in one query](/docs/7/guidelines-for-sql/writing-code-compliant-with-both-mysql-and-postgresql/mysqlism-and)

SQL-99 does not allow to delete data in several tables in one query. The reasons for this are quite obscure. Maybe that it was considered

## [MySQLism: MySQL considers INT and BOOLEAN the same](/docs/7/guidelines-for-sql/writing-code-compliant-with-both-mysql-and-postgresql/mysqlism-mysql)

SQL-99 standard does not consider that a boolean is an integer with 0 or 1 value. It may also be NULL, which is a third value. Therefore,

## [MySQLism: MySQL will automatically cast INT into VARCHAR/CHAR](/docs/7/guidelines-for-sql/writing-code-compliant-with-both-mysql-and-postgresql/mysqlism-mysql-will)

SQL-99 forbids to cast data between integer and alphanumerical values. The reason is that such a cast may vary depending on locales and the

## [MySQLism: Use CASE instead of IF().](/docs/7/guidelines-for-sql/writing-code-compliant-with-both-mysql-and-postgresql/mysqlism-use-case)

MySQL has a easy syntax that lets you execute IF/ELSE statements in SQL. For example:

## [MySQLism: Use SELECT(DISTINCT ) only for one field, use SELECT COUNT(\*) FROM (SELECT DISTINCT ... ) ... for multiple](/docs/7/guidelines-for-sql/writing-code-compliant-with-both-mysql-and-postgresql/mysqlism-use)

SQL99 specifies COUNT(DISTINCT ) as only taking a single parameter. MySQL and DB/2 support a list of fields for this fuction, Postgres will

## [MySQLism: avoid UPDATE on duplicate](/docs/7/guidelines-for-sql/writing-code-compliant-with-both-mysql-and-postgresql/mysqlism-avoid-0)

MySQL has a nice SQL feature to update records when a duplicate key exist.

## [MySQLism: avoid ambiguous queries](/docs/7/guidelines-for-sql/writing-code-compliant-with-both-mysql-and-postgresql/mysqlism-avoid)

See bug: http://drupal.org/node/1044410

## [MySQLism: avoid nested ORDER BY, use nested queries](/docs/7/guidelines-for-sql/writing-code-compliant-with-both-mysql-and-postgresql/mysqlism-avoid-4)

SQL-99 allows nested queries, but forbids nested ORDER BY. The reason is that nested queries improve the ability of the parser to understand

## [MySQLism: avoid using IF() in SELECT use CASE()](/docs/7/guidelines-for-sql/writing-code-compliant-with-both-mysql-and-postgresql/mysqlism-avoid-using)

Use CASE WHEN \[condition\] THEN result \[WHEN \[condition\] THEN result ...\] \[ELSE result\] END not IF()

## [MySQLism: avoid using MySQL IGNORE syntax](/docs/7/guidelines-for-sql/writing-code-compliant-with-both-mysql-and-postgresql/mysqlism-avoid-1)

MySQL allows the use of IGNORE in UPDATE or REPLACE queries.

## [MySQLism: avoid using MySQL REPLACE syntax](/docs/7/guidelines-for-sql/writing-code-compliant-with-both-mysql-and-postgresql/mysqlism-avoid-2)

MySQL allows running INSERT or UPDATE in one single query, which is extremely useful.

## [MySQLism: avoid using double quotes for alphanumerical values](/docs/7/guidelines-for-sql/writing-code-compliant-with-both-mysql-and-postgresql/mysqlism-avoid-3)

According to SQL-99, double quotes should only be used to reference a column name or a table name.

## [MySQLism: use TEXT values and not VARCHAR(255)](/docs/7/guidelines-for-sql/writing-code-compliant-with-both-mysql-and-postgresql/mysqlism-use-text)

When inserting TEXT into a VARCHAR(255), MySQL trims the value to the first 255 characters. PostgreSQL complains and returns an error, which

## [Oracleism: Don't use AS for table aliases](/docs/7/guidelines-for-sql/writing-code-compliant-with-both-mysql-and-postgresql/oracleism-dont-use)

In both MySQL and PostgreSQL, when giving tables aliases in the FROM clause, it is optional to use the AS keyword.

## [PostgreSQLism: CONCAT() can only take two arguments (D6 only, fixed in D7)](/docs/7/guidelines-for-sql/writing-code-compliant-with-both-mysql-and-postgresql/postgresqlism-concat)

The CONCAT() is supported on both MySQL and Postgresql, but only with two parameters. Where you could write (in MySQL):

## [PostgreSQLism: all non-aggregated fields to be present in the GROUP BY clause](/docs/7/guidelines-for-sql/writing-code-compliant-with-both-mysql-and-postgresql/postgresqlism-all)

This issue is seen very frequently.

## [PostgreSQLism: avoid mutiple ROW inserts (PostgreSQL \< 8.2 only)](/docs/7/guidelines-for-sql/writing-code-compliant-with-both-mysql-and-postgresql/postgresqlism-avoid)

PostgreSQL 8.2, 83 and 8.4 are not affected by this issue.

## [Testing SQL 99 compliance](/docs/7/guidelines-for-sql/writing-code-compliant-with-both-mysql-and-postgresql/testing-sql-99)

Writing SQL-99 compliant code is highly recommended. Mimer validator allows to test SQL-99 compliance online. Writing SQL 99 code ensures

## [Writing code compliant with both MySQL and PostgreSQL](/docs/7/guidelines-for-sql/writing-code-compliant-with-both-mysql-and-postgresql/writing-code)

This section explains how to write compatible SQL code for both MySQL and PostgreSQL and more generally any SQL99 compatible database. It
