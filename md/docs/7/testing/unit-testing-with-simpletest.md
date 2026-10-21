---
title: "Unit Testing with SimpleTest"
source_url: "https://www.drupal.org/docs/7/testing/unit-testing-with-simpletest"
page_type: page
last_updated: "Last updated on 29 November 2016"
published: "2010-05-27T19:57:21+00:00"
modified: "2016-11-29T14:47:36+00:00"
breadcrumb: ["Drupal 7", "Automated testing for Drupal 7"]
fetched: "2026-10-21T08:09:02Z"
raw: "raw/docs/7/testing/unit-testing-with-simpletest.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Unit Testing with SimpleTest

Note: The code for this tutorial is maintained in the [Examples for Developers module](http://drupal.org/project/examples). This means:

- You can grab a copy there and fiddle with it, change it, experiment with it.
- If you find problems, file an issue there and get it fixed. Patches and improvements are welcome.

Simpletest offers very powerful functionality through its DrupalWebTestCase, but there may be times when you want to write a traditional, simple unit test. Simpletest offers that functionality too. An example of how to write offline unit tests is described in this page.

## What to test?

The purpose of unit testing is to test an isolated piece of functionality, such as functions or methods. For example, a module can have a function with the following implementation:

``` php
function simpletest_example_empty_mysql_date($date_string) {
    if (empty($date_string) || $date_string == '0000-00-00' || $date_string == '0000-00-00 00:00:00') {
        $date_is_empty = TRUE;
    }
    else {
        $date_is_empty = FALSE;
    }

    return $date_is_empty;
}
```

We should test this function under a variety of conditions. For the purposes of this example, we'll only test a few values: NULL, an empty string, '0000-00-00', and a valid date.

## Building the test

The first thing to do is to create a test file. Inside the module folder, create a new .test. In our example simpletest_example.test

In order for Drupal to detect your tests, you need to add the path to your test file inside a 'files\[\]' parameter in your module's .info file. In this case, inside simpletest_example.info, we'll add:

``` php
files[] = simpletest_example.test
```

Now go back to 'simpletest_example/simpletest_example.test' and create a class for the unit tests. This class will extend DrupalUnitTestCase:

``` php
class SimpletestUnitTestExampleTestCase extends DrupalUnitTestCase {

}
```

Just like classes that extend DrupalWebTestCase, our SimpletestUnitTestExampleTestCase class needs to implement the getInfo() method. This method will provide descriptive information on the simpletest page:

``` php
public static function getInfo() {
  // Note: getInfo() strings should not be translated.
  return array(
    'name' => 'Simpletest Example unit tests',
    'description' => 'Test that simpletest_example_empty_mysql_date() works properly.',
    'group' => 'Examples',
  );

}
```

After we have written getInfo(), we can start writing our actual unit tests. All unit test methods should start with 'test' in lower-case. Any public method that starts this way will automatically be recognized by Simpletest and run when requested. Although it is possible to put each assertion into a separate method, testing several different assertions at once is recommended instead and that can be achieved as follows:

``` php
public function testEmptyMySQLDate() {

  $result = simpletest_example_empty_mysql_date(NULL);
  // Note: Test output messages should not be translated.
  $message = 'A NULL value should return TRUE.';
  $this->assertTrue($result, $message);

  $result = simpletest_example_empty_mysql_date('');
  $message = 'An empty string should return TRUE.';
  $this->assertTrue($result, $message);

  $result = simpletest_example_empty_mysql_date('0000-00-00');
  $message = 'An "empty" MySQL DATE should return TRUE.';
  $this->assertTrue($result, $message);

  $result = simpletest_example_empty_mysql_date(date('Y-m-d'));
  $message = 'A valid date should return FALSE.';
  $this->assertFalse($result, $message);

}
```

That's all there is to it. Obviously, you may need to do more complex setup before your assertions, but by their nature unit tests should be much simpler than the full functional tests provided by DrupalWebTestCase.

Once you have written your unit tests, ***clear the cache*** and then follow the directions for running Simpletest for [Drupal 6](/simpletest-tutorial#running_tests) or [Drupal 7](/simpletest-tutorial-drupal7#running_tests).
