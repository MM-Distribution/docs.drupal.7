---
title: "Tools and best practices"
source_url: "https://www.drupal.org/docs/7/theming/tools-and-best-practices"
page_type: guide
published: "2016-09-08T13:30:10+00:00"
modified: "2016-09-08T13:36:40+00:00"
breadcrumb: ["Drupal 7", "Theming Drupal 7"]
fetched: "2026-10-21T06:06:37Z"
raw: "raw/docs/7/theming/tools-and-best-practices.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Tools and best practices

This guide presents best practices and conventions for theming Drupal 7 through a discussion of general tools and techniques for developing websites.

## [Safe theme development](/docs/7/theming/tools-and-best-practices/safe-theme-development)

You will invariably run into problems when developing a theme. Here are some safeguards and considerations when resolving issues with your

## [Theme coding conventions](/docs/7/theming/tools-and-best-practices/theme-coding-conventions)

Coding standards

## [Theming the Drupal maintenance page](/docs/7/theming/tools-and-best-practices/theming-the-drupal-maintenance-page)

What is the maintenance page?

## [Adding your theme to Drupal.org](/docs/7/theming/tools-and-best-practices/adding-your-theme-to-drupalorg)

Theme contributors are strongly encouraged to host your themes at Drupal.org rather than elsewhere (GitHub, BitBucket, your personal site,

## [Cross-browser testing](/docs/7/theming/tools-and-best-practices/cross-browser-testing)

Cross-browser testing refers to the practice of testing your theme in multiple browsers to ensure that each browser renders pages as

## [Recommended target browsers](/docs/7/theming/tools-and-best-practices/recommended-target-browsers)

Drupal 8

## [Creating a screenshot for the appearance page](/docs/7/theming/tools-and-best-practices/creating-a-screenshot-for-the-appearance-page)

Every theme for Drupal 7 needs a screenshot in the form of a screenshot.png placed in the theme directory.

## [Creating a screenshot for the administration page](/docs/7/theming/tools-and-best-practices/creating-a-screenshot-for-the-administration-page)

Note: There is a separate page on this for Drupal 7: http://drupal.org/node/647754

## [Making your theme semantically correct](/docs/7/theming/tools-and-best-practices/making-your-theme-semantically-correct)

Semantic (X)HTML elements convey meaning. Semantic markup combined with CSS is also the primary way to separate content from presentation.

## [Doctype, XML, and XHTML](/docs/7/theming/tools-and-best-practices/doctype-xml-and-xhtml)

Doctype is the first line of any HTML page and tells the browser how to interpret the HTML.

## [Feature detection](/docs/7/theming/tools-and-best-practices/feature-detection)

Browsers of all types connect to the web, and the diversity is only increasing. It used to be acceptable to specify which browser parameters

## [Installing Modernizr module and JavaScript library](/docs/7/theming/tools-and-best-practices/installing-modernizr-module-and-javascript-library)

Modernizr is not GPLv2, and therefore cannot ship within Drupal modules. Since the Modernizr module depends on the upstream JavaScript

## [Creating a custom build of Modernizr based on your Drupal setup](/docs/7/theming/tools-and-best-practices/creating-a-custom-build-of-modernizr-based-on-your-drupal)

When your site is ready to go live, you'll want to take inventory of which feature tests you used, and reduce your Modernizr JS library to

## [Modernizr.load() and Drupal: Basics](/docs/7/theming/tools-and-best-practices/modernizrload-and-drupal-basics)

Modernizr can also be a conditional resource loader, which means it can load different CSS or JS files based on the outcome of Modernizr

## [Implementing the Modernizr Test API within a module or theme](/docs/7/theming/tools-and-best-practices/implementing-the-modernizr-test-api-within-a-module-or-theme)

The Modernizr Drupal module provides a Test API which allows site admins to generate a custom build which contains all the features needed
