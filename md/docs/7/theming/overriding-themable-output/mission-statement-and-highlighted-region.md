---
title: "Mission statement and highlighted region"
source_url: "https://www.drupal.org/docs/7/theming/overriding-themable-output/mission-statement-and-highlighted-region"
page_type: page
last_updated: "Last updated on 31 August 2016"
published: "2010-04-22T19:57:59+00:00"
modified: "2016-08-31T14:15:53+00:00"
breadcrumb: ["Drupal 7", "Theming Drupal 7", "Overriding themable output"]
fetched: "2026-10-21T08:20:39Z"
raw: "raw/docs/7/theming/overriding-themable-output/mission-statement-and-highlighted-region.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Mission statement and highlighted region

## Drupal 6.x

In Drupal 6, the page template receives a special variable called \$mission. This contains the mission statement, displaying it on the front page. Drupal 6 themes also had an option on the theme settings page to toggle this functionality.

*In .info:*

``` php
features[] = mission
```

*In page.tpl.php:*

``` php
<?php print $mission; ?>
```

## Drupal 7.x

Drupal 7 removes the mission setting (and the option toggle) in favor of the more general custom block placement in regions. Drupal 7 core themes now include a region named 'highlighted' which uses the same display as D6's mission statement area. Whether this region has content now depends on administrators setting block placement, and is no longer limited to the front page.

If your theme defines custom regions, and does not include a "highlighted" region, you may [define the region](http://drupal.org/node/171224) by adding it to the existing list of regions your .info file. If the theme does not define regions in the .info file, the regions provided by core will be inherited automatically, and you'll only need to ensure that you print it in page.tpl.php.

*in .info:*

``` php
regions[highlighted] = Highlighted
```

*in page.tpl.php:*

``` php
<?php print render($page['highlighted']); ?>
```
