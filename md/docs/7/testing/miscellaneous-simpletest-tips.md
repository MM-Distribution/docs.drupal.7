---
title: "Miscellaneous SimpleTest tips"
source_url: "https://www.drupal.org/docs/7/testing/miscellaneous-simpletest-tips"
page_type: page
last_updated: "Last updated on 6 February 2017"
published: "2005-08-30T12:37:38+00:00"
modified: "2017-02-06T09:29:02+00:00"
breadcrumb: ["Drupal 7", "Automated testing for Drupal 7"]
fetched: "2026-10-21T08:13:26Z"
raw: "raw/docs/7/testing/miscellaneous-simpletest-tips.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Miscellaneous SimpleTest tips

This is a list of some general tips for writing tests, feel free to pitch in and add your own!

## Posting to a multiple select field

To select multiple options of a select field (e.g. testing taxonomy terms), in which case:

``` php
<div class="form-item">
  <label for="edit-parent">Parent term:</label>
  <select name="parent[]" multiple="multiple" size="3" id="edit-parent">
    <option value="806" selected="selected">one</option>
    <option value="807">two</option>
    <option value="808">three</option>
  </select>
</div>
```

we need to post an array for \#name:

``` php
  $edit = array(
    'parent[]' => array('807', '808'),
  );
  $this->drupalPost('taxonomy/term/123/edit', $edit, t('Save'));
```

## Testing the Uploading Functionality

In the new version of Simpletest, there is an uploading feature. The example below best illustrates this. You MUST first create the full path to the file and then pass it into the \$edit parameter of the [drupalPost() method.](https://api.drupal.org/api/drupal/modules%21simpletest%21drupal_web_test_case.php/function/DrupalWebTestCase%3A%3AdrupalPost/7) In the example (and in your tests), the path is relative to the root Drupal installation directory. The realpath() function resolves all symbolic links and references within a path string (more documentation [here](http://us3.php.net/manual/en/function.realpath.php)).

``` php
$rpath = realpath('sites/all/modules/my_module/test-file.pdf');
$this->drupalPost('form/upload', array('name-of-file-field-here' => $rpath), t('Upload file'));
```

The first parameter is the path where the form is found. You don't need to do a \$this-\>drupalGet to "visit" the page in the virtual browser in order to test form submissions. You can just do \$this-\>drupalPost('path/to/my/form's/page', \$edit, t('Submit')). You can also pass in NULL as this first parameter if you are already on the page where the form exists.

Notice that the \$edit parameter is a key-value array. Specifically for file upload testing, you'll want to replace the key "name-of-file-field-here" with the name of the file field as it appears in the final HTML output of a form. So if you've produced a form with a file field named "file_drop_point" as in this example...

``` php
$form['file_drop_point'] = array(
'#type' => 'file',
'#title' => t('Upload a file'),
);
```

... your subsequent test that tests this file field's uploading capability will actually look something like this:

``` php
$rpath = realpath('sites/all/modules/my_module/test-file.pdf');
$this->drupalPost('form/upload', array('files[file_drop_point]' => $rpath), t('Upload file'));
// There are no quotes around "file_drop_point" in the key, by the way.  It's valid the way it looks.
```

Why? Go to the page where the form is, then look at the HTML code for the file upload field. It will resemble this:

``` php
<input ... name="files[file_drop_point]" ... />
```

Your tests should now run properly, though be sure to check mark "Provide verbose information when running tests" in the test settings (Administer \> Site Building \> Testing \> Settings tab). Verbose output will provide snapshots of the pages that the Drupal browser was seeing as the test ran.

The 3rd parameter of drupalPost is the text of the submit button for the form.

## Viewing Source during a Browser Test

Use `$this->drupalGetContent()` (or Drupal 8: `$this->getRawContent()`) to output the source that the simpletest browser is receiving. This is useful for debugging during development.

## Triggering your debugger (xdebug client) from a Browser Test

Debugging errors in tests using xdebug is different from debugging other processes, because tests go through cURL rather than through your browser. The second PHP process started by the cURL request should be passed the correct session variables, get parameters, or cookies so that it will connect to the xdebug client. Also, your xdebug should accept multiple connections (at least 4).

### Drupal 8 + cookies

