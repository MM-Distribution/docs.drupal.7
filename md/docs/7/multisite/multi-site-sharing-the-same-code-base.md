---
title: "Multi-site - Sharing the same code base"
source_url: "https://www.drupal.org/docs/7/multisite/multi-site-sharing-the-same-code-base"
page_type: page
last_updated: "Last updated on 16 January 2020"
published: "2008-04-25T05:58:07+00:00"
modified: "2020-01-16T22:55:55+00:00"
breadcrumb: ["Drupal 7", "Multisite Drupal 7"]
fetched: "2026-10-21T06:10:29Z"
raw: "raw/docs/7/multisite/multi-site-sharing-the-same-code-base.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Multi-site - Sharing the same code base

If you are running more than one Drupal site, you can simplify the management and also can upgrade your sites by using the multi-site feature. Multi-site allows you to share a single Drupal installation (including core code, contributed modules, and themes) among several sites.

This is particularly useful for managing the code since each upgrade only needs to be done once. Each site will have its own database and its own configuration settings, so each site will have its own content, settings, enabled modules and enabled theme. However, the sites are sharing a code base and web document root, so there may be security concerns with multiple administrators. (See section"[Security Concerns](#security)" below for more information).

## Overview of the Process

To create a new site using a shared Drupal code base you must complete the following steps:

