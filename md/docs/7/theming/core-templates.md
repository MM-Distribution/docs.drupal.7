---
title: "Core templates"
source_url: "https://www.drupal.org/docs/7/theming/core-templates"
page_type: page
last_updated: "Last updated on 30 November 2017"
published: "2011-03-11T20:27:36+00:00"
modified: "2017-11-30T10:54:26+00:00"
breadcrumb: ["Drupal 7", "Theming Drupal 7"]
fetched: "2026-10-21T06:04:48Z"
raw: "raw/docs/7/theming/core-templates.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Core templates

Core comes with a number of default template files. In order to override these templates, all you need to do is copy them into your theme folder and [clear the theme registry](/node/173880#theme-registry).

You can also override these templates in a more targeted way. In Drupal 7, they need to be renamed to use a double-hyphen. For example, "node--article.tpl.php". A single hyphen is still used to separate words: for example, "user-picture.tpl.php" or "node--long-content-type-name.tpl.php", so the double hyphen always indicates a more targeted override of what comes before the "--".

See [Converting 6.x themes to 7.x](http://drupal.org/update/themes/6/7#template_files_double_hyphen) for more info.

## Core templates

Default templates:

These are the default template *(.tpl.php)* files provided by core in Drupal 7. Documentation on the variables and purpose of these templates are located inside the templates. There is a [default set of variables](/node/226776) available to all templates.

Drupalize.Me offers a free, eight-minute video on the [ins and outs of modifying template.php](https://drupalize.me/videos/overview-templatephp "Overview of Template.PHP").

In order to override these templates, all you need to do is copy them into your theme folder and [clear the theme registry](/node/173880#theme-registry).

To override templates in a more targeted way, see [Drupal 7 Template Suggestions](/node/1089656).

Aggregator

*"modules/aggregator/..."*

- [aggregator-feed-source.tpl.php](http://api.drupal.org/api/file/modules/aggregator/aggregator-feed-source.tpl.php)
- [aggregator-item.tpl.php](http://api.drupal.org/api/file/modules/aggregator/aggregator-item.tpl.php)
- [aggregator-summary-item.tpl.php](http://api.drupal.org/api/file/modules/aggregator/aggregator-summary-item.tpl.php)
- [aggregator-summary-items.tpl.php](http://api.drupal.org/api/file/modules/aggregator/aggregator-summary-items.tpl.php)
- [aggregator-wrapper.tpl.php](http://api.drupal.org/api/file/modules/aggregator/aggregator-wrapper.tpl.php)

Block

*"modules/block/..."*

- [block-admin-display-form.tpl.php](http://api.drupal.org/api/file/modules/block/block-admin-display-form.tpl.php)
- [block.tpl.php](http://api.drupal.org/api/drupal/modules--block--block.tpl.php/7)

*Note: the Drupal 6 version of [block.tpl.php](http://api.drupal.org/api/file/modules/system/block.tpl.php/6) used to be part of "modules/system/...".*

Book

*"modules/book/..."*

- [book-all-books-block.tpl.php](https://api.drupal.org/api/drupal/modules%21book%21book-all-books-block.tpl.php/7.x)
- [book-export-html.tpl.php](https://api.drupal.org/api/drupal/modules%21book%21book-export-html.tpl.php/7.x)
- [book-navigation.tpl.php](https://api.drupal.org/api/drupal/modules%21book%21book-navigation.tpl.php/7.x)
- [book-node-export-html.tpl.php](https://api.drupal.org/api/drupal/modules%21book%21book-node-export-html.tpl.php/7.x)

Comment

*"modules/comment/..."*

- [comment-wrapper.tpl.php](http://api.drupal.org/api/file/modules/comment/comment-wrapper.tpl.php)
- [comment.tpl.php](http://api.drupal.org/api/file/modules/comment/comment.tpl.php)

*Note: [comment-folded.tpl.php](http://api.drupal.org/api/file/modules/comment/comment-folded.tpl.php/6) has been deprecated in Drupal 7.*

Field

*"modules/field/theme/..."*

- [field.tpl.php](http://api.drupal.org/api/drupal/modules--field--theme--field.tpl.php)

*Note: [field.tpl.php](http://api.drupal.org/api/drupal/modules--field--theme--field.tpl.php) is a new template in Drupal 7.*

Forum

*"modules/forum/..."*

- [forum-icon.tpl.php](http://api.drupal.org/api/file/modules/forum/forum-icon.tpl.php)
- [forum-list.tpl.php](http://api.drupal.org/api/file/modules/forum/forum-list.tpl.php)
- [forum-submitted.tpl.php](http://api.drupal.org/api/file/modules/forum/forum-submitted.tpl.php)
- [forum-topic-list.tpl.php](http://api.drupal.org/api/file/modules/forum/forum-topic-list.tpl.php)
- [forums.tpl.php](http://api.drupal.org/api/file/modules/forum/forums.tpl.php)

*Note: [forum-topic-navigation.tpl.php](http://api.drupal.org/api/file/modules/forum/forum-topic-navigation.tpl.php/6) has been deprecated in Drupal 7.*

Node

*"modules/node/..."*

- [node.tpl.php](https://api.drupal.org/api/drupal/modules!node!node.tpl.php/7)

Overlay

*"modules/overlay/..."*

- [overlay.tpl.php](http://api.drupal.org/api/drupal/modules--overlay--overlay.tpl.php/7)

*Note: [overlay.tpl.php](http://api.drupal.org/api/drupal/modules--overlay--overlay.tpl.php/7) is a new template in Drupal 7.*

Poll

*"modules/poll/..."*

- [poll-bar--block.tpl.php](http://api.drupal.org/api/search/7/api/drupal/modules--poll--poll-bar--block.tpl.php)
- [poll-bar.tpl.php](http://api.drupal.org/api/file/modules/poll/poll-bar.tpl.php)
- [poll-results--block.tpl.php](http://api.drupal.org/api/search/7/api/drupal/modules--poll--poll-results--block.tpl.php)
- [poll-results.tpl.php](http://api.drupal.org/api/file/modules/poll/poll-results.tpl.php)
- [poll-vote.tpl.php](http://api.drupal.org/api/file/modules/poll/poll-vote.tpl.php)

*Note: Former templates [poll-results-block.tpl.php](http://api.drupal.org/api/file/modules/poll/poll-results-block.tpl.php/6) and [poll-bar-block.tpl.php](http://api.drupal.org/api/file/modules/poll/poll-bar-block.tpl.php/6) have been renamed with a double dash in Drupal 7.*

Profile

*"modules/profile/..."*

- [profile-block.tpl.php](http://api.drupal.org/api/file/modules/profile/profile-block.tpl.php)
- [profile-listing.tpl.php](http://api.drupal.org/api/file/modules/profile/profile-listing.tpl.php)
- [profile-wrapper.tpl.php](http://api.drupal.org/api/file/modules/profile/profile-wrapper.tpl.php)

Search

*"modules/search/..."*

- [search-block-form.tpl.php](http://api.drupal.org/api/file/modules/search/search-block-form.tpl.php)
- [search-result.tpl.php](http://api.drupal.org/api/file/modules/search/search-result.tpl.php)
- [search-results.tpl.php](http://api.drupal.org/api/file/modules/search/search-results.tpl.php)

*Note: [search-theme-form.tpl.php](http://api.drupal.org/api/file/modules/search/search-theme-form.tpl.php/6) has been deprecated in Drupal 7.*

System

*"modules/system/..."*

- [page.tpl.php](https://api.drupal.org/api/drupal/modules!system!page.tpl.php/7)
- [maintenance-page.tpl.php](https://api.drupal.org/api/drupal/modules!system!maintenance-page.tpl.php/7)
- [region.tpl.php](https://api.drupal.org/api/drupal/modules!system!region.tpl.php/7)
- [html.tpl.php](https://api.drupal.org/api/drupal/modules!system!html.tpl.php/7)

*Note: [box.tpl.php](http://api.drupal.org/api/file/modules/system/box.tpl.php/6) has been deprecated in Drupal 7. [html.tpl.php](https://api.drupal.org/api/drupal/modules!system!html.tpl.php/7) and [region.tpl.php](https://api.drupal.org/api/drupal/modules!system!region.tpl.php/7) have been added.*

Taxonomy

*"modules/taxonomy/..."*

- [taxonomy-term.tpl.php](http://api.drupal.org/api/drupal/modules--taxonomy--taxonomy-term.tpl.php/7)

*Note: [taxonomy-term.tpl.php](http://api.drupal.org/api/drupal/modules--taxonomy--taxonomy-term.tpl.php/7) is a new template in Drupal 7.*

Toolbar

*"modules/toolbar/..."*

- [toolbar.tpl.php](http://api.drupal.org/api/drupal/modules--toolbar--toolbar.tpl.php/7)

*Note: [toolbar.tpl.php](http://api.drupal.org/api/drupal/modules--toolbar--toolbar.tpl.php/7) is a new template in Drupal 7.*

User

*"modules/user/..."*

- [user-picture.tpl.php](http://api.drupal.org/api/file/modules/user/user-picture.tpl.php)
- [user-profile-category.tpl.php](http://api.drupal.org/api/file/modules/user/user-profile-category.tpl.php)
- [user-profile-item.tpl.php](http://api.drupal.org/api/file/modules/user/user-profile-item.tpl.php)
- [user-profile.tpl.php](http://api.drupal.org/api/file/modules/user/user-profile.tpl.php)
