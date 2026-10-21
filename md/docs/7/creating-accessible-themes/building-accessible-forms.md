---
title: "Building accessible forms"
source_url: "https://www.drupal.org/docs/7/creating-accessible-themes/building-accessible-forms"
page_type: page
last_updated: "Last updated on 12 December 2017"
published: "2012-06-15T19:44:37+00:00"
modified: "2017-12-12T01:43:58+00:00"
breadcrumb: ["Drupal 7", "Theming Drupal 7", "Creating accessible themes"]
fetched: "2026-10-21T08:23:15Z"
raw: "raw/docs/7/creating-accessible-themes/building-accessible-forms.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Building accessible forms

The following tips will improve the accessibility of your forms:

- **Place important information/instructions at the top of the form.** Providing instructions first reduces user error and provides a better user experience.
- **Always indicate required fields.** In addition, inform users at the beginning of the form how required fields will be indicated. The convention is to use a red asterisk, but this can also be provided by a small icon accompanied by alt text that says “required”.
- **Ensure all form fields have a label and explicitly associate it using the for attribute.** Explicit association allows screen readers to announce the correct label, and moves the focus to the associated element when the label text is clicked. If there is absolutely no room for a visible label, the label may be moved offscreen using `{position: absolute; top: -999em}` in CSS, or the title attribute used instead.
- **Place labels close to their associated element.** Too much white space between label and element can mean that screen magnification users cannot see the label along with the field, which may lead to increased errors when completing the form.
- **Include the required field indicator within the label element.** If this is placed after or below the form field, it may be missed by those who use screen reader or screen magnification software.
- **Place help text between the label and the form field.** If guidance is needed to enable users to complete the field correctly, it should be provided before the relevant field, not after.
- **Allow users to hide/show help text.** This allows users to control how much information they are presented with and cuts down on visual or auditory “clutter” for frequent users.
- **Group form controls and label them appropriately.** Use a fieldset with an appropriate legend to provide context for groups of radio buttons or checkboxes.
- **Write legend text with care.** Be aware when writing legend text that screen readers read the legend and label text for each item enclosed within the fieldset. Try to ensure that each label makes sense when read together with the legend, as well as on its own. A great example of this can be found at <http://uk.tv.yahoo.com/> where a fieldset legend of “Search” combines well with radio button labels of “the web”, “for images”, “for video”, and “for audio”.
- **Segment lengthy forms**. When working with lengthy forms, consider splitting them into multiple pages or using headings in addition to fieldsets with legends. In this case, headings can be worded slightly differently to the legend to minimize repetition and hidden offscreen using CSS.
- **Summarize errors at the top of the form.** This provides an overview of all action required to complete the form correctly. It is also beneficial to provide anchor links to fields which require attention. Highlight fields with errors clearly. This could be accomplished by using an icon at the beginning of the label with alt text of “error: \[concise description of error\]”.
- **Allow users to confirm or undo important actions.** This helps increase user confidence and reduce errors.

For more information about creating accessible forms see [WebAim: Creating Accessible Forms](https://webaim.org/techniques/forms/).
