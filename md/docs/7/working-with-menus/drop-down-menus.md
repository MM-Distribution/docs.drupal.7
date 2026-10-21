---
title: "Drop Down menus"
source_url: "https://www.drupal.org/docs/7/working-with-menus/drop-down-menus"
page_type: page
last_updated: "Last updated on 25 March 2022"
published: "2010-12-06T07:52:04+00:00"
modified: "2022-03-25T12:01:58+00:00"
breadcrumb: ["Drupal 7", "Working with menus in Drupal 7"]
fetched: "2026-10-21T07:20:08Z"
raw: "raw/docs/7/working-with-menus/drop-down-menus.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Drop Down menus

- [What is a drop down menu?](#whatisadropdownmenu)
- [Popular dropdown menus in Drupal](#populardropdownmenus)
- [Comparison of drop down menus](#comparisonofdropdownmenus)

## <span id="whatisadropdownmenu">What is a drop down menu?</span>

Drop down menus are one of the most common features in a website. Scripting allows you to add a menu bar with attached drop down menus to the top of your website which helps in website navigation.

How are they created?  
Web designers can create horizontal or vertical drop down navigation menus with the help of CSS. However, it should be noted that by using JavaScript, more interactive, responsive and flexible navigation bars can be created for any website.

What are the advantages of websites using a drop down menu?

1.  A drop down menu is useful because it reveals the contents of a website simply by placing the cursor over the main menu navigation bar. When this happens, the pages below the main sections appear dynamically and third tier pages are also revealed when one goes further down. It enables the visitor to click on any of these links and go straight to these pages.
2.  Drop down menus makes sure that navigating a website is extremely simple.
3.  The menu acts like a dynamic site map that provides navigation.
4.  Search engines can index the site using the menu structure and can then provide a structured search result

What are the different ways in which drop down menus can be created?  
It can be created using:

1.  HTML
2.  CSS
3.  DHTML
4.  jQuery
5.  JavaScript

How can a simple drop down navigation bar be created?  
A navigation bar is basically a list of links which is created using CSS and html. By using html, we create links using the "li" and "ul" /"ol" tags. Then, we remove the bullets, the margin and the padding using CSS (by setting value =0). If we want to create a vertical navigation bar, we just need to style the "a" element. If we are creating a horizontal navigation bar, we can create it using the inline or floating list items. However, for same sized links, we have to use a floating list item.

## <span id="populardropdownmenus">Popular drop down menus in Drupal:</span>

1.  [Mega Menu](http://drupal.org/project/megamenu)
2.  [Nice Menus](http://drupal.org/project/nice_menus)
3.  [Superfish Menu](http://drupal.org/project/superfish)

### Mega Menu

What are Mega menus?  
A Mega menu is basically a single drop-down that appears on when hovered upon and shows all the options in one large window which enables easy website navigation. Group options are also shown in related categories and uses icons or other graphics to help the user.  
The Drupal module is used to create a type of mega menu in Drupal leveraging both jQuery and the existing Drupal system.

Note: *this project is only pre - alpha (for drupal7) or beta (for drupal6) and is not yet to be used on production sites.*

How does it work?  
Mega menu takes all three levels of depth of a Drupal menu, and converts it into a categorized 3-level mega-drop down-style menu. It shows what that particular website is about at a glance.

What are the features of Mega menus?

1.  Single drop down appears down the hover.
2.  Shows all options in one large panel.
3.  Uses icons and illustrations to help and captivate the user.
4.  Division of various categories in a single panel.
5.  Most of all limited to zero scrolling required.
6.  Helps the web designer to express their artistic creativity.

What are the advantages of using a Mega menu?

1.  For bigger sites with many features, regular drop-down menus typically hide most of the user's options. Scrolling down for items in the regular drop down menus hides the initial options. Hence, a person can't visually compare all your choices and has to rely on short-term memory.
2.  Mega drop-downs show everything at a glance, so users can see rather than try to remember.
3.  Illustrations can indeed be worth a mouthful of words. Mega drop-downs make it easy to use icons and pictures when appropriate. Even if you use text alone, you have richer typography at your disposal (letting you differentiate link sizes according to their importance, for example).

### Nice Menus

What are Nice menus?  
It is a module created by the Drupal community which enables left/right drop down menus for navigations.

How does it work?  
It works with a combination of CSS and minimal JavaScript. They require CSS to get customized styling. However, it should be noted that version 2 uses the Superfish jQuery plug-in for all browsers, with an option to disable JavaScript. Menu blocks can be created in existing menus.

What are the features found in Nice menus?

1.  The ability to add and customize Nice menus functionality to unlimited menus using the included theme functions.
2.  Three styles/types of menus are currently possible: horizontal where the menus drop down; vertical where the menus fly to the left; vertical where menus fly to the right.
3.  The ability to configure the no. of Nice menu blocks. (Till 10 blocks)
4.  It is also possible to theme a menu as a Nice Menu directly by using the provided theme functions.

### Superfish Menu

What is Superfish?  
Superfish is a jQuery plug-in that enables the user to add styling options to the existing CSS drop down menu.

What is a Superfish menu?  
Superfish Menu is a Drupal module which integrates jQuery Superfish plug-in with Drupal menus. It is an enhanced menu with the jQuery plug-in that takes an existing pure CSS drop-down menu and adds many features without manually coding JavaScript. If Javascript is disabled in the browser it does not work.

How does it work?  
Superfish can be used to combine with a menu module to easily create and manipulate drop down menus.

What are the configuration options that Superfish can offer?  
The various configuration options that Superfish offers are shadows, arrows, vertical menu, horizontal menu, navigation bar menu, I-frame for IE6 use, fade in, slide in, fade and slide in, opacity, intelligent cursor handling, and other options.

What are the advantages of using Superfish menus?  
Since it is styled purely through CSS, it gives the web designer full control over how it appears while maintaining its necessary functions.

What are the extra features that the Superfish menu provides?

1.  Timed mouse out delay.
2.  Sub-menu animated reveals.
3.  Keyboard accessibility (tab key).
4.  Obligatory IE6 hover capability.
5.  Automatic use of hover intent plug- in if available.
6.  Automatic generation of arrows to indicate sub-menus.

### <span id="comparisonofdropdownmenus">Comparison of Nice Menu and Superfish Menu</span>

Here is a comparison of Nice Menu version 2.1 and pure Superfish version 1.6 made by the Drupal community.

|                                                |                                                               |                                          |
|------------------------------------------------|---------------------------------------------------------------|------------------------------------------|
| Features                                       | Nice Menus v2.1                                               | Superfish v1.6                           |
| Structure                                      | Nice Menus (including CSS, etc) + Superfish (just JavaScript) | Purely Superfish (with its own CSS, etc) |
| SF Delay                                       | User-Defined (site-wide)                                      | User-Defined (block specific)            |
| SF Animation Speed                             | User-defined (site-wide)                                      | User-defined (block-Specific)            |
| Built-in custom skins                          | No                                                            | Several                                  |
| Slide- in effect                               | On by default (site-wide)                                     | User-defined (block specific)            |
| Drop Shadows                                   | On by default (site-wide)                                     | User-defined (block specific)            |
| Auto Arrows                                    | On by default (site-wide)                                     | User-defined (block specific)            |
| B.G.I Frame                                    | On by default (site-wide)                                     | User-defined (block specific)            |
| Super Subs                                     | No                                                            | Yes (block-specific)                     |
| First\Last classes                             | On by default (site-wide)                                     | User-defined (block specific)            |
| Odd\Even classes                               | On by default (site-wide)                                     | User-defined (block specific)            |
| Item count classes                             | No                                                            | Yes (block-specific)                     |
| Custom classes                                 | No                                                            | Yes (block-specific)                     |
| link to custom CSS file                        | Theme settings (site-wide)                                    | Block settings (block specific)          |
| Html wrapper for links, link texts and main UL | No                                                            | Yes (block-specific)                     |

### Menus found in Drupal Themes

How can Superfish menu be added into your theme?  
The Superfish menu can be added into your theme by:

1.  Once a standard Drupal menu is built, select the expanded option and then disable the primary links. Once this is done, enable Superfish setting.
2.  Add menu block, thus making it a drop down menu.
3.  For further menu modifications, configure your Superfish plug-in. Use the Drupal.behaviors.(Respective theme)Superfish = function (context) {} function in your sub-theme to change the speed, arrows and drop shadows.

### List of themes that support and employ the use of Superfish menus:

1.  [Fusion](/project/fusion)
2.  [AdaptiveTheme](/project/adaptivetheme)
3.  [Pixture Reloaded](/project/pixture_reloaded)
4.  [Danland](/project/danland)
5.  [Corolla](/project/corolla)
6.  [Fusion Marina](/project/fusion_marina)
7.  [Likable Clean Theme](/project/likable)
8.  [Bluejems](/project/bluejems)
9.  [Xurxo](/project/xurxo)

### List of sites using Nice Menus:

[Sites Using Nice Menus](/node/448620)
