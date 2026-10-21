---
title: "URL paths"
source_url: "https://www.drupal.org/docs/7/understanding-drupal/url-paths"
page_type: page
last_updated: "Last updated on 28 June 2021"
published: "2005-09-19T16:47:59+00:00"
modified: "2021-06-28T06:47:48+00:00"
breadcrumb: ["Drupal 7", "Understanding Drupal 7"]
fetched: "2026-10-21T05:50:51Z"
raw: "raw/docs/7/understanding-drupal/url-paths.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# URL paths

In Drupal terms, a *path* is the unique end portion part of the URL for a specific function or piece of content. For instance, in the URL `http://example.com/?q=node/7`, the path is *node/7*. If your site is using [clean URLs](/node/15365), the URL in this example would be `http://example.com/node/7`, meaning the path would still be *node/7*. Paths containing node IDs are sometimes referred to as *internal paths*, since [URL aliases](/handbook/modules/path) are often used to replace the URL that visitors see.

Many configuration screens in the Drupal admin area refer to paths. For instance, when adding a new menu link to a menu, you tell Drupal what page the menu item should point to using the path for that page.

Here are some examples of paths you might find in a Drupal site:

- node/7
- taxonomy/term/6
- admin/content/comment
- user/login
- user/3

### How to find Drupal paths

There are several ways to find the path to a particular page on your Drupal site. The first step is to find the URL of the page of interest:

- If you know how to navigate to the page, you can go there and find the URL in your browser's URL bar.
- You can also hover your mouse over a link to the page (such as in the Views administration screen or the content management screen at Menu \> Content (admin/content)), and most browsers will show you the URL in the status section at the bottom of the browser window.
- In some cases the browser's URL bar or hovering over the link will give you the alias for the page. If you want the internal id (node id or nid) navigating to the page in question and hovering over the edit link (if you have permission to edit that page) will give you the node ID. For example if you are on this page the URL would be */node/31644/edit* and the node id is *31644*.

The URL you find could have several forms:

- `http://example.com/?q=[something]` -- In this case, the *\[something\]* after *?q=* is the path. For example, if the URL is `http://example.com/?q=node/7`, the path is *node/7*.
- `http://example.com/[something]` or `http://example.com/[your Drupal subdirectory]/[something]` -- In this case, the *\[something\]* after the base path of your Drupal site is the path. For example, your URL could be `http://example.com/node/7` or `http://example.com/mysubdir/node/7`; the path in either case is *node/7*.

## Duplicate content

The use of the [path module](/documentation/modules/path) can lead to duplicate paths leading to one page. Search engines consider this as duplicate content. The module [Global Redirect](/project/globalredirect) can prevent problems as a result of duplicate content.

## How to automatically generate friendly URLs

You can use the [Pathauto](https://www.drupal.org/project/pathauto) module to automatically generate user-friendly URL aliases for various kinds of content (nodes, taxonomy terms, users) without having to manually specify the alias. The [Pathauto](https://www.drupal.org/project/pathauto) module uses tokens and patterns, which the administrator can change, to create friendly URLs.
