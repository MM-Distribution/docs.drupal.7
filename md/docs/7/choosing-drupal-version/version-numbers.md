---
title: "Drupal 7 Version numbers"
source_url: "https://www.drupal.org/docs/7/choosing-drupal-version/version-numbers"
page_type: page
last_updated: "Last updated on 11 April 2017"
published: "2009-05-19T14:57:41+00:00"
modified: "2017-04-11T14:23:17+00:00"
breadcrumb: ["Drupal 7", "Version numbering scheme for Drupal 7 core and contributed modules"]
fetched: "2026-10-21T06:16:41Z"
raw: "raw/docs/7/choosing-drupal-version/version-numbers.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Drupal 7 Version numbers

What do version numbers mean?

## Drupal release versions

Starting with Drupal 5.0, the "5" indicates the major version of Drupal, and the .0 is the minor version i.e. the bug-fix release or patch level. That means that 5.0, 5.1, 5.2 and so on all have the same underlying structure. Collectively, these versions are often referred to as "5.x". Modules for 5.x are generally all compatible with each other and with any Drupal 5.x version of core. However, modules written for Drupal 6.x or 7.x will not work with 5.x and vice-versa.

The newest version in each series fixes problems that were discovered since the previous version, and these fixes sometimes include critical security updates. This newest version will also include all the problem fixes since the first version of this series.

## Development snapshots

A release with "-dev" at the end of the version indicates a development snapshot from the end of a [branch](/node/1066342) (as opposed to an official release from a [tag](/node/1066342)). These snapshots, by their nature, include changing code. It is therefore hard to know exactly what revisions of each file they contain, even if it is a snapshot of a stable branch where only bug fixes and security enhancements are being made (such as the [6.x-dev snapshot release](/node/97368) of Drupal core). This makes them more difficult to debug, and they should be avoided for production sites. Development snapshots also use "x" for the patch level to further indicate the variable nature of the code they contain. Both Drupal core and the contributions can have development snapshots.

## What do version numbers mean on contributed modules and themes?

The version number indicates the version of Drupal core the contribution is compatible with, whether it is a stable or development release, and what specific "patch level" of the code it represents. These numbers have the form:

`Core Compatibility-Major.PatchLevel[-Extra]`

- *Core Compatibility* is required, and will be something like "7.x", or "6.x", to indicate what version of Drupal core this contribution is compatible with. Since the API for Drupal core does not change across stable releases, a module that is compatible with Drupal core 7.4 would also (generally) work with 7.8. This is why the version strings for contributions contain the character 'x' to show that they are compatible with any core release ("7.x") not just a specific version of core ("7.4").
- *Major* is the major revision number, which indicates what set of functionality a given release has, if it is stable (bug-fixes only) or development (new features), and so on. The default branch of a project for a given release of core (for example, the "DRUPAL-7" branch) will be major version 1. By convention, this major revision should always remain stable, and only security patches and bug fixes and limited feature enhancements should be added to it. Optionally, project maintainers could create additional branches, which would have higher major versions (2, 3, etc.). These additional major revisions will be for whatever the maintainer of the project sees fit. It is up to the project maintainer to document on their project node and in their releases how they're using their own branches and what users of their modules should expect from any available major revision numbers. By convention, if the maintainer is adding major new features to a module or doing a complete rewrite, they would use major revision 2 or higher.
- *PatchLevel* is for a specific release of a given major revision. The first release would be patch level 0. As bugs are fixed, each new releases would have a higher patch level number. If the patch level is the letter "x", it indicates a development snapshot (see *\[-Extra\]* immediately below for more information).
- *\[-Extra\]* is optional, and is for specifying things like "-dev", to indicate a development snapshot from the end of a branch (as opposed to an official release from a tag). These snapshots, by their nature, include changing code. It is therefore hard to know exactly what revisions of each file they contain, and this makes them more difficult to debug. Development snapshots also use "x" for the patch level to further indicate the variable nature of the code they contain.

Some example version strings and what they mean should help clarify:

- `7.x-1.0` The initial (patch-level 0) stable release (major revision 1) of a module compatible with any version of Drupal core 7.\*.
- `7.x-2.1` An updated (patch-level 1) new-feature release (major revision 2) of a module compatible with any version of Drupal core 7.\*.
- `6.x-1.0-alpha3` The third alpha (for testing) release of a still unstable release (major revision 1) of a module compatible with any version of Drupal core 6.\*.
- `6.x-1.x-dev` A nightly development snapshot ("-dev") of a stable release (major revision 1) of a module compatible with any version of Drupal core 6.\*.
