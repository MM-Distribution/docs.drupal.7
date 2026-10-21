---
title: "Add a vocabulary to a content type"
source_url: "https://www.drupal.org/docs/7/organizing-content-with-taxonomies/add-a-vocabulary-to-a-content-type"
page_type: page
last_updated: "Last updated on 22 August 2016"
published: "2013-01-12T16:20:45+00:00"
modified: "2016-08-22T20:50:05+00:00"
breadcrumb: ["Drupal 7", "Organizing content with taxonomy in Drupal 7"]
fetched: "2026-10-21T07:08:30Z"
raw: "raw/docs/7/organizing-content-with-taxonomies/add-a-vocabulary-to-a-content-type.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Add a vocabulary to a content type

To use taxonomy terms to organize your content, the vocabulary must be associated with the content type. To add vocabulary, go to structure-\>taxonomy-\>add vocabulary. Here you can add a vocabulary list. Once created, you will see it appear in the list and can click to "view terms" and then will be able to add terms to the vocabulary list.

1.  In order to associate taxonomy terms to your content, you must add a field of type 'term reference' on the /Administration/Structure/Content types/\[your-content-type\]/Manage fields page.
2.  Add a new field by entering a label in the **Add new field** box, select **Term reference** from the dropdown box in Field Type, then select the relevant widget.  
    ![Add a term reference field in a content type](/files/node1886980_1.jpg)  
3.  Click **Save**. You are immediately taken to the Field Settings page.
4.  Select the vocabulary that you want to use with this term reference field, then click **Save Field Settings**.  
    ![Select the vocabulary to use for the term reference](/files/node1886980_2.jpg)  
5.  You are taken to a page to configure the newly added term reference field. Here you can change the term label, provide some help text and provide a default value.
