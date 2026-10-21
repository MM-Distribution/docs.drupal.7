---
title: "Design for Low Bandwidth"
source_url: "https://www.drupal.org/docs/7/managing-site-performance/design-for-low-bandwidth"
page_type: page
last_updated: "Last updated on 16 August 2016"
published: "2015-09-19T15:08:22+00:00"
modified: "2016-08-16T20:34:52+00:00"
breadcrumb: ["Drupal 7", "Managing Drupal 7 site performance and scalability"]
fetched: "2026-10-21T06:59:58Z"
raw: "raw/docs/7/managing-site-performance/design-for-low-bandwidth.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Design for Low Bandwidth

Drupal offers a variety of tools and features to reduce bandwidth requirements, including:

### Adaptive Images

Your site is being increasingly viewed on smaller, slower, low bandwidth devices. On those devices your desktop-centric images load slowly, cause interface lag, and cost you and your visitors un-necessary bandwidth and money. Drupal includes the functionality to deliver small images to small devices; reducing bandwidth and resource requirements.

Drupal is capable of detecting a visitor's screen size and automatically create, caches, and deliver device appropriate re-scaled versions of your web page's embedded HTML images. No mark-up changes are required. It is intended for use with responsive designs. See [Adaptive Image](https://www.drupal.org/project/adaptive_image) module for more information.

### Aggregated and Compressed Stylesheets and JavaScript

Drupal has many stylesheets and JavaScript files. Of course, you want to keep the number of files at a minimum on your live sites for performance reasons, so Drupal includes options to aggregate and compress CSS and JavaScript files.

Drupal aggregates files in two ways: it creates a per-site aggregation file from files that would be loaded on every page, and it creates a per-page aggregation files for the remaining files that are conditionally loaded depending on the page. For CSS files, it further aggregates by media type.

Enabling aggregation and compression for CSS files on all live sites is highly recommended, as it will lower bandwidth and resource requirements for website visitors. Aggregation will also minimize the number of HTTP requests required to load a page; each request has an amount of overhead and latency associated with it. Too many requests would add delays to page loading.

### Support for Browser Caching

A user’s browser can keep a static file (image, stylesheets, etc.) without checking the server for an update and downloading it again. Therefore, each time someone visits a page on your website, the visitor will not be required to download the static content again, reducing bandwidth, resource requirements, and page load times. For more information regarding browser caching, see [mod_expires](http://httpd.apache.org/docs/2.2/mod/mod_expires.html) documentation.

If you are interested in learning more about low bandwidth design, please review [Web Design Guidelines for Low Bandwidth](http://www.aptivate.org/webguidelines/Home.html).
