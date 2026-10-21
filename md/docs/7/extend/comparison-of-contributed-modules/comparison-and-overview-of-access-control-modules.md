---
title: "Comparison and Overview of Access Control modules"
source_url: "https://www.drupal.org/docs/7/extend/comparison-of-contributed-modules/comparison-and-overview-of-access-control-modules"
page_type: page
last_updated: "Last updated on 14 May 2025"
published: "2008-06-12T23:21:42+00:00"
modified: "2025-05-14T15:01:00+00:00"
breadcrumb: ["Drupal 7", "Extending Drupal 7", "Comparison of contributed modules"]
fetched: "2026-10-21T08:56:38Z"
raw: "raw/docs/7/extend/comparison-of-contributed-modules/comparison-and-overview-of-access-control-modules.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Comparison and Overview of Access Control modules

Drupal's API contains a pretty good description ([Drupal 7](http://api.drupal.org/api/group/node_access/7) and [Drupal 8](https://api.drupal.org/api/drupal/core%21modules%21node%21node.module/group/node_access/8.9.x)) of how node access works. Developers should also analyze the node access functions themselves ([Drupal 7](https://api.drupal.org/api/drupal/modules%21node%21node.module/function/node_access/7.x) and [Drupal 8](https://api.drupal.org/api/drupal/core%21modules%21node%21node.module/function/node_node_access/8.9.x)).

There are many contributed node access control modules for Drupal and you really should understand the basics of node access before installing and configuring one. The API should suffice for developers but for the benefit of our many community members who build sites without reading code, here is a translation and some basic rules of thumb (these rules were originally written for Drupal 6, and they need to be reviewed and updated for Drupal 7, 8 and 9):

