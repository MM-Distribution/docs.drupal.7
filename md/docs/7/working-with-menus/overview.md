---
title: "Overview"
source_url: "https://www.drupal.org/docs/7/working-with-menus/overview"
page_type: page
last_updated: "Last updated on 2 December 2018"
published: "2005-05-09T19:20:54+00:00"
modified: "2018-12-02T19:22:15+00:00"
breadcrumb: ["Drupal 7", "Working with menus in Drupal 7"]
fetched: "2026-10-21T07:19:37Z"
raw: "raw/docs/7/working-with-menus/overview.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Overview

You can add, remove, and rename menus and menu items/tabs. You can also configure a special block for a menu and you can specify the default menu to which new items will be added.

In many themes, there are at least two menus, the Main (or primary) menu, and a secondary menu. The Main menu's links drive the main navigation structure for your site and are often displayed prominently across the top or side of the site. The Secondary menu is often used for items like the copyright and privacy notices, and is often displayed at the bottom or very top of the page in smaller text. You can specify which menus are used for the main and secondary links.

When adding or editing site content, you can also specify the content's menu item. You can specify a default menu for the content authoring form.

Each default or custom menu has a corresponding block. For more information on blocks, see [Working with Blocks](/documentation/modules/block).

### Configuration

**Creating a menu**

![Drupal 7 Menu Screen](/files/menu_drupal7_main_screen.png)

1.  Navigate to the Menus page (***Structure \> Menus*** or `http://example.com/admin/structure/menu`).
2.  Click **Add menu**.
3.  In the **Title** field, enter a title.
4.  In the **Description** field, enter an optional description.
5.  Click **Save**.

To learn how to add new menu items to the menu, read further on [Adding a link to a menu](/node/788972). To add tabs to a menu, see [Creating menu tabs](/node/1578582).

**Enable the menu**

Assuming you plan to add nodes to your menu and not just external links, you must enable it in the content type for the node(s) that will be the target of the menu's links. It is possible to add menu links that are not enabled this way through the Menus page. If you do, you will find that certain changes cause your link to disappear from the assigned menu. Menus can be enabled on multiple content types.

![Drupal 7 Enable Menu](/files/menu_drupal7_enable_menu.png)

1.  Navigate to the content type for the node(s) (***Structure \> Content type*** or `http://example.com/admin/structure/types`).
2.  Locate the content type and click **edit**.
3.  Choose **Menu settings**.
4.  Click the checkbox of the menu(s) you want to enable.
5.  (Optional) Set the **Default parent item** to choose a default menu for the content type.

**Specify the menus to use for main and secondary links**

![Menu Setting Drupal 7](/files/menu_drupal7_specify_menu.png)

1.  Navigate to the Menu settings page (**/admin/structure/menu/settings**).
2.  Specify any of the following settings:
    - **Source for the main links**: The menu that will provide the "main links". In many themes, the main links are displayed at the top of the page.
    - Source for the secondary links: The menu that will provide the "secondary links". In many themes, the secondary links are displayed at the bottom of the page.
3.  Click **Save configuration**.

**Renaming menus**

1.  Navigate to the Menus page (**/admin/structure/menu**).
2.  Click **Edit Menu**.
3.  In the **Title** field, enter a new title.
4.  Click **Save**.

*Note: The default menus cannot be renamed.*

**Removing a menu**

1.  Navigate to the Menus page (**/admin/structure/menu**).
2.  Click **Edit Menu**.
3.  Click **Delete**.
4.  Click **Delete** again to confirm.

*Note: The default menus cannot be deleted.*

**Expanding Menus**

If you have hierarchical menu items within a menu and you'd like to show the submenu items, on each parent menu item's edit page, check Show as expanded and save. This only affects the immediate children below the menu item. That is, if you have 3 levels of menu items, checking Show as expanded on the first-tier items will only show the second-tier items, not the third-tier items. For example:

- First-tier menu item 1
  - Second-tier menu item 1 (only shown if First tier menu item 1 has Show as expanded selected)
    - Third-tier menu item 1 (only shown if Second tier menu item 1 has Show as expanded selected)
    - Third-tier menu item 2 (only shown if Second tier menu item 1 has Show as expanded selected)
  - Second-tier menu item 2
- First-tier menu item 2
- First-tier menu item 3

**Note: The default Bartik theme might appear to not follow the "show as expanded" rule as explained above for the main menu in the header, but you can place that menu in other regions and see the expected behavior. Just note that themes can have implementations that seem to deviate from the rule.**
