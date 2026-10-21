---
title: "Organizing your test cases"
source_url: "https://www.drupal.org/docs/7/testing/organizing-your-test-cases"
page_type: page
last_updated: "Last updated on 30 November 2016"
published: "2009-09-20T22:34:59+00:00"
modified: "2016-11-30T14:18:19+00:00"
breadcrumb: ["Drupal 7", "Automated testing for Drupal 7"]
fetched: "2026-10-21T08:09:18Z"
raw: "raw/docs/7/testing/organizing-your-test-cases.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Organizing your test cases

Here are some suggestions for organizing your test cases. It is best to put your test cases in files with certain names in certain locations. You can share test code, and sample data, by centralizing and organizing your test cases. It is good to make your test cases modular. You can test the database without the overhead of installing your module.

## Where to put test case files

A good place to put your first test cases is in your module's root, in a file named after your module with an extension ".test". For instance, the test file for module **example** would be called **example.test**.****

For your test file to be found, your **modulename.info** file needs to have a line under the files\[\] section which references this test file, i.e. **files\[\] = modulename.test**

If you have test cases in multiple files, a good place to put them is in a subdirectory named **tests/** under your module's root directory. The names of the files are up to you, but they must all have the extension ".test".

Alternatively, you can locate your files according to [PSR-0, the PHP Framework Interop Group's *Autoloading Standard*](http://www.php-fig.org/psr/psr-0/). (See the SimpleTest module code for specifics).

The class containing your test cases must also have a method **getInfo()**, or they will be discarded.

See [function **simpletest_test_get_all()** in `modules/simpletest/simpletest.module`](https://api.drupal.org/api/drupal/modules!simpletest!simpletest.module/function/simpletest_test_get_all/7), which does the actual loading of test classes, for the detailed requirements.

## Centralizing and sharing test code

In many modules different test cases will need to run in different contexts. For example, one set of tests might need test data inserted into the database; another might need the module's tables created but to bypass the module's \_install function.

DrupalWebTestCase and DrupalUnitTestCase can be extended to handle these scenarios and you can see this sort of approach at work in ` modules/simpletest/tests/database_test.test `

## Centralizing the creation of sample data for tests

For consistency, and to save time, you can create all your sample data in a class, and let your test cases inherit it.

``` php
class MyModuleWebTestCase extends DrupalWebTestCase {
  function setUp() {
    parent::setUp('mymodule');
    // Insert your data into the database here
    // Use db_insert() etc. Hard coded SQL will affect your actual drupal installation, not your test environment
  }
}

class MyModuleExampleTestCase extends MyModuleWebTestCase {

  // No setUp() function necessary, because the setUp is inherited

  public static function getInfo() {
    ...
  }

  function testExample() {
    // Your test(s) here
  }
}
```

**Note:** Do not declare a `getInfo()` or any test methods (e.g. `testExample()`) in your parent class (`MyModuleWebTestCase` above). Doing so will cause errors.

## Making your test cases modular

The best test cases are small and modular -- each method such as `testExample()` within your test class should test a small piece of code or functionality.

## Testing the database without the overhead of installing your module

This is an advanced technique that will not be necessary for most test writers.

Tests that do not need any database functionality simply extend DrupalUnitTestCase, but if you wish to test your module's interaction with the database without enabling the whole module, you can use `drupal_install_schema()` to make the necessary tables.

``` php
class MyModuleDatabaseTestCase extends DrupalWebTestCase {
  function setUp() {
    // Create the module's tables without running hook_install or hook_enable
    drupal_install_schema('mymodule');
  }
}

class MyModuleSchemaTestCase extends MyModuleDatabaseTestCase {

  // No setUp() function necessary, because the setUp is inherited

  public static function getInfo() {
    return array(
      'name' => 'Database functions test',
      'description' => 'Tests CRUD functions',
      'group' => 'My Module',
    );
  }

  /*
   * Tests that parent class created module tables
   */
  function testSchemaCreated() {
    // Your test(s) here
  }
}
```
