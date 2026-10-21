---
title: "Local multi-site installation of Drupal 7 on Linux"
source_url: "https://www.drupal.org/docs/7/multisite-drupal/local-multi-site-installation-of-drupal-7-on-linux"
page_type: page
last_updated: "Last updated on 23 January 2018"
published: "2011-04-02T16:54:27+00:00"
modified: "2018-01-23T12:04:05+00:00"
breadcrumb: ["Drupal 7", "Multisite Drupal 7"]
fetched: "2026-10-21T06:11:00Z"
raw: "raw/docs/7/multisite-drupal/local-multi-site-installation-of-drupal-7-on-linux.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Local multi-site installation of Drupal 7 on Linux

Drupal allows you to run multiple sites from a single Drupal code installation -- each with its own modules, content, theme, etc. For instance, you can run:

- Multiple sites on your local computer.
- Multiple domains in a single hosting account.
- Multiple sub-domains.
- Multiple sub-directory sites.

For a live multi-site installation, see [Multisites Using Drupal 7](http://groups.drupal.org/node/121989).

These pages describe one way to run multiple test sites on your **local** computer with Drupal 7 on Mageia 3 or 4 or Ubuntu 11.04. But the method probably works with little modifications for other distributions. Purposely, we only present one way to do that, in details, and we try to explain a bit what we're doing. We think this procedure probably contains useless things.

**Note**: If you are creating multiple sites, it is necessary to make a list of the desired sites before reading through these instructions completely. Some steps can be done in bulk to save time.

Why to create extra sites? In addition to having several sites running already, you may have some ideas in the back of your head for other sites that you might put up in the future. So before you totally pooh-pooh the idea, give it a few minutes' thought. And you can always change your mind later; it just might be a bit messier then.

## The Basics

In a normal situation, any web page is served by a server to a client, as a meal in a restaurant. "Server" refers both to a computer (usually a mainframe) or to a piece of software. Both are necessary to do the job. Similarly, "client" refers both to a computer (usually a PC) and to a piece of software, such as Mozilla Firefox or Google Chromium. Here, a same computer (yours) will be the server and its own client, but the server and client applications keep separate. In this page, we chose Apache as the server software. You may wonder why a server piece of software is even necessary on your computer. After all, you can just double-click on any HTML file to see it in your browser, even if Apache is not installed. This is because HTML, XHTML, CSS and JavaScript are interpreted client-side, i.e. by the browser itself. On internet, they are served by a server, but, on your local computer, they can be read directly. But Drupal also uses PHP, a programming language interpreted server-side: even on your own computer, if you don't have a server application installed, the program will not be interpreted, and Drupal will not work. In Ubuntu, Apache serves the files in the /var/www/ hierarchy (in Mageia 3 and 4, it is /var/www/html/), except if taught another location.

The main idea in this multi-site installation is that you need **a MariaDB** (or MySQL) **database and a subdirectory** of /var/www/drupal7/sites **for each web site**. It will be easier for you if their names are identical or similar (except for the default site, whose directory is /var/www/drupal7/sites/default and database is "drupal7"). In the instructions below, the site short name is "example", the database name is "company_example", and the site future URL: "example.com". The database will contain your web site text, while the subdirectory /var/www/drupal7/sites/example.com/ (Remember that example.com stands for your website future URL.) will usually contain your web site pictures, specific modules and themes, in subdirectories called "files", "modules" and "themes" respectively. The modules and themes common to multiple web sites are in /var/www/drupal7/sites/all/. The Drupal package installation creates automatically a subdirectory /var/www/drupal7/sites/default/.

## The packages

To install the packages, you can use your distribution's package manager: "Ubuntu software center", "Mandriva control center" or "Mageia control center" (then → "Software management" → "Install & remove software", choosing "All" and "All" in the top left corner except if you want to restrain your search.) etc..

- If your distribution includes Drupal 7, install this package; if prompted to choose between MySQL and MySQLi, choose the latter, and go directly to the paragraph "Mono-site installation of Drupal 7".
- If your distribution doesn't include Drupal 7
  1.  Install Apache, MySQL and PHP: if your distribution includes a meta-package called "LAMP" (Linux, Apache, MySQL, PHP), or "LAMP PHP", use it (In Mageia 3 or 4: Mageia control center → Software management, you can restrain your search to "Meta packages" and "All" in the top left corner. The same for Mageia 3, where the package is called "task-lamp-php".). If your distribution doesn't include such a meta package, install the three packages one by one.
  2.  Install also PhpMyAdmin.
  3.  (Step normally not needed in Ubuntu 11 and Mageia 3 or 4, but might still be needed in other distributions, or may have disappeared for some reason.) Install the PHP-PDO MySQL package: in Mageia 3 and 4, it's called php-pdo_mysql. And enable it: in Mageia 3 and 4, add the line  
      extension=pdo_mysql.so  
      to the file /etc/php.d/70_php.ini .

## Responsibility and acknowledgements

This page, redacted by [Fiable.biz](http://fiable.biz/index%20en.html), includes partial copy and update of the author's contribution to [How to documentation for creating Drupal 7 multisite configuration](http://groups.drupal.org/node/121064) from Drupal's multisite group and [Local multi-site installation of Drupal](http://wiki.mandriva.com/en/Local_multi-site_installation_of_Drupal#Setting_the_hostnames) from Mandriva wiki. [NancyDru](http://drupal.org/user/101412) and [jcl_vanier](http://forum.mandriva.com/fr/viewtopic.php?t=130810) are also to thank for the latter.

## Other resources

[Configuring a basic multisite development environment in Linux](http://drupal.org/node/823990)  
[Migrating a site](http://drupal.org/node/776864)

[Directory selection rules](https://api.drupal.org/api/drupal/sites%21default%21default.settings.php/7.x)

[Multi-site directory aliasing feature.](https://api.drupal.org/api/drupal/sites%21example.sites.php/7.x)

## Steps to follow
