---
title: "User Roles"
source_url: "https://www.drupal.org/docs/7/managing-users/user-roles"
page_type: page
last_updated: "Last updated on 14 March 2018"
published: "2012-10-04T17:45:26+00:00"
modified: "2018-03-14T00:03:47+00:00"
breadcrumb: ["Drupal 7", "Managing users in Drupal 7"]
fetched: "2026-10-21T07:02:02Z"
raw: "raw/docs/7/managing-users/user-roles.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# User Roles

One of the most basic ways to administer user Web Site permissions through Drupal is by creating roles.

Rather than assigning individual permissions to each user, permissions are assigned to roles, and roles are assigned to users. Using roles gives administrators greater control over permissions, making it easy to assign and remove roles when necessary.

For example, assigning the role of "Author" to select authenticated users could allow certain people to write and publish articles on your Web Site. Permissions for the "Author" role could open the permissions under "Node", "Article", - "Create new content", "Edit new content", and Delete own content" that other users and/or roles do not have. If a user no longer writes for your Web Site, their user role can be quickly modified by removing the "Author" role, which also removes all permissions assigned under that role.

Your first step is to go to **Administration/People/Permissions/Roles**. Once there you will find three default roles of "Anonymous", "Authenticated", and "Administrator" along with a text box allowing the addition of a custom role.

![admin_people_permissions_roles](/files/admin_people_permissions_roles_2.PNG)

To create a new role, all you have to do is come up with a name for it, type it in the textbox and "Add Role" to your list. To the right of your role will be an "edit role" and an "edit permissions" selection.

![admin_people_permissions_roles_author](/files/admin_people_permissions_roles_author_2.PNG)

The "edit permissions" selection will show only the permission selections for the individual role making it easier to alter. This permission will also reveal itself at **Administration/People/Permissions** with all the other roles for your Web Site.

![admin_people_permissions_roles_selection](/files/admin_people_permissions_roles_selection_2.PNG)

The "edit role" will only allow a role name change or a delete option. If you are deleting this role, be sure there are no users attached.

![admin_people_permissions_roles_edit](/files/admin_people_permissions_roles_edit_2.PNG)

For a listing of all users with a specific role, go to **Administration/People**. The third column on this listing will display the role assigned to each users. The last "edit" column on the right of each user line at this location will lead back to the User Profile where roles may be assigned or removed. Note: A user may have more than one role at any given time. This makes it easy to divide permissions into multiple roles and allows for users to be assigned complex permissions.

![admin_people_users_author_role](/files/admin_people_users_author_role_2.PNG)

If the Administrator is setting up a new User Profile **(Administration/People/Add User)** for the Web Site user, a role may be established at that time. Otherwise, the Administrator must go in after the user has set up their own User Profile and update the user's role.

![admin_people_mark_author_role](/files/admin_people_mark_author_role_2.PNG)
