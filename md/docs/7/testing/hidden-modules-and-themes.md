---
title: "Hidden modules and themes"
source_url: "https://www.drupal.org/docs/7/testing/hidden-modules-and-themes"
page_type: page
last_updated: "Last updated on 15 October 2016"
published: "2008-09-01T10:38:09+00:00"
modified: "2016-10-15T21:58:40+00:00"
breadcrumb: ["Drupal 7", "Automated testing for Drupal 7"]
fetched: "2026-10-21T08:12:55Z"
raw: "raw/docs/7/testing/hidden-modules-and-themes.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Hidden modules and themes

Sometimes, hooks we want to test are not used in any of the core modules, or core modules do not cover all the use cases of these hooks.

However, Drupal's testing framework allows hidden modules and themes to be tested.

(See [\#953336: Contributed modules are not able to test theme-related functionality](/project/drupal/issues/953336 "Status: Closed (fixed)") for testing theme-related functionality in modules.)

### Creating a hidden module or theme

A hidden module or theme is just like a regular module or theme. The only difference is that it is hidden from the normal user by adding a `hidden = TRUE` line to the `.info` file.

Hidden modules should be put in the `tests` subdirectory of the module they are meant to test, or in the `modules/simpletest/tests` directory for hooks defined by core in one of the include files.

As an example, the `XML-RPC Test` module, that tests XML-RPC hooks, is in `modules/simpletest/tests/xmlrpc_tests.module`. Its info file is written this way:

``` php
name = "XML-RPC Test"
description = "Support module for XML-RPC tests according to the validator1 specification."
package = Testing
version = VERSION
core = 7.x

hidden = TRUE
```

The `hidden = TRUE` property instructs the administrative interface to hide this module from the user.

In `modules/simpletest/test/xmlrpc.test`, we simply have:

``` php
  /**
   * Implementation of setUp().
   */
  function setUp() {
    parent::setUp(array('xmlrpc_test'));
  }
```

To install the test modules during the setUp phase.
