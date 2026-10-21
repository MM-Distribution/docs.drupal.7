---
title: "Managing Drupal 7 site performance and scalability"
source_url: "https://www.drupal.org/docs/7/managing-drupal-7-site-performance-and-scalability"
page_type: guide
published: "2016-07-11T13:26:57+00:00"
modified: "2026-02-24T10:45:30+00:00"
breadcrumb: ["Drupal 7"]
fetched: "2026-10-21T06:58:41Z"
raw: "raw/docs/7/managing-drupal-7-site-performance-and-scalability.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Managing Drupal 7 site performance and scalability

Drupal 7 is a complex application. A well configured Drupal 7 site can be highly performant and scale to many millions of visitors per day. Conversely, a poorly optimised site can be frustratingly slow for its users.

This series of articles will demonstrate how Drupal 7 can be configured for optimal performance.

## [Planning for Performance](/docs/7/managing-site-performance-and-scalability/planning-for-performance)

You should establish performance goals to ensure you spend effort wisely.

## [Caching to improve performance](/docs/7/managing-site-performance-and-scalability/caching-to-improve-performance)

Caching to improve performance

- [Caching Overview](/docs/7/managing-site-performance-and-scalability/caching-to-improve-performance/caching-overview)
- [Opcode Caching](/docs/7/managing-site-performance-and-scalability/caching-to-improve-performance/opcode-caching)
- [Reverse Proxy Cache](/docs/7/caching-to-improve-performance/reverse-proxy-cache)
- [Squid Caching](/docs/7/caching-to-improve-performance/squid-caching)
- [Varnish Cache](/docs/7/caching-to-improve-performance/varnish-cache)
- [Varnish 2.x Configuration](/docs/7/caching-to-improve-performance/varnish-2x-configuration)
- [Varnish 3.x Configuration](/docs/7/caching-to-improve-performance/varnish-3x-configuration)
- [Varnish 4.x Configuration](/docs/7/caching-to-improve-performance/varnish-4x-configuration)
- [Google's mod_pagespeed for Apache 2.2+](/docs/7/caching-to-improve-performance/googles-mod_pagespeed-for-apache-22)
- [Load Page Cache after cron Runs](/docs/7/caching-to-improve-performance/load-page-cache-after-cron-runs)

## [Changing PHP memory limits](/docs/7/managing-site-performance-and-scalability/changing-php-memory-limits)

There are several techniques to increase the PHP memory limit. Use the right one for your system configuration.

## [Content Delivery Network \[CDN\]](/docs/7/managing-site-performance/cdn-%E2%80%94-content-delivery-network)

A CDN offloads much of your site delivery to a network of dedicated edge caches.

## [Design for Low Bandwidth](/docs/7/managing-site-performance/design-for-low-bandwidth)

Drupal offers a variety of tools and features to reduce bandwidth requirements, including:

## [Increase upload size in your php.ini](/docs/7/managing-site-performance-and-scalability/increase-upload-size-in-your-phpini)

note: increasing PHP upload size is different from increasing PHP memory limit. You can learn to increase memory limit here.

## [Optimizing Drupal to load faster (Server, MySQL, caching, theming, HTML)](/docs/7/managing-site-performance-and-scalability/optimizing-drupal-to-load-faster-server-mysql-caching-theming-html)

Basic settings

## [Optimizing MySQL](/docs/7/managing-site-performance/optimizing-mysql)

Details of how to optimize MySQL for use with Drupal.

## [Randomizing MySQL Users For Exceeded max_questions Error](/docs/7/managing-site-performance/randomizing-mysql-users-for-exceeded-max_questions-error)

Sometimes malicious HTTP GET requests can take down your site, by bootstrapping Drupal so frequently that you can exceed a MySQL max_user

## [Server tuning considerations](/docs/7/managing-site-performance/server-tuning-considerations)

The performance of your Drupal site is dependent on three main factors: the goals of your site, the resource demands of your site traffic,

## [Tuning php.ini for Drupal](/docs/7/managing-site-performance/tuning-phpini-for-drupal)
