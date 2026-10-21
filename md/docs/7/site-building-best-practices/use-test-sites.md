---
title: "Use test sites"
source_url: "https://www.drupal.org/docs/7/site-building-best-practices/use-test-sites"
page_type: page
last_updated: "Last updated on 17 August 2016"
published: "2005-05-07T22:32:18+00:00"
modified: "2016-08-17T08:49:39+00:00"
breadcrumb: ["Drupal 7", "Drupal 7 site building best practices"]
fetched: "2026-10-21T07:11:36Z"
raw: "raw/docs/7/site-building-best-practices/use-test-sites.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Use test sites

There are many programs (XAMPP, MAMP, Apache2Triad) that help you setup a local test system easily. You should set one up to play with your site and to test backups and restores of your production site. Set up a test site using a copy of your live data. You do not want to have to ask in the forums how to save your site. You have worked hard to build it, it would be a shame to lose it.

- *Never* do development or testing on your live production site. Drupal is fast and easy to install. Always test on a test site first.
- Test that your backups work and that you know how to do a restore of your site. The test system can be your local desktop if you wish. You do not want to discover the hard way that you forgot a file or did not know how to do this when your site is down.
- Test your site upgrade procedure before risking your live site and document the steps you take. Documentation aids repeating the process if necessary. Testing can be done with [Simpletest](/simpletest).

For more information on installing test sites, please see the [setting up a development environment](http://drupal.org/node/147786) and [getting started sections](/getting-started/). There are some specific examples of copying a production site to a test/development environment in the [Special cases](http://drupal.org/node/21875) subsection under Installation.
