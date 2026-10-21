---
title: "Viewing unpublished content"
source_url: "https://www.drupal.org/docs/7/managing-users/viewing-unpublished-content"
page_type: page
last_updated: "Last updated on 12 July 2022"
published: "2011-03-26T21:37:21+00:00"
modified: "2022-07-12T09:34:24+00:00"
breadcrumb: ["Drupal 7", "Managing users in Drupal 7"]
fetched: "2026-10-21T07:04:06Z"
raw: "raw/docs/7/managing-users/viewing-unpublished-content.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Viewing unpublished content

By default, anonymous and authenticated users will not be able to see unpublished content in Drupal. The way to grant them access is slightly different in Drupal 6 and 7.

## Drupal 6

Users that are allowed to create content, will be able to see unpublished content created by themselves, but not nodes created by others. By enabling the permission 'administer nodes' in Drupal 6, you give them permission to see all unpublished content.

Note that 'administer nodes' does much more than just allowing users to see unpublished content and should be used with care. ([more information on 'administer nodes'](/node/132202))

**View Unpublished Content with Views Module**  
The Views module allows access to view data from unpublished nodes. It has a separate filter for published / unpublished status to block access if wanted.

## Drupal 7

In Drupal 7, users are not allowed to view any unpublished content by default, not even content created by themselves. By enabling 'View own unpublished content', you grant users access to their own unpublished content.

The only way to allow users access to all unpublished content in Drupal 7 (without using a contributed module), is to enable the permission 'Bypass content access control'.  
Use this permission with extreme caution as it has far more consequences than just allowing access to unpublished content. In combination with Organic Groups for example, this permission allows access to private group content regardless of whether the user is a group member.

**View Unpublished Content with Views Module**  
The Views module allows access to view data from unpublished nodes. It has a separate filter for published / unpublished status to block access if wanted.

## View unpublished module

The module [View unpublished](/project/view_unpublished) allows you to grant access for specific user roles to view unpublished nodes of a specific type. Access control is quite granular in this regard. Additionally, using this module does not require any modifications to your existing URL structure.

## Workbench module

[Workbench](http://drupal.org/project/workbench) publishing workflow module also can be used to add this functionality. Workbench is actually a suite of modules designed to meet ubiquitous editorial workflow needs in Drupal.

## Revisioning module

[Revisioning](http://drupal.org/project/revisioning) module, which adds permissions for viewing node revisions can also be used to grant editorial access to unpublished node states.

## Content Access module

The [Content Access](http://drupal.org/project/content_access) module interferes with the Node module's global "View own unpublished content" permission. There is information about this issue, plus a workaround, at [Access control module prevents View of user's own unpublished content](http://mbharris.co.uk/content/access-control-module-prevents-view-users-own-unpublished-content).

## Drupal 9

In Drupal 8/9, users are not allowed to view any unpublished content by default, not even content created by themselves. By enabling 'View own unpublished content', you grant users access to their own unpublished content.

The only way to allow users access to all unpublished content in Drupal 9 (without using a contributed module), is to enable the permission 'Bypass content access control'.  
Use this permission with extreme caution as it has far more consequences than just allowing access to unpublished content. In combination with Organic Groups for example, this permission allows access to private group content regardless of whether the user is a group member.

### Content Moderation module

Drupal 9 ships with the [content moderation](https://www.drupal.org/docs/8/core/modules/content-moderation/overview) module which allows content editors to view unpublished content, simply by turning it on and reviewing permissions. 

Enabling the Content Moderation module creates a default [Workflow](http://www.drupal.org/docs/8/core/modules/workflows/overview) called "Editorial" that can be used for custom block types or content types. **(Note: The Editorial Workflow will only be created, if you installed your site from the standard Drupal installation profile. See [Troubleshooting](https://www.drupal.org/docs/8/core/modules/content-moderation/overview#s-troubleshooting) section for details on how to fix that.)** You can use the default settings, or [customize the workflow configuration](https://www.drupal.org/docs/8/core/modules/workflows/overview). From here, there are also some additional steps necessary in order to use Content Moderation.

### Access Unpublished module

Drupal 9 [Access unpublished](https://www.drupal.org/project/access_unpublished) is an easy to use module that grants access to view unpublished content (node, media, anything that implements EntityPublishedInterface) to anyone who has a unique URL and appropriate permissions. This module is useful for proofreaders, content checkers etc. Webmaster does not need to create user accounts and can keep the website safer. Each content item has its own unique access URL.

### View unpublished module

The module [View unpublished](/project/view_unpublished) allows you to grant access for specific user roles to view unpublished nodes of a specific type. Access control is quite granular in this regard. Additionally, using this module does not require any modifications to your existing URL structure.
