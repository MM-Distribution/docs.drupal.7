---
title: "Enabling user pictures (avatars)"
source_url: "https://www.drupal.org/docs/7/managing-users/enabling-user-pictures-avatars"
page_type: page
last_updated: "Last updated on 30 September 2016"
published: "2005-05-07T21:47:17+00:00"
modified: "2016-09-30T21:02:32+00:00"
breadcrumb: ["Drupal 7", "Managing users in Drupal 7"]
fetched: "2026-10-21T07:03:05Z"
raw: "raw/docs/7/managing-users/enabling-user-pictures-avatars.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Enabling user pictures (avatars)

The Drupal core user module provides pictures (or avatars) for each Drupal user out of the box.

## Enabling user pictures

1.  Navigate to Configuration \> People \> Account settings.
2.  In the *Personalization* settings, select *Enable user pictures.*
3.  For *Picture directory* type *pictures*
4.  Under *Picture display style*, select *thumbnail* (you can change the size settings
5.  Click "Save configuration".

Next, ensure your user pictures display in your theme. These are enabled by default in Bartik, the default theme of Drupal 7 , so you may have to check this with any new theme you add.

1.  Go to *Appearance* and click "Settings" for the theme you have enabled as default.
2.  In the *Toggle display* settings, select *User pictures in posts* and/or *User pictures in comments*.
3.  Click "Save configuration".

## Displaying avatar images (in theme)

In the node.tpl.php, use "\$node-\>picture" to get the URL of the image.

## Moving images

The database stores the name of the directory you set in Step \#3. If you want to move your images to a new directory you must complete the following steps:

1.  Update the directory identified in the previous section.
2.  Move existing images to the new directory.
3.  Update the database manually to use the new directory location. In Drupal 6.x the images are stored in the table `users`.
