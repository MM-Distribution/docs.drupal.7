---
title: "Using taxonomy URLs to display sets of content"
source_url: "https://www.drupal.org/docs/7/organizing-content-with-taxonomies/using-taxonomy-urls-to-display-sets-of-content"
page_type: page
last_updated: "Last updated on 22 August 2016"
published: "2005-05-07T21:59:25+00:00"
modified: "2016-08-22T20:50:05+00:00"
breadcrumb: ["Drupal 7", "Organizing content with taxonomy in Drupal 7"]
fetched: "2026-10-21T07:09:32Z"
raw: "raw/docs/7/organizing-content-with-taxonomies/using-taxonomy-urls-to-display-sets-of-content.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Using taxonomy URLs to display sets of content

When displaying nodes, both in teaser listings on the Drupal home pages and in full, single-node view, many Drupal themes display the categories applied to the node. If the user selects any category term, Drupal will then display a browsable listing for all nodes tagged with that term.

Examine the Taxonomy URL for one such category listing. The end of the URL should look something like this:

`taxonomy/term/1`

And another Taxonomy URL, for a different term, something like this:

`taxonomy/term/2`

Note that Taxonomy URLs always contain one or more Term IDs at the end of the URL. These numbers, 1 and 2 above, tell Drupal which categories to display.

Now combine the Term ID's above in one URL using a comma as a delimiter:

`taxonomy/term/1,2`

The resulting listing represents the boolean AND operation. It includes all nodes tagged with both terms. To get a listing of nodes using either taxonomy term 1 OR 2, use a plus sign as the operator

`taxonomy/term/1+2 `

Want to combine more categories? Just add more delimiters and numbers. Know that you can use the taxonomy section in Drupal site administration to find out any Term ID. Just place the cursor over any *edit term* and look to the status bar at the bottom of the browser. Then substitute the new Term ID's found there to create a different category listing.

In addition to displaying Drupal nodes by category on site, Drupal has category specific RSS feeds for other sites to access your site content. See how the URL format for the RSS feed is very similar to the Taxonomy URL:

`taxonomy/term/1+2/0/feed`

This feature has been removed in Drupal 7.

Building individual Taxonomy URL's is not the most user friendly way to provide site users access to browsable listings. Nor do administrators necessarily want to build custom blocks for users with links to each category listing. To extend the means of accessing nodes by category, evaluate the following modules:

- [Taxonomy Menu](http://drupal.org/project/taxonomy_menu)
- [Dhtml Menu](http://drupal.org/project/dhtml_menu)
