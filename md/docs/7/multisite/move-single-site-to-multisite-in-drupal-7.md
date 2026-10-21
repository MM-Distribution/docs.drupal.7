---
title: "Move single site to multisite in Drupal 7"
source_url: "https://www.drupal.org/docs/7/multisite/move-single-site-to-multisite-in-drupal-7"
page_type: page
last_updated: "Last updated on 14 July 2025"
published: "2012-10-21T15:35:36+00:00"
modified: "2025-07-14T22:17:30+00:00"
breadcrumb: ["Drupal 7", "Multisite Drupal 7"]
fetched: "2026-10-21T06:15:55Z"
raw: "raw/docs/7/multisite/move-single-site-to-multisite-in-drupal-7.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Move single site to multisite in Drupal 7

This is a simple howto for moving single coded website to a multi-site environment. I had a few White Screens Of Death (WSOD) before I gained the wisdom to write this (and hopefully help others).

**the environment.**

So, Drupal 7 website is created ([www.site1.com](http://www.site1.com)) and we would like to take advantage of Drupal's multisite functionality by adding a second site ([www.site2.com](http://www.site2.com)) that will be using the same libraries, modules and themes as in [www.site1.com](http://www.site1.com).

Probably on a shared web-hosting and just want to make life easier.

We already know that libraries/modules/themes placed in /sites/all will be used for all websites, and libraries/modules/themes placed in /sites/site2.com will be used by site2.com only.

We already know that we should take out (uninstall and delete) any libraries/modules/themes that aren't used in site1 or site2.

The first website is using the primary domain name, which by default points to /public_html. This website domain name is not a site that has a content, it's the 'master site', the 'bearer'.

[www.site2.com](http://www.site2.com) already has content, so we only want to move it from a single setup to a multi-site environment under [www.site1.com](http://www.site1.com), within the same hosting provider.

**The steps**

- Backup the files and the database
- Put site2.com offline
- Update Drupal core and all the libraries/modules/themes to their latest releases; both on site1 and site2, so they have the same release number
- Run database updates on both
- Create a folder site2.com (no www) and place it in the /sites folder of the site1.com installation.  
  So it looks like this:` /public_html/site2.com`
- In site2.com, change the files directory to /sites/site2.com/files
- Copy all the libraries, modules and themes that were used in site2.com to /sites/all  
  *...this is essential: if Drupal (the mysql) has been configured for single use, it will search for the libraries/modules/themes in /sites/all only*
- Copy the /files directory of site2.com to /sites/site2.com, so it now looks like this: `/public_html/sites/site2.com/files`
- Copy settings.php into the site2.com folder, so it looks lie this: ` /public_html/sites/site2.com/settings.php`  
  *Don't change a single word in settings.php*
- In the control panel (od site5.com), point site2.com to the folder of site1.com - in my case, to `/public_html`  
  *...Drupal will do the rest*
- Type [www.site2.com](http://www.site2.com) in the web-browser and arrive at site2.com that is now using the shared codebase of site1.com
- Run site2.com/update.php just to make sure that all is good.

Disable update checks for site2.com (they are enabled for site1.com)

If a specific module is to be used only for site2,

- Disable that module in both site1 and site2 and uninstall/delete it.
- Move the module to /sites/site2.com/modules.  
  *So, for admin_menu it looks like this:* `/public_html/sites/site2.com/modules/admin_menu`
- But then checks for updates for site2.com should be re-enabled, otherwise one wont be able to see the update to this module. Same for themes and libraries

If an update Drupal from say 7.15 to 7.16 is performed, /update.php needs to run on both site1 and site2 immediately. The same applies to any upgrade of modules or themes.

**Security warning:** In /admin/reports/updates/settings, one should click "Check for updates of disabled modules and themes", so that modules that are not used on the master Drupal installation (site1) are checked, especially for security updates.  
Again, don't keep modules that are not used on any website.
