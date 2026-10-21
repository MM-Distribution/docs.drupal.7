---
title: "Users, permissions, and roles"
source_url: "https://www.drupal.org/docs/7/understanding-drupal/users-permissions-and-roles"
page_type: page
last_updated: "Last updated on 4 October 2022"
published: "2013-03-10T02:46:13+00:00"
modified: "2022-10-04T13:26:47+00:00"
breadcrumb: ["Drupal 7", "Understanding Drupal 7"]
fetched: "2026-10-21T05:50:21Z"
raw: "raw/docs/7/understanding-drupal/users-permissions-and-roles.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Users, permissions, and roles

Every visitor to your site, whether they have an account and log in or visit the site anonymously, is considered a user to Drupal. Every user also has a numeric user ID special to the type of user.

If a user is not logged in, then the user is considered an Anonymous user having user ID **0**. Otherwise, the Drupal site visitor has a user id greater than **0**. User ID 1 is reserved for the Administrator. This is also called the master Administrator.

## Types of Users

### Main (UID 1) Administrator

This user has the ID one (1). User of ID one (1) is the primary admin user account created during Drupal installation. This user is very special because it has permission to do absolutely everything on the site.

### Logged In

These users are assigned a user ID when they register for the website. A user name and email address is associated with any user that isn't anonymous (therefore must be logged in).

### Anonymous

Anonymous users who visit the website, but do not log in, all share a user ID of zero (0).

#### Associating more information with Users

Other information can also be associated with users by modules; for instance, if you use the core Profile module, you can define user profile fields to be associated with each user.

1.  **Computer User**: The person installing Drupal must have access to the computer where the installation lives. If you are installing Drupal locally on your own computer, then the "computer user" is you. It is also important to note that you are most likely the "administrator" user role, too. If you are installing Drupal at a remote server such as a web hosting company, then the computer user account could be called one of the following (not a complete list):

    - Web hosting account login
    - FTP login
    - cPanel login
    - Secure shell (SSH) login

    *Who are the people who are associated with the computer user?* In some cases, like for your own computer or for some FTP logins, these "users" are individual people. In other cases, such as a web hosting account login or cPanel, one user (or "account") name/password is used to log in to control the account and may be shared by several people.

2.  **Database User**: A Drupal installation requires a database to run. (MySQL and PostgreSQL are the best supported database programs compatible with Drupal.) Databases typically have access control mechanisms and require "users" with the right permissions to change the database (add/edit/remove data, create tables, etc.). A Drupal installation needs to have full control over the database, so when you set up a new Drupal site, you (or your web hosting company) create a database user with full privileges and then give the user name and password to the Drupal installation so that Drupal will have full control over the database. The database user information is stored in the settings.php file, which is either in sites/default or a different subdirectory of sites in your Drupal installation.

    *Who is the database user?* The database "user" is *not* a person. It is an account created with the database software in order to give Drupal control of the database.

