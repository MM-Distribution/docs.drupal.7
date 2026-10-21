---
title: "Logging slow SQL queries server-side in PostgreSQL"
source_url: "https://www.drupal.org/docs/7/guidelines-for-sql/logging-slow-sql-queries-server-side-in-postgresql"
page_type: page
last_updated: "Last updated on 8 September 2016"
published: "2009-08-26T16:29:55+00:00"
modified: "2016-09-08T14:47:50+00:00"
breadcrumb: ["Drupal 7", "Drupal 7 SQL guidelines"]
fetched: "2026-10-21T07:14:11Z"
raw: "raw/docs/7/guidelines-for-sql/logging-slow-sql-queries-server-side-in-postgresql.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Logging slow SQL queries server-side in PostgreSQL

A first solution is to modify PostgreSQL **postgresql.conf** configuration file:

Connect to the database server,  
open postgresql.conf configuration file,  
enable query logging and set maximum execution time to 30 ms:

``` php
logging_collector = on
log_directory = 'pg_log'

log_min_duration_statement = 30
```

Restart PostgreSQL server for logging_collector and log_directory to take effect.  
The logs will be written in log_directory under PostgreSQL data directory.

You can decide to print the query plan using these variables (unckeck \# to modify):

``` php
#debug_print_parse = off
#debug_print_rewritten = off
#debug_print_plan = off
#debug_pretty_print = on
#log_checkpoints = off
#log_connections = off
#log_disconnections = off
#log_duration = off
#log_hostname = off
log_line_prefix = '%t ' 
```

These settings apply to the whole database server.

A second solution is to log slow queries interactively using an SQL command.

Connect to the database server, open postgresql.conf file and enable query logging and set maximum execution time to 30 ms:

``` php
logging_collector = on
log_directory = 'pg_log'
```

Restart PostgreSQL for settings to take effect.

Then connect to your SQL client and run:

``` php
SET log_min_duration_statement to 30;
SET debug_print_plan to ON;
```

You can modify Drupal PostgreSQL session manager to run this code automatically on startup.

The code is located in: drupal/includes/database.pgsql.inc  
Locate function db_connect(\$url):

Replace:

``` php
  pg_query($connection, "set client_encoding=\"UTF8\"");
  return $connection;
```

with:

``` php
  pg_query($connection, "set client_encoding=\"UTF8\" ; 
  SET log_min_duration_statement to 30;
  SET debug_print_plan to ON;
  ");
  return $connection;
```

The logs will be written to log_directory.

Retrieving logs in PostgreSQL database  
To be written
