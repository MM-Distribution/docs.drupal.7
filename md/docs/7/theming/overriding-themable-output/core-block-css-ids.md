---
title: "Core Block CSS IDs"
source_url: "https://www.drupal.org/docs/7/theming/overriding-themable-output/core-block-css-ids"
page_type: page
last_updated: "Last updated on 31 August 2016"
published: "2010-04-22T18:02:50+00:00"
modified: "2016-08-31T14:15:55+00:00"
breadcrumb: ["Drupal 7", "Theming Drupal 7", "Overriding themable output"]
fetched: "2026-10-21T08:20:24Z"
raw: "raw/docs/7/theming/overriding-themable-output/core-block-css-ids.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Core Block CSS IDs

Drupal Core generates a number of blocks, each with a unique CSS ID. In Drupal 7, many of the core block IDs have changed so they more clearly indicate the purpose of the block.

**Active forum topics**  
Drupal 6: block-forum-0  
Drupal 7: block-forum-active

**Author information**  
Drupal 6: block-profile-0  
Drupal 7: block-profile-author-information

**Book navigation**  
Drupal 6: block-book-0  
Drupal 7: block-book-navigation

**Language switcher**  
Drupal 6: block-locale-0  
Drupal 7: block-locale-language-switcher

**Most recent poll**  
Drupal 6: block-poll-0  
Drupal 7: block-poll-recent

**Navigation**  
Drupal 6: block-user-1  
Drupal 7: block-system-navigation

**New forum topics**  
Drupal 6: block-forum-1  
Drupal 7: block-forum-new

**Popular content**  
Drupal 6: block-statistics-0  
Drupal 7: block-statistics-popular

**Powered by Drupal**  
Drupal 6: block-system-0  
Drupal 7: block-system-powered-by

**Recent blog posts**  
Drupal 6: block-blog-0  
Drupal 7: block-blog-recent

**Recent comments**  
Drupal 6: block-comment-0  
Drupal 7: block-comment-recent

**Search form**  
Drupal 6: block-search-0  
Drupal 7: block-search-form

**Syndicate**  
Drupal 6: block-node-0  
Drupal 7: block-node-syndicate

**User login**  
Drupal 6: block-user-0  
Drupal 7: block-user-login

**Who's new**  
Drupal 6: block-user-2  
Drupal 7: block-user-new

**Who's online**  
Drupal 6: block-user-3  
Drupal 7: block-user-online

Drupal 6 CSS style declaration:

``` php
/* Make the text in the user login block bigger. */
#block-user-0 {
  font-size: 1.5em;
}
```

Drupal 7 CSS style declaration:

``` php
/* Make the text in the user login block bigger. */
#block-user-login {
  font-size: 1.5em;
}
```
