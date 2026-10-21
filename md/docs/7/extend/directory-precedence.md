---
title: "Directory precedence and multi-site considerations"
source_url: "https://www.drupal.org/docs/7/extend/directory-precedence"
page_type: page
last_updated: "Last updated on 5 February 2018"
published: "2007-09-16T07:46:12+00:00"
modified: "2018-02-05T13:39:31+00:00"
breadcrumb: ["Drupal 7", "Extending Drupal 7"]
fetched: "2026-10-21T06:08:40Z"
raw: "raw/docs/7/extend/directory-precedence.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Directory precedence and multi-site considerations

**Directory Precedence**

Drupal's core modules are located in the /modules directory directly inside the Drupal docroot. Core themes are located in the /themes directory. Additional contributed modules, themes and libraries can be placed in several locations:

1.  Inside the **profiles** directory of the website's installation profile. For example, a website built using the Panopoly installation profile has modules inside directory */profiles/panopoly/modules*, and its theme inside directory */profiles/panopoly/themes*, and libraries inside directory */profiles/panopoly/libraries*.
2.  Inside the **sites/all** directory, e.g., */sites/all/modules*, */sites/all/themes*, */sites/all/libraries*.
3.  Inside the website's configuration directory, which can be either the directory named "default" or a directory whose name matches the website's base domain. In other words, if your website has a base domain of <http://yoursite.com>, Drupal will recognize a named "yoursite.com" as the configuration directory instead of "default," and code will be detected if it is placed in directories */sites/yoursite.com/modules*, */sites/yoursite.com/themes*, and */sites/yoursite.com/libraries*.

If you place versions of the same module or theme in more than one of these locations, Drupal follows an order of precedence to determine which version of that module or theme it will load. Code in the /profiles directory overrides code in Drupal's core /modules directory. Code inside /sites/all overrides code in the /profiles directory. Code inside the configuration directory overrides code in /sites/all. You could, for example, have different versions of the Views module in several locations and a custom theme for yoursite.com, as follows:

- /profiles/panopoly/modules contains Views 7.x-3.11
- /sites/all/modules contains Views 7.x-3.13
- /sites/yoursite.com/modules contains Views 7.x-3.x-dev, and /sites/yoursite.com/themes contains a theme named yourtheme.

If you were using this codebase and Drupal multi-sites to run more than one website, the website at <http://yoursite.com> would use the 3.x-dev version of Views, and all other websites would use the 7.x-3.13 version. The theme named "yourtheme" would only be available to yoursite.com.

This system of directory precedence gives you quite a bit of flexibility and the ability to have different versions of modules -- even core modules and modules associated with an installation profile -- available to different websites all sharing the same codebase.

You can also place modules and themes within subfolders underneath any of the /modules and /themes folders in any of these locations. They will be searched recursively when you visit your admin/build/modules page. You can use this to further organise your available items.

**Multi-site Considerations**

If you use the /sites/all directory for a codebase using multi-sites, then any module or theme installed under it will be available to all sites using the same code base.

If you wish to limit the access to a module or theme to a specific site, then create a modules and/or themes directory under that site's configuration folder.

Anything in a site specific directory will not be accessible to other sites sharing the code base.

**System registry**

Drupal uses the system table in its database (sometimes called the "registry") to keep track of the file location where it should find and load modules, themes and libraries. If you are having trouble getting your website to recognize the correct file location where it should be finding your code, you may need to [rebuild the registry](https://www.drupal.org/project/registry_rebuild).
