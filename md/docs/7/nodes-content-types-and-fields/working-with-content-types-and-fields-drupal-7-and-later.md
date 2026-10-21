---
title: "Working with content types and fields (Drupal 7 and later)"
source_url: "https://www.drupal.org/docs/7/nodes-content-types-and-fields/working-with-content-types-and-fields-drupal-7-and-later"
page_type: page
last_updated: "Last updated on 12 November 2017"
published: "2009-11-30T01:06:28+00:00"
modified: "2017-11-12T03:43:07+00:00"
breadcrumb: ["Drupal 7", "Drupal 7 nodes, content types, and fields"]
fetched: "2026-10-21T07:05:55Z"
raw: "raw/docs/7/nodes-content-types-and-fields/working-with-content-types-and-fields-drupal-7-and-later.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Working with content types and fields (Drupal 7 and later)

In Drupal, a **Content Type** consists of the following primary elements:

- Content type **base configuration**
- Content type **fields**

**Base configuration:**

The base configuration of a content type defines the default behavior and properties of the content type. Examples include whether or not a newly created item of content has the status of *published* by default; or whether or not a newly created item of content is associated with one or more menus.

Moreover, the base configuration of a content type may also permit other additional custom settings provided by add-on modules.

**Fields:**

Content Types permit the creation of a set of fields that are associated together in some meaningful way.

Content Types are the building blocks for structured authoring in Drupal. Content types often work in conjunction with [Views](/project/views), which is one way you can serve up content to your end users; you can control the content types that appear and the order in which they appear. Developers can also customize the authoring experience in the same way.

> One way to think of content types is to visualize the contacts on your mobile phone. If you were to duplicate this on a Drupal site you would create a Content Type. You would name your new Content Type (e.g. Contacts), define the information that you wanted to store about each contact (called Fields in Drupal), and then add those Fields (e.g. First name, last name, and mobile phone number, etc.) to that Content Type. You would then use this "Contacts" Content Type to enter the information for each of the contacts you had in your contacts list. You would use a View (as described above) to display your Contacts in a list similar to that which you see on your mobile phone.

**Field terminology:**

- **Field.** A category of data that can be added to an element, for example, Title, Body, Comment body, Tags, Image.
- **Field type.** The data type of a field, for example, text, integer, image.
- **Field instance.** A field added to an element.

