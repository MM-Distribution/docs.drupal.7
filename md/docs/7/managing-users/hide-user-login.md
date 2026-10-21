---
title: "Hide user login"
source_url: "https://www.drupal.org/docs/7/managing-users/hide-user-login"
page_type: page
last_updated: "Last updated on 23 May 2021"
published: "2004-12-01T20:47:23+00:00"
modified: "2021-05-23T19:07:48+00:00"
breadcrumb: ["Drupal 7", "Managing users in Drupal 7"]
fetched: "2026-10-21T07:03:35Z"
raw: "raw/docs/7/managing-users/hide-user-login.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Hide user login

In the default setup the Drupal login block is always displayed unless a user is logged in. This may not always be desirable. For example, if you are using Drupal to create a site that has a very small number of people actually logging into the system to create or edit content, then you probably don't want a large portion of your screen real-estate taken up with a login block that only serves a small minority of users. This also confuses the majority of your users that will not have the option to log in.

## To disable the login block

1.  Go to the blocks administration page:
    - Drupal 6: *Administration* » *Site building* » *Blocks*
    - Drupal 7: *Administration* » *Structure* » *Blocks*
    - Drupal 8: *Manage* » *Structure* » *Block layout*
2.  In the *Region* column next to *User login* select *None*  
    ![](/files/hide_user_login_1.PNG)
3.  At the bottom of the page, click *Save Blocks*

Your regular content editors and administrators can still log in to the site by directly accessing the login page:

- <http://www.example.com/?q=user>
- <http://www.example.com/user> (if [Clean URLs](/node/15365) are enabled)

**NOTE FOR DRUPAL 8: **If you do not have any content on the front page and remove the default "Front Page" under configuration \>\> settings, the default content for the front page is the user page or the login form for users who are not logged in. This can not be removed through the block layout system. 

## Selectively hide the login block

Since the login block is a normal block, you can configure it on the blocks administration page. Use the *configure* link next to each block and you will be given options to set the visibility of the block by page:

![](/files/edit_user_login_vis1.PNG)

by content type:

![](/files/edit_user_login_vis3.PNG)

or by role:

![](/files/edit_user_login_vis2.PNG)

## Hide the login page

You can hide the login page from anonymous users and bots by requiring a secret querystring by enabling the [disable login page](https://www.drupal.org/project/disable_login) module in D8 / D9. This can be useful on sites that do not need any public login and only needs webmasters or select few internal users.

## Move the login page

Obscurity is not security, and it is essentially [impossible to hide](/node/766404) that a site runs Drupal. Still, it is possible to move the login page from `/user` to another path with the [Rename Admin Paths](https://www.drupal.org/project/rename_admin_paths) module.
