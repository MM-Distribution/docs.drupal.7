---
title: "Step 5: troubleshooting"
source_url: "https://www.drupal.org/docs/7/multisite-drupal/step-5-troubleshooting"
page_type: page
last_updated: "Last updated on 30 August 2016"
published: "2014-03-24T10:57:46+00:00"
modified: "2016-08-30T13:47:16+00:00"
breadcrumb: ["Drupal 7", "Multisite Drupal 7"]
fetched: "2026-10-21T06:15:08Z"
raw: "raw/docs/7/multisite-drupal/step-5-troubleshooting.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Step 5: troubleshooting

## Clearing cache

**If** you got an error or a empty screen during the process, then modified something and want to try again, **then you may need to clear your browser cache** to check whether your new attempt is fruitful. For this,

- in Mozilla Firefox, go to Edit → Preferences → Privacy → "Clear your recent history"; in "Time range history", choose a duration at least as long as the time elapsed since your first modification; if unsure, choose "Everything". In "Details", check only "Cache", then click on "Clear now".
- In Chromium web browser, go to the wrench icon on the top right → Preferences → Under the bonnet → Privacy: Clear browsing data. In "Obliterate the following items from:" choose the duration (If unsure, choose "the beginning of time".), check only "Empty the cache" then click on "Clear browsing data".

## Checking Apache and PHP

You can rename your drupal7/index.php file (to save it) and replace it temporarily by a new index.php file containing only `<?php phpinfo(); ?>`. Then go with your browser to your site <http://example> . If you can see something like this:  
![ description of Apache, its modules and the system](/files/phpinfo_0.jpg)  
it proves that Apache and PHP work together and are serving the right first Drupal file (index.php).

## Blank page

If Apache and PHP works but you get **only** blank pages (often referred to "WSOD": "white screen of death"), it may be that the package php-pdo_mysql is not installed in your system: install it and restart Apache (httpd). In Mageia 3 or 4, you can go in "Mageia control center" → System → "Manage system services by enabling or disabling them", then "stop" and "start" httpd.  
Reference: [PDO](http://www.drupal.org/requirements/pdo "drupal.org")  
Note that getting only a blank page is a problem different from getting some blank pages inside a website.

It is often useful to navigate with your browser to the page example/update.php, as this may provide an error message.

There is a [section](http://www.drupal.org/node/201872 "drupal.org") of the reference book, about blank pages:

## Access denied

If you get an "access denied" error message, it may be that your Apache configuration doesn't allow the connection. You should have a directive `Require local granted` in your Apache configuration, for instance a paragraph

``` php
<Directory /usr/share/drupal/>
   Require local granted
</Directory>
```

in /etc/httpd/conf/sites.d/drupal.conf (in Mageia 4).

## No watchdog table

If you get an error message complaining the watchdog table doesn't exist, go in "modules", disable the watchdog module, click on "Save" (at the bottom of the page), enable it again and save again. If the problem persists or if you couldn't log in to disable this module, then go in PhpMyAdmin (<http://localhost/phpmyadmin>), choose your database ("company_example" in our example), in the horizontal menu, choose "SQL", and copy the following into the frame named "Run SQL query/queries on company_example:" ("company_example" standing for your database name).

``` php
--
-- Database: `company_example`
-- 
-- --------------------------------------------------------
--
-- Table structure for table `watchdog`
-- 
CREATE TABLE `watchdog` (
  `wid` int(11) NOT NULL auto_increment,
  `uid` int(11) NOT NULL default '0',
  `type` varchar(16) NOT NULL default '',
  `message` longtext NOT NULL,
  `variables` longtext NOT NULL,
  `severity` tinyint(3) unsigned NOT NULL default '0',
  `link` varchar(255) NOT NULL default '',
  `location` text NOT NULL,
  `referer` varchar(128) NOT NULL default '',
  `hostname` varchar(128) NOT NULL default '',
  `timestamp` int(11) NOT NULL default '0',
  PRIMARY KEY  (`wid`),
  KEY `type` (`type`)
) DEFAULT CHARSET=utf8;
```

replacing "company_example" by your database name. Then click on "Go". This will create the lacking database. Reference: old [bug 429188](https://drupal.org/node/429188 "Drupal.org") and [bug 1784548](https://drupal.org/node/1784548 "Drupal.org").

## Reference

There is a [chapter](https://www.drupal.org/troubleshooting "drupal.org") of the documentation about troubleshooting.
