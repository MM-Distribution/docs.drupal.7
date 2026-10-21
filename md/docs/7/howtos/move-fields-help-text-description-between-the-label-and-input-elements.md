---
title: "Move field's help text (description) between the label and input element(s)"
source_url: "https://www.drupal.org/docs/7/howtos/move-fields-help-text-description-between-the-label-and-input-elements"
page_type: page
last_updated: "Last updated on 21 January 2023"
published: "2014-08-11T12:23:23+00:00"
modified: "2023-01-21T10:53:32+00:00"
breadcrumb: ["Drupal 7", "Site building and development HowTos for Drupal 7"]
fetched: "2026-10-21T08:06:58Z"
raw: "raw/docs/7/howtos/move-fields-help-text-description-between-the-label-and-input-elements.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Move field's help text (description) between the label and input element(s)

A common problem with field types that takes up a lot of screen estate is that the help text disappears at the bottom and users won't notice it. The most obvious example of this is a text field with input format with more than 20 rows. Another example is a multi-value field with many added values. In cases like these, developers might want to make the help text more visible by moving it above the input element.

There are several solutions to this, and these can be grouped into two main types:

- Solutions that move the field's existing help text from below to above the input area.
- Solutions that add a new text setting which are put between the label and the input area

There is a third kind of solution which involves using JavaScript to manipulate the DOM, but this is considered a hack and is not included here.

## Solutions using the existing field help text

These solutions will use the *existing* field help text and move it around in various ways.

- Override [theme_webform_element](http://www.drupalcontrib.org/api/drupal/contributions!webform!webform.module/function/theme_webform_element/7) in your theme's template.php file. More info: [Overriding themable output](https://www.drupal.org/node/341628).
- [Form element layout](/project/fel). This lets you configure the position of the field's existing help text on a per field basis to be before or after the input element. It defaults to standard/core behavior. Developers can override the position in any form using the `#description_display` attribute.
- [Top Description](/sandbox/jrb/top_description). A minimalist sandbox module that will unconditionally move *all* form descriptions above the input element. Minimally maintained and maintenance fixes only.
- Use front-end [JavaScript to move the fields](https://drupal.stackexchange.com/questions/68369/how-to-move-description-below-the-label-for-a-field-in-a-form/314460#314460) around.

## Solutions with a new help text

These are modules that will add a new text setting for the field and inject it between the label and otherwise ignore the existing help text.

- [Label Help](/project/label_help). Does not modify existing help text and this can be used as an additional help text.
- [Extra Field Description](/project/extra_field_description). Behaves exactly like *Label Help*, but it seems to be less maintained.
- [Better field descriptions](/project/better_field_descriptions). Like the two options above, it creates an additional field setting for the additional help text. However, this module extracts the configuration to a separate admin page with its own permission, thereby making it possible for users without the *Administer site configuration* permission to edit the additional field help texts.
