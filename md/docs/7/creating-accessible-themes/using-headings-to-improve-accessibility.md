---
title: "Using headings to improve accessibility"
source_url: "https://www.drupal.org/docs/7/creating-accessible-themes/using-headings-to-improve-accessibility"
page_type: page
last_updated: "Last updated on 8 September 2016"
published: "2009-08-28T00:13:22+00:00"
modified: "2016-09-08T13:24:09+00:00"
breadcrumb: ["Drupal 7", "Theming Drupal 7", "Creating accessible themes"]
fetched: "2026-10-21T08:26:55Z"
raw: "raw/docs/7/creating-accessible-themes/using-headings-to-improve-accessibility.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Using headings to improve accessibility

Headings allow screen-reader and assistive technology users to skim the structure of a page and navigate to or skip over sections.

Use headings for:

- The structure of page content
- Sections and sub-sections of an article
- Navigation menus
- Breadcrumbs
- Any other consistent sections that users may want to find or skip

## Best practices

There are a few simple rules to follow when using headings:

### Every page should have an `h1` heading

Without an h1 the user has no simple way to learn what the page is about. In most Drupal themes, the page.tpl.php \$title variable is wrapped in h1 tags. The \$title variable outputs the main title for the page. For example, on this page the title is "Using headings to improve accessibility".

Some pages — for example, the default Drupal front page — do not have a title. On the front page it is an accepted practice to wrap the site name in the h1 tag.

### Headings must be properly nested

Heading levels must not be skipped. For example, do not jump directly from h1 to h3.

### Headings are for structure, not formatting

Headings should be used to divide content into meaningful sections, not to format text. Your h2 styling may be italic and green, but that does not mean that anytime you want italic green text you should make the text an h2. Rather, the headings (no matter what their styling looks like) should be used to designate content structure.

## Hiding headings

Sometimes the role of a feature is perfectly clear to people who can see the page design, but difficult or impossible to discern if you can't see the design. When this happens, you might want to add a heading to label that feature but make the heading invisible.

- The accessible way to make a heading invisible is to use CSS: `class="element-invisible"`. The heading will not appear in the displayed page, but screen readers and other forms of assistive technology will recognize the heading and make it available to their users.
- Don't use `display:none`. Although this coding will make the heading invisible, it also makes the heading unavailable to assistive technology — so nobody will find it, regardless of how they try to access the content.

For more information, read [Accessible Techniques for Hiding Content](/node/472572).

## Further reading about headings

- [Watch a person who uses a screen reader navigate a Web page with headings](http://www.youtube.com/watch?v=AmUPhEVWu_E)
- [Use of h2 headings above the navigation menu preceding the h1](http://www.w3.org/TR/WCAG-TECHS/H42.html)
- [Use of headings in order (h1, h2, h3) without skipping levels](http://www.w3.org/TR/WCAG-TECHS/H69.html)
- [Importance of headings for screen reader users](http://www.raymondselda.com/importance-of-html-headings-for-accessibility/)
