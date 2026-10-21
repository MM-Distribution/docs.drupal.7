---
title: "Theming Drupal 7"
source_url: "https://www.drupal.org/docs/7/theming"
page_type: guide
published: "2016-08-31T13:52:31+00:00"
modified: "2026-02-24T08:09:04+00:00"
breadcrumb: ["Drupal 7"]
fetched: "2026-10-21T06:00:40Z"
raw: "raw/docs/7/theming.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Theming Drupal 7

This guide covers **Drupal 7 (Legacy)**. For the most recent standards and best practices, see the modern guide version: [**Theming Drupal 8+**](https://www.drupal.org/docs/develop/theming-drupal)

Theming guide for Drupal 7.

## [Overview of theme files](/docs/7/theming/overview-of-theme-files)

A theme is a collection of files that define the presentation layer. You can also create one or more "sub-themes" or variations on a theme.

## [Writing theme .info files](/docs/7/theming/writing-theme-info-files)

The .info file is a static text file for defining and configuring a theme. Each line in the .info file is a key-value pair with the key on

## [Default .info values](/docs/7/theming/default-info-values)

The following are the assumed defaults. When they are not defined, the theme will automatically take these values.

## [Assigning content to regions](/docs/7/theming/assigning-content-to-regions)

If none are defined, the following values are assumed in Drupal 6 and Drupal 7.

## [Checking if a region is occupied](/docs/7/theming/checking-if-a-region-is-occupied)

While theming page.tpl.php it's possible to check whether a region is empty, by checking the content of the relevant variable which

## [Theme settings](/docs/7/theming/theme-settings)

Various page elements output by the theme can be toggled on and off on the theme's configuration page.

## [Global settings](/docs/7/theming/global-settings)

The global settings a theme has

## [Integration with the Color module](/docs/7/theming/integration-with-the-color-module)

The Color module allows to change the theme color scheme.

## [Creating a sub-theme](/docs/7/theming/creating-a-sub-theme)

Sub-themes are just like any other theme, with one difference: They inherit the parent theme's resources. There are no limits on the

## [Clearing the theme cache](/docs/7/theming/clearing-the-theme-cache)

The contents of the .info file is cached in the database, so altering it will not be noticed by Drupal. Also if you add new tpl.php files or

## [Sub Theme - Inheritance Summary](/docs/7/theming/sub-theme-inheritance-summary)

In the previous section, we understood how a sub theme is created along with inheritance of various properties. The table summarises

## [Example: creating a Garland sub-theme that utilizes the Color module](/docs/7/theming/example-creating-a-garland-sub-theme-that-utilizes-the-color-module)

A Garland sub-theme that utilizes the Color module

## [Working with CSS](/docs/7/theming/working-with-css)

Working with CSS in Drupal 7.

- [CSS overview](/docs/7/theming/working-with-css/css-overview)
- [Overriding style sheets from modules and base themes](/docs/7/theming/working-with-css/overriding-style-sheets-from-modules-and-base-themes)
- [Adding style sheets](/docs/7/theming/working-with-css/adding-style-sheets-from-info-files)
- [Adding CSS to form or page with attachments](/docs/7/theming/working-with-css/adding-css-to-form-or-page-with-attachments)
- [Adding styles through the API](/docs/7/theming/working-with-css/adding-styles-through-the-api)
- [Live_css with .less support](/docs/7/theming/working-with-css/live_css-with-less-support)
- [Sass techniques and tools](/docs/7/theming/working-with-css/sass-techniques-and-tools)
- [Standard Drupal core styles and classes](/docs/7/theming/working-with-css/standard-drupal-core-styles-and-classes)
- [.clear-block and .clearfix](/docs/7/theming/working-with-css/using-clearfix)
- [Supporting "right to left" (RTL) languages](/docs/7/theming/working-with-css/supporting-right-to-left-rtl-languages)

## [Working with JavaScript and jQuery](/docs/7/theming/working-with-javascript-and-jquery)

Using JavaScript adds dynamic presentation effects to a theme. In addition to custom JavaScript files many Drupal developers find jQuery

## [Using Newer Versions of jQuery](/docs/7/theming/using-newer-versions-of-jquery)

You will often need a newer version of jQuery to use a certain jQuery plugin. There are several ways to achieve this.

## [Core templates](/docs/7/theming/core-templates)

Core comes with a number of default template files. You can override these templates in a number of ways.

## [Template (theme hook) suggestions](/docs/7/theming/template-theme-hook-suggestions)

A theme hook suggestion is an alternate template (.tpl.php) file that you have created to override the base or original template file.

## [Theming blocks](/docs/7/theming/theming-blocks)

Theming blocks in Drupal 7 individually, by region, or by module.

## [Advanced theming](/docs/7/theming/advanced)

Advanced theming in Drupal 7.

- [Creating advanced theme settings](/docs/7/theming/advanced/creating-advanced-theme-settings)
- [Theming forms in your theme](/docs/7/theming/advanced/theming-forms-in-your-theme)
- [Theming Custom Entities](/docs/7/theming/advanced/theming-custom-entities)
- [Adding browser-specific style sheets](/docs/7/theming/advanced/adding-browser-specific-style-sheets)

## [Overriding themable output](/docs/7/theming/overriding-themable-output)

Overriding themable output in Drupal 7.

- [Overriding themable output](/docs/7/theming/overriding-themable-output/overriding-themable-output)
- [Beginners guide to overriding themable output](/docs/7/theming/overriding-themable-output/beginners-guide-to-overriding-themable-output)
- [Introduction to PHP for theming](/docs/7/theming/overriding-themable-output/introduction-to-php-for-theming)
- [About overriding themable output](/docs/7/theming/overriding-themable-output/about-overriding-themable-output)
- [Setting up variables for use in a template (preprocess and process functions)](/docs/7/theming/overriding-themable-output/setting-up-variables-for-use-in-a-template-preprocess-and)
- [Default baseline variables](/docs/7/theming/overriding-themable-output/default-baseline-variables)
- [Customizing and Overriding User Login page, Register, and Password Reset in Drupal 6 and 7](/docs/7/theming/overriding-themable-output/customizing-and-overriding-user-login-page-register-and)
- [How to add a "?destination=URL" to the request new password link](/docs/7/theming/overriding-themable-output/how-to-add-a-destinationurl-to-the-request-new-password)
- [Useful tutorials & links](/docs/7/theming/overriding-themable-output/useful-tutorials-links)
- [Example: Themable output](/docs/7/theming/overriding-themable-output/example-themable-output)
- [Identifying Core Components](/docs/7/theming/overriding-themable-output/identifying-core-components)
- [Core Block CSS IDs](/docs/7/theming/overriding-themable-output/core-block-css-ids)
- [Mission statement and highlighted region](/docs/7/theming/overriding-themable-output/mission-statement-and-highlighted-region)
- [Primary and Secondary links renamed to Main and Secondary menu](/docs/7/theming/overriding-themable-output/primary-and-secondary-links-renamed-to-main-and-secondary)
- [Taxonomy](/docs/7/theming/overriding-themable-output/taxonomy)
- [Unrendered taxonomy links no longer available as a separate variable in node.tpl.php files](/docs/7/theming/overriding-themable-output/unrendered-taxonomy-links-no-longer-available-as-a)
- [Menu theming](/docs/7/theming/overriding-themable-output/menu-theming)
- [Overriding a menu in a block or template file](/docs/7/theming/overriding-themable-output/overriding-a-menu-in-a-block-or-template-file)
- [The theme registry for special cases](/docs/7/theming/overriding-themable-output/the-theme-registry-for-special-cases)
- [Working with template suggestions](/docs/7/theming/overriding-themable-output/working-with-template-suggestions)
- [Architectural view of theming](/docs/7/theming/overriding-themable-output/architectural-view-of-theming)

## [Creating accessible themes](/docs/7/theming/creating-accessible-themes)

This guide provides a guide to accessibility best practices for theme developers.

- [Accessibility principles](/docs/7/creating-accessible-themes/accessibility-principles)
- [Building accessible forms](/docs/7/creating-accessible-themes/building-accessible-forms)
- [Contributed modules to help with accessibility](/docs/7/creating-accessible-themes/contributed-modules-to-help-with-accessibility)
- [Creating accessible site and page navigation](/docs/7/creating-accessible-themes/creating-accessible-site-and-page-navigation)
- [Creating accessible structure and markup](/docs/7/creating-accessible-themes/creating-accessible-structure-and-markup)
- [Getting started with accessibility](/docs/7/creating-accessible-themes/getting-started-with-accessibility)
- [Hide content properly](/docs/7/creating-accessible-themes/hide-content-properly)
- [Improving readability with fonts and typography](/docs/7/creating-accessible-themes/improving-readability-with-fonts-and-typography)
- [Maintaining accessibility in rich Internet applications and Javascript/Ajax features](/docs/7/creating-accessible-themes/maintaining-accessibility-in-rich-internet-applications-and)
- [Managing images and media for accessibility](/docs/7/creating-accessible-themes/managing-images-and-media-for-accessibility)
- [Providing Useful Alternative Text for Images](/docs/7/creating-accessible-themes/providing-useful-alternative-text-for-images)
- [Providing a way to skip navigation](/docs/7/creating-accessible-themes/providing-a-way-to-skip-navigation)
- [Specifying colors and contrast for accessibility](/docs/7/creating-accessible-themes/specifying-colors-and-contrast-for-accessibility)
- [Tools for validating accessibility](/docs/7/creating-accessible-themes/tools-for-validating-accessibility)
- [Using headings to improve accessibility](/docs/7/creating-accessible-themes/using-headings-to-improve-accessibility)

## [Theming HowTos](/docs/7/theming/howto)

Theming HowTos for Drupal 7.

- [Change the favicon](/docs/7/theming/howto/change-the-favicon)
- [Clearing floats with class="clear-block"](/docs/7/theming/howto/clearing-floats-with-classclearfix)
- [Convert any website layout or template into a Drupal theme - easily!](/docs/7/theming/howto/convert-any-website-layout-or-template-into-a-drupal-theme-easily)
- [Create a Views event list grouped by month](/docs/7/theming/howto/create-a-views-event-list-grouped-by-month)
- [Create a new custom theme with CSS alone](/docs/7/theming/howto/create-a-new-custom-theme-with-css-alone)
- [Customize Drupal User Profiles with CiviCRM Contact Fields](/docs/7/theming/howto/customize-drupal-user-profiles-with-civicrm-contact-fields)
- [Customize the User Edit page in Drupal 7 - an example](/docs/7/theming/howto/customize-the-user-edit-page-in-drupal-7-an-example)
- [Customize the front page template](/docs/7/theming/howto/customize-the-front-page-template)
- [Customizing core and/or contributed themes](/docs/7/theming/howto/customizing-core-andor-contributed-themes)
- [Enable submit via Enter key on Ajax forms](/docs/7/theming/howto/enable-submit-via-enter-key-on-ajax-forms)
- [How to edit ALT tag on your site logo](/docs/7/theming/howto/how-to-edit-alt-tag-on-your-site-logo)
- [Overriding Theme Templates in Drupal 6 and 7](/docs/7/theming/howto/overriding-theme-templates-in-drupal-7)
- [Put an HTML non breaking space (&nbsp;) in menu items titles](/docs/7/theming/howto/put-an-html-non-breaking-space-%C2%A0-in-menu-items-titles)
- [Rounded Corners in Drupal 7 (jquery corner)](/docs/7/theming/howto/rounded-corners-in-drupal-7-jquery-corner)
- [Show a block depending on node type and node id](/docs/7/theming/howto/show-a-block-depending-on-node-type-and-node-id)
- [Static and Dynamic Thumbnails for Facebook](/docs/7/theming/howto/static-and-dynamic-thumbnails-for-facebook)
- [Style a horizontal login block in the footer](/docs/7/theming/howto/style-a-horizontal-login-block-in-the-footer)
- [Theming Web-Form](/docs/7/theming/howto/theming-web-form)

## [Tools and best practices](/docs/7/theming/tools-and-best-practices)

Best practices and conventions for theming Drupal 7.

- [Safe theme development](/docs/7/theming/tools-and-best-practices/safe-theme-development)
- [Theme coding conventions](/docs/7/theming/tools-and-best-practices/theme-coding-conventions)
- [Theming the Drupal maintenance page](/docs/7/theming/tools-and-best-practices/theming-the-drupal-maintenance-page)
- [Adding your theme to Drupal.org](/docs/7/theming/tools-and-best-practices/adding-your-theme-to-drupalorg)
- [Cross-browser testing](/docs/7/theming/tools-and-best-practices/cross-browser-testing)
- [Recommended target browsers](/docs/7/theming/tools-and-best-practices/recommended-target-browsers)
- [Creating a screenshot for the appearance page](/docs/7/theming/tools-and-best-practices/creating-a-screenshot-for-the-appearance-page)
- [Creating a screenshot for the administration page](/docs/7/theming/tools-and-best-practices/creating-a-screenshot-for-the-administration-page)
- [Making your theme semantically correct](/docs/7/theming/tools-and-best-practices/making-your-theme-semantically-correct)
- [Doctype, XML, and XHTML](/docs/7/theming/tools-and-best-practices/doctype-xml-and-xhtml)
- [Feature detection](/docs/7/theming/tools-and-best-practices/feature-detection)
- [Installing Modernizr module and JavaScript library](/docs/7/theming/tools-and-best-practices/installing-modernizr-module-and-javascript-library)
- [Creating a custom build of Modernizr based on your Drupal setup](/docs/7/theming/tools-and-best-practices/creating-a-custom-build-of-modernizr-based-on-your-drupal)
- [Modernizr.load() and Drupal: Basics](/docs/7/theming/tools-and-best-practices/modernizrload-and-drupal-basics)
- [Implementing the Modernizr Test API within a module or theme](/docs/7/theming/tools-and-best-practices/implementing-the-modernizr-test-api-within-a-module-or-theme)

## [Upgrading 6.x themes to 7.x](/docs/7/theming/upgrading-6x-themes-to-7x)

NOTE: We are now using a different system to track version-to-version changes in Drupal. Most of the theme changes between Drupal 6 and
