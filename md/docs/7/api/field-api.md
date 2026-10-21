---
title: "Field API"
source_url: "https://www.drupal.org/docs/7/api/field-api"
page_type: guide
published: "2016-10-14T20:55:37+00:00"
modified: "2018-02-19T07:18:04+00:00"
breadcrumb: ["Drupal 7", "Drupal 7 APIs"]
fetched: "2026-10-21T07:54:50Z"
raw: "raw/docs/7/api/field-api.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Field API

Documentation for Field API in Drupal 7.

## [Field API glossary](/docs/7/api/field-api/field-api-glossary)

## [Adding and reusing a field](/docs/7/api/field-api/adding-and-reusing-a-field)

Let's begin with creating a last name field. We will add this to users and to the 'picture' node type so that it's possible to put names on

## [Field API tutorial](/docs/7/api/field-api/field-api-tutorial)

In previous Drupal versions, most modules defined their own tables, handled writing and reading data from tables, managed data entry and

## [Field Types and Settings](/docs/7/api/field-api/field-types-and-settings)

There are a defined number of field types in use, and each type has its own available settings (links below are to API HOOK_field_info()

## [Implementing entity revisioning](/docs/7/api/field-api/implementing-entity-revisioning)

Entity revisioning is fairly simple - most of it is handled by field API, so you just need to implement a revision table, and appropriate

## [Making an entity fieldable](/docs/7/api/field-api/making-an-entity-fieldable)

There are a number of hooks involved in making an entity fieldable. hook_entity_info provides the info (surprise!):

## [Implementing the field management UI](/docs/7/api/field-api/implementing-the-field-management-ui)

The field_ui module has a built in field management system for your entity bundles. Enabling this system for your entity is a relatively

## [Language support for entity fields](/docs/7/api/field-api/language-support-for-entity-fields)

About multilingual fields
