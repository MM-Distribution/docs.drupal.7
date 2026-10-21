---
title: "Example: creating a Garland sub-theme that utilizes the Color module"
source_url: "https://www.drupal.org/docs/7/theming/example-creating-a-garland-sub-theme-that-utilizes-the-color-module"
page_type: page
last_updated: "Last updated on 21 May 2023"
published: "2013-04-12T19:35:12+00:00"
modified: "2023-05-21T11:23:11+00:00"
breadcrumb: ["Drupal 7", "Theming Drupal 7"]
fetched: "2026-10-21T06:03:46Z"
raw: "raw/docs/7/theming/example-creating-a-garland-sub-theme-that-utilizes-the-color-module.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Example: creating a Garland sub-theme that utilizes the Color module

Let's say you want to use Garland as your base theme, but want to be able to make CSS tweaks to it and want to keep the Color module functionality that is integrated in it by creating a subtheme.

My Garland subtheme is called my_garland.

### Make your sub-theme directory and .info file

Create your subtheme directory in sites/all/themes/my_garland.

Create a my_garland.info file and add the following to it. This is how you let Drupal know your subtheme exists and that it should show it in admin/appearance.

``` php
name = My Garland
description = My subtheme of Garland
core = 7.x
base theme = garland
;stylesheets[all][] = style.css 
stylesheets[all][] = my_garland.css
```

Notice that we're ***not*** including style.css as we have commented it out. It's just there to remind us that it is inherited automatically as described in [creating a sub theme](https://www.drupal.org/docs/7/theming/creating-a-sub-theme), style inheritance.

### Make your sub-theme CSS file

Create a my_garland.css file. This can be empty until you decide to start adding your custom css which will override or be used in addition to Garland's style.css file.

### Copy Garland's color and images directory

In order to use the Color module, you need to copy over the color and images directory from Garland. Copy themes/garland/color and themes/garland/images to sites/all/themes/my_garland/color and . There should now be a directory in your subtheme folder that is identical to the one in Garland's.

Now that this is here, when you go to your new themes Settings, you will see the color wheel and the dropdown list of color schemes just like in Garland. Note that you need to make the color changes to your subtheme's settings -- not Garland's. The color scheme is not inherited, so your subtheme cannot know about the colors chosen by the parent.

### So, why isn't this working yet?

Yet at this point, if you make changes to your subtheme's color scheme the changes do not show up. No matter what colors you may have chosen for my_garland or Garland, you just get that same icy blue. If you look in themes/garland/color you can see all those icy blue pngs that are currently being used. And you can see style.css referencing them in the images directory:

``` php
/**
 * Layout
 */
.region-header {
  min-height: 1em;
  background: #d2e6f3 url(images/bg-navigation.png) repeat-x 50% 100%;
}
```

### Template.php is the missing link

Here's where template.php comes in. And here's also why it is confusing. Subthemes inherit what is in template.php. And if you look closely at that file in Garland, way down at the bottom there's this:

``` php
/**
 * Override or insert variables into the page template.
 */
function garland_process_page(&$vars) {
    // Hook into color.module
    if (module_exists('color')) {
        _color_page_alter($vars);
    }
}
```

Huh, looks like my subtheme should be all set when it comes to the color module. But, apparently not. (**Anyone with the technical knowledge:** it would be interesting to have an idea of why this is -- or why I am incorrect.)

You need to add your own template.php file to your subtheme directory that will mimic this function -- if you simply tried to copy the template.php file from Garland to your subtheme you will generate an error, since (as stated here: <http://drupal.org/node/225125> ), preprocess functions are not overridden, they are repeated. PHP does not like it when two functions with the same name are defined.

So, to keep things simple, just add the function above but alter its name to reflect that it is in your subtheme by renaming it my_garland_preprocess_page():

``` php
function my_garland_preprocess_page(&$vars) {
    // Hook into color.module
    if (module_exists('color')) {
        _color_page_alter($vars);
    }
}
```

And that should be it! Now, remember to clear your theme registry by clearing your cache by going to admin/config/development/performance or using the magic of drush: drush cc. With Garland and your subtheme enabled, and your subtheme set as the default theme, you should now see changes you make to the color in your subtheme's settings.

### What is going on here? My hypothesis

So, what exactly is going on here? Why don't you need to have a style.css in your subtheme folder? Because (as far as I can surmise) my_garland_process_page() changes the path to style.css which will be used AND alters some of the content in it reflecting that the .png images now reside in the same directory as style.css. Compare directories within sites/default/files/color/ to the themes/garland/image directory.

That said, even if you do not have a style.css file in your subtheme directory, you still must add it to your .info file with stylesheets\[all\]\[\] = style.css. Again (I can only surmise) it would seem that my_garland_process_page() depends on this bit of information in the .info file to know it needs to create a reference to it in the header of a page. (\*don't know is it true, as without copy the style.css, the color cannot change)

HOWEVER, if you now take a look at the source of any of your pages, you will only find style.css buried in minified jQuery. So, what **exactly** is going on here remains obfuscated, from my perspective, for good or ill.
