---
title: "Comparison of \"captcha free\" anti-spam modules"
source_url: "https://www.drupal.org/docs/7/extend/comparison-of-contributed-modules/comparison-of-captcha-free-anti-spam-modules"
page_type: page
last_updated: "Last updated on 30 April 2025"
published: "2016-01-18T16:14:15+00:00"
modified: "2025-04-30T20:53:04+00:00"
breadcrumb: ["Drupal 7", "Extending Drupal 7", "Comparison of contributed modules"]
fetched: "2026-10-21T08:56:55Z"
raw: "raw/docs/7/extend/comparison-of-contributed-modules/comparison-of-captcha-free-anti-spam-modules.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Comparison of "captcha free" anti-spam modules

### [Antibot](https://www.drupal.org/project/antibot)

**Concept:** Requires JavaScript to display the form and blocks submission processing until human user interaction detected (mouse move, key press, mobile swipe gesture... the action of the form is then switched back to the path that it was originally set to be).  
  
**Log of blocked attempts:** NOT Available.  
  
**UI to enable protection for certain forms:** Available.  

### [Captcha-free Form Protection](https://www.drupal.org/project/captcha_free)

**Concept:** Checks if JS and cookies are enabled. Additionally a maximum time for filling out the form can be set. Submission what take longer are refused.  
  
**Log of blocked attempts:** NOT Available.  
  
**UI to enable protection for certain forms:** Available.

### [Honeypot](https://www.drupal.org/project/honeypot)

**Concept:** Adds a visually hidden form element, and refuses input if form field is not empty. Additionally a minimum time for filling out the form can be set. Submissions that are too fast are refused.  
  
**Log of blocked attempts:** Available.  
  
**UI to enable protection for certain forms:** Available.

### [Spaces Enforced](https://www.drupal.org/project/spaces_enforced)

**Concept:** Inspired by spambot usernames, checks by default whether the registering username has any spaces and a user-defined number of user-defined characters by configuration.  
  
**Log of blocked attempts:** NOT Available.  
  
**UI to enable protection for certain forms:** NOT Available.

### [Spamicide](https://www.drupal.org/project/spamicide)

**Concept:** Adds a visually hidden form element, and refuses input if form field is not empty.  
  
**Log of blocked attempts:** Available.  
  
**UI to enable protection for certain forms:** Available.
