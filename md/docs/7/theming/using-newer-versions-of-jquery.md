---
title: "Using Newer Versions of jQuery"
source_url: "https://www.drupal.org/docs/7/theming/using-newer-versions-of-jquery"
page_type: page
last_updated: "Last updated on 11 March 2021"
published: "2011-02-11T01:50:33+00:00"
modified: "2021-03-11T21:35:31+00:00"
breadcrumb: ["Drupal 7", "Theming Drupal 7"]
fetched: "2026-10-21T06:04:33Z"
raw: "raw/docs/7/theming/using-newer-versions-of-jquery.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Using Newer Versions of jQuery

You will often need a newer version of jQuery to use a certain jQuery plugin. There are several ways to achieve this.

Note that the JavaScript in Drupal core depends on the specific version of jQuery that is packaged with core. Drag and drop, table sorting, and other features may not work with higher versions of jQuery unless you adapt the code of those core .js files. If you only need a higher version of jQuery for a certain plugin, specify that it should only be swapped for the frontend of your site or for the specific page it is needed.

## jQuery update

[jQuery update](http://drupal.org/project/jquery_update) takes care of the changes needed in core javascript code so it stays compatible also in the backend. This is the simplest way and other methods should only be used if you have problems with it.

## Method 1: Using hook_js_alter

In Drupal 7 you can use [hook_js_alter](http://api.drupal.org/api/drupal/modules%21system%21system.api.php/function/hook_js_alter/7) for replacing jQuery conditionally. This way you don't need to load jQuery twice which is better for performance and you also don't need to adapt your code. You can easily wrap some conditions around so it only targets the front-end pages where you need an updated version of jQuery and avoid breaking the backend js.

``` php
function hook_js_alter(&$javascript) {
  // Swap out jQuery to use an updated version of the library. 
  $javascript['misc/jquery.js']['data'] = drupal_get_path('module', 'jquery_update') . '/jquery.js';
}
```

In Drupal 6 you can use [JS Alter](http://drupal.org/project/jsalter), which has a similar hook.

## Method 2: Running 2 versions of jQuery side-by-side - the jQuery noConflict() function.

### jQuery Multi module

Note: The [jQuery Multi module](http://drupal.org/project/jqmulti) has built an interface around this method.

### The Problem

Your custom theme, dropdown menu, slideshow, or other jQuery-dependent scripts require jQuery 1.4, jQuery UI 1.8, or some other jQuery version or component. Drupal 6 ships with jQuery 1.2.6. You could just replace the jquery.js file in example.com/misc with a newer version, but you'd run into some issues, such as:

- Useful UI features like draggable tables and ajax search will stop working
- Contributed modules that use jQuery assume you are using 1.2.6
- After updating Drupal to a newer version, your custom jquery.js file would be overwritten with 1.2.6

### The Solution

jQuery already has the functionality to run along side a different version of jQuery (or, really, along side any other JavaScript library that uses the \$ symbol as a function or variable). This is the **`noConflict()`** function. You can view the API page here: <http://api.jquery.com/jQuery.noConflict/>

To use this functionality within your project, simply tell the browser about your new jQuery library and that you'll be referencing it via your custom noConflict identifier:

``` php
<script type="text/javascript" src="//ajax.googleapis.com/ajax/libs/jquery/1.4.4/jquery.min.js"></script>
<script type="text/javascript"> 
  var $jq = jQuery.noConflict(); 
</script> 
```

### Example: my-theme/page.tpl.php

``` php
<head>
  <title><?php print $head_title; ?></title>
  <?php print $head; ?>
  <?php print $styles; ?>
  <script type="text/javascript" src="//ajax.googleapis.com/ajax/libs/jquery/1.4.4/jquery.min.js"></script>
  <script type="text/javascript"> 
    var $jq = jQuery.noConflict(); 
  </script> 
  <?php print $scripts; ?>
</head>
```

With this method jQuery 1.2.6 is loading with every page, and can be used by Views, Draggable.js, any contributed Ajax calls, etc. Also, jQuery 1.4.4 (as in this example) is also loading and the 2 are not interfering with each other. Another point worth adding is that 1.4.4 is being loaded from the Google CDN - one less file for your audience to download from your server.

### Using noConflict in your scripts

To execute scripts with the *new* version of jQuery you simply need to use `$jq` instead of `$` in your scripts, for example:

``` php
$jq(document).ready(function(){
  $jq('#my-div').function();
});
```

More information about this method: <http://www.drupal.org/node/578712>

### Using noConflict in contributed scripts

You can easily modify an external script to use your custom noConflict identifier. For example, the Qtip library depends on jQuery 1.5. You could include it via the above methods and then alter `jquery.qtip.js`, replacing the first line

`(function($, window, undefined) {`

with

`(function($jq, window, undefined) {`

## Method 3: Using jquery_update module

Unfortunately as long as the patch in [\#426764: Allow other modules to alter the replacements](/project/jquery_update/issues/426764 "Status: Closed (outdated)") has not landed for Drupal 6 you need to hack the jquery_update module as described in [\#1184704: Load different jQuery version on specified page.](/project/jquery_update/issues/1184704 "Status: Closed (outdated)").

Example: Install jquery-1.7.1.js in /jquery_update/replace and hack the last bit of code of the jquery_update.module as follows

``` php
/**
 * Return the path to the jQuery file.
 */
function jquery_update_jquery_path() {
  if (arg(0) =='admin' || arg(1) == 'add' || arg(2) == 'edit' || arg(0) == 'panels' || arg(0) == 'ctools') {
    $jquery_file = array('none' => 'jquery.js', 'min' => 'jquery.min.js');
    return JQUERY_UPDATE_REPLACE_PATH . '/' . $jquery_file[variable_get('jquery_update_compression_type', 'min')];
  }
  else {
    $jquery_file = array('none' => 'jquery-1.7.1.js', 'min' => 'jquery-1.7.1.min.js');
    return JQUERY_UPDATE_REPLACE_PATH . '/' . $jquery_file[variable_get('jquery_update_compression_type', 'min')];
  }
}
```

## Method 4: Swapping jQuery with preprocess page

This method has the advantage that it is specific for your theme, so if you use a different backend theme for the administration of your site, you normally should not have any problems with core js files not working anymore.

``` php
function yourModuleOrThemeName_preprocess_page(&$variables) {
  // exclude backend pages to avoid core js not working anymore
  // you could also just use a backend theme to avoid this
  if (arg(0) != 'admin' || !(arg(1) == 'add' && arg(2) == 'edit') || arg(0) != 'panels' || arg(0) != 'ctools') {
    $scripts = drupal_add_js();
    $new_jquery = array(drupal_get_path('theme', 'YOURTHEME') . '/js/jquery-1.7.1.min.js' => $scripts['core']['misc/jquery.js']);
    $scripts['core'] = array_merge($new_jquery, $scripts['core']);
    unset($scripts['core']['misc/jquery.js']);
    $variables['scripts'] = drupal_get_js('header', $scripts);
  }
}
```
