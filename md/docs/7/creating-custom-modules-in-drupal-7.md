---
title: "Creating custom modules in Drupal 7"
source_url: "https://www.drupal.org/docs/7/creating-custom-modules-in-drupal-7"
page_type: guide
published: "2016-09-21T17:38:07+00:00"
modified: "2026-02-24T08:15:55+00:00"
breadcrumb: ["Drupal 7"]
fetched: "2026-10-21T07:20:39Z"
raw: "raw/docs/7/creating-custom-modules-in-drupal-7.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Creating custom modules in Drupal 7

This guide covers **Drupal 7 (Legacy)**. For the most recent standards and best practices, see the modern guide version: **[Creating modules for Drupal 8 and later](https://www.drupal.org/docs/develop/creating-modules)**

This guide includes tutorials and other information that you need to create modules for Drupal 7.

Other helpful resources:

- [API reference](https://api.drupal.org/api/drupal/7)
- [Coder module](https://www.drupal.org/project/coder)

## [Getting started](/docs/7/creating-custom-modules/getting-started)

Main topic described: module file name and location

## [Telling Drupal about your module](/docs/7/creating-custom-modules/telling-drupal-about-your-module)

Main topic described: .info files

## [Writing module .info files (Drupal 7.x)](/docs/7/creating-custom-modules/writing-module-info-files-drupal-7x)

Overview

## [Creating Drupal 7 hooks](/docs/7/creating-custom-modules/creating-drupal-7-hooks)

The Drupal 7 Hook Concept

## [Writing comments and implementing your first hook](/docs/7/creating-custom-modules/writing-comments-and-implementing-your-first-hook)

Drupal hook described: hook_help()

## [Writing .install files (Drupal 7.x)](/docs/7/creating-custom-modules/writing-install-files-drupal-7x)

This page is about Drupal 7. For Drupal 6, see Writing .install files, (Drupal 6.x).

## [Declaring the block](/docs/7/creating-custom-modules/declaring-the-block)

Drupal hook described: hook_block_info()

## [Retrieving data](/docs/7/creating-custom-modules/retrieving-data)

Main topic described: Database API

## [Generating block content](/docs/7/creating-custom-modules/generating-block-content)

Drupal hook described: hook_block_view()

## [Testing and troubleshooting the module](/docs/7/creating-custom-modules/testing-and-troubleshooting-the-module)

It's time to enable and fully test your module!

## [Preparing for a module configuration form](/docs/7/creating-custom-modules/preparing-for-a-module-configuration-form)

Drupal hook described: hook_menu()

## [Creating the configuration form](/docs/7/creating-custom-modules/creating-the-configuration-form)

Main topic described: Form API

## [Validating the data](/docs/7/creating-custom-modules/validating-the-data)

Main topic described: Form API

## [Specifying a custom permission for a new page](/docs/7/creating-custom-modules/specifying-a-custom-permission-for-a-new-page)

Drupal hooks described: hook_permission(), hook_menu()

## [Adapting the query](/docs/7/creating-custom-modules/adapting-the-query)

Main topic described: Database API

## [Theming the page](/docs/7/creating-custom-modules/theming-the-page)

Main topic described: Render API

## [Adding a 'More' link](/docs/7/creating-custom-modules/adding-a-more-link)

Main topic described: Block system, Render arrays, Menu system

## [Testing with SimpleTest](/docs/7/creating-custom-modules/testing-with-simpletest)

Main topic described: SimpleTest, Assertions

## [Practicing patches](/docs/7/creating-custom-modules/practicing-patches)

Main topic described: Git

## [Show all errors while developing](/docs/7/creating-custom-modules/show-all-errors-while-developing)

Set Drupal to show all errors when developing your module.

## [Drupal 7's code registry](/docs/7/creating-custom-modules/drupal-7s-code-registry)

Drupal 7 introduces a code registry - an inventory of all classes and interfaces for all enabled modules and Drupal's core files. The

## [Exportable configuration](/docs/7/creating-custom-modules/exportable-configuration)

If your module includes data structures that could be considered site configuration, you will probably want to make that data exportable so

## [Suppress caching (for development) or to use an external page cache](/docs/7/creating-custom-modules/suppress-caching-for-development-or-to-use-an-external-page-cache)

This instruction is for Drupal 7 read about disabling caching in Drupal 8

## [Using the theme layer (Drupal 7.x)](/docs/7/creating-custom-modules/using-the-theme-layer-drupal-7x)

A well-made Drupal module allows all elements of its presentation to be overridden by the theme of the site on which it is used. In order

## [Drupal 6/7 programming from an object-oriented perspective](/docs/7/creating-custom-modules/drupal-67-programming-from-an-object-oriented-perspective)

Note: This page is about Drupal 7's (and prior versions') architecture. Drupal 8 changed a great deal and now uses actual OOP practices.

## [Making your custom data translatable](/docs/7/creating-custom-modules/making-your-custom-data-translatable)

When developing a module, you should give some consideration to making the text your module displays translatable into other languages. An

## [Module development HowTos](/docs/7/creating-custom-modules/howtos)

Drupal 7 module development tutorials.

- [Examples for database update scripts using hook_update_N (how to do one time configuration programmatically)](/docs/7/creating-custom-modules/howtos/examples-for-database-update-scripts-using-hook_update_n-how)
- [How to add a column with dynamically generated action buttons in a View](/docs/7/creating-custom-modules/howtos/how-to-add-a-column-with-dynamically-generated-action-buttons)
- [How to change a field value](/docs/7/creating-custom-modules/howtos/how-to-change-a-field-value)
- [How to connect to multiple databases within Drupal](/docs/7/creating-custom-modules/howtos/how-to-connect-to-multiple-databases-within-drupal)
- [How to integrate UUID with third party entities](/docs/7/creating-custom-modules/howtos/how-to-integrate-uuid-with-third-party-entities)
- [How to integrate with the Stripe module](/docs/7/creating-custom-modules/howtos/how-to-integrate-with-the-stripe-module)
- [How to make configuration objects exportable with CTools](/docs/7/creating-custom-modules/howtos/how-to-make-configuration-objects-exportable-with-ctools)
- [How to rebuild node_comment_statistics](/docs/7/creating-custom-modules/howtos/how-to-rebuild-node_comment_statistics)
- [How to update a module's weight](/docs/7/creating-custom-modules/howtos/how-to-update-a-modules-weight)
- [How to use EntityFieldQuery](/docs/7/creating-custom-modules/howtos/how-to-use-entityfieldquery-for-drupal-7)
- [Paging non-SQL data](/docs/7/creating-custom-modules/howtos/paging-non-sql-data)
- [Using template (.tpl.php) files in your own module](/docs/7/creating-custom-modules/howtos/using-template-files-in-your-own-module)

## [Understanding the hook system for Drupal modules](/docs/7/creating-custom-modules/understanding-the-hook-system-for-drupal-modules)

A Drupal module is a collection of files containing some functionality and is written in PHP. Because the module code executes within the

## [Working with multilingual content](/docs/7/creating-custom-modules/working-with-multilingual-content)

As of Drupal 6, the core content translation module enables multilingual content.
