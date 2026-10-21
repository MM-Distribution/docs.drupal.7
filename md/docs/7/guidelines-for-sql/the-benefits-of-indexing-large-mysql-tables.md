---
title: "The Benefits of Indexing Large MySQL Tables"
source_url: "https://www.drupal.org/docs/7/guidelines-for-sql/the-benefits-of-indexing-large-mysql-tables"
page_type: page
last_updated: "Last updated on 28 April 2020"
published: "2010-06-07T20:04:11+00:00"
modified: "2020-04-28T08:36:07+00:00"
breadcrumb: ["Drupal 7", "Drupal 7 SQL guidelines"]
fetched: "2026-10-21T07:14:27Z"
raw: "raw/docs/7/guidelines-for-sql/the-benefits-of-indexing-large-mysql-tables.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# The Benefits of Indexing Large MySQL Tables

The use of indexes to assist with large blocks of tables, data may have considerable impact on reducing MySQL query execution and, thus, overall CPU overhead. Non-indexed tables are nothing more than unordered lists; hence, the MySQL engine must search them from starting to end. This may have little impact when working with small tables, but may dramatically affect search time for larger tables.

Informit.com offers an excellent [essay](http://www.informit.com/articles/article.aspx?p=377652) on why and how we index. It also talks about the dangers of "over-indexing".

It is encouraged that Drupal developers familiarize themselves with the concepts described above, so that they may make appropriate decisions on how and when to index tables of data used within their modules.

## Mysql Index Advantages

Indexing is an important feature of MySQL. It supports different type of indexes like primary key index, unique index, normal index and full-text index. Indexes help to speed up the retrieval of data from MySQL database server. When retrieving the data from a database table, MySQL first checks whether the index of table exists; If yes it will use index to select exact physical corresponding rows without scanning the whole table.

##### Creating Indexes

Mostly we create index when creating table. Any column in creating table statement declared as PRIMARY KEY, KEY, UNIQUE or INDEX will be indexed automatically by MySQL. In addition, you can add indexes to the tables which has data. The statement to create index in MySQL is as follows:

`CREATE [UNIQUE|FULLTEXT|SPATIAL] INDEX index_name`  
`USING [BTREE | HASH | RTREE]`  
`ON table_name (column_name [(length)] [ASC | DESC],…)`

In above statement UNIQUE specify that MySQL will create a constraint that all values in the index must be distinct. Duplicated NULL is allowed in all storage engine except BDB.

The FULLTEXT index is supported only by MyISAM storage engine and only accepted columns which have data type is CHAR,VARCHAR or TEXT.

The SPATIAL index supports spatial column and available in MyISAM storage engine. In addition, the column value must not be NULL.

Then you name the index using index types such as BTREE, HASH or RTREE also based on storage engine

In below index create statement, I have created index to emp_no column on employees table to make the record retreaval faster. The SQL statement to create index is as follows

`CREATE INDEX emp_no ON employees(emp_no)`

##### Advantages of MySQL Indexes

1- Indexes make search queries much faster.

2- Indexes like primary key index and unique index help to avoid duplicate row data.

3- Full-text indexes in MySQL, users have the opportunity to optimize searching against even large amounts of text located in any field indexed as such.

[db_index](https://www.drupal.org/project/db_index) module (D7) provide the user interface to add or drop the database Table indexes for the Mysql databases. Using this module you can have the information about what all are the Indexes with associated columns and its Tables.