3.  **User/1**: "User/1", also known as the "maintenance account" or "super-user account" is the Drupal account you are prompted to create immediately after you have successfully installed a new Drupal site. This account is unique to your site (it doesn't have anything to do with Drupal.org or any other web site). This account is different from all other users in a Drupal installation because it has no permissions limitations ("permissions" were called "access control" in Drupal 5 and before). "User/1", in Drupal 6 and before, is also the *only* account that can launch the update.php script that you need to run after a software upgrade.

    *Who is user/1?* User/1 shouldn't be associated with an individual person, but rather with the person or persons who have the responsibility for keeping software up-to-date on your site.

    It is a best practice to *avoid* creating site content with user/1. That is so because it is awkward when responsibility for site maintenance done as User/1 needs to change to a new person if the original User/1 wrote content that still needs to be associated with him/her. The content written by the original author would have to then be assigned to a new user account. It's better to simply create that second account immediately after installing the site.

4.  **User/2 and all other users**: User/2 and all other registered users on your Drupal site should each be associated with an individual person. Registered users can be assigned to roles, which are given fine-grained permissions to allow different users different access to administer the site and add content.

5.  **User/0 or Anonymous user**: User/0 is reserved for the unregistered/anonymous user. In database 'users' table uid = 0 is assigned for anonymous users. **Note:** In Database's `users` table, uid = 0 row must exist or the site will have severe problems.

## Permissions

Other users on your site can be assigned permissions via roles. To do this, you first need to create a role by navigating to people --\> permissions --\> role. A common role is "Content editor" or "Member". Next, you will assign permissions to that role, to tell Drupal what that role can and can't do on the site. Finally, you will grant certain users on your site your new role, which will mean that when those users are logged in, Drupal will let them do the actions you gave that role permission to do.

You can also assign permissions for the special built-in roles of "anonymous user" or "guest" (a user who is not logged in) and "authenticated user" (a user who is logged in, with no special role assignments). Drupal permissions are quite flexible—you are allowed to assign permission for any task to any role, depending on the needs of your site.

There are some exceptions: As example, if you want a guest allowed to see content on the front page, you can't prevent them from seeing any content of the same content type on any page, if they know the correct url (from viewing over your shoulder ...) without any login.

Read more about this topic in [The Drupal Cookbook (for beginners).](http://drupal.org/node/120614)

## User Profile

The default Drupal 7/ Drupal 8 or any version has user profile section. The user profile section has only few fields like username, password, email address, profile picture and time zone.

You may have as many fields to the user profile as you require.

To add a new or existing field with different field types (such as Image, Tags field etc.) to the user profile:

1.  Enable the **Field UI** module.

2.  Go to "**Admin → Configuration → People: Account settings**" in the admin menu, and then to "**Manage fields**" (the second tab).

    (Alternatively, use the direct path in the URL: `/admin/config/people/accounts/fields`).

3.  Fill out the "Add new field" or "Add existing field" line at the bottom of the form and click "Save".

## Content Permissions

As example, you could have 3 kinds of content:

- red: restricted to a special group of registered users --\> red users.
- blue: restricted to all registered users --\> all registered users.
- green: free visibility for all users.

Now you could have 2 sub-groups of red users:

- red.white
- red.black

Members of each sub-group may not edit the content of the other sub-group.

Content of the group "red.black" is not visible for non-members.

A user could have a membership for both groups.

So the configuration could be as follows:

- Adam:  
  Registered user --\> rights to view any blue and red.white content  
  Member of red.white --\> full rights to create and edit any red.white content.
- Beth:  
  Registered user --\> rights to view any blue and red.white content  
  Member of red.white --\> full rights to create and edit any red.white content.  
  Member of red.black --\> full rights to create and edit red.black any content.
- Christoph:  
  Registered user --\> rights to view any blue and red.white content  
  Member of red.white --\> full rights to create and edit red.white any content.  
  Member of red.black --\> rights to view any red.black content.
- Daniel:  
  Registered user --\> rights to view any blue and red.white content  
  Member of red.black --\> rights to view any red.black content.
- Esther:  
  Registered user --\> rights to view any blue and red.white content  
  Special Rights to create and edit blue and green content.
- Fred:  
  Registered user --\> rights to view any blue and red.white content

### Appearance

- Schools
- Educational groups
- Publishers
- Communities
- Companies with different product groups
- and more ...

### Realization in Drupal

Such a configuration is not possible to achieve in Drupal at this time without additional programming. So it's possible to realize it for developers only.

There are NO actual modules, which can support such structures or give some help in the realization of such a structure.

In Drupal 7 several modules existed, which were able to support it, but these were not upgraded or lost some functionality.

## Membership State Permissions

As working in groups or divisions, a membership to that group or division is required, which also requires to set permissions not only to user roles, but also to membership roles.

A membership state has to be defined or created, which holds the actual state of a user.

It is required, that a user can enter or leave a group, with a consequent update of their membership.

If the user enters a group, they are a visitor, if there is no explicit membership defined. Depending on the permissions for this group they can view, edit or create content inside this group. Freshly created content have to be automatically assigned to this group, making it easy to handle. It is very annoying, to be forced every time to do the related settings manually, every time a new content is created. Sure, there must be a possibility to override this manually.

If the user leaves the group, they lose their state as visitor or other assigned permissions. A creation of content would then be in the area for registered users, if allowed.

Recapitulation:

1.  We can say, that membership states are required to manage content group permissions.
2.  It is required, to have the possibility, to add roles to content groups, which are then assigned to users, who are entering these groups, independently of user roles.
3.  It is required to have an automatism, to assign content to content groups, where it is created.
