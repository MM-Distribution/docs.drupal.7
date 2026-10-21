---
title: "Accessibility principles"
source_url: "https://www.drupal.org/docs/7/creating-accessible-themes/accessibility-principles"
page_type: page
last_updated: "Last updated on 12 December 2017"
published: "2009-05-17T11:23:08+00:00"
modified: "2017-12-12T01:48:01+00:00"
breadcrumb: ["Drupal 7", "Theming Drupal 7", "Creating accessible themes"]
fetched: "2026-10-21T08:22:59Z"
raw: "raw/docs/7/creating-accessible-themes/accessibility-principles.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Accessibility principles

This is a Drupal-centric version of Principles of Accessible Design, part of the [Introduction to Web Accessibility](http://www.webaim.org/intro/) by WebAIM.org.

- [All non-text content has alternative text](#alt-text)
- [All data tables have headings](#data-tables)
- [Users can complete and submit all forms](#forms)
- [Links make sense out of context](#link-text)
- [Media has captions and/or transcripts](#transcripts)
- [Non-HTML content is accessible](#non-html-content)
- [Users can skip repetitive elements on the page](#skip-nav)
- [Users can comprehend the page structure and purpose](#comprehend)
- [Meaning is not conveyed through color alone](#color)
- [Content is clearly written and easy to read](#writing)
- [JavaScript is accessible](#javascript)
- [Users can access content from various devices and browsers](#responsive)
- [The site complies with standards](#standards)

All non-text content has alternative text  
Alternative text provides a textual alternative to non-text content in web pages (most commonly images). It is especially helpful for people who are blind and rely on a screen reader to have the content of the website read to them, but is also very important for search engine optimization (SEO) purposes as it allows for more content to be meaningfully indexed.

- Provide a short, relevant description of all images that convey information using the `alt` attribute within the `img` tag. [WebAIM's Appropriate Use of Alternative Text](http://www.webaim.org/techniques/alttext/) explains how to use the `alt ` attribute in a variety of contexts.
- Images containing text are still being used when a non-standard typeface is required by a site design. This is fine provided the alt text exactly replicates the text on the image.
- Decorative images however should be given empty or null `alt` text (`alt=""`) so screen readers ignore these images.
- If a longer description of the non-text content would be helpful either include a link to the longer description near the non-text content or use a `longdesc` attribute (`<img alt="example" longdesc="URL">`) to provided additional information.
- Learn more about `alt` attribute usage in [Managing Images and Media for Accessibility](/node/464496).

<!-- -->

All data tables have headings  
Tables are used to organize and present tabular data such as financial results, calendars, etc. Data cells need to be associated explicitly with header cells so screen reader users have an easier time navigating and understanding the content of the data table.

- Describe complex data tables using the `summary` attribute in the `table` tag.
- Consider using the `caption` element to describe the content of data tables.
- Use `th` elements to tag columns or row headers; nest these headers in a `thead` tag.
- Associate data cells explicitly with their appropriate headers using the `headers` and `id` attributes.

<!-- -->

Users can complete and submit all forms  
Provide each form element (text field, checkbox, dropdown list, etc.) with a descriptive label that is explicitly associated with the form element so users understand what input is expected of them.

- Use the `label` tag and `for` attribute to structure the labels.
- Provide each form element with a unique name, using the `id` attribute.
- Make sure the values of the `for` and `id` attributes are the same, so that the association is clear.
- Allow the user to submit the form and to recover from errors, such as the failure to fill in all required fields, by making sure the information is also disclosed using only the keyboard or fully available to screen readers.
- Do not hide form labels using `display: none`, as it also hides the labels from screen readers. Use CSS off-screen positioning instead.
- Be aware when using [hook_form_alter](http://api.drupal.org/api/drupal/modules--system--system.api.php/function/hook_form_alter/7) and other techniques to modify forms that you are not reducing the accessibility of forms.

<!-- -->

Links make sense when taken out of context  
Every link should make sense if the link text is read by itself. Screen reader users may choose to read only the links on a web page. Certain links like "read more" or "click here" should therefore be avoided because those will not allow a user to understand where the links lead once they are taken out of their context.

- If such links need to be used, consider making them understandable out of context by completing them with significant complementary text that will then be positioned off-screen using CSS.
- Use [hook_link_alter](http://api.drupal.org/api/drupal/developer--hooks--core.php/function/hook_link_alter/6) to remove or modify Drupal's default "read more" link on node teasers.

<!-- -->

Media has captions and/or transcripts  
Videos and live audio should, at minimum, have captions and preferably a transcript. With archived audio, a transcription may be sufficient.

- Transcriptions add value to your web site. For example educational podcasts can be printed by students.
- See the [Lullabot Podcasts](http://www.lullabot.com/podcast). Note how they provide additional added value text content to podcast nodes.
- Learn more about media accessibility in [Managing Images and Media for Accessibility](/node/464496).

<!-- -->

Non-HTML content is accessible (including PDF files, Microsoft Word documents, PowerPoint presentations and Adobe Flash content).  
In addition to all of the other principles listed here, PDF documents and other non-HTML content must be as accessible as possible. If you cannot make it accessible, consider using HTML instead or, at the very least, provide an accessible alternative. PDF documents should be saved with the tagged format. A tagged PDF file looks the same, but it is almost always more accessible to a person using a screen reader. OpenOffice is an open source office suite that allows you to [create properly tagged PDF files](http://webaim.org/techniques/ooo/).

- Learn more about [PDF documents and accessibility](http://www.alistapart.com/articles/pdf_accessibility).

<!-- -->

Users can skip repetitive elements on the page  
Provide a mechanism that allows users to skip over navigation or other elements or blocks of information that repeat on every page. This is usually accomplished by providing a "Skip to Content", "Skip to Main Content", or "Skip Navigation" link at the very top of the page which jumps to the main content of the page.

- Create a hyperlink at the beginning of the page that points to an anchor at the very beginning of the page's main content.
- Ensure the main content section of the page begins with a first level heading (`h1`) so screen reader users can jump to the main content by selecting the `h1`.
- Learn more about [Skip navigation for web pages](http://drupal.org/node/464492#skip-links).

<!-- -->

Users can comprehend the page structure and purpose  
Users who use screen readers or who have sight limitations do not have the ability to glance at a page and comprehend its structure and purpose. This must be conveyed through the text on the page, in the order that the text is presented on the page.

Problems can arise, for instance, when a form field is given the initial focus on a page -- this should only be done if that form field is or enables the primary purpose of the page. For example, on a Search This Site page, giving focus to a Search Keywords field would probably be appropriate, because searching is the primary purpose of the page. But on a Modules List page, giving focus to a Filter Keywords field would be inappropriate, because filtering the module list is far from being the page's primary purpose.

<!-- -->

Meaning is not conveyed through color alone  
The use of color can enhance comprehension, but that information may not be available to a person who is colorblind and will be unavailable to screen reader users. Do not use color alone to convey information.

- Make sure that information conveyed through color is also conveyed in text so it can be picked up by screen readers as well.
- Refrain from only using color to present a hyperlink, as some users may not be able to perceive the color contrast with surrounding text.

<!-- -->

Content is clearly written and easy to read  
There are many ways to make your content easier to understand. Write clearly, use clear fonts, and use headings and lists appropriately.

- Learn more about [fonts and accessibility](http://www.webaim.org/techniques/fonts/).

<!-- -->

JavaScript is accessible  
Ensure that JavaScript event handlers are device independent (e.g., they do not require the use of a mouse) and make sure that your page does not rely on JavaScript to function.

- Join the [jQuery accessibility group](http://groups.google.com/group/jquery-a11y/about).

<!-- -->

Users can access content from various devices and browsers  
When we say that a site is "accessible," we usually mean that the site is navigable for and the content available to users with blindness, deafness, muscular disorders, etc. However, an accessible site is also one that users can access from both mobile and desktop devices and that functions properly on different web browsers.

- [Drupal's documentation for creating responsive sites](https://www.drupal.org/node/1322126)
- [browserling's free browser-compatibility tool](https://www.browserling.com/)

<!-- -->

The site complies with standards  
HTML compliant and accessible pages are more robust and provide better search engine optimization. Cascading Style Sheets (CSS) allow you to separate content from presentation. This provides more flexibility and accessibility of your content.

- [Web Accessibility Initiative (WAI)](http://www.w3.org/WAI/)
- [WASP Accessibility Task force](http://www.webstandards.org/action/atf)
- [Designing With Web Standards](http://www.zeldman.com/dwws/) by Jeffrey Zeldman
- [A Roadmap to Standards](http://www.mezzoblue.com/archives/2004/04/30/a_roadmap_to/) by Dave Shea
