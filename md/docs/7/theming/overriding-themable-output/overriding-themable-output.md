---
title: "Overriding themable output"
source_url: "https://www.drupal.org/docs/7/theming/overriding-themable-output/overriding-themable-output"
page_type: page
last_updated: "Last updated on 30 April 2020"
published: "2008-12-02T15:39:51+00:00"
modified: "2020-04-30T18:36:01+00:00"
breadcrumb: ["Drupal 7", "Theming Drupal 7", "Overriding themable output"]
fetched: "2026-10-21T08:17:34Z"
raw: "raw/docs/7/theming/overriding-themable-output/overriding-themable-output.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Overriding themable output

Depending on how your site is configured, the HTML code that makes up each page in your site is compiled from the output of various Drupal modules.

## About modifying HTML markup

If the default HTML markup supplied by any module does not suit the requirements of your theme, you can override some or all of it, so that the resulting page is exactly what you need for your design.

For example, you might decide that for your site, the default search box should have an image of a magnifying glass and that the label on the search button should read "Discover great stuff!" rather than the default label of "Search". You can completely override the default markup, so that the markup calls for your image file and that the button is labeled the way you want.

## Don't hack core

It's very important to understand the concept of "overriding". While it is technically possible to just find the module responsible for the search field and edit the code directly, this is definitely NOT recommended. In the short term, it will seem to solve your problem, but it will soon make it difficult to keep your site up to date. Whenever you update the module, perhaps for a general security release, you would need to remember to redo any of your customizations.

## How to change HTML the Drupal way

The "Drupal Way" is to do an override. This involves four basic steps:

1.  Locate the module responsible for the markup
2.  Do *one* of the following:
    - If the module provides a template (tpl.php file), copy the template to your theme directory. See [Core Templates and Suggestions](/node/190815) for a list of core templates. *OR...*
    - In the module code, identify the theme or preprocess function that is generating the markup you want to change and copy the function to your theme's template.php file. You will need to change the "theme\_" or "template\_" prefix to match the name of your theme. For example, "theme_breadcrumb" would become "mythemename_breadcrumb"; "template_preprocess_page" would become "mythemename_preprocess_page".
3.  Within the copied function or template, change the HTML code to suit your needs.
4.  Refresh the theme cache.

The [About overriding themeable output](http://drupal.org/node/173880) page provides a more in-depth look at overriding Drupal's default markup and the underlying system that makes it possible.

These steps are explained in greater detail in the following pages.

## Using PHP for theming

If you are not already familiar with PHP, the process might seem somewhat intimidating, but it generally does not require that you understand anything about actually writing PHP. As long as you know what HTML you want to be displayed, it's simply a matter of modifying that part of the code. As with any theming work, you should not make changes to a live or production site until you have thoroughly tested the changes on a development site.

## Overriding CSS

Many modules also provide style sheets (.css files) which specify the default look and feel of the markup. These style sheets can also be overridden. For more information, see [Overriding style sheets from modules and base themes.](/node/263967)

## Popular Contributed Modules that override the default HTML output

Some contributed modules have their own theming guides. Also see [overriding style sheets from modules and base themes](http://drupal.org/node/263967).

Modules for which theming-specific documentation exists are listed below by Drupal version.

### Drupal 7–compatible modules

- [Panels](http://drupal.org/node/495654)
- [Views 3 Slideshow](http://drupal.org/node/903244)
- [Print](http://drupal.org/node/190171)
- [Menu Block](https://www.drupal.org/node/1934824)
