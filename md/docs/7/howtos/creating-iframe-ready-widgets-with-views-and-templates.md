---
title: "Creating iFrame-ready Widgets with Views and Templates"
source_url: "https://www.drupal.org/docs/7/howtos/creating-iframe-ready-widgets-with-views-and-templates"
page_type: page
last_updated: "Last updated on 25 January 2018"
published: "2011-11-29T18:37:13+00:00"
modified: "2018-01-25T23:51:24+00:00"
breadcrumb: ["Drupal 7", "Site building and development HowTos for Drupal 7"]
fetched: "2026-10-21T08:03:21Z"
raw: "raw/docs/7/howtos/creating-iframe-ready-widgets-with-views-and-templates.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Creating iFrame-ready Widgets with Views and Templates

You can use views and a specific, trimmed-down page template to create blocks or pages containing widget content to be viewed in an iframe.

## Requirements:

- Views
- Page and (optionally) views templates
- Theme preprocessing functions (preprocess_html and preprocess_page)
- CSS styles

## Procedure

1.  Define a path specific to widgets.

    Widget layout will be determined by a path on your site, which will contain your widget pages or blocks: for example, *[www.example.com/widgets/](http://www.example.com/widgets/)*

2.  Create views for your widgets

    Create a view for each block or page of widget content, containing only the content you want to display in the widget.

    When creating views pages, make sure the path begins with the argument you’re using for widgets.  
    For example, if you are using the path /widgets/ for widgets, you might use the page path: */widgets/first-widget*

3.  Copy your theme's *page.tpl.php* to a new template for pages containing any widget-related view. Menus etc. should be removed from these pages.
    - Here’s a sample widget-page template based on the Bartik theme (and named *page--widgets.tpl.php*):  

      ``` php
      <div id="content" class="widget-block">
          <?php  
              if ($page['content']['system_main']['main']) {  
              $page_content = $page['content']['system_main']['main']['#markup'];

              // Widget pages: add 'parent' target to node links
              $page['content'] = preg_replace('/<a (.+?)>/','<a $1 target="_parent">',$page_content);
          }
          ?>
          <?php print render($page['content']); ?>
      </div> <!-- /.section, /#content -->
      ```

      Page wrapper, header, tabs, and other sections have been removed: only the main content will be displayed in the final iframe.  
      Be sure to adjust this section to suit the main-content area of your theme, to preserve basic theme styling as desired.

      The *widget-block* class has been added to the block content so that the widget can be given a specific size, etc.

    - The example above is based on the suggestion found here:  
      <http://stackoverflow.com/questions/4042366/create-an-iframe-from-a-drupal-website>  
      A line has also been added to add targets to widget content links, set to ‘parent’, so that widget links aren’t opened inside the iFrame.

4.  You can also alter the views templates themselves as needed. The views template for standard widgets created as pages or blocks is *views--view.tpl.php*.

5.  Create a page for each of your views blocks, making sure to use your widget-specific path. Assign the blocks to their pages in *Structure-\>Blocks*.

6.  Use theme functions to assign a template and body class to your widgets.
    - In *yourtheme_preprocess_page*, assign your widget page template to all widget pages on the site, according to your selected path:  

      ``` php
      <?php
      function bartik_preprocess_page(&$variables) {
        // Check path to determine widget pages
        $pathargs = explode('/',request_uri());
        if ($pathargs[1] == 'widgets') {
           // Use template: page__widgets
           $variables['theme_hook_suggestion'] = 'page__widgets';
        }
      }
      ?>
      ```

      Note that the line beginning “if(\$pathargs …” will need to be changed according to which section of your path is being checked, and its name.

    - In *yourtheme_preprocess_html*, add a class to the body of all widget pages for CSS styling (so that you can center widget content, etc., as needed).  

      ``` php
      <?php
      function bartik_preprocess_html(&$variables) {
      // Add a widget-page class to all widget pages, by path  
          if (isset($variables['page'])) {   
              $pathargs = explode('/',request_uri());
              if ($pathargs[1] == 'widgets') {
                  $variables['classes_array'][] = 'widget-page';
              }
          }
         }
      ?>
      ```

      You can use additional paths and argument checks here suggest other templates based on size, etc.; e.g. */widgets/300x250/*.  
      Now your site’s widget pages should contain only the views content you have created. (If you’re logged in, you will probably see your administrative toolbar also.)

7.  Style your widgets as needed.

    Sample CSS (based on Bartik):

    - This rule may be useful in removing any page background you’re using:  

      ``` php
      body.widget-page {
        background: transparent;
      }
      ```

    - Make sure default page styling doesn’t interfere with widget sizing or placement:  

      ``` php
      body.widget-page #content, body.widget-page #sidebar-first, body.widget-page #sidebar-second {
      float: none;
      display: block;
      }  
      ```

    - This rule sets the widget block to a specific size, centered, with a white background and a rounded black border:  

      ``` php
      #content.widget-block {
      margin: 0 auto;
      width: 400px;
      text-align: left;   
      overflow: hidden;
      background-color: #fff;
      border: 1px solid #000;
      border-radius: 7px 7px 7px 7px;
      padding: 5px 10px;
      }
      ```

Once the pages are ready, just drop the widget link into an iframe tag like this one:  
(You may need to adjust the widget and iframe size in order to prevent scrollbars from appearing.)

``` php
<iframe frameborder="0" style="border: none;" width="400" height="400"
src="http://www.example.com/widgets/first-widget"
seamless="seamless">
</iframe>
```

This code can now be used on other websites, and you can change the content simply by updating the view for that widget.
