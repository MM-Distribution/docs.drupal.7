---
title: "Testing setup and configuration"
source_url: "https://www.drupal.org/docs/7/automated-testing-for-drupal-7/testing-setup-and-configuration"
page_type: page
last_updated: "Last updated on 17 January 2023"
published: "2009-07-14T21:59:54+00:00"
modified: "2023-01-17T09:15:30+00:00"
breadcrumb: ["Drupal 7", "Automated testing for Drupal 7"]
fetched: "2026-10-21T08:09:49Z"
raw: "raw/docs/7/automated-testing-for-drupal-7/testing-setup-and-configuration.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Testing setup and configuration

## Requirements

SimpleTest has a few non-default requirements. In addition to the requirements listed below, all core requirements need to be met since tests may execute any module.

- CURL extension for PHP
- PHP [open_basedir](http://php.net/manual/en/ini.core.php#ini.open-basedir) restriction needs to be disabled.
- DOM extension for PHP. DOM support is included by default in php5.
- Recommended PHP memory limit of 256MB (not exact)

### Drupal 7.x

1.  SimpleTest is now in core, where it is called the Testing (`simpletest`) module. Enable it under *admin/modules*.
2.  If necessary, go to Testing settings page under *admin/config/development/testing/settings* to configure the HTTP auth settings.

## Environment

Since Testing will be accessing your computer in the same manner as your browser does, it needs to have the necessary permissions (ie. HTTP auth, firewall) to access your development site.

Once you have these items in place you may enable SimpleTest/Testing.

More details are available in the SimpleTest [INSTALL.txt](http://drupalcode.org/project/simpletest.git/blob/3c689dc0f6f9e86da2bcec54d0bbf67e081b55ad:/INSTALL.txt).
