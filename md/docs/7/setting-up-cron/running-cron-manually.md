---
title: "Running cron manually"
source_url: "https://www.drupal.org/docs/7/setting-up-cron/running-cron-manually"
page_type: page
last_updated: "Last updated on 5 August 2016"
published: "2007-07-12T20:45:35+00:00"
modified: "2016-08-05T14:59:34+00:00"
breadcrumb: ["Drupal 7", "Setting up cron for Drupal 7"]
fetched: "2026-10-21T06:23:39Z"
raw: "raw/docs/7/setting-up-cron/running-cron-manually.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Running cron manually

#### To run cron manually in Drupal 7

Go to *Administration \> Reports \> Status report*. Scroll down to "Cron maintenance tasks" and click "run cron manually" at <http://example.com/admin/reports/status/run-cron>

In that same section, core also provides a link with a unique cron_key to run cron from outside your site.

#### To run cron manually in Drupal 5 and 6

To run a cron job manually, simply visit your own site's url at <http://example.com/cron.php> with your web browser, and cron will run and complete in the background. You'll be left with a blank white page, which is normal. Use the browser's back button to return to the previous page and continue where you left off. It doesn't matter how long you wait while you're seeing the blank white page, and returning to the previous page at any time won't stop the cron process from running.

Core provides a convenience link for running cron manually too. Look at the Status page's link: /admin/logs/status/run-cron?destination=admin%2Flogs%2Fstatus. You can paste that into your own site's address bar any time you want to run a cron.

In addition, if you have the [update_status.module](/project/update_status) installed, and you should since it's simply glorious, you'll be presented with a custom link on your admin/logs/updates page.

For Drupal 6.x, see in your site: *Administer \> Reports \> Status report \> Cron maintenance tasks \> Run cron manually*.
