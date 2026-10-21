---
title: "Writing .install files (Drupal 7.x)"
source_url: "https://www.drupal.org/docs/7/creating-custom-modules/writing-install-files-drupal-7x"
page_type: page
last_updated: "Last updated on 3 March 2017"
published: "2010-08-07T02:24:42+00:00"
modified: "2017-03-03T09:42:23+00:00"
breadcrumb: ["Drupal 7", "Creating custom modules in Drupal 7"]
fetched: "2026-10-21T07:22:12Z"
raw: "raw/docs/7/creating-custom-modules/writing-install-files-drupal-7x.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Writing .install files (Drupal 7.x)

This page is about **Drupal 7**. For **Drupal 6**, see [Writing .install files, (Drupal 6.x)](http://drupal.org/node/323314).

Drupal 7 uses .install files to create database tables and fields, and to insert data. Drupal 7 .install files can also provide updates to change the database structure and content. Drupal 7 also uses .install files and includes the Field module in core. Field provides a different way to send data to nodes than in Drupal 6 and could replace some .install files.

## .install file

In Drupal 7, .install files can define new tables, load data, and implement conversions during updates.

A `.install` file is run the first time a module is enabled, and is used to run setup procedures as required by the module. The most common task is creating database tables and fields. The `.install` file does not have any special syntax. It is merely a PHP file with a different extension.

`.install` files are also used to perform updates when a new version of a module needs it.

## Instructions

Install instructions are enclosed in a `_install()` function. This hook will be called when the module is first enabled. Any number of functions can reside here, but the most typical use is to create the necessary tables for your module.

Database tables are created using the [**Schema API**](http://drupal.org/node/146843) .  
The Schema API allows modules to declare their database tables in a structured array (similar to the Form API) and provides API functions for creating, dropping, and changing tables, columns, keys, and indexes.

## A sample schema data structure (taken from the Schema Api Documentation)

As an example, here is an *excerpt* of the schema definition for Drupal's 'node' table:

``` php
 $schema['node'] = array(
    'description' => 'The base table for nodes.',
    'fields' => array(
      'nid' => array(
        'description' => 'The primary identifier for a node.',
        'type' => 'serial',
        'unsigned' => TRUE,
        'not null' => TRUE),
      'vid' => array(
        'description' => 'The current {node_revisions}.vid version identifier.',
        'type' => 'int',
        'unsigned' => TRUE,
        'not null' => TRUE,
        'default' => 0),
      'type' => array(
        'description' => 'The {node_type} of this node.',
        'type' => 'varchar',
        'length' => 32,
        'not null' => TRUE,
        'default' => ''),
      'title' => array(
        'description' => 'The title of this node, always treated a non-markup plain text.',
        'type' => 'varchar',
        'length' => 255,
        'not null' => TRUE,
        'default' => ''),
      ),
    'indexes' => array(
      'node_changed'        => array('changed'),
      'node_created'        => array('created'),
      ),
    'unique keys' => array(
      'nid_vid' => array('nid', 'vid'),
      'vid'     => array('vid')
      ),
    'primary key' => array('nid'),
    );
```

In this excerpt, the table 'node' has four fields (table columns) named 'nid', 'vid', 'type', and 'title'. Each field specifies its type ('serial', 'int', or 'varchar' in this example) and some additional optional parameters, including a description.

The table's primary key is the single field 'nid'. There are two unique keys: first named 'vid' on the field 'vid' and second called 'nid_vid' on fields 'nid' and 'vid'. Two indexes, one named 'node_changed' on field 'changed' and one named 'node_created' on the field 'created'.

## Creating tables: hook_schema and .install files

For the Schema API to manage a module's tables, the module must have a `.install` file that implements hook_schema(). For example, mymodule's mymodule.install file might contain:

``` php
function mymodule_schema() {
  $schema['mytable1'] = array(
     // specification for mytable1
  );
  $schema['mytable2'] = array(
     // specification for mytable2
  );
  return $schema;
}
```

The tables declared by hook_schema() will be automatically created when the module is first enabled, and removed when the module is uninstalled. This happens before hook_install() is invoked, and after hook_uninstall() is invoked, respectively.

## Module updates using hook_update_N

Updating your module, for example updating your schema, can be done using hook_update_N functions. The API page for this is at: [function hook_update_N](https://api.drupal.org/api/drupal/modules%21system%21system.api.php/function/hook_update_N/7).

Suppose you add a new column called 'newcol' to mytable1. First, be sure to update your schema structure in mymodule_schema() so that newly created tables get the new column. Then, add an update function to mymodule.install:

``` php
function mymodule_update_1() {
  $ret = array();
  db_add_field($ret, 'mytable1', 'newcol', array('type' => 'int'));
  return $ret;
}
```

For D7

``` php
function mymodule_update_1() {
  db_add_field('mytable1', 'newcol', array('type' => 'int'));
}
```

There is also a module available called as [**Schema Module**](http://drupal.org/project/schema) which provides additional Schema-related functionality not provided by the core Schema API that is useful for module developers. Currently, this includes:

- Schema documentation: hyperlinked display of the schema's embedded documentation explaining what each table and field is for.
- Schema structure generation: the module examines the live database and creates Schema API data structures for all tables that match the live database.
- Schema comparison: the module compares the live database structure with the schema structure declared by all enabled modules, reporting on any missing or incorrect tables.

There is also a module available called as [Schemadata](https://www.drupal.org/project/schemadata) which provide a page to display all the mysql table and its data. This module is helpful for developers to save time.

## Converting from Drupal 6 to Drupal 7

This page on conversions from Drupal 6 to Drupal 7, <http://drupal.org/node/224333>, mentions .install in several places. Follow the Drupal 6 .install documentation and include the following changes.  
<http://drupal.org/node/224333#registry>  
<http://drupal.org/node/224333#update_php>  
<http://drupal.org/node/224333#schema_translation>  
<http://drupal.org/node/224333#schema_html>  
<http://drupal.org/node/224333#module_file_during_install>  
<http://drupal.org/node/224333#foreign-keys-added>

## Fields as a replacement

With the Field module, you can add fields to nodes. If the only thing you do in your install file is add fields to nodes by adding a table and some columns, you can now use the Field API, <http://api.drupal.org/api/group/field/7>, and the field hooks. You can search for the field hooks in <http://api.drupal.org/api/7>. Search for `hook_field_`.

hook_field_schema is a hook for adding fields. You can see examples of its use in modules/image/image.field.inc and modules/taxonomy/taxonomy.module. The hook is used in your .module file and might replace the schema in your .install file if you are not adding any other tables. If the only thing in your .install file is a schema, you might not need the .install file.

One other use for the .install file is to delete stuff when someone uninstalls the module. No information yet on how the Field module handles an uninstall.

## Dependencies

When you are installing a module that is dependent on another module, the other module might not be 100% functional. Install and test the other module first. During the alpha and beta stage, you can really only depend on Drupal core modules. Add-on modules can be a long way behind. Even core modules can be a problem so, if you have to switch on extra core modules, switch them on one at a time.

## White screen of death

Drupal and PHP suppress a lot of errors. If your changes to the .install or .info files produce a blank white screen, the dreaded Drupal White Screen of Death, see [Show all errors while developing](http://drupal.org/node/1056468).
