---
title: "About nodes"
source_url: "https://www.drupal.org/docs/7/nodes-content-types-and-fields/about-nodes"
page_type: page
last_updated: "Last updated on 24 May 2018"
published: "2005-05-09T19:24:05+00:00"
modified: "2018-05-24T16:00:26+00:00"
breadcrumb: ["Drupal 7", "Drupal 7 nodes, content types, and fields"]
fetched: "2026-10-21T07:05:40Z"
raw: "raw/docs/7/nodes-content-types-and-fields/about-nodes.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# About nodes

Most content on a Drupal website is stored and treated as "nodes". A node is any piece of individual content, such as a page, poll, article, forum topic, or a blog entry. Comments are not stored as nodes but are always connected to one. Treating all content as nodes allows the flexibility to create new types of content. It also allows you to painlessly apply new features or changes to all content of one type.

**Behind the scenes, the Node module manages these nodes. This module lets you:**

1.  List, sort through, and manage all the content on your site.
2.  Set defaults for how all posts are displayed.
3.  List and configure the "content types" for your site, and create new ones.

The ability to create different "content types" is a way Drupal allows you to have different kinds of nodes for different purposes. For example, an "article" is one content type, a "book page" is another, and a "blog entry" yet another. You can also create new content types of your own.

The Node module manages the creation, editing, deletion, settings, and display of the main site content. Content items managed by the Node module are typically displayed as pages on your site, and include a title, some meta-data (author, creation time, content type, etc.), and optional fields containing text or other data. (Fields are managed by the [Field module](/documentation/modules/field) in Drupal 7.)

Each node has an [unique ID](/node/624494).

## Uses

### Creating content

When new content is created, the Node module records basic information about the content, including the author, date of creation, and the content type. It also manages the *publishing options*, which define whether or not the content is published, promoted to the front page of the site, and/or sticky at the top of content lists. Default settings can be configured for each type of content on your site at *Administration \> Structure \> Content types \> \[Specific content type\]* or `http://example.com/admin/structure/types`.

### Creating custom content types

The Node module gives users with the *Administer content types* permission the ability to create new content types in addition to the default ones already configured. Creating custom content types allows you the flexibility to add and delete fields and configure default settings that suit the differing needs of various site content. To add new content types in Drupal 7, navigate to *Administration \> Structure \> Content Types \> Add content type* or `http://example.com/admin/structure/types/add`.

### Administering content

The Content administration page allows you to review and bulk manage your site content. To access this page in Drupal 7, navigate to *Administration \> Content* or `http://example.com/admin/content`.

### Creating revisions

The Node module also enables you to create multiple versions of any piece of content, and revert to older versions using the *Revision information* settings. You can review and revert revisions through the "Revisions" tab on any content, and add new ones in the "Revision information" settings when editing a given node.

### User permissions

The Node module makes a number of permissions available for each content type, which can be set by role on the permissions page (*Administration \> People \> Permissions tab* or `http://example.com/admin/people/permissions`).

For more useful materials on content administration in Drupal, see [Resource Guide: Tools for Content Administration in Drupal](/resource-guides/content-administration).
