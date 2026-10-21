---
title: "Contributed modules to help with accessibility"
source_url: "https://www.drupal.org/docs/7/creating-accessible-themes/contributed-modules-to-help-with-accessibility"
page_type: page
last_updated: "Last updated on 15 September 2018"
published: "2009-03-07T17:12:38+00:00"
modified: "2018-09-15T17:14:36+00:00"
breadcrumb: ["Drupal 7", "Theming Drupal 7", "Creating accessible themes"]
fetched: "2026-10-21T08:23:30Z"
raw: "raw/docs/7/creating-accessible-themes/contributed-modules-to-help-with-accessibility.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Contributed modules to help with accessibility

The following modules can help improve the accessibility of your site.

Note: Some of these modules may be outdated and/or not covered by Drupal's security advisory policy. Please check individual module page for more details. [For Drupal 8 modules](https://www.drupal.org/docs/8/accessibility/contributed-modules-for-extending-accessibility-in-drupal-8).

Note: Version \#'s under module names were current as of 2016.10.12

## [Accessibility (a11y) Checklist](http://drupal.org/project/a11y_checklist)

7.x-1.x-dev    2013-09-30

The [Accessibility (a11y) Checklist module](http://drupal.org/project/a11y_checklist) is designed to help web developers step through some basic accessibility tests for reviewing their website. Like the other checklists, it's an important way to keep track of things to review.

## [Accessible Helper Module](http://drupal.org/project/accessible)

7.x-2.x-dev    2013-09-30

The [Accessible module](http://drupal.org/project/accessible) is designed to help overcome deficits in Drupal core and contributed modules without theming and coding. It works through form hooks, CSS additions, and theming.

### Issues Addressed

- Adds ability for block authors to class individual block titles as off-screen.
- Fixes Google CSE search form label and heading accessibility issues through hook form alter.

## [Readability Analyzer](http://drupal.org/project/readability)

7.x-1.0-rc2    2012-01-11

This module is designed to help copywriters and editors develop more consistently readable content across a Drupal site. It performs five popular automated readability tests that provide a grade level equivalency of the difficulty of a page's readability.

## [Accessible Forms](http://drupal.org/project/accessible_forms)

7.x-1.0-alpha2    2015-06-15

This is a simple Drupal 7 module for adding form attributes for improved accessibility.

## [Better Select](http://drupal.org/project/betterselect)

7.x-1.0-beta3    2013-09-15

Multi-select HTML select elements are hard for users. Selecting more than one requires Ctrl+clicking (or Cmd+clicking on Mac), and explaining this to users who sometimes have trouble even clicking the mouse at all is no one's idea of fun.

Better Select module overrides all multi-select HTML elements in Drupal and replaces them with checkboxes, in an auto-scrolling div so they don't take up much room on the page.

## [Block ARIA Landmark Roles](http://drupal.org/project/block_aria_landmark_roles)

7.x-1.4    2012-11-18  
7.x-1.x-dev    2015-05-07

Inspired by Block Class, this module adds additional elements to the block configuration forms that allow users to assign a ARIA landmark role to a block.

## [Text Resize](http://drupal.org/project/text_resize) \*

The [Text Resize module](http://drupal.org/project/text_resize) provides your end-users with a block that can be used to quickly change the font size of text on your Drupal site. The block includes two buttons that can increase and decrease the printed text on the page. This module is primarily focused on increasing the accessibility of your pages, by helping visually-impaired users to adjust the text size so that it is most comfortable for their eyesight.

## [Text Size](http://drupal.org/project/textsize) \*

The [Text Size module](http://drupal.org/project/textsize) provides your end-users with a block that can be used to quickly change the font size of text using a drop-down menu with relative percentages. Like Text Resize, this module is primarily focused on increasing the accessibility of your pages, by helping visually-impaired users to adjust the text size so that it is most comfortable for their eyesight. No JavaScript required (WCAG/BITV 6.3). The module can use simply the images/[templates](http://www.zwahlendesign.ch/textsize) designed for the Text Size module.

**\* Note regarding the Text Resize and the Text Size modules:**  
There is some debate as to whether or not text resize icons are actually just an unnecessary crutch for inexperienced users. All modern browsers do a great job of resizing the text, eliminating the need for resize icons stuck in some semi-accessible corner of your webpages. Instead of using those modules, you could inform your users on how to use their browser's built-it functionalities. Typically, they would need to hold down 'control' keyboard key ("Ctrl"), and then, either spin the mouse wheel, or click the keys 'plus' (+) or 'minus' (-). Browser addons are also an option, for example, Firefox addon 'NoSquint Plus' for zooming is great for one-handed mouse-only browsing.

## [Switchtheme](http://drupal.org/project/switchtheme)

7.x-1.0    2011-01-07

The [Switchtheme module](http://drupal.org/project/switchtheme) adds a block to allow users to switch between enabled themes. Themes can be given 'user friendly' names and access can be controlled by user role.

## [Page Style](http://drupal.org/project/pagestyle)

7.x-1.0    2011-01-05  
7.x-1.x-dev    2016-05-14

The [Page Style module](http://drupal.org/project/pagestyle) displays a style changer in a block and in the browser for better web accessibility. Switch between black/white, white/black, yellow/blue & standard displays of almost any site. No JavaScript required (WCAG/BITV 6.3).

## [High contrast](http://drupal.org/project/high_contrast)

7.x-1.3    2016-06-12

Provides a quick solution to allow the user to switch between the active theme and a high contrast version of it.

## [htmLawed](http://drupal.org/project/htmlawed)

7.x-3.     2016-02-11

The htmLawed module enables the use of the [htmLawed (X)HTML filter/purifier PHP script](http://www.bioinformatics.org/phplabware/internal_utilities/htmLawed/index.php) as an input filter with input format-, content (node) type- and body/comment/teaser-specific configurations.

## [HTML Purifier](http://drupal.org/project/htmlpurifier)

7.x-1.0    2012-11-03  
7.x-2.x-dev    2016-08-29

[HTML Purifier](http://htmlpurifier.org/) is a standards-compliant HTML filter library. HTML Purifier will not only remove all malicious code (better known as XSS) with a thoroughly audited, secure, yet permissive whitelist, it will also make sure your documents are standards compliant, something only achievable with a comprehensive knowledge of W3C's specifications.

## [HTML Tidy](http://drupal.org/project/htmltidy)

7.x-1.0-beta2    2012-07-04

This module tidies Drupal's HTML output with [HTML Tidy](http://en.wikipedia.org/wiki/HTML_Tidy) by optionally sanitizing it when it is saved or when it is displayed, like a traditional input formatter. Missing and mis-ordered tag components are replaced and reordered automatically so that user input doesn't break site structure with open tags and the like.

For more information about these modules see [the accessibility group wiki page](http://groups.drupal.org/node/85199).
