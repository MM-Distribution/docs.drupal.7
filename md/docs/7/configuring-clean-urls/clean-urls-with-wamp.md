---
title: "Clean URLs with WAMP"
source_url: "https://www.drupal.org/docs/7/configuring-clean-urls/clean-urls-with-wamp"
page_type: page
last_updated: "Last updated on 8 August 2016"
published: "2015-10-01T07:26:11+00:00"
modified: "2016-08-08T13:10:26+00:00"
breadcrumb: ["Drupal 7", "Configuring clean URLs in Drupal 7"]
fetched: "2026-10-21T06:51:42Z"
raw: "raw/docs/7/configuring-clean-urls/clean-urls-with-wamp.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Clean URLs with WAMP

WAMP needs a small change to make the Clean URLs work with it.

\- Open the httpd.conf file from the WAMP menu inside the Apache section.  
- Find this:

`# LoadModule rewrite_module modules/mod_rewrite.so`

\- Uncomment the line by removing '#'.  
- Save the file  
- Restart Apache
