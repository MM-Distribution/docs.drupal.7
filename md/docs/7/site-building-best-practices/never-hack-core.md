---
title: "Never hack core"
source_url: "https://www.drupal.org/docs/7/site-building-best-practices/never-hack-core"
page_type: page
last_updated: "Last updated on 17 August 2016"
published: "2007-05-16T01:55:52+00:00"
modified: "2016-08-17T08:49:39+00:00"
breadcrumb: ["Drupal 7", "Drupal 7 site building best practices"]
fetched: "2026-10-21T07:10:34Z"
raw: "raw/docs/7/site-building-best-practices/never-hack-core.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Never hack core

"**Never hack core!**"

This phrase is commonly heard in the Drupal community. You might have seen it on T-shirts or stickers. [You might have seen the video](http://buildamodule.com/video/drupal-7-core-concepts-welcome-to-module-building-why-to-build-a-module-instead-of-modifying-source-code-and-how-this-video-series-works). It is one of the most important best practices for Drupal.

"Core" means all the files that belong to the [original Drupal installation](/project/drupal). That is all files except the ones in the "sites" folder. You can add installation profiles to the directory "profiles," but you should not modify any of the files already present in that folder.

### Reasons against modifying core files

- You will make it complicated, difficult, or nearly impossible to apply site updates such as Security and bug fixes.
- You will make it difficult for those that come after to maintain the site.
- You could possibly leave your site vulnerable to exploits.

The Drupal core has been designed to be modular, so there should be [no reason to hack it](http://drupal.org/node/1559728). If there is a feature you want and it cannot be accomplished outside of modifying core, consider submitting your hack as a patch. [Create an issue](/node/add/project-issue/drupal) and tell the community the feature you want to accomplish. It will then be tested and your feature may become a part of the Drupal core.

### Exceptions

Are there exceptions to this rule?

Nope.

Okay, maybe. But they are generally reserved for specific implementations by people who are extremely familiar with the Drupal code base, development practices, and security model, especially those who properly document their changes and practice proper revision control with their code. If you have to ask, the answer should almost always be "no."
