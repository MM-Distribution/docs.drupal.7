---
title: "Standard Drupal core styles and classes"
source_url: "https://www.drupal.org/docs/7/theming/working-with-css/standard-drupal-core-styles-and-classes"
page_type: page
last_updated: "Last updated on 16 September 2016"
published: "2009-03-02T11:08:52+00:00"
modified: "2016-09-16T00:44:05+00:00"
breadcrumb: ["Drupal 7", "Theming Drupal 7", "Working with CSS"]
fetched: "2026-10-21T08:15:45Z"
raw: "raw/docs/7/theming/working-with-css/standard-drupal-core-styles-and-classes.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Standard Drupal core styles and classes

Drupal core takes a modular approach to CSS classes for standard page elements. A number of classes occur throughout a Drupal site. This list is meant as a quick crib sheet for remembering which classes mean what and occur where.

Note: themes you download may alter these classes, and add further ones.

### Page elements

.menu

All menu trees get this class, such as the navigation menu.

.block

All blocks. See <http://drupal.org/node/104319> for more on styling blocks.

.links

Lists of links, including Primary and Secondary links in the page header, and also node links and taxonomy terms (see below).

.nowrap (D7)

The role of this class is to prevent text wrapping.

.element-hidden (D7) or .hidden (D8)

The role of this class is to hide elements from all users (both visually and screen-readers). This class should be used for elements which should not be immediately displayed to any user. An example would be a collapsible fieldset that will be expanded with a click from a user. The effect of this class can be toggled with the jQuery show() and hide() functions.

.element-invisible (D7) or .visually-hidden (D8)

The role of this class is to hide elements visually, but keep them available for screen-readers. This class should be used for information required for screen-reader users to understand and use the site, where visual display is undesirable. Information provided in this manner should be kept concise, to avoid unnecessary burden on the user. An example would be the title of a menu.

.element-invisible.element-focusable (D7) or .visually-hidden.focusable (D8)

The `element-focusable` (D7) or `focusable` (D8) class extends the `element-invisible` (D7) or `visually-hidden` (D8) class to allow the element to be focusable when navigated to via the keyboard. An example would be the "Skip to content" and "Skip to menu" links at the top of most themes.

.container-inline (D7)

Inline items inside the parent element having specified class.

.invisible (D8)

The role of this class is to hide elements from all users but maintain the visual layout (i.e.: a blank space where the element would be if visible).

### Node elements

.node

A wrapper div around all of a node, including its title.

.node-title

The title of the node.

.content

The body of the node. This will include additions other modules make, such as uploaded files or CCK fields.

.links

Applied to any UL that is a list of links, including Primary and Secondary links in the page header, and also node links and taxonomy terms (see below). Node links however get the .links class on their enclosing DIV.

.terms

Taxonomy terms, which also get .links and .inline.

.inline

This is a system class for styling UL items into a horizontal line.

.feed-icon

RSS feed icons, usually at the foot of the page content area.

### Core Block IDs

See [Core Block CSS IDs](http://drupal.org/node/778884) documentation.
