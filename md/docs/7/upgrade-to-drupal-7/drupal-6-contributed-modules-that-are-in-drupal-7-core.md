---
title: "Drupal 6 contributed modules that are in Drupal 7 core"
source_url: "https://www.drupal.org/docs/7/upgrade-to-drupal-7/drupal-6-contributed-modules-that-are-in-drupal-7-core"
page_type: page
last_updated: "Last updated on 18 August 2016"
published: "2010-08-27T14:42:48+00:00"
modified: "2016-08-18T20:20:17+00:00"
breadcrumb: ["Drupal 7", "Upgrade to Drupal 7"]
fetched: "2026-10-21T06:22:22Z"
raw: "raw/docs/7/upgrade-to-drupal-7/drupal-6-contributed-modules-that-are-in-drupal-7-core.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Drupal 6 contributed modules that are in Drupal 7 core

Below is a list of Drupal 6 contributed modules whose functionality now exists wholly or partially in Drupal 7 core.

*Currently this list is a build in progress. In particular, the lists below are not final, and modules may get moved from one list to another as more information becomes available. **Please help by keeping this list up to date when documentation becomes available.** (If you see a mistake, please update the page or drop a note on [this issue](http://drupal.org/node/950672).)*

### Modules that can be uninstalled from your D6 site prior to upgrade

The functionality of these modules is in D7 core, and no major data migration needs to be performed. When upgrading from D6 to D7, you can remove the contributed D6 version from your 'sites' folder. After the upgrade, you may need to reconfigure your D7 settings to reestablish the preferences you had in your D6 site (For some modules with potentially large amounts of settings, we are enquiring with module maintainers on possibility of upgrade path).

- [404 Blocks](http://drupal.org/project/blocks404)
- [Absolute src](http://drupal.org/project/abssrc)
- [Admin:hover](http://drupal.org/project/admin_hover)
- [Admin Role](http://drupal.org/project/adminrole)
- [Archive::Tar](http://drupal.org/project/tar)
- [AHAH helper](http://drupal.org/project/ahah_helper)
- [Already in](http://drupal.org/project/already_in)
- [Autoload](http://drupal.org/project/autoload)
- [Auto Menu Title](http://drupal.org/project/auto_menutitle)
- [AutomaticMenu](http://drupal.org/project/automaticmenu)
- [Auto Menu](http://drupal.org/project/automenu)
- [Block edit](http://drupal.org/project/block_edit)
- [Block Node Visibility](http://drupal.org/project/block_node_visibility)
- [Canonical URL](http://drupal.org/project/canonical_url)
- [Checkbox Validate](http://drupal.org/project/checkbox_validate)
- [Comment Display](http://drupal.org/project/comment_display)
- [DBTNG](http://drupal.org/project/dbtng)
- [Documentation](http://drupal.org/project/documentation)
- [Drupal Queue](http://drupal.org/project/drupal_queue)
- [Edit term](http://drupal.org/project/edit_term)
- [Elements](http://drupal.org/project/elements)
- [Element theme hook](http://drupal.org/project/element_themehook)
- [File API](http://drupal.org/project/hook_file)
- [Filter Default](http://drupal.org/project/filter_default)
- [Image API](http://drupal.org/project/imageapi)
- [Image Cache](http://drupal.org/project/imagecache)
- [Image Field](http://drupal.org/project/imagefield)
- [Input Format Permissions](http://drupal.org/project/input_format_permissions)
- [Javascript Tools](http://drupal.org/project/jstools)
- [jQ](http://drupal.org/project/jq)
- [jQuery Cookie](http://drupal.org/project/jquery_cookie)
- [jQuery Form Update](http://drupal.org/project/jquery_form_update)
- [jQuery Plugin Handler (JQP)](http://drupal.org/project/jqp)
- [jQuery plugin manager](http://drupal.org/project/plugins)
- [jQuery UI](http://drupal.org/project/jquery_ui)
- [JS Alter](http://drupal.org/project/jsalter)
- [Login Security](http://drupal.org/project/login_security)
- [Menuless Node Type](http://drupal.org/project/menuless_nodetype)
- [Menu Settings per Content Type](http://drupal.org/project/ctm)
- [No Anonymous Sessions](http://drupal.org/project/no_anon)
- [Node Preview by Content type](http://drupal.org/project/nodepreview_by_type)
- [Parallel](http://drupal.org/project/parallel)
- [Permissions API](http://drupal.org/project/permissions_api)
- [Plugin Manager](http://drupal.org/project/plugin_manager)
- [Poor man's cron](http://drupal.org/project/poormanscron)
- [Preview](http://drupal.org/project/preview)
- [RDF](http://drupal.org/project/rdf)
- [Secure Password Hashes (phpass)](http://drupal.org/project/phpass)
- [Shortlink](http://drupal.org/project/shortlink)
- [Simple CDN](http://drupal.org/project/simplecdn)
- [Simpletest](http://drupal.org/project/simpletest)
- [Site Configuration Permissions](http://drupal.org/project/config_perms)
- [Storage API](http://drupal.org/project/storage_api)
- [Taxidermy](http://drupal.org/project/taxidermy)
- [TinyMCE AHAH Integration](http://drupal.org/project/tinymce_ahah)
- [TinyMCE Drag and Drop Integration](http://drupal.org/project/tinymce_dragdrop)
- [Transaction](http://drupal.org/project/transaction)
- [Upload element](http://drupal.org/project/upload_element)
- [Upload preview](http://drupal.org/project/upload_preview)
- [URL alter](http://drupal.org/project/url_alter)
- [User Cancellation](http://drupal.org/project/user_cancellation)
- [User Default Filter](http://drupal.org/project/user_default_filter)
- [User Delete](http://drupal.org/project/user_delete)
- [Vertical Tabs](http://drupal.org/project/vertical_tabs)
- [View unpublished](http://drupal.org/project/view_unpublished)
- [Vocabulary Permissions](http://drupal.org/project/vocabperms)
- [Wysiwyg API CCK Integration](http://drupal.org/project/wysiwygcck)

### Modules that may also be uninstalled, depending on the functionality you require

These modules have part of their functionality in D7 core, but a contrib module will still exist to handle the remaining functionality. If you don't need this additional functionality, you can uninstall the module.

- [Token](http://drupal.org/project/token)  
  - there will still be a D7 contrib module to handle UI, as well as field and profile tokens
- [Better Formats](http://drupal.org/project/better_formats) - d7 contrib module still control per role display of: format tips, format tips link and format selection for \[entity\]

### Modules that require data migration

During core upgrade, you can leave the D6 module where it is. Before migrating data, you should first go through all the upgrade steps for core as described in your UPGRADE.txt, and then install the D7 contrib modules that will handle the migration.

- [Content Construction Kit (CCK)](http://drupal.org/project/cck)  
  - There is a D7 contrib module to handle miscellaneous field functions - it includes the Content Migrate submodule to handle D6-\>D7 data migration. Node and user references have been split off into the [References](http://drupal.org/project/references) module. [Content permissions](http://drupal.org/project/field_permissions), [fieldgroups](http://drupal.org/project/field_group) and content copy will be hived off into their own separate modules.
- [Content Taxonomy](http://drupal.org/project/content_taxonomy) - - Will need to migrate data: on the module page it says there will be an upgrade path provided.
- [Date Timezone](http://drupal.org/project/date) - This is a submodule of the Date module. Replacing the D6 version of the date module with the D7 version and performing any required upgrades for that module will suffice here.
- [Features](http://drupal.org/project/features) - This module makes Drupal configurables such as content types, CCK fields, image cache presets, taxonomy vocabularies and views exportable in module format. Before you can upgrade these "feature modules". You need to consolidate their content into the database. This needs to be done before the D7 upgrade is started. Once consolidated, the upgrade itself is handled by the core and contrib modules relevant to the feature exportables (ie: CCK, Imagecache, Taxonomy, Views, etc)
- [Field Taxonomy](http://drupal.org/project/field_taxonomy) - Will need to migrate data: so far, no indication on the module page of an upgrade path.
- [Filefield/Imagefield](http://drupal.org/project/filefield) - A preliminary version of an upgrade path is provided in the Content Migrate submodule of cck (see above).
- [Image](http://drupal.org/project/image) - the image nodes will need to be migrated to FieldAPI using [Field Converter module](http://drupal.org/project/field_convert). Some functionality (e.g. import) will still exist in contrib in separate modules.
- [Taxonomy Delegate](http://drupal.org/project/taxonomy_delegate) - may need to migrate delegation: so far, no indication on the module page of an upgrade path, although they are following D7 progress.
- [Taxonomy Intro](http://drupal.org/project/taxonomy_intro)  
  - Will need to migrate introduction field: so far, no indication on the module page of an upgrade path.
- [Term fields](http://drupal.org/project/term_fields) - Will need to migrate data: so far, no indication on the module page of an upgrade path.
