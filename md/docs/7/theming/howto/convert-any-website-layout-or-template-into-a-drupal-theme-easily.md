---
title: "Convert any website layout or template into a Drupal theme - easily!"
source_url: "https://www.drupal.org/docs/7/theming/howto/convert-any-website-layout-or-template-into-a-drupal-theme-easily"
page_type: page
last_updated: "Last updated on 11 July 2018"
published: "2008-09-25T19:45:41+00:00"
modified: "2018-07-11T20:48:02+00:00"
breadcrumb: ["Drupal 7", "Theming Drupal 7", "Theming HowTos"]
fetched: "2026-10-21T08:27:42Z"
raw: "raw/docs/7/theming/howto/convert-any-website-layout-or-template-into-a-drupal-theme-easily.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Convert any website layout or template into a Drupal theme - easily!

Theming for Drupal is not actually as hard as you may think. Certainly there are more advanced areas of theming possible with Drupal, which may or may not be necessary depending on the needs of your site or whether there are subtle defaults which you wish to change (and which you can learn about if and when they become necessary for your site). Creating the "overall theme" for your site though is very simple.

A Drupal theme is nothing more than a standard website layout, with a few bits of PHP code added in certain places, which you can simply copy/paste into place in order to call up Drupal's "dynamic" content and features in those spots.

