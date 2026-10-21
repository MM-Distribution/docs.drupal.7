---
title: "Avoid too many modules"
source_url: "https://www.drupal.org/docs/7/site-building-best-practices/avoid-too-many-modules"
page_type: page
last_updated: "Last updated on 28 March 2018"
published: "2011-04-28T16:30:14+00:00"
modified: "2018-03-28T15:21:41+00:00"
breadcrumb: ["Drupal 7", "Drupal 7 site building best practices"]
fetched: "2026-10-21T07:12:07Z"
raw: "raw/docs/7/site-building-best-practices/avoid-too-many-modules.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Avoid too many modules

It is always good to think it over before enabling a module; too many enabled modules can slow down your site and may be tricky when updating especially on shared servers as their maximum allowed hardware resource usage is much lower than VPS and dedicated servers. If a module's functionality is no longer required by the site, it should be uninstalled; and preferably the related files should be removed from the server. Additionally, modules that are poorly maintained and contain bugs can be detrimental to the security and stability of your site.

Each website's needs and resources vary widely so the following numbers are offered as rough advice, not strict guidelines in any sense. These numbers are in addition to the core modules that come with your installation:

- For a small website on a shared hosting service: 20 or less well chosen contributed modules should provide plenty of flexibility and functionality while keeping a lean well performing site.
- For moderately complex sites: 20-50 modules may be more adequate, though a good site builder may be able to get more functionality out of less modules. You might start to feel the shortcomings of a shared host and might consider moving to a VPS.
- If your website is very complex and must satisfy many, many different use cases: 50 - 100 modules may be necessary. A shared hosting service may serve the site, but performance could be inadequate.
- If you have 100 - 150 modules enabled on your site, you either have a very complex website or there are more efficient ways to build your site - consider removing modules and finding simpler solutions for your use cases.
- If you have over 150 modules enabled on your site - either your Drupal site powers NASA or you have a serious module addiction, get help.

It is important to investigate the most well-maintained contributed modules, such as Views, Rules, Panels, and others before installing a large number of different modules on your site. The functionality of these modules can often mitigate the need to install slews of other modules on your Drupal site.

Theres 3 way to know how many modules are installed :

1.  Manually count it in your back office
2.  Make a query with mysql
3.  With Drush in command line

There is a drush command that can count your enabled modules:

``` php
drush pml --type=module --status=enabled | wc -l
```

By adding option --no-core you should get only contrib' module.

``` php
drush pml --type=module --status=enabled --no-core | wc -l
```

It should return a number, note that this will include every module from core as well as modules you have added, many of which contain multiple add on modules themselves.
