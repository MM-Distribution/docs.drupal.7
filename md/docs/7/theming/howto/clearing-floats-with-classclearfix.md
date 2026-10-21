---
title: "Clearing floats with class=\"clearfix\""
source_url: "https://www.drupal.org/docs/7/theming/howto/clearing-floats-with-classclearfix"
page_type: page
last_updated: "Last updated on 9 September 2016"
published: "2009-02-23T11:49:04+00:00"
modified: "2016-09-09T06:41:01+00:00"
breadcrumb: ["Drupal 7", "Theming Drupal 7", "Theming HowTos"]
fetched: "2026-10-21T08:27:26Z"
raw: "raw/docs/7/theming/howto/clearing-floats-with-classclearfix.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Clearing floats with class="clearfix"

Many HTML layouts require floats to be cleared so they don't interfere with content below them. This can be done by setting the 'clear' property on the subsequent element, but in flexible situations where the next element is not known, this is traditionally done with an empty DIV element with the clear property.

There is however a simpler way to do this. Drupal's system stylesheet has a very useful class: "clearfix" ("clear-block" in version of Drupal prior to 7). This is an implementation of the easy clearing technique [described at CSSCreator](http://csscreator.com/attributes/containedfloat.php).

To use this, simply give the class 'clearfix' to the element that contains the floats.

So for example, if you have a gallery of floated images that are LIs, put 'class="clearfix"' on the containing UL.

There are many examples of this in core Drupal, such as node links.
