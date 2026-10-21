---
title: "Specify how fields are displayed"
source_url: "https://www.drupal.org/docs/7/nodes-content-types-and-fields/specify-how-fields-are-displayed"
page_type: page
last_updated: "Last updated on 22 December 2016"
published: "2010-04-18T21:07:06+00:00"
modified: "2016-12-22T14:12:24+00:00"
breadcrumb: ["Drupal 7", "Drupal 7 nodes, content types, and fields"]
fetched: "2026-10-21T07:06:57Z"
raw: "raw/docs/7/nodes-content-types-and-fields/specify-how-fields-are-displayed.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Specify how fields are displayed

Content can be displayed differently depending on whether it's in a list with similar content, in search results, or being viewed in full. For example, content displayed in a list is typically trimmed so it doesn't take up too much space on the page and may only display the most important fields.

## What is a view mode?

Drupal refers to the different ways a piece of content can be displayed as *View modes* (also called *Display modes*, or *Build modes* in Drupal 6). All entities, including user profiles, taxonomy terms, and blocks (D8 only) have at least one view mode, plus a *Default* view mode which is used when a view mode has not been explicitly set. You can use the [Entity view modes module](https://www.drupal.org/project/entity_view_mode) or the [Display Suite module](https://www.drupal.org/project/ds) to create your own view modes.

## Hiding, showing and ordering fields and their labels

For each view mode, Drupal allows you to:

- show and hide fields,
- change the order that fields are rendered in,
- hide or show the field's label, and,
- change how certain types of fields are displayed (for example, whether a field's content is trimmed).

Modules like [Display Suite](https://www.drupal.org/project/ds) and [Panels](https://www.drupal.org/project/panels) also let you set a custom layout for the fields in each view mode.

### Changing how nodes are displayed

Drupal lets you set different display settings for each content type. To change how a content type is displayed:

1.  Navigate to the *Content types* page (*Administer \> Structure \> Content types*).
2.  In the table, locate the row that contains the content type you wish to change and click the **manage display** link. This takes you to the *Default* view mode settings page.
3.  At the bottom of the page, in the *Custom display settings* section, check the checkboxes next to the view modes you want to customize and click **Save**.
4.  Once the page re-loads, you will see links under the tabs at the top of the page. There will be a link for each view mode you selected in the previous step. Clicking one of these links will take you to a screen where you can hide, show, reorder, and customize fields.

Out-of-the-box, Drupal defines five view modes for nodes:

Full content  
The most detailed view of a node. You see this when you visit the node's URL.

Teaser  
A short summary of the node intended to catch visitors' interest so they will view the Full content. Displayed on many of Drupal's default listing pages, such as the front page and taxonomy term listing pages.

RSS  
How the node is displayed in RSS feeds. Visitors or webservices subscribed to the RSS feed will see content that looks like this.

Search index  
The content that Drupal's internal search sees when it goes to index the page (search engines such as Google typically see the *Full content* view mode).

Typically, you only customize this view mode if you want to *hide* data from Drupal's internal search.

Search result  
A short summary of the node when Drupal's internal search displays it as a search result (search engines such as Google generate their own search result view, typically from the *Full content* view mode).

### Taxonomy terms

1.  Navigate to the *Taxonomy* page (*Administer \> Structure \> Taxonomy*).
2.  In the table, locate the row that contains the vocabulary you wish to change, and click the **edit vocabulary** link.
3.  Click the **Manage display** tab. This takes you to the *Default* view mode settings page. Since Drupal only defines one view mode for taxonomy terms, you may hide, show, reorder, and customize fields here.

Out-of-the-box, Drupal defines one view mode for taxonomy terms:

Taxonomy term page  
The most detailed view of a taxonomy term. You see this when you click on a taxonomy term link from a node page, or you visit the URL of the taxonomy term directly.

You can only customize the upper portion of the taxonomy term page (the part that contains data about the term itself). Drupal displays a listing of all nodes tagged with the term (in their *Teaser* view mode) in the lower portion.

### Users

1.  Navigate to the *Account settings* page (*Administer \> Configuration \> People \> Account settings*).
2.  Click the **Manage display** tab. This takes you to the *Default* view mode settings page. Since Drupal only defines one view mode for user accounts, you may hide, show, reorder, and customize fields here.

Out-of-the-box, Drupal defines one view mode for user accounts:

User account  
The most detailed view of a user account. You see this when you log in, or when you visit the URL of the user directly.

## Field label display options

Field labels can be displayed in the following ways:

Above  
The field label is displayed on it's own line above the field value(s).

Inline  
The field label is displayed before the field value(s), on the same line.

Visually hidden (Drupal 8 only)  
The field label is hidden for sighted users, but still visible to visitors using assistive technologies like screenreaders.

If you don't want a field label to show up on the page, this is almost always the best option because it provides context about the data in the field to blind or low-vision users which they may not be able to figure out if the label was *Hidden*.

If you're using Drupal 7 and you want to hide content in a similar way, please refer to the section of the Theming guide about [Hiding content properly](https://www.drupal.org/node/472572).

Hidden  
Completely removes the field label for all users.

Typically, you only choose this if you only have two fields which are supposed to appear as if they are a single field.

## Manage Display Page Details

Manage Display page contains a table with 3 columns with following titles:

Field  
The field column contains all the visible and hidden field names.

Label  
The label column contains options to show label *Above, Inline or Hidden* respectively. These values are described above.

Format  
The format column contains the options to show the field value in different formats. *Hidden* is the global value which is present in all the format option list, if you choose hidden then it will hide the whole field from showing on the content page.
