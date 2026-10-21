---
title: "Configuring cron jobs with DreamHost"
source_url: "https://www.drupal.org/docs/7/setting-up-cron-for-drupal/configuring-cron-jobs-with-dreamhost"
page_type: page
last_updated: "Last updated on 5 August 2016"
published: "2005-09-18T15:23:02+00:00"
modified: "2016-08-05T14:28:27+00:00"
breadcrumb: ["Drupal 7", "Setting up cron for Drupal 7"]
fetched: "2026-10-21T06:24:42Z"
raw: "raw/docs/7/setting-up-cron-for-drupal/configuring-cron-jobs-with-dreamhost.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Configuring cron jobs with DreamHost

On DreamHost you can configure cron jobs using either the web panel or the shell.

## Setting up cron jobs using the web panel

Visit <https://panel.dreamhost.com/index.cgi?tree=goodies.cron&>

Click 'Add a New Cron Job' and enter the following command:  
`curl --silent --compressed http://example.com/cron.php`

**Note: The above code is dependent on http being accessible. If you want to run a cron job on a password protect domain, use the include the following with the absolute path for your domain to cron.php instead of the example:**  
`/dh/cgi-system/php5.cgi /home/username/example.com/drupal/cron.php`

In the same interface, you should specify a title (such as 'Drupal Cron'), e-mail address for results (not recommended), and a run interval. If you have more than one Drupal site, you can add more than one command per cron job (one per line).

## Setting up cron jobs using the shell

*This information comes from the Dreamhost knowledge base.*

Via the "crontab" command from the shell.

**crontab -l** will show you your currently set up cron jobs on the server.  
**crontab -r** will delete your current cron jobs.  
**crontab -e** will allow you to add or edit your current cron jobs by using your default text editor to edit your "crontab file".

Your crontab includes all the cron jobs you'd like, with one cron entry per line. A cron entry looks like this:

45 2 \* \* \* curl --silent --compressed <http://example.com/cron.php>

Here are some examples to help you learn the syntax for the numbers:

You can also edit crontab on a local file. Upload it to a directory and run:

**crontab YourFileName**

It'll replace your crontab with what's on the text file, without having to edit it online. This is useful if you're using a telnet client which doesn't support ANSI control codes (such as the Windows' one) and can't understand what the heck is going on on the editors.

In my own experience, I found that only by entering one cron command per line worked (one line each for :10, :20, :30, etc.). I could not get crontab to take the "\*/15" argument, so I worked around it. Also, if you have ANY character after the last command (space, CR, whatever) the file will not take.

I like this file-load approach because I have a basic command file to edit or call up again if needed. Afterwards, running crontab -l will confirm that the job did take.
