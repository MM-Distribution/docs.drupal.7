---
title: "Distribution developers guide"
source_url: "https://www.drupal.org/docs/7/creating-distributions/distribution-developers-guide"
page_type: page
last_updated: "Last updated on 11 March 2021"
published: "2012-05-01T01:53:02+00:00"
modified: "2021-03-11T21:35:31+00:00"
breadcrumb: ["Drupal 7", "Creating Drupal 7 distributions"]
fetched: "2026-10-21T07:52:14Z"
raw: "raw/docs/7/creating-distributions/distribution-developers-guide.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Distribution developers guide

## Relevant specifications

As you develop your distribution, you can take steps to ensure that what you build is compatible with the features provided by other distribution developers.

- The [Kit](http://drupal.org/project/kit) feature specification provides specific guidelines for ensuring your distribution's features integrate with diverse sites and the features provided by other distributions.
- The [Open App](http://groups.drupal.org/open-app-standard/oas) specification provides specific guidelines for ensuring your distribution's features integrate with diverse sites and the features provided by other distributions.

Efforts are underway to expand the Kit specification, see [\#1456518: Governance of the Kit Spec](/project/kit/issues/1456518 "Status: Active"). One extension of the Kit specification is [Debut](http://drupal.org/project/debut), which provides extended guidelines for feature integration.

See also [\#1554852: Define Drupal Distribution Experience (#DDX) commitment](/project/kit/issues/1554852 "Status: Active").

## Key tools

- The [Features](http://drupal.org/project/features) module is the leading tool for capturing bundles of configuration in Drupal distributions.
- [Drush make](https://www.drupal.org/node/625094) is a powerful command line tool for automating parts of the distribution process.

## Additional tools

- [Apps](http://drupal.org/project/apps) "provides facilities to download modules and all of their dependencies in one easy step".
- [Feature set](http://drupal.org/project/feature_set) "allows site builders and install profile maintainers to expose a simplified administration page that allows users to enable and disable complete sets of functionality without having to expose the features admin page or the modules administration page to end users".

See also links to articles and tutorials on the [additional distribution documentation](http://drupal.org/node/1085574) handbook page.

## Best practices

- *Distinguish between "hard" and "soft" configuration*. When building a distribution, some configuration should be left for site admins to override rather than being hard set. See [Hard and Soft configuration in Drupal Distributions](http://nuvole.org/blog/2012/feb/07/hard-and-soft-configuration-drupal-distributions) for details.

## Packaging your distribution

See the section on [packaging a distribution on Drupal.org](/developing/distributions/drupalorg) for detailed instructions.
