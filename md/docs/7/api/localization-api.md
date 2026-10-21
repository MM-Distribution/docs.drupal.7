---
title: "Localization API"
source_url: "https://www.drupal.org/docs/7/api/localization-api"
page_type: guide
published: "2016-10-13T19:58:05+00:00"
modified: "2018-02-19T07:20:15+00:00"
breadcrumb: ["Drupal 7", "Drupal 7 APIs"]
fetched: "2026-10-21T07:55:37Z"
raw: "raw/docs/7/api/localization-api.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Localization API

Documentation about Localization API in Drupal 8.

## [Localization API overview](/docs/7/api/localization-api/localization-api-overview)

Drupal makes it easy to develop translatable interfaces.

## [When to use st(), t() and get_t() in install and update functions](/docs/7/api/localization-api/when-to-use-st-t-and-get_t-in-install-and-update-functions)

Drupal does not have access to a database in the early stages of the installation process, so any interface strings which might be generated

## [Dynamic strings with placeholders](/docs/7/api/localization-api/dynamic-strings-with-placeholders)

The t() function family not only allows you to translate simple strings. It is possible that you need a variable component in the string: a

## [Dynamic or static links and HTML in translatable strings](/docs/7/api/localization-api/dynamic-or-static-links-and-html-in-translatable-strings)

The general rule of thumb for translatable strings is that we keep inline markup for translation but avoid block tags (but do read the whole

## [Formatting numbers, dates/times, sizes and intervals with localization](/docs/7/api/localization-api/formatting-numbers-datestimes-sizes-and-intervals-with-localization)

While t() can translate strings from one language to another, there are cases where we must display item counts, dates/times, etc. Drupal

## [Strings at well-known places: built-in menus, permissions, log messages and .info files](/docs/7/api/localization-api/strings-at-well-known-places-built-in-menus-permissions-log-messages-and)

As with format_plural(), Drupal has functions where you don't explicitly use t(), but the provided strings are still translated. In some

## [Translating strings in JavaScript](/docs/7/api/localization-api/translating-strings-in-javascript)

The JavaScript library shipped with Drupal 6 includes ports of the t() and format_plural() functions, for formatting and translating strings

## [Language Negotiation API](/docs/7/api/localization-api/language-negotiation-api)

It is possible to customize the language negotiation process both for how we detect the user's language and also on what type of data they

## [String context](/docs/7/api/localization-api/string-context)

Note: This handbook page is under discussion, see \[#1035716\]
