---
title: "Copying your test site to your live site (command line)"
source_url: "https://www.drupal.org/docs/7/upgrade-to-drupal-7/copying-your-test-site-to-your-live-site-command-line"
page_type: page
last_updated: "Last updated on 18 August 2016"
published: "2005-11-09T20:04:51+00:00"
modified: "2016-08-18T20:23:56+00:00"
breadcrumb: ["Drupal 7", "Upgrade to Drupal 7"]
fetched: "2026-10-21T06:21:05Z"
raw: "raw/docs/7/upgrade-to-drupal-7/copying-your-test-site-to-your-live-site-command-line.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Copying your test site to your live site (command line)

*TIP: Make sure your test site is a recent copy of your live site, otherwise you will lose changes. It might be a good idea to create a new test site if it has been a while.*

**I. Backup Your Drupal Files**  
Copy the contents of your live site directory to a 'backup' directory, in case something goes wrong.

`cp live_site/.htaccess backup/.`

Make sure the .htaccess file gets copied to the 'backup' directory as well.

Once you have copied your test site to your live site and are using your test database as your live database, *make sure that you create a new test copy of your live database when you create a new test site!*

***Do not use your live database with your test site or you risk corrupting and losing your live data!***

**II. Copy your test site files to your live site directory**

1.  Delete all your live site files with the Unix 'rm' command. **You made a backup, right?**

2.  Copy the contents of your test site directory to your live site directory

    `cp test_site/.htaccess live_site/.`

Make sure the .htaccess file gets copied to the test_site directory as well.

**III. Change settings.php in your live site Drupal files**  
Open and edit the file located under live_site/sites/default/settings.php with a plain text editor such as [jEdit](http://www.jedit.org/). Follow the directions in the file and modify this setting:

`$base_url = 'http://www.example.com/';`

*(This is the address of your live site directory. This tells Drupal where to look for the Drupal files to connect with.)*

There is no need to change the database settings. Just take note that *your test site database is now being used as the live site database.*

**IV. Check if your live site works**  
Navigate to <http://www.example.com/> and you should see your newly upgraded live site.
