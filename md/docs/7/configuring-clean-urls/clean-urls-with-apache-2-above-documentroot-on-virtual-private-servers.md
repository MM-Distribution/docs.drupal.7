---
title: "Clean URLs with Apache 2 - above DocumentRoot on virtual private servers"
source_url: "https://www.drupal.org/docs/7/configuring-clean-urls/clean-urls-with-apache-2-above-documentroot-on-virtual-private-servers"
page_type: page
last_updated: "Last updated on 8 August 2016"
published: "2006-08-29T19:46:52+00:00"
modified: "2016-08-08T13:10:26+00:00"
breadcrumb: ["Drupal 7", "Configuring clean URLs in Drupal 7"]
fetched: "2026-10-21T06:50:09Z"
raw: "raw/docs/7/configuring-clean-urls/clean-urls-with-apache-2-above-documentroot-on-virtual-private-servers.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Clean URLs with Apache 2 - above DocumentRoot on virtual private servers

To set up clean URLs above web document root on virtual private servers, you need to change a setting in httpd.conf.

(default setting)  
Options FollowSymLinks  
AllowOverride None

Change it to  
Options FollowSymLinks  
AllowOverride All

None of the other changes discussed in this section of the handbook were necessary (and in fact had to be undone).

The hosting provide said this does not provide any security issues (no guarantees).

You may need to reset the VPS before the changes take effect.
