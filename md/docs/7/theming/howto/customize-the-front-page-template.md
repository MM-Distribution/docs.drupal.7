---
title: "Customize the front page template"
source_url: "https://www.drupal.org/docs/7/theming/howto/customize-the-front-page-template"
page_type: page
last_updated: "Last updated on 21 March 2017"
published: "2008-10-06T04:27:04+00:00"
modified: "2017-03-21T20:13:23+00:00"
breadcrumb: ["Drupal 7", "Theming Drupal 7", "Theming HowTos"]
fetched: "2026-10-21T08:49:56Z"
raw: "raw/docs/7/theming/howto/customize-the-front-page-template.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Customize the front page template

If you want to layout your front page dramatically different from the rest of your site, you can define a whole other template just for that.

## Creating a Front Page Template

Creating a front page template is rather simple. In your theme folder (sites/all/themes/), copy the page.tpl.php file from drupal core or your parent theme. Then rename it accordingly (see below). You probably won't see the results until you clear your cache; so make sure to do that.

**Drupal 7**  
In Drupal 7, copy the `page.tpl.php` file and name it `page--front.tpl.php`.

**Drupal 6**  
In Drupal 6, copy the `page.tpl.php` file and name it `page-front.tpl.php`

## Template Suggestions

Any Drupal page can be themed specifically, using the [template-suggestions](http://drupal.org/node/190815#template-suggestions) process used in phptemplate theme engine. This is powerful, learn about it.

Note that using *relative paths* to images (or swf) directly from that page will not work to find images stored nearby in your theme directory. *Placing those images in your theme directory is the correct thing to do*, but you will have to rewrite your HTML to either use:  
`<img src="/sites/all/themes/yourtheme/images/yourimage.gif" />` (which is bad, but quick) or `<img src="<?php print $directory; ?>/images/yourimage.gif" />` which is much better, if you're working on a base theme - \$directory returns the current active theme path. If you're creating a subtheme, though, \$directory will still [return your base theme path](https://www.drupal.org/node/2374769). So, in subtheme we've to use slightly more complex construction:  
`<img src="<?php print $base_path . drupal_get_path('theme', 'YOURSUBTHEME_NAME'); ?>/images/yourimage.gif"/>`

To do a custom front page that is *mostly* unique, yet merges seamlessly with Drupal, you can:

1.  Create a template file with the following naming convention`page--front.tpl.php` in your active theme directory.
2.  Paste in solid, static HTML, with appropriate file path fixes.
3.  **Compare** your template file with the default page.tpl.php in the theme folder and edit and needed.
4.  You can put `$content` in the middle, sidebars in a useful place for you to call blocks into later, and the \$footer in your footer zone, etc. Try to copy as much as possible - most of it can be useful, and is the real reason for using a CMS.

Under Drupal 6, new templates may not always be recognized or used immediately. Visit the admin-themes page and submit once to refresh the themes cache the first time you add the \*.tpl.php

There are also several module designed to give you advanced control of the page without too much template work, such as [Panels](http://drupal.org/project/panels) or maybe [Node Style](http://drupal.org/project/node_style)

See the tutorials for advice on [how to change the *content* of the front page](http://drupal.org/node/265172) and replace the "River of news" or the "Welcome to Drupal" with a specific page.
