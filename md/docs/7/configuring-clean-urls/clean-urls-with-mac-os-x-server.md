---
title: "Clean URLs with Mac OS X Server"
source_url: "https://www.drupal.org/docs/7/configuring-clean-urls/clean-urls-with-mac-os-x-server"
page_type: page
last_updated: "Last updated on 11 April 2017"
published: "2007-04-09T11:55:04+00:00"
modified: "2017-04-11T06:39:37+00:00"
breadcrumb: ["Drupal 7", "Configuring clean URLs in Drupal 7"]
fetched: "2026-10-21T06:51:27Z"
raw: "raw/docs/7/configuring-clean-urls/clean-urls-with-mac-os-x-server.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Clean URLs with Mac OS X Server

For Mac OS X Server 10.4 (Tiger Server) and most likely previous versions as well, do not make changes to `/etc/httpd/httpd.conf` expecting the `AllowOverride All` directive to work. The correct file to add the `AllowOverride All` directive is in the directory `/etc/httpd/sites/`. In that directory are the virtual host configuration files. Each virtual server has a configuration file in that directory so it is in those files that you must enable `AllowOverride All`. If you only have one web server on your server configured, then the file you want to modify is `/etc/httpd/sites/0000_any_80_.conf`.

### Mac OS 10.7 Lion Server

For Mac OS X Server 10.7 (Lion Server), the appropriate .conf files are located at `/etc/apache2/sites`. Within that directory, you should find .conf files for each virtual host you've configured through Web Server panel of the Server Tools application.

Changing the `AllowOverride None` line to `AllowOverride All` then stopping and restarting the web server (using the Server Tools application) should make clean URLs on Lion Server work correctly (with an unmodified .htaccess file).
