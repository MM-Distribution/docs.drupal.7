---
title: "Reports"
source_url: "https://www.drupal.org/docs/7/monitoring-a-site/reports"
page_type: page
last_updated: "Last updated on 18 August 2016"
published: "2008-04-25T06:47:34+00:00"
modified: "2016-08-18T16:43:49+00:00"
breadcrumb: ["Drupal 7", "Monitoring a Drupal 7 site"]
fetched: "2026-10-21T07:05:09Z"
raw: "raw/docs/7/monitoring-a-site/reports.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Reports

View reports from system logs and other status information.

- [Recent log entries](http://drupal.org/documentation/modules/watchdog)
- Top 'access denied' errors
- Top 'page not found' errors
- Available updates
- Status Report
- [Site statistics](http://drupal.org/documentation/modules/statistics)

### Recent log entries

The dblog module monitors your website, capturing system events in a log to be reviewed by an authorized individual at a later time. The dblog log is simply a list of recorded events containing usage data, performance data, errors, warnings and operational information. It is vital to check the dblog report on a regular basis as it is often the only way to tell what is going on.

### Top 'access denied' errors

Will show messages where page access was denied.

### Top 'page not found' errors

Will show log messages where requested pages were not found.

### Available updates

Here you can find information about available updates for your installed modules and themes, including whether or not they are security releases. Note that each module or theme is part of a "project", which may or may not have the same name, and might include multiple modules or themes within it.

To extend the functionality or to change the look of your site, a number of contributed modules and themes are available. If you are not running cron.php regularly you can run the check manually.

![](/files/08-available_updates_sm.jpg)

### Status report

Here you can find a short overview of your site's parameters as well as any problems detected with your installation. It may be useful to copy and paste this information into support requests filed on drupal.org's support forums and project issue queues.

![](/files/10-status_report_sm.jpg)
