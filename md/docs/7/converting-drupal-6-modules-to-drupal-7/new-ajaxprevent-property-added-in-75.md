---
title: "New #ajax['prevent'] property added in 7.5"
source_url: "https://www.drupal.org/docs/7/converting-drupal-6-modules-to-drupal-7/new-ajaxprevent-property-added-in-75"
page_type: page
last_updated: "Last updated on 15 October 2016"
published: "2011-07-01T18:58:45+00:00"
modified: "2016-10-15T22:13:12+00:00"
breadcrumb: ["Drupal 7", "Converting Drupal 6 modules to Drupal 7"]
fetched: "2026-10-21T07:51:28Z"
raw: "raw/docs/7/converting-drupal-6-modules-to-drupal-7/new-ajaxprevent-property-added-in-75.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# New #ajax['prevent'] property added in 7.5

See <http://drupal.org/node/634616#comment-4681706>

A new `#ajax['prevent']` setting was added, defaulting to `'click'`

Binding to mousedown rather than click means that it is possible to trigger a  
click by pressing the mouse, holding the mouse button down until the Ajax  
request is complete and the button is re-enabled, and then releasing the mouse  
button. Set 'prevent' so that ajax.js binds an additional handler to prevent  
such a click from triggering a non-Ajax form submission. This also prevents a  
textfield's ENTER press triggering this button's non-Ajax form submission  
behavior.
