---
title: "Translating content"
source_url: "https://www.drupal.org/docs/7/multilingual/translating-content"
page_type: page
last_updated: "Last updated on 11 March 2021"
published: "2012-03-24T20:40:54+00:00"
modified: "2021-03-11T21:35:31+00:00"
breadcrumb: ["Drupal 7", "Multilingual guide for Drupal 7"]
fetched: "2026-10-21T06:09:27Z"
raw: "raw/docs/7/multilingual/translating-content.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Translating content

In Drupal 7, two methods exist for translating site content:

- Content translation and
- Entity translation

A site can use both methods as long as the relevant modules are enabled: Content Translation (core) and Entity Translation (Drupal 7 contrib). The method of multilingual support can then be configured for each content type. In other words, you can use *Content Translation* for some content types and *Entity Translation* for others.

The *Content Translation* module allows nodes to be translated by creating a set of nodes which are translations of each other (in other words, by creating a *node translation set*). By contrast, the *Entity Translation* module allows particular fields to be translated, while only a single node or entity is created. With *Entity Translation*, the entity is language-independent. Only the associated fields are flagged with a language.

Notes:

- There are two main methods to choose from to configure a multilingual Drupal website:
  1.    ***Entity Translation*** is the *newer method*
  2.    ***Content Translation*** is the *older method*
- *[**Entity Translation**](https://www.drupal.org/project/entity_translation)* is now in Drupal 8 core. It is available for both Drupal 7 and 8, with an upgrade path from Drupal 7 to 8
- *[**Content Translation**](https://www.drupal.org/project/translation)* is available for Drupal 7 (and previous versions)
- Below is the documentation for *Content Translation* (the older method)

------------------------------------------------------------------------

When the *Content Translation* module is enabled you can translate site content into different languages. Working with the [**Locale module**](/documentation/modules/locale) (which manages the enabled languages and provides translation for the site interface), the *Content Translation* module is key to creating and maintaining translated site content.

### Configure content translation

1.  Navigate to the Permissions page **(*Administration \> User permissions* in Drupal 6, or *Administration \> People \> Permissions* in Drupal 7)** and assign the “translate content” permission to the appropriate user roles.
2.  Navigate to the Languages page**(*Administration \> Settings \> Language* in Drupal 6, or *Administration \> Configuration \> Regional and language \> Languages* in Drupal 7)** and add and enable desired languages.

### Enable translation support for a content type

1.  Navigate to the *Content types* administration page **(*Administration \> Content \> Types* in Drupal 6, or *Administration \> Structure \> Content types* in Drupal 7)**.
2.  Select a content type you want translated, and select "edit", then "Workflow settings" for Drupal 6 or "Publishing options" for Drupal 7.
3.  At the "Multilingual support" section, select "Enabled, with translation".
4.  Be sure to save each content type after enabling multilingual support.

For more useful materials on configuring a multilingual site in Drupal, see [Resource Guide: Configuring a Multilingual Site](/resource-guides/configuring-multilingual-site).

### Tips for content type translation

- Use the “Language” drop-down to select the appropriate language when creating or editing posts.
- Provide new or edit current translations for existing posts via the “Translation” tab. Only visible while viewing a post as a user with the “translate content” permission, this tab allows translations to be added or edited using a specialized editing form that also displays the content being translated.
- Update translations as needed, so that they accurately reflect changes in the content of the original post. The translation status flag provides a simple method for tracking outdated translations. After editing a post, for example, select the "Flag translations as outdated" check box to mark all of its translations as outdated and in need of revision. Individual translations may be marked for revision by selecting the "This translation needs to be updated" check box on the translation editing form.
- The "Content management" administration page displays the language of each post, and also allows filtering by language or translation status.

Use the language switcher block provided by the *Locale* module to allow users to select a language. If available, both the site interface and site content are presented in the language selected.

### Import data in multiple languages

This tutorial will explain, step-by-step, how to import multilingual data into Drupal. This is important for projects that require data to be imported, whether it's new data, data from an old site, or data from a desktop application.

There are a few modules that provide data import functionality; the most important one at the moment is [Feeds](/project/feeds). However, it's not currently able to import multilingual data.

An [article](http://www.lullabot.com/articles/drupal-data-imports-migrate-and-table-wizard) on the Lullabot website gives an overview of importing data using Migrate and Table Wizard. This documentation page provides details on how to use these tools when importing multilingual content.

- First, it's necessary to install Drupal and also install and enable the following modules: [Migrate](/project/migrate) and [Migrate_i18n](/project/migrate_i18n). You must also install and enable their dependencies: [Table Wizard](/project/tw), [Schema](/project/schema), [Views](/project/views), [Migrate Extras](/project/migrate_extras), and [Advanced Help](/project/advanced_help).

- Next, and very importantly, you must prepare the data to be loaded. Drupal must have access to the data using the "Table Wizard" module, so we have to create a table in the same database where Drupal installation has its own tables.

  In our case, we are going to load a table of designers, which includes the name of each designer. The table is as follows:

  |     |     |                 |      |
  |-----|-----|-----------------|------|
  | id  | nid | name            | lang |
  | 1   | 1   | Todd Bracher    | es   |
  | 2   | 1   | Todd Bracher    | ca   |
  | 3   | 1   | Todd Bracher    | en   |
  | 4   | 2   | Jasper Morrison | es   |
  | 5   | 2   | Jasper Morrison | en   |
  | 6   | 2   | Jasper Morrison | ca   |

  lang: the language code for i18n, in our case (en) English, (es) Spanish, (ca) Catalan

  - id: the primary key
  - nid: the node identifier that must be the same for each designer in every language
  - name: the name of the designer that can be different in every language

  We name our table "load_designers" with the structure and data as described above.

- Now go to *Admin \> Content management \> Table Wizard*. Select "Add existing tables" and it shows a list of tables present in the Drupal database. Select the table "load_designers" and click "Add tables". This action creates a new handler for the table and an associated view to query its data in the *Views* module. You can go to *Admin \> Site building \> Views* and take a look at its definition.

- It's time to create the load process via the *Migrate* module. Go to *Admin \> Content Management \> Migrate* and click on "Add content set". In the form that slides down write the name and "load_designers" and select the content type where you want to load data, in our case "Node:Designer" (a custom content type created using CCK, but that's another story). Select the Table Wizard "load_designers", which we created previously, as the data source. Click "Add" and, in the next form, associate the necessary fields depending on your data. Click "Submit".

- Now we are ready to run the loading process, but in our case we want to load data in multiple languages and associate each node with its translations. This is what the *Migrate_i18n* module does. Go to *Admin \> Content Management \> Migrate \> Internationalization* and select, in the first combo box, the field that contains the language identifier (i.e. "lang"). In the second combo box, select the field that identifies nodes across languages (that's "nid"). Click "Submit", and the bottom options will be activated.

  In the bottom form you should see a list for each language active in the Drupal installation and each list with the different available language values (the contents of the "lang" column in the "load_designers" table). Then, select the corresponding language code for each language and click "Submit".

- Now we are ready to start loading the data into Drupal. Go to *Admin \> Content management \> Migrate*. Select "Import" from the "load_designers" process and click "Execute" to slide down the execution options. Simply click "Run".

- When the process finishes all data is loaded and we can see it at *Admin \> Content management \> Content*. To verify that all translations are loaded correctly, open a node and you should see three translations, corresponding to each language.
