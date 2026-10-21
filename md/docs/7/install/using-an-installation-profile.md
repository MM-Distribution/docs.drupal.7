---
title: "Using an installation profile"
source_url: "https://www.drupal.org/docs/7/install/using-an-installation-profile"
page_type: page
last_updated: "Last updated on 10 October 2017"
published: "2008-09-09T23:19:12+00:00"
modified: "2017-10-10T02:20:56+00:00"
breadcrumb: ["Drupal 7", "Installing Drupal 7"]
fetched: "2026-10-21T05:56:01Z"
raw: "raw/docs/7/install/using-an-installation-profile.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Using an installation profile

## What is an installation profile?

From [Installation profiles](http://drupal.org/project/Installation+profiles):

> Installation profiles provide site features and functions for a specific type of site as a single download containing Drupal core, contributed modules, themes, and pre-defined configuration. They make it possible to quickly set up a complex, use-specific site in fewer steps than if installing and configuring elements individually. For example, an [installation profile for conferences](http://drupal.org/project/cod) might include modules for advanced user registration, attendee profiles, ticketing, and a list of speakers and sessions. Once installed, installation profiles can be configured and customized the same as traditionally-built Drupal sites. Refer to the [installation profile documentation](http://drupal.org/documentation/build/distributions) for more information.

Please note that an installation profile can only be used when you're installing a new Drupal instance. This means that you can not run an installation profile on an existing Drupal to add extra functionality. You can also only select one installation profile per site. For example, it is not possible to install a wiki installation profile along with a French language profile.

The installation of an installation profile is not required, but optional.

Documentation for Distributions and Installation Profiles contain documentation for some of the more popular distributions/installation profiles. [Additional distribution documentation](http://drupal.org/node/1085574) lists documentation that is kept on third-party sites. You should always check first to see if your distribution or installation profile has documentation, as they sometimes also contain installation instructions.

If there isn't an installation profile that fits your needs, consider [creating one](/node/159730) and contributing it to the Drupal community.

## Installing the profile

1.  Follow the usual preparation steps to prepare the Drupal installation:
    1.  [Download and uncompress Drupal](http://drupal.org/documentation/install/download)
    2.  [Create the database](http://drupal.org/documentation/install/create-database)
    3.  [The settings.php file](http://drupal.org/documentation/install/settings-file)
    4.  Be sure to *not* start the installation script just yet.
2.  [Download](http://drupal.org/project/Installation+profiles) the installation profile and unpack it. (You must download the release archive. If you checkout the profile from version control, you will have the profile, but not the dependencies.)
3.  Copy the entire directory that you just unpacked into the `profiles` directory located inside the Drupal root directory. For example, if you have a Drupal installation at `/home/www/htdocs` and you downloaded and unpacked an installation profile called "fooprofile", you would want to copy the entire "fooprofile" directory into `/home/www/htdocs/profiles/fooprofile`.
4.  Read the documentation on the installation pack you downloaded. This can either be found on the profile's project page (example: [Innovation News Installation Profile](http://drupal.org/project/innovationnewsprofile)) or in the README.TXT that came with the download (example: [Drupal Hebrew Installation Profile](http://drupal.org/project/drupalhe)). It should contain installation instructions such as listing the required extra modules and/or themes that you will have to download.
5.  Modules and themes required by the installation profile / distribution may be placed in any of the following directories, including the usual `sites/all/modules` and `sites/all/themes`. Alternatively, modules and themes may be placed within the profile folder itself at `profiles/[profilename]/modules` and `profiles/[profilename]/themes`, or `sites/all/profiles/[profilename]/modules` and `sites/all/profiles/[profilename]/themes` respectively, which will restrict the modules/themes for use only on sites that are installed with the given profile. This is also a desired configuration for packaging and releasing distributions.
6.  Go to your site's install.php to start the installation process.
7.  When you are presented with the option to select a profile, select your desired profile.
