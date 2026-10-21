---
title: "Beginners guide to overriding themable output"
source_url: "https://www.drupal.org/docs/7/theming/overriding-themable-output/beginners-guide-to-overriding-themable-output"
page_type: page
last_updated: "Last updated on 27 September 2016"
published: "2009-05-08T19:50:01+00:00"
modified: "2016-09-27T00:30:41+00:00"
breadcrumb: ["Drupal 7", "Theming Drupal 7", "Overriding themable output"]
fetched: "2026-10-21T08:17:49Z"
raw: "raw/docs/7/theming/overriding-themable-output/beginners-guide-to-overriding-themable-output.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Beginners guide to overriding themable output

Drupal theming is based on the concept of *overriding* the output from Drupal core and modules. Instead of having to modify the module to change the output (which you don't want to do, because it will make upgrades difficult later), you can modify it by adding functions or files to your theme. The functions or files will take precedence over the module's choice for how to produce the HTML.

Overriding is done one of two ways: overriding **theme functions**, or overriding **theme files**, depending on how the output from Drupal is being created.

## Avoiding having to override at all

Before you decide that you need to modify the output coming from Drupal or one of the modules on your site, check the following possibilities -- you may be able to avoid the whole process:

- Can you just change a setting? For instance, you can click on a "Configure" link for any block, and it will allow you to change the text of the block title, or even remove the title completely (you can also move any block to a different region of the page on the blocks configuration screen). Other modules will let you change aspects of their output through settings too (labels for text fields, order of output, etc.). To find settings pages, click on Administer, and then By module, and check out all the settings pages offered by your module. Some settings are also on your theme's configuration page, and some are in various tabs of your content types' settings pages (under Content management \>\> Content types).
- Can you accomplish your goal through CSS? Nearly all output in Drupal is enclosed in DIV elements with specific classes or IDs, so you can easily customize a particular piece of output. CSS will let you change fonts, sizes, placement, background images, etc. To override the CSS provided by Drupal or a module, just add to one of your theme's CSS files.

If neither of these options lets you change what you want to customize, then you do actually need to customize the HTML output of Drupal or one of your modules -- read on.

## Overriding theme functions

A theme function is a PHP function in Drupal whose name begins with 'theme\_', such as 'theme_username'. To override a theme function:

1.  Open your theme's *template.php* file in a plain text editor.

2.  Copy the theme or template function you found into your *template.php* file. (One way of finding the function is searching for the function name at <http://api.drupal.org>. There is also a Function reference in the menu provided by the [Devel](http://drupal.org/project/devel) module.)

3.  Rename the function you copied in (see note below). If your theme's base prefix is "wonderful", and the theme function you are trying to override is called "theme_xyz", then you need to rename the function "wonderful_xyz". If you are overriding "template_preprocess_xyz", then the new name should be "wonderful_preprocess_xyz".

    To change a function name, e.g. from "theme_xyz" to "wonderful_xyz", find a line that looks something like this:

    ``` php
    function theme_xyz( $a, $b, $c) {
    ```

    and change it to:

    ``` php
    function wonderful_xyz( $a, $b, $c) {
    ```

    Make sure you leave the part inside the parentheses unchanged!

4.  Modify the function so that it does what you want it to do.

5.  Upload the template.php file to your web site, in your theme directory.

6.  Refresh the theme cache (see <http://drupal.org/node/173880#theme-registry>).

## Overriding a template file

If the HTML output you want to override is in a template file, here are the steps to override it:

1.  Copy the template file to your theme directory, if your theme directory does not already have a file by that name.
2.  If you are implementing a [*suggestion*](http://drupal.org/node/223440), rename the file to the suggestion name it should have. Note that some suggestion files will not be recognized unless their base file is also present -- for instance, if you want to make a node content type suggestion file for your content type, you need to have node.tpl.php present in your theme directory order for your node-my_content_type.tpl.php file to be recognized. However, suggestions for Views do not require that the base Views template file be present in your template directory.
3.  Modify the file so it does what you want it to do.
4.  Upload the file to your web site, including the new base theme file if necessary, into your theme's directory.
5.  Refresh the theme cache (see <http://drupal.org/node/173880#theme-registry>)

## Finding where the themable output is coming from

The first step in overriding Drupal's HTML output is to figure out where the HTML output you want to modify is coming from. What you are looking for is either a *theme function* (a PHP function called "theme_xyz", such as "theme_search" or "theme_aggregator_block_item"), a *template preprocess function* (a PHP function called "template_preprocess_xyz"), or a *theme file* (a PHP file whose name ends in .tpl.php, such as "views-more.tpl.php").

To find the right file or function, start by finding the module directory for the module that is producing the output (under "modules", "sites/all/modules", or "sites/your_sub_dir/modules"). Theme files will generally be in either the top-level module directory, a sub-module directory underneath, or a directory called "theme" underneath. Theme and template preprocess functions will generally be in either a module file (ending in .module) or an include file (usually ending in .inc); the file will be located in the module directory or a sub-directory. A good way to find the right function or file is to search for a specific CSS ID or class on the HTML element you are trying to modify, or some other unique text that the module is producing.

Another method of finding the appropriate override function is using the [Theme developer](http://drupal.org/project/devel_themer) module, which is an add-on to the popular [Devel](http://drupal.org/project/devel) project. When enabled, Theme Developer allows the site builder to hover over the elements of the page and click the ones where more theme information is required.

Some modules also will honor theme file *suggestions*. For instance, in Views 2, you can get theme information when you are editing a View -- it tells you which theme files will be used to produce the view, and the first one in each list is a theme file that is located in the "themes" sub-directory of your views module; this is the theme file you will want to override. The other names in the list are possibilities for what you will want to name the file when you put it into your theme, depending on how specific you want your override to be (e.g., do you want to override how all views are displayed, or just your specific view?).

You can also use suggestions to override core Drupal module theming. For instance, if you want to override how a particular node content type is displayed, you can use the node.tpl.php file from your theme (or Drupal core) as the overrideable file, and rename the copy node-content_type_name.tpl.php. There is more information about the core module files and suggestion file names you can use on the [Core templates and suggestions](http://drupal.org/node/190815) page.

Once you have found the right function or file to override, follow the directions in one of the next two sections to override it.

However, if you find what is producing the HTML output you want to override, and it is not inside a theme function, template preprocess function, or theme file, then you will probably not be able to modify the output with theme functions alone. You may need to check the support forums or contact the module developer to find out how to modify the output.
