---
title: "Migrating from Joomla/Mambo"
source_url: "https://www.drupal.org/docs/7/migrating-to-drupal/migrating-from-joomlamambo"
page_type: page
last_updated: "Last updated on 7 June 2023"
published: "2006-08-23T07:27:02+00:00"
modified: "2023-06-07T16:26:17+00:00"
breadcrumb: ["Drupal 7", "Migrating to Drupal 7"]
fetched: "2026-10-21T06:54:17Z"
raw: "raw/docs/7/migrating-to-drupal/migrating-from-joomlamambo.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Migrating from Joomla/Mambo

This guideline focuses on migration from Joomla! to Drupal. It also covers Mambo to some extent, a legacy CMS that was forked to become Joomla!.

It's also aiming to be useful for people who are used to Joomla! and want to learn how to use Drupal, and vice versa.

The term "Drupal 8+" is shorthand for "Drupal 8 and later" (i.e. Drupal 8, 9, 10, 11, and so on).

For migrating from Joomla! to Drupal 8+, you may want to read [Skynet Technologies: The ultimate guide for migrating Joomla to Drupal.](https://www.skynettechnologies.com/blog/migrating-joomla-to-drupal)

Before you start a migration you must understand some differences between both to make sure your migration to be successful:

## Joomla! vs Drupal

1.  Joomla! only supports one Section and one Category for each content, while you can assign Drupal contents to several Sections/Categories.
2.  Joomla! does not support multi-site setups, so the migration must be put into a certain site if you already setup a multi-site with Drupal.
3.  Comments on contents are not available in Joomla! by default, while Drupal by default supports comments for all content-types.

## Joomla! vs. Drupal Terminology

There are some different terms between Joomla! and Drupal. Here is a list to give you a quick understanding:

|                      |                                                                                                    |
|----------------------|----------------------------------------------------------------------------------------------------|
| Joomla!              | Drupal                                                                                             |
| Template             | Theme                                                                                              |
| Component            | Module.                                                                                            |
| Module               | Block.                                                                                             |
| Plugin               | Input filter.                                                                                      |
| Menu-Horizontal      | Primary Links                                                                                      |
| Menu-Vertical        | Navigation                                                                                         |
| Dynamic Content Item | Story                                                                                              |
| Static Content       | Page                                                                                               |
| Back-end             | there is no explicit back-end in Drupal, but the Administration Menu provides a similar interface. |
| SEF                  | Clean URLs (but some docs refer to SEF, too).                                                      |
| Section              | Taxonomy Vocabulary/Term                                                                           |
| Section Title        | Taxonomy Term (master)                                                                             |
| Category             | Taxonomy Term (child)                                                                              |
| Introtext            | Teaser                                                                                             |
| Maintext             | Body (see explanation below)                                                                       |
| Pathway              | Breadcrumb                                                                                         |

Other terms are the same, such as: forum discussion, editor, search, region, comment, subject/title, preview, html tag, view, edit, advertising/banner, log in/log out, profile, avatar, access control, logs, cache, site maintenance, RSS feed, parent-child and snippets.

## Directories

|           |                   |           |
|-----------|-------------------|-----------|
| Joomla    | Drupal 7          | Drupal 8+ |
| plugins   | sites/all/modules | modules   |
| templates | sites/all/themes  | themes    |

## Migrating Joomla! Content/Items

First, you must transfer all Joomla-Sections to Drupal-Categories and transfer Joomla-Categories to Drupal-Term according to their parent. After that, you can transfer Joomla! content/item from jos_content table. Drupal tables for saving article are drupal.node and drupal.node_revisions!

## Migrating Joomla! Introtext

Introtext vs Teaser, this is very important, you must know that Drupal can automatic turn the beginning of an article into an introtext. The introtext is called a teaser in Drupal. Now, how to convert Joomla! introtext to Drupal:

1\. copy the Joomla! Introtext to drupal.node_revisions:teaser  
2. copy the Joomla! Introtext+Maintext to drupal.node_revisions:body

Why does step \#2 include the Introtext again? Because in Drupal, there is a possibility to set Teaser different from the First Paragraph of a body. In other words, the First Paragraph of Drupal does not always become a Teaser!

If you want to edit migrated contents later on in Drupal, you should actually copy

Introtext + "\<!--break--\>" + Maintext

in step \#2.

## Migrating Joomla! Forum

Here we assume you use Joomlaboard forum for Joomla. In Drupal, forum is built-in, then you only need enable it on **administer-module** then show it on certain front page section using **administer-blocks**. You must transfer Parent-Forum Category of Joomlaboard to Drupal-Forum Container and Child-Forum Category to Drupal-Forum Category. *(Former version: Again, I am using SQLyog to transfer the entire forum contents, SQLyog is very easy because its GUI.)*

## Tips

You better not convert the Joomla! templates to Drupal Theme, but edit any existing Drupal theme to meet your requirement. Drupal expects you to use theme engines (*PHPtemplate* in Drupal 7, and *twig* in Drupal 8+) and let you use separate templates for various elements.

## Conceptual differences between the two

### Creating Content and Menu Structure

Joomla's content is stored in a hierachy with content categorisation being heavily intertwined with its menu structure. In Drupal all content is a flat Node where menus and taxonomy "sit on top" of the content. In Joomla!, a common structure for creating with content is this:

Choose where in the Menu article should go » Create Menu item » Define the type of content (e.g. Article) » Input Content

However in Drupal it is potentially simpler.

Create Content » Input Content » Change Settings including Menu placement, taxonomy, etc

However this can create a confusion to Joomla! users not used to the Drupal way. If you try and create a menu item before creating the content (or Node) then the Drupal Menu administration seems comparatively basic. The most complicated aspect of Drupal Menu system is that you have to manually type the path to the content, rather then selecting this from a list. This is not complicated if you create the content first and then change its menu settings whilst editing the content. But if you create the content without assigning menus it can only be found through the administrative menu.

Similarly to categorise content you do that on the actual edit content page. It requires you to have already have set up the Taxonomy for your website. This is powerful because the sorting of your content is not always tied into the Menus. But if you are used to Joomla's way of doing this, there is a [**Taxonomy Menu**](/project/taxonomy_menu) module to emulate the Joomla! way.

## Helpful Modules

You may also want to check out the following modules:  
[Migrate](/project/migrate) - for everything, quite popular as of 2014  
[User Import](/project/user_import) - for users  
[Node Import](/project/node_import) - for content  
[Joomla](/project/joomla) - all-in-one migration, stalled at Drupal 7  
[Joomla2Drupal](/project/joomla2drupal) - another all-in-one migration, stalled at Drupal 6
