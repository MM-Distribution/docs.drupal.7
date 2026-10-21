---
title: "Browser requirements"
source_url: "https://www.drupal.org/docs/7/system-requirements/browser-requirements"
page_type: page
last_updated: "Last updated on 13 October 2017"
published: "2006-05-02T21:16:30+00:00"
modified: "2017-10-13T15:22:23+00:00"
breadcrumb: ["Drupal 7", "Drupal 7 system requirements"]
fetched: "2026-10-21T05:53:11Z"
raw: "raw/docs/7/system-requirements/browser-requirements.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Browser requirements

Websites built using just [Drupal core](http://drupal.org/download) (i.e. with no additional, [contributed modules](http://drupal.org/project/Modules)) are compatible with, and fully functional, in all modern browsers that support CSS and JavaScript. However, browsers have varying levels of compliance with Internet standards such as CSS 2, so there may be minor variations in appearance.

Here is an incomplete list of browsers that are known to work well with Drupal 7 core and support all of its features:

- Internet Explorer 6.x and later
- Microsoft Edge
- Firefox 5.x and later
- Opera 12 and later
- Safari 5.x and later
- Google Chrome

It is also possible to use a browser that does not support JavaScript with Drupal, although the functionality will, of course, be slightly different. It is also possible to use a browser that does not support CSS with Drupal, but of course, the site will not look very similar to how it looks in a browser that does support CSS.

Some contributed modules and themes may not be compatible with all browsers. If you find a problem with browser compatibility in a contributed module or theme, or some functionality in a contributed module that does not work at all without JavaScript enabled, please [submit an issue](/node/add/project_issue) to report it to the module or theme maintainer.

## Known Issues

IE8 and older has a problem with loading more than 31 stylesheets, a situation that may be encountered if you are using a contributed theme or number of contributed modules. An acceptable workaround is to enable CSS aggregation.
