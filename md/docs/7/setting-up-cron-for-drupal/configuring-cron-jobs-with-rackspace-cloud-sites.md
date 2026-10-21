---
title: "Configuring cron jobs with Rackspace Cloud Sites"
source_url: "https://www.drupal.org/docs/7/setting-up-cron-for-drupal/configuring-cron-jobs-with-rackspace-cloud-sites"
page_type: page
last_updated: "Last updated on 5 August 2016"
published: "2009-09-01T16:09:53+00:00"
modified: "2016-08-05T14:28:27+00:00"
breadcrumb: ["Drupal 7", "Setting up cron for Drupal 7"]
fetched: "2026-10-21T06:25:59Z"
raw: "raw/docs/7/setting-up-cron-for-drupal/configuring-cron-jobs-with-rackspace-cloud-sites.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Configuring cron jobs with Rackspace Cloud Sites

Setting up a cron job on Rackspace Cloud Sites is a straight forward process and can be set up any number of ways.

1.  **Log in** to your Rackspace Cloud account.
2.  **Select the domain** you want to update.
3.  Click on the **Features** tab.
4.  Scroll down to the cron job list. Click on **add new task**.
5.  Enter a **task name**. *NOTE:* The task name can be anything.
6.  *(Optional)* If you would would like to receive a notification e-mail when the cron is complete, check **Send me an email** and enter the e-mail address you would like the cron system to notify. The e-mail contains the results of the cron job and can be useful for debugging but can be annoying if you receive one for a simple cron task.
7.  For Command Language, select **http**.
8.  For Command to Run, enter the URL of the cron.php file in your Drupal installation. For example, you would enter:
    - **Drupal 6**  
      *<http://www.example.com/cron.php>*
    - **Drupal 7**  
        
      *  
      1) Choose to enter your email if you want to get a notification  
      2) Choose the command language: PHP  
      3) Type the command to run "web/content/cron.php". Note need to specify the "Document" folder*
9.  Select the **Repeat by the:** drop down and select the interval to run the task. Generally, it is recommended to run the maintenance cron task once an hour. In the drop down, select **hour** and then choose the frequency and the minute (0 - 59).
10. Click on **Save Task**.
11. You're done!

Explanation for Drupal 7. The PHP interpreter is being called directly from the directory where it is installed. Since the call source is local, no key is needed. However you have to go and modify the cron.php file, to tell it where to find "bootstrap.php"; see the illustration below.  
![location of bootstrap.php](/files/bootstrap_dot_php_dir_0.jpg)  
The function call "getcwd()" in cron.php does not resolve to the "Document" folder, but 2 folders above that. So cron.php will be looking for bootstrap.php in the wrong folder. You need to add "/[www.youdomainname.com/web/content](http://www.youdomainname.com/web/content)" to the return string of "getcwd()".
