---
title: "Database server"
source_url: "https://www.drupal.org/docs/7/system-requirements/database-server"
page_type: page
last_updated: "Last updated on 30 January 2021"
published: "2012-09-13T00:39:17+00:00"
modified: "2021-01-30T13:34:50+00:00"
breadcrumb: ["Drupal 7", "Drupal 7 system requirements"]
fetched: "2026-10-21T05:52:24Z"
raw: "raw/docs/7/system-requirements/database-server.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Database server

**Recommended:** [MySQL](http://www.mysql.com/) (or an equivalent such as [MariaDB](http://mariadb.org/) or [Percona Server](http://www.percona.com/software/percona-server))

### MySQL, MariaDB or Percona Server

Drupal 7 supports MySQL 5.0.15/MySQL 5.1.30/MariaDB 5.1.44/Percona Server 5.1.70 or higher, and requires the PDO database extension for PHP. (See [What is PDO?](/requirements/pdo)). MySQL 8 support was added since Drupal 7.76 release.

Drupal has been extensively tested with [MariaDB](http://mariadb.org/).

**Notes**

- Drupal makes use of some features not available on some inexpensive hosting plans so please check that your host allows database accounts with the following rights:  
  SELECT, INSERT, UPDATE, DELETE, CREATE, DROP, INDEX, ALTER.  
  These rights are sufficient to run Drupal 7
- Some contributed modules, additionally require the following rights:  
  CREATE TEMPORARY TABLES, LOCK TABLES.
- It may be necessary to set the system variable max_allowed_packet to at least 16M. Some inexpensive hosting plans set this value too low (the MySQL default is only 1M, the MariaDB default from 10.1.7 is 4MB). In that case, you may need to choose a better hosting plan. A value of 1M may be sufficient for Drupal 5.
- Drupal 7 and earlier support MyISAM and InnoDB table types. Drupal 8 no longer supports MyISAM as the primary storage engine, so InnoDB table types are recommended. NDB tables (MySQL Cluster) are not supported.
- Note that if your web hosting account is set up with a graphic control panel such as Plesk or CPanel, it is very likely that you do not need to worry about installing a driver for MySQL -- it is probably already installed on your server. You might wish to simply create your database and proceed with installing Drupal, and then refer back to Drupal documentation for specific troubleshooting help if you run into problems.
- NO_AUTO_CREATE_USER was removed in MySQL 8.0.11. Some hosting providers/MySQL packages may report the wrong MySQL version. If this is the case, set 'sql_mode' ('init_commands') manually in settings.php. The settings will override defaults.

### PostgreSQL

Drupal 7 supports PostgreSQL 8.3 or higher.

Note: Some contributed modules are not as abstracted from MySQL-specific code as everyone would like. If you are familiar with PostgreSQL please file issues with those contributed modules as you find them.

### SQLite

Drupal 7 supports SQLite 3.3.7 or higher.

Note: Some contributed modules are not as abstracted from MySQL-specific code as everyone would like. If you are familiar with SQLite please file issues with those contributed modules as you find them.

### Other database servers

[Microsoft SQL Server](http://drupal.org/project/sqlsrv), [Oracle](http://drupal.org/project/oracle), and [MongoDB](https://drupal.org/project/mongodb) are supported by additional modules.

Please see discussions in the [Enterprise Group](http://groups.drupal.org/enterprise) if you are interested in working on database support.
