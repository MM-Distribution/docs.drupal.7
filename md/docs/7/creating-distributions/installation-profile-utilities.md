---
title: "Installation Profile Utilities"
source_url: "https://www.drupal.org/docs/7/creating-distributions/installation-profile-utilities"
page_type: page
last_updated: "Last updated on 17 October 2016"
published: "2007-10-01T20:59:37+00:00"
modified: "2016-10-17T21:51:40+00:00"
breadcrumb: ["Drupal 7", "Creating Drupal 7 distributions"]
fetched: "2026-10-21T07:52:46Z"
raw: "raw/docs/7/creating-distributions/installation-profile-utilities.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Installation Profile Utilities

There are several Drupal projects that can be used to help you create an installation profile.

## Drush make

Drush make (included as part of the [drush](/project/drush) project since Drush 5) is a [command-line](http://en.wikipedia.org/wiki/Command-line_interface) packaging tool specifically designed for Drupal. It natively supports downloading, unpacking, and installing Drupal modules and themes via a simple configuration file (the 'make' file), and a single command. *Drush make* is the tool used by the Drupal.org packaging system to create [packaged distributions](/node/642116), and is a very useful tool to have in your local development environment for generating, formatting, and verifying `.make` files you'll eventually commit to your profile.

For more information about using `drush make` see [Packaging a distribution on Drupal.org](/node/642116).

## Apps

The [Apps](http://drupal.org/project/apps) module includes install-time integration to enabling users to select which apps to download and enable. Apps can be used to combine components from multiple distributions.

## Drush Recipes

The [Drush Recipes](http://drupal.org/project/drush_recipes) drush plugin allows for the automated creation of .drecipe files which store the drush commands needed to produce something. drecipe files can work either to replace or work in conjunction with installation profiles, distributions and make files. Drush Recipes does much more then install profiles but the command `drush ddt` can analyze a built site and turn it into drush commands necessary to assemble much of it automatically.

## Features

The [Features](http://drupal.org/project/features) module is increasingly the core of install profiles, providing tools for creating diverse types of configuration, from content types and fields to views and user permissions.

## Feature set

The [Feature set](http://drupal.org/project/feature_set) module allows site builders and install profile maintainers to expose a simplified administration page that allows users to enable and disable complete sets of functionality without having to expose the features admin page or the modules administration page to end users.

## Install Profile API

If you're writing a profile for Drupal 5 or 6, you can make use of the [Install Profile API](/project/install_profile_api), which provides a set of helper functions that make it easier to create, update, or delete elements from Drupal's data structures. You will still have to be familiar with PHP as this is not an "end user" module.

## Profile Generator

Drupal 5 and 6 users can get a jump-start on an installation profile by using the [Profile Generator](/project/profile_generator) module to create a profile for an existing site.

## Profiler

The [Profiler](http://drupal.org/project/profiler) module provides a number of tools for building profiles and also allows you to have 'Sub' Install Profiles, where one Install Profile inherits from and extends another Install Profile. [Profiler Builder](http://drupal.org/project/profiler_builder) is a small module to create profiler profiles.

## Profiler Builder

The [Profiler Builder](http://drupal.org/project/profiler_builder) module provides an automated method for production of Installation Profiles. It analyzes your site and automatically authors the required files including drupal.org compliant make files. Profiler builder can work with or without the Profiler module referenced above.

## Subprofiles

The [Subprofiles](http://drupal.org/project/subprofiles) module can be used to provide different "flavors" of your install profile, consisting of different sets of features.

See [Groups.Drupal.org/Distributions](http://groups.drupal.org/distributions) for ongoing discussion about installation profiles.
