---
title: "Customize Drupal User Profiles with CiviCRM Contact Fields"
source_url: "https://www.drupal.org/docs/7/theming/howto/customize-drupal-user-profiles-with-civicrm-contact-fields"
page_type: page
last_updated: "Last updated on 8 September 2016"
published: "2014-04-07T00:57:37+00:00"
modified: "2016-09-08T14:07:08+00:00"
breadcrumb: ["Drupal 7", "Theming Drupal 7", "Theming HowTos"]
fetched: "2026-10-21T08:49:25Z"
raw: "raw/docs/7/theming/howto/customize-drupal-user-profiles-with-civicrm-contact-fields.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Customize Drupal User Profiles with CiviCRM Contact Fields

Drupal's user profile page or user's account page in its OEM form seems somewhat bland when compared with the rest of Drupal and it also seems a bit limited when compared to the theming capabilities that are available for the majority of a Drupal sites pages and content. This article discusses techniques that can be used to improve the customization options for developers/themers to personalize user profile pages without writing reams of spaghetti code; in particular when Drupal is used with CiviCRM.

This page is in no way the complete and definitive method for customizing the user profile so please correct, update and add to it as required : )

## Custom user-profile.tpl.php

If you want to make a lot of changes to the Drupal user profile page, you'll want to customize the user template page by copying the existing one at /modules/user/user-profile.tpl.php to your theme to customize it to your liking. I like to use the \$user_profile or the global \$user object in keeping with OOP techniques and render the fields that I need to use where I want to use them. As you add custom profile fields to your site, they will become available in the \$user_profile array and rather than just rendering the complete array, you can choose what fields to place where. More information about the user profile template with a discussion about customizing it can be found here: <https://api.drupal.org/api/drupal/modules!user!user-profile.tpl.php/7>

## Using CiviCRM Custom Data Profiles

If your Drupal website is integrated with CiviCRM, you have an opportunity to bring much more personalized content into the Drupal user profile page through CiviCRM's Contact Record Fields. The most straight forward way to bring CiviCRM contact record data to the Drupal user profile page is by configuring the appropriate CiviCRM Custom Data Profiles to be visible in the Drupal user profile page. This can be done by being logged in with permissions to administer CiviCRM, navigating to CiviCRM -\> Administer -\> Custom Data and Screens -\> Profiles. Edit the Profile you would like to expose in the user profile page and adjust the setting for it to be used for: View/Edit Drupal User Account. You can also use these settings to remove CiviCRM content from the Drupal user profile page by un-setting it to be used for the Drupal User Account.

## Custom Code

In order to take your Drupal user profile page to the next level, you'll want to get into a little custom coding. There are many ways to go about customizing a user profile with custom code. This article will present a method where the developer/themer will create a custom module to access the CiviCRM Contact Record fields and then expose them to the user-profile.tpl.php through the global variable. This will enable the developer/themer to add CiviCRM data to the user profile page in a clear and succinct manner, keeping the user profile template clean and easy to understand.

### Acquiring CiviCRM Contact Record Fields

The first thing we need to do is create a module that will connect to CiviCRM and expose the data we're looking for. The following is a brief description of just such a module built according to the current CiviCRM V3 API. We'll call the module civicrm_custom_user_profile and all of the files will be in a directory called: civicrm_custom_user_profile

**civicrm_custom_user_profile.info**  
Every module needs an info file so create a file called civicrm_custom_user_profile.info as follows and place it into the civicrm_custom_user_profile directory. Our module will require CiviCRM to be active so we add dependencies\[\] = civicrm. This means that the module will not be able to be installed without CiviCRM being present.

``` php
name = CiviCRM Custom User Profile
description = Exposes CiviCRM Contact Record Fields to the Drupal User Profile Page.
core = 7.x
package = Custom
dependencies[] = civicrm
```

**civicrm_custom_user_profile.module**  
Our module is quite simple and all it needs to do is figure out who's profile page we're looking at, ask CiviCRM for the Contact Record fields and then expose those fields so that we can use them.

The first thing I want to do is change the title of the user profile page. By default, Drupal will provide a title for the profile page that consists of just the user name by itself. I would rather it said something a little more intuitive like my organizations name and something about it being a profile page so that new users get a feel for what the page is for. We'll do that with the following file that will be saved as civicrm_custom_user_profile.module

**Note:** I've borrowed the code for the civicrm_custom_user_profile_get_contact() function from a module called the CiviCRM Realname module which can be found here: <https://drupal.org/project/civicrm_realname>

``` php
<?php

/**
 * Retrieves a CiviCRM contact by Drupal user ID.
 */
function civicrm_custom_user_profile_get_contact($uid) {
  $contacts = &drupal_static(__FUNCTION__);
  if (isset($contacts[$uid])) {
    return $contacts[$uid];
  }
  if (!isset($contacts)) {
    $contacts = array();
  }
  $contacts[$uid] = FALSE;
  civicrm_initialize();
  require_once 'api/api.php';
  $res = civicrm_api('uf_match', 'get', array('uf_id' => $uid, 'version' => 3));
  if ($res['is_error'] || empty($res['id']) || empty($res['values'][$res['id']])) {
    return FALSE;
  }
  $id = $res['values'][$res['id']]['contact_id'];
  $res = civicrm_api('contact', 'get', array('contact_id' => $id, 'version' => 3));
  if ($res['is_error']) {
    return FALSE;
  }
  $contacts[$uid] = $res['values'][$res['id']];
  return $contacts[$uid];
}

/**
 * Implements hook_user_view().
 * We'll modify the title on the user profile 
 * and add a global $civi_user variable that we can 
 * expose in the profile page template
 */
function civicrm_custom_user_profile_user_view($account, $view_mode, $langcode) {
  
  global $civi_user;
  $user = user_load(arg(1));
  $uid = $user->uid;
  $civi_user = civicrm_custom_user_profile_get_contact($uid);

  if ($civi_user['display_name']) {
    drupal_set_title('My Organization Profile - ' . $civi_user['display_name']);
  } 
  
}
```

When added to a Drupal CiviCRM website, the module described above will change the Drupal user profile page title from the plain username to "My Organization User Profile - display_name". In the case of my user profile it would change from the plain: *awasson* to: *My Organization User Profile - Andrew Wasson*

### Exposing CiviCRM Fields in the Profile Page

In the custom module described above we also added a global variable called \$civi_user that can be invoked within the user-profile.tpl.php file to expose all of the available CiviCRM Contact Record fields.

In order to get an idea of what CiviCRM Contact Record fields are available in the user profile page, you can install the Devel module (<https://drupal.org/project/devel>) or you can recursively print \$civi_user to the page with the following couple of lines of code within the user-profile.tpl.php file:

``` php
<?php

 global $civi_user;
 print '<pre>';
 print_r($civi_user);
 print '</pre>';

?>
```

Using the module described above the developer/themer can ignore the way the existing template file renders Drupal and CiviCRM fields and instead use the global \$civi_user variable along with Drupal's \$user_profile variable to render or print the fields any way they choose.

Feel free to update and improve this page as necessary.
