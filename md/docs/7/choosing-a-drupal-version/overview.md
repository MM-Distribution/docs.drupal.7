---
title: "Overview"
source_url: "https://www.drupal.org/docs/7/choosing-a-drupal-version/overview"
page_type: page
last_updated: "Last updated on 25 June 2024"
published: "2005-07-24T09:11:02+00:00"
modified: "2024-06-25T02:42:14+00:00"
breadcrumb: ["Drupal 7", "Version numbering scheme for Drupal 7 core and contributed modules"]
fetched: "2026-10-21T06:16:26Z"
raw: "raw/docs/7/choosing-a-drupal-version/overview.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Overview

This page explains Drupal’s version numbering scheme for both Drupal core and contributed modules. It is designed to help you understand what the various version numbers mean and how you can use this information when building a Drupal site.

## Which version of Drupal core should I install?

**In brief, you should always run one of the recommended official releases.** These can be found at the [Drupal Project](http://drupal.org/project/Drupal) page.

At any given time, there are two major *release series* of Drupal which are [supported](https://www.drupal.org/docs/understanding-drupal/drupal-9-release-date-and-what-it-means/what-happens-to-drupal-7-now-that). Currently, these are [Drupal 7](https://www.drupal.org/drupal-7.41-release-notes) and [Drupal 10](https://www.drupal.org/project/drupal). Updated versions of each of these are issued on a regular basis. For example, within the Drupal 7 series, several versions have been released: 7.0, 7.1, 7.2, etc. These versions are sometimes collectively referred to as “7.x”; however, they are not all equal. The newest version in each series fixes problems that were discovered since the previous version, and these fixes sometimes include critical [security updates](http://drupal.org/security). Thus, regardless of whether you are using Drupal 7 or the current supported version, you should always run the most current release in the series.

In deciding between Drupal 7 and Drupal 10, several factors should be taken into consideration. Drupal 10 is newer, will be supported longer, and contains more features and enhancements than Drupal 7; therefore, if all else is equal, use [Drupal 10](https://www.drupal.org/9). However, the releases of contributed [modules](/project/Modules), [themes](/project/Themes), [translations](http://localize.drupal.org/), and [installation profiles](/project/installation+profiles) compatible with each major Drupal release series sometimes lag behind Drupal itself, so if the functionality you need is not yet available for Drupal 10, this may affect your decision.

To read more about Drupal 10, see [Drupal 10](/about/10).

## Which version of contributed modules, themes, and translations should I install?

You usually should run one of the “official releases” from the module, theme, or translation’s project page, because these are the versions that are currently supported by the maintainer. Note that when examining a particular release available on these pages, the first part of the version number shows you which major release series of Drupal core a module, theme, or translation is compatible with. For example, a module with a version number of *7.x*-1.2 will only work with Drupal 7, whereas a module with a version number of *10.x*-1.2 will only work with Drupal 10.

## When is the next release?

New stable releases of Drupal core are scheduled to occur within particular release “windows“:

- A bug fix (patch) release window is on the first Wednesday of each month.
- A security release window is on the third Wednesday of each month.
- For Drupal 10, minor (feature) releases are scheduled approximately every six months, usually on either the first or third Wednesday of that month.

For detailed information on these types of releases, see the [Drupal core release cycle overview](https://www.drupal.org/core/release-cycle-overview).

A release window does *not* necessarily mean that a release will actually be made on that date, but it exists so that site administrators can know in advance which days they should be on the look out for one.

For bugfix (patch) and feature (minor) releases, if a release is planned, a "code freeze" will be called a few days prior to the release date, and the upcoming release will be announced on [the core announcement group](http://groups.drupal.org/core), which also posts the announcement to the [@drupalcore](http://twitter.com/#!/drupalcore) Twitter account and [Planet Drupal](http://drupal.org/planet). This is a good time to update to the latest code in the branch for your version of Drupal, and help make sure the code is solid. The release window and associated code freeze typically begin at 12:00 UTC Tuesday and extend until 12:00 UTC Thursday.

[Security release windows](http://drupal.org/node/1173280) are handled via a separate process, and the final decision to make or not make a core release during a particular release window is made in private by the Drupal security team and only announced once the security fix is in place and the release is available for download.

Exceptions to the above schedule may be made in case of security vulnerabilities being actively exploited in the wild, severely critical bugs that prevent Drupal from being used, holidays, etc. When appropriate, changes will be announced in advance via Planet Drupal (and also via the [Drupal core group](http://groups.drupal.org/core)).

## How do I know which version of Drupal I’m running?

If it’s available, go to ***Administer (or Administration) \> Reports \> Status report***. This will list your version number if you have Drupal 6.0 or later. In Drupal 5.x and earlier, the path to go to is ***Administer \> Logs \> Status report***.

Failing that, look for a file called CHANGELOG.txt in the root of your Drupal directory and open it up to find the version you are running.

If CHANGELOG.txt is missing, you can also check in includes/bootstrap.inc for a line at the top like:

`define('VERSION', '7.16');`

Before Drupal 7 this was in modules/system/system.module  
If one of these is present, it will tell you which version you are running. If not, you have a version earlier than 4.7.2.

## How do I know which version of a module or theme I’m running?

You can see the versions of your installed modules and themes on the modules and themes administration screens. In Drupal 7, go to ***Administration \> Modules*** or ***Administration \> Appearance***, and you will see a column listing the version number. (In Drupal 6, the equivalent pages can be found at ***Administer \> Site building \> Modules*** and ***Administer \> Site building \> Themes***.)

## What about upgrading and backwards compatibility?

For more details about upgrading and backwards compatibility, read [this overview of Drupal’s philosophy on backwards compatibility](/node/65922).

## More details

The pages below have some more details for advanced users.
