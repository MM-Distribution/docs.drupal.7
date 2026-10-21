---
title: "Providing a way to skip navigation"
source_url: "https://www.drupal.org/docs/7/creating-accessible-themes/providing-a-way-to-skip-navigation"
page_type: page
last_updated: "Last updated on 28 December 2017"
published: "2009-05-20T12:14:19+00:00"
modified: "2017-12-28T08:19:30+00:00"
breadcrumb: ["Drupal 7", "Theming Drupal 7", "Creating accessible themes"]
fetched: "2026-10-21T08:26:09Z"
raw: "raw/docs/7/creating-accessible-themes/providing-a-way-to-skip-navigation.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Providing a way to skip navigation

Skip navigation links are one of the easiest ways to quickly improve the accessibility of your site. Skip links allow site visitors to jump or "skip" over repetitive page elements and are most useful to users confined to using their keyboard for navigating web pages.

There are a couple of important points to know when implementing skip navigation:

- Skip links should be the first thing on the page, right below the body element.
- You can use more than one.
- Do not use `display: none` to hide the link.
- Use the pseudo :focus and :active classes to highlight links for tabbed navigation.

## How to code skip navigation

Depending on your site you will need to consider which method is best suited.

For example, some sites will not show elements such as menus and search forms on every page, therefore you do not want redundant skip links to be included in those pages. If your site does this you will need to consider one of the more advanced techniques detailed further on in this article under *Dynamic Skip Links*.

If you just want to include one "Skip to main content," link then a simple static link will do the job.

### Static skip links

Skip links are really just [named anchor links](http://www.w3schools.com/HTML/html_links.asp). There are two parts to a named anchor.

1.  A normal link that uses the `href` attribute with the `#` (hash) symbol.
2.  A hidden anchor that uses the `name` attribute.

The code examples use Drupal's [t() function](http://api.drupal.org/api/function/t) to allow for translation of the link text.

Note that the `name` attribute is the same as the `href` attribute, only without the \# (hash) symbol:

Place the following code in your page.tpl.php file (html.tpl.php file in Drupal 7).  
This is the actual link. Place this at the top of your template file, just below the body element:

``` php
<div id="skip-nav">
  <a href="#main-content"><?php print t('Skip to main content'); ?></a>
</div>
```

Next, place the hidden anchor where you want the skip link to jump to. This is usually to the first H1 heading on the page (being the main heading for the page's content):

``` php
<a name="main-content" tabindex="-1"></a>
<h1>Title</h1>
```

Note the `tabindex="-1"` attribute - this is needed to make the skip-link work in WebKit-based browsers such as Chrome.

You can use more than one link, for example, if you want to add skip links to the navigation menus or the search form:

``` php
<ul id="skip-nav">
  <li><a href="#main-content"><?php print t('Skip to main content'); ?></a></li>
  <li><a href="#nav"><?php print t('Skip to navigation'); ?></a></li>
  <li><a href="#search"><?php print t('Skip to search'); ?></a></li>
</ul>

<a name="main-content" tabindex="-1"></a>
<a name="nav" tabindex="-1"></a>
<a name="search" tabindex="-1"></a>
```

### Dynamic skip links

A more sophisticated approach is to use PHP to conditionally show skip links depending on what elements are showing in your page. For example, if your main navigation is at the bottom of the source order you may want to include a "Skip to navigation" link, however if that navigation does not show on every page, then you do not want to include a link that does nothing and potentially confuses users.

In this example we are going to use conditional statements to show "Skip to navigation" and "Skip to search". The dynamic skip links will only show if their respective elements (primary menu or search box) are enabled. We'll also include a static "Skip to main content" link for completeness.

**Tip:** Instead of using the `name` attribute, we will use the `id` attribute on the wrapper divs to link to. This is the more modern method and is supported by all major browsers.

Note that in Drupal 7 the [\$primary_links variable has been renamed to \$main_menu](/update/theme/6/7#menus). Additionally the [\$search_box variable has been removed from Drupal 7](/update/theme/6/7#search_box) and you will need to use \#search-block-form (the ID on the search blocks form).

This example is for Drupal 6.

``` php
// Conditionally print skip links:
<ul id="skip-nav">
  <!-- assumes id="main-content" on the content wrapper -->
  <li><a href="#main-content"><?php print t('Skip to main content'); ?></a></li>

  <?php if ($primary_links): ?>
    <!-- assumes id="nav" on the primary links wrapper -->
    <li><a href="#nav"><?php print t('Skip to navigation'); ?></a></li>
  <?php endif; ?>

  <?php if ($search_box): ?>
    <!-- assumes id="search-box" on the search box wrapper -->
    <li><a href="#search-box"><?php print t('Skip to search'); ?></a></li>
  <?php endif; ?>
</ul>
```

For these to work you must be sure the id attributes are included in the respective elements when they print. For example, the code in page.tpl.php would be along the lines of:

``` php
<?php if ($primary_links): ?>
  <div id="nav">
     // print primary link here...
  </div>
<?php endif; ?>

<?php if ($search_box): ?>
  <div id="search-box">
    <?php print $search_box; ?>
  </div>
<?php endif; ?>

<div id="main-content">
  // main content goes here...
</div>
```

If you would like to study a theme that implements conditional skip navigation links, see the [Flexible](/project/flexible) theme.

## Hiding skip navigation

See also: [Accessible Techniques for Hiding Content](/update/theme/6/7#element-hidden).

**Many sites prefer to hide the skip links from normal view. I would encourage you not to. Skip navigation is not just for screen reader users but also for those who cannot use a mouse for navigation.**

Many disabled people can only use the keyboard and are thus forced to use repetitive tab keystrokes to navigate your pages. Skip links can help these visitors by allowing them to jump over repetitive page elements.

If you really must hide the skip links you can either:

- Hide it completely
- Hide it until it comes into focus (when the user tabs onto it)

### Hiding the skip navigation completely

**Never use `display: none` in your CSS to hide skip links.** This will hide it from screen readers!

There are at least two accessibility friendly methods of hiding content—setting a height of 0 and hiding any overflow, and the other is to position the content off the screen using position absolute.

You can include either of the following classes in your theme's CSS file and use them whenever you need an accessible way to hide content:

``` php
.invisible {
  height: 0;
  overflow: hidden;
}

.offscreen {
  position: absolute;
  left: -10000px;
  top: auto;
  width: 1px;
  height: 1px;
  overflow:hidden;
}

// For example, in the HTML you would include the class like this:
<div id="skip-nav" class="invisible">
  <a href="#main-content"><?php print t('Skip to main content'); ?></a>
</div>
```

Note that using the alternative technique of `position: absolute; top: -1000px;` may cause the browser to scroll unexpectedly when the link comes into focus.

### Hide skip links until they come into focus

This is the best method, because it preserves the focus for sighted keyboard users.

You can achieve this by simple making the skip links the same color as the background, and then adding :focus and :active styles, so when the user tabs to the link it becomes highlighted. We need to use :active to support Internet Explorer 7. Note that :focus styles are not supported by all browsers.

For example, let's imagine the background is black. We can set styles to reveal the link using the [pseudo :focus class](http://www.w3schools.com/CSS/pr_pseudo_focus.asp).

``` php
.reveal a:link {
  color: black;
}

.reveal a:active,
.reveal a:focus {
  background: yellow;
}

// For example, in the HTML you would include the class like this:
<div id="skip-nav" class="reveal">
  <a href="#main-content"><?php print t('Skip to main content'); ?></a>
</div>
```

See [The Web Standards Project](http://www.webstandards.org/) website for an example of using :focus to reveal skip navigation links.
