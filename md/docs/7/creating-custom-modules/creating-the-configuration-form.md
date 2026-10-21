---
title: "Creating the configuration form"
source_url: "https://www.drupal.org/docs/7/creating-custom-modules/creating-the-configuration-form"
page_type: page
last_updated: "Last updated on 1 March 2018"
published: "2011-03-30T21:43:39+00:00"
modified: "2018-03-01T16:58:05+00:00"
breadcrumb: ["Drupal 7", "Creating custom modules in Drupal 7"]
fetched: "2026-10-21T07:23:44Z"
raw: "raw/docs/7/creating-custom-modules/creating-the-configuration-form.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Creating the configuration form

**Main topic described: *Form API***  
**Main functions described: *variable_get(), system_settings_form()***

Next, we will build the `current_posts_form()` function. We build the form by adding elements to the `$form` array. In a pattern similar to the menu `$items` variable, the name of each element is its key in the array, with that key's value being a specially formatted associative array. In this value array, we list the attributes of the element, this time preceding each key with a hash mark (#).

Add the following to your `current_posts.module` file:

``` php
/**
 * Page callback: Current posts settings
 *
 * @see current_posts_menu()
 */
function current_posts_form($form, &$form_state) {
  $form['current_posts_max'] = array(
    '#type' => 'textfield',
    '#title' => t('Maximum number of posts'),
    '#default_value' => variable_get('current_posts_max', 3),
    '#size' => 2,
    '#maxlength' => 2,
    '#description' => t('The maximum number of links to display in the block.'),
    '#required' => TRUE,
  );

  return system_settings_form($form);
}
```

### The element attributes

Here we create a text field, with a title of 'Maximum number of posts', and a description, which will appear below the field. Note that both of these strings are passed through the `t()` function for translation. Size is 2, maximum length is 2. The Form API will automatically validate the `maxlength` attribute when the form is submitted and throw an error if the length exceeds 2. We have also designated the field as required. The form API will mark it with an asterisk and will throw an error if the form is submitted with no value in the field. See the [forms_api_reference](http://api.drupal.org/api/drupal/developer--topics--forms_api_reference.html/7#elements) for the complete list of available elements and properties.

### Persistent variables

Certain data, like system settings and user-configurable information, needs to be saved and retrievable for a website to function properly. Drupal accomplishes this through the use of persistent variables. These variables are stored in a database table with keys provided by the implementing module.

The function `variable_get()` retrieves a persistent variable, and `variable_set()`, as you might expect, sets one. We use `variable_get()` above to retrieve the value of our field if it has been set. If not, we specify a default value of 3. `variable_get()` uses the name of the element, `current_posts_max`, to find the relevant data.

### System settings

Drupal makes it easy for us to save the form's data with the function `system_settings_form()`. By using the function in our code, we tell Drupal to provide a submit button and to save data into persistent variables using `variable_set()`. It will also provide a green confirmation message when data is successfully saved, and a red error message if something went wrong. If you prefer, you can create a submit function yourself, (see [Form API Quickstart Guide](http://drupal.org/node/751826)) but for now, we will use this handy shortcut.

### Editing the query

We must add two lines of code to our query function, `current_posts_contents`, one using `variable_get()` to retrieve the data from our settings form, and the other adding the range function to include this limit in the query. Here's the revised function, with the new lines noted in comments:

``` php
function current_posts_contents() {
  //Get today's date.
  $today = getdate();
  //Calculate midnight a week ago.
  $start_time = mktime(0, 0, 0,$today['mon'],($today['mday'] - 7), $today['year']);
  //Get all posts from one week ago to the present.
  $end_time = time();

 //NEW LINE 
 $max_num = variable_get('current_posts_max', 3);

  //Use Database API to retrieve current posts.
  $query = db_select('node', 'n')
    ->fields('n', array('nid', 'title', 'created'))
    ->condition('status', 1) //Published.
    ->condition('created', array($start_time, $end_time), 'BETWEEN')
    ->orderBy('created', 'DESC') //Most recent first.
    ->range(0, $max_num) //NEW LINE
    ->execute();
  return $query;
}
```

Using `variable_get()`, we save the configuration setting into the `$max_num` variable or assign a default of 3. Then we add the range method to our select query. That method's first argument is set to zero to specify starting at the beginning of the set. The second argument, `$max_num`, determines how many records to return.

### Check

Go ahead and again enable your module. Then you will need to clear the menu cache, so that Drupal will recognize the new URL. (Drupal caches a lot of data, including a list of all the URLs it recognizes.) To clear the cache, go to *Configuration \> Performance* or `http://example.com/admin/config/development/performance`, and click the *Clear all caches* button.

Now you can test the settings form. Navigate to it: *Configuration \> Content authoring \> Current posts* or `http://example.com/admin/config/content/current_posts`. Adjust the number of links and save the configuration. The maximum number of links in the block should adjust accordingly. See how `system_settings_form()` has added a submit button and gives you a confirmation message when you have successfully saved.

Please note: be sure to disable your module before continuing.

### See also

- [Form generation](http://api.drupal.org/api/drupal/includes--form.inc/group/form_api/7)
- [forms_api_reference](http://api.drupal.org/api/drupal/developer--topics--forms_api_reference.html/7#elements)
- [Form API Quickstart Guide](https://www.drupal.org/docs/7/api/form-api/creating-a-builder-function-to-generate-a-form)
- [system_settings_form()](http://api.drupal.org/api/drupal/modules--system--system.module/function/system_settings_form/7)
