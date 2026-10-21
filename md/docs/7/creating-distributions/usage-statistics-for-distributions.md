---
title: "Usage statistics for distributions"
source_url: "https://www.drupal.org/docs/7/creating-distributions/usage-statistics-for-distributions"
page_type: page
last_updated: "Last updated on 23 December 2016"
published: "2012-02-02T19:17:40+00:00"
modified: "2016-12-23T06:07:37+00:00"
breadcrumb: ["Drupal 7", "Creating Drupal 7 distributions"]
fetched: "2026-10-21T07:53:16Z"
raw: "raw/docs/7/creating-distributions/usage-statistics-for-distributions.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Usage statistics for distributions

[Usage statistics](http://drupal.org/node/329620) are linked from drupal.org's [project](http://drupal.org/node/1015224) and [release](http://drupal.org/documentation/releases/types) pages of each [distribution](http://drupal.org/documentation/build/distributions), and are the basis for the default *Sort by: Most installed* search filter on the [installation profiles / distributions](http://drupal.org/project/installation+profiles) listing.

To obtain usage statistics on drupal.org, distributions need:

1.  Releases of the distribution available on its project at drupal.org, in order to collect release statistics.

2.  Core modules [Update Status (D6), or Update Manager (D7)](http://drupal.org/documentation/modules/update), enabled. It's advisable to have them enabled by default, for information and usage tracking, with a possible notice -if needed- to use only the compatible updates provided by the distribution maintainers.  
    Distributions can use [hook_update_status_alter()](http://api.drupal.org/api/drupal/modules--update--update.api.php/function/hook_update_status_alter/7) (also in [Drupal 6](http://api.drupal.org/api/drupal/developer--hooks--core.php/function/hook_update_status_alter/6)) so that update module can remain enabled but still hide warnings about releases from projects managed by the distribution. That's better than using [hook_update_projects_alter()](http://api.drupal.org/api/drupal/modules--update--update.api.php/function/hook_update_projects_alter/7) since removing projects from the list at that point would prevent those modules from getting proper usage tracking. It's better for update module to keep fetching info for those, but just not display warnings for new releases.  
    This is as well a feature request for the [update_advanced](/project/update_advanced) contributed module, that would provide an easy to use solution for distributions. The issue is [\#1425522: Help manage updates for distributions](/project/update_advanced/issues/1425522 "Status: Active").

3.  For Drupal 6 only, because of the lack of .info files for D6 versions of distributions, one or more custom modules such as features should be committed directly to the profile directory, on the Drupal git repository, before the packaging system adds core and contrib. The drupal.org packaging script writes metadata in the .info files of the custom modules or features, telling the Update Status module to query the distribution project at drupal.org for available releases, which triggers usage tracking. For example:  
     

    ``` php
    ; Information added by drupal.org packaging script on 2012-01-18
    version = "6.x-2.4"
    core = "6.x"
    project = "distribution_name"
    datestamp = "1326924940"
    ```

For *Drupal 6*, all items on the list, \#1, \#2, and \#3, are needed.  
For *Drupal 7*, just \#1 and \#2 are all that is needed for usage statistics.

## Download statistics

**Update:** In addition to the usage stats, and since April 6, 2012, download count has been [deployed](http://drupal.org/node/1353138) on the project pages, including distributions. The default sort order is still by usage.
