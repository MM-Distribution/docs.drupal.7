---
title: "Front-end performance"
source_url: "https://www.drupal.org/docs/7/mobile/front-end-performance"
page_type: page
last_updated: "Last updated on 22 September 2016"
published: "2011-12-29T15:21:07+00:00"
modified: "2016-09-22T01:51:45+00:00"
breadcrumb: ["Drupal 7", "Mobile guide for Drupal 7"]
fetched: "2026-10-21T07:19:05Z"
raw: "raw/docs/7/mobile/front-end-performance.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Front-end performance

Front end performance is a critical task shared by all mobile solutions.

- Minify JavaScript, CSS and HTML
- Combine JavaScript and combine CSS
- Parallelize downloads across hostnames
- Leverage browser caching
- Enable gzip compression
- Specify image dimensions
- Optimize images
- Lazy loading assets
- Inline background images under ~4KB
- Remove unused CSS
- Use efficient CSS selectors

### Testing

Here are some tools that can be used to test frontend performance:

- [YSlow](http://yslow.org/) profiles pages and offers recommendations for speeding them up.
- Network tab of [Firebug](http://getfirebug.com/)/[Chrome](https://developers.google.com/chrome-developer-tools/docs/network)/Safari/Opera devtools.
- [Learn to read waterfall charts](http://www.strangeloopnetworks.com/blog/how-to-use-a-waterfall-chart-to-interpret-web-performance-data/) from Strangeloop Networks
- [WebPageTest.org](http://www.webpagetest.org/) offers frontend performance testing from various locations worldwide. You choose the browser to test.
- [gtmetrix.com](http://gtmetrix.com/) & [loads.in](http://loads.in/) also offer more front-end performance testing.
- [jdrop.org](http://jdrop.org) allows you to collect data on mobile devices and analyze it on a bigger computer using JavaScript-powered storage of test results.
- [PageSpeed Insights](https://developers.google.com/speed/pagespeed/insights/ "PageSpeed Insights") offers website performance insights and provide recommendation to improve page speed on all devices.
