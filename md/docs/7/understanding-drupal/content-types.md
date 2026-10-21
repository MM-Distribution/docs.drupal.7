---
title: "Content types"
source_url: "https://www.drupal.org/docs/7/understanding-drupal/content-types"
page_type: page
last_updated: "Last updated on 3 November 2016"
published: "2005-05-04T05:54:40+00:00"
modified: "2016-11-03T15:23:22+00:00"
breadcrumb: ["Drupal 7", "Understanding Drupal 7"]
fetched: "2026-10-21T05:50:36Z"
raw: "raw/docs/7/understanding-drupal/content-types.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Content types

A single web site could contain many types of content, such as informational pages, news items, polls, blog posts, real estate listings, etc. In Drupal, each item of content is called a *node*, and each node belongs to a single *content type*, which defines various default settings for nodes of that type, such as whether the node is published automatically and whether comments are permitted. (Note that in previous versions of Drupal, content types were known as *node types*.)

When you first install Drupal with the default installation profile (in contrast to the *minimal* installation profile), you will have two *content types* defined: "Article" and "Basic page". When you enable other core and contributed modules ([by visiting Modules](/project/modules)), you will find that you have other content types available; you can also create your own content types (see below).

## Content types

### Article

The *Article* content type (formerly, "story") is enabled in Drupal in the default installation profile. Articles are generally used for information that is updated more frequently and often cross-referenced and categorized (such as news items or resources). By default, Articles are sorted with the most recent post at the top, but this can be customized with contributed modules like [Views](/project/views).

### Basic page

The *Basic page* content type is enabled in Drupal in the default installation profile. Typically Basic pages are used for static content that can (but are not required to) be linked into the main navigation bar. This is one of the most "basic" content types and can be very flexible.

### [Blog Entry](/handbook/modules/blog)

The *Blog* (short for weblog) content type was removed in Drupal 8. It is an online journal or diary, and [Blog module](/project/blog) allows registered users on your site to create their own blogs. Each entry in a user blog has content type *Blog Entry*.

### [Book Page](/handbook/modules/book)

*Book pages* are designed to be part of a collaborative book, enabled by the core Book module. An example of a collaborative book is the [Drupal developer documentation](/node/316). In older versions of Drupal, only nodes of content type Book Page could be added to a book. However, since Drupal 7 nodes of any content type can be part of a book.

### [Forum topic](/handbook/modules/forum)

A *Forum topic* defines a topic for a forum discussion; people can reply to the topic by using comments. Forum nodes are organized into subject areas via a Taxonomy (list of categories).

### [Poll](/handbook/modules/poll)

A *poll* is a question with a set of possible responses. Once created, a poll automatically provides a simple running count of the number of votes received for each response.

## Your own custom content type

You can create your own custom content types by going to *Administer \> Structure \> Content types \> Add content type*. For more information on how to create your own custom content type, [click here](https://www.drupal.org/docs/7/nodes-content-types-and-fields/create-a-custom-content-type).

There are two main reasons for creating your own content type. First, content types lets you organize your site more efficiently. For instance, you might have "Info" and "News flash" as two simple content types on your site, rather than just using "Article" for both. Additionally, creating your own content type means that you can create custom fields. These fields can appear as text boxes, select lists, check boxes, etc., providing extensive functionality to content on your site.

## Content types by contributed modules

Finally, contributed modules define their own content types. Check the [Download & Extend/Modules page](/project/modules) of the Drupal handbook for more information on locating an appropriate module for your needs.
