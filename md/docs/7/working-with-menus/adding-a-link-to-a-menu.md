---
title: "Adding a link to a menu"
source_url: "https://www.drupal.org/docs/7/working-with-menus/adding-a-link-to-a-menu"
page_type: page
last_updated: "Last updated on 30 September 2016"
published: "2010-05-03T22:57:33+00:00"
modified: "2016-09-30T11:33:26+00:00"
breadcrumb: ["Drupal 7", "Working with menus in Drupal 7"]
fetched: "2026-10-21T07:19:52Z"
raw: "raw/docs/7/working-with-menus/adding-a-link-to-a-menu.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Adding a link to a menu

## Before you begin

Ensure that the *Menus* module is activated.

If the link you plan to add leads to a Drupal node, first be sure your menu is enabled in the node's content type.

It is possible to add menu links that are not enabled in the content type using the first method below. If you do, you will find that certain changes can cause your link to disappear from the assigned menu.

## Adding a link directly into the Menu

![Locate a menu to edit](/files/Add%20Menu3.jpg)

1.  Navigate to the Menus page (*Structure \> Menus* or `http://example.com/admin/structure/menu`).
2.  Locate a menu to edit and click **add link**.
3.  In the **Menu link title** field, enter the title as it will be displayed in the menu.
4.  In the **Path** field, enter a path for the link. This can be an internal Drupal path such as node/add (see "Before you begin" above) or an external URL such as `http://example.com`. Enter `<front>` to link to the front page.
5.  In the **Description** field, enter the text that will be displayed when a user hovers over the link.
6.  Enable any of the following options:

- **Enabled**: If the link is not enabled, it will not be displayed in the menu.
- **Expanded**: If this option is enabled and the menu link has children, the first level children of the menu link will always be expanded. (NOTE: This rule doesn't cascade down for subsequent levels of children links. You must enable this option at each level where you want the next level to be expanded.)
- In the **Parent link** list, select the parent of the link.
- (Optional) In the **Weight** list, select the relative weight of the link. Links with the "lightest" weight will display higher in a menu. Links with the same weight will display in alphabetical order.
- Click **Save**.

## Configuring Menu settings for a content type

This configuration allows you to use the node edit page to configure a menu link

1.  Navigate to the content type for the node (*Structure \> Content types* or `http://example.com/admin/structure/types`).
2.  Locate the content type and click **edit**.
3.  Choose **Menu settings**.
4.  Click the checkbox of the menu you need.
5.  (Optional) Set the **Default parent item** to choose a default menu for this content type.

## Using the node edit page to add a menu link

1.  Navigate to the node editing screen (*Node \> Edit* or `http://example.com/node/*/edit`) for the node you want to add to the menu (this is in the Content menu for Drupal 7). This can also be done when you first create the node.
2.  Click the checkbox marked **Provide a menu link**. The menu options will appear.
3.  In the **Menu link title** field, enter the title as it will be displayed in the menu.
4.  In the **Description** field, enter the text that will be displayed when a user hovers over the link.
5.  In the **Parent item** list, choose the menu that should display this item. Note: the menu you want will only appear in this list if you have assigned it to the content type of the node you are editing. See "Before you begin" above.
6.  (Optional) In the **Weight** list, select the relative weight of the link.
7.  Click **Save**.

![edit content](/files/Content%20Edit2.png)
