---
title: "Managing Drush make files for an installation profile"
source_url: "https://www.drupal.org/docs/7/creating-distributions/managing-drush-make-files-for-an-installation-profile"
page_type: page
last_updated: "Last updated on 17 October 2016"
published: "2012-03-10T05:25:53+00:00"
modified: "2016-10-17T21:52:09+00:00"
breadcrumb: ["Drupal 7", "Creating Drupal 7 distributions"]
fetched: "2026-10-21T07:53:01Z"
raw: "raw/docs/7/creating-distributions/managing-drush-make-files-for-an-installation-profile.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Managing Drush make files for an installation profile

Drush make is a powerful tool for assembling all the dependencies needed for an installation profile to work as a full Drupal website. It is included as part of [Drush](/project/drush) as of Drush version 5. It is the central tool used for [Packaging a distribution on Drupal.org](/node/642116).

However, to build a fully functional site including the installation profile code itself, things get a bit complicated. You need multiple .make files that work together.

## drupal-org.make

This file defines all of the contributed modules, themes, and 3rd party libraries used by the installation profile. This file will be used in a few circumstances:

1.  When the Drupal.org packaging script builds distribution releases of the installation profile.
2.  When `drush make` builds the installation profile recursively. More on this below.

A trivial example might look something like this:

``` php
api = 2
core = 7.x

projects[views] = 3.3
projects[ctools] = 1.0-rc1
```

For more details, see [Full example drupal-org.make file](/node/1432374).

## drupal-org-core.make

This file is optional. If the distribution requires patches to Drupal core, a -dev release, or a specific Git revision, Drupal.org packaging system needs to know about this in a separate file. For the gory details about why see [\#1455614: Packaging script doesn't allow distributions to patch core or specify a git revision](/project/drupalorg/issues/1455614 "Status: Closed (fixed), Assigned to: dww"). But, for example, this file might look like this:

``` php
api = 2
core = 7.x
projects[drupal][type] = core
projects[drupal][version] = 7.12
projects[drupal][patch][] = http://drupal.org/files/issues/object_conversion_menu_router_build-972536-1.patch
projects[drupal][patch][] = http://drupal.org/files/issues/992540-3-reset_flood_limit_on_password_reset-drush.patch
;projects[drupal][patch][] = http://drupal.org/files/i673020_deliver_1-make_0.patch
```

## build-\[distro\].make

This file is used to build a fully functional website that includes core, the profile code itself, and all of its dependencies. Drush make has a feature where if it downloads something that includes a .make file, it will recursively build that .make file. This can be confusing and at times annoying, but it can also be really helpful. The build-\[distro\].make file utilizes this feature to build core, download the profile, and then let `drush make` build all of the profile's dependencies automatically. For example, in the [OpenPublic](/project/openpublic) distribution, you'll find a file called `build-openpublic.make` (there's no magic about this filename -- "build-\[distro\].make" is just a convention) that looks something like this:

``` php
api = 2
core = 7.x
; Include the definition for how to build Drupal core directly, including patches:
includes[] = drupal-org-core.make
; Download the OpenPublic install profile and recursively build all its dependencies:
projects[openpublic][version] = 1.0-beta6
```

This .make file includes the contents of the `drupal-org-core.make` file in the same directory and directly builds that. It checks out Drupal core version 7.12 and applies some patches. Then this build make file continues and downloads version 7.x-1.0-beta6 of the openpublic installation profile into the profiles/openpublic subdirectory of the version of core it just built. After it's done downloading, it finds a drupal-org.make file in that profile directory, and recursively builds that to pull in all the modules, themes, and libraries that OpenPublic depends on.

So, if you're a developer working on OpenPublic or are just trying to build a copy of it yourself directly, all you need is a copy of those two files, and then you run the command:

`drush make build-openpublic.make /path/to/webroot`

If the profile doesn't require a `drupal-org-core.make` file and is happy with an official release of core, the build make file might look like this, instead:

``` php
api = 2
core = 7.x
projects[drupal][version] = 7.12
projects[openpublic][version] = 1.0-beta6
```

See also:

- [Drush Make - Drupal Distributions Packaging Automation Tool](https://www.drupal.org/node/625094)
- [Drush Make theory for happy profile development](https://www.drupal.org/node/1006620)