- **In general, you don't want to use more than one node access module on your site.** There are many node access modules to choose from: taxonomy access, nodeaccess, simple access, workflow access, etc. We all tend to add lots of modules to our sites and to expect them to play well together, but node access is an area where we need to be extra thoughtful.
- Users with permission to 'bypass node access' (Drupal7) are never restricted by node access modules. Users who do not have permission to 'view published content' (Drupal 7) will never gain access from a node access module. **Only users who have 'access content'/'view published content' and not 'administer nodes'/'bypass node access' are eligible for the wild world of node access module control.**.
- If a user's role has permission to create or edit a content type, or to edit their own posts in that content type, that ability will always be allowed regardless of your node access module's configuration. Delete access is included in the 'edit' permission. **If you want to control creating, editing, or deleting of your nodes with a node access module, be sure to not give your users these permissions in the permissions table.**
- If your content type comes from an additional module (forum, event, etc.) other than cck/fields, it may have its own permissions to set. Giving a role these permissions will also supersede the use of any node access module.
- **Node access modules always GRANT access and never restrict it** (it is a whitelisting rather than a blacklisting system). Combining multiple node access modules may produce undesirable results (e.g. if one module grants access and another doesn't, access IS granted). If you need the combined power of several node access modules in such a way that access is only granted if **all** controlling access modules provide a grant, take a look at the generic and powerful [Access Control Bridge](http://drupal.org/project/acb). Other possibilities are the [Deny access](http://drupal.org/project/deny_access) module, as well as the old [Module Grants](http://drupal.org/project/module_grants).
- The four types of possible grants on a node are: view, update, create, and delete. You can use [Devel module's devel_node_access](http://drupal.org/project/devel) to analyze a node's node access grants.
- The node access table in the database can become confused if you have, for example, toyed with multiple node access modules or come into contact with a deranged one. If you have been involved with risky node access behaviors you should rebuild your permissions. You can find this option at admin/reports/status report/rebuild permissions. It is rarely necessary.

To find a suitable module, you may want to [search for projects tagged "content access"](http://drupal.org/project/modules/?f%5B0%5D=im_vid_3%3A13434&f%5B1%5D=bs_project_sandbox%3A0&solrsort=iss_project_release_usage%20desc "Content Access search"), or browse the capsule reviews below.

## General purpose modules for Drupal 7

### Tables key

?  
Unsure, and unclear from the project page. You should check and, please, correct this piece of information.

#### Abbreviations used in the “D7” and “D8” columns

D7  
Drupal 7

D8  
Drupal 8

0  
none: no release available.

a  
alpha: 1st stage of complete project, buggy (usually very buggy).

ß  
beta: complete project to be tested, still buggy.

dev  
development: module not complete yet, probably extremely buggy.

rc  
release candidate: complete project to be tested, possibly stable.

st  
stable: tested complete project, suitable for production website (though a few secondary bugs might remain).

~~st~~  
stable (as above) but unsupported.

Although all modules are supposed to reach the stable stage, quite many are abandoned before that.

#### Abbreviations used in the “permission” column:

a  
all permissions together, i.e. the module itself doesn't manage the permissions one by one.

c  
create new content.

d  
delete.

r  
read, view.

w  
write, edit.

The “permission” column lists the permissions managed by the said module. Note that, in this column, the abbreviated permissions are not separated by commas. For instance, “rw” means “read and write”.

This table is sorted by popularity - the number of sites reporting using the all version of the module. Current order based on stats from drupal.org on 9 March 2019.

| Module name                                                                                      | D7     | D8  | smallest content unit                                    | smallest user unit                                                               | permissions                  | characteristics                                                                                                                                       |
|--------------------------------------------------------------------------------------------------|--------|-----|----------------------------------------------------------|----------------------------------------------------------------------------------|------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Access By Reference](https://drupal.org/project/access_by_ref)                                  | st     | st  | node                                                     | user                                                                             | w                            | Extends edit privileges to referenced users, to editors of referenced nodes, and/or to users with shared value in their user profile.                 |
| [Access by term](http://drupal.org/project/abt)                                                  | st     | 0   | node with taxonomy term                                  | user with taxonomy term                                                          | rwd                          | Grants are based on the relationship between the user-\>term\<-node.                                                                                  |
| [Access Control Bridge](https://drupal.org/project/acb)                                          | ~~st~~ | st  | node                                                     | user                                                                             | rwcd                         | Creates a working interplay between all enabled access control modules by requiring each access module controlling the node to grant access.          |
| [ACL](http://drupal.org/project/acl)                                                             | st     | ß   | node                                                     | list of users                                                                    | rwd                          | Helper module. Provides API for other modules. Only install if required by other modules.                                                             |
| [AUL (Access User Lists)](https://drupal.org/project/aul)                                        | st     | 0   | node                                                     | user                                                                             | rwd                          | Extends node access system per user. Has graphic interface in 2.x. version.                                                                           |
| [Commerce file](http://drupal.org/project/commerce_file)                                         | st     | ß   | file                                                     | user                                                                             | r                            | Submodule of the "Commerce" module, designed to sell file access.                                                                                     |
| [Content access](http://drupal.org/project/content_access)                                       | ß      | a   | node                                                     | user list (with ACL)                                                             |                              |                                                                                                                                                       |
| [Custom Permissions](/project/config_perms)                                                      | st     | st  | path                                                     | role                                                                             | r                            | Create a permission with name and path(s).                                                                                                            |
| [Deny access](http://drupal.org/project/deny_access)                                             | st     | 0   | content type                                             | role                                                                             | rwcd                         | **Overrides access granted by other node access modules** and/or core.                                                                                |
| [Directory based access control (ACL)](http://drupal.org/project/odir_acl)                       | st     | 0   | directory                                                | role                                                                             | rw, add file, move file etc. | Directory based access control                                                                                                                        |
| [Flexi access](http://drupal.org/project/flexiaccess)                                            | st     | 0   | node                                                     | list of users                                                                    | rwd                          | Interface to ACL module                                                                                                                               |
| [Forum access](http://drupal.org/project/forum_access)                                           | st     | a   | forum                                                    | role                                                                             | rwd, post                    | For private forums                                                                                                                                    |
| [Groups, Communities and Co (GCC)](http://drupal.org/project/gcc)                                | st     | 0   | ?                                                        | group                                                                            | wcd, publish                 | Manage groups or users.                                                                                                                               |
| [Hidden nodes](http://drupal.org/project/hidden_nodes)                                           | st     | 0   | content type                                             | role                                                                             | r                            | Withdraw read, edit and delete permissions together.                                                                                                  |
| [Node access book](http://drupal.org/project/node_access_book)                                   | st     | 0   | book                                                     | role, or users defined by another content access module                          | r                            | Gives content access permissions on a book child page if users have access to the root of the book, typically provided by another node access module. |
| [Node access keys](http://drupal.org/project/nodeaccesskeys)                                     | st     | 0   | content type                                             | role                                                                             | r                            | Helps to grant users temporary view permission.                                                                                                       |
| [Node access node reference](http://drupal.org/project/nodeaccess_nodereference)                 | st     | 0   | content with field provided by module "Entity reference" | user                                                                             | rwd                          | Gives content access permissions to users if they have access to content that is referenced with entity reference. Needs 3 other modules to work.     |
| [Node access password](http://drupal.org/project/nodeaccess_password)                            | st     | 0   | node                                                     | node password bearers                                                            | r                            | Each node generates only one password, allowing to see it.                                                                                            |
| [Node access relation](http://drupal.org/project/node_access_relation)                           | dev    | 0   | relation type                                            | user                                                                             | rwd                          | Based on the "Relation" module.                                                                                                                       |
| [Node access user reference](http://drupal.org/project/nodeaccess_userreference)                 | st     | 0   | content with field provided by module "Entity reference" | user                                                                             | a?                           | Needs 3 other modules to work.                                                                                                                        |
| [Node menu permissions](http://drupal.org/project/node_menu_permissions)                         | st     | 0   | menu link                                                | role                                                                             | w                            | Provides permissions to edit the menu link, while not having permissions to administer whole menus.                                                   |
| [Node view permissions](http://drupal.org/project/node_view_permissions)                         | st     | st  | content type                                             | role                                                                             | r                            | Of very simple use: adds options "View own content" and "View any content" for each content type on permissions page.                                 |
| [Nodeaccess](http://drupal.org/project/nodeaccess)                                               | st     | st  | node                                                     | user                                                                             | rwd                          | Adds "Grant" tab where you assign read/edit/delete permissions to individual nodes by role and/or user.                                               |
| [OG Forum D7](http://drupal.org/project/og_forum_D7)                                             | st     | 0   | forum                                                    | user group                                                                       | rw, post?                    |                                                                                                                                                       |
| [Permissions by Term](https://www.drupal.org/project/permissions_by_term)                        | 0      | st  | content with taxonomy term                               | user                                                                             | ?                            | extends Drupal by functionality for restricting access to single nodes via taxonomy terms.                                                            |
| [Privacy per user](http://drupal.org/project/privacypu)                                          | dev    | 0   | page element                                             | user                                                                             | r                            | Enables privacy settings per user, similar to the privacy settings on a site like Facebook.                                                           |
| [Private Entity](http://drupal.org/project/private_entity)                                       | 0      | a   | entity                                                   | role                                                                             | r                            | Simple per entity access flag limited to the view operation.                                                                                          |
| [Private files download permission](http://drupal.org/project/private_files_download_permission) | st     | st  | file                                                     | user                                                                             | r                            | Designed to restrict file download access.                                                                                                            |
| [Profile2 privacy](http://drupal.org/project/profile2_privacy)                                   | st     | 0   | profile field                                            | role                                                                             | r                            | Manage access to user profile fields.                                                                                                                 |
| [Protected Pages](/project/protected_pages)                                                      | st     | st  | path                                                     | user                                                                             | r                            | Secure any page by password.                                                                                                                          |
| [Restrict node page view](http://drupal.org/project/restrict_node_page_view)                     | st     | 0   | node type                                                | role                                                                             | r                            | Only controls direct access by URL.                                                                                                                   |
| [Taxonomy access control](http://drupal.org/project/taxonomy_access)                             | st     | 0   | content with taxonomy term                               | role                                                                             |                              | Taxonomy-based.                                                                                                                                       |
| [Taxonomy tools](http://drupal.org/project/taxonomy_tools)                                       | st     | 0   | taxonomy term, node with taxonomy term                   | role                                                                             | a?                           | Control access to taxonomy terms and nodes associated with taxonomy terms.                                                                            |
| [Term per role](http://drupal.org/project/term_per_role)                                         | ~~st~~ | 0   | taxonomy term page                                       | role                                                                             | r                            | Allows you to restrict access to term page based on user roles.                                                                                       |
| [User field privacy](http://drupal.org/project/user_field_privacy)                               | st     | 0   | profile field                                            | the one group of all people except the user himself (and the site administrator) | r                            | Allows private fields in the user profile.                                                                                                            |
| [View access per node](https://www.drupal.org/project/vapn)                                      | 0      | st  | node                                                     | role or user                                                                     | r                            | This module only deals with viewing nodes, it does not affect other ops (eg. create/update/delete).                                                   |
| [Workbench access](http://drupal.org/project/workbench_access)                                   | st     | st  | node                                                     | editorial section                                                                | wc                           | Allows node editing access based on "Taxonomy" or "Menu" modules.                                                                                     |
| [Workbench OG](http://drupal.org/project/workbench_og)                                           | **ß**  | 0   | node group?                                              | organic group                                                                    | wcd, publish                 | Organic group roles can be defined to be responsible to perform different transitions that will move content from the different stages.               |
| [Workflow Content Permissions](http://drupal.org/project/workflow_content_permissions)           | st     | 0   | workflow node field                                      | role?                                                                            | rw                           | Manage permissions to edit or view fields of a node that participates in a Workflow for each state.                                                   |
| module name                                                                                      | D7     | D8  | smallest content unit                                    | smallest user unit                                                               | permissions                  | characteristics                                                                                                                                       |

## Outdated and unsupported modules

| module name                                                                      | smallest content unit                                    | smallest user unit        | characteristics                                                                                         |
|----------------------------------------------------------------------------------|----------------------------------------------------------|---------------------------|---------------------------------------------------------------------------------------------------------|
| [Book access](http://drupal.org/project/book_access)                             | user                                                     | rwd, add book/child pages | Allows for per-book permissions.                                                                        |
| [Node access auto reference](http://drupal.org/project/nodeaccess_autoreference) | content with field provided by module "Entity reference" | user                      | Needs 3 other modules to work.                                                                          |
| [Taxonomy access user](http://drupal.org/project/taxonomy_access_user)           | content with taxonomy term                               | user                      | Taxonomy-based. Access follows taxonomy inheritance.                                                    |
| [Node relativity access control](http://drupal.org/project/relativity_access)    | node                                                     | ?                         | Based on the "Node relativity" module and grants automatically the permissions to the node's offspring. |
| [Node access](http://drupal.org/project/node_access)                             | node                                                     | ?                         | Bypass the node access system.                                                                          |
| [Menu node edit](http://drupal.org/project/menu_node_edit)                       | node with menu item                                      | ?                         | Bypass the node access system. Allows node editing access based on menu relationships.                  |
| module name                                                                      | smallest content unit                                    | smallest user unit        | characteristics                                                                                         |

Key: see “General purpose modules for Drupal 7” above.

## Access modules

[Security Modules](http://drupal.org/node/382752) lists some access modules and <http://drupal.org/taxonomy/term/69> lists every module with the security tag.

### Generic modules

#### [Nodeaccess](http://drupal.org/project/nodeaccess)

> Users with the 'grant node permissions' permission will have a grant tab on node pages which allows them to grant access to that node by user or role. Administrators can set default access controls per content type, and also define which roles are available to grant permissions to on the node grants tab.

### [Access control list modules](http://drupal.org/project/acl)

> The ACL module, short for Access Control List, is an API for other modules to create lists of users and give them access to nodes. It has no UI of its own and will not do anything by itself; install this module only if some other module tells you to.

#### [Content access](http://drupal.org/project/content_access)

> This module allows you to manage permissions for content types by role and author. It allows you to specify custom view, edit and delete permissions for each content type. Optionally you can enable per content access settings, so you can customize the access for each content node.

#### [Flexi access](http://drupal.org/project/flexiaccess)

> This module provides a simple and flexible interface to the ACL (Access Control List) module. It will let you set up and manage ACLs naming individual users that are allowed access to a particular node. The grants managed by the module are: View (read), update (edit), delete.

#### [Forum access](http://drupal.org/project/forum_access)

> This module changes your forum administration page to allow you to set forums private. You can control what user roles can view, edit, delete, and post to each forum. You can also give each forum a list of users who have administrative access on that forum (AKA moderators).

#### [Image gallery access](http://drupal.org/project/image_gallery_access)

> This module changes your image gallery administration page to allow you to set image galleries private. You can control what user roles can view, edit, delete and post to each gallery. You can also give each gallery a list of users who have administrative access on that gallery (AKA moderators).

### CCK field based modules

#### [Nodeaccess userreference](http://drupal.org/project/nodeaccess_userreference)

> Allows you to configure a CCK user reference field so that the user whom is referenced in a node is granted access to view the node. There are also options to give the user access to edit or delete the node.

#### [Nodeaccess Nodereference](http://drupal.org/project/nodeaccess_nodereference)

> Gives access to users if they have access to a referenced node. Checks view, update, and delete grants.

#### [Node access auto reference](http://drupal.org/project/nodeaccess_autoreference)

> Gives automatic access to users if they are referenced somehow to this node.  
> It's scanning automatically for references with unlimited deep path, so you don't need to worry anymore how to configure your permissions correct, because it's checking for references automatically.

### Taxonomy based

Use these modules to control access based on those tags, vocabularies, and terms you already use, if you use them. [Classification, taxonomy and tagging modules]() lists modules to help you classify and tag content.

#### [Taxonomy Access Control](http://drupal.org/project/taxonomy_access)

Access control for user roles based on taxonomy categories (vocabulary, terms).

Connect roles to terms. Useful if everyone has the right role. A good way to control a lot of people when they slot easily into a few roles.

#### [Taxonomy Access Control Lite](http://drupal.org/project/tac_lite)

This module restricts access so that some users may view content that is hidden from others. A simple scheme based on taxonomy, roles and users controls which content is hidden.

Take the Taxonomy Access Control role based access and add user based controls. Lets you assign users to roles and give the roles access to nodes by term but then lets you give special access to those annoying management types who refuse to wait while you create a new role. Also gives you a quick way to let contractors and temps grab quick access to resources. You know the situation. Hey it is seven minutes before your contract runs out. Rearrange the CRM system to include images the same as Facebook. I will give you access to the 398 nodes you have to change. Fix all the spelling mistakes while you are at it.

#### [Taxonomy access user](http://drupal.org/project/taxonomy_access_user)

> Taxonomy access with inheritance.

### Modules that contain node access modules

#### [Group](https://drupal.org/project/group)

> The heir of Organic Groups (OG). Enables users to create and manage their own "groups". Each group can have members and its own shared content. Subgroups are implemented as well via a bundled submodule. The main difference from OG is that OG implements groups as nodes and uses Entity Reference fields to connect groups and content, while Group implements groups as a new Entity type, allowing for better conceptual separation of concerns between groups and content, and should be more compatible with the Drupal way of Fieldable Entities going forward from Drupal 8 and beyond.

#### [Organic Groups](http://drupal.org/project/og)

> Enable users to create and manage their own 'groups'. Each group can have subscribers, and maintains a group home page where subscribers communicate amongst themselves.

#### [Workflow](http://drupal.org/project/workflow)

> The workflow module allows the creation and assignment of arbitrary workflows to Drupal node types. Workflows are made up of workflow states. For example, a workflow with the states Draft, Review, and Published could be assigned to the Story node type.

#### [Domain](http://drupal.org/project/domain)

> The Domain Access project is a suite of modules that provide tools for running a group of affiliated sites from one Drupal installation and a single shared database. The module allows you to share users, content, and configurations across a group of sites such as:

### Modules for use by other modules

#### [Node Access Relation](http://drupal.org/project/node_access_relation)

> Node Access Relation allows content access permissions to be set for users referenced via relations created by the Relation module.

#### [Relativity access](http://drupal.org/project/relativity_access)

> This module enables access control based on (and so requires) the Node Relativity module. It propagates the grants from a node to its descendants. You should use another module like nodeaccess to provide the grant to the ancestors.

#### [Ubercart node access](http://drupal.org/project/uc_node_access)

> UC Node Access lets you attach Node access features to products in your Ubercart store. These features allow customers who purchase the product to receive view access to nodes on your site either indefinitely or for a limited time based on the feature's settings. UC Node Access does not handle access grants itself but rather depends on other modules to define handlers that integrate UC Node Access with the various node access modules developed for Drupal.

#### [User points node access](http://drupal.org/project/userpoints_nodeaccess)

> The Drupal userpoints nodeaccess module enables you to sell access to a single node for a specific category and amount of userpoints.

#### [Ecommerce Node Access Product](http://drupal.org/project/ec_nodeaccess)

> Provides 'Node Access' settings for product nodes, whereby users who purchase the product are granted view access to content, which can be predefined either by category, by node, or by view.

### Modules that alter the menu to allow access to give edit access

These modules bypass the node access system and instead alter access of node/%/view, node/%/edit and node/%/delete, so may have issues scaling.

#### [Node access](http://drupal.org/project/node_access)

#### [Menu node edit](http://drupal.org/project/menu_node_edit)

> Allows node editing access based on menu relationships.
