---
title: "Hide content properly"
source_url: "https://www.drupal.org/docs/7/creating-accessible-themes/hide-content-properly"
page_type: page
last_updated: "Last updated on 20 December 2017"
published: "2009-05-25T22:08:27+00:00"
modified: "2017-12-20T15:39:38+00:00"
breadcrumb: ["Drupal 7", "Theming Drupal 7", "Creating accessible themes"]
fetched: "2026-10-21T08:24:32Z"
raw: "raw/docs/7/creating-accessible-themes/hide-content-properly.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Hide content properly

Not all techniques for hiding content are appropriate for users with screen readers or other adaptive technologies. This page covers major techniques for hiding content for all users and users with screen readers.

## Making content invisible (visually-hidden)

If an element on the page:

- is an interactive element but needs to be made invisible so it can be themed (e.g.: a link, checkbox, radio-button or form control with custom styles),
- is a heading or label for something whose purpose is visually-apparent (and therefore, the heading/label does not need to be shown to sighted users; e.g.: a section label or a form-element label), or,
- in general, shouldn't be visible to sighted users but should be visible to screen-reader users,

... then you should make it invisible (visually-hidden).

You can do this by:

- giving the element the `element-invisible` class (D7) or the `visually-hidden` class (D8),

- using CSS to position it outside the visible area of the page,

- (D8 only) if it is a field label in an entity sub-type, set it's label display to "- Visually Hidden -" on the *Manage display* page for that entity sub-type, or,

- using the CSS  

  ``` php
  position: absolute !important;
  clip: rect(1px, 1px, 1px, 1px);
  overflow: hidden;
  height: 1px;
  width: 1px;
  word-wrap: normal;
  ```

  on the element.

Example:  
Hiding the title of the error, warning and status messages.

Reasoning:  
In most themes, the status messages are displayed prominently in a colored box so that they are eye-catching for sighted users, but, to conform with [WCAG 2.0 section 1.3.3](http://www.w3.org/TR/WCAG20/#content-structure-separation), understanding and operating content should not rely solely on sensory characteristics of components such as shape, size, visual location, or orientation.

Without a title to indicate what the status messages are, they might be confusing to screen-reader users.

Most screen-readers can skip through the page using headings on the page. Giving the messages a header will make the messages easier to find.

## Making content invisible, until someone navigates to it using the keyboard

If an element on the page:

- is a link to help users jump to the main content or main navigation,
- is an alternative to other elements which can only be used with a mouse, or,
- in general, shouldn't be visible to sighted users unless they are using a keyboard to navigate the page,

... then you should make it invisible, until someone navigates to it using the keyboard.

You can do this by:

- giving the element BOTH the `element-invisible` and `element-focusable` classes (D7) or BOTH the `visually-hidden` and `focusable` classes (D8), or,

- using the CSS  

  ``` php
  css_selector_for_my_element {
    position: absolute !important;
    clip: rect(1px, 1px, 1px, 1px);
    overflow: hidden;
    height: 1px;
    width: 1px;
    word-wrap: normal;
  }
  css_selector_for_my_element:active,
  css_selector_for_my_element:focus {
    position: static !important;
    clip: auto;
    overflow: visible;
    height: auto;
    width: auto;
  }
  ```

  Where `css_selector_for_my_element` is the selector for the element you want to make invisible until someone navigates to it using the keyboard.

Example:  
The "Skip to main content" link at the top of every page in Bartik & Seven.

Reasoning:  
Keyboard-only and screen-reader users want a way to quickly jump to the main content of the page.

To conform to [WCAG 2.0 section 2.4.1](http://www.w3.org/TR/WCAG20/#navigation-mechanisms-skip) standards, you must provide a way to skip blocks of content that are repeated on multiple pages.

## Completely hide content for all users

If an element on the page:

- shouldn't be shown until a JavaScript event makes it visible,
- isn't relevant to sighted users or screen-reader users in the context,
- contains values that are read/written by JavaScript but should never be shown directly, or,
- in general, shouldn't be visible to sighted users or screen-reader users,

... then you should completely hide it for all users.

You can do this by:

- giving the element the `element-hidden` class (D7) or the `hidden` class (D8),
- if it is a field in an entity sub-type, set it's Format to "- Hidden -" on the *Manage display* page for that entity sub-type,
- if it is a field label in an entity sub-type, set it's label display to "- Hidden -" on the *Manage display* page for that entity sub-type, or,
- using the CSS `display: none;` on the element.

Example:  
Hiding the color module's preview area until JavaScript has run:

``` php
/* color.css (Drupal 7 and 8) */
#preview {
  display: none;
}
```

Reasoning:  
The preview doesn't work if JavaScript is not running, so it is of no use to anyone.

### Misuse

A common inappropriate use of "display:none" is to remove a form label or heading in order to change the *visual appearance* of a page. However, this will render the form element unusable to screen-reader users!

For example, if you remove a form label with "display: none," a screen-reader user might tell you, "I have a required text field to type into but I have no idea what the field is for." In this situation, making the content invisible (visually-hidden) would be more appropriate.

## Making content invisible to screen readers

If an element on the page:

- has an accessible alternative and would be confusing by itself, or,
- in general, should only be visible to sighted users,

... then you should make it invisible to screen readers.

You can do this by:

- giving the element the attribute `aria-hidden="true"`

Example:  
A control to remove a search filter shows an "x" to sighted users only AND provides accessible, visually-hidden instructions for screen-reader users:

``` php
Currently filtering by: <a href="...">Module <span class="element-invisible">Click to remove this filter.</span> <span aria-hidden="true">x</span></a>
```

Reasoning:  
There is already accessible alternative text.

Hearing an "x" by itself, even after hearing the alternative text, would be confusing to screen-reader users.

### Misuse

Making content invisible to screen readers means that people using them cannot perceive or interact with it. To conform to [WCAG 2.0 section 1.1](http://www.w3.org/TR/WCAG20/#text-equiv), you **must** provide accessible, alternative content, otherwise people using assistive technology will not be able to use it.

## Further reading about invisible content

- [WebAIM Recommendations](http://www.webaim.org/techniques/css/invisiblecontent/)
- [display:none Problems for screen readers](http://juicystudio.com/article/screen-readers-display-none.php)
