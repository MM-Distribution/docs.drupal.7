---
title: "Optimizing MySQL"
source_url: "https://www.drupal.org/docs/7/managing-site-performance/optimizing-mysql"
page_type: page
last_updated: "Last updated on 7 April 2021"
published: "2006-02-25T07:36:24+00:00"
modified: "2021-04-07T07:24:34+00:00"
breadcrumb: ["Drupal 7", "Managing Drupal 7 site performance and scalability"]
fetched: "2026-10-21T07:00:45Z"
raw: "raw/docs/7/managing-site-performance/optimizing-mysql.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Optimizing MySQL

- For a general overview read the [High Performance MySQL](http://www.amazon.com/High-Performance-MySQL-Optimization-Replication/dp/1449314287/) book and/or the [MySQL Performance Blog](http://www.mysqlperformanceblog.com/), especially the [InnoDB performance basics](http://www.mysqlperformanceblog.com/2007/11/01/innodb-performance-optimization-basics/) article.

- Start with an appropriate MySQL [option file](http://dev.mysql.com/doc/refman/5.0/en/option-files.html). For servers with at least 2GB RAM dedicated to MySQL we recommend my-huge.cnf. For servers with a lot of writes, we recommend my-innodb.cnf instead of the default MyISAM engine type.

- To reduce the overhead of creating connections we recommend using [persistent DB connections](http://us2.php.net/mysql_pconnect). **Note: Deprecated as of PHP 5.5.0.**

- In sites running MySQL 5.7.1 or older, if a query is called at least twice with no modifications to the queried tables a significant performance improvement may be gained by avoiding the processing of the query and the execution of the query by reading the query from the [MySQL query cache](https://dev.mysql.com/doc/refman/5.6/en/query-cache.html). **Note: This is no longer recommended as query cache is [deprecated](https://dev.mysql.com/doc/refman/5.7/en/query-cache.html) as of MySQL 5.7.20, and was removed as of MySQL 8.0.**

- Be sure to have enough cached threads or you will launch too many new threads as described in [this story about a Yahoo site](http://jeremy.zawodny.com/blog/archives/000173.html).

- The biggest performance boosts can come from identifying and tuning the slowest queries using the [MySQL slow query logs](https://dev.mysql.com/doc/refman/5.0/en/slow-query-log.html).

- You can use the [DB Maintenance](/node/41588) module or use the mysqlcheck commands below in a cronjob.  

  ``` php
  echo "OPTIMIZE TABLE accesslog,cache,comments,node,users,watchdog;FLUSH TABLES;" |mysql -u user -ppasswd 
  ```

  If you have complete control of the database server you can use:

  ``` php
  mysqlcheck -o -A -p 
  ```

- MySQL supports many different engine types including Archive (MySQL 5+), MyISAM, and InnoDB. Performance sites should use InnoDB for most tables particularly tables such as node that get a lot of writes and reads. [MyISAM exclusive table locks for updates before selects versus InnoDB's row level locking](http://dev.mysql.com/doc/refman/5.0/en/ansi-diff-transactions.html) can mean MyISAM blocks reads if there are many writes. [Convert from MyISAM to InnoDB](http://dev.mysql.com/doc/refman/4.1/en/converting-tables-to-innodb.html).

- In MySQL 5 a new table type called the archive table type was introduced to deal with common requirements for web applications like access logs where only INSERTS and SELECTS were done. If tables such as the Access Log table are determined to not have DELETE, UPDATE, and REPLACE then this MySQL engine type can often offer significant performance improvements as they have done for sites like Slashdot, Yahoo, and Live Journal.

- Make use of the [Percona Toolkit](http://www.percona.com/software/percona-toolkit), especially [pt-variable-advisor](http://www.percona.com/doc/percona-toolkit/2.2/pt-variable-advisor.html) to check for problem settings and [pt-mysql-summary](http://www.percona.com/doc/percona-toolkit/2.2/pt-mysql-summary.html) to get an at-a-glance look at your configuration.

- Avoid [RAID-5](http://en.wikipedia.org/wiki/Standard_RAID_levels#RAID_5) in a high write environment. [It can degrade performance significantly](http://dba.stackexchange.com/a/13036).

- Consider [changing the IO scheduler](http://www.cyberciti.biz/faq/linux-change-io-scheduler-for-harddisk/) if you are running on a dedicated MySQL server. The noop or deadline schedulers can have [significant performance increases](http://www.mysqlperformanceblog.com/2009/01/30/linux-schedulers-in-tpcc-like-benchmark/) over anticipatory and cfq.

## Tools, tips and links

Here are some basic, but high impact ways to optimize MySQL for Drupal (there are much more sophisticated and expensive ways to speed up your database of course):

Note that if you are on a shared hosting plan then only your host will be able to tune MySQL since you won't have access to the my.cnf file. Also, I can only confirm these setting for MySQL 4.0.2 thru the latest 4.0.x version, but I think it would work for 5.x (maybe someone can confirm this and leave a comment...). Actually, it will work for below 4.0.2 I think as long as you add `set-variable =` before each line (see this page for more on [set-variable](http://dev.mysql.com/doc/refman/4.1/en/program-variables.html))

1\. You can analyze your MySQL performance with the [MySQL Performance Tuning Primer Script](https://github.com/BMDan/tuning-primer.sh).

``` php
# cd /usr/local/src/
# wget https://raw.githubusercontent.com/BMDan/tuning-primer.sh/master/tuning-primer.sh
# chmod u+x tuning-primer.sh
# ./tuning-primer.sh 
```

It will ask for your database root user name and password and print out a list of recommendations. Was shocked to learned that on my VPS the cache was not even enabled - very helpful to know (Note: [Read up on the query cache](http://www.tocker.ca/2013/09/27/how-do-you-use-the-query-cache.html) before changing any values there)!

*Another MySQL tuning script using perl:*

<https://github.com/major/MySQLTuner-perl>

``` php
# git clone https://github.com/major/MySQLTuner-perl.git
# cd MySQLTuner-perl
# chmod u+x mysqltuner.pl
# perl mysqltuner.pl 
```

Example of Recommendations (on dedicated server with 2GB of RAM)

``` php
General recommendations: Run OPTIMIZE TABLE to defragment tables for better performance MySQL started within last 24 hours - recommendations may be inaccurate Enable the slow query log to troubleshoot bad queries Set thread_cache_size to 4 as a starting value Increase table_cache gradually to avoid file descriptor limits Read this before increasing table_cache over 64: http://bit.ly/1mi7c4C Variables to adjust: query_cache_size (>= 8M) thread_cache_size (start at 4) table_cache (> 400) innodb_buffer_pool_size (>= 365M) 
```

2\. Next open your my.cnf file in pico or some kind of proper code/text editor:

Depending on the memory resources you have available you'll want to paste in something like these examples (adjust up or down depending on how your system differs, of course):

For a setup with 500mb of RAM your my.cnf file *may* look like this:

``` php
[mysqld]
max_connections = 150
max_user_connections = 150
key_buffer = 36M
myisam_sort_buffer_size = 64M
join_buffer_size = 2M
read_buffer_size = 2M
sort_buffer_size = 3M
table_cache = 1024
thread_cache_size = 286
interactive_timeout = 25
wait_timeout = 1800
connect_timeout = 10
max_allowed_packet = 16M
max_connect_errors = 1000
query_cache_limit = 1M
query_cache_size = 16M
query_cache_type = 1
tmp_table_size = 16M
innodb-flush-log-at-trx-commit=2
```

For a system with 256mb of ram it *may* look like this:

``` php
[mysqld]
max_connections = 75
max_user_connections = 75
key_buffer = 16M
myisam_sort_buffer_size = 32M
join_buffer_size = 1M
read_buffer_size = 1M
sort_buffer_size = 2M
table_cache = 1024
thread_cache_size = 286
interactive_timeout = 25
wait_timeout = 1000
connect_timeout = 10
max_allowed_packet = 1M
max_connect_errors = 1000
query_cache_limit = 1M
query_cache_size = 16M
query_cache_type = 1
tmp_table_size = 16M
innodb-flush-log-at-trx-commit=2
```

**Please note that every server configuration is going to differ and simply pasting these in may cause unexpected results.**

3\. Save your my.cnf file and restart mySQL. This can be done via your control panel or the command line (on some unixes: service mysqld restart otherwise /etc/rc.d/init.d/mysqld restart or /etc/init.d/mysqld restart)

Your new settings are now active and you can run the script from above again and see the difference in your results. After some experimenting I've found that it is useful to look at the script results right after making a change just to see if your modifications were recognized by the system and get the early returns from whether things were improved or not -- but, to get a truly accurate reading from the script you should check back in 24-48 hours after rebooting mysql (this is actually noted at the top of the script itself, but it doesn't really explain why) depending on your site traffic. Also, I've found that the way I've got Drupal set up it is particularly demanding in the tmp_table_size and table_cache areas (e.g., you may want to bump up the number for both of these areas in the settings above)

Also you could use [Releem MySQLConfigurer](https://github.com/initlabopen/mysqlconfigurer) for fully automated preparing MySQL performance optimized configuration. 

If you'd like to read up on more about mySQL tuning I suggest taking a look at these resources:

[MySQL variables](https://dev.mysql.com/doc/refman/5.0/en/server-system-variables.html)  
[Awesome Mysql Performance](https://github.com/Releem/awesome-mysql-performance) - A curated list of awesome links related to MySQL/MariaDB/Percona performance tuning.
