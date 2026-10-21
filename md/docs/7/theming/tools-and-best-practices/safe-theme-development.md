---
title: "Safe theme development"
source_url: "https://www.drupal.org/docs/7/theming/tools-and-best-practices/safe-theme-development"
page_type: page
last_updated: "Last updated on 15 February 2023"
published: "2008-11-20T09:26:16+00:00"
modified: "2023-02-15T13:43:44+00:00"
breadcrumb: ["Drupal 7", "Theming Drupal 7", "Tools and best practices"]
fetched: "2026-10-21T08:52:47Z"
raw: "raw/docs/7/theming/tools-and-best-practices/safe-theme-development.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Safe theme development

You will invariably run into problems when developing a theme. Here are some safeguards and considerations when resolving issues with your theme.

### Always Develop on a Test Site

To prevent users seeing a website full of bugs, you need a test site. The best alternative is to [set up a local server](/node/157602) and [install Drupal](/node/157602) on your localhost.

### Write Secure Code

Any PHP functions in your theme should use the Drupal API and follow best practices for [writing secure code](/writing-secure-code). Note that functions should be placed in template.php or a module and not in \*.tpl.php.

### Deploy Your Theme Selectively

When your theme is ready to show to other people but not ready to go live, you can use several methods to selectively show only certain users your theme.

#### By Role:

Configure the permissions for a role to allow users to select their own theme via their user account settings. This is perhaps the most straightforward method and requires no additional modules.

#### Use Theming Modules:

Use the [Switchtheme module](/project/switchtheme) and allow only certain roles to switch themes.  
The [Sections module](/project/sections) allows you to apply a theme to one or more sections of your site, rather than to the entire site. This capability is especially useful if you are theming for a very large site because it makes it possible to deploy your theme in stages.

#### Use Drupal's Multi-site Feature:

You can use Drupal's [Multi-site](/getting-started/6/install/multi-site) capability to set up a live test site alongside your existing site.

### Turn on both PHP Error Reporting and Error Message Display in Development Environments

Every PHP error, no matter how minor, puts PHP into an error reporting state, which drastically slows execution. It's also an indication that there's a problem with your code that needs to be fixed. The best practice is to thoroughly exercise and test your site and resolve any PHP errors that are displayed.

Go to /admin/config/development/logging and under "Error messages to display", check "All messages".

Alternatively, if you have environment-specific configurations:

``` php
// Show all PHP error messages.
$conf['error_level'] = '2';
```

### Turn off Error Message Display in Production Environments

When PHP encounters an error, it can generate an error log and display a report on the screen. While these error messages can be helpful in debugging your site, they can be a security risk on a live site as they may reveal information about your server that can be used to compromise it.

Therefore, it's best practice to log PHP errors, but not display them to users. Go to /admin/config/development/logging and under "Error messages to display", check "None".

``` php
// Hide all PHP error messages.
$conf['error_level'] = '0';
```

### Use a Stable Administrative Theme During Development

Many themes are not suitable for your administration area, in particular narrow fixed-width themes. Drupal allows you to select a separate theme just for the admin pages. If you need additional flexibility in defining which pages should render with the admin theme, try the [Administration theme module](/project/admin_theme).

All core themes support all admin pages, so it's a safe bet to assign either Garland or [Blue Marine](http://drupal.org/project/bluemarine) (or [Stark](http://drupal.org/node/1012208) if using Drupal 7) as the admin theme. Go to the Administration theme section on the Appearance page (*Administration \> Appearance*, or `http://example.com/admin/appearance`) and change Administration theme to Stark. In Drupal 6, go to the Administration theme page (*Administer \> Site configuration \> Administration theme*) and change \<system default\> to Garland.

Even if your own theme breaks during development, you will still be able to access the vast majority of your admin pages if you are using a separate admin theme that is stable. The one page where this is not possible is the **Block configuration page** for your theme. Because blocks can be configured on a per-theme basis, Drupal loads up that particular theme. If your theme does not display this page well, you will need to work on it.

Themes such as Zen, Genesis and many others have body class CSS selectors that make it possible to target this page with unique styles, which is one way to selectively theme this page.
