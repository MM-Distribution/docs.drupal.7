---
title: "Add a field to a content type"
source_url: "https://www.drupal.org/docs/7/nodes-content-types-and-fields/add-a-field-to-a-content-type"
page_type: page
last_updated: "Last updated on 22 December 2016"
published: "2010-04-18T19:05:40+00:00"
modified: "2016-12-22T14:02:51+00:00"
breadcrumb: ["Drupal 7", "Drupal 7 nodes, content types, and fields"]
fetched: "2026-10-21T07:06:26Z"
raw: "raw/docs/7/nodes-content-types-and-fields/add-a-field-to-a-content-type.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Add a field to a content type

1.  Navigate to the Content types page (*Administer \> Structure \> Content types*).

2.  In the table, locate the row that contains your content type and click the **MANAGE FIELDS** link. If you can't find the **MANAGE FIELDS** link, be sure to enable the Field UI module.![](/files/Screen%20Shot%202016-11-03%20at%2011.26.47%20AM.png)

3.  In the Add new field section, enter a label for the field.

4.  In the Field name field, enter the machine name for the field. You can only use numbers, lower-case letters and the underscore character (\_). The node that the machine name is automatically generated and it is not necessary that it be changed.

5.  In the field type list, select one of the following types. Note that more fields such as '[Date](https://www.drupal.org/project/date)' and '[Location](https://www.drupal.org/project/location)' can be added using Drupal modules. To find modules, click [here](https://www.drupal.org/project/project_module). For help installing modules, click [here](https://www.drupal.org/node/120641).

    **Text**

    short text such as a name (limited to 255 characters)

    **Long text**

    long, multi-line alphanumeric text such as a biography

    **Boolean**

    has one of two values (for example: "yes/no" or "true/false" or "small/large")

    **List (text)**

    select from a list of text options (which can be formatted as either a drop-down list or checkboxes)

    **File**

    reference to a file (such as a PDF) on the Drupal file system

    **Image**

    reference to an image file such as GIF, JPG, PNG on the Drupal file system

    **Term reference**

    reference id to an existing Taxonomy Term (or tag)

    **Integer**

    a whole number, such as a year (e.g. 2012) or value (e.g. 1, 2, 5, 305); it does not allow decimals.

    **Float**

    a number that can use decimals, such as 0.0123456789

    **Decimal**

    a number that allows **exact** decimal values; often used for price or cost (such as \$199.99)

    **List (float)**

    select from a drop-down list of floats

    **List (integer)**

    select from a drop-down list of integers

    **Long text and summary**

    same as long text, but with an additional summary text

6.  In the Widget field, select a widget. The options vary depending on the field type.

7.  Click **Save**.

Note: Not all field types are provided by Drupal core. Things like References, Dates, Links, and various other types can be found [by filtering on "field" in the module list on drupal.org](http://drupal.org/project/modules?filters=tid%3A20224%20drupal_core%3A103%20bs_project_sandbox%3A0&solrsort=sis_project_release_usage%20desc) (or "Content Construction Kit" for Drupal 6). Users of the CCK module in Drupal 6 should note that the node reference and user reference fields are not supported in Drupal 7 core; however, there is a separate [References module](/project/references) that provides support for these fields in Drupal 7. In Drupal 7 [Entity reference](https://drupal.org/project/entityreference) is a good option to use for references because in Drupal 7 most of the things in the core are managed through entity.
