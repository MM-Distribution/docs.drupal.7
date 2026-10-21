---
title: "Creating accessible structure and markup"
source_url: "https://www.drupal.org/docs/7/creating-accessible-themes/creating-accessible-structure-and-markup"
page_type: page
last_updated: "Last updated on 11 June 2019"
published: "2012-06-15T20:26:08+00:00"
modified: "2019-06-11T11:22:56+00:00"
breadcrumb: ["Drupal 7", "Theming Drupal 7", "Creating accessible themes"]
fetched: "2026-10-21T08:24:01Z"
raw: "raw/docs/7/creating-accessible-themes/creating-accessible-structure-and-markup.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Creating accessible structure and markup

This page provides information on accessibility issues with structure, markup, data tables and page navigation

## Structure and markup

- **Use appropriate markup.** Lists are lists, headings are headings, and quotations deserve appropriate markup, too. Paying careful attention to web standards automatically increases the accessibility of any page we create.
- **Avoid using structural markup for presentation.** The H1-H6 elements are for providing structure not altering text size, and blockquote elements are for distinguishing quotations, not indenting text.
- **Avoid using unconventional markup.** At best, unconventional markup can be confusing for users, at worst, it can make pages difficult or impossible to use. For example, don’t use form elements instead of lists for navigation, and don’t use links instead of buttons for form submission.
- **Use the `title` element effectively.** Putting the information in the form you’d use for a reverse breadcrumb trail (e.g., \[page\] - \[section\] - \[site name\]) places unique information first and means less repetitive reading for users.
- **Specify the natural language of the document.** This ensures that browsers display characters properly and screen readers use the correct pronunciation rules. For English in HTML add `lang="en"` to your `<html>` element. For XHTML1.0, change your `<html>` element to `<html xmlns="http://www.w3.org/1999/xhtml" lang="en" xml:lang="en">`. Language codes can be found at <http://www.loc.gov/standards/iso639-2/php/English_list.php>.
- **Specify any changes in the natural language.** If you change language midway through a page and don’t markup the change correctly, the screen reader will read the second language as if it was the first. The lang attribute can be added to any element. The span element can be used within a containing element or a div can be used if the change includes multiple elements. For example, `<p lang="fr">Bonjour</p>`, `<p><span lang="es">Hasta la vista</span>, baby</p>` or `<div lang="la"><p>Lorem ipsum...</p><p>Etiam in risus ipsum...</p></div>`.
- **Use lists for navigation.** This allows screen reader users to build a mental model of the size of the site/navigation without having to listen to and count each item in the menu.
- **Use the most appropriate source code order for the type of site.** Designing a page structure based on user needs allows us to provide a better experience for our users. Putting navigation before content works well for sites where users browse before reading, but putting the content first may be more appropriate for blogs and other content-rich sites where readers are more likely to read first and then browse for other content.
- **Use skip links to provide keyboard shortcuts to content or navigation.** Ideally, skip links should be visible by default, because they are especially useful to those who have mobility difficulties or do not use specialized accessibility software. However, having them appear when the links receive focus is acceptable, if they are placed sensibly. To be most useful, they should be kept to a minimum (no more than three) and be the first links in the source code order. The link text should ideally describe the destination, for example “Skip to main content” or “Skip to main navigation,” rather than “Skip navigation.”
- **Create a logical page structure.** Check the page without CSS. It should still have a logical structure and be easy to navigate and understand.
- **Use headings appropriately, including section headings if necessary.** `<h1>` is used for the main heading of each page (which is not always the site name). Any subheadings (including section headings) of `<h1>` are `<h2>`, and so on. Using this type of heading structure allows screen reader users to create a mental model of the page, quickly determine if it contains the information they seek, and then navigate directly to the section they want.
- **Write good link text.** Link text should contain all important information, be concise, be unique, and make sense when read out of context. “Terms and Conditions (PDF 30kb)” is good. “Click here” is not.
- **Do not repeat redundant information in title attributes.** Using the title attribute in a link can be a good way to communicate information about the link to assistive technology users. However, if the information in your title attribute presents the same information that is in the linked text, or does not accurately describe the link then remove it or change the text in the title attribute. **Attention:** The [W3C does not recommend the use of the title attribute](https://www.w3.org/TR/html5/dom.html#the-title-attribute) for accessibility.
- **Notify users of pop-ups and new windows.** In general, use of pop-ups and new windows should be avoided in favor of allowing users to choose the desired behavior. However, if the use of a pop-up or a new window is unavoidable, the user should be notified within the link text. This can be done by including the words “(new window)” or “(pop-up)” in the link text or inserting an appropriate icon and giving it appropriate alt text.
- **Avoid CAPTCHAs if at all possible.** If their use is unavoidable, provide an audio alternative (e.g., <http://recaptcha.net/>) and a mechanism for users to get timely support if they need it, for example, an e-mail address or telephone number.

## Data tables

- **Specify table headers.** Row and column headings should be marked up using the `<th>` element and `scope="row"` or `scope="col"` attributes as appropriate.
- **Associate headers with cells.** If more than one level of heading is required, give each header cell a unique ID (e.g., `<th id="id1">`) and use the headers attributes to explicitly associate the cell and its headers. Each heading ID should be referenced, in order, within the headers attribute, for example, `<td headers="id1 id2">`. This ensures that the headers are read out to screen reader users in the correct order.
- **Describe the purpose of the table.** Use the caption element to provide a visual description which concisely describes what information is being provided. For example, using “June 2009” for a calendar. Describe the structure of the data. Use the summary element to provide a concise description of the data structure of the table. Using the calendar example, the summary could be “Columns contain days of the week from left to right, starting on Sunday.”

## Orientation and way-finding

- **Provide focus states as well as hover states for links.** Ensure that any changes which happen on hover also occur on focus to help keyboard only users identify the focused element.
- **Identify the current location in navigation.** Using a different visual style to identify the current section or page within navigation can help users to quickly orient themselves within the site.
- **Do not remove the default browser focus outline.** The focus outline is vitally important to users who have mobility difficulties and navigate through the site without using a mouse. If the default focus outline seems insufficient, it can be enhanced using CSS.
- **Do not move links out of the viewport using CSS.** If links are moved offscreen, keyboard-only users can become disorientated as the focus indicator will disappear from view until the user has moved to a focusable element within the viewport.
- **Make links easy to identify.** Make links clear and easy to distinguish from emphasized or body text. Make clickable targets bigger. For example, using `display: block` within a navigation menu to allow users to click the area around the text or making clickable buttons or links larger. In addition to attracting more attention from all users, this particularly helps users who have impaired motor skills.
