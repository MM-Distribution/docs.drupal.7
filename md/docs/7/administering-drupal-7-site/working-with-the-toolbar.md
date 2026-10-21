---
title: "Working with the toolbar"
source_url: "https://www.drupal.org/docs/7/administering-drupal-7-site/working-with-the-toolbar"
page_type: page
last_updated: "Last updated on 10 August 2016"
published: "2009-12-01T04:08:46+00:00"
modified: "2016-08-10T19:28:48+00:00"
breadcrumb: ["Drupal 7", "Administering Drupal 7 site"]
fetched: "2026-10-21T06:00:09Z"
raw: "raw/docs/7/administering-drupal-7-site/working-with-the-toolbar.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Working with the toolbar

The administrative toolbar gives you quick access to the most important administrative pages. The Toolbar module is enabled by default (unless you choose the "Minimal" profile when installing). The shortcut bar that is displayed below it

![](/files/toolbar.png "toolbar")

## Uses

### Toolbar

The following links are available, given that their respective module(s) are enabled.

1.  **The home icon:** Return to the home page.
2.  **Dashboard:** Go to the administration dashboard.
3.  **Content:** Find, manage, and create new pages; manage comments.
4.  **Structure:** Edit blocks, define new content types, configure menus, administer tags with [taxonomy](/handbook/modules/taxonomy), and configure some contributed modules.
5.  **Appearance:** Switch between themes, install themes, and update existing themes.
6.  **People:** Manage existing users, or create new user accounts.
7.  **Modules:** Update, enable, disable, and install new modules.
8.  **Configuration:** Configure the settings for various functionality, including some contributed modules. You can edit user account settings, general site information, and settings for other general administrative tasks.
9.  **Reports:** Display information about site security, necessary updates, and information on site activity.
10. **Help:** Display information about the functionality of all of the modules installed on the site, including core modules. Each help page has a link to the module's online documentation page on Drupal.org, where more information can be found.
11. **User-specific actions:** Display the user account page or log out.

### Shortcut bar

The grey bar below the Toolbar is a customizable list of [shortcuts](/handbook/modules/shortcut). Click "edit shortcuts" on the right side to add to the default shortcuts. Or click on the down arrow next to "Log out" to hide the short-cut bar.

You can customize different sets of shortcuts on the Shortcuts administration page (*Administer \> Configuration \> User interface \> Shortcuts* or `http://example.com/admin/config/user-interface/shortcut/`). Each set of shortcuts is its own list of custom links, and each user can select which set they would like to see on their user profile.

The shortcut set that is selected can also be displayed as a block in any region, by adding the Shortcuts block to a region on the Blocks administration page (*Administer \> Structure \> Blocks* or `http://example.com/admin/structure/block`).

### Roles and permissions

For the site administrator (User 1) and users with the "Use the administration toolbar" permission, the toolbar is displayed at the top of the page.

## Disabling

The Toolbar and Shortcuts bar can both be disabled by disabling their associated module via the Modules administration page (*Administer \> Modules* or `http://example.com/admin/modules`).

If the toolbar is disabled, you can reach the administrative screens directly by going to `http://example.com/admin`. Also, you can navigate to the Dashboard (which is at `http://example.com/admin/dashboard` and linked to in the default "Management" block in the default Bartik theme) and then use the "By task" and "By module" tabs.
