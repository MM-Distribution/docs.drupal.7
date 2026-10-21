---
title: "Static and Dynamic Thumbnails for Facebook"
source_url: "https://www.drupal.org/docs/7/theming/howto/static-and-dynamic-thumbnails-for-facebook"
page_type: page
last_updated: "Last updated on 8 September 2016"
published: "2011-11-22T18:43:00+00:00"
modified: "2016-09-08T14:07:08+00:00"
breadcrumb: ["Drupal 7", "Theming Drupal 7", "Theming HowTos"]
fetched: "2026-10-21T08:52:00Z"
raw: "raw/docs/7/theming/howto/static-and-dynamic-thumbnails-for-facebook.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Static and Dynamic Thumbnails for Facebook

We wanted to declare a specific version of our logo as available when sharing to Facebook from a site, but also to retain the ability to select images from the shared page. The standard meta-tag method limited us to a single thumbnail, and prevented page-specific thumbnails from appearing.

To provide both static and page-specific thumbnails, add the new image for all pages to the header area of the page template and assign to it the existing Drupal “element-invisble” class. Facebook will still load and display this "invisible" image, along with other suitable images on the page.

Modified *page.tpl.php* code (second line added):

``` php
<div id="header"><div class="header-inner section clearfix">
 <img class="element-invisible" src="http://www.example.com/sites/default/files/public/logo-for-fb.gif">
<?php print render($page['header']); ?>
```

CSS class:  
.element-invisible {  
clip: rect(1px, 1px, 1px, 1px);  
position: absolute !important;  
}

Because the image doesn’t belong in the main flow of the document, we also added another class, with a rule to move it off-screen and confirm that it wouldn’t show up (left: -999px;).

After making changes, you may wish to clear Facebook's cache for a given page here:  
<http://developers.facebook.com/tools/lint/>