"Element" above is not Drupal terminology but is used here for convenience. In Drupal terminology, this is either an [entity type](https://www.drupal.org/node/1261744) (such as a node or taxonomy term) or a [bundle](https://www.drupal.org/node/1261744) (such as an article or page).

The illustration of the Field UI below shows the field instances of the content type, Basic page. There are instances of the fields Title and Body.

An element (i.e., an entity type or bundle) can have only one instance of each field. However, a field can have a setting called "Number of values," which determines how many times a field can appear in an element. For example, if an instance of the field Image is added to the content type Basic page with "Number of values" set to 1, 3, or unlimited, then a page is allowed to have, respectively, only one, or up to three, or an unlimited number of images on it.

The primary (but not all) information about fields and field instances is stored in, respectively, the database tables "field_config" and "field_config_instance". The field type of a field is stored in the column "type" of the table "field_config". (**Warning:** Don't modify the structure or content of those tables (or any Drupal database tables) unless you know what you're doing. The data in those tables are connected to other data elsewhere, so changes need to be handled by the software.)

## The Field UI

The Field UI module provides an administrative user interface (UI) for attaching and managing fields. Fields can be defined at the content-type level for content items and comments, at the vocabulary level for taxonomy terms, and at the site level for user accounts. Other modules may also enable fields to be defined for their data. Field types (text, image, number, etc.) are defined by modules, and collected and managed by the [Field module](http://drupal.org/documentation/modules/field).

The Field UI is a form used for managing fields. It comes up when you click on the *Manage Fields* tab of an editing form, for example, when editing a content type (such as Basic page) (/admin/structure/types/manage/page) or a taxonomy term (such as Tags) (/admin/structure/taxonomy/tags/edit). It can also be brought up by clicking on "manage fields" in the list of content types (/admin/structure/types).

The following image shows the Field UI as it appears for managing the fields of the content type Basic page:

![Managing fields with the Field UI](/files/field-ui_0.png)

Managing fields with the Field UI

The Field UI has two parts:

- A list of field instances of the element being edited (e.g. Basic page or Tags). In the above image, the field instances are Title and Body.
- A pair of subforms for adding new field instances. These subforms are:
  - **Add new field.** This is used to both create a new field and to add an instance of that field to the element being edited.
  - **Add existing field.** This is used to add an instance of a field that already exists.

To add images or tags to a page, you use "Add existing field" because when Drupal is first installed, it predefines the fields Image and Tags.

## Uses

### Planning fields

There are several decisions you will need to make before defining a field for content, comments, etc.:

- **What the field will be called**  
  A field has a label (the name displayed in the user interface) and a machine name (the name used internally). The label can be changed after you create the field if needed, but the machine name cannot be changed after you have created the field. The machine name also must be unique - you cannot have two fields with the same machine name, even if they belong to different content types. 
- **What type of data the field will store**  
  Each field can store one type of data (text, number, file, etc.). When you define a field, you choose a particular field type, which corresponds to the type of data you want to store. The field type *cannot* be changed after you have created the field.
- **How the data will be entered and displayed**  
  Each field type has one or more available "widgets" associated with it; each widget provides a mechanism for data input when you are editing (text box, select list, checkboxes, file upload, etc.). Each field type also has one or more display options, which determine how the field is displayed to site visitors. The widget and display options can be changed after you have created the field.
- **How many values the field will store?**  
  You can store one value, a specific maximum number of values, or an unlimited number of values in each field. For example, an employee identification number field might store a single number, whereas a phone number field might store multiple phone numbers. This setting can be changed after you have created the field, but if you reduce the maximum number of values after inputting/entering data, you may lose information.

### Reusing fields

Once you have defined a field, you can reuse it. For example: if you define a custom image field for one content type, and you need to have an image field with the same parameters on another content type, you can add the same field to the second content type, in the Add existing field area of the user interface. You could also add this field to a taxonomy vocabulary, comments, user accounts, etc.

Some settings of a reused field are unique to each use of the field; others are shared across all places you use the field. For example, the label of a text field is unique to each use, while the setting for the number of values is shared.

There are two main reasons for reusing fields. First, reusing fields can save you time over defining new fields. Second, reusing fields also allow you to display, filter, group, and sort content together by field across content types. For example, the contributed Views module allows you to create lists and tables of content. So if you use the same field on multiple content types, you can create a View containing all of those content types together displaying that field, sorted by that field, and/or filtered by that field.

There is one main reason to not reuse a field: different permissions. For example, you may need different user roles to have different levels of access to a field, depending on the content type to which it has been added. This can be difficult if you reuse a field.

- **Fields on content items**  
  Fields on content items are defined at the content-type level, on the Manage fields tab of the content type edit page (which you can reach from the Content types page). When you define a field for a content type, each content item of that type will have that field added to it. Some fields, such as the Title and Body, are provided for you when you create a content type or are provided on content types created by your installation profile.
- **Fields on taxonomy terms**  
  Fields on taxonomy terms are defined at the taxonomy vocabulary level, on the Manage fields tab of the vocabulary edit page (which you can reach from the Taxonomy page). When you define a field for a vocabulary, each term in that vocabulary will have that field added to it. For example, you could define an image field for a vocabulary to store an icon with each term.
- **Fields on user accounts**  
  Fields on user accounts are defined on a site-wide basis on the Manage fields tab of the Account settings page. When you define a field for user accounts, each user account will have that field added to it. For example, you could add a long text field to allow users to include a biography.
- **Fields on comments**  
  Fields on comments are defined at the content-type level, on the Comment fields tab of the content type edit page (which you can reach from the Content types page). When you add a field for comments, each comment on a content item of that type will have that field added to it. For example, you could add a website field to the comments on forum posts, to allow forum commenters to add a link to their website.

### Remove field

If you need to remove a field completely one would delete it from all existing content types where it exists. The Field UI can tell you what content types a field is being used on before you try and delete the field.

However, some modules create fields automatically and must be uninstalled to have their fields removed. After you disable the module, you'll have to go to the uninstall tab to complete the uninstall process.

The fields you want to delete should be deleted when cron runs, however, some people have reported that multiple cron runs are needed for the field to fully deleted depending on how much data or how many fields are being deleted at one time. Run cron several times, if your field isn't deleted right away.

A better way to do this is run these two functions:

``` php
field_delete_field($field_name); field_purge_batch(); // note: only run this if you need the field deleted immediately!! otherwise it will just be deleted the next time the cron runs 
```

If you manually delete fields from the database, many things can go wrong. For example, hook_field_delete will not be called and one of your modules might fail and crash the site. For this reason, it is best to only use the Field UI for deleting fields if you aren't comfortable with the code or with SQL/databases.

## Versions

### Drupal 7

The Fields module was incorporated into Drupal 7. Unlike earlier versions, you do not need to download a separate module to add fields to a content type.

### The Content Construction Kit (CCK) in Drupal 6 and lower

Field UI module is the core version of the Drupal 6 [CCK module](http://drupal.org/documentation/modules/cck).

## Technical details

**Default module:** Yes.  
**Dependencies:** [Field](http://drupal.org/documentation/modules/field), Field SQL Storage module or custom storage module.  
**Related Modules:** [Field](http://drupal.org/documentation/modules/field), Field SQL Storage, File, Image, List, Number, Node, Taxonomy, User, Text  
**Permissions:** None.  
**API Documentation:** [Field storage API](http://api.drupal.org/api/group/field_storage/7)  
**Database tables:** None.
