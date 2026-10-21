---
title: "File API"
source_url: "https://www.drupal.org/docs/7/api/file-api"
page_type: guide
published: "2016-10-14T20:52:32+00:00"
modified: "2018-02-19T07:18:56+00:00"
breadcrumb: ["Drupal 7", "Drupal 7 APIs"]
fetched: "2026-10-21T07:55:05Z"
raw: "raw/docs/7/api/file-api.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# File API

Documentation for File API in Drupal 7.

## [File API overview](/docs/7/api/file-api/file-api-overview)

The Drupal 7 File API provides an abstraction layer for accessing virtually any type of resource as a normal file.

## [File usage functions](/docs/7/api/file-api/file-usage-functions)

One of the things to think about when using the Drupal 7 File API is the new file_usage\_\* functions. These provide a way for modules to

## [General concepts](/docs/7/api/file-api/general-concepts)

The Drupal File API leverages PHP stream wrappers allowing virtually any type of resource to be represented as a normal file. This is a

## [Important Drupal 7 File API Functions](/docs/7/api/file-api/important-drupal-7-file-api-functions)

All the File API functions are at http://api.drupal.org/api/drupal/includes--file.inc/7, but it can be hard to sort out which ones you

## [Writing stream wrappers](/docs/7/api/file-api/writing-stream-wrappers)

This document will first discuss the implementation of a simple local stream wrapper, similar to the public wrapper included with Drupal

## [File API changes from Drupal 6 to Drupal 7](/docs/7/api/file-api/file-api-changes-from-drupal-6-to-drupal-7)

There are three key and pervasive things that happened to the File API between Drupal 6 and Drupal 7:
