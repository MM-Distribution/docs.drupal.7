---
title: "Configuring cron jobs with Media Temple Grid (gs) and DV servers"
source_url: "https://www.drupal.org/docs/7/setting-up-cron-for-drupal/configuring-cron-jobs-with-media-temple-grid-gs-and-dv-servers"
page_type: page
last_updated: "Last updated on 5 August 2016"
published: "2007-07-14T16:12:16+00:00"
modified: "2016-08-05T14:28:27+00:00"
breadcrumb: ["Drupal 7", "Setting up cron for Drupal 7"]
fetched: "2026-10-21T06:25:28Z"
raw: "raw/docs/7/setting-up-cron-for-drupal/configuring-cron-jobs-with-media-temple-grid-gs-and-dv-servers.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Configuring cron jobs with Media Temple Grid (gs) and DV servers

Through my experience and to my knowledge, cron jobs on Media Temple's Grid Servers must be run via an .sh file in the "/scripts" directory of your Drupal installation. This was confusing to me as I've always setup cron jobs in cPanel. Media Temple does not use cPanel. Following the steps to setup a cron job like `45 * * * * /usr/bin/wget -O - -q http://www.example.com/cron.php` through a typical cPanel interface will not work in Media Temple's cron job creation tool.

#### Use the following steps to get cron jobs working on a Media Temple Grid Server:

1.  Log into your **(mt) AccountCenter** and go to your **WebControl** panel.
2.  Click on the "**Cron Jobs**" icon to enter the cron configuration page.
3.  Select the "**Add a new cron job**" button.
4.  Enter an email address for the "**Output email**". ***Note**:Leave this blank if you don't want constant emails.*
5.  Enter the following in the "**command to run**" text box:  
    `curl http://www.example.com/cron.php`  
    *where "example.com" is your domain name.*
6.  Under "**Scheduling Settings**" select how often you want your cron job to run.
7.  Note the Media Temple will not allow a cron job to run more often than "every 5 minutes".
    - To setup a cron job to run once an hour:
      - Under the "minutes" entry, specify the minute value on which the cron job will start each hour.
      - Then select the following radio boxes: hour, day, month, day of the week.

![Screenshot](/files/Parallels_Plesk_Panel_11_5_30_and_Configuring_cron_jobs_on_Media_Temple_Grid__gs__and_DV_servers___Drupal_org-28.png)

## Setup Cron Jobs on Mediatemple DV Server on Drupal 7

We want cron to run every 10 minutes, but Drupal's cron only allows for 1 hour granularity.

1.  In the Drupal admin Go to Report \> Status Report
2.  Copy your unique cron key url from the cron maintenance tasks section.
3.  In Mediatemple's plesk, open Websites & Domains \> Scheduled Tasks \> click your username \> click Schedule New Task and enter this info:

Minute: \*/10  
Hour: \*  
Day of Month: \*  
Month: \*  
day of Week: \*  
Command: curl [http://yourdomain.com/cron.php?cron_key=1Vulq8M6-xW4cG0F8ewU5PeckY39_MW6...](http://yourdomain.com/cron.php?cron_key=1Vulq8M6-xW4cG0F8ewU5PeckY39_MW6pTi4f0x_NMo)  
For the command field I used "curl" and the url I copied in step 2.

#### Note about Chroot

If your FTP accounts are chrooted then cron will not run because curl command cannot run in the chrooted environment. In order to allow curl to run try these steps:

1.  SSH into your server as root or equivalent user.
2.  Run this command
3.  If you ever need to undo this setting (but it will stop cron from running again):

Reference on chroot and curl command: <http://kb.parallels.com/en/115889>

#### To Turn off cron email alerts:

Login to Plesk, go to Home \> Subscriptions \> domain.com \> Websites & Domains \> Scheduled Tasks \> Settings
