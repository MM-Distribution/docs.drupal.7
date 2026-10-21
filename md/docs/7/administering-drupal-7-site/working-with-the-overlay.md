---
title: "Working with the overlay"
source_url: "https://www.drupal.org/docs/7/administering-drupal-7-site/working-with-the-overlay"
page_type: page
last_updated: "Last updated on 29 September 2018"
published: "2009-12-10T23:47:44+00:00"
modified: "2018-09-29T06:21:57+00:00"
breadcrumb: ["Drupal 7", "Administering Drupal 7 site"]
fetched: "2026-10-21T05:59:38Z"
raw: "raw/docs/7/administering-drupal-7-site/working-with-the-overlay.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Working with the overlay

The administrative overlay makes it easier to administer a Drupal site by displaying administrative pages as a layer over the current page (using JavaScript), rather than replacing the page in your browser window. Once an overlay is active, you can use the close link on the overlay to return to the page you were viewing before you clicked the link. In a "Standard" install, the Overlay module is enabled by default.

## Uses

### Example

Administrative interface **without** the overlay:  
![](/files/non-overlay.png)

Administrative interface **with** the overlay:  
![](/files/overlay.png)

### Accessing the overlay

When enabled, the overlay will appear when you click on administrative links. If you manually enter a URL in your browser, overlay will not be used. To reset so that overlay is used again, leave the admin section of your site, then return to the page on which you want to use overlay.

### Roles and permissions

Users must have "access overlay" permission in order to see administrative pages in the overlay.

## Disabling

1.  On the admin toolbar, click *Modules*.
2.  In the Core section, disable the *Overlay* module.
3.  Click *Save Configuration*.

## Altering the appearance of the overlay

This is an advanced topic and the task should not be necessary in the majority of cases of Drupal administration. However, if you find that a node is not displaying correctly inside the overlay, the overlay can be modified using code.

The following example shows how to modify the overlay when a specific node type (test) is displayed inside the overlay. The script re-sizes the overlay to 450px wide and also hides some unwanted items.

If you want to alter all the layouts no matter what, then [overlay.tpl.php](http://api.drupal.org/api/drupal/modules--overlay--overlay.tpl.php/7) would be a better choice.

Declare your hook:

``` php
function mymodule_overlay_child_initialize() {
  // Add our custom JavaScript.
  drupal_add_js(drupal_get_path('module', 'mymodule') . '/overlay-child.js');
}
```

Add the code to your JavaScript file:

``` php
(function ($) {

  // Adjust the overlay dimensions.
  Drupal.behaviors.myModule = {
    
    attach: function (context) {
      $('#overlay:not(.mymodule-adjusted)', context).each(function() {
        var $test = $(this).find('.node-type-test');
        
        if ($test.length){
          // adjust the overlay
          $(this).css({
            'width'     : '450px',
            'min-width' : '450px'
          });
            
          $('.add-or-remove-shortcuts', this).hide();  // hide "add short-cut" button
          $('#branding', this).hide();  // hide branding container
        }  
      }).addClass('mymodule-adjusted');
    }
    
  };

})(jQuery);
```
