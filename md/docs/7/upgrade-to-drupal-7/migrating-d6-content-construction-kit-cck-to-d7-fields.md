---
title: "Migrating D6 Content Construction Kit (CCK) to D7 Fields"
source_url: "https://www.drupal.org/docs/7/upgrade-to-drupal-7/migrating-d6-content-construction-kit-cck-to-d7-fields"
page_type: page
last_updated: "Last updated on 18 August 2016"
published: "2011-05-01T22:25:25+00:00"
modified: "2016-08-18T20:27:12+00:00"
breadcrumb: ["Drupal 7", "Upgrade to Drupal 7"]
fetched: "2026-10-21T06:22:38Z"
raw: "raw/docs/7/upgrade-to-drupal-7/migrating-d6-content-construction-kit-cck-to-d7-fields.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Migrating D6 Content Construction Kit (CCK) to D7 Fields

Data must be migrated to upgrade Content Construction Kit (CCK) in Drupal 6 to Drupal 7 core fields. Much but not all of CCK functionality is now part of Drupal 7 core. Several features require the installation of new, dedicated 7.x modules.

- **Node Reference and User Reference** are replaced by either the [References](/project/references) module or the [Entity Reference](/project/entityreference) module. To use Entity Reference (as it's better maintained and more sustainable), it's necessary to migrate to References first, and then use the [Reference to Entity Reference Field Migration](/project/entityreference_migration) module.
- **Content permissions** require the ***Field Permissions*** module (<http://drupal.org/project/field_permissions>).
- **Field Groups** require the ***Field Group*** (<http://drupal.org/project/field_group>) module.
- **Multigroups** require the [Field Collection](/project/field_collection) module, along with a patch from [Create path/tool/feature that upgrades data from D6 CCK3 Multigroup to Field Collection](/node/1722450).

The following instructions describe the steps necessary to migrate CCK for a site that was upgraded from Drupal 6 to Drupal 7. [Learn more on upgrading from Drupal 6 to Drupal 7.](http://drupal.org/node/570162)

## Upgrade Steps

The Migrate Fields page is divided into 3 sections:

**Available fields**- Fields that have not been migrated but are available for migration. Some fields will be listed as available, but may have attributes that will be lost (e.g., option widgets, permission setting for that field, the attached image) because the appropriate module has yet to be enabled. If you care about that attribute, enable the supporting modules BEFORE migrating the field.

**Converted fields**- Fields that have already been converted. You can choose to roll them back if the conversion did not work correctly. Note that rolling fields back will completely destroy the new field tables. This operation cannot be undone!

**Unavailable fields**- Fields that cannot be migrated because some modules are missing. Download and install/enable any required modules listed in the ***Other information*** column (aka Step 4) of this section.

**Note:** If you find that some image or file fields cannot be migrated, check to make sure that the Drupal Core 'field', 'file' and 'image' modules are enabled.

If you are getting "exception 'PDOException' with message 'SQLSTATE\[42000\]: Syntax error or access violation: 1064" errors while migrating fields with autocomplete_widgets, you should install version 7.x-1.x-dev of [Autocomplete Widgets for Text and Number Fields](http://drupal.org/project/autocomplete_widgets) module as this is fixed in [\#1790758: PDO exception on migrate autocomplete_widgets longtext field](/project/autocomplete_widgets/issues/1790758 "Status: Closed (fixed)").

1.  **Download latest 7.x CCK module**

    After upgrading to Drupal 7, download the latest 7.x CCK module version (<http://www.drupal.org/project/cck>). Typically this will be placed in your *sites/all/modules or sites/example.com/modules* directory.

2.  **Enable the CCK Content Migrate module**

    Browse to <http://example.com/admin/modules> and check the box next to Content Migrate in the CCK field group. Remember to press save configuration at the bottom of the screen. You may need to clear your cache in order for the Migrate fields option to be displayed in the next step.

3.  **Browse to the Migrate fields page**

    Browse to *Structure \> Migrate Fields* or <http://example.com/admin/structure/content_migrate> for a page to walk you through the migration process.

4.  **Download additional modules if necessary**

    Typically these will be placed in your *sites/all/modules or sites/example.com/modules* directory. Be sure to back up your database and run update.php after enabling a module.

    - **References module** (<http://drupal.org/project/references>).
    - **Field Permissions module** (<http://drupal.org/project/field_permissions>).
    - **Field Group module** (<http://drupal.org/project/field_group>).
    - **Link module** (<http://drupal.org/project/link>).
    - **Email module** (<http://drupal.org/project/email>).
    - **Date module** (<http://drupal.org/project/date>). Also look at DateAPI, Date Repeat, and Date Repeat API.
    - **Viewfield module** (<http://drupal.org/project/viewfield>).
    - **Location module** (<http://drupal.org/project/location>).

5.  **Enable additional modules if necessary**

    Browse to <http://example.com/admin/modules> and check all applicable boxes in the ***Fields*** section. Remember to press save configuration at the bottom of the screen.

6.  **Migrate fields**

Browse to *Structure \> Migrate Fields* or <http://example.com/admin/structure/content_migrate>.

Check the box next to all fields you would like to migrate in the ***Available fields*** section.

Press the ***Migrate selected fields*** button.

If the migration process is successful you should receive a message detailing that each field was created. All fields should now be listed in the ***Converted fields*** section of the page.

Once the migration of all fields is done you can disable the module.

1.  **Uninstall CCK Content Migrate module**
