---
title: "Troubleshooting tests"
source_url: "https://www.drupal.org/docs/7/testing/troubleshooting-tests"
page_type: page
last_updated: "Last updated on 20 December 2016"
published: "2009-03-08T05:55:51+00:00"
modified: "2016-12-20T08:02:14+00:00"
breadcrumb: ["Drupal 7", "Automated testing for Drupal 7"]
fetched: "2026-10-21T08:10:35Z"
raw: "raw/docs/7/testing/troubleshooting-tests.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Troubleshooting tests

### Use the new debug()

If you are using the latest version of simpletest in Drupal 7 you can use the [debug feature.](http://drupal.org/node/296574) The debug feature and the verbose mode are explained [here](http://blog.boombatower.com/drupal-7-debug-and-simpletest-verbose).

### Print out Random Variables

Often you want to print out variables to see what they contain. In simpletest this is not particularly possible, but you can output them to the results screen inside the message associated with a test that has passed:

``` php
$var = $this->doAwesomeStuff($settings);
$this->pass(var_export($var, TRUE));
```

### View the content of the Current Page

Many tests will get a page, or post to a page. By enabling 'Verbose mode' in Simpletest's settings, you can view each page via links in the test results. Be warned that this is not a perfect representation of the page as it would be seen by a human user.

For example, uploaded images are rendered as usual, but will not be visible in this viewer. (Typically because the test files no longer exist by the time you're reviewing this HTML. They were removed during Simpletest's clean-up process.)

You can also use this code to write the page to a file in your site's root directory:

``` php
file_put_contents('output.html', $this->drupalGetContent());
```

### 0 bytes from a GET

It's possible to get messages like:

> GET <http://example.local/member> returned 0 (0 bytes).

As a failure. This is usually an indication of a "white screen of death" in your site, but can also be caused by a DNS lookup failure, or other failure to make a HTTP request to the site. Make sure that the server does not fail the [HTTP status test](/node/588186), if it is failing follow the instructions to, for example: add a DNS entry for the site that is the same as where you are accessing it, change firewall or SE Linux settings.

### Tests failing as soon as they start

If you encounter an issue where the batch fails as soon as you start to run tests double check that you are in english, with no multilingual settings enabled. If you have for example 'fr' in your url, switch back to english or remove the language prefix and your issue should be fixed.

### xdebug

The [Simpletest reference Tips page](http://drupal.org/node/30011) has a section at the bottom on getting xdebug working with Simpletest.

### Calls to \$this-\>drupalLogin() failing

If your tests are failing when logging in users, you may need to set your `$base_url` in settings.php. (In Drupal 8, this is `SIMPLETEST_BASE_URL` in phpunit.xml)

Errors will look like this:

- *Failed to set field name to random_string*
- `Test MyGreatTest->testSomething() failed: GET http://default/user returned 0 (0 bytes).`

Alternatively, if you are running your tests from [drush](http://drupal.org/project/drush "drush"), you can pass the `--uri` parameter:

``` php
drush test-run AttachBlockTestCase --uri=local.mysite.org
```

If you're using modules such as html5_tools there is an issue where the simpletest does not regard the \<button\> as a valid login button, so simpletest will report that it could not find the form (usually 'Failed to set field name') Use [this patch](https://www.drupal.org/node/1481148#comment-7045568) [\#1481148: Simpletest does not consider form items of type 'button' for submitting forms](/project/simpletest/issues/1481148 "Status: Needs work")

If you find that \$this-\>drupalGet() is returning zero bytes even though a request generally works to that same URL, try disabling 'keepalive' in your HTTP server (nginx is *"keepalive_timeout 0;"*)

### Tests hanging

If you are experiencing hanging tests (they just never finish), try running your tests from the command line: go to the Drupal root and call

``` php
php scripts/run-tests.sh "test-group"
```

This might reveal a PHP error like an attempt to access a member of a non-object, within your code. It might also reveal an integrity constraint PDOException, for example if you are running a test on a Feature which exports non-existent user permissions.

### The test did not complete due to a fatal error. (Completion check)

If you get this when running a test, you've not got a lot of info to work with. Under the hood, it may imply that something went wrong at the setup stage.  
To find out more, it may be possible to investigate the logs *of the dummy site that fell over*.

- Open up your SQL tool, and connect to *the database of the site running the tests*
- You may see a number of prefixed tables there, eg ` simpletest228205actions`
- Investigate the `watchdog` table there, eg `simpletest228205watchdog`
- There is a good chance the last line in that table contains info about what failed. You may have to read between the lines as the strings are tokenized, but that's the logs you can investigate.

*In my case I found clues that told me that my setup field creation was conflicting with a field name already provided by the install profile:*

``` php
'25', '1', 'php', '%type: !message in %function (line %line of %file).', 'a:6:{s:5:"%type"; s:14:"FieldException"; s:8:"!message"; s:127:"Attempt to create field name &lt;em class=&quot;placeholder&quot;&gt;field_image&lt;/em&gt; which already exists and is active."; s:9:"%function";s:20:"field_create_field()";s:5:"%file"; s:53:".../modules/field/field.crud.inc"; s:5:"%line"; i:85; s:14:"severity_level"; i:3;}'
```
