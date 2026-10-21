---
title: "Supporting \"right to left\" (RTL) languages"
source_url: "https://www.drupal.org/docs/7/theming/working-with-css/supporting-right-to-left-rtl-languages"
page_type: page
last_updated: "Last updated on 1 June 2022"
published: "2008-02-17T06:42:22+00:00"
modified: "2022-06-01T16:44:22+00:00"
breadcrumb: ["Drupal 7", "Theming Drupal 7", "Working with CSS"]
fetched: "2026-10-21T08:16:16Z"
raw: "raw/docs/7/theming/working-with-css/supporting-right-to-left-rtl-languages.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Supporting "right to left" (RTL) languages

Adding support for RTL *(Right to Left)* languages involves overriding the lateral styles through cascades and naming the file based on the style sheet it is paired to. The inclusion of the RTL style sheet is automated. The inclusion of the file depends on the language settings set for the site.

For example, in the core theme Garland, "style.css" is the main style sheet. It also includes "style-rtl.css" for right to left languages like Arabic, Hebrew or Persian. The inclusion of the two styles always loads with the main style first and the RTL style second. This allows cascading of all the rulesets within the two files without having to worry about specificity in the selectors used in the RTL style.

There is a coding standard to keep the rules organized. Rules that are dependent on the lateral positioning or dimensions should be commented with `/* LTR */` indicating that the property is specific to a left to right layout. This includes floats, margins, padding, etc. Inline text should flow automatically as long as the theme sets the language direction of the document through the "page.tpl.php" template.

*Example base style:*

``` php
ul.primary-links {
  margin-top: 1em;
  padding: 0 1em 0 0; /* LTR */
  float: left; /* LTR */
  position: relative;
}
```

*Corresponding RTL style:*

``` php
ul.primary-links {
  padding: 0 0 0 1em;
  float: right;
}
```

While working with the main CSS file, this makes it easier to spot where changes may be needed in the RTL style.

*Note that if your theme [overrides a module style](/node/171209#styles-override-module), the associated RTL style will be omitted unless it is present in your theme.*
