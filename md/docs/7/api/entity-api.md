---
title: "Entity API"
source_url: "https://www.drupal.org/docs/7/api/entity-api"
page_type: guide
published: "2016-10-14T21:19:35+00:00"
modified: "2018-02-19T07:17:21+00:00"
breadcrumb: ["Drupal 7", "Drupal 7 APIs"]
fetched: "2026-10-21T07:54:34Z"
raw: "raw/docs/7/api/entity-api.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Entity API

This guide includes best practices and documentation for working with entities in Drupal.

Drupal 7 core has the following functions in files:

- [/includes/entity.inc](http://api.drupal.org/api/drupal/includes%21entity.inc/7)
- [hook_entity\_\* of /includes/system.api.php](http://api.drupal.org/api/drupal/modules%21system%21system.api.php)

These functions provide limited functionality for Entity usage. However, developers who want to develop using the Entity concept usually utilize the contributed module [Entity API](http://drupal.org/project/entity).

## [An Introduction to Entities](/docs/7/api/entity-api/an-introduction-to-entities)

If you are looking for the documentation or the entity API in Drupal 8, click here.

## [Entity API Tutorial](/docs/7/api/entity-api/entity-api-tutorial)

This is the developer documentation for the Entity API module. Also check the README.

## [Entity Token Support](/docs/7/api/entity-api/entity-token-support)

Drupal 7

## [Providing a new entity type](/docs/7/api/entity-api/providing-a-new-entity-type)

The Entity CRUD API allows you to easily create a new entity type. You'll get full Create, Read, Update, Delete and Index (CRUDI) functions,

## [Make an entity type exportable](/docs/7/api/entity-api/make-an-entity-type-exportable)

If your entity could be considered a site configuration, it is usually a good idea to make it exportable.

## [Making an entity revisionable](/docs/7/api/entity-api/making-an-entity-revisionable)

Requires entity version 7.x-1.0 or greater

## [Enabling Revisions on a Table With Existing Data](/docs/7/api/entity-api/enabling-revisions-on-a-table-with-existing-data)

Overview

## [Viewing entities](/docs/7/api/entity-api/viewing-entities)

The entity API assists in writing the code for viewing an entity by providing entity_build_content() and entity_view() functions which take

## [Module integration helpers](/docs/7/api/entity-api/module-integration-helpers)

The entity API provides some useful defaults for integrating with Rules and for providing Entity property information. If your entity type

## [i18n module integration](/docs/7/api/entity-api/i18n-module-integration)

There is a i18n controller for integration (exportable) entities with the i18n module. However, the controller requires some additional code

## [Making use of the admin UI](/docs/7/api/entity-api/making-use-of-the-admin-ui)

Optionally, the entity API helps provide an administrative interface for managing entities, e.g. the UI for managing profile types of the

## [Documentation template for provided hooks](/docs/7/api/entity-api/documentation-template-for-provided-hooks)

The Entity API implements hooks for any entity types implemented with the provided controller. To make developers aware of this hooks, it's

## [Basic file skeleton + CRUD hooks](/docs/7/api/entity-api/basic-file-skeleton-crud-hooks)

Values to replace:

## [View-related hooks.](/docs/7/api/entity-api/view-related-hooks)

If your module makes use of entity_view(), add the following view-related hooks:

## [Additional hooks for exportable entities](/docs/7/api/entity-api/additional-hooks-for-exportable-entities)

Values to replace:

## [Misc hooks](/docs/7/api/entity-api/misc-hooks)

If your module implements an entity form with the help of entity_ui_get_form(), the following template helps you documenting the according

## [Providing metadata for additional entity types](/docs/7/api/entity-api/providing-metadata-for-additional-entity-types)

In case your module is providing an additional entity type, but is not making use of the Entity CRUD API (as described previously) some

## [Views integration](/docs/7/api/entity-api/views-integration)

Entity API tries to generate suitable Views integration for the entity based upon:

## [Entity property information](/docs/7/api/entity-api/entity-property-information)

For a general introduction of metadata about entity properties and its purpose, check this blog post.

## [Data types](/docs/7/api/entity-api/data-types)

These are the data types to be used for describing entity properties:

## [Entity metadata wrappers](/docs/7/api/entity-api/entity-metadata-wrappers)

Table of contents

## [Property info for fields](/docs/7/api/entity-api/property-info-for-fields)

Fields are added in automatically by the Entity API module, as long as the field type is supported. However, the module providing the field

## [Displaying properties when viewing entities](/docs/7/api/entity-api/displaying-properties-when-viewing-entities)

When an entity is viewed, the EntityAPIController calls the buildContent() method to assemble the entity information, entity's field data
