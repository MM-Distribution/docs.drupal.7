---
title: "Randomizing MySQL Users For Exceeded max_questions Error"
source_url: "https://www.drupal.org/docs/7/managing-site-performance/randomizing-mysql-users-for-exceeded-max_questions-error"
page_type: page
last_updated: "Last updated on 16 August 2016"
published: "2014-08-18T15:18:23+00:00"
modified: "2016-08-16T20:24:53+00:00"
breadcrumb: ["Drupal 7", "Managing Drupal 7 site performance and scalability"]
fetched: "2026-10-21T07:01:00Z"
raw: "raw/docs/7/managing-site-performance/randomizing-mysql-users-for-exceeded-max_questions-error.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Randomizing MySQL Users For Exceeded max_questions Error

Sometimes malicious HTTP GET requests can take down your site, by bootstrapping Drupal so frequently that you can *exceed a [MySQL max_user_connections limit](http://dev.mysql.com/doc/refman/5.0/en/server-system-variables.html#sysvar_max_user_connections) of even 480000!*  
(The default setting for MySQL max_user_connections is generally 360000)

When checking the site status with [drush status](https://github.com/drush-ops/drush), you may get a message like:

> User "username" has exceeded the max_questions resource (current value: 360000) \[warning\]

**This code is not intended for basic MySQL max_user_connections errors; it is specifically for situations where you have tried everything else, and you are getting slammed by malicious requests. Also, this is not recommended for dealing with normal high traffic issues; to deal with normal traffic that exceeds your site's capabilities, consider using a CDN ([Content Delivery Network](http://en.wikipedia.org/wiki/Content_delivery_network)), a HTTP accelerator like [Varnish](https://github.com/varnish/Varnish-Cache), or multiple site instances behind a load balancer.**

The Drupal 6 site where this solution was tested is optimized with the [Boost module](https://www.drupal.org/project/boost), and also served by the [CloudFlare CDN](https://www.cloudflare.com/). Still, the site would go down with the "exceeded MySQL max_questions" error. And when the problem is with MySQL, CloudFlare does NOT serve a cached page. *Boost and CloudFlare are not required for this solution, but they help overall performance.*

Solution also tested on Drupal 7.

The solution is to randomize MySQL users, so that one does not exceed the max_user_connections limit.

## Steps:

1.  Create a few MySQL users named sequentially eg. username1, username2, username3, username4 (4 users should be sufficient; if not, add more)
2.  Set the same MySQL password on all the users
3.  Allow the users access to your database
4.  In the site's settings.php file section for database connection:

### Drupal 6

``` php
# randomize MySQL user number
$muser = mt_rand ( 1 , 4 );
$db_url = 'mysqli://username' . $muser . ':[password]@host/dbname';
```

### Drupal 7

``` php
# randomize MySQL user number
$muser = mt_rand ( 1 , 4 );
$databases['default']['default'] = array(
  'driver' => 'mysql',
  'database' => 'dbname',
  'username' => 'username' . $muser,
  'password' => 'password',
  'host' => 'host',
  'prefix' => '',
);
```

## Improvements:

### Rotating vs Randomizing?

The live test on a D6 site has been successful dealing with the problem.

It's possible using this solution that the **same MySQL user** will be returned randomly, and *still trigger an exceeded max_questions error*.

In that case, a method to step through the MySQL users sequentially, *rotating* vs *randomizing* could be an improvement.
