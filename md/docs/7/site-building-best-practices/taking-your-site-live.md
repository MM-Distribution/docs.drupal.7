---
title: "Taking your site live"
source_url: "https://www.drupal.org/docs/7/site-building-best-practices/taking-your-site-live"
page_type: page
last_updated: "Last updated on 17 August 2016"
published: "2007-04-10T21:44:41+00:00"
modified: "2016-08-17T08:49:39+00:00"
breadcrumb: ["Drupal 7", "Drupal 7 site building best practices"]
fetched: "2026-10-21T07:11:52Z"
raw: "raw/docs/7/site-building-best-practices/taking-your-site-live.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Taking your site live

Once you've got your Drupal installation set up just the way you want it, there are a few final considerations before you unleash it on the world.

## Moving from a temporary location

It's likely that you've put Drupal in a subfolder on your server, so it doesn't interfere with your existing website while you get it set up. So you have [www.example.com](http://www.example.com) showing your old site, [www.example.com/drupal](http://www.example.com/drupal) showing drupal, and you want [www.example.com](http://www.example.com) to show off your new site to the world. There are two ways you can go about this:

### Moving Drupal

For newer versions of Drupal, moving the Drupal base folder shouldn't pose any problems. For versions prior to Drupal 5, some settings may need to be changed so Drupal can find everything. See [this forum thread](http://drupal.org/node/20853) for more details.

### Redirecting your server

Alternatively, you can leave Drupal where it is in a subfolder, and just have your webserver fool everyone into thinking that folder is [www.example.com](http://www.example.com).

With Apache, you need to add the following to the .htaccess in the root folder (or create an .htaccess file if there isn't one there):

``` php
RewriteEngine on
#
# stuff to let through (ignore)
#RewriteCond %{REQUEST_URI} "/folder1/" [OR]
#RewriteCond %{REQUEST_URI} "/folder2/"
RewriteRule (.*) drupal/$1 [L]
```

Use the RewriteCond rules to let through URLS without modification (for example, you might have other subfolders you still want accessible). Replace 'drupal' with the name of the folder Drupal is in.

You also need to modify the settings.php file for your site. By default, this is at sites/default/settings.php. Uncomment (or change) the line that sets \$base_url, and set it to the URL you want browsers to see as the base for your site:

``` php
$base_url = 'http://www.example.com';
```

In other words, ensure that this does *not* include the drupal subdirectory. This changes the links that Drupal generates so they point to the correct location.

### Excluding paths from Drupal

It may be that your site is made up components other than Drupal, or that you have an archive version of your old site you want to be browsable. Drupal in a root folder takes over all URLs; Drupal in a subfolder fooled into thinking it's root likewise.

Either way, the .htaccess file in the root folder needs to be changed to let through the paths to files or folders you want Drupal to ignore.

In the case where Drupal is in the root folder, here's what you need to do:

1.  In your webserver root's .htaccess file, find the section marked with the comment '# Various rewrite rules.'

2.  Below 'RewriteEngine on' but before any other rules, add lines in the following form:  

    ``` php
      RewriteRule /folder - [L]     # a subfolder Drupal should ignore
      RewriteRule /file.html - [L] # a file in root Drupal should ignore
    ```

*This page is a work in progress. Please suggest other tasks it should cover.*
