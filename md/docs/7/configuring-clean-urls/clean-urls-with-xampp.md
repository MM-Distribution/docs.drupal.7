---
title: "Clean URLs with XAMPP"
source_url: "https://www.drupal.org/docs/7/configuring-clean-urls/clean-urls-with-xampp"
page_type: page
last_updated: "Last updated on 11 October 2017"
published: "2006-01-06T05:13:32+00:00"
modified: "2017-10-11T07:03:56+00:00"
breadcrumb: ["Drupal 7", "Configuring clean URLs in Drupal 7"]
fetched: "2026-10-21T06:51:58Z"
raw: "raw/docs/7/configuring-clean-urls/clean-urls-with-xampp.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Clean URLs with XAMPP

Clean URLs works out of the box on current XAMPP. However, you probably need to set the rewrite base in the `.htaccess` file. Uncomment the line

`# RewriteBase /drupal`

if you have installed Drupal in a directory named `drupal` (inside the XAMPP `htdocs` directory).

Modify the RewriteBase if using Drupal in a subdirectory.  
For example if site is at **"Xampp/htdocs/Project/drupal"** and  If site URL looks like this**: "<http://localhost/project/drupal>".**

Then modify the following line in the .htaccesss :

``` php
   RewriteBase /Project/drupal
```
