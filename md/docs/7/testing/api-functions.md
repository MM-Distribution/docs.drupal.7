---
title: "API functions"
source_url: "https://www.drupal.org/docs/7/testing/api-functions"
page_type: page
last_updated: "Last updated on 13 March 2017"
published: "2008-06-02T19:43:02+00:00"
modified: "2017-03-13T14:02:56+00:00"
breadcrumb: ["Drupal 7", "Automated testing for Drupal 7"]
fetched: "2026-10-21T08:11:53Z"
raw: "raw/docs/7/testing/api-functions.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# API functions

**The internal browser**

The DrupalWebTestCase features an internal browser that can be used to navigate on your test site.

**`function $this->drupalGet($path, $options = array())`**  
This function does a get request to a Drupal page.  
The `$path` indicates a page that can be visited; `$options` contain additional data which may be passed to the url() function in order to determine the url to visit. The content will be loaded and saved into \$this-\>\_content (as well as returned), where it can be retrieved by using the function \$this-\>drupalGetContent().

See the API documentation for the url() function (<http://api.drupal.org/api/function/url/7>) for more information on how to properly construct the `$options` associative array

**`function $this->drupalPost($path, $edit, $submit, array $options = array(), array $headers = array())`**  
This function does a post request on a Drupal page.

- The `$path` indicates a page containing a form that will be filled with `$edit` data.
- The `$options` will be passed to `url()` to build the URL from `$path`
- Then the button indicated by `$submit` will be clicked (submit caption will be translated by this method).
- Optional HTTP `$headers` can be added to the POST operation
- `$edit` data should be an array where each index is the value of the "name" attribute of the HTML form element. Use something like Firebug to inspect the HTML to get this value.

It also performs assertions that the requests were successful and form fields could be set.

**Example:**

``` php
$name = $this->randomName();
$mail = "$name@example.com";
$edit = array(
  'name' => $name,
  'mail' => $mail,
  'status' => FALSE, // checkboxes must be set with TRUE/FALSE rather than 1/0
);
$this->drupalPost('user/register', $edit, 'Create new account');
```

Note: this function used to be called drupalPostRequest()

With multi-step forms, it is possible to post each subsequent step by passing NULL as the \$path.

**`function $this->clickLink($label, $index = 0)`**  
Follows a link on the current page by name. Will click the first link found with this link text by default, or a later one if an `$index` is given.  
An assertion is done about the availability of the link and the URL it points to. Also gives some output including current and requested URL.

**Example:**

``` php
$this->clickLink(t('Log out')); 
```

**`function $this->drupalCreateUser($permissions = NULL)`**  
This function creates a user and returns the user object with an additional value `pass_raw` containing the non-hashed password.  
It also creates a role with the specified `$permissions` that is assigned to the returned user.  
The `$permissions` are specified as an array of strings. If it is omitted or NULL, the default permissions for a registered user will be used:  
`array('access comments', 'access content', 'post comments', 'post comments without approval')`  
An assertion for success is done as well as clean-up on the user and role tables.

**`function $this->drupalLogin($user = NULL)`**  
This function logs a user into your site via the internal browser. You can just hand it a `$user` object (required is a `pass_raw` value).  
If the argument is omitted this function will create a user and role with the standard permissions mentioned above.

After the user is logged in, you can now navigate with the internal browser.

**Example:**

``` php
// Prepare a user to do the stuff
$user = $this->drupalCreateUser(array('access content', 'create page content'));
$this->drupalLogin($user);

// Now do something with the users
$this->drupalGet('node/' . $node->nid));
```

This method also does several assertions about the login process from the browsers perspective.

**`function $this->drupalLogout()`**  
This function logs out the current user in the internal browser. This function is automatically called by `$this->drupalLogin($user = NULL)`, so you do not need to call this function if you want to login as another user, only if you want to logout from a current user session and switch the internal browser to an anonymous user session.

**Example:**

``` php
// Prepare a Drupal user to retrieve a page
$user = $this->drupalCreateUser(array('access content', 'create page content'));
$this->drupalLogin($user);
$test_page = 'node/' . $node->nid;

// Retrieve page as the logged in user
$this->drupalGet($test_page);
$this->assertText(t('Welcome'), t('Check that a welcome message is set'));

// Logout and retrieve the page as an anonymous user
$this->drupalLogout();
$this->drupalGet($test_page);
$this->assertText(t('Please login'), t('Check that user is prompted to login'));
```

Note: In this example the logout is only necessary because the internal browser was previously logged in with a Drupal user session. If you are not logged-in you obviously will already be browsing as an anonymous user and will not have to logout first.

**`function $this->drupalCreateRole($permissions = NULL)`**  
This function is rarely useful. The `$permissions` parameter behaves exactly like in `drupalCreateUser`.  
The return value is a role-id integer or FALSE on failure.  
A success assertion is done, as well as decent clean-up of the role and permission tables.

<!-- -->

**`function $this->randomString($number = 8)`**  
Returns a string with \$number ASCII characters of codes 32 to 126 prefixed by a prefix unique to the test run. The first character will not be a number.

**`function $this->randomName($number = 8)`**  
Returns a string with \$number alphanumerical character(s) prefixed by a prefix unique to the test run. The first character will not be a number.

**`function $this->drupalCreateContentType($settings)`**  
Creates a custom content type based on default settings. The default values for nodes are set for you. You can selectively override these (or append new data to these) using the `$settings` associative array that is passed into this function.

**Example:**

``` php
$settings = array(
  'type' => 'my_special_node_type', // Override default type (a random name)
  'title_label' => 'Name', // Override default title label ("Title")
  'body_label' => 'Description', // Override default body label ("Body")
);
$content_type = $this->drupalCreateContentType($settings);

$this->assertEqual($content_type->type, 'my_special_node_type'); // We set this.
```

**`function $this->drupalCreateNode($settings)`**  
Create a new node. The default values for nodes are set for you. You can selectively override these (or append new data to these) using the `$settings` associative array that is passed into this function.

**Example:**

``` php
$settings = array(
  'type' => 'my_special_node_type', // This replaces the default type
  'my_special_field' => 'glark', // This appends a new field.
);
$node = $this->drupalCreateNode($settings);

$this->assertEqual($node->type, 'my_special_node_type'); // We set this.
$this->assertEqual($node->comment, 2); // This is default.
```

Default settings are as follows:

``` php
    // Populate defaults array
    $defaults = array(
      'body'      => $this->randomName(32),
      'title'     => $this->randomName(8),
      'comment'   => 2,
      'changed'   => time(),
      'format'    => FILTER_FORMAT_DEFAULT,
      'moderate'  => 0,
      'promote'   => 0,
      'revision'  => 1,
      'log'       => '',
      'status'    => 1,
      'sticky'    => 0,
      'type'      => 'page',
      'revisions' => NULL,
      'taxonomy'  => NULL,
    );
    $defaults['teaser'] = $defaults['body'];
    // If we already have a node, we use the original node's created time, and this
    if (isset($defaults['created'])) {
      $defaults['date'] = format_date($defaults['created'], 'custom', 'Y-m-d H:i:s O');
    }
    if (empty($settings['uid'])) {
      global $user;
      $defaults['uid'] = $user->uid;
    }
```

**`function $this->cronRun()`**  
This function runs the cron functionality of the Drupal installed by SimpleTest. Never call `drupal_run_cron` directly. Not available in SimpleTest 6.x!

**`function $this->addLanguage($language_code)`**  
Installs the specified language, or enables it if it is already installed. Example:

``` php
  // Install and enable the Italian language.
  $this->addLanguage('it');
```

Note: This function is not generally available in all tests; for example, in Drupal 7, it is only available to test cases that extend the TranslationTestCase class.

For a complete list of available methods and attributes check the [DrupalWebTestCase](https://api.drupal.org/api/drupal/modules%21simpletest%21drupal_web_test_case.php/class/DrupalWebTestCase/7.x) class definition in the Drupal 7 API.
