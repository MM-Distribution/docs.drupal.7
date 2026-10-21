---
title: "Simpletest Testing overview (Drupal 7)"
source_url: "https://www.drupal.org/docs/7/testing/simpletest-testing-overview-drupal-7"
page_type: page
last_updated: "Last updated on 14 February 2017"
published: "2009-03-08T03:06:07+00:00"
modified: "2017-02-14T04:38:14+00:00"
breadcrumb: ["Drupal 7", "Automated testing for Drupal 7"]
fetched: "2026-10-21T08:08:16Z"
raw: "raw/docs/7/testing/simpletest-testing-overview-drupal-7.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Simpletest Testing overview (Drupal 7)

### Testing methodology

Testing in Drupal 7 focuses on [functional testing](http://en.wikipedia.org/wiki/Functional_testing) instead of [unit testing](http://en.wikipedia.org/wiki/Unit_testing). What this means is that the tests are written in such a way that they test the interface as a whole instead of testing individual functions or finite pieces of code. This focus is because it is more effective for the way Drupal 7 is written. Functional testing ends up being just as effective if not more effective than unit testing especially due to the code style used in these Drupal versions. The testing framework in Drupal 6 and 7 is geared towards this type of testing and the documentation focuses on writing functional tests. In Drupal 8, unit testing is also a good option; this method of testing is geared towards testing small pieces of code separately, and this is much more suited to Drupal 8 because it makes use of Object Oriented Programming much more than its predecessors.

## Separate testing environment

[![Overview of SimpleTest flow](/files/issues/simpletest_overview.png)](http://drupal.org/files/issues/simpletest_overview.png)

The functional testing framework automatically creates a separate environment for each test to run in. This means an entirely separate set of database tables is created along with a separate files directory. Drupal is *installed* into that environment and the tests are performed. What this means is that the tests always start from the same environment and there is no chance for *contamination* from other tests. When you write your test it means that you do not have to *clean up* the environment at the end of each test.

Having a separate environment is necessary to ensure that each test can count on the same "starting position." It also means that changes made to the local development environment will not be present in the testing environment and cannot be tested. Tests should perform all the necessary setup (eg. creating content, creating users, etc).

## Test case layout

Each test case can only have one `setUp()` and `tearDown()` implementation. This means that all tests that require the same set of modules to be enabled and test similar functionality should be grouped in the same test case. Tests that have different setup needs should be moved to a different test case, but kept in the same test file.

## Test file location

In D7, all tests for a module are to be placed in a central test file placed in the root of a module directory. The file name should be in the form `modulename.test`. For example the test file for the node module would be `modules/node/node.test`. If additional test files are needed, like test modules, they should be placed in a `tests` directory that is also placed in the module root.

In D8, each class lives in a separate file which is placed in src/Tests/ folder. For example:  
`/modules/my_module/src/Tests/MyEntityTest.php`

## Run tests

The testing system provides two methods for running tests: a web interface and a command line script. To use the web interface navigate to `admin/build/testing` under site building in the menu (Drupal6), `admin/config/development/testing` under "configuration" (Drupal7). You can then select the tests you wish to run and click the *Run tests* button. You should see a nice progress bar that shows you what percentage of the tests are complete and what the results are so far.

If you prefer to use the command line script it is located in the scripts directory with the name `run-tests.sh`. Please read the documentation included in the file to see how to use it or from a console in the Drupal installation root type: `php ./scripts/run-tests.sh`
