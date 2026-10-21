---
title: "Troubleshooting cron"
source_url: "https://www.drupal.org/docs/7/setting-up-cron/troubleshooting-cron"
page_type: page
last_updated: "Last updated on 5 March 2019"
published: "2009-08-19T10:55:07+00:00"
modified: "2019-03-05T16:39:49+00:00"
breadcrumb: ["Drupal 7", "Setting up cron for Drupal 7"]
fetched: "2026-10-21T06:24:11Z"
raw: "raw/docs/7/setting-up-cron/troubleshooting-cron.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Troubleshooting cron

Various things can keep cron from doing its job on your Drupal site. If your Status report (`admin/reports/status`) indicates that cron hasn't run recently, try the following to diagnose and fix the problem:

## There is a module for that!

Before resorting to code or sql magic, try <https://www.drupal.org/project/cron_debug>

## Make sure cron.php is being called at all

If your Status report indicates that cron has *never* run, you may simply need to configure [configure a cron job](http://drupal.org/cron "Configuring cron jobs"). If you can successfully run cron manually from your Status report screen, [Admin menu](http://drupal.org/project/admin_menu), or [Drush](http://drupal.org/project/drush), this is almost certainly the case. If manually running cron fails, you have a deeper problem...

## Understand how update.modules permission interacts with cron.php

In 6x, update.modules became part of core. By default, user 1 has permission to run update.module. To expand that permission, you need to grant the user permission to "administer site configurations." You can test this behavior by running cron.php logged out versus logged in as admin. You may find that cron.php is performing correctly even if does not update modules -- check the permissions to see if that is true.

## Check for problems with cron itself

If cron hangs, redirects, returns a 404 error, or just plain fails when run manually, you have a problem with cron itself.

- Cron may be cached badly. Clear your site caches from `admin/settings/performance`, [Admin menu](http://drupal.org/project/admin_menu), or [Drush](http://drupal.org/project/drush), or truncate (empty) all database tables with names beginning with `cache_`. You could also search for cached instances of cron. To truncate tables using phpMyAdmin, go to the table of interest (beginning with `cache_`) and select the Operations tab. Click the red Empty the Table (Truncate) in the lower right. If you don't want to do this manually for each `cache_` table, you can run:  

  ``` php
  TRUNCATE TABLE cache_[table-name];
  TRUNCATE TABLE cache_[table-name];
  ```

  etc for each `cache_` table you have. The number and names of `cache_` tables will depend on your website setup.

  To return return the 'TRUNCATE TABLE' command for all the 'cache\_' tables in your database use the following query:

  ``` php
  SELECT Concat('TRUNCATE TABLE ', TABLE_SCHEMA, '.', TABLE_NAME,';') FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE='BASE TABLE' AND TABLE_NAME like 'cache_%'
  ```

- Cron may have been interrupted during execution, such as by a server restart. This can result in watchdog (error) messages like "Attempting to re-run cron while it is already running" and "Cron has been running for more than an hour and is most likely stuck". Try resetting the semaphore and deleting the "last run" timestamp from the database. (Note: deleting the "last run" timestamp will cause your Status report to indicate that cron has never run.) You can do so with this SQL...  

  ``` php
  USE Name_Of_Your_Drupal_Database;
  DELETE FROM variable WHERE name="cron_semaphore";
  DELETE FROM variable WHERE name="cron_last";
  ```

  ...or with this PHP in a custom module or script (Drupal7):

  ``` php
  variable_del('cron_semaphore');
  variable_del('cron_last');
  ```

  ... or with drush (Drupal7):

  ``` php
  drush vdel cron_semaphore
  drush vdel cron_last
  drush sqlq "DELETE FROM semaphore WHERE name = 'cron';"
  ```

  ... For drush with Drupal8:

  ``` php
  drush php-eval "\Drupal::lock()->release('cron');"
  ```

  Or with a tiny module: <http://drupal.org/project/semiclean>.  
  If you delete these items from the variable table and still receive the "Attempting to re-run cron while it is already running" error it is probably because those variable values are cached. Follow the instructions above the clear the cache tables and this will likely solve the problem.

- Cron may be taking too long to complete, resulting in [WSOD](http://drupal.org/node/482956) or in watchdog (error) messages like "Cron run exceeded the time limit and was aborted". All cron jobs of all modules combined should not exceed the 240s timeout limit. This is especially common on sites that have been online for some time where database tables cron is attempting to clean up have become unmanageably large. Check the size of the `watchdog`, `sessions`, and `accesslog` tables and truncate (empty) them if necessary. Check max_execution_time in php.ini.

- A cron process with too much to do may also easily run out of memory, resulting in PHP error messages like "PHP Fatal error: Allowed memory size of X bytes exhausted (tried to allocate Y bytes) in file on line *x*". Try [increasing PHP's memory limit](http://drupal.org/node/76156 " Allowed memory size of X bytes exhausted (tried to allocate Y bytes)...").

- Semaphore expires value is very old. If clearing cache, truncating watchdog, sessions, and accesslog tables, and deleting cron_semaphore and cron_last from the variables table don't resolve your cron issues, check the expire value in the semaphore table:  
  `select * from semaphore`  
  If the expire value is old ([convert from unix timestamp to human time](http://www.onlineconversion.com/unix_time.htm)) try clearing the semaphore table:  
  `delete from semaphore;`  
  and then see if you can run cron.

### Check for problems with modules

Certain modules may cause cron to abort, redirect, or return a 404 error. To find an offending module, first find out which ones implement [`hook_cron`](http://api.drupal.org/api/function/hook_cron). Print a list using this code:

``` php
echo theme('item_list', module_implements('cron'));
```

Disable the modules, one by one, running cron after each one. (At least) the last module you disabled before it starts working again was causing a problem.

The Core search module is frequently the source of problems because of errors in nodes it's trying to index. Cron may choke on the following things in your content:

- Invalid PHP code
- Non-ASCII characters
- [`drupal_goto`](http://api.drupal.org/api/function/drupal_goto) (See [\#102138: cron breaks on drupal_goto](/project/drupal/issues/102138 "Status: Closed (works as designed)").)

If you know cron is failing during search indexing and you suspect bad content to be to blame, you can use the following SQL to see which nodes haven't been indexed yet—chances are it's choking on one of them.

``` php
SELECT *
FROM node n
LEFT JOIN search_dataset d
  ON d.type = 'node'
  AND d.sid = n.nid
WHERE
  n.status = 1
  AND n.type IN ('blog', 'page')
  AND (d.sid IS NULL OR d.reindex > 0)
```

### Advanced debugging

Debugging option: go into the module.inc and edit the module_invoke_all function so it looks like this:

``` php
  foreach (module_implements($hook) as $module) {
    $function = $module .'_'. $hook;
    if ($hook=='cron'){
        echo "$module  <br />";
     }
```

That will give you an idea of exactly which cron implementation it's hanging up at, then you can just revert the changes in module.inc when you are done troubleshooting.

#### Debugging with Drush:

``` php
find sites/all/modules/ -type f -regex ".*\.\(module\|inc\)" -print | xargs grep "function.*_cron"
drush dis -y <module>
drush cron
```

Repeat as necessary.

You can also run the cron from Drush, and turn on debugging mode to see real-time status of the actions as they are being executed. To do so, run `drush cron` commnd with `-d`option.

``` php
drush cron -d 
```

### Alternative cron modules

<https://drupal.org/project/EasyCron>, <http://drupal.org/project/elysia_cron>, <http://drupal.org/project/supercron> and <https://www.drupal.org/project/ultimate_cron> offer a more advanced cron which might provide a workaround for hard to solve cron problems.
