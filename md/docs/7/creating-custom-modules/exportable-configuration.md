---
title: "Exportable configuration"
source_url: "https://www.drupal.org/docs/7/creating-custom-modules/exportable-configuration"
page_type: page
last_updated: "Last updated on 23 December 2016"
published: "2012-03-12T03:34:09+00:00"
modified: "2016-12-23T07:04:18+00:00"
breadcrumb: ["Drupal 7", "Creating custom modules in Drupal 7"]
fetched: "2026-10-21T07:26:54Z"
raw: "raw/docs/7/creating-custom-modules/exportable-configuration.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Exportable configuration

If your module includes data structures that could be considered site configuration, you will probably want to make that data exportable so that it can be stored and transferred between multiple sites. Adding exportables support will make it possible for site administrators to export data and import it into a different site. It will also allow data from your module to be included in [features](http://drupal.org/project/features), [apps](http://drupal.org/project/apps) and [distributions](http://drupal.org/documentation/build/distributions).

The good news is that solid APIs exist that make implementing exportables straightforward. It's a good idea to plan for exportables support early on in your module development process, as the main exportables APIs include extensive support for administrative UIs. By using one of these APIs, you can save a lot of coding that would be taken to produce custom admin forms and pages.

## Concepts in exportables: machine names, overrides, reverting, cloning

Familiar examples of exportable configuration are image styles and views. In Drupal 7, you can create an image style through the UI and then export it to be used on another site or included in the code of a module. Similarly, the Views module includes support for views to live in code or in the database.

To be exportable, a data object must be identifiable by a [machine name](http://drupal.org/node/1227546) instead or in addition to a numerical ID.

Typically, an exportable configuration can have a number of different states. Naming conventions vary a bit, but the basics include:

- **Default**: configuration that is stored in code.
- **Normal**: configuration that has been made through the UI and is stored in the site database.
- **Overridden**: configuration that exists in code (default) but has been edited via the UI and so also has a database version, which supersedes the original default version.

Exportables support typically includes the following actions:

- **Export**: Create a code representation of the item.
- **Import**: Add the item to the site based on a previous export.
- **Override**: Customize a code-based item, creating a database version.
- **Revert**: Delete database-level changes made to a code-based item.
- **Clone**: Create a new item based on the existing item.

## Exportables APIs

It's of course possible to implement custom exportables support in your module. But two proven and documented APIs exist in Drupal contrib that greatly facilitate the process.

- **Entity API exportables**. If your data is an [entity type](http://drupal.org/node/1260694), you can use the [Entity API](http://drupal.org/project/entity) module to make your data exportable. Documentation is available on [how to make an entity type exportable](http://drupal.org/node/1021526) and [making use of the admin UI](http://drupal.org/node/1021576) in Entity API. Modules that implement Entity API exportables include [Profile2](http://drupal.org/project/profile2).
- **CTools exportables**. [CTools](http://drupal.org/project/ctools) can be used to provide exportables support whether or not your data is an entity type. See [how to make configuration objects exportable with CTools](http://drupal.org/node/928026). Modules that implement CTools exportables include [Views](http://drupal.org/project/views).

## Exportables and Features

The Features module automates the process of exporting configuration to code. Features include a set of hooks that can be implemented to provide custom Features support. However, if you make your configuration exportable via the Entity API or CTools, your entities will automatically be recognized by Features and feature authors will be able to select them and add them to features. See the [Features documentation](http://drupal.org/node/580026) for more information.

## The future of exportables

In Drupal 8, configuration will be stored in code by default thanks to the work of the [configuration management initiative](http://groups.drupal.org/build-systems-change-management/cmi).