1.  Create a new database for the site (if there is already an existing database you can also use this by defining a prefix in the installation procedure).
2.  Create a new subdirectory off of the 'sites' directory with the name of your new site. ( e.g., `sites/example.com/` ) See [below](#domains-urls) or the comments in the [`default.settings.php` file](https://api.drupal.org/api/drupal/sites!default!default.settings.php/7.x) for information on how to name the subdirectory. Create a files directory in subdirectory and allow the webserver write permissions to it.
3.  Copy the file `sites/default/default.settings.php` into the subdirectory you created in the previous step and name it as `settings.php`.
4.  For Drupal 8 only: Activate the multi-site feature by copying (and renaming) the file `sites/example.sites.php` to `sites/sites.php`. There is no need to edit the file unless you need site aliases. For Drupal 7: There is no need for sites.php file unless you need [site aliasing feature](https://api.drupal.org/api/drupal/sites%21example.sites.php/7.x). The normal [site selection rules](https://api.drupal.org/api/drupal/sites%21default%21default.settings.php/7.x) applies. 
5.  Adjust the permissions of the new site directory to [grant write permissions to the configuration file (`settings.php`).](http://drupal.org/documentation/install/settings-file)
6.  If you are using a subdirectory such as `example.com/subdir` and not a subdomain such as `subd.example.com` you can probably have to create a symbolic link for each site. See the [subdirectory multi-site](#symlink) section below for details.
7.  In a Web browser, navigate to the URL of the new site and continue with the standard Drupal installation procedure (if you get an infinite redirection loop, check if the file `install.php` exists in the document root).

It may also be necessary to modify your Web server's configuration file (often named `httpd.conf` for Apache) to allow Drupal to override Apache's settings. This is true for all installations in Drupal and It is not specific to the multi-site install. Additional information is available in the [Best Practices: Configuring Apache and PHP for Drupal in a Shared Environment](http://drupal.org/node/36628) section of the Install Guide.

## Details of the Process

### Domains, URLs, and sites subdirectory name

The new subdirectory of the sites directory has a name that is constructed from the site's URL. For example, the configuration for `www.example.com` would be in `sites/example.com/settings.php`. No need to include 'www' as part of the directory name.

Drupal will use the same `sites/example.com` directory for any subdomain of `example.com`, including www, unless there is an alternative, matching subdomain sites subdirectory. For instance, URL `http://sub.example.com` would be served from `sites/sub.example.com`, if it exists.

For a subdirectory URL, such as `http://example.com/subdir`, name the sites subdirectory as follows: `sites/example.com.subdir` -- and read the section below on getting subdirectory multi-site working.

If you are installing on a non-standard port, the port number is treated as the first part of the subdomain. For example, `http://www.example.com:8080` could be loaded from `sites/8080.example.com`. If that directory doesn't exist, Drupal would then look for `sites/example.com`, just like a real subdomain.

### Site-specific modules and themes

Each site configuration can have its own site-specific modules and themes in addition to those installed in the standard 'modules' and 'themes' directories. To use site-specific modules or themes, simply create a 'modules' or 'themes' directory within the site configuration directory. For example, if sub.example.com has a custom theme and a custom module that should not be accessible to other sites, the setup would look like this:

    sites/sub.example.com/settings.php 
    sites/sub.example.com/themes/custom_theme 
    sites/sub.example.com/modules/custom_module

### Document root

One area of frequent confusion is that in a Drupal multisite installation the webserver document root is the same for all sites. For example with the following three sites: `example.com, sub.example.com and example.com/site3` there will be a single Drupal directory and all the three sites will be calling the same index.php file.

Some webhosts automatically creates a new directory (i.e. example.com) when creating a new domain or subdomain. In this case it is necessary to make it into a symbolic link to the main Drupal directory, or better yet, when creating the domain or subdomain, set it to use the same document root as the site where you have Drupal installed.

### Subdirectory multi-site

If you are attempting to get Drupal multi-site working using subdirectory URLs rather than subdomain or different domain URLs, you may encounter problems. You'll start out by making a directory such as `sites/example.com.subdir`, and putting a settings.php file there. If this works for you, great! But it probably will not ...

To make it work read [the subdirectory specific multi-site documentation](/docs/7/multisite-drupal/multi-site-in-subdirectories) - also if it happened to work for you.

### Localhost alias for local workstation

On many systems it is possible to create entries in a "hosts" file to create aliases for the localhost name for a local workstation. By creating aliases for localhost it is possible to create names such as localdev1.example.com and localdev2.example.com, both for the local computer.

If on the other hand you use subdirectories in your local web root, create a symbolic link like this:

``` php
ln -s drupaldir subdir
```

and name your site folder localhost.subdir.

### Domain name changes

Once a site is in production in a particular subdirectory under the sites directory, the subdirectory should not be renamed, even if the Web site URL changes. This is because several database tables (for example: system and files) include references to "sites/[www.mydomain.com](http://www.mydomain.com)." Instead of renaming the sites directory, you can create a symlink to the new URL from the old one. Navigate to the sites directory and then use the following command:  
`$ ln -s /path/to/drupal/sites/old.domainname.com new.domainname.com`

## Security Concerns

You might want to reconsider using Drupal's multi-site configuration, in situations where the administrators for all of the sites being run from the same code base are not either the same person or a small group with a high level of mutual trust. The reason is that anyone with full administrative privileges on a Drupal site can execute arbitrary PHP code on that site through various means (even without FTP access to the site), and that arbitrary PHP code could be used from one site to affect another site, if the two sites are in the same HTTP document root and sharing the same Drupal code.

So, unless you completely trust all of the administrators of the sites you are considering running from the same Drupal code base to be knowledgeable, careful, and not malicious, you might want to consider installing their Drupal sites in completely separate areas of the web server that are not able to affect each other via PHP scripting.

### Exploits

Occasionally, Drupal is subject to [security vulnerabilities](https://www.drupal.org/security), bugs which allow an unauthorized user access to Drupal core code. Once a hacker has access to your core code, they have access to *all* your multisites through one attack. Non-multisites require separate attacks, which may offer sufficient time for the vulnerability to be secured.

## When to multisite

As a general rule on whether to use multisite installs or not you can say:

- If the sites are for the same client and it is to simplify the scope of each site, **consider it**.
- If the sites are similar in functionality, use the same modules or use the same Drupal distribution, **consider it**.
- If you have limited resources / staffing, but lots of sites to manage and maintain, **definitely consider it**.
- If the functionality or scope are different, **don't use multisite**.
- If you are managing multiple distributions, **don't use multisite**.
- If the clients are different, **don't use multisite**.

The DrupalCon Austin (2014) conversation / debate on multisite where the pros, cons, and some suggestions are discussed by a wide audience of user perspectives is [available on youtube](https://www.youtube.com/watch?v=9dJxEUM2YOY).

Multisite is popular when you want your sites to stay as up-to-date as possible regarding Drupal module security updates but when you have different functionality, this is more difficult to do because it takes a more time to test each site independently. If you are doing multisite, then the update needs to be run at the same time for all the sites which is not always possible. If this is a concern or you have a very large multisite but still favor the approach, you may want to consider exploring a drush plugin called [DSLM](https://www.drupal.org/project/dslm) that treats multisite management a little differently but with the same advantages.

Sites with different functionality usually end up being upgraded at different times because each needs to be tested and backed up. Site updates and backups can be automated with drush with or without multisite though the @sites target available to drush simplifies bulk application of commands to multisites.

## Recommended Multisite Configuration details

These are not hard and fast rules but will certainly help prevent you from painting yourself into a corner with multisite.

### Use Drush to manage deployment / site upgrades

Drush is a powerful CLI that allows for scripting commands against Drupal sites. When combined with multisites, they become much easier to manage at scale. Drush aliases (which allow referencing groupings of sites / targets with single commands) are critical to successfully managing large multisite deployments. For example, many educational institutions run multisites with well over 100 to 1000 sites running off a single multisite.

### Use sites.php to manage sites

Use the included sites/sites.php (Drupal 7.x) or sites/sites.example.php (Drupal 8.x.x) to reference sites in a multisite instead of address based. This will allow you to migrate between deployments (eg. dev, stage, prod) more easily. Traditional multisite configuration would have you create directories like `sites/my.new.domain.address/settings.php` but you don't need to use the domain as the folder name for it to work. In sites.php you can make a reference like `'my.new.domain.address' => 'project/version1'`. By doing this, you make it possible to use sites.php mappings on dev that look more like `our.dev.address` and still have it point to `project/version1` as its target.
