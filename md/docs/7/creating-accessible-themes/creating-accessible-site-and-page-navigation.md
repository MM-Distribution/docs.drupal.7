---
title: "Creating accessible site and page navigation"
source_url: "https://www.drupal.org/docs/7/creating-accessible-themes/creating-accessible-site-and-page-navigation"
page_type: page
last_updated: "Last updated on 8 September 2016"
published: "2009-05-16T14:53:49+00:00"
modified: "2016-09-08T13:24:12+00:00"
breadcrumb: ["Drupal 7", "Theming Drupal 7", "Creating accessible themes"]
fetched: "2026-10-21T08:23:45Z"
raw: "raw/docs/7/creating-accessible-themes/creating-accessible-site-and-page-navigation.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Creating accessible site and page navigation

This page provides an overview of best practices for making page and site navigation more accessible.

## Content

- [Skip links](#skip-links)
- [Headings for navigation](#headings-for-navigation)
- [Anchor links](#anchor-links)
- [List markup for menus](#list-markup-for-menus)
- [Meaningful link text](#meaningful-link-text)
- [Non-traditional navigation devices](#keyboard)

## Skip links

Skip links or "Skip navigation" are links that allow users to jump or "skip" over page elements, and are one of the most basic and useful tweaks for increasing the usability of your page by [screen-readers](http://en.wikipedia.org/wiki/Screen_readers) and other [assistive technologies (AT)](http://en.wikipedia.org/wiki/Assistive_technology#Software).

These links allow users to skip directly to the main content of the page without having to tab through or listen to repetitive page elements such as the site name, navigation menus and so on. Skip links should be placed at the top of the page so they are first in the tab order, allowing users who are restricted to using the tab key for navigation to access the skip links immediately.

Your site can have multiple skip links. Depending on the structure or content of your pages you may want to include several links such as "Skip to main content", "Skip to navigation", "Skip to search" and so on. Additional skip links can also be embedded anywhere on the page.

You should also incorporate `:focus` and `:active` styles to show the link when users tab the skip link into focus.

**Tutorial:** [Learn how to include Skip navigation links in page.tpl.php](/node/467976).

## Headings for page navigation

Headings allow people who use screen readers or other forms of assistive technology to skim the structure of a page and navigate to or skip over sections.

**Further reading:** [Using Headings to Improve Accessibility](/node/561750)

## Anchor links

Anchor links allow users to jump to sections within the web page.

For example on this page there is a jump menu that allows you to jump directly to sections:

``` php
<ul>
  <li><a href="#skip-links">Skip Links</a></li>
  <li><a href="#headings-for-navigation">Headings for Navigation</a></li>
  <li><a href="#anchor-links">Anchor Links</a></li>
  <li><a href="#list-markup-for-menus">List Markup for Menus</a></li>
  <li><a href="#meaningful-link-text">Meaningful Link Text</a></li>
  <li><a href="#keyboard">Non-Traditional Navigation Devices</a></li>
</ul>
```

The markup and techniques used are the same as for skip links. You can view the tutorial on [how to include skip links](/node/467976) as a guide for building jump menus with anchor links.

## List markup for menus

Many screen readers and other assistive technologies interpret lists of links as navigation menus. Drupal's menu system uses lists by default, but if you are writing menu code manually or customizing a menu, lists are still the best choice.

Menus can use the ARIA landmark of [`role="navigation"`](http://www.w3.org/TR/wai-aria/roles#navigation) to help screen readers convey the purpose of the list to people who use them.

Not all screen readers recognize ARIA tags, just as not all browsers support HTML5 or CSS3. To help people who use older assistive technologies, menu lists should be preceded by an `h2` label.

## Meaningful link text

It is important when creating a link to be as descriptive as possible about what it is you are linking to and why.

Examples:  
<img src="/misc/watchdog-ok.png" title="Good link text" data-align="absbottom" alt="Yes" /> **Good:** [Download the April 2012 report](#)  
<img src="/misc/watchdog-error.png" title="Please avoid this style" data-align="absbottom" alt="No" /> **Bad:** [Click here](#) to download the report

Many links are automatically generated. For example, the "read more", "comment", "email to friend" and "print friendly" links that are associated with each node. When different links have identical text but go to different URLs, it can be difficult for people using screen readers to quickly understand the differences. There are two general approaches to solving this problem:

- Be sure that context makes the destination of the links clear. In other words, if the title of a node is an H3 and only one "Read more" link occurs between it and the next H3, then the context has made it clear that the target of that link will have more information about the current node.
- If context doesn't make the destination of each link clear, add at least a sufficient short title of the destination page to the link text. For example, instead of "Read more," make the link say "Read more about 'Article example ABCD'". To avoid adding visual clutter to the page, you can hide this additional text so that it is visible to screen readers only.  
    
  **Drupal 7**  
  `<a href="#">Read more<span class="element-invisible"> about @title</span></a>.`  
  **Drupal 8**  
  `<a href="#">Read more<span class="visually-hidden"> about @title</span></a>.`

## Non-traditional navigation devices

Not everyone uses a keyboard and a mouse. People with mobility disabilities may be using solely the tab key to move through your site.

Navigating your site without a mouse is a good test for a theme. WebAIM has written an article on [Keyboard Accessibility](http://www.webaim.org/techniques/keyboard/) that provides more details on how to ensure that all of your content can be accessed with the keyboard alone.
