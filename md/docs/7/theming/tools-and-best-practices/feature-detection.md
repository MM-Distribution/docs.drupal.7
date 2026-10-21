---
title: "Feature detection"
source_url: "https://www.drupal.org/docs/7/theming/tools-and-best-practices/feature-detection"
page_type: page
last_updated: "Last updated on 1 March 2018"
published: "2013-02-10T23:38:15+00:00"
modified: "2018-03-01T14:00:14+00:00"
breadcrumb: ["Drupal 7", "Theming Drupal 7", "Tools and best practices"]
fetched: "2026-10-21T08:55:21Z"
raw: "raw/docs/7/theming/tools-and-best-practices/feature-detection.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Feature detection

Browsers of all types connect to the web, and the diversity is only increasing. It used to be acceptable to specify which browser parameters (e.g. browser maker or screen size) the user should adopt to properly view your content, but this is no longer the case. Instead, it is better to adapt the web page to the users' individual browsers, based on the presence or absence of *specific features*. This is where the concept of **feature detection** comes from.

Think of feature detection as a way of fingerprinting a web browser. Just like two people with the same name, two devices running the same browser will produce different fingerprints.

## Modernizr

[Modernizr](https://modernizr.com) is the most popular feature detection library. It is a small JavaScript library that checks each user's browser features on every page load. It then prints the outcome of each test as a class inside the `<html>` tag of each page, allowing stylesheets that contain rules for both outcomes to "choose" a set of features. [Modernizr provides detailed docs](https://modernizr.com/docs/) on their website.

## Example

Touch devices often need very different interfaces than non-touch devices. Instead of relying on *user-agent sniffing*, it is more robust and future-proof to **check for the presence of touch events** and then develop CSS or JavaScript solutions for both outcomes.

### Conditional CSS

When Modernizr is executed each page load, by default it injects the results of all its tests into the `<html>` class attribute. If a feature is not supported, it is prefixed with `no-`.

``` php
.touch nav li {
  display: block;
  padding: .5em 1em;
  background: #456;
  border-radius: 5px;
}
.no-touch nav li {
  display: inline;
  float: left;
}
```

### JavaScript

JavaScript is a little more obvious because conditionals are one of its fundamental features.

``` php
if (Modernizr.touch) {
  $('nav').touchNav();
}
else {
  $('nav').notouchNav();
}
```

## Drupal integration

Drupal's [Modernizr module](https://drupal.org/project/modernizr) harnesses the power of Modernizr and provides additional integration, allowing Modernizr to be fully aware of your unique Drupal installation.
