---
title: "Testing module"
source_url: "https://www.drupal.org/docs/7/testing/testing-module"
page_type: page
last_updated: "Last updated on 15 October 2016"
published: "2008-01-21T01:15:20+00:00"
modified: "2016-10-15T22:02:52+00:00"
breadcrumb: ["Drupal 7", "Automated testing for Drupal 7"]
fetched: "2026-10-21T08:08:31Z"
raw: "raw/docs/7/testing/testing-module.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Testing module

The Testing module (Drupal 7.x and beyond) or SimpleTest module (Drupal 6.x) provides a framework for running automated unit and functional tests in Drupal. It can be used to verify a working state of Drupal before and after any code changes, or as a means for developers to write and execute tests for their modules. The original module was based on the [SimpleTest PHP library](http://www.simpletest.org/).

Visit **Administration \>\> Configuration \>\> Development \>\> Testing** (Drupal 7.x or 8.x dev) or **Administer \>\> Site building \>\> SimpleTest** (Drupal 6.x) to display a list of available tests. For comprehensive testing, select all tests, or individually select tests for more targeted testing. (Note: Selecting all tests may take several minutes to complete in Drupal 7.x or below, and if you select too many, they may fail to complete. In Drupal 8.x you may need to increase your max_input_vars setting to 2000 in your php.ini file for the Testing admin page to load. There are far too many tests to run all locally. For a full coverage test, use testbot. Once you have identified the test or group that is failing, run those tests locally.)

After the tests have run, a message will be displayed next to each test group indicating whether tests within it passed, failed, or had exceptions. A pass means that a test returned the expected results, while fail means that it did not. An exception normally indicates an error outside of the test, such as a PHP warning or notice. If there were fails or exceptions, the results are expanded, and the tests that had issues will be indicated in red or pink rows. Use these results to refine your code and tests until all tests return a pass.
