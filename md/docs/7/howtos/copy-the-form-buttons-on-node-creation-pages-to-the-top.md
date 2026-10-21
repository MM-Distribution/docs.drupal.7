---
title: "Copy the form buttons on node creation pages to the top"
source_url: "https://www.drupal.org/docs/7/howtos/copy-the-form-buttons-on-node-creation-pages-to-the-top"
page_type: page
last_updated: "Last updated on 1 November 2016"
published: "2012-01-24T14:05:30+00:00"
modified: "2016-11-01T16:31:20+00:00"
breadcrumb: ["Drupal 7", "Site building and development HowTos for Drupal 7"]
fetched: "2026-10-21T08:01:48Z"
raw: "raw/docs/7/howtos/copy-the-form-buttons-on-node-creation-pages-to-the-top.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Copy the form buttons on node creation pages to the top

**Background:**

I have a custom content type with a lot of form elements (close to 100) and scrolling down to the bottom got a bit irritating when all you wanted to do it update or edit a node of this content type.  
So I wanted to copy the form action buttons to the top (but still keep them at the bottom).

Here is how I did it:

1\) Create a custom module

1a) In your sites/default/modules/ folder create a new folder CUSTOM_MODULE\*

1b) Create the mandatory CUSTOM_MODULE.info and CUSTOM_MODULE.module files.

1c) Fill out the CUSTOM_MODULE.info file with some basic info. eg:

``` php
name = Custom node form modify module
description = Custom module to duplicate the form buttons on node creation forms and place them above the form items.
package = Custom
core = 7.x
version = 0.1
```

1d) Copy the following code into the CUSTOM_MODULE.module file. I'll then go through the code to explain what it does.

``` php
/**
* Implementation of HOOK_form_alter()
*/
function CUSTOM_MODULE_form_alter(&$form, $form_state, $form_id) {

  /**
   * Copy the action buttons (submit, preview, etc ..) 
   * and place them at the top of the form
   */
  if(!empty($form['actions'])) {

    foreach($form['actions'] as $name => $button) {
      
     // I DEFINE EACH BUTTON SEPERATELY BECAUSE I WISH TO DEFINE THE ORDER
     // OTHERWISE YOU COULD SIMPLY USE:

/*
        $form["$name-copy"] = $button;
        $form["$name-copy"]['#weight'] = -1000;
*/

      
      // SUBMIT BUTTON
      if($name == 'submit') {
        // WE NEED TO USE DOUBLE QUOTATION MARKS 
        // SO PHP CAN SEE AND INTERPRET VARIABLES WITHIN
        $form["$name-copy"] = $button;
        $form["$name-copy"]['#weight'] = -1001;
      }
      
      // PREVIEW BUTTON
      if($name == 'preview') {
        // WE NEED TO USE DOUBLE QUOTATION MARKS 
        // SO PHP CAN SEE AND INTERPRET VARIABLES WITHIN
        $form["$name-copy"] = $button;
        $form["$name-copy"]['#weight'] = -1000;
      }
      
      // CHANGES DEPENDS ON DIFF MODULE
      if($name == 'preview_changes') {
        // WE NEED TO USE DOUBLE QUOTATION MARKS 
        // SO PHP CAN SEE AND INTERPRET VARIABLES WITHIN
        $form["$name-copy"] = $button;
        $form["$name-copy"]['#weight'] = -999;
      }
      
      // DELETE BUTTON
      if($name == 'delete') {
        // WE NEED TO USE DOUBLE QUOTATION MARKS 
        // SO PHP CAN SEE AND INTERPRET VARIABLES WITHIN
        $form["$name-copy"] = $button;
        $form["$name-copy"]['#weight'] = -998;
      }            

    } // end foreach
  }

}
```

As you can see we simply use the hook_form_alter() function to modify the form. If you only wish to apply this module to a single content type, you can filter the function by using:

``` php
if ($form_id == 'CONTENT_TYPE_node_form') {

// PLACE CODE IN HERE AND RENAME CONTENT_TYPE TO YOUR CONTENT TYPE
// CHECK THE FORMS SOURCE CODE IF UNCERTAIN OR USE 
// dsm($form); // requires the devel module

}
```

2\) Enable the module.

3\) Clear Cache.

4\) Try it out

\* you may rename CUSTOM_MODULE to whatever you want, just make sure you rename it everywhere.
