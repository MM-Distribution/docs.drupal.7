---
title: "How to add a \"?destination=URL\" to the request new password link"
source_url: "https://www.drupal.org/docs/7/theming/overriding-themable-output/how-to-add-a-destinationurl-to-the-request-new-password"
page_type: page
last_updated: "Last updated on 15 May 2020"
published: "2014-09-10T10:37:52+00:00"
modified: "2020-05-15T10:20:40+00:00"
breadcrumb: ["Drupal 7", "Theming Drupal 7", "Overriding themable output"]
fetched: "2026-10-21T08:19:22Z"
raw: "raw/docs/7/theming/overriding-themable-output/how-to-add-a-destinationurl-to-the-request-new-password.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# How to add a "?destination=URL" to the request new password link

Problem 1:  
Drupal encodes the "?" and the "=" when entering the parameters de/encoded directly to the url and you´ll get "user/password%253Fdestination%253Dhomepage" in the browser URL when clicking the link.  
  
  
BAD EXAMPLE:

``` php
$newlinks = l(t('Forgot your password?'), 'user/password?destination=homepage', array('attributes' => array('title' => t('Request new password via e-mail.'))));
$form['links']['#markup'] = $newlinks;
```

------------------------------------------------------------------------

GOOD EXAMPLE:

``` php
$newlinks = l(t('Request new password'), 'user/password', array('query' => array('destination' => 'homepage', 'foo' => 'bar'), 'attributes' => array('title' => t('Request new password via e-mail.'))));
```

------------------------------------------------------------------------

Problem 2:  
The links also appears within a message when the user has entered a wrong password with an already attached parameter username (a href="/user/password?name=username").

How/Where do I change this?

Answer: via translations and adding "&destination=homepage" to the URL.

------------------------------------------------------------------------

The complete function:

``` php
// modify user login block
function YOURTHEMENAME_form_user_login_block_alter(&$form) {
  $newlinks = l(t('Request new password'), 'user/password', array('query' => array('destination' => 'homepage'), 'attributes' => array('title' => t('Request new password via e-mail.'))));
  $newlinks = '<div class="wrapperForgotPassword">' . $newlinks . '</div>';
  $form['links']['#markup'] = $newlinks;
  $form['links']['#weight'] = 10000; // put the links after the other items
  $form['pass']['#attributes']['placeholder'] = t('password'); // add placeholders
  $form['name']['#attributes']['placeholder'] = t('username');
  return $form;
}
```

Additional note:

When you want to set the current page as a destination target to redirect the user back to the current page, you can use `drupal_get_destination()`. A good example for Drupal 7 can be found in the core nodes list page callback `node_admin_nodes()`.

node_admin_nodes():

``` php
function node_admin_nodes() {
  ...

  $destination = drupal_get_destination();

  ...

    $operations = array();
    if (node_access('update', $node)) {
      $operations['edit'] = array(
        'title' => t('edit'),
        'href' => 'node/' . $node->nid . '/edit',
        'query' => $destination,
      );
    }

  ...

    if (count($operations) > 1) {
      // Render an unordered list of operations links.
      $options[$node->nid]['operations'] = array(
        'data' => array(
          '#theme' => 'links__node_operations',
          '#links' => $operations,
          '#attributes' => array('class' => array('links', 'inline')),
        ),
      );
    }
    elseif (!empty($operations)) {
      // Render the first and only operation as a link.
      $link = reset($operations);
      $options[$node->nid]['operations'] = array(
        'data' => array(
          '#type' => 'link',
          '#title' => $link['title'],
          '#href' => $link['href'],
          '#options' => array('query' => $link['query']),
        ),
      );
    }

  ...
}
```
