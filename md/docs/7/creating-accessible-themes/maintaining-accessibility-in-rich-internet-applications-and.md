---
title: "Maintaining accessibility in rich Internet applications and Javascript/Ajax features"
source_url: "https://www.drupal.org/docs/7/creating-accessible-themes/maintaining-accessibility-in-rich-internet-applications-and"
page_type: page
last_updated: "Last updated on 8 September 2016"
published: "2009-05-16T15:00:19+00:00"
modified: "2016-09-08T13:24:09+00:00"
breadcrumb: ["Drupal 7", "Theming Drupal 7", "Creating accessible themes"]
fetched: "2026-10-21T08:25:22Z"
raw: "raw/docs/7/creating-accessible-themes/maintaining-accessibility-in-rich-internet-applications-and.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Maintaining accessibility in rich Internet applications and Javascript/Ajax features

The following guidelines will help with building rich Internet applications

- **Build a solid base.** Design the base experience to be a great one before jumping into dynamic interactions. This ensures that the users who cannot access or use the rich experience do not feel deprived.
- **Be aware that screen readers parse JavaScript.** Many modern screen readers have some level of support for JavaScript and care should be taken to ensure that its use does not cause pages to become less accessible.
- **Be careful when implementing functionality that changes areas of the page without refreshing the page, such as AJAX.** Screen reader software works by taking a virtual copy of the page, which it then interrogates. If the page changes without a refresh (or some indication that the user should refresh their virtual copy) users may be unaware that content has changed. In Drupal 8, consider using the [`Drupal.announce()` function](https://www.drupal.org/node/2014521) to announce changes to screen readers.
- **Research best practice techniques before implementing rich interactions and functionality.** As this is a relatively new area, techniques are continually being developed and improved and support for rich interactions is increasing. The Paciello Group is doing great work in this area and documenting it at <http://www.paciellogroup.com/blog/>.
- **Understand the impact of the desired functionality.** It is better to exercise caution when considering the use of new techniques or functionality. If, following research, it is not possible to implement the desired functionality in an accessible manner, consider using an alternative until an accessible solution is found.

WebAIM articles on making [JavaScript](http://www.webaim.org/techniques/javascript/) and [Ajax](http://www.webaim.org/techniques/ajax/) accessible.
