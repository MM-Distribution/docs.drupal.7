---
title: "Caching to improve performance"
source_url: "https://www.drupal.org/docs/7/managing-site-performance-and-scalability/caching-to-improve-performance"
page_type: guide
published: "2016-07-11T13:27:20+00:00"
modified: "2016-09-09T20:44:48+00:00"
breadcrumb: ["Drupal 7", "Managing Drupal 7 site performance and scalability"]
fetched: "2026-10-21T06:59:12Z"
raw: "raw/docs/7/managing-site-performance-and-scalability/caching-to-improve-performance.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Caching to improve performance

The single biggest improvement to application performance is to skip as many computation steps as possible by using caching.

Caching in Drupal can occur at many levels. This guide will help you to understand best practice and how to implement caching appropriately for your application.

## [Caching Overview](/docs/7/managing-site-performance-and-scalability/caching-to-improve-performance/caching-overview)

In order to maximize performance of Drupal, we need to understand Drupal's execution and caching model.

## [Opcode Caching](/docs/7/managing-site-performance-and-scalability/caching-to-improve-performance/opcode-caching)

Enabling an Opcode Cache is an easy and effective way to improve performance of PHP execution.

## [Reverse Proxy Cache](/docs/7/caching-to-improve-performance/reverse-proxy-cache)

A well tuned reverse proxy cache, sometimes also referred to as a "web accelerator", can dramatically increase a websites performance. Squid

## [Squid Caching](/docs/7/caching-to-improve-performance/squid-caching)

Squid is a fully-featured, open-source web-content caching system. In accelerator mode, squid can be used in between your users and your

## [Varnish Cache](/docs/7/caching-to-improve-performance/varnish-cache)

Varnish Cache is a modern reverse proxy cache software package. It has been built from the ground up to be a dedicated reverse proxy cache

## [Varnish 2.x Configuration](/docs/7/caching-to-improve-performance/varnish-2x-configuration)

The VCL snipets below are based on a Varnish 2.0.x example configuration from this blogpost by Caleb G

## [Varnish 3.x Configuration](/docs/7/caching-to-improve-performance/varnish-3x-configuration)

Backends

## [Varnish 4.x Configuration](/docs/7/caching-to-improve-performance/varnish-4x-configuration)

Backends

## [Google's mod_pagespeed for Apache 2.2+](/docs/7/caching-to-improve-performance/googles-mod_pagespeed-for-apache-22)

In November of 2010 Google released an Apache module named mod_pagespeed. This is a server side module for Apache designed to manage caching

## [Load Page Cache after cron Runs](/docs/7/caching-to-improve-performance/load-page-cache-after-cron-runs)

Drupal creates pages and serves them to clients. The completed pages are also stored in the cache_page table of the database -- referred to
