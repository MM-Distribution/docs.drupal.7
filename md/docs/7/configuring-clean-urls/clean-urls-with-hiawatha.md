---
title: "Clean URLs with Hiawatha"
source_url: "https://www.drupal.org/docs/7/configuring-clean-urls/clean-urls-with-hiawatha"
page_type: page
last_updated: "Last updated on 30 April 2019"
published: "2014-05-28T18:09:14+00:00"
modified: "2019-04-30T19:41:51+00:00"
breadcrumb: ["Drupal 7", "Configuring clean URLs in Drupal 7"]
fetched: "2026-10-21T06:50:26Z"
raw: "raw/docs/7/configuring-clean-urls/clean-urls-with-hiawatha.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Clean URLs with Hiawatha

[Hiawatha Webserver](https://www.hiawatha-webserver.org/ "Hiawatha Webserver") offers URL rewriting via the [URL Toolkit](https://www.hiawatha-webserver.org/howto/url_toolkit "URL Toolkit"). The required toolkit rule for your Drupal website is:

``` php
UrlToolkit {
    ToolkitID = drupal
    RequestURI isfile Return
    Match ^/favicon.ico$ Return
    Match /(.*)\?(.*) Rewrite /index.php?q=$1&$2
    Match /(.*) Rewrite /index.php?q=$1
}

VirtualHost {
    Hostname = www.yoursite.org
    WebsiteRoot = /path/to/drupal
    ...
    UseToolkit = drupal
}
```
