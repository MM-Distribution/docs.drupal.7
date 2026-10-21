---
title: "Core tests"
source_url: "https://www.drupal.org/docs/7/testing/core-tests"
page_type: page
last_updated: "Last updated on 15 October 2016"
published: "2005-08-31T15:23:43+00:00"
modified: "2016-10-15T21:58:40+00:00"
breadcrumb: ["Drupal 7", "Automated testing for Drupal 7"]
fetched: "2026-10-21T08:12:39Z"
raw: "raw/docs/7/testing/core-tests.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Core tests

Drupal core now comes with numerous tests for functionality (in the region of 50-70% code coverage as of June 2008).

When reviewing or writing patches, you should ensure that no new test failures are introduced by running all tests both before and after applying the patch. Ideally no patch should ever be marked RTBC if it breaks tests.

Since testing is still quite new in Drupal, there are currently some tests which fail in core due to exposing core bugs or issues in the test framework itself.

If you find a failing test that wasn't caused by your own changes, first check the [issue queue](http://drupal.org/project/issues) to see if there's an existing report, or [file a new bug report](http://drupal.org/node/add/project_issue/drupal/bug). There are also informal snapshots of known issues available in the Testing group on groups.drupal.org - <http://groups.drupal.org/node/11993>

If you think your test ought to pass, but still get fails or exceptions, please include as much information about your environment as possible - especially PHP, MySQL versions and operating system.
