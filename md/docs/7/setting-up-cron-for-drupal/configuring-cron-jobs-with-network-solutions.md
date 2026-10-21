---
title: "Configuring cron jobs with Network Solutions"
source_url: "https://www.drupal.org/docs/7/setting-up-cron-for-drupal/configuring-cron-jobs-with-network-solutions"
page_type: page
last_updated: "Last updated on 5 August 2016"
published: "2011-04-12T11:45:17+00:00"
modified: "2016-08-05T14:28:27+00:00"
breadcrumb: ["Drupal 7", "Setting up cron for Drupal 7"]
fetched: "2026-10-21T06:25:43Z"
raw: "raw/docs/7/setting-up-cron-for-drupal/configuring-cron-jobs-with-network-solutions.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Configuring cron jobs with Network Solutions

[Network Solutions](http://networksolutions.com) , has a unique and complicated setup that tends to cause problems and confusion for Drupal developers. Setting up a cron job is one task that leads to confusion, but it is possible. Here's how, based on this comment:  
<http://drupal.org/node/145723#comment-1569234>

To run the cron job on Network Solutions:  
1. log into you account

2\. Go to the "Webhosting" tab  
then to the "Configurations" tab  
then to "Scheduled Tasks" tab

3\. Click on "Add a task" and in the "Program file:" field put in:  
wget -O - <http://www.Your_domain_name/cron.php>

4\. Set it up to run every hour and click "Save".
