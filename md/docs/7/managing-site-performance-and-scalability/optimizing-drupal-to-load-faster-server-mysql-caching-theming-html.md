---
title: "Optimizing Drupal to load faster (Server, MySQL, caching, theming, HTML)"
source_url: "https://www.drupal.org/docs/7/managing-site-performance-and-scalability/optimizing-drupal-to-load-faster-server-mysql-caching-theming-html"
page_type: page
last_updated: "Last updated on 26 November 2023"
published: "2012-08-10T12:51:58+00:00"
modified: "2023-11-26T12:57:17+00:00"
breadcrumb: ["Drupal 7", "Managing Drupal 7 site performance and scalability"]
fetched: "2026-10-21T07:00:30Z"
raw: "raw/docs/7/managing-site-performance-and-scalability/optimizing-drupal-to-load-faster-server-mysql-caching-theming-html.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Optimizing Drupal to load faster (Server, MySQL, caching, theming, HTML)

### Basic settings

1.  Configure cron job (for Drupal 6 <http://drupal.org/project/poormanscron>)
2.  Make sure all cache tables are clearing properly especially cache_form
3.  Enable cache options on the performance page
4.  (For Drupal 6, <http://drupal.org/project/advagg> )

### Theme optimization

1.  Manually Remove blankspaces and comments from .tpl
2.  No indentation in .tpl
3.  Turn on CSS and JS aggregation in the performance page
4.  Manually reduce css file size by removing duplicate and combine similar together
5.  Move codes to functions that should be in a custom common module. Use functions for similar problems instead of coding separately. Refer core API

### Coding standard and proper use of already existing core API

1.  <http://drupal.org/coding-standards>
2.  <https://drupalize.me/videos/understanding-drupal-coding-standards?p=2012>

### Secure codes

1.  <http://drupal.org/writing-secure-code>

### DB Query optimization in codes

1.  Join db queries whenever possible
2.  For Db update and insert, use core API
3.  Use drupal standard <http://drupal.org/coding-standards>

### DB table optimization

1.  <http://drupal.org/project/db_maintenance>

### Disable unnecessary modules

1.  Devel
2.  Statistics
3.  Update status
4.  Use syslog instead of Database logging

### Remove unnecessary contents and others

### Cache modules

1.  Make use of object caches to reduce database overhead, e.g. [Memcache](https://www.drupal.org/project/memcache), [Redis](https://www.drupal.org/project/redis) or [APC](https://www.drupal.org/project/apc)
2.  <https://drupal.org/project/authcache>
3.  Some module may help improve  
    <http://drupal.org/project/ajaxblocks> (not available with Drupal 8 & 9 )

### Make changes according to Google Pagespeed and yahoo YSlow suggestions

### MySQL Settings

1.  Cache Size say 32MB in MySQL
2.  Use <https://github.com/initlabopen/mysqlconfigurer> for fully automated MySQL performance tuning

### Apache settings

1.  DNS lookup : OFF
2.  Set FollowSymLinks everywhere and never set SymLinksIfOwnerMatch
3.  Avoid content negotiation. Or use type-map files rather than Options MultiViews directive
4.  KeepAlive on, and KeepAliveTimeout very low (1 or 2 sec)
5.  Disable or comment access.log settings
6.  Enable mod_deflate or mod_gzip
7.  Install APC server with higher memory limit apc.shm_size = 64

### Also, we can check these options :

### 1) Turn Page Caching On

What page caching does is that instead of using a bunch of database queries to get the data used in making a typical web page, the rendered contents of the web page are stored in a separate database cache table so that it can be recalled quicker. If you have 10 people visiting the site from different computers, Drupal first looks into the database cache table to see if the page is there, if it is, it just gives them the page. Think of saving the output of 50 separate queries so that is accessible with a single query. You obviously are reducing the SQL queries required by a lot. What the page cache table actually stores is HTML content.

Page Caching is that it only works to optimize the page load time for Anonymous users. This is because when you are logged in, you might have blocks that show up on the page that are customized for you, if it served everybody on the same page, they would see your customized information (think of a My Recent Posts block), so Drupal does not use the Page Cache for Authenticated users automatically. This allows you to turn Page Caching on and still get the benefit of Anonymous user page load times but does not break the site for Authenticated users. There are other caching options that will help with Authenticated user page performance, we will talk about those later.

To enable Page Caching, you go to Configuration \| Development and select the checkbox next to "Cache pages for anonymous users".

### 2) Turn Views caching on

As mentioned when talking about Page Caching only working for anonymous users above, there are other caching options for helping with Authenticated user page performance. One of those options is to turn on caching for blocks and pages that you create using the Views module. This allows you to cache the output of the query used to generate the view, or the end HTML output of your View, and you can tune the cache for them separately. And realize too that this means you can cache portions of a page if you are using one or several Views blocks in the page, it will just cache that block in the page, not the whole page.

See more (Drupal7) @ [https://www.lullabot.com/articles/a-beginners-guide-to-caching-data-in-d...](https://www.lullabot.com/articles/a-beginners-guide-to-caching-data-in-drupal-7)
