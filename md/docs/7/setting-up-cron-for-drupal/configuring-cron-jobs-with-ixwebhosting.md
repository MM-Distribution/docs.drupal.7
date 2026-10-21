---
title: "Configuring cron jobs with ixWebHosting"
source_url: "https://www.drupal.org/docs/7/setting-up-cron-for-drupal/configuring-cron-jobs-with-ixwebhosting"
page_type: page
last_updated: "Last updated on 5 August 2016"
published: "2009-01-20T23:22:19+00:00"
modified: "2016-08-05T14:28:27+00:00"
breadcrumb: ["Drupal 7", "Setting up cron for Drupal 7"]
fetched: "2026-10-21T06:27:17Z"
raw: "raw/docs/7/setting-up-cron-for-drupal/configuring-cron-jobs-with-ixwebhosting.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Configuring cron jobs with ixWebHosting

Login to the control panel at <https://manage.ixwebhosting.com/index.php>

Click on "Manage" following this path: My Products \>\> Hosting Products \>\> Manage

This will take you to H-Sphere page. Click on "FTP Manager" under FTP.

You'll see one of the parameters as Crontab. The Value will be set to Off by default. Click on the Off button.(Note: If it's been set to On, click on Edit button)

This will take you to list of cron jobs(should be empty at first).  
Fill in the Mail-To field with an email address where you want cron run success/failure messages sent.  
The other fields are:  
TT- Opens up a help popup.  
Minute - Set to some number to run at every time at that hour.  
Hour - Set to "\*" to run every hour or say for example "8" to run at 8am in the morning.  
Day of month - Set to "\*" to run every day in the month.  
Month - Set to "\*" to run every month.  
Day of week - Set to "\*" to run every day of week.  
Command - This is the only tricky part. Copy paste command below replacing "example.com" with the actual site name.

/usr/bin/curl -o /dev/null <http://example.com/cron.php>

Delete - Can be checked to delete previously stored cron jobs.(will otherwise state "New")

That should be it. Click on "Submit Query" to save cron job. You can add multiple ones by filling in the last row which is always empty and cannot be deleted.

Hope this helps. If pictures help, I'll re-edit this post with some.
