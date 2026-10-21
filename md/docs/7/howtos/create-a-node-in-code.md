---
title: "Create a Node in Code"
source_url: "https://www.drupal.org/docs/7/howtos/create-a-node-in-code"
page_type: page
last_updated: "Last updated on 5 July 2022"
published: "2011-12-30T00:46:19+00:00"
modified: "2022-07-05T17:39:56+00:00"
breadcrumb: ["Drupal 7", "Site building and development HowTos for Drupal 7"]
fetched: "2026-10-21T08:02:04Z"
raw: "raw/docs/7/howtos/create-a-node-in-code.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Create a Node in Code

The code below presents a simple example of the means by which you can create a node in PHP code. This example makes no use of the Entity API module.

``` php
function a_page_submit($form, &$form_state) {
  global $user;

  $node = new stdClass();
  $node->title = "YOUR TITLE";
  $node->type = "YOUR_NODE_TYPE";
  // Sets some defaults. Invokes hook_prepare() and hook_node_prepare().
  node_object_prepare($node); 
  // Or e.g. 'en' if locale is enabled.
  $node->language = LANGUAGE_NONE; 
  $node->uid = $user->uid; 
  // Status is 1 or 0; published or not.
  $node->status = 1; 
  // Promote is 1 or 0; promoted to front page or not.
  $node->promote = 0; 
  // Comment is 0, 1, 2; 0 = disabled, 1 = read only, or 2 = read/write.
  $node->comment = 1; 

  // Text field
  $node->field_some_text[$node->language][0]['value'] = "YOUR TEXT";
  
  // Term reference (taxonomy) field
  $node->field_product_tid[$node->language][0]['tid'] = $form_state['values']['a taxonomy term id'];

  // Entity reference field.
  $node->field_customer_nid[$node->language][] = array(
    'target_id' => $form_state['values']['entity id'],
    // Default target_type is 'node', Other possible values are "user", 
    // "taxonomy_term" or other valid entity machine name.
    'target_type' => 'node',
  );
 

  $node = node_submit($node); // Prepare node for saving
  node_save($node);

  // drupal_set_message( "Node with nid " . $node->nid . " saved!\n");
  $form_state['redirect']  = 'SOME WHERE';
}
```

The same result can be achieved with the contrib [Entity API](https://www.drupal.org/project/entity) module but with fewer lines of code, better clarity, and less trouble from language/translation issues.

``` php
function my_create_a_node() {
global $user;

// entity_create replaces the procedural steps in the first example of
// creating a new object $node and setting its 'type' and uid property
$values = array(
  'type' => 'YOUR_NODE_TYPE',
  'uid' => $user->uid,
  'status' => 1,
  'comment' => 1,
  'promote' => 0,
);
$entity = entity_create('node', $values);

// The entity is now created, but we have not yet simplified use of it.
// Now create an entity_metadata_wrapper around the new node entity
// to make getting and setting values easier
$ewrapper = entity_metadata_wrapper('node', $entity);

// Using the wrapper, we do not have to worry about telling Drupal
// what language we are using. The Entity API handles that for us.
$ewrapper->title->set('YOUR TITLE');

// Setting the body is a bit different from other properties or fields
// because the body can have both its complete value and its
// summary
$my_body_content = 'A bunch of text about things that interest me';
$ewrapper->body->set(array('value' => $my_body_content));
$ewrapper->body->summary->set('Things that interest me');

// Setting the value of an entity reference field only requires passing
// the entity id (e.g., nid) of the entity to which you want to refer
// The nid 15 here is just an example.
$ref_nid = 15;
// Note that the entity id (e.g., nid) must be passed as an integer not a
// string
$ewrapper->field_my_entity_ref->set(intval($ref_nid));

// Entity API cannot set date field values so the 'old' method must
// be used
$my_date = new DateTime('January 1, 2013');
$entity->field_my_date[LANGUAGE_NONE][0] = array(
   'value' => date_format($my_date, 'Y-m-d'),
   'timezone' => 'UTC',
   'timezone_db' => 'UTC',
 );

// Now just save the wrapper and the entity
// There is some suggestion that the 'true' argument is necessary to
// the entity save method to circumvent a bug in Entity API. If there is
// such a bug, it almost certainly will get fixed, so make sure to check.
$ewrapper->save();
}
```

Be sure to note that in the Entity API example, the functions node_object_prepare and node_submit are not necessary and should not be used. Again, the Entity API handles those tasks.

For more on using the Entity API, just search the web for "drupal entity_api". The number of articles, tutorials, and videos on the subject is a testament to the fantastic work done by *fago* -- the entity API maintainer.
