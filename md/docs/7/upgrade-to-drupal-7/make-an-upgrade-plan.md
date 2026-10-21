---
title: "Make an Upgrade Plan"
source_url: "https://www.drupal.org/docs/7/upgrade-to-drupal-7/make-an-upgrade-plan"
page_type: page
last_updated: "Last updated on 11 October 2017"
published: "2009-08-15T19:09:13+00:00"
modified: "2017-10-11T15:03:09+00:00"
breadcrumb: ["Drupal 7", "Upgrade to Drupal 7"]
fetched: "2026-10-21T06:19:16Z"
raw: "raw/docs/7/upgrade-to-drupal-7/make-an-upgrade-plan.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Make an Upgrade Plan

This is a list of things you need to do *BEFORE* you upgrade to Drupal 7. It is important to understand how your existing site is built before you start your upgrade. It is best to practice your upgrade on a test or development site before you upgrade your production site.

If you are unsure about what version your site is running, see the [Drupal Version Numbering](/documentation/version-info) page of the documentation.

## Module and Theme Inventory

Identify the modules that are installed (including ones that are installed and not enabled). To do this, you can either look at the listed modules on the Modules admin page (*Administer \> Site building \> Modules*), or in your *sites/all/modules* directory.

Identify which theme is active on the site by looking at the Themes page (*Administer \> Site building \> Themes*), which shows all installed themes, and which ones are enabled.

Drupal 5 users may benefit from the [Update Status](/project/update_status) module which can make this process much easier. It lists all modules installed on your site, their version numbers, and whether or not the most up to date version is installed. This has been added to core in Drupal 6 and later. The Available Updates page is found at admin/reports/updates. Also useful is the [Update status advanced settings](http://drupal.org/project/update_advanced) module which adds some of the functionality present in contrib that was not included in core.

Write down the complete list of modules and themes installed on your site. You can use this as a checklist when upgrading contributed modules as well as when you disable and re-enable modules during the actual Drupal upgrade.

## Disable and Uninstall Unused Modules

After taking inventory of your modules, you may become aware of modules that your site is not actually using. It is always recommended to disable and remove modules that are not actually in use for both security and performance reasons. During an upgrade you also save yourself from having to update or upgrade unused modules.

## Contributed Module Upgrade Planning

Answer the following questions for each of the modules in your inventory:

1.  Is there a version of the module for Drupal 7? You can find out by visiting the project page on Drupal.org for each of your modules.
2.  Has the module moved to Drupal core? Drupal core often incorporates several key contributed modules into the next release.
3.  Is there an upgrade path for the version of a module you have and the version that is available for the target version? In some cases module authors release multiple versions of a module (e.g. module_name 7.x-1.x and module_name 7.x-2.x).
4.  Does the target version of a module introduce any new dependencies? In some cases new version of modules will have dependencies on other contributed modules that they did not have in previous versions. When you upgrade your site you will need to make sure to install the modules your module depends on.

## Theme Upgrade Planning

If your site uses a contributed theme, you will need to research whether your theme can be upgraded to the target version.

1.  Is there a version of your theme available for the target version of core?
2.  Is your theme based on a theme framework like Zen or 960? What is the upgrade path for those frameworks?

If your theme is entirely custom or is a modified version of a contributed theme or even based on a theme framework, you will need to plan on spending time upgrading the code for your theme at some point prior to upgrading your site. See [Upgrading a theme to a new version](http://drupal.org/update/theme)

## Identify Core Customizations and Contributed Module Customizations

As a rule you should [never 'Hack Core'](http://drupal.org/node/144376 "Do Not Hack Core") i.e. modify core modules or files.  
If, however, you have modified your core Drupal files and modules, it is entirely your own responsibility to make note of those changes and plan your upgrade accordingly.  
The same is true of modified contributed modules.

## Document your Upgrade Plan

Using your module and theme inventory and the research you did planning for your module and theme upgrades begin documenting your overall upgrade plan. This plan should include steps found in [UPGRADE.txt](http://drupal.org/node/550126). Make a list of steps and checklists that you can refer to as you proceed through the upgrade process. There are too many things that are easily forgotten when performing an upgrade and having everything written down ahead of time will save you time and aggravation. Also, having a document like this ahead of time provides you with a place to take additional notes during the upgrade. These notes may prove valuable the next time you have to do an upgrade.

Consider documenting the following as part of your upgrade plan.

- Modules that cannot be upgraded and what alternative choices exist.
- Modules requiring an upgrade before upgrading the core codebase.
- Special upgrade instructions (if any) for each module.
- The order in which modules should be upgraded.
- A plan for testing whether the upgrade was successful.
