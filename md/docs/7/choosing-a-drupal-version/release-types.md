---
title: "Release types"
source_url: "https://www.drupal.org/docs/7/choosing-a-drupal-version/release-types"
page_type: page
last_updated: "Last updated on 21 March 2025"
published: "2009-05-19T14:53:00+00:00"
modified: "2025-03-21T11:27:22+00:00"
breadcrumb: ["Drupal 7", "Version numbering scheme for Drupal 7 core and contributed modules"]
fetched: "2026-10-21T06:16:57Z"
raw: "raw/docs/7/choosing-a-drupal-version/release-types.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Release types

*This page is related to Drupal 7. Find [here](https://www.drupal.org/docs/8/understanding-drupal-version-numbers/what-are-alpha-and-beta-releases-and-release-candidates) a most recent page for Drupal \>8.*

## What are alpha and beta releases, and release candidates?

Before every official "x.0" stable release of a new major version of Drupal core, there are usually a handful of *alpha releases*, *beta releases* and *release candidates* that are made available. These releases are **not yet stable enough for production use**, but are essential milestones on the way towards the official release. They allow a much wider pool of users to test the latest code and provide feedback before the official stable release. **These releases should only be downloaded and used by developers** very familiar with Drupal **or those wishing to help find bugs** in the software.

The guidelines below are for Drupal core. Some maintainers of contributed modules and themes might choose to provide alpha or beta releases or release candidates of their projects (though this is not required). You should read the release notes carefully in these cases, since the details might vary across projects, though the basics explained here should hold (an "alpha" is less stable than a "beta", which is less stable than an "RC", etc).

### Alpha releases

These are the first to come out, and are therefore the least stable. Most reported errors are resolved but there are most likely still outstanding known issues, which might include security issues.

### Beta releases

Beta releases are usually only created once:

- All critical data loss and security bugs are resolved
- The APIs are frozen enough so that contributed module and theme authors can start upgrading their projects.
- Most of the problems with the upgrade path are fixed and it's possible to successfully upgrade a copy of the Drupal.org database to the new Drupal version.

During the period of beta releases, usability features are still considered, the translatable strings (help texts, words in the interface, etc) might be altered, and if absolutely necessary, the API or database schema could change (to fix a critical bug). Of course, other kinds of bug fixes are always applied.

### Release candidates

Release candidates are usually only created once no more critical bugs have been reported in a given beta release. These are considered nearly stable code, something the Drupal development community is considering as a *candidate* to be released as the official .0 version. No more usability changes are made, and the translatable strings are usually unchanged at this point.

Once a *feature freeze* is announced, no new features will be added to that version of Drupal. That version of Drupal's feature set is locked and any new features or change of behavior will need to go into the next release version.

This doc is cross referenced with [Release naming conventions](https://drupal.org/node/1015226 "Release naming conventions").

## Release stable version

The "Release stable version" of a project is simply that project branch.

Tags are used for creating stable releases. To create a tag for using with the Git Drupal Repository, first, ensure that you're following the tag naming convention if you're using this tag for making a release. From inside the directory of the project, an example is:

``` php
git tag 7.x-1.0 
```

Once the tag is created, you need to push the tag up to the master repository. By itself, push doesn't send the tags up, you also need to tell it to include the tags in the push by appending the --tags flag:

``` php
git push --tags 
```

If you don't want to push all your tags, you can also be specific:  
Example:

``` php
git push origin tag 7.x-1.0 
```

For more information follow this link:-  
[Creating a branch or tag in Git](https://www.drupal.org/node/1066342)
