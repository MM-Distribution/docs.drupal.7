---
title: "Testing with SimpleTest"
source_url: "https://www.drupal.org/docs/7/creating-custom-modules/testing-with-simpletest"
page_type: page
last_updated: "Last updated on 21 September 2016"
published: "2011-04-15T13:32:10+00:00"
modified: "2016-09-21T18:04:23+00:00"
breadcrumb: ["Drupal 7", "Creating custom modules in Drupal 7"]
fetched: "2026-10-21T07:25:52Z"
raw: "raw/docs/7/creating-custom-modules/testing-with-simpletest.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Testing with SimpleTest

**Main topic described: *SimpleTest, Assertions***  
**Main function described: *module_invoke()***  
**Main class described: *DrupalWebTestCase***

Drupal 7 includes testing capabilities in core. The Drupal SimpleTest module is based on the [SimpleTest PHP Library](http://simpletest.sourceforge.net/). If you are familiar with that framework, you should have no trouble learning its application in Drupal.

Drupal testing focuses on functional testing rather than unit testing. Functional tests check the interface as a whole rather than individual functions or finite pieces of code. This approach is more effective for the way Drupal is written. We are just getting started with testing, so we will write very basic tests that ascertain if our four main hooks function as expected.

Part of the challenge of writing good tests is knowing what you need to test. The information you'll get from these tests won't tell you much about how the module really functions. These tests will expose you to the testing environment and several of the assertions. For a discussion of how to design your tests, see the [Figuring out what we need to test](http://drupal.org/simpletest-tutorial-drupal7) section of the SimpleTest tutorial. And once you are comfortable with these rudimentary tests, you will be better prepared to investigate the many tutorials and other resources in the [SimpleTest](http://drupal.org/simpletest) section of drupal.org.

### Create the file

To get started, first we'll create and register a test file. Test files must take the form `{modulename}.test`. Create a PHP file in your `current_posts` directory, named `current_posts.test`, again with only an opening PHP marker and no `.php` suffix.

Like the Database API, the SimpleTest framework uses object oriented programming. Tests are written as classes. As explained back in [Telling Drupal about your module](http://drupal.org/node/1075072), all modules must declare any code files containing class declarations in the `.info` file. Add the following at the end of your `current_posts.info` file:

``` php
files[] = current_posts.test
```

### Extend the class

Next, we will add a doc block and begin writing the tests. Add the following to your test file:

``` php
/**
 * @file
 * Tests for the Current posts module
 */

class CurrentPostsTestCase extends DrupalWebTestCase {
  public static function getInfo() {
    return array(
      'name' => 'Current posts module functionality',
      'description' => 'Tests hooks in the Current posts module',
      'group' => 'Current posts',
    ); 
  }
```

We will write all of our tests as methods of the class `CurrentPostsTestCase`. Note the standard for capitalization. Each word in the class name should be capitalized. Then in methods, the first word is small case, but each additional is capitalized, as in `getInfo()`. Underscores and dashes should not be used in class or method names.

The base class `DrupalWebTestCase` provides the framework for running our tests, building an internal Drupal site and browser as a context for the tests. See [API functions](http://drupal.org/node/265762) for a full exploration of its capabilities. SimpleTest also provides the class `DrupalUnitTestCase` for unit tests of functions that do not require the full bootstrapped Drupal.

The `getInfo()` method is necessary for any SimpleTest you write for Drupal. Without it, your tests will not run. The elements in the array determine how your test appears in the list of tests in your Drupal installation.

### `setUp()` method

The next piece of code looks very simple:

``` php
  public function setUp() {
    parent::setUp('current_posts');
  }
```

With this, we call a method of the parent class to do whatever setup is necessary. You can create a user, specify special permissions, and log the user in. All we need is to install the module we pass as an argument, in this case, of course, `current_posts`. Our tests will run without this method, but we include it because more often than not, you will need setup for your tests.

### First test and `module_invoke()`

Next, add the following:

``` php
  public function testPermission() {
    $data = module_invoke('current_posts', 'permission');
```

We'll begin the test methods with one of our simplest hook implementations, `current_posts_permission()`. We start by creating a variable `$data` to hold the results from `module_invoke()`. This function takes two parameters, the name of the module, and the name of the hook. When it runs, it's effectively the same as calling `current_posts_permission()`, which is exactly what we want. Each of our tests will begin with a call to this function.

### Assertions

Once we have invoked the hook, the actual tests are done through [assertions](http://drupal.org/node/265828), a group of methods that check for a condition and return a Boolean. If `TRUE`, the test passes, if `FALSE`, the test fails. They take the form of `$this->assertion(condition(s), message)`. The message is wrapped in `t()` for translation and will be shown after the tests are run to indicate what was tested.

Add the following tests for this hook to your `testPermission()` method:

``` php
    $this->assertTrue(is_array($data), t('Permission hook returns array.'));
    
    $this->assertTrue(array_key_exists('access current_posts content', $data),
    t('Permission is as expected.'));
  }
```

`assertTrue` checks that the first argument resolves to true. The second argument is the message shown on the test result screen after the tests run. We ask first if the function returns an array, and then if the string for our permission is a key in the array. The messages reflect what we expect to find. That's it for our method to test `current_posts_permission()`.

### Tests for equality

Next we will test the menu hook. Add the following to your test file:

``` php
  public function testMenu() {
    $items = module_invoke('current_posts', 'menu');
    
    $this->assertEqual(2, count($items), t('Two items in menu.'));
    
    $this->assertIdentical($items['admin/config/content/current_posts']['title'], 
    $items['current_posts']['title'], t('Titles are identical.'));
  }
```

(Note the last assertion above is on two lines only to fit on the page. You should not include a line break in your file.)

After invoking the module, we use two more assertions. `assertEqual()` works like the `==` operator. It asserts that the two conditions in the argument are equal, that 2 (known value) equals the result of `count($items)` (tested value). Here it means the implementation creates two menu items, so we put that in our message.

`assertIdentical` works like the `===` operator. With this assertion, we check that the titles of the two menu items are exactly the same and reflect that in the message.

### Another assertion

Here's the code for the next test method:

``` php
  public function testBlockView() {
    $data = module_invoke('current_posts', 'block_view', 'current_posts');
        
    $this->assertEqual(t('Current posts'), $data['subject'], t('Subject is as expected.'));
    
    $this->assertNotNull($data['content'], t('Block contains data.'));
  }
```

In our tests for `current_posts_block_view()` we have a third argument for `module_invoke()`, telling the method to call the `current_posts` case of that function. We first use the equality assertion to test the string set as the subject of the block. Be careful with a test like this. It will break if you change the subject of the block without also changing the test. It works well as an example, but in practice you would only use a test like this for an important string unlikely to change.

Next we use `assertNotNull()` to check that the first argument does not resolve to null. We expect the variable to contain data and state that in the message.

### Two negative assertions

Add the following to test `current_posts_block_info()`:

``` php
  public function testBlockInfo() {
    $info = module_invoke('current_posts', 'block_info');
    
    $this->assertNotEqual('DRUPAL_CACHE_PER_USER', $info['current_posts']['cache'],
    t('Cache is not set to DRUPAL_CACHE_PER_USER'));
    
    $this->assertFalse(count($info) > 1, t('No more than one block defined.'));
  }
```

(Again, don't include line breaks in your code where the lines wrap here on the page.)

`assertNotEqual()` works much like its equality counterpart, comparing the first, known value to second, tested value. Here we check that the cache is not set to 'DRUPAL_CACHE_PER_USER'. Note the tested value delves deeper into the variable with an additional key.

With `assertFalse` we use a formula for the tested value, checking that the function does not define more than one block.

### Invoking two modules

Add the following code to your file to finish off the tests:

``` php
  public function testBlock() {
    $info = module_invoke('current_posts', 'block_info');
    $data = module_invoke('current_posts', 'block_view', 'current_posts');
      
    $this->assertIdentical($info['current_posts']['info'], $data['subject'], t('Block list 
    name and subject are identical.'));
  }
}
```

Here we invoke both of the block functions in our module and compare the strings set in each, using the `===` assertion. That's it for `current_posts.test`.

### Check

SimpleTest is part of core but not installed by default. To be sure it's enabled, go to *Modules* (`http://example.com/admin/modules`) and look for the core module called 'Testing'. Check the box beside it and save to enable it, then click the 'configure' link and be sure 'Provide verbose information when running tests' is checked. The more information you get from your tests the better.

Now enable your 'Current posts' module at *Modules*. If your module is enabled, disable and re-enable it. Navigate to the 'Testing' page at *Configuration \> Development (link) \> Testing (link)* (`http://example.com/admin/config/development/testing`) and look for the 'Current posts' test in the list. If you have been running tests already, you may need to click the 'Clean environment' button at the bottom of the page to get your test to show up.

Once everything is set, check the box for the 'Current posts' test, then click the 'Run tests' button. You'll see a progress bar as your tests are run. Be patient; it takes awhile to create the virtual environment and run all the tests. Note that the phrase under the progress bar matches what you coded for the `name` key of the `getInfo()` method.

When the tests are finished, you will see a message indicating whether they passed, failed, or had exceptions. To see details for each test, click the link below, again the name of the tests, 'Current posts module functionality.' A pass (green background) means that a test returned the expected results, while fail (red background) means that it did not. An exception (yellow background) normally indicates an error outside of the test, such as a PHP warning or notice. If there were fails or exceptions, go back and check your code, then try again until all are green.

### View the code

You can view all the code for this SimpleTest file here: [current_posts.test](http://drupalcode.org/sandbox/jn2/1117260.git/blob/62795e39402fd29a0c5069b2386c25f7a994d863:/current_posts.test)

### See also

- [SimpleTest PHP Library](http://simpletest.sourceforge.net/)
- [SimpleTest tutorial](http://drupal.org/simpletest-tutorial-drupal7)
- [SimpleTest section](http://drupal.org/simpletest)
- [API functions](http://drupal.org/node/265762)
- [module_invoke()](http://api.drupal.org/api/drupal/includes--module.inc/function/module_invoke/7)
- [Assertions](http://drupal.org/node/265828)
