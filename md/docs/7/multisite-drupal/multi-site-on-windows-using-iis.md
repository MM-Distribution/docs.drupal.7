---
title: "Multi-site on Windows - using IIS"
source_url: "https://www.drupal.org/docs/7/multisite-drupal/multi-site-on-windows-using-iis"
page_type: page
last_updated: "Last updated on 30 August 2016"
published: "2009-08-20T02:40:40+00:00"
modified: "2016-08-30T13:47:11+00:00"
breadcrumb: ["Drupal 7", "Multisite Drupal 7"]
fetched: "2026-10-21T06:12:17Z"
raw: "raw/docs/7/multisite-drupal/multi-site-on-windows-using-iis.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Multi-site on Windows - using IIS

## Prerequisites

This guide assumes you have the following installed and running:

- Microsoft's Internet Information Services web server 6 or 7
- [PhP](http://php.iis.net/) 5.2 or higher with [PDO dlls enabled](http://drupal.org/node/549702).
- The IIS FastCGI Module ([IIS6 version here](http://www.iis.net/downloads/default.aspx?tabid=34&g=6&i=1521) - in IIS7 it's an integrated module that needs to be enabled).
- MySQL
- If you want clean urls, you'll also need the URL Rewrite module (IIS7) or a third-party url-rewrite module set up at some point, though you can do this afterward.

## Process

1.  **Install a site.** This will be the parent site, providing the code-base for all the child sites.

    **IIS7**: be sure your parent site has a web.config file (see [this](http://drupal.org/node/557898) for more info). Child sites will use the settings in the parent site's web.config file. To override these settings, put a web.config file with just the settings you want to override in the child site's folder (eg sites/site2.com/).

2.  **Create child site folders.** Decide how you want people to navigate to your sub-site. In the parent site's /sites/ folder, create sub-folders for each new site you wish to install.

- Example 1: parentsite.com/subsite/ - in parent /sites/ folder, create /sites/parentsite.com.subsite
- Example 2: subsite.parentsite.com - in parent /sites/ folder, create /sites/subsite.parentsite.com
- Example 3: subsite.com - in parent /sites/ folder, create /sites/subsite.com

**Copy the files & private subfolders.** Go into the parent site's sites/default folder, and copy the /files and /private folders. Navigate to each new child site's folder (eg sites/parentsite.com/subsite/) and paste them.

**Create child site settings.php file(s).** Into each child site folder copy the parent's /sites/default/settings.php. Make each settings.php writable to IIS_WPG (IIS6) or IIS_IUSRS(IIS7).

**Create IIS Site Mapping or Virtual Directory**, depending on how you set up your site structure.

**IIS7** - Start the IIS Manager.

- Example 1: parentsite.com/subsite/ - Right-click on parentsite.com \| Add virtual directory. Alias: \[new site name, eg subsite\]. Physical path: \[parent site's physical path\]. Click OK.
- Example 2: subsite.parentsite.com - Right-click on Sites \| Add web site. Site name: \[new site name, eg site2\]. Click to select the application pool, and select the parent site. Physical path: enter the parent site's physical path. Host name: \[new site url, eg site2.localhost\]. Click OK.
- Example 3: subsite.com - add a web site as example 2, calling the host name subsite.com.

**Set up the database(s).**

**Multiple databases** - If you want each site to have it's own database, create them now.

For each child site, change settings.php to include each site's database name, username, and password:

``` php
$databases['default']['default'] = array(
  'driver' => 'mysql',
  'database' => 'databasename',
  'username' => 'username',
  'password' => 'password',
  'host' => 'localhost',
);
```

**Single database** - See [this](http://drupal.org/node/547862) tutorial.

Run the setup script for each site, eg <http://site2.localhost/install.php>.
