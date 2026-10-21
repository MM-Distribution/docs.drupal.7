---
title: "Create a custom User Registration form with FAPI D7"
source_url: "https://www.drupal.org/docs/7/howtos/create-a-custom-user-registration-form-with-fapi-d7"
page_type: page
last_updated: "Last updated on 28 June 2019"
published: "2011-02-16T17:11:58+00:00"
modified: "2019-06-28T09:38:13+00:00"
breadcrumb: ["Drupal 7", "Site building and development HowTos for Drupal 7"]
fetched: "2026-10-21T08:02:35Z"
raw: "raw/docs/7/howtos/create-a-custom-user-registration-form-with-fapi-d7.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Create a custom User Registration form with FAPI D7

There are many reasons to create a custom User Registration form in Drupal, so I won't get into the "Why?" of it. This isn't a tutorial about necessarily how to use FAPI, but rather a particular way to accomplish something with FAPI. I assume when writing this that you understand the FAPI and the basics of putting your own module together.

Essentially we start with FAPI and and a [Form Generation callback](https://api.drupal.org/api/drupal/includes!form.inc/group/form_api/7.x) to build the form itself in our module:

### Form generation callback

``` php
function foo_user_register_form($form, &$form_state){
    $form['name'] = array(
        '#title' => 'username',
        '#description' => 'choose a username',
        '#type' => 'textfield',
        '#required' => TRUE,
    );
    $form['mail'] = array(
        '#title' => 'email',
        '#description' => 'enter a valid email address',
        '#type' => 'textfield',
        '#required' => TRUE,
    );
        $form['submit'] = array(
        '#type' => 'submit',
        '#value' => t('Save'),
    );
    return $form;
}
```

The username and email are all that are specifically required to create the account, other fields created with Field UI can be added in at will. You could even call them something different if you wanted, here in the form builder callback.

The real magic of saving the user happens in the submit handler of your module, which utilizes user_save().

### Submit Handler

``` php
function foo_user_register_form_submit($form, &$form_state){
    $edit = array(
          'name' => $form_state['values']['name'], 
          'pass' => user_password(),
          'mail' => $form_state['values']['mail'],
          'init' => $form_state['values']['mail'], 
          'status' => 1, 
          'access' => REQUEST_TIME,
    );
    user_save(drupal_anonymous_user(), $edit);
}
```

The user_password() function generates a random string to be stored as the user's password.

### Adding additional fields to the submit handler

Let's say that we added some custom fields "First Name" (field_fname) and "Last Name" (field_lname) to our users via the UI in d7. We can represent that in our form any way we want to because the key of the \$edit array (in our submit handler) is what matters.

``` php
function foo_user_register_form($form, &$form_state){
    $form['name'] = array(
        '#title' => 'username',
        '#description' => 'choose a username',
        '#type' => 'textfield',
        '#required' => TRUE,
    );
    $form['mail'] = array(
        '#title' => 'email',
        '#description' => 'enter a valid email address',
        '#type' => 'textfield',
        '#required' => TRUE,
    );
        $form['field_fname'] = array(
        '#title' => 'First Name',
        '#type' => 'textfield',
    );
        $form['field_lname'] = array(
        '#title' => 'Last Name',
        '#type' => 'textfield',
    );
        $form['submit'] = array(
        '#type' => 'submit',
        '#value' => t('Save'),
    );
```

In Drupal 6 we had a 'data' key in the new user array, in Drupal 7 it's been deprecated. To add these fields programmatically when saving a user we add them to our submit handler like so:

``` php
function foo_user_register_form_submit($form, &$form_state){
    $edit = array(
          'name' => $form_state['values']['name'], 
          'pass' => user_password(),
          'mail' => $form_state['values']['mail'],
          'init' => $form_state['values']['mail'], 
          'status' => 1, 
          'access' => REQUEST_TIME,
              'field_fname' => array(LANGUAGE_NONE => array(array('value' => $form_state['values']['field_fname']))),
          'field_lname' => array(LANGUAGE_NONE => array(array('value' => $form_state['values']['field_lname']))),
    );
    user_save(drupal_anonymous_user(), $edit);
}
```

If you happen to be fond of adding fieldsets to your forms with FAPI (probably to make use of \#states or something) and you slap your extra fields in one, you do not need to have to actually mention that fieldset in the submit handler.

``` php
$form_state['values']['fieldset_name']['field_fname']
```

vs.

``` php
$form_state['values']['field_fname']
```

If you add the fieldset in betwixt the \['values'\] and \['field_name'\] in the submit handler, you'll get a NULL value in the database for that field.

### Saving roles

In my form, I decided I would let users choose their own roles. I created a field of \#type "select" and used the role names I created as options. In the submit handler I added \$roles as an empty variable and set it within if() statements based on the \$form_state\['value'\] of my field.

``` php
  $roles = '';
    if($form_state['values']['user_kind'] == 'A User Role'){
        $roles = array('1' => 'A User Role');
    }
    elseif($form_state['values']['user_kind'] == 'A Different Role'){
        $roles = array('2' => 'A Different Role');
    }
```

Keep in mind that the key must match the value in the database. After this simply add the following to the \$edit array:

``` php
        'roles' => $roles,
```

### Set up notification email.

In Drupal 6 there was drupal_mail_send() which was great. Drupal 7 took that away and left us with what is, in my opinion, a too complicated function called drupal_mail(). I opted to use PHP's mail() instead.

In the form builder I added a checkbox:

``` php
  $form['send_message'] = array(
        '#type' => 'checkbox',
        '#title' => t('Notify user of new account via email.'),
        '#description' => 'If left unchecked, a message will not be sent.',
        '#default_value' => 1,
    );
```

At the end of the submit function I tacked on the setup for a notification:

``` php
  $to = $form_state['values']['mail'];
    $subject = 'New account created';
    $headers = "From: something@somewhere.org\nContent-type: text/html";
    $body = 'A new user account has been created for you at <a href="http://something.org/">Something.org</a>.<br /> Your login details are as follows:<br />Username: <b>'.$form_state['values']['name'].'</b><br /> Password: <b>'.$form_state['values']['password'].'</b> <br /><br /> Please login to <a href="http://something.org/">Something.org</a> and change your password.<br />';
    
    if($form_state['values']['send_message'] == 1){
        mail($to,$subject,$body,$headers);
    } 
```

It's really important that your headers use new lines "\n" between each other, and I also discovered that it didn't really work unless \$headers value was in double quotes.
