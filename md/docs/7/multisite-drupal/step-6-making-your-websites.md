---
title: "Step 6: making your websites"
source_url: "https://www.drupal.org/docs/7/multisite-drupal/step-6-making-your-websites"
page_type: page
last_updated: "Last updated on 30 August 2016"
published: "2014-03-24T10:59:58+00:00"
modified: "2016-08-30T13:47:16+00:00"
breadcrumb: ["Drupal 7", "Multisite Drupal 7"]
fetched: "2026-10-21T06:15:24Z"
raw: "raw/docs/7/multisite-drupal/step-6-making-your-websites.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Step 6: making your websites

- Dowload the contributed modules and themes you need. They have to be compatible with your main version of Drupal. The main version is indicated by the first number. For instance, If you have installed Drupal 7.0, the main version is refered to as "7.x", and the modules compatible with it are numbered 7.x-a.b, where a and b are integers (Example: "7.x-3.7"). Versions called "7.x-a.b-dev" are versions in development. Don't worry: you can install and uninstall contributed modules and themes as soon as Drupal is installed, and later at any time. (Before uninstalling anything, check it's not used.) So if you don't know what you will need, you can just begin with Drupal's core modules and themes, and are not required to install any. You can get trouble with development versions, even after you've desintalled them.
- Decompress the modules and themes you have downloaded and read carefully the README.txt and INSTALL.TXT (if any) files in them. Then put into /var/www/drupal7/sites/all/modules/ the decompressed directories of modules which will be used by several sites. Put into /var/www/drupal7/sites/all/themes/ the decompressed directories of contributed themes which will be used by several sites, if you need so. Put into /var/www/drupal7/sites/all/files/ the files (notably pictures) which will be used by several sites if any.
- Open your browser if it's not open yet.

## Bulk loop

- Install in /var/www/drupal7/sites/example.com/modules/ the contributed modules which will only be used by the website called databasename, if any.
- Install in /var/www/drupal7/sites/example.com/themes/ the contributed themes which will only be used by the website whose directory example.com, if any. If, for the sole website example.com, you modify a theme present in /var/www/drupal7/sites/all/themes/ and put the modified version into /var/www/drupal7/sites/example.com/themes/, change its name so that you can easily distinguish the two. Don't change the folder name, but change the name Drupal will display: if you theme is called myTheme, then open the file myTheme/myTheme.info, at the beginning of this file, find the line beginning by "name =" and change what follows the "=" sign. You may also want the change the "description" of the theme, thanks to the line beginning by "description =". Remember that if you modify a copyrighted theme, you need the author's authorisation. If it's a theme distributed with a free license, this authorisation is granted automatically under some conditions, notably that you provide in turn your modified version under a similar license, on request.
- In your brower, visit <http://example> and follow those instructions. You notably have to give your site a title, and to enable the modules and themes you will use. Again, you may enable or disable any module or theme later. But changing theme may cause problems in an existing site, specially if you change for a contributed theme.

**End of bulk loop**
