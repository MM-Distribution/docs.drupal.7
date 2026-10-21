---
title: "Create a custom content type"
source_url: "https://www.drupal.org/docs/7/nodes-content-types-and-fields/create-a-custom-content-type"
page_type: page
last_updated: "Last updated on 27 May 2017"
published: "2010-04-18T18:45:10+00:00"
modified: "2017-05-27T01:47:08+00:00"
breadcrumb: ["Drupal 7", "Drupal 7 nodes, content types, and fields"]
fetched: "2026-10-21T07:06:11Z"
raw: "raw/docs/7/nodes-content-types-and-fields/create-a-custom-content-type.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Create a custom content type

When creating a custom content type the first step is to set the **base configuration** for the content type. After that you may optionally add one or more **fields**.

**Step by step:**

1.  Navigate to the Content types page (*Administer \> Structure \> Content types*).
2.  Click **Add Content Type**.
3.  In the **Name** field, add a name for the content type. The name is required.
4.  In the **Description** field, you can write a description of the content type that will show up on the Add new content page (*Administer \> Content \> Add new content*). The description is not required.
5.  Set your preferred **base configuration** for this content type. Any content that you create of this content type will have these values by default. The values can be overridden for each content created. You can specify default values for **Submission form settings**, **Publishing options**, **Display settings**, **Comment settings** and **Menu settings**.
6.  Once your preferred **base configuration** is saved, you can either click **Save content type** or **Save and add fields**. Save Content Type leaves the content type with the Title and Body fields, while Save and Add Fields allows you to add more fields to the content type. You can always add more fields later.
7.  When adding fields, you have the choice to either add a new field or add an existing field. See [this guide](https://www.drupal.org/docs/7/nodes-content-types-and-fields/add-a-field-to-a-content-type) for adding fields to content types.
8.  Once your content type has the desired fields, you can create an instance of it as a node by navigating to the content page (*Administer \> Content*). Then select the name of your content type.

**Submission form settings**  
![Submission form](/files/ContentType_Submission4_10-31-11.jpg)

In the Title field label, you may add a title for your content type. For example, if your content type is "Furniture," you can choose a title of "Furniture Type." Note: The default for this field is "Title."

**Publishing options**  
![Publishing options](/files/ContentType_PublishingOptions3_10-31-11.jpg)

The default publishing options are Published and Promoted to front page. Additional options are available.

**Display settings**  
![Display settings](/files/ContentType_DisplaySettings3_10-31-11.jpg)

The Display Settings has one option which allows the Author username and publish date to be displayed with the content.

**Comment settings**  
![Comment settings](/files/ContentType_CommentSettings3_10-31-11.jpg)

You may leave comments open, closed, or hidden. The default values allow for 50 comments to be published per page in a threaded list. If you're a beginner, you may want to keep these default values.

There is more information on the comment settings at: [Administering a content type's comment settings](http://drupal.org/node/777818).

**Menu settings**  
![Menu settings](/files/ContentType_MenuSettings3_10-31-11.jpg)

In the Menu settings you can choose which default parent item to use. This comes in handy when using taxonomy in your site.
