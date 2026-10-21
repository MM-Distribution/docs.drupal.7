---
title: "Copy your test site to a live site (GUI)"
source_url: "https://www.drupal.org/docs/7/upgrade-to-drupal-7/copy-your-test-site-to-a-live-site-gui"
page_type: page
last_updated: "Last updated on 18 August 2016"
published: "2005-11-09T19:35:51+00:00"
modified: "2016-08-18T20:23:46+00:00"
breadcrumb: ["Drupal 7", "Upgrade to Drupal 7"]
fetched: "2026-10-21T06:20:49Z"
raw: "raw/docs/7/upgrade-to-drupal-7/copy-your-test-site-to-a-live-site-gui.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Copy your test site to a live site (GUI)

*TIP: Make sure your test site is a recent copy of your live site, otherwise you will lose changes. It might be a good idea to create a new test site if it has been a while.*

**I. Backup Your Test Site Files**  
Using an FTP client such as [SmartFTP](http://www.smartftp.com), download all your existing test site files to your hard drive. The especially important files to keep track of are [settings.php](http://cvs.drupal.org/viewcvs/drupal/drupal/sites/default/settings.php?only_with_tag=DRUPAL-4-7&view=markup), and [.htaccess](http://cvs.drupal.org/viewcvs/drupal/drupal/.htaccess?only_with_tag=DRUPAL-4-7&view=markup).

**II. Change settings.php in your test site Drupal files**  
Open and edit the file located under sites/default/settings.php (or includes/conf.php) with a plain text editor such as [jEdit](http://www.jedit.org/). Follow the directions in the file and modify this setting:

`$base_url = 'http://www.example.com/';`

*(This is the address where you will upload your live site directory. This tells Drupal where to look for the Drupal files to connect with.)*

There is no need to change the database settings. Just take note that *your test site database is now being used as the live site database.*

**III. Upload the test site Drupal files to your live site directory**  
Using an FTP client such as [SmartFTP](http://www.smartftp.com),

1.  Download all your live site files to a backup folder on your desktop.

2.  Delete all your live site files on your server. **You made a backup, right?**

3.  Upload all the test site files to the directory:  
    <http://www.example.com/>

    In FTP world this is usually seen as "public_html/" or "www/".

**IV. Check if your test site works**  
Navigate to <http://www.example.com/> and you should see your newly upgraded Drupal site.

## 

### Some more suggestions:

- .htaccess may need to be changed too

If you uncommented the following line in your .htaccess file in order to get rewrite rules to work properly with a subdirectory for your test site, you may need to re-comment it.

from:

``` php
# Modify the RewriteBase if you are using Drupal in a subdirectory and
# the rewrite rules are not working properly.
RewriteBase /drupal
```

to:

``` php
# Modify the RewriteBase if you are using Drupal in a subdirectory and
# the rewrite rules are not working properly.
# RewriteBase /drupal
```

Note:

Once you have copied your test site to your live site and are using your test database as your live database, make sure that you create a new test copy of your live database when you create a new test site!. Do not use your live database with your test site or you risk corrupting and losing your live data!
