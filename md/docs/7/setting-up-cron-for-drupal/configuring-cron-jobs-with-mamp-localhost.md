---
title: "Configuring cron jobs with MAMP localhost"
source_url: "https://www.drupal.org/docs/7/setting-up-cron-for-drupal/configuring-cron-jobs-with-mamp-localhost"
page_type: page
last_updated: "Last updated on 5 August 2016"
published: "2009-04-15T15:10:21+00:00"
modified: "2016-08-05T14:28:27+00:00"
breadcrumb: ["Drupal 7", "Setting up cron for Drupal 7"]
fetched: "2026-10-21T06:24:57Z"
raw: "raw/docs/7/setting-up-cron-for-drupal/configuring-cron-jobs-with-mamp-localhost.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Configuring cron jobs with MAMP localhost

These are instructions for setting up a cron job on your localhost using MAMP on a Mac.

1.  In Terminal type `crontab -e`. This allows you to add a cron job, using the vim editor.
2.  Press `i` on your keyboard to go into vim's insert mode.
3.  Type in you cron command. For example, to run at minute 5 of every hour using curl, use:  
    `5 * * * * /usr/bin/curl --silent --compressed http://localhost:8888/cron.php`  
    But to run every 5 minutes, use:  
    `*/5 * * * * /usr/bin/curl --silent --compressed http://localhost:8888/cron.php`  
    Note that if you are not using MAMP's default 8888 port, you should leave that off.
4.  While in insert mode you can use the arrows and delete keys as you would normally.
5.  Press escape key to exit vim's insert mode.
6.  Type `ZZ` (Must be capital letters -- saves the file and exits crontab).
7.  Verify the cron job details by typing `crontab -l` (that's a lower case L) at the terminal prompt.

I recommend that you first try setting the job to run every 2 minutes (with \*/2), so that you can check, reasonably quickly, that it is running. Then edit crontab again and change the curl command to your preferred time.

### Non-Vim alternative

For those with a reservation against Vim (or any other command-line editor), you can do it like this:  
- Create a document with your editor of choice.  
- Add the cronjobs you want to add, like described above.  
- Save the file as "mycron.txt" on your desktop (or any other place you like).  
- Open up a Terminal window, and go to the desktop ( `cd ~/Desktop` ).  
- Type in `crontab mycron.txt`  
- Type in `crontab -l` to verify that your commands were added to cron.  
Note: This method will overwrite the entire crontab, so keep the mycron.txt file available. When you need to add or change cronjobs, just edit that file and repeat the `crontab mycron.txt` command to update your cronjobs.
