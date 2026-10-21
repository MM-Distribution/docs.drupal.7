---
title: "Assigning permissions and users to roles"
source_url: "https://www.drupal.org/docs/7/managing-users/assigning-permissions-and-users-to-roles"
page_type: page
last_updated: "Last updated on 17 October 2018"
published: "2005-05-07T22:23:36+00:00"
modified: "2018-10-17T05:58:12+00:00"
breadcrumb: ["Drupal 7", "Managing users in Drupal 7"]
fetched: "2026-10-21T07:02:33Z"
raw: "raw/docs/7/managing-users/assigning-permissions-and-users-to-roles.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Assigning permissions and users to roles

This page needs to be merged into [managing-users/managing-access-control-with-permissions-and-user-roles](/docs/7/managing-users/managing-access-control-with-permissions-and-user-roles)

Access to almost all Drupal modules can be controlled by either enabling or disabling permissions for a given role. As a security precaution, the anonymous and authenticated users are configured with very minimal permissions during a site install. You'll have to consider which permissions to enable.

Go to the permissions administration page (*administer* \>\> *access control* \>\> *permissions*) tab to begin enabling or disabling permissions. Consider the following descriptions of permissions:

- Administer -- Administer permissions, such as *administer content* and *administer users*, are usually reserved for the most trusted site users. These administration privileges grant users extensive control of the specific module(s) described by the permission title. For example, when administer permissions are granted on modules associated with specific node types, the user will be able to edit and delete all content for that node type on the entire site. Reminder: you'll have to assign access administration pages rights to any role which also needs to configure site options in the administration menu.
- Access -- Permissions which grant access allow users read-only rights or general use of specific site modules, without any significant configuration privileges. Typically, these roles do not permit the creation of content. Most access permissions are safe to assign to any user role, although giving *access administration* should generally be reserved for the most trusted users.
- Create -- Allows users to create, but not necessarily edit later, the specified type of content. Generally applies to node types.
- Maintain -- These permissions generally enable a user to create content, as well as allowing the author of the submitted content to edit their own content. If you want to allow new site members to keep a weblog or work on the collaborative book, you'll need to enable maintain permissions for the authenticated user.
