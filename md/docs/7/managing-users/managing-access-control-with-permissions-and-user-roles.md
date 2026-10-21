---
title: "Managing access control with permissions and user roles"
source_url: "https://www.drupal.org/docs/7/managing-users/managing-access-control-with-permissions-and-user-roles"
page_type: page
last_updated: "Last updated on 20 November 2018"
published: "2005-05-07T22:15:53+00:00"
modified: "2018-11-20T04:12:31+00:00"
breadcrumb: ["Drupal 7", "Managing users in Drupal 7"]
fetched: "2026-10-21T07:02:18Z"
raw: "raw/docs/7/managing-users/managing-access-control-with-permissions-and-user-roles.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Managing access control with permissions and user roles

Roles enables you to assign specific permissions to a group and to fine-tune the security, use and administration of modules, therefore of Drupal in general. Users assigned to the role or group, are granted those permissions as assigned to the role. Common examples of roles used with which you may be familiar include: anonymous user, authenticated user, moderator, and administrator.

By default, **Drupal 6** automatically defines two roles as a part of site installation:

- **anonymous user** -- readers of the site who either do not have an account or are not logged in.
- **authenticated user** -- the role assigned to new accounts on a Drupal site.

**Drupal 7** creates a third role **Administrator** when you use the *standard* installation profile. This has all permissions enabled by default. If you want to have an Administrator role using the *Minimal* installation profile, create a new role and select this as the admin role in admin/config/people/accounts.

The first Drupal account created on a new installation, sometimes referred to as the "root user", always has full permissions for all Drupal activities, including administration and content creation, editing and removal.

Take note, however, that installation and enabling of additional, contributed modules DOES NOT automatically grant module permissions to the administrator role and its users. Such default Drupal setting is primarily for security purposes. Therefore, after installation and enabling of additional contrib modules, you need to manually assign and grant module permissions to the administrator role, or as required, to other roles. 

Permissions typically fall under one of the following categories:

- Administer -- Administer permissions, such as *administer content* and *administer users*, are usually reserved for the most trusted site users. These administration privileges grant users extensive control of the specific module(s) described by the permission title. For example, when administer permissions are granted on modules associated with specific node types, the user will be able to edit and delete all content for that node type on the entire site. Reminder: you'll have to assign access administration pages rights to any role which also needs to configure site options in the administration menu.
- Access -- Permissions which grant access allow users read-only rights or general use of specific site modules, without any significant configuration privileges. Typically, these roles do not permit the creation of content. Most access permissions are safe to assign to any user role, although giving *access administration* should generally be reserved for the most trusted users.
- Create -- Allows users to create, but not necessarily edit later, the specified type of content. Generally applies to node types.
- Maintain -- These permissions generally enable a user to create content, as well as allowing the author of the submitted content to edit their own content. If you want to allow new site members to keep a weblog or work on the collaborative book, you'll need to enable maintain permissions for the authenticated user.

The *Anonymous user* role should typically have the least access and permissions among other roles. *Authenticated user* may be given more permissions depending on the nature and requirements of the website. Such instances may be the ability to create some types of content. If administrator approval is required for new users, or if they match certain criteria (such as having a company email address), you may be able to grant more permissions.More trusted users might be granted special privileges through an administrator-created role, and must be manually added to that role through the user administration interface.

**To create a new role**

1.  Navigate to /admin/user/roles (Drupal 6) or /admin/people/permissions/roles (Drupal 7).
2.  Enter a label for the new role in the available text field at the bottom of the current list of roles.
3.  Click Add Role.

**To assign permissions to a role**

1.  Navigate to /admin/user/permissions (Drupal 6) or admin/people/permissions (Drupal 7).
2.  Your new role will be listed as a new column in the permission matrix. Grant permissions to the new role.

**To add or remove a user from a role**

1.  Navigate to /admin/user/user (Drupal 6) or admin/people (Drupal 7)
2.  Enable the checkbox beside one or more user names.
3.  In the Update Options dropdown box, select a role to add or remove.

***Note:***

Although all roles you create yourself receive any permissions you give to authenticated users automatically, neither roles you create yourself nor the authenticated user role receives permissions given to anonymous users. If you check any of the permissions boxes for anonymous users in the access control page, you should almost always also check the equivalent box for authenticated users to avoid odd site behavior.
