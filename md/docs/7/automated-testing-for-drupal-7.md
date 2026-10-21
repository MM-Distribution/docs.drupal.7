---
title: "Automated testing for Drupal 7"
source_url: "https://www.drupal.org/docs/7/automated-testing-for-drupal-7"
page_type: guide
published: "2016-10-15T21:45:36+00:00"
modified: "2020-07-26T17:56:57+00:00"
breadcrumb: ["Drupal 7"]
fetched: "2026-10-21T08:08:00Z"
raw: "raw/docs/7/automated-testing-for-drupal-7.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Automated testing for Drupal 7

SimpleTest is Drupal's custom testing framework. In Drupal 7, SimpleTest became an integral part of the workflow as the Testing core module. It significantly enhanced the way core is developed and enabled major API enhancements. In Drupal 6, it was known as the [SimpleTest contrib module](http://drupal.org/project/simpletest).

Tests in Drupal core are usually one of three types:

- **Functional tests** are most common. They create a fresh database installation and specifically create data for the test in the database and then make assertions based on expected results.
- **Unit tests** work without a database installation in the backend and are useful for isolated functions that don't make assumptions about the larger system.
- **Upgrade tests** use a database dump from an earlier version of Drupal and import that to run update.php and then check assertions.

## [Simpletest Testing overview (Drupal 7)](/docs/7/testing/simpletest-testing-overview-drupal-7)

Testing in Drupal 7 focuses on functional testing instead of unit testing.

## [Testing module](/docs/7/testing/testing-module)

The Testing module (Drupal 7.x and beyond) or SimpleTest module (Drupal 6.x) provides a framework for running automated unit and

## [Simpletest Testing tutorial (Drupal 7)](/docs/7/testing/simpletest-testing-tutorial-drupal-7)

This tutorial will take you through the basics of testing in Drupal 7.

## [Unit Testing with SimpleTest](/docs/7/testing/unit-testing-with-simpletest)

Drupal 7: There may be times when you want to write a traditional, simple unit test. Simpletest offers that functionality.

## [Organizing your test cases](/docs/7/testing/organizing-your-test-cases)

Here are some suggestions for organizing your test cases. It is best to put your test cases in files with certain names in certain locations

## [Selenium testing](/docs/7/automated-testing-for-drupal-7/selenium-testing)

Selenium is a tool which automates browser testing, and so can be used to test your Drupal website.

## [Testing setup and configuration](/docs/7/automated-testing-for-drupal-7/testing-setup-and-configuration)

SimpleTest has a few non-default requirements.

## [Writing upgrade path tests](/docs/7/testing/writing-upgrade-path-tests)

This document explains how to write tests for the Drupal core upgrade path.

## [Running automated tests](/docs/7/testing/run-tests)

Once you have completed the Setup and configuration (enabled the Testing module) you are ready to run some tests.

## [Running tests through command-line with run-tests.sh](/docs/automated-testing/phpunit-in-drupal/running-tests-through-command-line-with-run-testssh)

Basics of how to use run-tests.sh from the command line.

## [Troubleshooting tests](/docs/7/testing/troubleshooting-tests)

Use the new debug()

## [SimpleTest upload tests hanging](/docs/7/testing/simpletest-upload-tests-hanging)

SimpleTests involving file uploading of any kind result in the test never finishing on Mac OS X covering Leopard and possibly other versions

## [SimpleTest \[Browser\] on Vista](/docs/7/testing/simpletest-browser-on-vista)

The Symptom

## [Improving SimpleTest performance](/docs/7/testing/improving-simpletest-performance)

Performance: improving the speed of SimpleTest during development.

## [Testing Reference](/docs/7/testing/testing-reference)

The following resources provide some additional information on testing with Drupal. Please also read the sub-pages with more details.

## [API functions](/docs/7/testing/api-functions)

The internal browser

## [Writing SimpleTest assertions](/docs/7/testing/assertions)

Find up to date SimpleTest documentation at the api.drupal.org reference site.

## [Why test](/docs/7/testing/why-test)

You should write SimpleTests for your modules to ensure quality. SimpleTests allow you, the developer, to quickly test your module after

## [Core tests](/docs/7/testing/core-tests)

Drupal core now comes with numerous tests for functionality (in the region of 50-70% code coverage as of June 2008).

## [Hidden modules and themes](/docs/7/testing/hidden-modules-and-themes)

Sometimes, hooks we want to test are not used in any of the core modules, or core modules do not cover all the use cases of these hooks.

## [Comprehensive example](/docs/7/testing/comprehensive-example)

Now it's time to try a browser test. We don't have to change too much in our class, because DrupalWebTestCase class contains tools for both

## [Miscellaneous SimpleTest tips](/docs/7/testing/miscellaneous-simpletest-tips)

This is a list of some general tips for writing tests, feel free to pitch in and add your own!
