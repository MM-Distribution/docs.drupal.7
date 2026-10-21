---
title: "Content Delivery Network [CDN]"
source_url: "https://www.drupal.org/docs/7/managing-site-performance/cdn-%E2%80%94-content-delivery-network"
page_type: page
last_updated: "Last updated on 30 August 2016"
published: "2012-05-07T13:59:34+00:00"
modified: "2016-08-30T10:22:18+00:00"
breadcrumb: ["Drupal 7", "Managing Drupal 7 site performance and scalability"]
fetched: "2026-10-21T06:59:43Z"
raw: "raw/docs/7/managing-site-performance/cdn-%E2%80%94-content-delivery-network.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Content Delivery Network [CDN]

In many cases, it's very advantageous to integrate your Drupal site with a [CDN](http://en.wikipedia.org/wiki/Content_delivery_network). 

CDNs are globally distributed networks of proxy servers. A basic CDN integration will offload static assets (like images, videos, and sometimes CSS and JS) to the CDN. More advanced CDNs can deliver entire pages.

CDNs offer several advantages over serving all traffic directly:

- Assets can be cached in a proxy which is geographically closer to the end user, which usually leads to lower latency and increased download speed;
- Each page response is shared between your origin server and the CDN, meaning that your origin server can serve more concurrent requests;
- By splitting a response across multiple servers, enhanced HTTP performance can be achieved via [domain sharding](http://www.stevesouders.com/blog/2009/05/12/sharding-dominant-domains/), although this is becoming less advantageous with the increasing adoption of [HTTP/2 and SPDY](https://www.stevesouders.com/blog/2013/09/05/domain-sharding-revisited/);
- Some CDNs offer page optimisation services which can further enhance performance for end users.

## CDN integration

To make the integration with a CDN easier, the [CDN module](http://drupal.org/project/cdn) can help.

If you want to get up to speed as fast as possible, the following are the key articles to read:

1.  Good intro on CDNs (beside the Wikipedia article): [Key Properties of a CDN](http://wimleers.com/article/key-properties-of-a-cdn)
2.  Tutorial: [Easy Drupal CDN integration for fun and profit](http://wimleers.com/article/easy-drupal-cdn-integration-for-fun-and-profit)
3.  A test case to see the impact of a CDN: [Drupal 6 CDN integration: a test case](http://wimleers.com/article/drupal-6-cdn-integration-a-test-case)