If you learn better visually, videos are available which cover much of the same information that will be illustrated here: [Acquia Webinar](http://acquia.com/community/resources/acquia-tv/tips-and-tricks-drupal-theming-90-minute-tutorial).

**Contributed/downloaded themes are more complex than "your" theme needs to be**

You may have looked at various pre-made themes that either come with Drupal core or are [available for download](http://drupal.org/project/Themes), and sighed with frustration upon seeing their code. To some, the code looks very confusing.

Keep in mind that those themes have been created to address the needs of many people. The themes must be able to handle all kinds of scenarios, which means they have been designed to allow you to dynamically add various columns and other layout elements, and to support custom theming for features and modules which you might not even need. These themes usually include a large amount of PHP code that essentially says, *"If this setting is true, then show this part this way, or else show that."* This makes the theme very flexible, but also very complicated.

However, your theme doesn't need to work for everyone. It only needs to do the things your site requires and nothing more. All that you need are a few bits of PHP, which you can simply copy and paste into your own HTML template. These PHP snippets tell Drupal to load its dynamic content in those spots.

You might also find it useful to have a look at Drupal's "most basic" core template files (those used when a theme doesn't provide any alternative template files to override them). To view these basic templates, look in the */modules/system* folder of your Drupal installation (in particular, look at *page.tpl.php* and *node.tpl.php*).

**Just a few simple & basic elements make up a Drupal theme**

The "main" template file in Drupal is called *page.tpl.php*. Make a copy of your website layout/template and call it *page.tpl.php*. Then, simply paste the following bits of code into your layout, in the locations noted (all the code mentioned in this lesson goes in the *page.tpl.php* file).

## Starting your page

**If you're using Drupal 5:**

``` php
<html xmlns="http://www.w3.org/1999/xhtml" lang="<?php print $language ?>" xml:lang="<?php print $language ?>">
```

**If you're using Drupal 6:**

``` php
<html xmlns="http://www.w3.org/1999/xhtml" lang="<?php print $language->language ?>" xml:lang="<?php print $language->language ?>" dir="<?php print $language->dir ?>">
```

**If you're using Drupal 7:**  
If you are using Drupal 7, your page.tpl.php file starts after the \<body\> tag and ends before the \</body\> tag, so you do not need to worry about the doctype, html, or head tags. If you'd like to override these, copy the html.tpl.php file from your modules/system folder and make whatever changes you'd like.

This is the recommended way to start your page, rather than just using \<html\>. The extra definitions here aid in proper validation and language handling of the resulting HTML markup.

## The \<head\> section of your site

``` php
<head>
  <title><?php print $head_title; ?></title>
  <?php print $head; ?>
  <?php print $styles; ?>
  <?php print $scripts; ?>
</head>
```

## The side bars or columns of your layout

Most websites have a left and/or right column next to the "main" larger content area. These side bars usually contain various features and information (for instance a log-in form, navigation, recent comments, etc). In Drupal these features/information are called "Blocks", and you can customize where they show up on your page by going to **Administer \> Site building \> Blocks** *(admin/build/block)*. In order for Drupal to know *where* to put the Blocks though, you need to add some "placeholders" to your theme (Drupal calls these placeholders "Regions"). There are more of these placeholders available (and you can create your own custom ones too) but it's important to add the side bar one(s) at first, since the admin menu appears in them. Add the below Region(s) to your side bar:

**If you're using Drupal 5:**

``` php
<?php print $sidebar_left; ?>

...and/or...

<?php print $sidebar_right; ?>
```

**If you're using Drupal 6:**

``` php
<?php print $left; ?>

...and/or...

<?php print $right; ?>
```

**If you're using Drupal 7:**

``` php
<?php print render ($page['sidebar_first']); ?>

...and/or...

<?php print render ($page['sidebar_second']); ?>
```

## Menu system / navigation

Drupal's default menu for your site's content is called **Primary Links**. There is also a **Secondary Links** menu which can show related sub-pages under the Primary menu. When stripped of all images and styles, a menu in Drupal is nothing more than a nested unordered list, in plain HTML, with links for each list item. You can use CSS to style a menu in any way you want; changing how it looks, whether it is horizontal (like tabs) or vertical, etc.

To make the Primary and Secondary Links menus appear on your site, paste the following into either the top area of your theme (for instance, if your menu is going to be styled as tabs or buttons), or in the sidebar area (for instance if you plan to have your menu show vertically in the sidebar).

**Simple way:**

Here's the simple version to use, if you're already sure you want to use "both" Primary and Secondary Links (or feel free to delete the Secondary Links portion if you don't need it):

``` php
<div id="primary">
  <?php print theme('links', $primary_links); ?>
</div> <!-- /#primary -->

<div id="secondary">
  <?php print theme('links', $secondary_links); ?>
</div> <!-- /#secondary -->
```

**More flexible way:**

If you're not sure that you will have both Primary and Secondary Links, you could use the following code instead (it's the same, but just does a "check" to see if the menus are enabled, and only shows them if they are):

``` php
<?php if ($primary_links): ?>
  <div id="primary">
    <?php print theme('links', $primary_links); ?>
  </div> <!-- /#primary -->
<?php endif; ?>

<?php if ($secondary_links): ?>
  <div id="secondary">
    <?php print theme('links', $secondary_links); ?>
  </div> <!-- /#secondary -->
<?php endif; ?>
```

**For Drupal 7:**

Primary and secondary links are now "main" and "secondary" menu.

``` php
<div id="menu">
    <?php if (isset($secondary_menu)) { ?><?php print theme('links', $secondary_menu, array('class' => 'links', 'id' => 'subnavlist')); ?><?php } ?>
    <?php if (isset($main_menu)) { ?><?php print theme('links', $main_menu, array('class' => 'links', 'id' => 'navlist')) ?><?php } ?>
  </div>
```

Note: the above code might be wrong. Try this:

``` php
print theme('links__system_main_menu', array('links' => $main_menu, 'attributes' => array('id' => 'main-menu', 'class' => array('links', 'inline', 'clearfix'))));
```

One more method for D7 that seems to work:

``` php
<?php print drupal_render(menu_tree('main-menu')); ?>
```

For Drupal 7 you also need to enable the main menu and secondary menu features in your theme's info file:

``` php
features[] = main_menu
features[] = secondary_menu
```

## The main "dynamic" content of the page

At this point, you've added all of the "framework" of your site's layout which surrounds every page, and is generally similar or the same throughout the entire site. Now though, it's time to include the area where actual **Content** will be displayed in the template (different content depending on the page being viewed, of course).

Simply locate the spot in your template where the main content is to be displayed (usually the center of the page, after the header and between any sidebars), and paste the below code in that spot (if you'd like to re-order things feel free, but otherwise you can simply paste this as-is):

``` php
<?php print $breadcrumb; ?>
<?php if ($mission): ?><div id="mission"><?php print $mission; ?></div><?php endif; ?>

<div id="content">
<?php if ($title): ?><h1 class="title"><?php print $title; ?></h1><?php endif; ?>
<?php if ($tabs): ?><div class="tabs"><?php print $tabs; ?></div><?php endif; ?>
<?php if ($show_messages): print $messages; endif; ?>
<?php print $help; ?>

<?php print $content; ?>
</div>
```

**For Drupal 7:**

``` php
<?php if ($breadcrumb || $title|| $messages || $tabs || $action_links): ?>
<div id="content-header">

            <?php print $breadcrumb; ?>

            <?php if ($page['highlight']): ?>
              <div id="highlight"><?php print render($page['highlight']) ?></div>
            <?php endif; ?>

            <?php if ($title): ?>
              <h1 class="title"><?php print $title; ?></h1>
            <?php endif; ?>

            <?php print $messages; ?>
            <?php print render($page['help']); ?>

            <?php if ($tabs): ?>
              <div class="tabs"><?php print render($tabs); ?></div>
            <?php endif; ?>

            <?php if ($action_links): ?>
              <ul class="action-links"><?php print render($action_links); ?></ul>
            <?php endif; ?>
            
          </div> <!-- /#content-header -->
        <?php endif; ?>

        <div id="content-area">
          <?php print render($page['content']) ?>
        </div>
```

## Footer: Add footer and footer message

To add a footer region and the footer message you have set in the administration backend you can use:

``` php
<?php if ($footer_message || $footer) : ?>
<div id="footer-message">
    <?php print $footer_message . $footer;?>
</div>
<?php endif; ?>
```

**For Drupal 7:**

``` php
<?php if ($page['footer']): ?>
    <div id="footer">
      <?php print render($page['footer']); ?>
    </div> <!-- /footer -->
  <?php endif; ?>
```

## Add a final tag at the bottom of your theme

Paste the following at the end of your *page.tpl.php* file. You *must* have this tag at the bottom, which will dynamically include any scripts that need to appear at the bottom of the page, as well as close up any loose ends and tags that might have been left open:

``` php
<?php print $closure; ?>
</body>
</html>
```

**For Drupal 7:**  
Good news! You don't need to worry about adding this tag to your D7 theme. It's all been taken care of.

## For Drupal 6 and 7: Create a YourThemeName.info file

Lastly, in Drupal 6 and 7, the one final element is to create a *YourThemeName.info* file (where *YourThemeName* is the name of your theme, with no spaces). Simply make a blank file and paste the following code into it, customize it with the appropriate name/description, and save it in the same directory along with the rest of your theme's template files:

``` php
name = YourThemeName
description = Description of YourTheme
core = 6.x
engine = phptemplate
stylesheets[all][] = style.css
regions[left] = Left sidebar
regions[right] = Right sidebar
regions[content] = Content
regions[header] = Header
regions[footer] = Footer
```

**For Drupal 7:**

``` php
name = System
description = Handles general site configuration for administrators.
package = Core
version = VERSION
core = 7.x
stylesheets[all][] = styles.css
regions[page_top] = Page top
regions[header] = Header
regions[highlight] = Highlight
regions[help] = Help
regions[content] = Content
regions[sidebar_first] = First sidebar
regions[sidebar_second] = Second sidebar
regions[footer] = Footer
regions[page_bottom] = Page bottom
```

I think the page_top and page_bottom regions are required by the default html.tpl.php, so leave them in there.

In Drupal 7, regions are printed out a bit differently, as noted above, but here are some examples:

``` php
<?php if ($page['header']): ?>
      <div id="header-region">
        <?php print render($page['header']); ?>
      </div>
<?php endif; ?>

...

<?php if ($page['highlight']): ?>
              <div id="highlight"><?php print render($page['highlight']) ?></div>
<?php endif; ?>

...

<?php print render($page['sidebar_first']); ?>

...

etc.
```

The "regions" portion after *style.css* includes all of Drupal's "standard" regions, and is recommended so that you can easily remove regions you don't want to use, or add custom regions. If you want to add custom regions, you must manually include any of the default ones you wish to keep as well or the defaults will disappear from your theme (simply copy/paste them from this page or another theme). If you want to add a custom region, simply copy one of the *region* lines and rename it.

**That's all - Paste the above bits of code into ANY site layout or template, and you have a basic, functional Drupal theme.**

## Learning more about Drupal theming

There are quite a few more elements you could use in your theme if you want to. Here are a number of excellent resources for learning the more detailed aspects of theming in Drupal:

- [Anatomy of a Drupal theme](http://drupal.org/node/171194)
- Full listing of available [Drupal 5 theme variables](http://drupal.org/node/11812) to choose from for page.tpl.php.
- Full listing of available [Drupal 6 theme variables](http://api.drupal.org/api/file/modules/system/page.tpl.php/6) to choose from for page.tpl.php.
- [Drupal theming for designers](http://neemtree.com.au/drupal-theming-designers) - this is a fantastic article, including screenshots and diagrams to help you clearly understand how Drupal's theming system works.
- [Drupal 7 Theme Guide](https://www.drupal.org/docs/7/theming), [Drupal 8 Theme Guide](https://www.drupal.org/docs/8/theming) - Official theming guides on Drupal.org

## Framework / Base / Starter themes

There are a variety of *Framework* themes (also known as *Base* or *Starter* themes), the purpose of which is to serve as a "blank slate" Drupal theme which you can build your own custom theme on top of. Many of these themes are stripped of all unnecessary styling so that they are just the core of a layout, paired with all the basic *tpl.php* template files for Drupal without any special customizations. Many also include a variety of helpful adjustments in their template.php files to add in commonly sought fixes and tweaks, so you'll have them before you even realize you need them. Several also add "extra" functionality that does not come by default in Drupal.

You can use these themes as a clean and simple basis for your own custom theme, or if you prefer, study them (and copy/paste from them) to see how to get Drupal's functionality into your own completely custom theme from scratch. Since these themes are clean and very lightly styled, it will be easier to work with versus other themes that are already highly customized.

Here is a list of many framework themes (though there may be more):

- [Adaptive Theme](http://drupal.org/project/adaptivetheme)
- [Advanced Theme Construction Kit](http://drupal.org/project/atck)
- [Basic](http://drupal.org/project/basic)
- [beginningW2](http://drupal.org/project/beginningW2)
- [Blueprint](http://drupal.org/project/blueprint)
- [Bootstrap](http://drupal.org/project/bootstrap)
- [Circle](http://drupal.org/project/circle)
- [Clean](http://drupal.org/project/clean)
- [Framework](http://drupal.org/project/framework)
- [Fusion](http://drupal.org/project/fusion)
- [Genesis](http://drupal.org/project/genesis)
- [Zen](http://drupal.org/project/zen)

**Additional note:**

When converting an existing webpage that uses HTML references to conventional images, the ` <img src="myimage.jpg"/> ` references must be changed to avoid Drupal's tendency to append "node/" to the front of relative paths.

Without any change, the new theme would change a ` <img src="myimage.jpg"/> ` reference into a ` <img src="node/myimage.jpg"/> ` reference.

Copy all of your original template's images into an images folder within the new theme's folder, and add the code `<?php print $base_path ?>` to the front of the path to eliminate the "node/" appendage.

So an original HTML reference in the page being converted ` <img src="myimage.jpg"/> ` would now become ` <img src="<?php print base_path() . path_to_theme(); ?>/images/myimage.jpg"/> ` where /images/ is a folder that you have created in the new theme for your new theme's images.

Thanks to idWorld for this solution
