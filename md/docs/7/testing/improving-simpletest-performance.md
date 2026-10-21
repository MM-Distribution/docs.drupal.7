---
title: "Improving SimpleTest performance"
source_url: "https://www.drupal.org/docs/7/testing/improving-simpletest-performance"
page_type: page
last_updated: "Last updated on 30 November 2016"
published: "2009-05-19T13:59:49+00:00"
modified: "2016-11-30T13:07:52+00:00"
breadcrumb: ["Drupal 7", "Automated testing for Drupal 7"]
fetched: "2026-10-21T08:11:22Z"
raw: "raw/docs/7/testing/improving-simpletest-performance.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Improving SimpleTest performance

- **Tweak MySQL configuration**  
  InnoDB, while recommended for production systems, is not ideal on a test slave because DDL operations (CREATE TABLE / DROP TABLE) tend to be much slower than MyISAM's.
- **Move MySQL database to tmpfs**  
  The test slave will stress the database server by issuing a lot of heavy queries (especially DDL queries) in a short period of time. After some of those queries, the database server explicitly flushes data to disk (MySQL tries to avoid that when possible, but it still calls `fsync()` after a DDL operation). Moving the database files to a tmpfs filesystem makes a lot of difference.
- **Tweak PostgreSQL configuration**  
  By default, the PostgreSQL server will try to make sure that updates are physically written to disk, by issuing `fsync()` system calls or various equivalent methods. This causes heavy I/O during testing.
- **Place SQLite database in memory**  
  By keeping the SQLite database in memory, most of the disk I/O is avoided speeding up the entire process. Note that this means the database must be recreated after rebooting the computer.
- **Use a minimal install profile**  
  Most DrupalWebTestCases bootstrap a 'default' install profile to run tests on, this involves enabling a dozen core modules that may not be necessary for your tests. *If you understand the implications* then you may speed startup time a lot by just using the 'minimal' install profile.

#### Tweak MySQL configuration

Add the following to your `my.cnf`:

``` php
skip-innodb
```

Its important to place this setting under the group \[mysqld\], otherwise it will not work.

#### Moving MySQL database to tmpfs

Tmpfs is a linux pseudo-filesystem that stores files and directory in memory. Files placed on a tmpfs will be lost after a reboot, but it doesn't matter for a test slave.

To move the test database to tmpfs, add the following line to your `/etc/fstab`:

``` php
tmpfs /var/lib/mysql/drupal_checkout tmpfs rw,nosuid,nodev,noexec,uid=<uid of the mysql user>,gid=<gid of the mysql group> 0 0
```

`<uid of the mysql user>` and `<gid of the mysql group>` can be found in `/etc/passwd` and `/etc/groups`, respectively.

#### Tweak PostgreSQL configuration

To stop postgresql from writing to disk on each change, place `fsync = off` in `postgresql.conf`. Note that this can cause serious data loss in case of a crash, so use this with care on a testing database server, and NEVER on a production database.

#### Place SQLite database in memory

To place the sqlite database entirely in memory, on Linux you can choose a file inside `/dev/shm` as the database path.

#### Use a minimal install profile

Placing this code inside your class definition will mean that many modules are skipped.

``` php
class MyLightweightTest extends DrupalWebTestCase {
  // Don't need most of default core modules.
  protected $profile = 'minimal';
```

Of course, this means that you will not have the default 'page' content type available, and you should now manually enable any other modules you need to setup, but on the other hand, each test bootstrap may be a few seconds faster at the beginning. [In testing (see attached)](https://www.drupal.org/files/bootstrap_speed.test), this optimisation reduced a simple do-nothing test case from 13 seconds to 6 seconds.