If a cookie is used to trigger xdebug connections, this cookie will propagate to the cURL session so no extra setup on the web server/PHP side should be necessary.

You can use <http://pollinimini.net/blog/xdebug-bookmarklet/> to set up your browser so that cookies will trigger xdebug. You can also try the "easy Xdebug" or "xdebug helper" plugins for Firefox and Chrome, which will set a cookie to make it so these requests automatically get sent to xdebug.

### Drupal 7, or sessions without cookies

As of [\#889338: Add support for xdebug in WebTestBase](/project/drupal/issues/889338 "Status: Closed (fixed)"), the same process as D8 should work in D7. If you are running an older version of D7, then read on.

Cookies will trigger xdebug from simpletest (see above how to set this up in your browser) but the drupalGet() and drupalPost() calls in your tests which go through cURL, don't have the get parameters, (for D7) cookies or session variables set correctly.

There are a few ways to fix this.

1.  Port issue [\#889338](https://drupal.org/node/889338) to Drupal 7.

2.  Edit the `drupalGet()` and `drupalPost()` methods in DrupalWebTestCase so that they have an  

    ``` php
    array('query' => 'XDEBUG_SESSION_START=mw')  // D6
    array('query' => array('XDEBUG_SESSION_START' => 'mw')) // D7
    ```

    added to their \$options parameter.  
    Substitute your own IDE key for *mw*. If you already know how to trigger debugging in your browser from your IDE, you can find the IDE key by looking at the URL that your IDE generates for debugging. Here's a code snippet for Drupal 7:

    ``` php
    if (!isset($options['query'])) {
      $options['query'] = array();
    }
    $options['query'] += array('XDEBUG_SESSION_START' => 'ECLIPSE_DPGP');
    ```

    This is if you are using the Eclipse IDE; again, substitute the correct IDE key if you are using something else.

3.  Another alternative is to setup a VirtualHost on your Apache with the following xdebug related lines. This causes all pages on this domain to trigger the debugger. Just use this domain when you want to debug and use a different domain when you are browsing or developing bug free :).

    More xdebug remote debugging params should be set in your php.ini or in this VirtualHost.

    ``` php
      #customize this path to point to your Xdebug extension 
      zend_extension=/Applications/Komodo IDE.app/Contents/SharedSupport/php/debugging/5.2/xdebug.so
       #customize this to match how you setup your xdebug client
      xdebug.idekey=mw
      xdebug.default_enable=1
      xdebug.remote_handler=dbgp
      php_admin_value xdebug.remote_enable 1
      #the following line triggers the xdebug client automatically for every request. useful for simpletest.
      php_admin_value xdebug.remote_autostart 1
    ```

Other notes:

- Make sure your IDE options are set up correctly so they will prompt you to accept remote debugging requests. Otherwise, even with the steps above, your request won't open up for debugging in your IDE.
- When using PHPStorm,
  - In your 'PHP \> Debug' preferences, set the "Max. simultaneous connections" to at least 4.
  - Do *not* use the [‘PHP Web Application’ Run Configuration](http://blog.jetbrains.com/webide/2011/03/configure-php-debugging-in-phpstorm-2-0/) to start a debug session from your IDE; instead use the ‘Listen PHP Debug Connections’ Mode/button. (The ‘PHP Web Application’ Run Configuration is fine for non-simpletest debugging. But the active xdebug connection from the browser's PHP process will block the cURL PHP-xdebug processes from connecting to PHPStorm. cURL requests will hang indefinitely -or until they time out- and only connect to PHPStorm *after* your browser request terminates.)

## Simulate external API calls

Some modules may interact with external APIs and it is desirable to avoid using them when running tests.

A mock module that defines a few items in its **hook_menu()** implementation can impersonate an external API just by being enabled on the test set up stage.

For example, the Twitter module has a sub-module within its tests directory called twitter_mock. This module changes the host that the module calls from api.twitter.com to the local website domain, so a request such as **<http://api.twitter.com/user_timeline.json?user_id=100>** will actually be made to **<http://yourlocalsite/user_timeline.json?user_id=100>**.

Have a look at the [twitter_mock.module](http://drupalcode.org/project/twitter.git/blob/refs/heads/7.x-3.x:/tests/twitter_mock.module "twitter_mock") implementation for more details.
