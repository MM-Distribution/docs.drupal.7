---
title: "Converting 6.x modules to 7.x"
source_url: "https://www.drupal.org/docs/7/converting-drupal-6-modules-to-drupal-7/converting-6x-modules-to-7x"
page_type: page
last_updated: "Last updated on 15 October 2016"
published: "2008-02-20T14:38:45+00:00"
modified: "2016-10-15T22:13:12+00:00"
breadcrumb: ["Drupal 7", "Converting Drupal 6 modules to Drupal 7"]
fetched: "2026-10-21T07:50:11Z"
raw: "raw/docs/7/converting-drupal-6-modules-to-drupal-7/converting-6x-modules-to-7x.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Converting 6.x modules to 7.x

## Overview of Drupal API changes in 7.x

**NOTE**: This page is locked to further edits (only people with node admin rights can edit it). The reason is that we are now using a different system to track version-to-version changes in Drupal. Most of the API changes between Drupal 6 and Drupal 7 are noted on this page, but changes that were recorded after we adopted the new system can be found here:  
<http://drupal.org/list-changes/drupal>  
To add a new change notice:  
<http://drupal.org/node/add/changenotice>

### How to Use this Guide

The changes required for updating a module from Drupal 6 to Drupal 7 are listed below in chronological order, grouped according to the pre-version release of Drupal 7 in which each change occurred. For example, changes that were introduced in the September 30, 2008 "UNSTABLE-1" release of Drupal 7 are listed below the subhead titled, "UNSTABLE-1 (2008-Sep-30)."

There is also a separate "[Categorical](/node/394070)" change list that organizes the list of changes by category, e.g., changes to the database API, changes to the menu system, blocks, comments, etc.

Each change listed in either the chronological list or the categorical list links to a detailed explanation of how to implement that change in your module. The detailed explanations appear on this instruction page, below the chronological list. If you are not interested in using the chronological list or the categorical list, you can simply go the [beginning of the detailed explanations](#detailed_change_instructions) and begin working through them.

There is also a "[Coder project](http://drupal.org/project/coder) that can help automate the process of converting your modules from D6 to D7. The [Categorical list](/node/394070) provides further information about how the Coder project can be used to review and update your code.

#### Changes related to modules that were not part of Drupal 6 core

Note: This page does **not** cover upgrades from modules that were contributed in Drupal 6 and are part of core in Drupal 7. These are documented on separate pages (if at all). Pages we know about:

- CCK - If you are upgrading a Drupal 6 CCK field module to Drupal 7, check out the [CCK field module update guide](http://drupal.org/node/728792).
- Token - Check out the [Token 6/7 API changes page](http://drupal.org/documentation/modules/token/update/6/7)

#### Missing documentation

This page is a work in progress and not every API change in Drupal 7 is covered here yet. If you are unable to find update documentation for something you feel should be here, please check the [list of issues with outstanding upgrade documentation](http://drupal.org/project/issues/search/drupal?status%5B%5D=Open&issue_tags_op=or&issue_tags=Needs+Update+Documentation). If you are unable to find the relevant issue there, please search core issues, update an existing one with the 'Needs Update Documentation' tag, or open a new one (and tag appropriately).

#### Annotation

- \[X\] indicates a change that has been cross-referenced in the [Categorical](/node/394070) change list.

### UNSTABLE-1 (2008-Sep-30)

1.  \[X\] [Drupal 7 requires PHP 5.2 or higher](#php_version)
2.  \[X\] [Permissions have titles (required) and descriptions (optional)](#descriptions_permissions)
3.  \[X\] [Permissions are no longer sorted alphabetically](#sorting_permissions)
4.  \[X\] [\_comment_load() is now comment_load()](#comment_load)
5.  \[X\] [Module .info files must now specify all loadable code files explicitly](#registry)
6.  \[X\] [~~The hook_menu() and hook_theme() "file" and "file path" keys have been removed~~](#menu_file_path)
7.  \[X\] [New permission tables](#permission_tables)
8.  \[X\] [Use '#markup' not '#value' for markup](#markup)
9.  \[X\] [Comment status values in the database have flipped so they match node status](#comment_status)
10. \[X\] [Rebuild functions have changed names](#rebuild_functions)
11. \[X\] [Use defined constant REQUEST_TIME instead of time()](#time)
12. \[X\] [referer_uri() has been removed](#referer_uri)
13. \[X\] [Some \#process functions have been renamed](#process_functions)
14. \[X\] [A completely new database API has been added](#dbtng)
15. \[X\] [file_validate_extensions() enforces check for uid=1](#file_validate_extensions)
16. \[X\] [file_scan_directory() and drupal_system_listing() use preg regular expressions](#preg_match)
17. \[X\] [Easier check for node form during hook_form_alter()](#node_form)
18. \[X\] [Update functions in .install files must include a Doxygen style comment](#update_php)
19. \[X\] [Replace drupal_clone() with clone](#drupal_clone)
20. \[X\] [Session functions are renamed.](#session_rename)

### UNSTABLE-2 (2008-Oct-11)

1.  \[X\] [Permissions have titles (required) and descriptions (optional)](#descriptions_permissions)
2.  \[X\] [hook_nodeapi, hook_node_type, hook_user, and hook_block removed and replaced with families of related functions](#remove_op)
3.  \[X\] [In hook_node_info() change 'module' back to 'base' and change 'node' to 'node_content'](#node_type_base)
4.  \[X\] [Use absolute path (constructed from DRUPAL_ROOT) when including a file](#absolute_includes)
5.  \[X\] [File API reworked, stream notation required, file_unmanaged\_\* functions](#unmanaged_files)
6.  \[X\] ["administer nodes" permission split into "administer nodes", "access content overview", and "bypass node access"](#bypass_node_access)
7.  \[X\] [New hooks: hook_modules_installed, hook_modules_enabled, hook_modules_disabled, and hook_modules_uninstalled](#hook_modules_action)
8.  \[X\] [drupal_uninstall_module() is now drupal_uninstall_modules()](#drupal_uninstall_modules)

### UNSTABLE-3 (2008-Nov-11)

1.  \[X\] [drupal_set_title() uses check_plain() by default](#drupal_set_title)
2.  \[X\] [Changed parameters for drupal_add_js() and drupal_add_css()](#drupal_add_js_options)
3.  \[X\] [Changed Drupal.behaviors to objects having the properties 'attach' and 'detach'](#drupal_behaviors)
4.  \[X\] [Taxonomy CRUD functions renamed and refactored](#taxonomy_crud)
5.  \[X\] [New taxonomy hooks for term and vocabulary](#taxonomy_hooks)
6.  \[X\] [Removed file_set_status()](#file_set_status)
7.  \[X\] [Replace 'core', 'module' and 'theme' with 'file' in drupal_add_js()](#drupal_add_js_weight)
8.  \[X\] [Parameters to check_markup() have changed, default format change](#check_markup_params)

### UNSTABLE-4 (2009-Jan-8)

1.  \[X\] [Schema descriptions are no longer translated](#schema_translation)
2.  \[X\] [file_scan_directory() now uses a preg regular expression for the nomask parameter](#file_scan_directory_nomask)
3.  \[X\] [Use module_implements not module_list when calling hook implementations](#module_implements_not_module_list)
4.  \[X\] [New hook_js_alter to alter JavaScript](#hook_js_alter)
5.  \[X\] [Changed log out path from 'logout' to 'user/logout' for consistency](/node/719612) Note: Link goes to separate sub-page!
6.  \[X\] [node_load() and node_load_multiple()](#node_load_multiple)
7.  \[X\] [taxonomy_term_load() and taxonomy_term_load_multiple()](#taxonomy_term_load_multiple)
8.  \[X\] [file_load_multiple()](#file_load_multiple)
9.  \[X\] [Taxonomy CRUD functions renamed and refactored](#taxonomy_crud)
10. \[X\] [New taxonomy hooks for term and vocabulary](#taxonomy_hooks)
11. \[X\] [Code documentation added to module.api.php](#api_php)
12. \[X\] [taxonomy_get_tree()](#taxonomy_get_tree)
13. \[X\] [Move node, taxonomy, and comment links into \$node-\>content; Deprecate hook_link()](#node_links)
14. \[X\] [hook_nodeapi, hook_node_type, hook_user, and hook_block removed and replaced with families of related functions](#remove_op)
15. \[X\] [Parameters for actions_synchronize() have changed](#actions_synchronize)
16. \[X\] [Parameters for drupal_http_request() have changed](#drupal_http_request_parameters)
17. \[X\] [db_rewrite_sql() replaced with hook_query_alter()](#db_rewrite_sql)
18. \[X\] [Removed FILE_STATUS_TEMPORARY](#remove_FILE_STATUS_TEMPORARY)
19. \[X\] [New user_cancel API](#user_cancel)
20. \[X\] [Taxonomy db table names have changed to begin with 'taxonomy\_'](#taxonomy_tables)

### UNSTABLE-5 (2009-Jan-26)

1.  \[X\] [User pictures are now managed files](#user_picture)
2.  \[X\] [drupal_set_session() replaces \$\_SESSION](#drupal_set_session) \[NOT ANYMORE\]
3.  \[X\] [Ability to reset JavaScript and CSS](#drupal_add_js_css_reset)
4.  \[X\] [Moved statistics settings from admin/reports/settings to ~~admin/settings/statistics~~ admin/config/system/statistics and added a new 'administer statistics' permission](#moved_statistics_settings)
5.  \[X\] [Default parameter when getting variables](#variable_get_default_null)
6.  \[X\] [Menu "page callbacks" and blocks should return an array and hook_page_alter() (Render arrays discussion)](#menu_callback_array)
7.  \[X\] [Block module now optional](#block_optional)
8.  \[X\] [Element \#type property no longer treated as a theme function in drupal_render()](#element_theme_properties)
9.  \[X\] [Use drupal_render_children() to render an element's children](#drupal_render_children)
10. \[X\] [~~Replace node_view() with node_build()~~](#node_view)

### UNSTABLE-6 (2009-Mar-14)

1.  \[X\] [JavaScript should be compatible with libraries other than jQuery](#javascript_compatibility)
2.  \[X\] [file_scan_directory()'s optional parameters are now an array](#file_scan_directory_array_itize)
3.  \[X\] [External JavaScript can now be referenced through drupal_add_js()](#drupal_add_js_external)
4.  \[X\] [user_load_multiple() and hook_user_load(), user_load() signature change, and \$reset parameter](#user_load_multiple)
5.  \[X\] [jQuery 1.3.x](#jquery_13)
6.  \[X\] [Settings passed locally to JavaScript Behaviors](#local_settings_behaviors)
7.  \[X\] [file_scan_directory() now uses same property names as file_load()](#file_scan_directory_property_names)

### UNSTABLE-7 (2009-May-21)

1.  \[X\] [Moved filter module administrative URLs from admin/settings/filters/\* to admin/settings/filter/\*](#filter_urls)
2.  \[X\] [Added taxonomy_vocabulary_load_multiple()](#vocabulary_load_multiple)
3.  \[X\] ~~[Added a new top-level 'international' admin menu item](#international_item)~~
4.  \[X\] [Changed hook_menu_link_alter() (removed the \$menu parameter)](#hook_menu_link_alter)
5.  \[X\] [Standardized API for static variables and resetting them](#static_variable_api)
6.  \[X\] [The function drupal_set_html_head() has been renamed to drupal_add_html_head()](#drupal_set_html_head)
7.  \[X\] [Inline cascading stylesheets from drupal_add_css()](#drupal_add_css_inline)
8.  \[X\] [Attached JavaScript and CSS for forms](#attached_js)
9.  \[X\] [Make sticky tableheaders optional](#sticky_headers)
10. \[X\] [Save new users and nodes with specified IDs](#specified_ids)
11. \[X\] [Parameters swapped in book_toc()](#book_toc_parameters)
12. \[X\] [drupal_execute() renamed to drupal_form_submit()](#drupal_execute_drupal_form_submit)
13. \[X\] [node_invoke_nodeapi() removed](#node_invoke_nodeapi)
14. \[X\] [Removed \$op "rss item" from hook_nodeapi() in favor of 'rss' view mode](#node_build_rss)
15. \[X\] [drupal_eval() renamed to php_eval](#php_eval)
16. \[X\] ["use PHP for settings" permission should be used for all PHP settings rights (replaces "use PHP for block visibility")](#php_permissions)
17. \[X\] [Changes to HTTP header functions](#http_header_functions)
18. \[X\] [drupal_get_form() returns a render array instead of a string](#unrendered)
19. \[X\] [Add Doxygen @file tag to all install files](#afile)
20. \[X\] [Add node_delete_multiple()](#delete_multiple)
21. \[X\] [Renamed drupal_set_content() and drupal_get_content()](#drupal_set_content)
22. \[X\] [Instead of theme('page', ...), think of drupal_set_page_content()](#theme_page)
23. \[X\][theme('box') no longer exists](#theme_box)
24. \[X\][Node Body and Teaser Changes](#body_teaser_fields)

### UNSTABLE-8 (2009-Jul-21)

1.  \[X\] [Node access hooks now have drupal_alter() functions](#node_access_alter_hooks)
2.  \[X\] [~~Hide empty menu categories with access callback~~](#system_admin_menu_block_access)
3.  \[X\] [Commenting style - use 'Implements hook_foo().' when documenting hooks](#implementation_hook_comment)
4.  \[X\] [node_get_types(\$op) replaced by node_type_get\_\$op()](#node_type_get_functions)
5.  \[X\] [Added hook_block_info_alter()](#hook_block_info_alter)
6.  \[X\] [Renamed module_rebuild_cache() to system_rebuild_module_data(), renamed system_theme_data() to system_rebuild_theme_data(), and added system_get_info()](#system_rebuild_module_data)
7.  \[X\] [Added string context support to t() and format_plural(), changed parameters](#locale_context)
8.  \[X\] [Alternative cache implementations changed](#cache_implementation)
9.  \[X\] [\$teaser parameter changed to \$view_mode in node viewing functions and hooks, \$node-\>build_mode property removed](#view_mode)
10. \[X\] [comment_save() now supports programmatic saving](#comment_save_refactor)
11. \[X\] [comment_validate() has been removed](#comment_validate_removed)
12. \[X\] [Login validation change for distributed authentication modules](#distauth)
13. [Some login validation functions were removed or changed](#login-funcs)
14. \[X\] [jQuery UI (1.7) was added into core](#jquery_ui)
15. \[X\] [comment_node_url() has been removed](#comment_node_url)
16. \[X\] [\#theme recommended for specifying theme function](#poundtheme)
17. \[X\] [hook_perm() renamed to hook_permission()](#hook_permission)
18. \[X\] [Ability to add multiple JavaScript/CSS files at once](#drupal_add_library)
19. \[X\] [Removed taxonomy module support for multiple tids and depth in term paths](#taxonomy_paths)
20. \[X\] [file_prepare_directory() (replacement for file_check_directory() will now recursively create directories](#file_check_directory_recursive)
21. \[X\] [Added comment_load_multiple() and hook_comment_load()](#comment_load_multiple)
22. \[X\] [hook_node_access_records() now applies to unpublished nodes; 'view own unpublished content' permission added](#hook_node_access_records)
23. \[X\] [New tar archive library added](#archive-tar)
24. \[X\] [hook_elements() renamed to hook_element_info()](#hook_element_info)
25. \[X\] [Blog API module removed from Drupal core](#remove-blogapi)
26. \[X\] [drupal_urlencode() replaced by drupal_encode_path()](#remove-drupal-urlencode)
27. \[X\] [Two page caching functions renamed](#page-cache-rename)
28. \[X\] [MIME types list changed from variable to alter hook/function](#mime-types)

### UNSTABLE-9 (2009-Sep-9)

1.  \[X\] [hook_footer() was removed, \$closure became \$page_bottom, \$page_top added](#hook_footer)
2.  \[X\] [Schema descriptions are now plain text instead of HTML](#schema_html)
3.  \[X\] [Related terms functionality was removed from taxonomy.module](#related_terms)
4.  \[X\] [db_result() has been removed; use -\>fetchField() instead](#db_result)
5.  \[X\] [Do not use SELECT COUNT(\*) to check for existence of rows in a table](#select_count)
6.  \[X\] [Added drupal_set_time_limit()](#time_limit)
7.  \[X\] [Module .info files can now optionally specify the version number of the module it depends on](#module_version_dependencies)
8.  \[X\] [hook_nodeapi_xxx() becomes hook_node_xxx()](#hook_node_xxx)
9.  \[X\] [.module file available during install](#module_file_during_install)
10. \[X\] [Parameters to function user_authenticate() changed](#user_authenticate)
11. \[X\] [JavaScript variable Drupal.jsEnabled has been removed](#no-jsenabled)
12. \[X\] [~~xmlrpc() wrapper function removed~~](#xmlrpc-wrapper)
13. \[X\] [Foreign keys added to core database table schema](#foreign-keys-added)
14. \[X\] [Removed several unnecessary arguments to various hook_user\_\$op hooks and removed hook_profile_alter](#hook-user-changes)
15. \[X\] [Many paths to admin screens have changed](#admin_path_changes)
16. \[X\] [hook_nodeapi, hook_node_type, hook_user, and hook_block removed and replaced with families of related functions](#remove_op)
17. \[X\] [drupal_add_css() now supports external CSS files](#add-css-external)
18. \[X\] [New hook_comment_presave() for comments](#comment_presave_hook)
19. \[X\] [Weighting of stylesheets](#drupal_add_css_weight)
20. \[X\] [AHAH/AJAX Processing has changed; \#ajax, new 'callback' member of the array, and the callback must be rewritten](#ahah-now-ajax)
21. \[X\] [hook_access() removed in favor of hook_node_access()](#hook_node_access)
22. \[X\] [hook_filter() and hook_filter_tips() replaced by hook_filter_info()](#hook_filter_info)
23. \[X\] [Convert class attributes to array in favor of a string](#class_attribute_array)
24. \[X\] ~~[Schema API now supports date and time types natively](#schema_date_time)~~
25. \[X\] [Added API functions for creating, loading, updating, and deleting user roles and permissions](#user-roles-api)
26. \[X\] [New hook: hook_file_url_alter()](#hook_file_url_alter)
27. \[X\] [jQuery Once method for applying JavaScript behaviors once](#jquery_once)
28. \[X\] [Database schema (un)installed automatically](#install-schema)
29. \[X\] [User 1 is now called *site maintenance account*](#user-1)
30. \[X\] [CRUD hooks for menu links: hook_menu_link_insert(), hook_menu_link_update(), hook_menu_link_delete()](#menu-link-hooks)
31. \[X\] [Default text formats have been revamped](#default-text-formats)
32. \[X\] [Text formats access is now controlled by permissions, and filter_access() parameters have changed](#text-format-permissions)
33. \[X\] [The parameters to filter_formats() have changed](#filter_formats_parameters)
34. \[X\] [Rename drupal_to_js() and drupal_json() to drupal_json_encode() and drupal_json_output()](#rename-drupal-to-js)
35. \[X\] [theme_links() has a new parameter 'heading' for accessibility](#theme-links-param)
36. \[X\] [API for modules providing search has changed](#search-api)
37. \[X\] [All taxonomy functions relating to nodes have been removed or refactored](#taxonomy_node)
38. \[X\] [Added hook_entity_load()](#hook_entity_load)
39. \[X\] [All e-mails are considered to originate as HTML](#email-html)
40. \[X\] [file_check_directory() renamed to file_prepare_directory()](#file_prepare_directory)
41. \[X\] [Block Cache constants renamed to DRUPAL_CACHE](#block_cache-constancts)
42. \[X\] [File API: \$file-\>filepath renamed to \$file-\>uri](#file-object)
43. \[X\] [HTML rendering of form elements has different CSS classes](#css-no-wrappers)
44. \[X\] [Form element value callbacks now always have \$form_state argument](#value-callback-state)
45. \[X\] [Changes to how Drupal sends email](#mail-sending)

### UNSTABLE-10 (2009-Nov-2)

1.  \[X\] [Trigger and Actions API overhaul](#trigger_overhaul)
2.  \[X\] [theme() now takes only two arguments](#theme_changes)
3.  \[X\] [hook_theme() requires "variables" or "render element" instead of "arguments" to better integrate with drupal_render()](#hook_theme_render_changes)
4.  \[X\] [drupal_alter() now takes at most 3 parameters by reference](#drupal_alter)
5.  \[X\] [The \$ret parameter has been removed from all Schema operations](#schema_ret)
6.  \[X\] [Update hooks now return strings or throw exceptions, and update_sql() is no more](#update_sql)
7.  \[X\] [The signature of the callback from drupal_get_form() changed to add \$form](#hook_forms_signature)
8.  \[X\] [Replaced taxonomy_term_path(), hook_term_path(), language_url_rewrite(), and custom_url_alter_outbound() with hook_url_outbound_alter()](#hook_url_outbound_alter)
9.  \[X\] [Replaced custom_url_rewrite_inbound() with hook_url_inbound_alter()](#hook_url_inbound_alter)
10. \[X\] [hook_load() signature and return value change](#hook_load_signature)
11. \[X\] [Renamed menu_path_is_external() to url_is_external()](#url_is_external)
12. \[X\] [Comment.timestamp split into 'created' and 'changed'](#comment_created_changed)
13. \[X\] [New entity_info_cache_clear() API function](#entity_info_cache_clear)
14. \[X\] [Permissions have titles (required) and descriptions (optional)](#descriptions_permissions)
15. \[X\] [Custom menu API](#custom_menu_api)
16. \[X\] ~~[drupal_set_header() and drupal_get_header() renamed to drupal_add_http_header() and drupal_get_http_header()](#drupal_set_header_renamed)~~
17. \[X\] [New hook_hook_info() added](#new_hook_hook_info)
18. \[X\] [Taxonomy synonyms have been removed](#no-synonyms-taxonomy)
19. \[X\] [drupal_goto() follows parameters of url()](#drupal_goto_params)
20. \[X\] [hook_user_form(), hook_user_register() are gone](#hook_user_form_register_gone)
21. \[X\] [hook_user_validate() and hook_user_submit() are gone](#hook_user_validate_gone)
22. \[X\] [hook_user_after_update() replaced by hook_user_update(), amended by hook_user_presave() for common operations](#hook_user_after_update)
23. \[X\] [url() 'query' field must be array](#url_query_parameter)
24. \[X\] [Query string functions renamed](#get_querystring)

### ALPHA1 (2010-Jan-15)

1.  \[X\] [New hooks: hook_admin_paths() and hook_admin_paths_alter()](#hook_admin_paths)
2.  \[X\] [theme('placeholder') replaced by drupal_placeholder()](#placeholder)
3.  \[X\] [The function menu_valid_path() has been renamed to drupal_valid_path(), and its inputs have changed](#drupal_valid_path)
4.  \[X\] [Language neutral content now has an explicit language associated with it](#drupal_language_none)
5.  \[X\] [New API function: format_username() and new hook: hook_username_alter()](#format_username)
6.  \[X\] [Functions called very often that need a drupal_static() variable can use an optimized way of calling that function](#drupal_static_advanced)
7.  \[X\] [A theme hook name followed by a double underscore ('\_\_') is a default 'pattern'](#theme_hook_suggestions_1)
8.  \[X\] [Preprocess functions need to now specify "theme_hook_suggestion(s)" instead of "template_file(s)"](#theme_hook_suggestions_2)
9.  \[X\] [Use \#theme='links\_\_MODULE' or \#theme='links\_\_MODULE_EXTRA_CONTEXT' when adding links to a render array](#theme_links_with_context)
10. \[X\] [Use \#type='link' for adding a single link to a render array, particularly for tables that include operation links like 'edit', 'delete', etc.](#operation_links)
11. \[X\] [Added entity_prepare_view() and hook_entity_prepare_view()](#entity_prepare_view)
12. \[X\] [New pattern for cross-database, performant, case-insensitive comparisons](#nomorelower)
13. \[X\] [Comment rendering overhaul](#comment_render)
14. \[X\] [taxonomy_form_all() removed](#taxonomy_form_all)
15. \[X\] [Module .info files can have configure line](#configure_info)
16. \[X\] [Forms are no longer automatically rebuilt when \$form_state\['storage'\] is set](#form-auto-rebuild)

### ALPHA2 (2010-Feb-21)

1.  \[X\] [New method for altering the theme used to display a page (global \$custom_theme variable removed)](#custom_theme)
2.  \[X\] [New update dependency system, affecting the order in which module updates are run](#update_dependencies)
3.  \[X\] [Block tables renamed](#block_tables_renamed)
4.  \[X\] [Block deltas are now specified as strings](#block_deltas_renamed)
5.  \[X\] [taxonomy_term_view() and taxonomy-term.tpl.php for term display](#taxonomy_term_view)
6.  \[X\] [Changed Clean URLs and Search settings page path](#clean_urls_search_paths)
7.  \[X\] [Function menu_tree_data() now expects an array of links instead of a query results](#menu_tree_data)
8.  \[X\] [hook_update_index() only runs when searching enabled for a given module](#hook_update_index)
9.  \[X\] [Format date types "small" and "large" have been changed to "short" and "long"](#format_date)
10. \[X\] ["Boxes" have been renamed to "custom blocks"](#custom_block)
11. \[X\] [Remove moderate column from node_schema()](#moderate_column)
12. \[X\] [theme_pager() no longer takes limit parameter](#theme_pager)
13. \[X\] [theme_username() parameters changed](#theme_username)
14. \[X\] [form_clean_id() has been renamed to drupal_html_id()](#form_clean_id)
15. \[X\] [New \#type 'text_format' for text format-enabled form elements](#text_format)

### ALPHA 3 (2010-Mar-21)

1.  \[X\] [New language negotiation API introduced](#language_negotiation)
2.  \[X\] [HTTP Status code setting with drupal_add_http_header() changed (on top of a previous API change)](#http_header_functions)
3.  \[X\] [WATCHDOG_EMERG was renamed to WATCHDOG_EMERGENCY](#watchdog_emerg)
4.  \[X\] [system_retrieve_file() API cleanup](#system_retrieve_file)
5.  \[X\] [menu_default_node_menu replaced with per-content type settings](#menu_default_node_menu)
6.  \[X\] [COMMENT_NODE\_\* constants have new names, but same values](#comment_node)
7.  \[X\] [Drupal.parseJson has been removed and replaced with jQuery.parseJSON.](#Drupal.parseJSON)

### ALPHA 4 (2010-Apr-27)

1.  \[X\] [New 'restrict access' parameter in hook_permission() for labeling unsafe permissions](#permissions_restrict_access)
2.  \[X\] [Removal of FAPI \$form\['#redirect'\] and \$\_REQUEST\['destination'\]](#fapi_changes)
3.  \[X\] [User-configured time zones now serve as the default time zone for PHP date/time functions](#date_default_timezone)
4.  \[X\] [db_is_active() has been removed](#db_is_active)
5.  \[X\] [Node body field now requires normal field API usage](#body_field)
6.  \[X\] [Rename file to file_managed](#file_file_managed)
7.  \[X\] [New hook_module_implements_alter](#hook_module_implements_alter)
8.  \[X\] [Database prefixes are now per-connection](#db_prefix)
9.  \[X\] [Form submit buttons consistently grouped in actions array](#actions_buttons)
10. \[X\] [New constants for user registration settings, and the default has been changed to "Visitors, but administrator approval is required"](#changed_user_default)
11. \[X\] [hook_form_alter and hook_form_FORM_ID_alter run together for each module](#form_alter_change)
12. \[X\] [Arguments to xmlrpc() have changed](#xmlrpc)
13. \[X\] [Translatable Fields](#translatable_fields)
14. \[X\] [Filter table updates](#filter_update)

### Beta 1 (6 Oct 2010) - may include Alpha 5-7

1.  \[X\] [file_directory_path() has been removed](#file_directory_path)
2.  \[X\] [hook_form_BASE_FORM_ID_alter() is invoked for shared form constructors](#hook_form_BASE_FORM_ID_alter)
3.  \[X\] ['comment_form' form ID changed to 'comment_node_TYPE_form'](#comment_form)
4.  \[X\] [Text formats (input formats) must be defined](#text_format_updates)
5.  \[X\] [Text format (input format) identifier is now a machine name](http://drupal.org/node/224333#text_format_string)
6.  \[X\] [Arbitrary user data is harder to stash in the user object](#user_data_change)
7.  \[X\] [Two new functions added: hook_page_build() and hook_page_alter()](#hook_page)
8.  \[X\] [Javascript and CSS loading changes](#js_css_loading_change)
9.  \[X\] [Node, filter and comment modules tables renamed to singular](#table_names)
10. \[X\] ['post comments without approval' permission name changed](#comment_perms)
11. \[X\] [MENU_CALLBACK meaning has changed for breadcrumbs, and some other menu API changes](#menu_breadcrumb)

### BETA 2 (22 Oct 2010)

1.  \[X\] [The *datetime* field type has been removed in favour of database engine specific types](#db_specific_types)
2.  \[X\] [l() function class attribute](#l_function)

### 7.0 full release (4 Jan 2011) - May include Beta 3 or RC1 or RC2

1.  \[X\] [New 'properties' element of block information](#block_properties)

### UNKNOWN

These changes were introduced somewhere in the 7.x development cycle, but we're not sure exactly when, sorry!

1.  \[X\] [\$element\['#post'\] is gone](#element_post)
2.  \[X\] [node_load() and other entity loading cache behavior has changed](#load_cache)
3.  \[X\] [\$form_state\['clicked_button'\] is deprecated, use \$form_state\['triggering_element'\] instead](#clicked_button)

### 7.4

Changes introduced with 7.4.

1.  \[X\] [Database driver prefix handling has changed](#driver_prefixes)

### Cross Reference Instructions

Before placing an \[X\] on an item in the chronological list above, please do the following:

- Add a cross-referencing item in the [Categorical](/node/394070) change list.
- Add an issue to the [Coder Upgrade issue queue](http://drupal.org/project/issues/coder?text=&status=Open&priorities=All&categories=All&version=All&component=Upgrade+Routines). The title of the issue should match the title herein and the body should contain a link to the details on this page. Refer to existing issues in this queue for examples.

## Detailed Change Instructions

### Drupal 7 requires PHP 5.2 or higher

Drupal 7 now requires PHP 5.2 or higher, so you can safely use and rely on PHP 5.2 functions and features in your modules. In particular, PHP 5 always passes objects into functions by reference; this includes objects inside arrays (the array is not passed by reference, but the objects inside the array are references). This means that you can omit the & to indicate passing by reference in function arguments if the argument is either an object or an array of objects. However, if the argument is an array of objects and you need to add or remove elements to the array rather than just modify objects within the array, you will still need the & so that the array will be passed by reference.

Example - Drupal 6:

``` php
mymodule_nodeapi(&$node, $op, $a3 = NULL, $a4 = NULL) {
  if ($op == 'load') {
    $node->mymodule_special = 'my value';
  }
}
```

Drupal 7:

``` php
mymodule_node_load($nodes, $types) {
  foreach ($nodes as $node) {
    $node->mymodule_special = 'my value';
  }
}
```

### Permissions have titles (required) and descriptions (optional)

[(issue)](http://drupal.org/node/30984) released in UNSTABLE_1, [(issue)](http://drupal.org/node/313213) released in UNSTABLE_2 and [(issue)](http://drupal.org/node/601586) released in UNSTABLE_10. In the implementation of [hook_permission()](http://api.drupal.org/api/function/hook_permission/7), the returned array format changed.

Drupal 6 supported this format:

``` php
function example_perm() {
  return array('administer my module', ...);
}
```

Drupal 7 code should use the following format:

``` php
function example_permission() {
  return array(
    'administer my module' => array(
      'title' => t('Administer my module'),
      'description' => t('Perform maintenance tasks for my module'),
    ),
    ...
  );
}
```

Previously, the values were the permission names; now permission names are the keys and the corresponding value is an array with permission title and description. If you happen to have composite permission names, which contain dynamic values such as content type names, look at the array format generated by [node_list_permissions()](http://api.drupal.org/api/function/node_list_permissions/7) which is reused by [node_permission()](http://api.drupal.org/api/function/node_permission/7) and hook_permission() implementations of other core node modules. Note that titles are required, but descriptions are optional. You are encouraged only to use descriptions if you need to tell users something you cannot do using a title only.

There is also an additional key ('restrict access') that can be added to the permission array in rare cases; this is intended for labeling unsafe permissions and is described [below](#permissions_restrict_access).

**NB.** While no API changes are involved, user.module will now remove permissions automatically when a module is uninstalled.

### Permissions are no longer sorted alphabetically

[(issue)](/node/108979) Permissions are no longer sorted alphabetically, but are displayed in the order defined in your hook_permission().

The recommended order for permissions is:

1.  administer-related permissions
2.  access-related permissions
3.  other global-level permissions
4.  create-related permissions
5.  edit-related permissions
6.  delete-related permissions
7.  other

### \_comment_load() is now comment_load()

[(issue)](http://drupal.org/node/195072) \_comment_load() was renamed to comment_load() as it is an external-facing API function.

In addition to the function name itself, any menu items that are using the %\_comment wildcard will need to change to %comment.

### Module .info files must now specify all loadable code files explicitly

[(issue)](/node/221964) and [partial roll-back](/node/497118). Drupal now supports a dynamic-loading code registry for classes and interfaces. To support it, all modules must declare files containing classes and interfaces in the .info file like so:

``` php
name = Menu
description = Allows administrators to customize the site navigation menu.
...
files[] = menu.test
```

When a module is enabled, Drupal will rescan all declared files and index all classes and interfaces it finds. That means any class or interface code can live outside the .module file, and it will be included on-demand. Classes will be loaded automatically by PHP when they are first accessed. ~~For functions, replace all calls to `function_exists()` with [drupal_function_exists()](http://api.drupal.org/api/function/drupal_function_exists/7), which will load the necessary file and return TRUE or FALSE depending on whether the function now exists. In the case of hooks or any code called via module_invoke\*(), node_invoke(), etc. that will be done automatically.~~ *Files containing only functions need not be listed in the .info file.*

### ~~The hook_menu() and hook_theme() "file" and "file path" keys have been removed~~

[Roll-back patch](/node/497118)  
~~In Drupal 6, menu items and theme elements could declare an include file to be loaded on-demand for that page request. In Drupal 7, that is no longer necessary as such files will be loaded automatically by the [registry](#registry). The file and file path entries should be removed from both hook_menu() and hook_theme() implementations.~~

### New permission tables

[(Issue)](http://drupal.org/node/73874) The `{permission}` table is gone, instead we have a `{role_permission}` which stores `(role ID, permission string)` pairs. Thus, each permission granted for a given role ID is a separate row in the table. This update is in system.install so that it will already be complete when any other core or contributed module update is running. This should make any alteration of existing permissions much easier.

### Use '#markup' not '#value' for markup

[(Issue)](http://drupal.org/node/252013) The new default type for items in forms or other structured array data (e.g. node content) passed to [drupal_render()](http://api.drupal.org/api/function/drupal_render/7) is `'#type' => 'markup'`. In Drupal 6 and earlier, the HTML content was added to the array using the `#value` attribute. In Drupal 7, this needs to be changed to `#markup`. This change also applies to those form elements of `'#type' => 'item'`. This change reduces the confusion between form values and markup and allows the code in drupal_render() to be simplified.

Example 1, from system.admin.inc  
In Drupal 6:

``` php
  $screenshot = $screenshot ? theme('image', $screenshot, t('Screenshot for %theme theme', array('%theme' => $theme->info['name'])), '', array('class' => 'screenshot'), FALSE) : t('no screenshot');

  $form[$theme->name]['screenshot'] = array('#value' => $screenshot);
```

In Drupal 7:

``` php
  $screenshot = $screenshot ? theme('image', array('path' => $screenshot, 'alt' => t('Screenshot for %theme theme', array('%theme' => $theme->info['name'])), 'attributes' => array('class' => 'screenshot'))) : t('no screenshot');

  $form[$theme->name]['screenshot'] = array('#markup' => $screenshot);
```

Example 2, from contact.pages.inc  
In Drupal 6:

``` php
  $form['from'] = array(
    '#type' => 'item',
    '#title' => t('From'),
    '#value' => check_plain($user->name) . ' &lt;' . check_plain($user->mail) . '&gt;',
  );
```

In Drupal 7:

``` php
  $form['from'] = array(
    '#type' => 'item',
    '#title' => t('From'),
    '#markup' => check_plain($user->name) . ' &lt;' . check_plain($user->mail) . '&gt;',
  );
```

### Comment status values in the database have flipped so they match node status

This handy table shows the status indicator and what the numeric values are:

``` php
Version          Type       Published   Unpublished

6.x and before   Nodes      1           0
6.x and before   Comments   0           1
7.x              Nodes      1           0
7.x              Comments   1           0
```

The major change is to queries and code that interacts with comments.

If you had code that looked something like this in Drupal 6.x or before:

``` php
// Get a list of all unpublished comment IDs.
$results = db_query("SELECT cid FROM {comments} WHERE status = 1");
```

Here's what it should be in 7.x

``` php
// Get a list of all unpublished comment IDs.
$results = db_query("SELECT cid FROM {comments} WHERE status = 0");
```

You may also want to use the constants that are defined in the comment module for increased code clarity and future-proofing:

``` php
// Get a list of all unpublished comment IDs.
$results = db_query("SELECT cid FROM {comments} WHERE status = :comment_constant", array(':comment_constant' => COMMENT_NOT_PUBLISHED));
```

### Rebuild functions have changed names

6.x:

``` php
drupal_rebuild_theme_registry();
drupal_rebuild_code_registry();
```

7.x:

``` php
drupal_theme_rebuild();
registry_rebuild();
```

### Use defined constant REQUEST_TIME instead of time()

[(Issue)](http://drupal.org/node/302763) For improved performance, it is highly recommended that any calls to `time()` are replaced with `REQUEST_TIME`, a defined constant which will always return the UNIX timestamp from the start of the current request. If you absolutely need to get the current time, you can still use `time()` but it is not recommended.

### referer_uri() has been removed

[(Issue)](http://drupal.org/node/302763) `referer_uri()` has been removed and replaced with the PHP-provided global variable `$_SERVER['HTTP_REFERER']`. If there is no referrer, Drupal will automatically set `$_SERVER['HTTP_REFERER']` to an empty string.

### Some \#process functions have been renamed

[(Issue)](http://drupal.org/node/245001) Some functions used for processing form elements (specified by the `#form` item in the Forms API) have been renamed to unify their overall naming. The follow changes occurred:

| Old Name                  | New Name                        |
|---------------------------|---------------------------------|
| `expand_password_confirm` | `form_process_password_confirm` |
| `expand_date`             | `form_process_date`             |
| `expand_radios`           | `form_process_radios`           |
| `form_expand_ahah`        | `form_process_ahah`             |
| `expand_checkboxes`       | `form_process_checkboxes`       |
| `process_weight`          | `form_process_weight`           |

If your module defines a new element using `hook_elements()`, you have to update your `#process` callbacks.

### A completely new database API has been added

[(Issue)](http://drupal.org/node/225450) Drupal 7 introduces a completely new database API, utilizing a number of dynamic query builders and formal prepared statements. The following Drupal 6 functions and hooks were removed: db_affected_rows(), db_distinct_field(), db_error(), db_last_insert_id(), db_placeholders(), db_lock_table(), db_prefix_tables(), db_result(), db_fetch\_\*(), db_version(), db_rewrite_sql(), hook_db_rewrite_sql(), pager_query(), tablesort_sql(), and others.

For full information, read the [Database API guide](http://drupal.org/node/310069). A few common examples of Drupal 6 to 7 conversion are also covered below.

Normal SELECT queries:

``` php
// Drupal 6
$result = db_query("SELECT nid, title FROM {node} WHERE uid = %d AND type IN (" . db_placeholders(array('page', 'story'), 'varchar') . ")", 5, 'page', 'story');

// Drupal 7
$result = db_query("SELECT nid, title FROM {node} WHERE uid = :uid AND type IN (:type)", array(
  ':uid' => 5,
  ':type' => array('page', 'story'),
));
```

Iterating a result set from db_query():

``` php
// Drupal 6
while ($record = db_fetch_object($result)) {
  // Do stuff with $record, which is an object
}

// Drupal 7
foreach ($result as $record) {

  // Do stuff with $record, which is an object
}
```

Insert statements:

``` php
// Drupal 6
db_query("INSERT INTO {mytable} (intvar, stringvar, floatvar) VALUES (%d, '%s', %f)", 5, 'hello world', 3.14);
$id = db_last_insert_id();

// Drupal 7
$id = db_insert('mytable')
  ->fields(array(
    'intvar' => 5,
    'stringvar' => 'hello world',
    'floatvar' => 3.14,
  ))
  ->execute();
```

Update statements:

``` php
// Drupal 6
db_query("UPDATE {node} SET title='%s', status=%d WHERE uid=%d", 'hello world', 1, 5);

// Drupal 7
db_update('node')
  ->fields(array('title' => 'hello world', 'status' => 1))
  ->condition('uid', 5)
  ->execute();
```

Delete statements:

``` php
// Drupal 6
db_query("DELETE FROM {node} WHERE uid=%d AND created < %d", 5, REQUEST_TIME - 3600);

// Drupal 7
db_delete('node')
  ->condition('uid', 5)
  ->condition('created', REQUEST_TIME - 3600, '<')
  ->execute();
```

Also note that dynamic queries that have tags may be altered by any module that implements [hook_query_alter()](http://api.drupal.org/api/function/hook_query_alter/7) or [hook_query_TAG_alter()](http://api.drupal.org/api/function/hook_query_TAG_alter/7). This takes the place of hook_db_rewrite_sql() in Drupal 6.

### file_validate_extensions() enforces check for uid=1

[(issue)](/node/308434) In 6.x the function for validating file extensions would bypass this check for the uid=1 user. This has been removed in 7.x. If your module depended on this behavior you need to check the user's uid and conditionally specify the file_validate_extensions() validator.

### file_scan_directory() and drupal_system_listing() use preg regular expressions

[(issue)](/node/64967) The [file_scan_directory()](http://api.drupal.org/api/function/file_scan_directory/7) and [drupal_system_listing()](http://api.drupal.org/api/function/drupal_system_listing/7) function now use preg_match() rather than ereg() which allows case-insensitive matching and speed improvements. As a result the formats of the regular expressions these functions accept as parameters have changed.

For most modules the change is as simple as adding a leading and trailing `/` (forward slash).

Drupal 6.x:

``` php
   // Get current list of modules.
  $files = drupal_system_listing('\.module$', 'modules', 'name', 0);
```

Drupal 7.x:

``` php
  // Get current list of modules.
  $files = drupal_system_listing('/\.module$/', 'modules', 'name', 0);
```

Modules with more complicated regular expressions should review the PHP documentation for the [ereg()](http://us.php.net/ereg) and [preg_match()](http://us.php.net/manual/en/function.preg-match.php) functions.

### Easier check for node form during hook_form_alter()

~~Modules wishing to alter the node form may now check for `!empty($form['#node_edit_form'])` instead of the verbose `if (isset($form['type']) && isset($form['#node']) && $form['type']['#value'] .'_node_form' == $form_id)`. See [\#161301: Make checking for node edit forms easier](/project/drupal/issues/161301 "Status: Closed (fixed), Assigned to: eaton")~~

Use `hook_form_node_form_alter()` now. See upgrade notes for [hook_form_BASE_FORM_ID_alter()](#hook_form_BASE_FORM_ID_alter).

### Update functions in .install files must include a Doxygen style comment

The [Doxygen style comment](/node/1354) is displayed to administrators on update.php. Background info - [\#286035: Remove update.php number dropdowns](/project/drupal/issues/286035 "Status: Closed (fixed), Assigned to: moshe weitzman")

### Replace drupal_clone() with clone

[(issue)](http://drupal.org/node/222385) Since Drupal 7 requires at least PHP 5, it allowed the removal of the [drupal_clone](http://api.drupal.org/api/function/drupal_clone) function for a direct call to [clone](http://us.php.net/language.oop5.cloning).

Drupal 6.x:

``` php
   // Make a copy of the node.
  $cloned_node = drupal_clone($node);
```

Drupal 7.x:

``` php
  // Make a copy of the node.
  $cloned_node = clone $node;
```

### Session functions are renamed

[(issue)](http://drupal.org/node/477944) All session functions starting with) sess\_\*, as well as session_save_session(), are now renamed. Most are renamed to drupal_session\_\* or \_drupal_session\_\*..

Drupal 6.x:

``` php
sess_write(TRUE);
```

Drupal 7.x:

``` php
_drupal_session_write(TRUE);
```

The easiest way to figure out the correspondence between old and new names is to look at the function lists from session.inc in [Drupal 6](http://api.drupal.org/api/drupal/includes--session.inc/6 "session.inc in Drupal 6") and [Drupal 7](http://api.drupal.org/api/drupal/includes--session.inc/7 "session.inc in Drupal 7"). Some got renamed in the process, like session_save_session is now [drupal_save_session](http://api.drupal.org/api/drupal/includes--session.inc/function/drupal_save_session/7).

### hook_nodeapi, hook_node_type, hook_user, and hook_block removed and replaced with families of related functions

([hook_nodeapi issue](http://drupal.org/node/314244), [hook_user issue](http://drupal.org/node/310212), released in UNSTABLE-2) ([hook_block issue](http://drupal.org/node/345866), released in UNSTABLE-4) ([hook_node_type issue](http://drupal.org/node/545306))

In Drupal 7, several hooks that previously allowed modules to do a group of related operations, with a \$op argument, were split into individual hooks for each operation. Gábor posted a [note in the developer mailing list about this](http://lists.drupal.org/pipermail/development/2008-May/029795.html) if you'd like to read more about it.

The hooks that were changed in this way:

- [hook_nodeapi() in Drupal 6](http://api.drupal.org/api/function/hook_nodeapi/6) became (see [Node API page](http://api.drupal.org/api/drupal/modules--node--node.api.php/7)) hook_node_delete(), hook_node_insert(), hook_node_load(), hook_node_prepare(), hook_node_prepare_translation(), hook_node_search_result(), hook_node_presave(), hook_node_update(), hook_node_update_index(), hook_node_validate(), and hook_node_view(). Note that the former 'alter' operation of hook_nodeapi() was replaced by [hook_node_view_alter()](http://api.drupal.org/api/drupal/modules--node--node.api.php/function/hook_node_view_alter/7), which works differently, as it receives a render array rather than operating on an HTML string that is part of the node.
- [hook_node_type() in Drupal 6](http://api.drupal.org/api/function/hook_node_type/6) became (see [Node API page](http://api.drupal.org/api/drupal/modules--node--node.api.php/7)) hook_node_type_delete(), hook_node_type_insert(), andhook_node_type_update().
- [hook_user() in Drupal 6](http://api.drupal.org/api/function/hook_user/6) became (see [User API page](http://api.drupal.org/api/drupal/modules--user--user.api.php/7)) hook_user_categories(), hook_user_insert(), hook_user_load(), hook_user_login(), hook_user_logout(), hook_user_presave(), hook_user_update(), and hook_user_view().
- [hook_block() in Drupal 6](http://api.drupal.org/api/function/hook_block/6) became (see [Block API page](http://api.drupal.org/api/drupal/modules--block--block.api.php/7)) hook_block_info(), hook_block_configure(), hook_block_save(), and hook_block_view().
- The "form" and "register" operations have been removed. Use [hook_form_alter](http://api.drupal.org/api/function/hook_form_alter/7) instead.

Here are some examples - Drupal 6.x:

``` php
/**
 * Implements hook_nodeapi().
 */
function book_nodeapi(&$node, $op, $teaser, $page) {
  switch ($op) {
    case 'load':
      // Load a book.
  }
}

/**
 * Implements hook_node_type().
 */
function mymodule_node_type($op, $info) {
  switch ($op){
    case 'delete':
      // Delete, insert or update according to $op.
  }
}

/**
 * Implements hook_user().
 */
function block_user($type, $edit, &$account, $category = NULL) {
  switch ($type) {
    case 'form':
      // Construct the user form.

  }
}

/**
 * Implements hook_block().
 */
function system_block($op = 'list', $delta = 0, $edit = array()) {
  switch ($op) {
    case 'list':
      // List blocks.
  }
}
```

Drupal 7.x:

``` php
/**
 * Implements hook_node_load().
 */
function book_node_load($nodes, $types) {
  // Load a book.
}

/**
 * Implements hook_block_info().
 */
function system_block_info() {
  // List blocks.
}

/**
 * Implements hook_node_type_delete().
 */
function mymodule_node_type_delete($info) {
  variable_del('comment_' . $info->type);
}

/**
 * Implements hook_node_update().
 */
function hook_node_update($node) {
  db_update('mytable')
    ->fields(array('extra' => $node->extra))
    ->condition('nid', $node->nid)
    ->execute();
}

/**
 * Implements hook_node_insert().
 */
function hook_node_insert($node) {
  db_insert('mytable')
    ->fields(array(
      'nid' => $node->nid,
      'extra' => $node->extra,
    ))
    ->execute();
}
```

### In hook_node_info() change 'module' back to 'base' and change 'node' to 'node_content'

([issue](http://drupal.org/node/206138)) between Drupal 4.7 and Drupal 5, the 'base' attribute in hook_node_info() was changed to 'module'. However, this is confusing for developers, since there is no requirement that this attribute correspond to the name of any module, and there may be multiple node types defined per module. This change reverts to using 'base'.

In addition, the content types managed by the node module had a 'module' (now 'base') attribute of 'node'. However, to prevent conflicts with the node module's own hooks, this was selectively altered when invoking hooks to 'node_content'. For example, they have always used [node_content_form()](http://api.drupal.org/api/function/node_content_form/7). By simply assigning the 'base' attribute of these types to be 'node_content' in the database, we can eliminate the error-prone coercing of these attributes at each hook invocation.

The helper function \_node_type_set_defaults() is now a more useful public function [node_type_set_defaults()](http://api.drupal.org/api/function/node_type_set_defaults/7).

Drupal 6.x:

``` php
/**
 * Implements hook_node_info().
 */
function blog_node_info() {
  return array(
    'blog' => array(
      'name' => t('Blog entry'),
      'module' => 'blog',
      'description' => t('A <em>blog entry</em> is a single post to an online journal.'),
     );
}
```

Drupal 7.x:

``` php
/**
 * Implements hook_node_info().
 */
function blog_node_info() {
  return array(
    'blog' => array(
      'name' => t('Blog entry'),
      'base' => 'blog',
      'description' => t('A <em>blog entry</em> is a single post to an online journal.'),
     );
}
```

Saving to the DB a node-type to be managed by node module:

Drupal 6.x:

``` php
function _book_install_type_create() {
  $book_node_type = array(
    'type' => 'book',
    'name' => t('Book page'),
    'module' => 'node',
    'description' => t('A <em>book page</em>.'),
    'custom' => TRUE,
    'modified' => TRUE,
    'locked' => FALSE,
  );

  $book_node_type = (object)_node_type_set_defaults($book_node_type);
  node_type_save($book_node_type);
}
```

Drupal 7.x:

``` php
function _book_install_type_create() {
  $book_node_type = array(
    'type' => 'book',
    'name' => t('Book page'),
    'base' => 'node_content',
    'description' => t('A <em>book page</em>.'),
    'custom' => 1,
    'modified' => 1,
    'locked' => 0,
  );

  $book_node_type = node_type_set_defaults($book_node_type);
  node_type_save($book_node_type);
}
```

### Use absolute path (constructed from DRUPAL_ROOT) when including a file

([issue](http://drupal.org/node/259623)) When including a file (via [include](http://php.net/include)(), [include_once](http://php.net/include_once)(), [require](http://php.net/require)() or [require_once](http://php.net/require_once)()) specify the absolute path to the file, using the named constant [DRUPAL_ROOT](http://api.drupal.org/api/constant/DRUPAL_ROOT/7) to give the absolute path to the root of the Drupal installation.

Drupal 6.x:

``` php
// Allow specifying special cache handlers in settings.php, like
// using memcached or files for storing cache information.
require_once variable_get('cache_inc', './includes/cache.inc');
```

Drupal 7.x:

``` php
// Allow specifying special cache handlers in settings.php, like
// using memcached or files for storing cache information.
require_once DRUPAL_ROOT . '/' . variable_get('cache_inc', 'includes/cache.inc');
```

In addition, a standalone script that requires access to Drupal will need to define DRUPAL_ROOT before including bootstrap.inc and invoking [drupal_bootstrap](http://api.drupal.org/api/function/drupal_bootstrap/7)(), e.g. for a script located in the Drupal root folder:

``` php
/**
 * Root directory of Drupal installation.
 */
define('DRUPAL_ROOT', dirname(realpath(__FILE__)));
```

This will need to be modified accordingly for a script located outside the Drupal root folder.

### File API reworked, stream notation required, file_unmanaged\_\* functions

([issue](http://drupal.org/node/142995))  
The File API, including most key functions has been radically restructured. Nearly every function is touched by these change.

To understand these changes you need to understand two key concepts. **Streamwrapper notation**: All filename notation now uses PHP's streamwrapper format: *scheme://path/to/file.txt*. (The "scheme" is a protocol or way of handling files, such as "public", "private", or other extensions.) In general, this will often be "public://somefile.txt" or "private://somefile.txt", but contributed modules can support other schemes. **Managed vs unmanaged files:** "Managed" means that we are working with the file via its database record in the file_managed table, and typically we'll pass a file object to it. "Unmanaged" means that we're just working with the file itself.

Three major changes have been made:

1.  Any file function that used to take a traditional filepath like "sites/default/files/something.txt" now must take a stream-oriented filepath like "public://something.txt" or "private://something.txt".
2.  Many APIs used to take a string if they were acting on an unmanaged file (a file with no entry in the database), or a file object if acting on a managed file. Now those functions have been split out, so we now have file_copy() (which takes a file object) and file_unmanaged_copy() (which takes a stream-oriented filepath like "public://example.txt").
3.  file_create_path() and file_check_directory() were merged into [file_prepare_directory()](http://api.drupal.org/api/function/file_prepare_directory/7).

The [file_copy()](http://api.drupal.org/api/function/file_copy/6), [file_move()](http://api.drupal.org/api/function/file_move/6), [file_delete()](http://api.drupal.org/api/function/file_delete/6) and [file_save_data()](http://api.drupal.org/api/function/file_save_data/6) functions from Drupal 6 have been renamed to [file_unmanaged_copy()](http://api.drupal.org/api/function/file_unmanaged_copy/7), [file_unmanaged_move()](http://api.drupal.org/api/function/file_unmanaged_move/7), [file_unmanaged_delete()](http://api.drupal.org/api/function/file_unmanaged_delete/7) and [file_unmanaged_save_data()](http://api.drupal.org/api/function/file_unmanaged_save_data/7).

In addition, the majority of the time drupal_realpath() must be used in place of former uses of realpath().

Please see [the handbook File API change page](http://drupal.org/node/877214) and the [main File API](http://drupal.org/node/555118) handbook page for more extensive discussion of the file API changes in Drupal 7. The Drupal 7 version of the [Examples project](http://drupal.org/project/examples) also contains a File Example demonstrating the use of many Drupal 7 File API functions.

### "administer nodes" permission split into "administer nodes", "access content overview", and "bypass node access"

([issue](http://drupal.org/node/305566)) The "administer nodes" permission has been split into two separate permissions, "administer nodes" and "bypass node access".

The "administer nodes" permission now grants the ability to alter all data associated with a given node, such as menu items, publication status and path aliases, *provided that the user already has permission to modify the node*. Unlike in 6.x and earlier, this permission does *not* allow the user to view or edit all nodes on a site.

The "bypass node access" permission grants the ability to view, edit or delete all nodes, without regard to any status checks made by hook_access or the node access system. The "bypass node access" check overrides any other checks made by permissions such as "edit page nodes". However, users with this permission will not automatically be able to edit all attributes of a given node (such as menu item, publication status and path alias), unless their other permissions allow them to do so.

When upgrading a site from 6.x to 7.x, roles with the "administer nodes" permission are automatically given the "bypass node access" permission as well, since having the "administer nodes" permission in 6.x is equivalent to having both in 7.x.

For modules that used the old "administer nodes" permission for access checks, you may now need to switch to "bypass node access" or to both permissions, for access checks.

[(issue)](http://drupal.org/node/301902) The "administer nodes" permission has been split into two separate permissions, "administer nodes" and "access content overview".

The "administer nodes" permission does not grant access to the content overview anymore.

The "access content overview" permission grants access to the content overview page which lists the nodes present on the site. The content and actions presented on this page will now depend on the node access rules and other permissions such as "administer nodes", "bypass node access" and "view own unpublished content".

Giving "access content overview" to users with "administer comments" permission allows them to see the "Comments" tab on the content overview page, allowing them to have an entry point to the comment administration interface they are given access to.

When upgrading a site from 6.x to 7.x, roles with the "administer nodes" permission are automatically given the "access content overview" permission as well, since having the "administer nodes" permission in 6.x is equivalent to having both in 7.x.

### New hooks: hook_modules_installed, hook_modules_enabled, hook_modules_disabled, and hook_modules_uninstalled

[(Issue)](http://drupal.org/node/253569) Four new hooks are provided so that other modules can react to modules' status changes. Each hook is passed an array of module short-names, i.e. array('blog', 'blogapi'). Note, these hooks should NOT be used by a module for its own installation or uninstallation; hook_install or hook_uninstall should be used. See the documentation for each hook for more information.

- [hook_modules_installed](http://api.drupal.org/api/function/hook_modules_installed/7)
- [hook_modules_enabled](http://api.drupal.org/api/function/hook_modules_enabled/7)
- [hook_modules_disabled](http://api.drupal.org/api/function/hook_modules_disabled/7)
- [hook_modules_uninstalled](http://api.drupal.org/api/function/hook_modules_uninstalled/7)

### drupal_uninstall_module() is now drupal_uninstall_modules()

([issue](http://drupal.org/node/253569)) The function drupal_uninstall_module() used to take one parameter (the name of the module to uninstall). It has been changed to a new function called drupal_uninstall_modules(), whose one parameter is an array of modules to uninstall.

### drupal_set_title() uses check_plain() by default

([issue](http://drupal.org/node/242873)) drupal_set_title() now uses check_plain() on the title text by default. To pass through text that has already been sanitized (e.g. using check_plain(), or the % or @ placeholders in t()), then supply the constant `PASS_THROUGH` as the second argument. If you are currently calling check_plain(), that can be removed to avoid double-escaping.

For example:

Drupal 6.x:

``` php
    drupal_set_title(check_plain($node->title));
```

Drupal 7.x:

``` php
    drupal_set_title($node->title);
```

Drupal 6.x:

``` php
  drupal_set_title(t("@name's blog", array('@name' => $account->name)));
```

Drupal 7.x:

``` php
  drupal_set_title(t("@name's blog", array('@name' => $account->name)), PASS_THROUGH);
```

### Changed parameters for drupal_add_js() and drupal_add_css()

([drupal_add_js() issue](http://drupal.org/node/315797), [drupal_add_css() issue](http://drupal.org/node/266358)) The [drupal_add_js()](http://api.drupal.org/api/function/drupal_add_js/7) and [drupal_add_css()](http://api.drupal.org/api/function/drupal_add_css/7) functions now take either a string defining the type of script that's being added to the page, or an array defining more about the data being added. The new function signature is as follows:

``` php
drupal_add_js($data = NULL, $options = NULL);
drupal_add_css($path = NULL, $options = NULL);
```

Again, \$options can be a string defining the type of script being added ('module', 'theme', 'setting', etc), or an associative array containing arguments about the data ('type', 'scope', 'defer', 'cache', 'preprocess', 'media'). In the end, the code change looks like the following:

Drupal 6.x:

``` php
drupal_add_js('misc/collapse.js', 'module');
drupal_add_js('misc/collapse.js', 'module', 'footer');
drupal_add_js('misc/collapse.js', 'module', 'header', FALSE, TRUE, FALSE);
drupal_add_css('/modules/devel/devel.css', 'module');
drupal_add_css('/modules/devel/devel.css', 'module', 'screen');
drupal_add_css('/modules/devel/devel.css', 'module', 'all', FALSE);
```

Drupal 7.x:

``` php
drupal_add_js('misc/collapse.js');  // 'module' must be removed or else css will not be added!
drupal_add_js('misc/collapse.js', array('type' => 'module', 'scope' => 'footer'));
drupal_add_js('misc/collapse.js', array('preprocess' => FALSE));
drupal_add_css('modules/devel/devel.css');
drupal_add_css('modules/devel/devel.css', array('media' => 'screen'));
drupal_add_css('modules/devel/devel.css', array('preprocess' => FALSE));
```

Note that the second parameter can either be the type, or an array defining more about the data being added. Therefore, this change should only apply to drupal_add_js() or drupal_add_css() calls that defined more than just the type during its call.

### Changed Drupal.behaviors to objects having the properties 'attach' and 'detach'

([issue](http://drupal.org/node/316225)) JavaScript behaviors are now objects, having the properties 'attach' and 'detach'. To each of these properties a function is assigned that (1) acts as a container for all the functionality to be attached or detached and (2) optionally passes the context and settings to any code within its scope. Correspondingly, `Drupal.attachBehaviors()` is now accompanied by `Drupal.detachBehaviors()`. Developers who make use of dynamic AJAX/AHAH contents should additionally invoke `Drupal.detachBehaviors()` **before** a page element is going to be **processed or removed** from the output, allowing special behaviors (such as client-side editors) to detach from it.  
Conversion of simple behaviors is easy:

Drupal 6.x:

``` php
Drupal.behaviors.tableSelect = function(context) {
  $('form table:has(th.select-all):not(.tableSelect-processed)', context).each(Drupal.tableSelect);
};
```

Drupal 7.x:

``` php
Drupal.behaviors.tableSelect = {
  attach: function(context) {
    $('form table:has(th.select-all):not(.tableSelect-processed)', context).each(Drupal.tableSelect);
  }
};
```

All AJAX/AHAH-driven applications should invoke `Drupal.detachBehaviors(context)` before a form is processed/sent and content is removed from the output, where 'context' refers to the affected page element, just like the context of `Drupal.attachBehaviors(context)`. For example:

Drupal 7.x:

``` php
/**
 * Processes a form in a modal dialog.
 */
Drupal.myModule.ajaxSubmit = function() {
  $('form#mymodule-ajax-form').submit(
    Drupal.detachBehaviors($(this));
    $(this).ajaxSubmit({
      url: Drupal.settings.myAjaxURL,
      data: '...',
      method: 'post'
    });
    return false;
  );
};

/**
 * Removes a modal dialog (dismissing form processing).
 */
Drupal.myModule.cancelModal = function() {
  var dialog = $('#mymodule-modal-content');
  Drupal.detachBehaviors(dialog);
  dialog.remove();
};
```

If behaviors need to detach from contents, they should additionally implement the 'detach' method, searching for elements using the reversed selector of the attaching method:

``` php
Drupal.behaviors.tableSelect = {
  attach: function(context) {
    $('form table:has(th.select-all):not(.tableSelect-processed)', context).each(Drupal.tableSelect);
  },
  detach: function(context) {
    $('form table.tableSelect-processed', context).each(
      ...
    );
  }
};
```

### Removed file_set_status()

[(Issue)](http://drupal.org/node/331013) The file_set_status() function which was used, primarily, to make temporary files permanent has been removed file_save() should be used in its place.

Drupal 6.x:

``` php
file_set_status($file, FILE_STATUS_PERMANENT);
```

Drupal 7.x:

``` php
$file->status |= FILE_STATUS_PERMANENT;
$file = file_save($file);
```

### Replace 'core', 'module' and 'theme' with 'file' in drupal_add_js()

[(issue)](http://drupal.org/node/315798) JavaScript can now be ordered according to its weight rather than in what order [drupal_add_js()](http://api.drupal.org/api/function/drupal_add_js/7) was called. Rather than using 'core', 'module' or 'theme' types to determine the order in which JavaScript is presented on the page, we now use a 'file' type, along with a 'weight' parameter. For the upgrade path in Drupal 6, we must simply replace 'core', 'module' and 'theme' with the respective weight parameter.

Drupal 6.x:

``` php
drupal_add_js($jquery_plugin, 'core');
drupal_add_js($module_javascript, 'module');
drupal_add_js($theme_javascript, 'theme');

drupal_add_js($other_javascript, 'module');
drupal_add_js($file);
```

Drupal 7.x:

``` php
drupal_add_js($jquery_plugin, array('weight' => JS_LIBRARY));
drupal_add_js($module_javascript, array('type' => 'file', 'weight' => JS_DEFAULT));
drupal_add_js($theme_javascript, array('weight' => JS_THEME));
drupal_add_js($other_javascript, 'file');
drupal_add_js($file);
```

For more information about the added 'weight' parameter, visit the [drupal_add_js() documentation](http://api.drupal.org/api/function/drupal_add_js/7).

### Parameters to check_markup() have changed, default format change

[check_markup()](http://api.drupal.org/api/function/check_markup/7) now accepts an additional parameter, \$langcode. This is needed for filters that implement language-specific text replacements.

In addition, the second argument, \$format_id, has a different default than it did in Drupal 6. In Drupal 6, check_markup(\$text) essentially ran the text through the 'Filtered HTML' format. In Drupal 7, it runs through the fallback format, which by default is "Plain text". So the return from check_markup(\$text) will have a different result by default in Drupal 7.

Objects that include a language should now pass this to `check_markup()`.

Drupal 6.x:

``` php
$node->body = check_markup($node->body, $node->format);
```

Drupal 7.x:

``` php
$node->body[$lang]['safe_value'] = check_markup($node->body[$lang]['value'], $node->format, $lang);
```

The \$check argument no longer exists, since [filter_access()](http://api.drupal.org/api/function/filter_access/7) and Form API perform access checks already at a lower level within the [filter_formats()](http://api.drupal.org/api/function/filter_formats/7) function.

There is a new fourth argument to enable caching on the resulting, filtered text. It is turned off by default, because most filtered text is contained in text fields in D7. Field API uses its own field cache to store filtered text. Passing FALSE for the \$cache parameter prevents redundant caching. If you are using check_markup() on text that lives in a custom storage, you may want to set this argument to TRUE to take advantage of the filter cache.

Drupal 6.x:

``` php
// The resulting string was cached in the filter cache in D6.
$content = check_markup($mycustom->body, $mycustom->format);
```

Drupal 7.x

``` php
// Only for text that in custom tables and storage,
// use the filter cache for the resulting, filtered text to speed up performance.
$content = check_markup($mycustom->body, $mycustom->format, $mycustom->language, TRUE);
```

### Schema descriptions are no longer translated

[(Issue)](http://drupal.org/node/332123) To reduce the strings to translate, descriptions of the [schema API](http://api.drupal.org/api/group/schemaapi/7) (tables and fields) in module.install no longer need to be translated.

6.x:  
  

``` php
function forum_schema() {
  $schema['forum'] = array(
    'description' => t('Stores the relationship of nodes to forum terms.'),
    'fields' => array(
      'nid' => array(
        'description' => t('The {node}.nid of the node.'),
      ),
    ),
  );
  return $schema;
}
```

7.x:  
  

``` php
function forum_schema() {
  $schema['forum'] = array(
    'description' => 'Stores the relationship of nodes to forum terms.',
    'fields' => array(
      'nid' => array(
        'description' => 'The {node}.nid of the node.',
      ),
    ),
  );
  return $schema;
}
```

### file_scan_directory() now uses a preg regular expression for the nomask parameter

[(issue)](/node/74645) The [file_scan_directory()](http://api.drupal.org/api/function/file_scan_directory/7) function now uses a preg style regular expression to determine which files and directories it ignores.

The majority of calls to file_scan_directory() just specify in the function's default parameter. In these cases all that's needed is to use the new default parameter. If you're doing more complicated exclusions you'll want to consult the PHP documentation for the [preg_match()](http://us.php.net/manual/en/function.preg-match.php) function.

Drupal 6.x:

``` php
file_scan_directory(file_create_path('css'), '/.*/', array('.', '..', 'CVS'), 'file_unmanaged_delete', TRUE);
```

Drupal 7.x:

``` php
file_scan_directory(file_prepare_directory('css', FILE_CREATE_DIRECTORY), '/.*/', '/(\.\.?|CVS)$/', 'file_unmanaged_delete', TRUE);
```

### Use module_implements not module_list when calling hook implementations

All code that did this:

``` php
foreach (module_list() as $module)) {
  // Do something with a hook on each module.
```

should now do this:

``` php
foreach (module_implements($hook) as $module)) {
  // Do something with $hook on each module.
```

### New hook_js_alter to alter JavaScript

[(issue)](http://drupal.org/node/315801) Before Drupal 7, when you wanted to alter JavaScript being presented on the page, you'd have to alter the \$scripts variable. The jQuery Update module, for example, would use hook_preprocess_page(\$variables) to alter the \$scripts variable directly. Now, with hook_js_alter(), we can just directly alter any JavaScript that will be presented on the page.

A live example of hook_js_alter() being used is available in [simpletest_js_alter()](http://api.drupal.org/api/function/simpletest_js_alter/7), which moves the simpletest.js's weight above tableselect.js's weight. The \$javascript parameter that's pass into hook_js_alter() is all JavaScript that's going to be presented on the page.

Drupal 6.x:

``` php
function jquery_update_preprocess_page(&$variables) {
  // Modify the scripts variable.
  if (!empty($variables['scripts'])) {
```

Drupal 7.x:

``` php
function jquery_update_js_alter(&$javascript) {
  // Modify the JavaScript being presented on the page.
```

### node_load() and node_load_multiple()

[(issue)](http://drupal.org/node/324313) Multiple nodes can now be loaded at once using [node_load_multiple()](http://api.drupal.org/api/function/node_load_multiple). All nodes loaded by this function are loaded in a single query. [hook_node_load()](http://api.drupal.org/api/function/hook_node_load) now takes an array of node objects, and modules should use one database query here where possible also.

[node_load()](http://api.drupal.org/api/function/node_load/7) has been simplified to take only nid and vid as parameters, and is a simple wrapper around [node_load_multiple()](http://api.drupal.org/api/function/node_load_multiple).

### taxonomy_term_load() and taxonomy_term_load_multiple()

[(issue)](http://drupal.org/node/324313) Multiple taxonomy terms can now be loaded at once using [taxonomy_term_load_multiple()](http://api.drupal.org/api/function/taxonomy_term_load_multiple). All terms loaded by this function are loaded in a single query. [hook_taxonomy_term_load()](http://api.drupal.org/api/function/hook_taxonomy_term_load) now takes an array of term objects, and modules should use one database query here where possible also. taxonomy_term_load() is a now a simple wrapper around the multiple function, sharing the same static cache.

### file_load_multiple()

[issue](http://drupal.org/node/348201). Multiple file objects can now be loaded at once using [file_load_multiple()](http://api.drupal.org/api/function/file_load_multiple). [hook_file_load()](http://api.drupal.org/api/function/hook_file_load/7) takes an array of file objects.

### Taxonomy CRUD functions renamed and refactored

To improve consistency, the CRUD functions for both taxonomy terms and vocabularies have been renamed and refactored:

- [(Issue)](http://drupal.org/node/305740) To load a taxonomy term, you should now use [taxonomy_term_load()](http://api.drupal.org/api/function/taxonomy_term_load/7) which has replaced taxonomy_get_term().
- [(Issue)](http://drupal.org/node/314147) To save taxonomy terms, you should now use [taxonomy_term_save()](http://api.drupal.org/api/function/taxonomy_term_save/7) which has replaced taxonomy_save_term(). Note that the new function takes a term object as a parameter instead of an array.
- [(Issue)](http://drupal.org/node/314147) To delete a taxonomy term, you should now use [taxonomy_term_delete()](http://api.drupal.org/api/function/taxonomy_term_delete/7) which has replaced taxonomy_del_term().

<!-- -->

- To load a vocabulary, keep using [taxonomy_vocabulary_load()](http://api.drupal.org/api/function/taxonomy_vocabulary_load/7).
- [(Issue)](http://drupal.org/node/329140) To save vocabulary, you should now use [taxonomy_vocabulary_save()](http://api.drupal.org/api/function/taxonomy_vocabulary_save/7) which has replaced taxonomy_save_vocabulary(). Note that the new function takes a vocabulary object as a parameter instead of an array.
- [(Issue)](http://drupal.org/node/329140) To delete a vocabulary, you should now use [taxonomy_vocabulary_delete()](http://api.drupal.org/api/function/taxonomy_vocabulary_delete/7) which has replaced taxonomy_del_vocabulary().

### New taxonomy hooks for term and vocabulary

[(Issue)](http://drupal.org/node/306224) New hooks are provided for taxonomy terms to allow modules to add information to the term object.

- [hook_taxonomy_term_load](http://api.drupal.org/api/function/hook_taxonomy_term_load/7)
- [hook_taxonomy_term_presave](http://api.drupal.org/api/function/hook_taxonomy_term_presave/7)
- [hook_taxonomy_term_insert](http://api.drupal.org/api/function/hook_taxonomy_term_insert/7)
- [hook_taxonomy_term_update](http://api.drupal.org/api/function/hook_taxonomy_term_update/7)
- [hook_taxonomy_term_delete](http://api.drupal.org/api/function/hook_taxonomy_term_delete/7)

<!-- -->

- [hook_taxonomy_vocabulary_load](http://api.drupal.org/api/function/hook_taxonomy_vocabulary_load/7)
- [hook_taxonomy_vocabulary_presave](http://api.drupal.org/api/function/hook_taxonomy_vocabulary_presave/7)
- [hook_taxonomy_vocabulary_insert](http://api.drupal.org/api/function/hook_taxonomy_vocabulary_insert/7)
- [hook_taxonomy_vocabulary_update](http://api.drupal.org/api/function/hook_taxonomy_vocabulary_update/7)
- [hook_taxonomy_vocabulary_delete](http://api.drupal.org/api/function/hook_taxonomy_vocabulary_delete/7)

### taxonomy_get_tree()

[(issue)](http://drupal.org/node/343259) [taxonomy_get_tree()](http://api.drupal.org/api/function/taxonomy_get_tree/7)'s `$depth` and `$max_depth` parameters have switched positions, since `$depth` is for internal use only. You will not have to specify its default value anymore if you want to set `$max_depth`

### Code documentation added to module.api.php

[(issue)](http://drupal.org/node/314870) If your module creates any hooks or has an associated API, add examples of these hooks in *modulename.api.php*. This not only helps other developers understand the provided API a little easier, but also gives IDEs the hook information. See [system.api.php](https://api.drupal.org/api/drupal/modules!system!system.api.php/7) for an example of this.

### Move node, taxonomy, and comment links into \$node-\>content; Deprecate hook_link()

[(issue)](http://drupal.org/node/339929) Node and taxonomy links are no longer emitted by hook_link() and hook_link_alter(). Instead, links are added to \$node-\>content during hook_node_view(). Similarly, comment links are now injected into \$comment-\>content during hook_comment_view(). Links and all of \$node-\>content may be re-arranged/changed during the **new hook: hook_node_view_alter()** and **new hook: hook_comment_view_alter()**. For example:

Drupal 6

``` php
function blog_link($type, $node = NULL, $teaser = FALSE) {
  $links = array();

  if ($type == 'node' && $node->type == 'blog') {
    if (arg(0) != 'blog' || arg(1) != $node->uid) {
      $links['blog_usernames_blog'] = array(
        'title' => t("!username's blog", array('!username' => $node->name)),
        'href' => "blog/$node->uid",
        'attributes' => array('title' => t("Read !username's latest blog entries.", array('!username' => $node->name))),
      );
    }
  }

  return $links;
}
```

Drupal 7

``` php
function blog_node_view($node, $view_mode, $langcode) {
  if ($node->type == 'blog') {
    if (arg(0) != 'blog' || arg(1) != $node->uid) {
      $links['blog_usernames_blog'] = array(
        // Unrelated to the change where links are added, Drupal 7 also adds a
        // format_username() function.
        'title' => t("!username's blog", array('!username' => format_username($node))),
        'href' => "blog/$node->uid",
        'attributes' => array('title' => t("Read !username's latest blog entries.", array('!username' => format_username($node)))),
      );
      $node->content['links']['blog'] = array(
        '#theme' => 'links__node__blog',
        '#links' => $links,
        '#attributes' => array('class' => array('links', 'inline')),
      );
    }
  }
}
```

### Parameters for actions_synchronize() have changed

[(issue)](http://drupal.org/node/319404) The \$actions_in_code parameter has been removed from actions_synchronize().  
Drupal 6.x:

``` php
function actions_synchronize($actions_in_code = array(), $delete_orphans = FALSE) {
  if (!$actions_in_code) {
    $actions_in_code = actions_list(TRUE);
  }
  ...
```

Drupal 7.x:

``` php
function actions_synchronize($delete_orphans = FALSE) {
  $actions_in_code = actions_list(TRUE);
  ...
```

### Parameters for drupal_http_request() have changed

[(issue)](http://drupal.org/node/337783) Instead of a long line of single arguments (the exact options and order of which were hard to remember), this function now takes an array to specify the optional arguments. The new function signature is as follows:

``` php
drupal_http_request($url, array $options = array());
```

\$options is an associative array that contains 'headers', 'method', 'data', and 'max_redirects.' Thus, the \$headers array that was a parameter in 6.x will now be passed in as \$options\['headers'\].

Drupal 6.x

``` php
drupal_http_request('http://example.com/', array('Header-Title' => 'value'), 'GET', NULL, 0);
```

Drupal 7.x

``` php
drupal_http_request('http://example.com/', array('headers' => array('Header-Title' => 'value'), 'max_redirects' => 0));
```

See <http://api.drupal.org/api/function/url/6> and <http://api.drupal.org/api/function/l/6> for more information.

### db_rewrite_sql() replaced with hook_query_alter()

[(issue)](http://drupal.org/node/299176) The string-parsing-based db_rewrite_sql() has been removed in favor of hook_query_alter(). Instead of passing a literal query through db_rewrite_sql() in order to add node access restrictions, for instance, in Drupal 7 use a [dynamic query](http://drupal.org/node/310075) and tag it "node_access".

Drupal 6.x

``` php
$result = db_query_range(db_rewrite_sql("SELECT n.nid, n.title, n.created FROM {node} n WHERE n.type = 'blog' AND n.status = 1 ORDER BY n.created DESC"), 0, 10);
```

Drupal 7.x

``` php
   $result = db_select('node', 'n')
      ->fields('n', array('nid', 'title', 'created'))
      ->condition('type', 'blog')
      ->condition('status', 1)
      ->orderBy('created', 'DESC')
      ->range(0, variable_get('blog_block_count', 10))
      ->addTag('node_access')
      ->execute();
```

The "node_access" tag tells implementations of hook_query_alter() that this query needs to be altered appropriately for "node_access"-relevant queries. Additional tags may also be used as desired. See the [handbook page](http://drupal.org/node/310077) for more information.

### Removed FILE_STATUS_TEMPORARY

[(issue)](http://drupal.org/node/353207) The FILE_STATUS_TEMPORARY constant has been removed. \$file-\>status is a bitmapped field and having FILE_STATUS_TEMPORARY for the 0 value of the bit didn't make any sense. To make a permanent file temporary use the inverse of the FILE_STATUS_PERMANENT constant:

``` php
$file->status &= ~FILE_STATUS_PERMANENT;
```

### New user_cancel API

[(issue)](http://drupal.org/node/8) Users can now cancel their own accounts, when the corresponding "cancel account" permission has been granted. There are multiple account cancellation methods, from which one can be configured as default. Users with the "administer users" permission are able to override the default method, f.e. to completely delete a user including all of the related content.

Each module should only do the appropriate action for the passed in \$method. All methods available in Drupal core by default are defined in [user_cancel_methods()](http://api.drupal.org/api/function/user_cancel_methods/7). Modules can enhance those methods by implementing [hook_user_cancel_methods_alter()](http://api.drupal.org/api/function/hook_user_cancel_methods_alter/7).

**IMPORTANT:** Please note that the default method for Drupal 7.x is `user_cancel_block`, which effectively only disables (blocks) a user account. Most modules should not need to alter any user data or information for this method.

### Taxonomy db table names have changed to begin with 'taxonomy\_'

[(issue)](http://drupal.org/node/225562)The names of the taxonomy database tables have changed to be consistent with our naming conventions. Each table has been prefixed with 'taxonomy\_'. Table vocabulary_node_types has also changed to the singular form: taxonomy_vocabulary_node_type.

- term_data -\> taxonomy_term_data
- term_hierarchy -\> taxonomy_term_hierarchy
- term_node -\> taxonomy_index (partly - but some information that used to be in term_node is now stored in field tables)
- term_relation -\> taxonomy_term_relation
- vocabulary -\> taxonomy_vocabulary
- vocabulary_node_types -\> taxonomy_vocabulary_node_type (singular)

### User pictures are now managed files

[(issue)](http://drupal.org/node/357403) The {users}.picture column is now a file id rather than a path. When a user is loaded with user_load() then \$user-\>picture is a file object.

### drupal_set_session() replaces \$\_SESSION

\[NEEDS UPDATE\]  
Note that drupal_set_session() is no longer being implemented so ignore this note and Coder's recommendation as well.  
(Amended in Coder as of 7.x-2.x-dev: [\#1844592: Coder still recommends using set_session()](/project/coder/issues/1844592 "Status: Closed (fixed)").)  
However, per discussion in IRC with Damien:  
- the reverse proxy changes are still there, including the lazy session start  
- so we probably need to keep a paragraph about that  
- we still do the same thing, but developers can access \$\_SESSION directly  
- what we need here is a paragraph that tell module developers not to over use the session, and to clean up session data as soon as possible

[\#201122: Drupal should support disabling anonymous sessions](/project/drupal/issues/201122 "Status: Closed (fixed)"): The \$\_SESSION superglobal should not be accessed directly. Instead, use [drupal_set_session(\$name, \$value)](http://api.drupal.org/api/function/drupal_set_session/7). This is a performance optimization so that no session is started for anonymous users unless a module has put data into the user's session. Note that it is important that modules try not to use \$\_SESSION for anonymous users. Such use ruins the optimization here. This optimization is particularly impressive when Drupal is coupled with a reverse proxy like Squid or Varnish.

### Ability to reset JavaScript and CSS

[(issue)](http://drupal.org/node/345973) If you need to reset the entire JavaScript or CSS, you can use [drupal_static_reset](http://api.drupal.org/api/function/drupal_static_reset/7), which will empty the cached values. Also take note of [hook_js_alter()](http://api.drupal.org/api/function/hook_js_alter/7).

``` php
// Reset all JavaScript that has been added.
drupal_static_reset('drupal_add_js');

// Reset all cascading stylesheets that have been added.
drupal_static_reset('drupal_add_css')
```

### Moved statistics settings from admin/reports/settings to ~~admin/settings/statistics~~ admin/config/system/statistics and added a new 'administer statistics' permission

[(issue)](http://drupal.org/node/80944) The settings page for the statistics module has been moved to the more appropriate location of ~~admin/settings/statistics~~ admin/config/system/statistics. A new permission (administer statistics) has been added in order to restrict access to the settings page.

### Default parameter when getting variables

[(issue)](http://drupal.org/node/88264) When using `variable_get` to retrieve variables, the `$default` parameter now defaults to `NULL`, so if you're getting a variable where you don't care about what the default is, then you don't have to pass "NULL" as the second parameter.

Drupal 6.x:

``` php
// Retrieve myawesomevariable. If it doesn't exist, retrieve NULL.
variable_get('myawesomevariable', NULL);
```

Drupal 7.x:

``` php
// Retrieve myawesomevariable. If it doesn't exist, this will return NULL.
variable_get('myawesomevariable');
```

### Menu "page callbacks" and blocks should return an array and hook_page_alter() (Render arrays discussion)

[(issue)](http://drupal.org/node/351235) Menu "page callbacks" and blocks should return a render array instead of a string. You are probably familiar with render arrays from Form API. These are arrays which [drupal_render()](http://api.drupal.org/api/function/drupal_render/7) knows how to process. The big benefit of returning an array is that sites may implement [hook_page_alter()](http://api.drupal.org/api/function/hook_page_alter/7) to change the contents of the array describing the page. For example, they could move some of the information to the 'left' region.

Your array should leave as many array elements unrendered as reasonably possible. For example, the default homepage has an array element for each node and another at the end for the pager. For examples of how some callbacks have been converted to arrays, see [node_page_default()](http://api.drupal.org/api/function/node_page_default/7) and [node_show()](http://api.drupal.org/api/function/node_show/7) and [blog_page_last()](http://api.drupal.org/api/function/blog_page_last/7) and [taxonomy_term_page()](http://api.drupal.org/api/function/taxonomy_term_page/7).

If you find yourself calling render() or drupal_render(), you're probably making a mistake.

### Block module now optional

[(issue)](http://drupal.org/node/367380) Modules and install profiles should be aware that block.module is enabled by default but no longer mandatory. Install profiles usually want to enable in the profile's info file by declaring it a dependency:  
`dependencies[] = block`

### Element \#type property no longer treated as a theme function in drupal_render()

[(issue)](http://drupal.org/node/355236) In previous versions of Drupal, `drupal_render()` used the value of an element's `#type` property as a theme function, and used the `#theme` property (if it was present) to override the default rendering of the element's *children.* Now, there are two explicit properties that control HTML generation: `#theme` and `#theme_wrappers`. `#theme` is the same as in Drupal 6: it can be used to override the normal rendering of the element's children. `#theme_wrappers` is called afterwards, and can be used to wrap markup around the rendered children. `drupal_render()` no longer uses the `#type` property to control theming. In addition, both `#theme` and `#theme_wrappers` can be overridden in alter hooks without changing an element's `#type.`

### Use drupal_render_children() to render an element's children

In Drupal 6, when an element was passed into `drupal_render()` with a custom `#theme` property, that theme function was expected to call `drupal_render($element)` a second time to render the element's children. In Drupal 7, calling `drupal_render()` on an element *in that element's own theme function* will cause an endless loop. The [drupal_render_children(\$elements)](http://api.drupal.org/api/function/drupal_render_children/7) function should be called instead.

Also see the [API docs for drupal_render()](http://api.drupal.org/api/function/drupal_render/7)

Drupal 6.x:

``` php
function theme_my_custom_element($element) {
  // Render one specific child of the current element.
  $output = '<blink>' . drupal_render($element['child1']) . '</blink>';

  // Render all the remaining children of the current element.
  $output .= drupal_render($element);
}
```

Drupal 7.x:

``` php
function theme_my_custom_element($element) {
  // Render one specific child of the current element.
  $output = '<blink>' . drupal_render($element['child1']) . '</blink>';

  // Render all the remaining children of the current element.
  $output .= drupal_render_children($element);
}
```

### ~~Replace node_view() with node_build()~~

~~[(issue)](http://drupal.org/node/351235)~~  
**Reverted in [\#658364: Does build/view/formatter terminology make sense?](/project/drupal/issues/658364 "Status: Closed (fixed)").**

### JavaScript should be compatible with libraries other than jQuery

[(issue)](http://drupal.org/node/125030). JavaScript should be made compatible with libraries other than jQuery by adding a small wrapper around your existing code:

``` php
(function ($) {
  // Original JavaScript code.
})(jQuery);
```

This wrapper is an anonymous closure that provides state throughout the page's lifetime and ensures your code does not unintentionally create/override global variables.

It also explicitly imports the global `jQuery` variable so that your code can use the local `$` variable instead of the `jQuery` global. This is essential because Drupal loads jQuery with `noConflict()` compatibility so the jQuery library does *not* setup the normal `$` as a global variable.

A detailed explanation of this JavaScript pattern can be found in the article [JavaScript Module Pattern: In-Depth](http://www.adequatelygood.com/2010/3/JavaScript-Module-Pattern-In-Depth).

### file_scan_directory()'s optional parameters are now an array

[(issue)](http://drupal.org/node/255551). [file_scan_directory()](http://api.drupal.org/api/function/file_scan_directory/7) had five optional parameters that have now been combined into an array making it easy to specify a single option without remembering all the default values.

Drupal 6.x:

``` php
file_scan_directory(file_create_path('css'), '/.*/', '/(\.\.?|CVS)$/', 'file_unmanaged_delete', TRUE);
```

Drupal 7.x:

``` php
file_scan_directory(file_prepare_directory('css', FILE_CREATE_DIRECTORY), '/.*/', array('callback' => 'file_unmanaged_delete'));
```

### External JavaScript can now be referenced through drupal_add_js()

[(issue)](http://drupal.org/node/91250) The [drupal_add_js()](http://api.drupal.org/api/function/drupal_add_js/7) function can now add reference to external JavaScript files by passing a 'external' type.

Drupal 6.x:

``` php
drupal_set_html_head('<script type="text/javascript" src="http://example.com/example.js" />');
```

Drupal 7.x:

``` php
drupal_add_js('http://example.com/example.js', 'external');
drupal_add_js('http://example.com/example.js', array('type' => 'external'));
```

### user_load_multiple() and hook_user_load(), user_load() signature change, and \$reset parameter

[user_load_multiple()](http://api.drupal.org/api/function/user_load_multiple/7) allows you to load multiple users with reduced queries. [user_load()](http://api.drupal.org/api/function/user_load/7) has had a signature change and now takes only a uid and optional \$reset parameter, as it is a thin wrapper around user_load_multiple(). [hook_user_load()](http://api.drupal.org/api/function/hook_user_load/7) now takes an array of user objects keyed by user ID, and acts on them by reference. Note that user objects may now be cached, so if user objects may have changed significantly, you should call user_load() or user_load_multiple() with the \$reset parameter set to TRUE: [user_load(\$uid, TRUE)](http://api.drupal.org/api/function/user_load/7).

If you want to load a user by name, try the new [user_load_by_name()](http://api.drupal.org/api/function/user_load_by_name/7).

### jQuery 1.3.x

[(issue)](http://drupal.org/node/350275) The move to [jQuery 1.3.x](http://docs.jquery.com/Release:jQuery_1.3) brought in a lot of JavaScript performance enhancements as well as a [number of other new features](http://docs.jquery.com/Release:jQuery_1.3#Features). In order to upgrade any module's JavaScript, see the [changes documentation](http://docs.jquery.com/Release:jQuery_1.3#Upgrading). The most common API change is:

jQuery 1.2.x:

``` php
$("a[@href*='admin/build/testing']").doSomething();
```

jQuery 1.3.x:

``` php
$("a[href*='admin/build/testing']").doSomething();
```

### Settings passed locally to JavaScript Behaviors

[(issue)](http://drupal.org/node/360081) Settings are now passed locally to Drupal's JavaScript behaviors rather than using the global Drupal.settings variable. This enables settings not part of the Drupal.settings to be used with the behaviors which is useful for AJAX/AHAH.

Drupal 6.x:

``` php
Drupal.behaviors.tableSelect = function(context) {
  $('#example', context).html(Drupal.settings.myvar);
};
```

Drupal 7.x:

``` php
Drupal.behaviors.tableSelect = {
  attach: function(context, settings) {
    $('#example', context).html(settings.myvar);
  }
};
```

### file_scan_directory() now uses same property names as file_load()

[(issue)](http://drupal.org/node/380064) [file_scan_directory()](http://api.drupal.org/api/function/file_scan_directory/7) previously returned objects with the properties `filename`, `basename`, and `name` (e.g., respectively, "foo/bar.txt," "bar.txt" and "bar"). `filename` has been renamed to `filepath`, and `basename` has been renamed to `filename`, i.e. the same names as used in objects returned by [file_load()](http://api.drupal.org/api/function/file_load/7).

### Moved filter module administrative URLs from admin/settings/filters/\* to admin/settings/filter/\*

[(issue)](http://drupal.org/node/244904) For greater consistency, administrative URLs in the Filter module have been renamed from plural to singular. Any hardcoded links to these URLs should be updated to point to the correct path. For example, instead of `url('admin/settings/filters/add')` (Drupal 6.x), use `url('admin/settings/filter/add')` (Drupal 7.x).

### Added taxonomy_vocabulary_load_multiple()

[(issue)](http://drupal.org/node/351797)

Taxonomy vocabularies have a [multiple load](http://api.drupal.org/api/function/taxonomy_vocabulary_load_multiple/7) function (similar to users, nodes, files and taxonomy terms). [taxonomy_get_vocabularies()](http://api.drupal.org/api/function/taxonomy_get_vocabularies/7) and [taxonomy_vocabulary_load()](http://api.drupal.org/api/function/taxonomy_vocabulary_load) remain as wrapper functions around multiple load, and also return full vocabulary objects.

### ~~Added a new top-level 'international' admin menu item~~

~~[(issue)](http://drupal.org/node/368064)  
A new top level 'international menu item has been provided at admin/international - all module exposing administrative pages dealing with internationalization and localization should group their pages under this link.~~

This is no longer the case. It looks like it is now admin/config/regional.  
[Locale](http://drupal.org/handbook/modules/locale)

### Changed hook_menu_link_alter() (removed the \$menu parameter)

([Issue](/node/317775))

Drupal 6.x:

``` php
function mymodule_menu_link_alter(&$item, $menu) {
  // Example 1 - make all new admin links hidden (a.k.a disabled).
  if (strpos($item['link_path'], 'admin') === 0 && empty($item['mlid'])) {
    $item['hidden'] = 1;
  }
}
```

Drupal 7.x:

``` php
function mymodule_menu_link_alter(&$item) {
  // Example 1 - make all new admin links hidden (a.k.a disabled).
  if (strpos($item['link_path'], 'admin') === 0 && empty($item['mlid'])) {
    $item['hidden'] = 1;
  }
```

### Standardized API for static variables and resetting them

([Issue](/node/254491)) A central facility is now available for holding static variable - these are typically used to cache expensive data during one page load. The advantage of using a central store is that some or all of the cached data can be cleared in a consistent fashion. For example, this will allow running Drupal a with a "clean slate" each time a test run starts, even if it's within the same page load. In addition, caches can be cleared when an object is saved - for example when a node is saved, the stored cache of previously loaded nodes can be cleared to avoid re-loading stale data.

This API contains only two functions , `drupal_static()` and `drupal_static_reset()`.  
The phpdoc for drupal_static() has documentation and usage examples.  
<http://api.drupal.org/api/function/drupal_static/7>

### The function drupal_set_html_head() has been renamed to drupal_add_html_head()

[(issue)](http://drupal.org/node/372563) In Drupal 6, the [drupal_set_html_head()](http://api.drupal.org/api/function/drupal_set_html_head/6) function, is misleading: it does not SET, but ADD HMTL header data. In Drupal 7, it has been renamed to [drupal_add_html_head()](http://api.drupal.org/api/function/drupal_add_html_head/7).

### Inline cascading stylesheets from drupal_add_css()

[(issue)](http://drupal.org/node/259368) Cascading stylesheets can now be added inline from a call to [drupal_add_css()](http://api.drupal.org/api/function/drupal_add_css/7). Stylesheets added in this way are not aggregated or cached, so it is usually best practice to use an actual file.

Drupal 6.x:

``` php
  $color = variable_get('backgroundcolor', '#FFFFFF');
  drupal_set_html_head("<style type='text/css'>body {background-color: $color}</style>");
```

Drupal 7.x:

``` php
  $color = variable_get('backgroundcolor', '#FFFFFF');
  drupal_add_css("body {background-color: $color}", 'inline');
```

### Attached JavaScript and CSS for forms

[(issue)](http://drupal.org/node/323112) Individual form elements now have the ability to define what JavaScript and cascading stylesheets are associated with them. This is stated in the [\#attached](http://api.drupal.org/api/file/developer/topics/forms_api_reference.html/7#attached) property.

Drupal 6.x:

``` php
function example_admin_settings() {
  // Add example.admin.css.
  drupal_add_css(drupal_get_path('module', 'example') .'/example.admin.css');
  // Add some inline JavaScript.
  drupal_add_js('alert("You are visiting the example form.");', 'inline');
  // Add a JavaScript setting.
  drupal_add_js(array('mymodule' => 'example'), 'setting');
  $form['example'] = array(
    '#type' => 'fieldset',
    '#title' => t('Example'),
  );
  return $form;
}
```

Drupal 7.x:  
Note: for a while, it was suggested to use \#attached_css and \#attached_js. Those functions are outdated and no longer work. Please use the examples below (\['#attached'\]\['css'\] & \['#attached'\]\['js'\])

``` php
function example_admin_settings() {
  $form['#attached']['css'] = array(
    // Add example.admin/css.
    drupal_get_path('module', 'example') . '/example.admin.css'
  );
  $form['#attached']['js'] = array(
    // Add some inline JavaScript.
    'alert("You are visiting the example form.");' => array('type' => 'inline'),
    // Add a JavaScript setting. Note that when the key is a number, the 'data' property will be used.
    array(
      'data' => array('mymodule' => array(...)),
      'type' => 'setting'
    ),
  );
  $form['example'] = array(
    '#type' => 'fieldset',
    '#title' => t('Example'),
  );
  return $form;
}
```

### Make sticky tableheaders optional

[(issue)](/node/336475) In previous Drupal versions table headers (if provided) would "stick" to the top of the screen when scrolling down. This is still enabled by default but the option has been added to disable this when theming a table.

(Note also that all Drupal 7 theme functions now take only two arguments, as described [here](#theme_changes).)

Drupal 6:

``` php
<?php
  // Sticky tableheaders always enabled.
  $table = theme('table', $headers, $rows, array(), NULL, array());
?>
```

Drupal 7:

``` php
<?php
  // With sticky tableheaders.
  theme('table', array('header' => $header, 'rows' => $rows));
  // Without sticky tableheaders.
  theme('table', array('header' => $header, 'rows' => $rows, 'sticky' => FALSE));
?>
```

### Save new users and nodes with specified IDs

[(issue)](/node/303965) When importing nodes or users, it is sometimes useful to preserve the ID from the legacy system. This is now possible by setting a nid or uid and setting the is_new property when calling node_save() or user_save().

### Parameters swapped in book_toc()

[(issue)](/node/361529)The non-optional parameter `$depth` followed the optional parameter `$exclude`. This has been corrected, the two parameters have swapped places.

Drupal 6.x

``` php
$toc = book_toc($bid, array(), 9);
```

Drupal 7.x

``` php
$toc = book_toc($bid, 9);
$toc = book_toc($bid, 9, array());
```

### drupal_execute() renamed to drupal_form_submit()

[(issue)](/node/408024) The function name `drupal_execute()` is fairly ambiguous about its function. The function has been renamed to `drupal_form_submit()` for better clarity.

### node_invoke_nodeapi() removed

[(issue)](/node/444876) The function node_invoke_nodeapi() has been removed. Use `module_invoke_all('node_' . $hook, $node);` where you used `node_invoke_nodeapi($node, $hook);`.

### Removed \$op "rss item" from hook_nodeapi() in favor of 'rss' view mode

[(issue)](/node/449718) \$op **rss item** of Drupal 6 [hook_nodeapi()](http://api.drupal.org/api/function/hook_nodeapi/6) was removed in favor of the `'rss'` view mode. Modules wishing to add RSS elements or namespaces to the node feed items should simply use the `$node->rss_elements` and `$node->rss_namespaces` attributes of the `$node` object, which are available with the `'rss'` view mode.

Example from taxonomy.module:  
In Drupal 6:

``` php
/**
 * Implements hook_nodeapi().
 */
function taxonomy_nodeapi($node, $op, $arg = 0) {
  switch ($op) {
    case 'rss item':
      $output = array();
      foreach ($node->taxonomy as $term) {
        $output[] = array(
          'key'   => 'category',
          'value' => check_plain($term->name),
          'attributes' => array('domain' => url('taxonomy/term/'. $term->tid, array('absolute' => TRUE)))
        );
        return $output;
      }
      break;
  }
}
```

In Drupal 7:

``` php
/**
 * Implements hook_node_view().
 */
function taxonomy_node_view($node, $view_mode) {
  if ($view_mode == 'rss') {
    foreach ($node->taxonomy as $term) {
      $node->rss_elements[] = array(
        'key' => 'category',
        'value' => $term->name,
        'attributes' => array('domain' => url(taxonomy_term_path($term), array('absolute' => TRUE))),
      );
    }
  }
}
```

Adding namespaces is done in the same manner outlined above, but using `$node->rss_namespaces`. Example:

``` php
$node->rss_namespaces['xmlns:example'] = 'http://example.com/example-namespace';
```

### drupal_eval() renamed to php_eval

[(issue)](/node/124158) The remaining PHP handling call `drupal_eval()` was moved to the PHP module. The function has been renamed to `php_eval()` to obey the coding standards. Since this is an optional module, your code should no longer assume that php_eval is always available, and should be wrapped in a `module_exists('php')` check.

In Drupal 6:

``` php
drupal_eval('<?php print "Hello World"; ? >');
```

In Drupal 7:

``` php
if (module_exists('php')) {
  php_eval('<?php print "Hello World"; ? >');
}
```

### "use PHP for settings" permission should be used for all PHP settings rights (replaces "use PHP for block visibility")

[(issue)](/node/124158) The block module-specific "use PHP for block visibility" was replaced by a more generic permission, handled by the PHP module: "use PHP for settings". If you re-used this permission in your code make sure to use the new permission title. If your module had its own PHP visibility permission, replace it with the generic one to simplify the site administration.

### Changes to HTTP header functions

[(issue)](http://drupal.org/node/451604), [(issue)](http://drupal.org/node/147310) and [(issue)](/node/732486) [drupal_set_header()](http://api.drupal.org/api/function/drupal_set_header/7) now takes the header name and header value as two separate arguments rather than as one complete header line, and has been renamed to [drupal_add_http_header](http://api.drupal.org/api/function/drupal_add_http_header/7). The function now also supports appending to and removing existing headers.

Drupal 6.x:

``` php
drupal_set_header('Content-Type: text/plain');
```

Drupal 7.x:

``` php
drupal_add_http_header('Content-Type', 'text/plain');
```

When setting the HTTP status code, the server protocol (e.g. "HTTP/1.1") should no longer be included.

Drupal 6.x:

``` php
drupal_set_header($_SERVER['SERVER_PROTOCOL'] . ' 500 Internal server error');
```

Drupal 7.x:

``` php
drupal_add_http_header('Status', '500 Internal server error');
```

[drupal_get_headers()](http://api.drupal.org/api/function/drupal_get_headers/6) has been renamed to [drupal_get_http_header()](http://api.drupal.org/api/function/drupal_get_http_header/7) and now also supports returning only the header with a given name.

The array returned from [hook_file_download()](http://api.drupal.org/api/function/hook_file_download) should now be a name/value array instead of an array of complete header lines.

Drupal 6.x:

``` php
function mymodule_file_download($filepath) {
  if (_mymodule_access($filepath)) {
    return array(
      'Content-Type: text/plain',
    );
  }
}
```

Drupal 7.x:

``` php
function mymodule_file_download($filepath) {
  if (_mymodule_access($filepath)) {
    return array(
      'Content-Type' => 'text/plain',
    );
  }
}
```

### drupal_get_form() returns a render array instead of a string

[(issue)](http://drupal.org/node/353069) [drupal_get_form()](http://api.drupal.org/api/function/drupal_get_form/7) no longer renders your form to an HTML string. Instead, it returns a render array as expected by drupal_render(). Your module should strive to keep this array structure, and return an array in your menu callback. You are welcome to add/modify the array as you wish. Only under severe distress should you call drupal_render(drupal_get_form()) in order to mimic previous versions of Drupal. Returning an array lets developers make easy changes during [hook_page_alter()](http://api.drupal.org/api/function/hook_page_alter/7).

For related details see [Menu "page callbacks" and blocks should return an array and hook_page_alter()](#menu_callback_array).

### Add Doxygen @file tag to all install files

[(issue)](http://drupal.org/node/320011) To standardize [code documentation](http://api.drupal.org/api/files/7), add doxygen `@file` to all .install files :

``` php
/**
 * @file
 * Install, update and uninstall functions for the XXX module.
 */
```

### Add node_delete_multiple()

[(issue)](http://drupal.org/node/). When you need to delete multiple nodes at a time, use the new [node_delete_multiple()](http://api.drupal.org/api/function/node_delete_multiple/7) function which is faster than calling node_delete() many times. node_delete() still exists  
for the single delete situation.

### Renamed drupal_set_content() and drupal_get_content()

[(issue)](http://drupal.org/node/428744). In Drupal 6, you could add content to a region with drupal_set_content() and request the full contents of a region with drupal_get_content(). These were renamed in Drupal 7 to [drupal_add_region_content()](http://api.drupal.org/api/drupal/includes--common.inc/function/drupal_add_region_content/7) and [drupal_get_region_content()](http://api.drupal.org/api/drupal/includes--common.inc/function/drupal_get_region_content/7). Apart from renaming them, functionality is the same.

Drupal 6:

``` php
// Add our own text to the footer.
drupal_set_content('footer', 'Adding custom text to footer');
// Get the complete footer contents.
$full_footer = drupal_get_content('footer');
```

Drupal 7:

``` php
// Add our own text to the footer.
drupal_add_region_content('footer', 'Adding custom text to footer');
// Get the complete footer contents.
$full_footer = drupal_get_region_content('footer');
```

### Instead of theme('page', ...), think of drupal_set_page_content()

[(issue)](http://drupal.org/node/428744). In Drupal 6, theme('page', ...) had a dual purpose. It was used to set the main page content text of the page and set some page display options (such as to hide the sidebars).

Drupal 7 made the page content an actual block, so setting the page content is done with the new drupal_set_page_content(). This can now take a string (rendered HTML) or a render array. By default, Drupal runs the output of page callbacks through rendering, so returning a string or array from your page callback is preferred. Drupal will call drupal_set_page_content() later anyway.

The only case when you need to call drupal_set_page_content() is when you need to alter page options. In that case, use element_info('page') to request the default page attributes (an array in Drupal 7), and modify them as needed. Set the page content with drupal_set_page_content() and return with that array from your page callback.

To reiterate, the basic use case did not change:

Drupal 6:

``` php
function mymodule_page_callback() {
  // Assemble page output here...

  // Return page output for Drupal.
  return $output;
}
```

Drupal 7:

``` php
function mymodule_page_callback() {
  // Assemble page output here...

  // Return page output for Drupal.
  return $output;
}
```

If you've used theme('page', ...) as a wrapper on your return value, but only passed on the output (not any of the other parameters), just remove it. This was already the suggested behavior in previous Drupal versions, so it is time to get rid of theme('page').

Drupal 6:

``` php
function mymodule_page_callback() {
  // Assemble page output here...

  // Return page output for Drupal.
  return theme('page', $output);
}
```

Drupal 7:

``` php
function mymodule_page_callback() {
  // Assemble page output here...

  // Return page output for Drupal.
  return $output;
}
```

If you need to alter page attributes, you can use the following approach. This can be used to alter the page output for one of your module's page callbacks. For example, to have one of your module's page callbacks not display any sidebars:

Drupal 6:

``` php
function mymodule_page_callback() {
  // Assemble page output here...

  // Return page output for Drupal, hide blocks.
  return theme('page', $output, FALSE);
}
```

Drupal 7:

``` php
function mymodule_page_callback() {
  // Assemble page output here...

  // Set page content for Drupal.
  drupal_set_page_content($output);
  // Return page attributes, and add a custom attribute to
  // look for in hook_page_alter().
  $page = element_info('page');
  $page['#mymodule_hide_blocks'] = TRUE;
  return $page;
}

function mymodule_page_alter(&$page) {
  // If the custom attribute is present, hide the blocks.
  if (isset($page['#mymodule_hide_blocks'])) {
    unset($page['sidebar_first'], $page['sidebar_second']);
  }
}
```

In short, always return the main page content in a string or render array unless you need to modify page attributes. In this later case, use drupal_set_page_content() and element_info('page') and return the modified attributes.

### theme('box') no longer exists

[(issue)](http://drupal.org/node/372471) The amorphous box.tpl.php template, the theme_box() function, and the ability to call theme('box'), have been removed. Those pieces of content that were using the box.tpl.php now have their own theme functions:

- The search results listings are themed with theme('search_results').
- The comment form box is themed with theme('comment_form_box').

If you have code calling theme('box'), you will need to add a new custom theme function to your module handle it, and an entry in your module's hook_theme().

### Node Body and Teaser Changes

[(issue)](http://drupal.org/node/372743) In Drupal 7 the node body becomes a field in core. This means the body field has changed from a specially handled node field to a field handled with the [Field API](http://api.drupal.org/api/group/field/7).

To understand how it is handled in Drupal 7, it helps to understand how it was handled in Drupal 6. In Drupal 6, the body and teaser were values added to the node by the node module. The body optionally contained code for a teaser break. If the break was present, the teaser contained a copy of all the content in the body up to the teaser break. If it was missing, the teaser contained a snippet from the body, and the size of the snippet was controlled by a site-wide 'post size' configuration setting.

In addition, the Drupal 6 code had an optional 'teaser splitter'. If the teaser splitter was used, it separated the 'body' into two separate textareas with different text, one for the body and one for the teaser. If it was not used, the body behaved noted above.

In the migration to Drupal 7, it was necessary to migrate the data into a field that was comprised of two different textareas that could be displayed in the different ways that the Drupal 6 body and teaser were displayed. To accomplish this, a 'Long text and summary' field was created, which contains a textarea for the body along with an optional textarea for the teaser. This new field has options to display the teaser using either the text that is in the teaser field or as a snippet from the body text of a stated size.

This change results in the following:

- The body field is a field in core of type: Long text and summary (text_with_summary)
- The `$node->teaser` field no longer exists
- The `$node->body` field still exists but it is an array and contains the body, the teaser, the format and the language of the field.
- The JavaScript splitter is no longer used on the node data entry form (If you want to recreate this behavior an example can be found in the [Drupal 6 Node Comment module](http://cvs.drupal.org/viewvc.py/drupal/contributions/modules/nodecomment/nodecomment.module?r1=1.3.2.15.2.17.2.16&r2=1.3.2.15.2.17.2.17&pathrev=DRUPAL-6--2))

The structure of the new body field looks like the following.

``` php
  $node->body = array(
    'und' => array(
      array(
        'value'  => 'body here',
        'summary' => 'teaser here',
        'format' => '1',
        'safe_value' => 'sanitized body',
        'safe_summary' => 'sanitized teaser',
      )
    ),
  );
```

The 'und' value is the language of the field. The language value could be 'und' (undefined) for sites that do not use the translation system or might be 'en' or 'fr' or whatever language the body field uses.

If you manually select values to display to the user in a template you should always use the 'safe_value' and the 'safe_summary' rather than the raw text from 'value' and 'summary'. The 'safe' values have been sanitized.

The 'format' contains the machine name of the format for this content, using the value from the filter_format table. Note that sites migrated from Drupal 6 will have filter format machine names that match the original numeric value of the format, but newly created Drupal 7 sites will have format values like 'filtered_text'.

The data entry form processing rules for the new *Summary* and *Full text* formatter is:

- If Summary text exists, it is used for the Teaser view
- If no Summary text exists, a trimmed version of Full text is used
- The length of the trimmed version is set in the node type's display settings
- The length of the Full text trimmed version can be manually set with \<!--break--\>

If your module changes user-facing behavior on node data entry forms familiarize yourself with the Field API widgets and formatters.

The following functions have been removed:

- `node_prepare()`. `$node->body` and `$node->teaser` no longer need special preparation.
- `node_body_field()`. The form element 'body' is now generated by Field API
- `node_teaser()` has been renamed to `text_summary()`. The function now runs `htmlcorrector` if applicable.

### Node access hooks now have drupal_alter() functions

[Node access](http://api.drupal.org/api/group/node_access/7) modules establish rules for user access to content. Node access records are stored in the {node_access} table and define which permissions are required to access a node.

Node access records are created with hook_node_access_records() and enforced by hook_node_grants().

In versions prior to Drupal 7, you could not modify the node access records or grants set by other modules. Now, to facilitate custom business logic, you may use a drupal_alter() hook to modify the records and grants passed by other modules.

[hook_node_access_records_alter(&\$grants, \$node)](http://api.drupal.org/api/function/hook_node_access_records_alter/7) runs after all node access records have been gathered, but *before they are written to the database*. Developers may modify the \$grants array by reference to change the records stored in {node_access}.

[hook_node_grants_alter(&\$grants, \$account, \$op)](http://api.drupal.org/api/function/hook_node_grants_alter/7) runs after all user access grants have been gathered, but *before those grants are used to restrict user access to node content*. Developers may modify the \$grants array by reference to change the queries run against the {node_access} table.

See the API documentation for example uses of these functions. You may also [read the background for this feature](http://drupal.org/node/309007).

### ~~Hide empty menu categories with access callback~~

[(issue)](http://drupal.org/node/296693) ~~Menu categories may now be hidden via the function [system_admin_menu_block_access()](http://api.drupal.org/api/function/system_admin_menu_block_access/7) when a user does not have permission to access any sub menu items. Once the menu category item has been updated to use `access arguments` menu categories with no accessible sub menu items will be hidden from users. If the new option is omitted administration menu items will behave as they did in Drupal 6 (categories will display even if no sub menu items are accessible to the user).~~

In Drupal 7:

``` php
$items['admin/content'] = array(
  'title' => 'Content management',
  'description' => "Manage your site's content.",
  'page callback' => 'system_admin_menu_block_page',
  'access callback' => 'system_admin_menu_block_access',
  'access arguments' => array('admin/content', 'access administration pages'),
);
```

~~The parameters for `access arguments` are as follows:~~

1.  ~~url of the menu category item~~
2.  ~~the permission the user needs to see the menu category item~~

### Commenting style - use 'Implements hook_foo().' when documenting hooks

[(issue)](http://drupal.org/node/472642) Commenting style for documenting hook_X() functions has changed.

Drupal 6:

``` php
/**
 * Implementation of hook_help().
 */
function blog_help($section) {
```

Drupal 7:

``` php
/**
 * Implements hook_help().
 */
function blog_help($section) {
```

### node_get_types(\$op) replaced by node_type_get\_\$op()

[(issue)](http://drupal.org/node/220233) Instead of a single function with several different return types, there are now several functions available.

Drupal 6:

``` php
// Load all node types and resets the static cache.
$types = node_get_types('types', NULL, TRUE);

// Get the node type name of a specific node.
$name = node_get_types('name', $node);
```

Drupal 7:

``` php
// Load all node types and resets the static cache.
node_types_rebuild();
$types = node_type_get_types();

// Get the node type name of a specific node.
$name = node_type_get_name($node);
```

As seen in the example, there is now a separate function, node_types_rebuild(), to clear the static cache. For more documentation, see the [API documentation](http://api.drupal.org/api/search/7/node_type_get).

### Added hook_block_info_alter()

[(issue)](http://drupal.org/node/370172)Modules can now add their own rules for block visibility to core's page, user and PHP defaults by manipulating the list of blocks before it is rendered. If your module currently uses db_rewrite_sql() or hook_query_alter() to alter the blocks list, you should consider converting to use this hook instead.

See the [API documentation](http://api.drupal.org/api/function/hook_block_info_alter/7) for details.

### Renamed module_rebuild_cache() to system_rebuild_module_data(), renamed system_theme_data() to system_rebuild_theme_data(), and added system_get_info()

Issues:  
[\#147000: Rewrite module_rebuild_cache() and system_theme_data()](/project/drupal/issues/147000 "Status: Closed (fixed)")  
[\#561452: Add API function to get module/theme info without rebuilding it.](/project/drupal/issues/561452 "Status: Closed (fixed)")

The existing functions for rebuilding and returning information about modules and themes have been renamed to have a more consistent API and share internally used functions.

In addition, a new, simple function has been added to return stored information about active modules or themes from the database (without forcing a full rebuild of that information via a scan of the filesystem).

See the API documentation for [system_rebuild_module_data()](http://api.drupal.org/api/function/system_rebuild_module_data/7), [system_rebuild_theme_data()](http://api.drupal.org/api/function/system_rebuild_theme_data/7), and [system_get_info()](http://api.drupal.org/api/function/system_get_info/7) for details.

### Added string context support to t() and format_plural(), changed parameters

[(issue)](http://drupal.org/node/334283) Before Drupal 7, the localization system was only capable of mapping the same character sequence to the same translation for a given language, regardless of the usage context. This results in errors in translations when simple strings like "view" or "track" are translated. "Track" for example can be used as a label when tracking users or a label for a music track in a media module. While English has the same string for both cases, other languages need different translations. The same issue applies to "May" as a month name in Drupal core. English uses "May" for both the short and long name of the month, so it was impossible to translate it to a short and long version in other languages. Therefore Drupal 6 introduced the !long-month-name prefix for long month names, but that was a one-off hack.

In Drupal 7, optional translation contexts were added. To make the optional parameters to t() and format_plural() easier to use, this also resulted in the existing \$langcode parameter being folded into an \$options array.

In Drupal 6:

``` php
// Translate to German.
t('Welcome to our site', array(), 'de');
// Translate to German with replacement.
t('!user, welcome to our site', array('!user' => theme('username', $user)), 'de');
// Translate May in the long version to current page language.
t('!long-month-name May');
// Translate May in the short version to current page language.
t('May');
// Translate May in the long version to German.
t('!long-month-name May', array(), 'de');
// Translate May in the short version to German.
t('May', array(), 'de');
```

In Drupal 7:

``` php
// Translate to German.
t('Welcome to our site', array(), array('langcode' => 'de'));
// Translate to German with replacement.
t('!user, welcome to our site', array('!user' => theme('username', array('account' => $user))), array('langcode' => 'de'));
// Translate May in the long version to current page language.
t('May', array(), array('context' => 'Long month name'));
// Translate May in the short version to current page language.
t('May');
// Translates May in the long version to German.
t('May', array(), array('context' => 'Long month name', 'langcode' => 'de'));
// Translate May in the short version to German.
t('May', array(), array('langcode' => 'de'));
```

To recap, \$langcode becomes an \$options array with the possible keys 'langcode' and 'context'. The 'context' is freely defined by your module; Drupal core only defines the 'Long month name' context which is used for the long month names. Because setting a custom 'context' disables sharing translations of your module strings with other modules not using the same context, you should think twice before introducing contexts.

### AHAH/AJAX Processing has changed; \#ajax, new 'callback' member of the array, and the callback must be rewritten

There are several changes here:

- \#ahah (D6) is now \#ajax (D7).
- The 'path' is now replaced in most cases by 'callback' (They are mutually exclusive.)
- Wrapper replacement has changed.

AHAH processing is now called AJAX processing, and the Forms API marker changes from \#ahah to \#ajax.

In addition, AJAX/AHAH processing is now far easier. Instead of setting up a discrete menu path and a callback function to be called by it, just use the 'callback' configuration element.

*Note that the old 'path' technique is still supported by \#ajax, but the menu function it would call must be rewritten if you stay with 'path'.*

Drupal 6:

``` php
$item['something'] = array(
  '#type' => 'submit',
  '#ahah' => array(
    'path' => 'some/callback',    // A path, not a function.
    'wrapper' => 'wrapper-to-replace',
  ),
);
```

Drupal 7:

``` php
$item['something'] = array(
  '#type' => 'submit',
  '#ajax' => array(
    'callback' => 'my_callback_function',   // A function, not a path.
    'wrapper' => 'wrapper-to-replace',
  ),
);
```

In Drupal 7, you *do not have* to declare the callback path in hook_menu(), and the callback function is far simpler.

Drupal 6:  
(For full information on the callback in D6, see <http://drupal.org/node/331941>)

``` php
// This function must be pointed to in hook_menu() in D6.
function my_callback_function() {
  // ... Much work to build the form ....

  drupal_process_form($form_id, $form, $form_state);
  $form = drupal_rebuild_form($form_id, $form_state, $args, $form_build_id);

  $output = drupal_render($form);

  // Final rendering callback.
  print drupal_json(array('status' => TRUE, 'data' => $output));
  exit();
}
```

Drupal 7:

``` php
// No path needs be set up to point to the function, and $form and $form_state are provided.
function my_callback_function($form, &$form_state) {
  // Often you would select a portion of the form to match #ajax['wrapper']
  // rather than processing the whole form.
  return $form;  // Either HTML or a render array may be returned.
}
```

Finally, wrapper replacement has changed. In Drupal 6, the javascript code replace only the *contents* of the wrapper element. In Drupal 7, it replaces the entire element. So for a wrapper with ID 'my-wrapper'

``` php
<div id="my-wrapper">some contents</div>
```

in Drupal 7, the replacement html returned by the callback or path function would be the entire div, whereas in Drupal 6 it would have been just the replacement text for "some contents".

The Drupal 7 version of the [examples module](http://drupal.org/project/examples) now has an AJAX example showing in depth how AJAX can be used with form elements.

### Alternative cache implementations changed

Previously you put `cache_get`, `cache_set` and `cache_clear_all` in a file and changed the cache_inc variable to point to this file. You need to implement the `get`, `set` and `clear` methods which get the same arguments as they did in D6 minus the bin. The bin was called table in Drupal 6. So here are the steps to convert:

1.  Wrap your implementation in `class MyCacheImplementation implements DrupalCacheInterface { ... } `

2.  Change the function name to get, set, clear.

3.  Remove the \$table argument from each function header.

4.  Add a new function  

    ``` php
     function __construct($bin) {
        $this->bin = $bin;
      }
    ```

    .

5.  Search-and-replace \$table with \$this-\>bin.

### \$teaser parameter changed to \$view_mode in node viewing functions and hooks, \$node-\>build_mode property removed

[(issue)](http://drupal.org/node/409750) The \$node-\>build_mode property, set before viewing a node, has been removed in favor of a new \$view_mode string parameter for the various functions and hooks related to node view, in place of the previous \$teaser Boolean parameter.

Drupal 6:

``` php
$node->build_mode = NODE_BUILD_NORMAL;
$output = node_view($node, TRUE);
```

Drupal 7:

``` php
$content = node_view($node, 'teaser');
$output = drupal_render($content);
```

Drupal 6:

``` php
/**
 * Implements hook_nodeapi().
 */
function comment_nodeapi($op, $node, $teaser) {
  switch ($op) {
    ...
    case 'view':
      if ($node->build_mode == NODE_BUILD_RSS) {
        ...
      }
      break;
    ...
  }
}
```

Drupal 7:

``` php
/**
 * Implements hook_node_view().
 */
function comment_node_view($node, $view_mode) {
  if ($view_mode == 'rss') {
    ...
  }
}
```

The affected functions and hooks are: [node_view()](http://api.drupal.org/api/function/node_view/7), [hook_view()](http://api.drupal.org/api/function/hook_view/7), [hook_node_view()](http://api.drupal.org/api/function/hook_node_view/7) (previously [node_nodeapi('view')](http://api.drupal.org/api/function/node_nodeapi/6) in Drupal 6 - see [here](http://drupal.org/node/224333#remove_op)), [hook_node_view_alter()](http://api.drupal.org/api/function/hook_node_view_alter/7) (new in Drupal 7), [hook_link()](http://api.drupal.org/api/function/hook_link/7)

An additional \$view_mode variable is available in node templates. For easier theme portability, the previous \$teaser variable is still declared (` == ('$view_mode = 'teaser')`).

Core-defined view modes have been moved from numeric constants to plain strings, to make it easier for contributed modules to expose additional view modes (in [hook_entity_info()](http://api.drupal.org/api/function/hook_entity_info/7) and [hook_entity_info_alter()](http://api.drupal.org/api/function/hook_entity_info_alter/7)):  
NODE_BUILD_NORMAL (0) is now either 'full' or 'teaser'  
NODE_BUILD_PREVIEW (1) was replaced by a \$node-\>in_preview Boolean flag.  
NODE_BUILD_SEARCH_INDEX (2) is now 'search_index'  
NODE_BUILD_SEARCH_RESULT (3) is now 'search_result'  
NODE_BUILD_RSS (4) is now 'rss'  
NODE_BUILD_PRINT(5) is now 'print'

Contributed modules are encouraged to declare new view modes when they need a custom presentation of a node. Site admins will then be able to manage which fields appear and how those fields are formatted using the Fields UI. For example, an 'Email this page to a friend' module would declare an 'email to friend' build mode using [hook_entity_info_alter()](http://api.drupal.org/api/function/hook_entity_info_alter/7).

### comment_save() now supports programmatic saving

All form-related logic has been removed from comment_save(), making it possible to use the function to save comments programmatically, similar to node_save(). The function arguments and their structure remain unchanged, but be aware that no validation is performed. Sensible defaults are provided for the following values: mail, homepage, name, status, timestamp -- all other data related to the inserting/updating of a comment is required.

### comment_validate() has been removed

[(issue)](http://drupal.org/node/335034) Use comment_form_validate() for all form-related validation of comments.

### Login validation change for distributed authentication modules

Modules which perform external authentication should now set \$form_state\['uid'\] to the ID of the user who is logging in. They should not load global \$user anymore. If wrong credentials are presented, modules continue to do nothing - core will return an invalid credentials message.

Example from the 7.x openid.module: (The Drupal UID is already known for this otherwise authenticated user)

``` php
<?php
        $form_state['uid'] = $account->uid;
        user_login_submit(array(), $form_state);
?>
```

### Some login validation functions were removed or changed

[(issue)](http://drupal.org/node/497612) Besides the change noted in the section above on login validation, several login-related functions were changed:

- user_external_login() was removed.  
  Drupal 6:

  ``` php
  user_external_login($account);
  ```

  Drupal 7:

  ``` php
  user_login_submit(array(), array('uid' => $account->uid));
  drupal_goto();
  ```

- The arguments of user_authenticate() changed. See the API documentation in [user_authenticate (Drupal 6)](http://api.drupal.org/api/drupal/modules--user--user.module/function/user_authenticate/6) and [user_authenticate (Drupal 7)](http://api.drupal.org/api/drupal/modules--user--user.module/function/user_authenticate/7) for details.

- The function user_authenticate_finalize() became user_login_finalize().

### jQuery UI (1.7) was added into core

[(issue)](http://drupal.org/node/315035) jQuery UI 1.7 was added into core. You can find the jQuery UI files in misc/ui and can add Javascript and CSS files from there to your pages with the regular drupal_add_js() and drupal_add_css() calls, no special function calls required. If you are migrating a module or custom code which was previously dependent on the jquery_ui contributed module, the difference in usage is:

Drupal 6 with jquery_ui module:

``` php
jquery_ui_add(array('ui.accordion', 'ui.dialog'));
```

Drupal 7 core:

``` php
drupal_add_library('system', 'ui.accordion');
drupal_add_library('system', 'ui.dialog');
```

Read more about [drupal_add_library below](#drupal_add_library). Drupal ships with the minified versions of jQuery UI files, just like we do in case of jQuery itself.

### comment_node_url() has been removed

[(issue)](http://drupal.org/node/506650) Use 'comment/' . \$comment-\>cid to build URLs instead.

### \#theme recommended for specifying theme function

[(issue)](http://drupal.org/node/373201)Now that menu callbacks should return arrays, we encourage render elements to use \#theme to specify a theme function instead of using \#markup =\> theme('foo', ...). This delays theming until later which gives [hook_page_alter()](http://api.drupal.org/api/function/hook_page_alter/7) a chance to make changes. Note that you may pass parameters to theme() by creating \#properties that match the name of the theme function parameter. Note that this feature applies to theme functions, not theme templates. For example, given that the theme declaration for 'image' \[from drupal_common_theme()\] is:

``` php
    'image' => array(
      'variables' => array('path' => NULL, 'alt' => '', 'title' => '', 'attributes' => array(), 'getsize' => TRUE),
    ),
 
```

In 6.x you would have done something like this:

``` php
$node->content['extra_picture'] = array(
  '#markup' => theme('image', 'http://foo.com/test.jpg', NULL, t('A title'), array('class' => 'external-image'), FALSE),
  '#weight' => 5,
);
```

In 7.x:

``` php
$node->content['extra_picture'] = array(
  '#theme' => 'image',
  '#path' => 'http://foo.com/test.jpg',
  '#title' => t('A title'),
  '#attributes' => array('class' => 'external-image'),
  '#getsize' => FALSE,
  '#weight' => 5,
);
```

Note that the names of the attributes here correspond to the names of the variables in the theme declaration (aside from '#theme', which gives the name of the theme, and '#weight', which orders this within the content of the node) .

### hook_perm() renamed to hook_permission()

[(issue)](http://drupal.org/node/506976) For clarity, hook_perm() has been renamed hook_permission().

### Ability to add multiple JavaScript/CSS files at once

[(issue)](http://drupal.org/node/315100) You can add related sets of JavaScript and CSS at once now with the [drupal_add_library()](http://api.drupal.org/api/function/drupal_add_library/7) function. The first argument is the name of the module that registers the library (via [hook_library](http://api.drupal.org/api/function/hook_library/7)), while the second argument is the name of the library you want to add.

Drupal 6:

``` php
  // Adds Farbtastic color picker.
  drupal_add_js('misc/farbtastic/farbtastic.js');
  drupal_add_css('misc/farbtastic/farbtastic.css');
```

Drupal 7:

``` php
  // Adds Farbtastic color picker.
  drupal_add_library('system', 'farbtastic');
```

These sets of JavaScript/CSS libraries must be registered through [hook_library](http://api.drupal.org/api/function/hook_library/7):

``` php
  function system_library() {
    $libraries['farbtastic'] = array(
      'title' => 'Farbtastic',
      'website' => 'http://code.google.com/p/farbtastic/',
      'version' => '1.2',
      'js' => array(
        'misc/farbtastic/farbtastic.js' => array(),
      ),
      'css' => array(
        'misc/farbtastic/farbtastic.css' => array('preprocess' => FALSE),
      ),
    );
    return $libraries;
  }
```

The library registry can also be altered through [hook_library_alter](http://api.drupal.org/api/function/hook_library_alter/7). This becomes useful if you are updating the library to a newer version.

### Removed taxonomy module support for multiple tids and depth in term paths

[(issue)](http://drupal.org/node/503456). Support for multiple tids and depth arguments for taxonomy term paths has been removed from core. This feature is still provided by Views, so if your module relies on those paths, you should add Views as a dependency and/or provide default views providing the same behaviour.

### file_prepare_directory() (replacement for file_check_directory() will now recursively create directories

[(issue)](http://drupal.org/node/515280). Previously [file_check_directory()](http://api.drupal.org/api/function/file_check_directory/6) would only create a directory if all its parent directories already existed. PHP 5 added the feature to [mkdir()](http://php.net/mkdir) to make it create directories recursively, which we can now use in the replacement [file_prepare_directory()](http://api.drupal.org/api/function/file_prepare_directory/7) since Drupal 7 requires PHP 5.

Drupal 6:

``` php
// Recursively add new directories if the parent does not exist.
$full_path = '';
foreach (explode('/', $directory) as $path) {
  $full_path .= $path;
  file_check_directory($full_path, FILE_CREATE_DIRECTORY);
  $full_path .=  '/';
}
```

Drupal 7:

``` php
// Recursively add new directories if the parent does not exist.
file_prepare_directory($directory, FILE_CREATE_DIRECTORY);
```

### Added comment_load_multiple() and hook_comment_load()

[(issue)](http://drupal.org/node/502538) . Comment module was converted from using direct queries in comment_render() to a new comment_load_multiple() central function for loading comments. If loading comments outside comment_render(), you should use comment_load() or comment_load_multiple() to ensure all hooks are correctly fired. See the [API documentation](http://api.drupal.org/api/function/comment_load_multiple/7) for further details.

### hook_node_access_records() now applies to unpublished nodes; 'view own unpublished content' permission added

[(issue)](/node/452538) In Drupal 6, any node grants provided by hook_node_access_records() would only apply to published nodes. For unpublished nodes, users were granted view access if they were the author.

In Drupal 7, hook_node_access_records() now applies to both published and unpublished nodes, giving the developer more flexibility to manage node access. Also, the 'view own unpublished content' was added to still grant users view access to their own unpublished content. This permission is granted to authenticated users by default in a Drupal 7 installation or upgrade.

If developers still want their implementation of hook_node_access_records() to apply only to published nodes in Drupal 7, they need only add these three lines of code to the top of the function.

``` php
if (!$node->status) {
  return;
}
```

### MIME types list changed from variable to hook

[(issue)](http://drupal.org/node/331171) Drupal maintains a list of default MIME types for files, and uses it in function file_get_mimetype() if one is not provided as a function argument. In Drupal 6, the default list of MIME types came from variable_get('mime_extension_mapping'). In Drupal 7, it comes from function [file_mimetype_mapping()](http://api.drupal.org/api/drupal/includes--file.mimetypes.inc/function/file_mimetype_mapping/7), which invokes [hook_file_mimetype_mapping_alter()](http://api.drupal.org/api/drupal/modules--system--system.api.php/function/hook_file_mimetype_mapping_alter/7) on the default list.

So, if your module did something to alter the 'mime_extension_mapping' variable in Drupal 6, it should instead implement hook_file_mimetype_mapping_alter() in Drupal 7. And if your module used the 'mime_extension_mapping' variable in Drupal 6, it should instead call file_mimetype_mapping() to get the list in Drupal 7.

### hook_footer() was removed, \$closure became \$page_bottom, \$page_top added

[(issue 1)](http://drupal.org/node/519782), [(issue 2)](http://drupal.org/node/511284) Drupal 6 used hook_footer() to add content to a special variable named \$closure which was mandatory to put in themes to the bottom of the HTML body output. Drupal 7 generalizes this under hook_page_build(), hook_page_alter(), and hidden regions.

Drupal 7 now comes with two hidden default regions internally named page_bottom and page_top. They are hidden in that they will not show up in the blocks administration interface, but they can receive programmatic data. The corresponding template variables are \$page_bottom and \$page_top, and \$page_bottom became the successor to \$closure.

Since you can use the hook_page_alter() and hook_page_build() hooks in Drupal 7 to add content to regions, hook_footer() and consequently theme_closure() were removed.

Drupal 6:

``` php
/**
 * Implements hook_footer().
 */
function example_footer($main = 0) {
  if (variable_get('dev_query', 0)) {
    return '<div style="clear:both;">'. devel_query_table() .'</div>';
  }
}
```

Drupal 7:

``` php
/**
 * Implements hook_page_build().
 */
function example_page_build(&$page) {
  if (variable_get('dev_query', 0)) {
    $page['page_bottom']['devel']= array(
      '#type' => 'markup',
      '#markup' => '<div style="clear:both;">' . devel_query_table() . '</div>',
    );
  }
}
```

Note that you need to return a render array construct and not simply plain HTML. Ideally, you'd not pre-render the output of your code and return a fully render structure instead.

Although hook_footer() did not have a counterpart to add content to the top of the markup output, Drupal 7 adds the special \$page_top region, which serves this purpose and can be used just like \$page_bottom.

### Schema descriptions are now plain text instead of HTML

[(issue)](http://drupal.org/node/412410) Descriptions of the [schema API](http://api.drupal.org/api/group/schemaapi/7) (tables and fields) in module.install are now non-markup plain text, because HTML is not supported by tools like phpMyAdmin.

6.x:  
  

``` php
function foo_schema() {
  $schema['foo_url'] = array(
    'description' => t('Stores URLs that appear in &lt;a href=....&gt; tags.'),
    'fields' => array(
      'url' => array(
        'description' => t('The URL.'),
      ),
    ),
  );
  return $schema;
}
```

7.x:  
  

``` php
function foo_schema() {
  $schema['foo_url'] = array(
    'description' => 'Stores URLs that appear in <a href=....> tags.',
    'fields' => array(
      'url' => array(
        'description' => 'The URL.',
      ),
    ),
  );
  return $schema;
}
```

As [mentioned above](#schema_translation), the strings no longer needs to be translated using t().

### Related terms functionality was removed from taxonomy.module

[(issue)](http://drupal.org/node/526120)  
All code referring to related terms has been removed from taxonomy.module. The taxonomy_term_relations table has been left in place to allow for an upgrade path for data. This functionality has been superceded by the Field API, which allows fields to be attached to terms, and provides a term reference field in core.

### db_result() has been removed; use -\>fetchField() instead

(unknown issue) [db_result()](http://api.drupal.org/api/function/db_result/6) is gone. [fetchField() \[handbook\]](http://drupal.org/node/310072) can do its old job.

Drupal 6:

``` php
$val = db_result(db_query($sql));
```

Drupal 7:

``` php
$val = db_query($sql)->fetchField();
```

### Do not use SELECT COUNT(\*) to check for existence of rows in a table

[(issue)](http://drupal.org/node/196862)  
Drupal 7 now creates InnoDB tables by default, which do not perform well when performing `SELECT COUNT(*) FROM table;` queries. If you only need to check the existence of rows in a table, you should use

Drupal 6:

``` php
$has_rows = db_result(db_query("SELECT COUNT(*) FROM {mytable}"));
```

Drupal 7:

``` php
$has_rows = (bool) db_query_range('SELECT 1 FROM {mytable}', 0, 1)->fetchField();
```

If you do in fact need to know the number of rows in a table or in a given result set, you should still use COUNT(\*) as before.

### Added drupal_set_time_limit()

[(issue)](http://drupal.org/node/193383)  
This function is a wrapper around [set_time_limit()](http://www.php.net/set_time_limit), it has been created to centralize this operation. It avoids the repetition of the code to check the basic requirements and also suppresses all the warnings and errors which could be caused by this function (set_time_limit is sensitive to the environment settings like *safe_mode*, disabled functions and various security extensions). See the [API documentation](http://api.drupal.org/api/function/drupal_set_time_limit/7) for further details.

### Module .info files can now optionally specify the version number of the module it depends on

[(issue)](http://drupal.org/node/211747)

Starting with Drupal 7, modules, in their .info files, can optionally specify the version numbers of the modules they depend on, with optional greater than or lesser than operators. For example, `dependencies[] = views (2.x)` means that the module requires the Views module on the major version 2, with any minor version. `dependencies[] = views (>2.1)` means that the module requires Views with a version number greater than 2.1. "Greater than or equal to" and "lesser than or equal to" is also supported. No operator means that equals is assumed, but "=" and "==" are also allowed. Modules can also optionally specify the Drupal core branch in the version number. See <http://drupal.org/node/542202#dependencies> for details.

### hook_nodeapi_xxx() becomes hook_node_xxx()

[\$op was removed from hook_nodeapi()](#remove_op), and the hook split into multiple hooks. Later in development, hook_nodeapi_xxx() was also renamed to hook_node_xxx(). All information is in the [updated discussion about the hook_nodeapi() \$op removal.](#remove_op)

### .module file available during install

The .module file and its functions are now loaded during the install process, as long as hook_requirements() is satisfied. In Drupal 6, a .install file that wanted to use a function from the .module file would have to load it explicitly, but that is no longer the case. Now, as long as hook_requirements() is satisfied, the .module file is loaded and available during the install process.

### Parameters to function user_authenticate() changed

Function user_authenticate() is now a general API function that can be used outside the context of a form submission. It now takes a user name and a plain-text password as parameters, and returns the uid on success, or FALSE on failure.

Drupal 6.x:

``` php
/**
 * Tries to log in the user locally.
 *
 * $form_state['uid'] is set to a user ID if successful.
 *
 * @param $form_state
 *   Form submission state with at least 'name' and 'pass' keys.
 */
function user_authenticate(&$form_state) {
 ...
}
```

Drupal 7.x:

``` php
/**
 * Tries to validate the user's login credentials locally.
 *
 * @param $name
 *   User name to authenticate.
 * @param $password
 *   A plain-text password, such as trimmed text from form values.
 * @return
 *   The user's uid on success, or FALSE on failure to authenticate.
 */
function user_authenticate($name, $password) {
 ...
}
```

### JavaScript variable Drupal.jsEnabled has been removed

In previous versions of Drupal, you could do the following in JavaScript code, to verify that JavaScript was enabled and sufficient for Drupal to do its "behaviors":

``` php
if( Drupal.jsEnabled ) {
   // Do something.
}
```

In Drupal 7, the `Drupal.jsEnabled` variable is no longer defined, and there is no work-around -- the assumption is that jQuery things will simply not work if they don't work, so there's no reason to check ahead of time. See issue [\#444352: Kill the killswitch](/project/drupal/issues/444352 "Status: Closed (fixed)") for discussion.

### ~~xmlrpc() wrapper function removed~~

[Issue](/node/352872), and [roll-back](/node/497118)  
~~  
In Drupal 6, there was an xmlrpc() function in the common.inc file that would load the xmlrpc.inc file and call an internal function that actually processed the XMLRPC request. In Drupal 7, this wrapper function has been removed, and you need to use `drupal_function_exists('xmlrpc');` to make sure the include files is loaded. Example:~~

Drupal 6.x:

``` php
xmlrpc(...);
```

Drupal 7.x

``` php
drupal_function_exists('xmlrpc');
xmlrpc(...);
```

### Foreign keys added to core database table schema

Issue: [\#111011: Add foreign keys to core](/project/drupal/issues/111011 "Status: Closed (fixed)")

For documentation purposes, a 'foreign keys' section was added to table schema descriptions for many core Drupal tables. For instance, the following was added to `forum_schema()` in `forum.install` to indicate that the nid and vid fields in this table are related to the same fields in the node table:

``` php
    'foreign keys' => array(
      'nid' => array('node' => 'nid'),
      'vid' => array('node' => 'vid'),
    ),
```

### Removed several unnecessary arguments to various hook_user\_\$op hooks and removed hook_profile_alter

Issue: [\#491972: Fix horrifying mess of crap in user module hooks](/project/drupal/issues/491972 "Status: Closed (fixed)")

Because [\$op was removed from hook_user](#remove_op), many hooks contained unnecessary arguments.

Changed hooks:

``` php
function hook_user_categories() {}
function hook_user_login(&$edit, $account) {}
function hook_user_logout($account) {}
function hook_user_view($account) {}
```

See also : <http://api.drupal.org/api/search/7/hook_user>

Additionally, hook_profile_alter() was doing exactly the same as [hook_user_view()](http://api.drupal.org/api/function/hook_user_view/7) and has been removed. Use the latter hook with a higher weight if you want to remove something that has been added by another module.

### Many paths to admin screens have changed

[This link goes to a separate sub-page describing all the path changes.](/node/719612)

### drupal_add_css() now supports external CSS files

Issue: [\#264876: Allow external CSS files through drupal_add_css](/project/drupal/issues/264876 "Status: Closed (fixed)")

The function drupal_add_css() now supports adding external CSS files, if you pass in 'external' as the type argument. Example:

``` php
drupal_add_css('http://example.com/style.css', 'external');
```

### New hook_comment_presave() for comments

Now modules may make changes to the comment before it is saved to the database. A new hook: [hook_comment_presave()](http://api.drupal.org/api/function/hook_comment_presave/7) was added. The `$comment` passed as argument to the hook can be altered. Example:

``` php
function mymodule_comment_presave($comment) {
  // Remove leading & trailing spaces from the comment subject.
  $comment->subject = trim($comment->subject);
}
```

### New tar archive library added

Drupal 7 includes a new third-party library, [Archive_Tar](http://api.drupal.org/api/file/modules/system/system.tar.inc/7/source) from the PEAR project, which you can use to create and extract tar files in your modules. External resources on how to use this module:

- [PHPDoc for the class, from pear.php.net](http://pear.php.net/package/Archive_Tar/docs/latest/Archive_Tar/Archive_Tar.html)
- [Article with usage examples from TechRepublic](http://articles.techrepublic.com.com/5100-10878_11-6161314.html)

### hook_elements() renamed to hook_element_info()

Issue [\#572932: Rename hook_elements() to hook_element_info()](/project/drupal/issues/572932 "Status: Closed (fixed), Assigned to: sun")

Since Drupal 4.7, modules could create new form element types with [hook_elements()](http://api.drupal.org/api/function/hook_elements/6). In Drupal 7, this hook is now called [hook_element_info()](http://api.drupal.org/api/function/hook_element_info/7). This is to keep it consistent with the new [hook_element_info_alter()](http://api.drupal.org/api/function/hook_element_info_alter/7).

Drupal 6.x:

``` php
  function example_elements() {
    // ...
  }
```

Drupal 7.x:

``` php
  function example_element_info() {
    // ...
  }
```

### Blog API module removed from Drupal core

[(issue)](http://drupal.org/node/537434) Blog API module has been removed from Drupal core. The functionality is now available as contributed module: <http://drupal.org/project/blogapi>

### drupal_urlencode() replaced by drupal_encode_path()

[(issue)](http://drupal.org/node/310139) [drupal_urlencode()](http://api.drupal.org/api/function/drupal_urlencode/6) was used to apply URL encoding to paths, but had special rules to take care of problems caused by Apache when Clean URLs were enabled. It has been replaced by [drupal_encode_path()](http://api.drupal.org/api/function/drupal_encode_path/7). [url()](http://api.drupal.org/api/function/url/7) takes care of this automatically, so take care not to encode paths twice.

### Two page caching functions renamed

[(issue)](http://drupal.org/node/477944) Two functions related to page caching were renamed:

- [page_get_cache()](http://api.drupal.org/api/drupal/includes--bootstrap.inc/function/page_get_cache/6) in Drupal 6 became [drupal_page_get_cache()](http://api.drupal.org/api/drupal/includes--bootstrap.inc/function/drupal_page_get_cache/7) in Drupal 7.
- [drupal_page_cache_header()](http://api.drupal.org/api/drupal/includes--bootstrap.inc/function/drupal_page_cache_header/6) became [drupal_serve_page_from_cache()](http://api.drupal.org/api/drupal/includes--bootstrap.inc/function/drupal_serve_page_from_cache/7) in Drupal 7.

### Weighting of stylesheets

[(issue)](http://drupal.org/node/92877) Added CSS now supports weight ordering through [drupal_add_css()](http://api.drupal.org/api/function/drupal_add_css/7). The numeric "weight" property of the `$options` array will determine the order in which the stylesheets will appear on the page.

Available constants are:

- CSS_SYSTEM: Any system-layer CSS.
- CSS_DEFAULT: Any module-layer CSS.
- CSS_THEME: Any theme-layer CSS.

Drupal 6.x:

``` php
// Add a CSS file that will appear with the other module CSS files.
drupal_add_css('mystylesheet.css', 'module');

// Add a stylesheet that will appear with the other theme layer CSS files.
drupal_add_css('mystylesheet.css', 'theme');
```

Drupal 7.x:

``` php
// Add a CSS file that will appear with the other module CSS files (CSS_DEFAULT).
drupal_add_css('mystylesheet.css');

// Add a stylesheet that will appear with the other theme layer CSS files.
drupal_add_css('mystylesheet.css', array('weight' => CSS_THEME));

// Add a CSS file that will appear before any other system-level CSS files.
drupal_add_css('mystylesheet.css', array('group' => CSS_SYSTEM - 1, 'preprocess' => FALSE));
```

### hook_access() removed in favor of hook_node_access()

The node-creating-module-specific [hook_access()](http://api.drupal.org/api/function/hook_access/6) has been removed and replaced with a the more flexible [hook_node_access()](http://api.drupal.org/api/function/hook_node_access/7). In Drupal 6, the module that created a node type had absolute control over its access hook. For admin-created node types that is the node module with a fixed set of global permissions. In Drupal 7, any module may influence the access a user has to a node regardless of which module created it. By default node.module provides global permissions for *any* node type. That may be disabled per-node type by setting the variable node_permissions\_\$typename to 0. A contrib module will be provided that includes an administrative UI.

Additional modules may provide their own hook_node_access() implementations that will layer on top of the core functionality, allowing for more complex node access rules. See the links above for more details.

### hook_filter() and hook_filter_tips() replaced by hook_filter_info()

hook_filter() has been removed and replaced with [hook_filter_info()](http://api.drupal.org/api/function/hook_filter_info/7), to allow modules to declare the input filters they provide using an associative array (hook_menu-alike registry structure), consistently with others info hooks in core. Issue: [\#546336: hook_filter_info(): Remove \$op from hook_filter()](/project/drupal/issues/546336 "Status: Closed (fixed), Assigned to: jhodgdon")

hook_filter_tips() is not required any more, since a 'tips callback' is provided in the hook_filter_info declaration, and used to generate filter tips. Issue: [\#548308: Remove hook_filter_tips()](/project/drupal/issues/548308 "Status: Closed (fixed), Assigned to: dropcube")

Drupal 6.x:

``` php
/**
 * Implements hook_filter().
 */
function filter_filter($op, $delta = 0, $format = -1, $text = '') {
  switch ($op) {
   case 'list':

   case 'description':

   case 'no cache':
      return TRUE;
  }
}

/**
 * Implements hook_filter_tips().
 *
 * Tips callback for php filter.
 */
function filter_filter_tips($delta, $format, $long = FALSE) {
}
```

Drupal 7.

``` php
function hook_filter_info() {
  $filters['filter_html'] = array(
    'title' => t('Limit allowed HTML tags'),
    'description' => t('Allows you to restrict the HTML tags the user can use. It will also remove harmful content such as JavaScript events, JavaScript URLs and CSS styles from those tags that are not removed.'),
    'process callback' => '_filter_html',
    'settings callback' => '_filter_html_settings',
    'tips callback'  => '_filter_html_tips',
    'cache' => FALSE,
  );
  return $filters;
}

// Filter callbacks.

function _filter_html($text, $filter, $format) {
}

function _filter_html_settings($format) {
}

function _filter_html_tips($filter, $format, $long = FALSE) {
}
```

### Convert class attributes to array in favor of a string

[(issue)](http://drupal.org/node/326539) Classes should always be an array. This is true *anytime* a class is used, even if only a single class is added.

In Drupal 6

``` php
$attributes['class'] = 'my-class';
// ...
$attributes['class'] .= ' my-second-class';
```

In Drupal 7

``` php
$attributes['class'] = array(
  'my-class',
);
// ...
$attributes['class'][] = 'my-second-class';

// Single classes should still be arrays.
$attributes2['class'] = array('single-class');
```

### ~~Schema API now supports date and time types natively~~

~~[(issue)](http://drupal.org/node/200953) The Schema API now supports native SQL "Date" and "Time" field types, in addition to combined datetime fields. Note that these fields do not include timezone information.~~  
[Rollback](http://drupal.org/node/866340)

### Added API functions for creating, loading, updating, and deleting user roles and permissions

New API functions to manipulate user roles added:

|                                                                                                 |                                                  |
|-------------------------------------------------------------------------------------------------|--------------------------------------------------|
| [user_role_delete](http://api.drupal.org/api/function/user_role_delete/7)                       | Delete a user role from database.                |
| [user_role_load](http://api.drupal.org/api/function/user_role_load/7)                           | Fetch a user role from database.                 |
| [user_role_permissions](http://api.drupal.org/api/function/user_role_permissions/7)             | Determine the permissions for one or more roles. |
| [user_role_save](http://api.drupal.org/api/function/user_role_save/7)                           | Save a user role to the database.                |
| [user_role_grant_permissions](http://api.drupal.org/api/function/user_role_grant_permissions/7) | Assign permissions to a user role.               |

Contrib modules and install profiles are encouraged to use the User roles API to create/load/update/delete user roles and assign permissions to roles; instead of directly querying the {role} and {role_permission} tables.

The following hooks were added to inform other modules about updates to user roles in the system:

|                                                                                     |                                                         |
|-------------------------------------------------------------------------------------|---------------------------------------------------------|
| [hook_user_role_delete](http://api.drupal.org/api/function/hook_user_role_delete/7) | Inform other modules that a user role has been deleted. |
| [hook_user_role_insert](http://api.drupal.org/api/function/hook_user_role_insert/7) | Inform other modules that a user role has been added.   |
| [hook_user_role_update](http://api.drupal.org/api/function/hook_user_role_update/7) | Inform other modules that a user role has been updated. |

Issue: [\#300993: User roles and permissions API](/project/drupal/issues/300993 "Status: Closed (fixed)")

### New hook: hook_file_url_alter()

[(Issue)](http://drupal.org/node/499156) The hook `hook_file_url_alter()` has been added, which allows URLs to files to be altered. This makes it possible to serve files from a CDN for example. See [the documentation](http://api.drupal.org/api/function/hook_file_url_alter/7) for details.

### jQuery Once method for applying JavaScript behaviors once

[(issue)](http://drupal.org/node/444344) When applying certain behaviours to elements through JavaScript, we apply a class to the element to depict whether or not the effect has been applied. Using jQuery Once, the developer experience of applying these effects is improved. Note that there is also the removeOnce method that will only take effect on elements that have already applied the behaviors.

Drupal 6.x:

``` php
Drupal.behaviors.mybehavior = function (context) {
  $('input.mybehavior:not(.mybehavior-processed)', context).addClass('mybehavior-processed').each(function () {
    // Apply the MyBehaviour effect to the elements only once.
  });
};
```

Drupal 7.x:

``` php
Drupal.behaviors.mybehavior = {
  attach: function (context, settings) {
    $('input.mybehavior', context).once('mybehavior', function () {
      // Apply the MyBehaviour effect to the elements only once.
    });
  }
};
```

This is also useful when bind with a spec event

``` php
 $("input.mybehavior", context).once('mybehavior').click(function() {
 });
```

### Database schema (un)installed automatically

[(issue)](http://drupal.org/node/306151) A module no longer should explicitly install or uninstall its database schema in hook_install() or hook_uninstall().

Drupal 6.x:

``` php
function example_schema() {
  $schema['example'] = array(
    'fields' => array(
      'nid' => array('type' => 'int', 'unsigned' => TRUE, 'not null' => TRUE, 'default' => 0),
      'primary key' => array('nid'),
    ),
  );
  return $schema;
}

function example_install() {
  drupal_install_schema('example');
}

function example_uninstall() {
  drupal_uninstall_schema('example');
}
```

Drupal 7.x:

``` php
function example_schema() {
  $schema['example'] = array(
    'fields' => array(
      'nid' => array('type' => 'int', 'unsigned' => TRUE, 'not null' => TRUE, 'default' => 0),
      'primary key' => array('nid'),
    ),
  );
  return $schema;
}
```

The installation of database schema occurs when the module is first enabled. You may then use hook_install() to perform actions on your database tables. The uninstallation of database schema occurs after your implementation of hook_uninstall(), allowing your module to act on its data.

Drupal 6.x:

``` php
function example_uninstall() {
  $result = db_query("SELECT * FROM {example}");
  while ($data = db_fetch_object($result)) {
    db_query("DELETE FROM {variable} WHERE name = '%s'", 'example_'. $data->nid);
  }
  drupal_uninstall_schema('example');
}
```

Drupal 7.x:

``` php
function example_uninstall() {
  $result = db_query("SELECT * FROM {example}");
  foreach ($result as $data) {
    db_query("DELETE FROM {variable} WHERE name = :name", array(':name' => 'example_', $data->nid));
  }
}
```

### User 1 is now called *site maintenance account*

[(issue)](http://drupal.org/node/570572) User 1 is now referred to as *site maintenance account*. Make sure you use this phrase when you mean this particular account. Avoid *administrator* or similar phrases, because that should only be used for the new [administrator role](http://drupal.org/node/480660).

### CRUD hooks for menu links: hook_menu_link_insert(), hook_menu_link_update(), hook_menu_link_delete()

[(issue)](http://drupal.org/node/457450) The menu system now fires hooks to inform modules that changes have been made to the menu system. The hooks are standard Drupal, each of which passes the \$links associative array generated by menu_link_save().

- [hook_menu_link_insert()](http://api.drupal.org/api/function/hook_menu_link_insert/7)
- [hook_menu_link_update()](http://api.drupal.org/api/function/hook_menu_link_update/7)
- [hook_menu_link_delete()](http://api.drupal.org/api/function/hook_menu_link_delete/7)

### Default text formats have been revamped

[(issue)](http://drupal.org/node/11218) The default text format provided by the filter module previously served two purposes at once:

1.  It was the text format that all users automatically had permission to use, and
2.  It was the text format that was selected by default when, for example, a user created new content.

In Drupal 7, these concepts have been split into two: the *fallback text format* and the *default text format*.

As a consequence, the following from Drupal 6.x are no longer available to use:

- The FILTER_FORMAT_DEFAULT constant
- The 'filter_default_format' variable, typically used via `variable_get('filter_default_format', 1)`
- The filter_resolve_format() function

In their place, there are two new functions in Drupal 7.x:

1.  [filter_fallback_format()](http://api.drupal.org/api/function/filter_fallback_format/7): This returns the ID of a safe format (for example, plain text) that all users automatically have permission to use. The filter system uses this to filter text when check_markup() is called without a text format being provided. Generally you do not need to call this function directly.

2.  [filter_default_format()](http://api.drupal.org/api/function/filter_default_format/7): This returns the ID of a format that should be used as the default choice when presenting a list of possible text formats to a user who has not selected one. It should *not* be used when filtering text. Generally you should not call this function directly. Instead, you should set the text format to NULL in your form constructor function, and the filter system will handle the rest. Example (from the user module):  

    ``` php
      $form['signature_settings']['signature'] = array(
        '#type' => 'text_format',
        '#title' => t('Signature'),
        '#default_value' => isset($account->signature) ? $account->signature : '',
        '#description' => t('Your signature will be publicly displayed at the end of your comments.'),
        // If the signature wasn't created yet and therefore doesn't have a stored
        // text format, we pass in NULL, and the filter system will automatically
        // pre-select the current user's filter_default_format() on the form.
        '#format' => isset($account->signature_format) ? $account->signature_format : NULL,
      );
    ```

In addition, you may have previously stored FILTER_FORMAT_DEFAULT (i.e., "0") in your module's database tables to indicate that a particular piece of content should be filtered using the default format. If so, you will need to write an update function to convert these instances to use the actual format. See [below](#text_format_updates) for more information on how to write these update functions.

Note that although the 'filter_default_format' variable is deprecated, Drupal 7 preserves it in the database so that it can be used for the purpose of these update functions only.

### Text formats access is now controlled by permissions, and filter_access() parameters have changed

[(issue)](http://drupal.org/node/11218) Text formats no longer have an associated "roles" element maintained as part of the text format itself; rather, access to each text format is now controlled by a permission that uses the normal Drupal user access system.

Your code should continue to use the filter_access() function to check all access to text formats, but be aware that this function now takes a full format object rather than a format ID as input.

Drupal 6.x:

``` php
if (filter_access($format_id)) {
  // Do stuff.
}
```

Drupal 7.x:

``` php
$format = filter_format_load($format_id);
if (filter_access($format)) {
  // Do stuff.
}
```

In addition, any code which relied on the existence of a `$format->roles` property or the existence of a "roles" column in the `{filter_format}` database table must be changed to use filter_access() instead.

Also note that there are new API functions [filter_get_roles_by_format()](http://api.drupal.org/api/function/filter_get_roles_by_format/7) and [filter_get_formats_by_role()](http://api.drupal.org/api/function/filter_get_formats_by_role/7) which can be used to determine the text formats that each user role has specific permission to access.

### The parameters to filter_formats() have changed

[(issue)](http://drupal.org/node/11218) By default (when called with no parameters), this function now returns a list of *all* text formats on the site, rather than only those formats that the current user has permission to use. You can use the new \$account parameter if you need a list of formats for a particular user.

Drupal 6.x:

``` php
// Get a list of formats that the current user has access to.
$formats = filter_formats();
```

Drupal 7.x:

``` php
// Get a list of formats that the current user has access to.
global $user;
$formats = filter_formats($user);
```

### Rename drupal_to_js() and drupal_json() to drupal_json_encode() and drupal_json_output()

[(issue)](http://drupal.org/node/556018) Rename drupal_to_js() and drupal_json() to drupal_json_encode() and drupal_json_output()

For example:

Drupal 6.x:

``` php
<?php
  echo drupal_to_js($var);
?>
```

Drupal 7.x:

``` php
<?php
  echo drupal_json_encode($var);
?>
```

Drupal 6.x:

``` php
<?php
  $matches = array(
    'result1' => 'result1',
  );
  drupal_json($matches);
?>
```

Drupal 7.x:

``` php
<?php
  $matches = array(
    'result1' => 'result1',
  );
  drupal_json_output($matches);
?>
```

### theme_links() has a new parameter 'heading' for accessibility

Issue: [\#364219: Navigation menus should be preceded by headings of the appropriate level (usually \<h2\>).](/project/drupal/issues/364219 "Status: Closed (fixed), Assigned to: jhodgdon")

The [theme_links()](http://api.drupal.org/api/function/theme_links/7) function, which is normally called via theme('links', \$variables) (in Drupal 7), has a new third parameter 'heading' that can be used to provide an invisible heading before a list of links, for accessibility. Headings such as these can be used by screen reader and keyboard-only users to navigate to or skip the list of links. Also, headings are required by the standard Web Content Accessibility Guidelines (WCAG) to be present at the beginning of each content section, including navigation sections (see <http://www.w3.org/TR/2008/WD-WCAG20-TECHS-20080430/H69.html>).

Example - Drupal 6:

``` php
theme('links', $main_menu, array('id' => 'main-menu', 'class' => array('links', 'clearfix')));
```

Drupal 7 (simple):

``` php
theme('links', array('links' => $main_menu, 'attributes' => array('id' => 'main-menu', 'class' => array('links', 'clearfix')), 'header' => array('text' => t('Main menu'), 'level' => 'h2', 'class' => array('element-invisible'))));
```

<http://drupal.org/update/theme/6/7#theme-links-param> has more detail about this change, including references.

### API for modules providing search has changed

Issue: [\#394182: DBTNG search.module](/project/drupal/issues/394182 "Status: Closed (fixed)")  
Second issue: [\#810176: Search result titles should be enclosed in a heading tag.](/project/drupal/issues/810176 "Status: Closed (fixed)")  
Third issue: [\#839524: Search results are themed too early](/project/drupal/issues/839524 "Status: Closed (fixed)")

The API for search modules (i.e. modules that provide search tabs to the core search.module) has been overhauled in Drupal 7. Key changes:

1.  In Drupal 6, the operations in [hook_search()](http://api.drupal.org/api/function/hook_search/6) let a module set up a search tab, add to the search settings admin page, perform a search, respond to search index resets, and return information about indexing status. In Drupal 7, this one hook has been separated out into [hook_search_info()](http://api.drupal.org/api/function/hook_search_info/7), [hook_search_admin()](http://api.drupal.org/api/function/hook_search_admin/7), [hook_search_execute()](http://api.drupal.org/api/function/hook_search_execute/7), [hook_search_reset()](http://api.drupal.org/api/function/hook_search_reset/7), and [hook_search_status()](http://api.drupal.org/api/function/hook_search_status/7). There is also a new hook, [hook_search_access()](http://api.drupal.org/api/function/hook_search_access/7), which allows setting permissions for your particular search module's search tab.

2.  In Drupal 6, modules were encouraged to use the [do_search()](http://api.drupal.org/api/function/do_search/6) function to perform the search. In Drupal 7, this function does not exist. Instead, modules should perform the serach query directly, using the "SearchQuery" extension.  
    Example - Drupal 6 -- see [node_search(\$op = 'search')](http://api.drupal.org/api/function/node_search/6):

    ``` php
    // Calculate join and special conditions first...
    $results = do_search($keys, 'node', 'INNER JOIN {node} n ON n.nid = i.sid '. $join1, $conditions1 . (empty($where1) ? '' : ' AND '. $where1), $arguments1, $select2, $join2, $arguments2);
    // Further processing.
    ```

    Drupal 7 -- see [node_search_execute()](http://api.drupal.org/api/function/node_search_execute/7):

    ``` php
    $query = db_select('search_index', 'i')->extend('SearchQuery')->extend('PagerDefault');
    $query->join('node', 'n', 'n.nid = i.sid');
    $query
      ->condition('n.status', 1)
      ->addTag('node_access')
      ->searchExpression($keys, 'node');
    // Add additional modifiers here...
    $found = $query
       ->limit(10)
       ->execute();
    // Further processing.
    ```

3.  The search results theming has changed. See [the theme update section on search results](http://drupal.org/update/theme/6/7#search-result-headings) for more information. Modules implementing their own custom search results page or pre-processing hooks will be affected.

4.  The search_data() and hook_search_page() return values have changed to be renderable arrays rather than rendered HTML.

### File API: \$file-\>filepath renamed to \$file-\>uri

Issue: [\#517814: File API Stream Wrapper Conversion](/project/drupal/issues/517814 "Status: Closed (fixed)")

In the File API, the \$file-object's field \$file-\>fileapi has been renamed to \$file-\>uri.

### HTML rendering of form elements has different CSS classes

[Issue](http://drupal.org/node/550572): The HTML rendering of form elements has changed, in that they have different CSS classes applied to the surrounding DIV: .form-type-TYPE and .form-item-NAME. Previously, the assigned classes were .form-item-TYPE and .NAME-wrapper. In both cases, TYPE is the \#type component of the form element, and NAME is the array key. For example, in:

``` php
$form['body'] = array(
  '#type' => 'textarea',
  ...
);
```

TYPE would be textarea, and NAME would be body. (For multi-word types and names, underscores are converted to hyphens.)

### Form element value callbacks now always have \$form_state argument

[(issue)](http://drupal.org/node/546568) Value callbacks for custom form elements are now always passed a third \$form_state argument. Previously, some calls to value callbacks did not get the \$form_state argument (depending on where in what type of form processing the callback was called); now, it is consistent.

### Changes to how Drupal sends email

[(issue)](/node/331180)

In Drupal 6.x, email sending was done by the function drupal_mail_send(), which checked variable_get('smtp_library', '') for a custom email back-end, and either used that custom back end or used the default SMTP back-end to send the email message.

In Drupal 7.x, the drupal_mail_send() function does not exist. Instead, drupal_mail_system() checks variable_get('mail_system') to figure out which class implementing MailSystemInterface to use to send the email message, and that class is used to first format and then send out the email message in drupal_mail().

### Trigger and Actions API overhaul

Issues: [\#525540: trigger.module and includes/actions.inc need overhaul](/project/drupal/issues/525540 "Status: Closed (fixed), Assigned to: jvandyk"), [\#585868: Triggers/actions need overhaul (part II) - Presave](/project/drupal/issues/585868 "Status: Closed (fixed)")

The Trigger and Actions APIs were changed extensively between Drupal 6 and Drupal 7, to simplify the API and make it more consistent. The following changes were made:

1.  Database table {actions} changed - 'description' field is now called 'label'.

2.  Database table {trigger_assignments} changed - 'op' field was removed, and the 'hook' field now contains the full function name. For instance, in Drupal 6 you might have had hook/op of node/insert, and in Drupal 7, the hook field would be node_insert.

3.  The arrays returned by hook_action_info(), hook_action_info_alter(), actions_list(), actions_get_all_actions(), actions_actions_map() were changed:

    - 'description' element becomes 'label'
    - 'hooks' element becomes 'triggers', and is now a flat array of trigger functions rather than a nested array of type/operation.
    - 'behavior' element - in Drupal 6 the only supported behavior was 'changes node property'. This becomes 'changes_property' in Drupal 7, which indicates that a property of the object is changed by this action. Using this behavior causes a 'save' action to be triggered or, if there is already a save action in the list, to be moved after the property-changing action.

    Example from comment_action_info() -- Drupal 6:

    ``` php
    return array(
        'comment_unpublish_action' => array(
          'description' => t('Unpublish comment'),
          'type' => 'comment',
          'configurable' => FALSE,
          'hooks' => array(
            'comment' => array('insert', 'update'),
          )
        ),
    );
    ```

    Drupal 7:

    ``` php
     return array(
        'comment_unpublish_action' => array(
          'type' => 'comment',
          'label' => t('Unpublish comment'),
          'configurable' => FALSE,
          'triggers' => array('comment_insert', 'comment_update'),
        ),
    );
    ```

4.  hook_hook_info() is now called hook_trigger_info(), and its return value has been changed and simplified.  
    Example from the node module implementation - Drupal 6:

    ``` php
     return array(
        'node' => array(
          'nodeapi' => array(
            'presave' => array(
              'runs when' => t('When either saving a new post or updating an existing post'),
            ),
            'insert' => array(
              'runs when' => t('After saving a new post'),
            ),
            'update' => array(
              'runs when' => t('After saving an updated post'),
            ),
            'delete' => array(
              'runs when' => t('After deleting a post')
            ),
            'view' => array(
              'runs when' => t('When content is viewed by an authenticated user')
            ),
          ),
        ),
      );
    ```

    Drupal 7:

    ``` php
     return array(
        'node' => array(
          'node_presave' => array(
            'label' => t('When either saving new content or updating existing content'),
          ),
          'node_insert' => array(
            'label' => t('After saving new content'),
          ),
          'node_update' => array(
            'label' => t('After saving updated content'),
          ),
          'node_delete' => array(
            'label' => t('After deleting content'),
          ),
          'node_view' => array(
            'label' => t('When content is viewed by an authenticated user'),
          ),
        ),
    );
    ```

5.  A new API function has been added, trigger_get_assigned_actions(), which allows your module to retrieve a list of actions assigned to one of its hooks. Drupal 6 had no approved method for finding this out.

6.  Tests were added to test triggering of actions in node, comment, taxonomy, and user modules.

7.  Numerous internal functions used to generate administrative pages have changed. In the unlikely event that your module is calling these functions directly, you will need to look at these functions' new definitions to see what has changed.

8.  The [Examples for Developers](http://drupal.org/project/examples) module has working demonstration code to show triggers and actions in action.

### All taxonomy functions relating to nodes have been removed or refactored

Issue: [\#412518: Convert taxonomy_node\_\* related code to use field API + upgrade path](/project/drupal/issues/412518 "Status: Closed (fixed), Assigned to: ")  
You should now use field API functions or views in nearly all cases where taxonomy / node relations were used in taxonomy module, since the only way to attach terms to nodes is via field API. Several functions were completely removed as part of this conversion, so please refer to taxonomy module code or field API documentation for full details. The removed functions include taxonomy_preview_terms(), taxonomy_node_get_terms_by_vocabulary(), taxonomy_node_get_terms(), taxonomy_node_save() and taxonomy_term_count_nodes().

For example, [the table taxonomy_vocabulary_node_type has been removed](http://api.drupal.org/api/function/taxonomy_schema/7). The following snippet iterates over [field_info_fields](http://api.drupal.org/api/function/field_info_fields/7) to collect machine names of all the vocabularies associated with node type "story" into a \$story_vocabs array:

``` php
// field_info_fields() returns information about all fields
$fields = field_info_fields();
$story_vocabs = array();
foreach ($fields as $field_name => $field) {
  // $field['bundles'] contains names of bundles and entities associated with this field.
  // keys are entity types, values are arrays of bundle names.
  if ($field['type'] == 'taxonomy_term_reference' && !empty($field['bundles']['node']) && in_array('story', $field['bundles']['node'])) {
    // Collect all vocabularies allowed for the field.
    foreach ($field['settings']['allowed_values'] as $allowed_values) {
      $story_vocabs[] = $allowed_values['vocabulary'];
    }
}
```

### Added hook_entity_load()

Issue [\#605442: Add a generic hook_entity_load()](/project/drupal/issues/605442 "Status: Closed (fixed)"). This allows you to act on any entity (nodes, comments, users) loaded via the entity API using a single hook. See the API documentation for details.

### All e-mails are considered to originate as HTML

[(issue)](http://drupal.org/node/407452) By default, Drupal core and [drupal_mail()](http://api.drupal.org/api/function/drupal_mail/7) assume that **any** mail that is sent through Drupal is HTML. Therefore, all e-mail messages are converted into plain-text as the last step of Drupal's default e-mail processing. Contributed modules can implement different mail handlers.

This means that if you are processing user-supplied text in the email system, any HTML entities in it need to be converted to plain text before being used in the system.

D6:

``` php
function hook_mail($key, &$message) {
  $message['body'][] = $user_supplied_input;
}
```

D7:

``` php
function hook_mail($key, &$message) {
  // If input is user-supplied, convert any HTML entities
  $body = check_plain($user_supplied_input);  // Make sure that later HTML processing does not truncate body
  $message['body'][] = $body;
  // Body will automatically be converted from HTML to text
}
```

[If your module needs to send HTML formatted emails, see this page for additional instructions.](/node/900794)

### Query string functions renamed

([issue](http://drupal.org/node/578520)) [drupal_query_string_encode()](http://api.drupal.org/api/function/drupal_query_string_encode/6) has been renamed to [drupal_http_build_query()](http://api.drupal.org/api/function/drupal_http_build_query/7). Support for the \$exclude argument has been moved to the new [drupal_get_query_parameters()](http://api.drupal.org/api/function/drupal_get_query_parameters/7) function.

Drupal 6:

``` php
  $query_string = drupal_query_string_encode($_GET, array('q', 'page'));;
```

Drupal 7:

``` php
  $query_string = drupal_http_build_query(drupal_get_query_parameters($_GET, array('q', 'page')));
```

[pager_get_querystring()](http://api.drupal.org/api/function/pager_get_querystring/6) and [tablesort_get_querystring()](http://api.drupal.org/api/function/tablesort_get_querystring/6) have been renamed to [pager_get_query_parameters() and](http://api.drupal.org/api/function/pager_get_query_parameters/7) [tablesort_get_query_parameters()](http://api.drupal.org/api/function/tablesort_get_query_parameters/7). Instead of returning a query string they now return a query array that may be passed to url(\$path, array('query' =\> \$query)) or converted to a query string using drupal_http_build_query(\$query).

### theme() now takes only two arguments

[(issue)](http://drupal.org/node/572618) The `theme()` function takes two arguments, where the first is the same as it was but the second one is an associative array.  
So if your `hook_theme` (which also changed, see below) contained

``` php
    'user_list' => array(
      'arguments' => array('users' => NULL, 'title' => NULL),
    ),
```

then previously you had

``` php
theme('user_list', $users, $title);
```

now you need to do

``` php
theme('user_list', array('users' => $users, 'title' => $title));
```

### hook_theme() requires "variables" or "render element" instead of "arguments" to better integrate with drupal_render()

In Drupal 6, the `#theme` property of an element could only be set to a theme function that was written to work with a render element as its first argument. In Drupal 7, the `#theme` property can be set to any theme function, but because of this, `drupal_render()` and `theme()` need to know whether the theme function expects the element itself, or an arbitrary set of variables to be gathered from the element's properties. Therefore, the theme hook needs to be registered with either a 'variables' key or a 'render element' key. This is best illustrated by showing the following change to `node_theme()`:

Drupal 6:

``` php
function node_theme() {
  return array(
    ...
    'node_list' => array(
      'arguments' => array('items' => NULL, 'title' => NULL),
    ),
    'node_search_admin' => array(
      'arguments' => array('form' => NULL),
    ),
    ...
  );
}
```

Drupal 7:

``` php
function node_theme() {
  return array(
    ...
    'node_list' => array(
      'variables' => array('items' => NULL, 'title' => NULL),
    ),
    'node_search_admin' => array(
      'render element' => 'form',
    ),
    ...
  );
}
```

### drupal_alter() now takes at most 3 parameters by reference

Issue [\#593522: Upgrade drupal_alter()](/project/drupal/issues/593522 "Status: Closed (fixed)"). `drupal_alter()` Now accepts an alteration type (such as form, menu, etc.), a \$data object to alter, and up to two optional context variables. The \$data object and both context variables are passed by reference. This differs from Drupal 6 where only the \$data object was passed by reference and an unlimited number of parameters were supported. If a particular alter needs more than two context properties, they can be placed into an array and passed together in the second context property. See the [API documentation](http://api.drupal.org/api/function/drupal_alter/7) for further examples.

### The \$ret parameter has been removed from all Schema operations

Issue [\#394268: DIE update_sql() DIE!](/project/drupal/issues/394268 "Status: Closed (fixed), Assigned to: Crell") and [\#570900: Destroy remnants of update_sql()](/project/drupal/issues/570900 "Status: Closed (fixed)"). All [schema modification functions](http://api.drupal.org/api/group/schemaapi/7) no longer take a \$ret parameter. The \$ret parameter was used exclusively in the update system, which no longer needs them.

Drupal 6:

``` php
$ret = array();
db_create_table($ret, 'mytable', $table_definition);
```

Drupal 7:

``` php
db_create_table('mytable', $table_definition);
```

### Update hooks now return strings or throw exceptions, and update_sql() is no more

Issue [\#394268: DIE update_sql() DIE!](/project/drupal/issues/394268 "Status: Closed (fixed), Assigned to: Crell") and [\#570900: Destroy remnants of update_sql()](/project/drupal/issues/570900 "Status: Closed (fixed)") [`hook_update_N`](http://api.drupal.org/api/function/hook_update_N/7) hooks no longer return a \$ret array. Instead, update hooks should return nothing if they have no "success" message to display or return a translated string to be displayed to the user indicating that the update ran successfully.

If an error occurred and the update process should not continue, the update hook should throw a DrupalUpdateException exception, passing a translated string as the error message to the constructor. That string will be shown to the user and the update process will terminate.

If an update hook needs to run batched, it should accept by reference a `&$sandbox` parameter and set \$sandbox\['#finished'\] to a decimal value less than 1 to indicate how complete the process is.

Additionally, the update_sql() function is no longer necessary. Instead, simply use the database API as normal for any schema or data changes.

``` php
/**
 * Descriptive string here to show in the UI.
 */
function system_update_7100(&$sandbox) {

  if (empty($sandbox['step'])) {
    $sandbox['step'] = 1;
  }

  if ($sandbox['step'] == 1) {
    // Indicate that this function should be called a second time.
    $sandbox['#finished'] = 0.5;

    // Do other expensive work...

    // Something went wrong somewhere...
    if ($something_bad) {
      throw new DrupalUpdateException(t('Something bad happened.'));
    }
  }
  else {
    // Indicate that this function should not be called again, it's done.
    unset($sandbox['#finished']);
  }

  $sandbox['step']++;

  return t('All dohicky tables updated with a new index.');
}
```

### The signature of the form builder function (the callback from drupal_get_form()) changed to add \$form

Issue: [\#571086: Allow to specify a 'wrapper callback' before executing a form builder function](/project/drupal/issues/571086 "Status: Closed (fixed), Assigned to: rfay")  
The signature of the callback called by drupal_get_form() was changed to add \$form.  
Drupal 6:

``` php
$form = drupal_get_form('my_form', ...);
...
function my_form(&$form_state, ...) {
}
```

Drupal 7:

``` php
$form = drupal_get_form('my_form', ...);
...
function my_form($form, &$form_state, ...) {
}
```

### Replaced taxonomy_term_path(), hook_term_path(), language_url_rewrite(), and custom_url_alter_outbound() with hook_url_outbound_alter()

Issue [\#320331: Turn custom_url_rewrite_inbound and custom_url_rewrite_outbound into hooks](/project/drupal/issues/320331 "Status: Closed (fixed), Assigned to: dave reid") If you had the special custom_url_rewrite_inbound() in your site's settings.php or implemented by a module, it has been replaced with the proper [hook_url_outbound_alter()](http://api.drupal.org/api/search/7/hook_url_outbound_alter). This allows any module to be able to alter the outbound path of [url()](http://api.drupal.org/api/search/7/url) and [l()](http://api.drupal.org/api/search/7/l) as they see fit. Please note that if the original path being altered has an URL aliases, the alias will override any alterations made with hook_url_outbound_alter().

Drupal 6:

``` php
function custom_url_rewrite_outbound(&$path, &$options, $original_path) {
  global $user;
  // Change all 'node' to 'article'.
  if (preg_match('|^node(/.*)|', $path, $matches)) {
    $path = 'article' . $matches[1];
  }
  // Create a path called 'e' which lands the user on her profile edit page.
  if ($path == 'user/' . $user->uid . '/edit') {
    $path = 'e';
  }
}
```

Drupal 7:

``` php
function mymodule_url_outbound_alter(&$path, &$options, $original_path) {
  global $user;
  // Change all 'node' to 'article'.
  if (preg_match('|^node(/.*)|', $path, $matches)) {
    $path = 'article' . $matches[1];
  }
  // Create a path called 'e' which lands the user on her profile edit page.
  if ($path == 'user/' . $user->uid . '/edit') {
    $path = 'e';
  }
}
```

For taxonomy links and modules: taxonomy_term_path() and hook_term_path() have been replaced by ~~hook_url_alter_outbound()~~ hook_entity_info_alter():

Drupal 6:

``` php
function forum_term_path($term) {
  return 'forum/' . $term->tid;
}
...
$term = taxonomy_get_term(1);
$link = return l($term->name, taxonomy_term_path($term));
```

Drupal 7:  
~~  
function forum_url_outbound_alter(&\$path, &\$options, \$original_path) {  
if (preg_match('!^taxonomy/term/(\d+)!', \$path, \$matches)) {  
\$term = taxonomy_term_load(\$matches\[1\]);  
if (\$term && \$term-\>vocabulary_machine_name == 'forums') {  
\$path = 'forum/' . \$matches\[1\];  
}  
}  
}  
...  
\$term = taxonomy_term_load(1);  
\$link = return l(\$term-\>name, 'taxonomy/term/' . \$term-\>tid);  
~~

``` php
function forum_entity_info_alter(&$info) {
  // Take over URI construction for taxonomy terms that are forums.
  if ($vid = variable_get('forum_nav_vocabulary', 0)) {
    // Within hook_entity_info(), we can't invoke entity_load() as that would
    // cause infinite recursion, so we call taxonomy_vocabulary_get_names()
    // instead of taxonomy_vocabulary_load(). All we need is the machine name
    // of $vid, so retrieving and iterating all the vocabulary names is somewhat
    // inefficient, but entity info is cached across page requests, and an
    // iteration of all vocabularies once per cache clearing isn't a big deal,
    // and is done as part of taxonomy_entity_info() anyway.
    foreach (taxonomy_vocabulary_get_names() as $machine_name => $vocabulary) {
      if ($vid == $vocabulary->vid) {
        $info['taxonomy_term']['bundles'][$machine_name]['uri callback'] = 'forum_uri';
      }
    }
  }
}
...
$term = taxonomy_term_load(1);
$uri = entity_uri('taxonomy_term', $term);
$link = return l($term->name, $uri['path']);
```

Also note that language_url_rewrite() has become [locale_url_outbound_alter()](http://api.drupal.org/api/search/7/ocale_url_outbound_alter). If you have an alternate locale module that needs to alter outgoing links, make sure you implement this hook.

You can also use the [URL alter module](/project/url_alter) to retain your custom_url_rewrite_outbound() function.

### Replaced custom_url_rewrite_inbound() with hook_url_inbound_alter()

Issue [\#320331: Turn custom_url_rewrite_inbound and custom_url_rewrite_outbound into hooks](/project/drupal/issues/320331 "Status: Closed (fixed), Assigned to: dave reid") If you had the special custom_url_rewrite_inbound() in your site's settings.php or implemented by a module, it has been replaced with the proper [hook_url_inbound_alter](http://api.drupal.org/api/search/7/hook_url_inbound_alter). This allows any module to be able to alter the inbound path of [drupal_lookup_path()](http://api.drupal.org/api/search/7/drupal_lookup_path) as they see fit.

Please note that this hook runs in opposite order of hook_url_outbound_alter() so that modules that alter the same path can undo each other's alterations correctly.

Drupal 6:

``` php
function custom_url_rewrite_inbound(&$result, $path, $path_language) {
  global $user;
  // Change all article/x requests to node/x.
  if (preg_match('|^article(/.*)|', $path, $matches)) {
    $result = 'node' . $matches[1];
  }
  // Redirect a path called 'e' to the user's profile edit page.
  if ($path == 'e') {
    $result = 'user/' . $user->uid . '/edit';
  }
}
```

Drupal 7:

``` php
function mymodule_url_inbound_alter(&$path, $original_path, $path_language) {
  global $user;
  // Change all article/x requests to node/x.
  if (preg_match('|^article(/.*)|', $path, $matches)) {
    $path = 'node' . $matches[1];
  }
  // Redirect a path called 'e' to the user's profile edit page.
  if ($path == 'e') {
    $path = 'user/' . $user->uid . '/edit';
  }
}
```

You can also use the [URL alter module](/project/url_alter) to retain your custom_url_rewrite_inbound() function.

### hook_load() signature and return value change

Issue [\#460320: Standarized, pluggable entity loading (nodes, users, taxonomy, files, comments)](/project/drupal/issues/460320 "Status: Closed (fixed), Assigned to: Frando")

Drupal 6:  
[hook_load()](http://api.drupal.org/api/function/hook_load/6) took a single node as argument, and returned an object with node properties.

Drupal 7:  
[hook_load()](http://api.drupal.org/api/function/hook_load/7) takes an array of nodes as its argument and returns nothing. The hook may make changes directly to the \$nodes passed in.

### Renamed menu_path_is_external() to url_is_external()

[(issue)](/node/607008) The Drupal 6 function `menu_path_is_external()` in includes/menu.inc has been renamed to `url_is_external()` and moved into includes/common.inc. This function doesn't depend on the menu system at all, it's just a generic helper function to test if a given URL is external or not. It is used by parts of the form API, and to allow this code to work at a low bootstrap level without needing to pull in all of menu.inc, it now lives in includes/common.inc. The new name also makes the function more self-documenting.

### Comment.timestamp split into 'created' and 'changed'

Issue [\#122098: Split comment.timestamp into 'created' and 'updated' columns](/project/drupal/issues/122098 "Status: Closed (fixed)")

`$comment->timestamp` has been removed and replaced by two fields, `$comment->created` and `$comment->changed` -- in the *comment* db table as well as the `$comment` object -- to track a comment's insert and update datetimes.

### New entity_info_cache_clear() API function

Issue [\#642612: No clean way to reset entity_info cache](/project/drupal/issues/642612 "Status: Closed (fixed)")

The entity_get_info() function collects information about the entity types (new D7 concept - see [Added hook_entity_load()](#hook_entity_load)) present on the site. For performance reasons, this information happens to be both statically and persistently cached.

The `entity_info_cache_clear()` API function can be used to reset both caches.

### ~~drupal_set_header() and drupal_get_header() renamed to drupal_add_http_header() and drupal_get_http_header()~~

Issue [\#451604: Rename drupal_set_header()](/project/drupal/issues/451604 "Status: Closed (fixed), Assigned to: brianV")

~~The `drupal_set_header()` function has been renamed to `drupal_add_http_header()` to better reflect it's purpose, and to be more consistent with the renaming of `drupal_add_html_head()`.~~

~~`drupal_get_header()` was renamed to `drupal_get_http_header()` to remain consistent with `drupal_add_http_header()`~~*This is explained in more detail and more accurately above at <http://drupal.org/update/modules/6/7#http_header_functions>. Specifically, the function parameters were changed too - it's not just a simple rename.*

### Custom menu API

In Drupal 6 in order to create a custom menu (i.e. a menu you would create via `admin/build/menu/add`) you had to query the {menu_custom} table yourself.

In D7 several API functions to create, update and delete custom menus and related hooks were added.

``` php
function foo() {
  $menu = array(
    'title' => 'My menu',
    'menu_name' => 'my_menu',
    'description' => 'My custom menu',
  );
  // Add a new custom menu.
  menu_save($menu);

  // Delete the custom menu.
  // Although only the 'menu_name' key is required, we pass the full
  // $menu, so other modules may act on it.
  menu_delete($menu);
}

function foo_menu_delete($menu) {
  if ($menu['menu_name'] == 'my_menu') {
    drupal_set_mesasge(t('You have deleted the foo custom menu.'));
  }
}
```

### New hooks: hook_admin_paths() and hook_admin_paths_alter()

Issue [\#610234: Overlay implementation](/project/drupal/issues/610234 "Status: Closed (fixed)")

New hooks are provided for indicating which paths on a Drupal site are associated with administrative actions. Modules should implement these hooks to specify any paths at which administration-related activities might be expected to occur. Note that pages which can be used interchangeably for both administrative and non-administrative purposes (for example, content creation pages) should be labeled administrative for the purposes of this hook.

It is not necessary for modules to use this hook to define administrative paths that live underneath the traditional `admin/*` location, since Drupal core already implements the hook to define these paths as administrative by default.

Other modules may use this information in a variety of ways - for example, to display administrative pages in a modal overlay, or in a different theme; the function [path_is_admin()](http://api.drupal.org/api/function/path_is_admin/7) is provided for this purpose.

See the hook documentation for more information:

- [hook_admin_paths()](http://api.drupal.org/api/function/hook_admin_paths/7)
- [hook_admin_paths_alter()](http://api.drupal.org/api/function/hook_admin_paths_alter/7)

### theme('placeholder') replaced by drupal_placeholder()

Issue [\#601548: Loosen the dependency between t() and the theming layer](/project/drupal/issues/601548 "Status: Closed (fixed)"). This is a straight Replace for module developers. Themes which implemented this funtion (are you out there?) must now achieve their style changes using the new `.placeholder` class that appears on the surrounding \[EM\] tag.

### The function menu_valid_path() has been renamed to drupal_valid_path(), and its inputs have changed

Issue [\#190867: Remove access check for anonymous users when creating aliases](/project/drupal/issues/190867 "Status: Closed (outdated)")

Previously this function accepted an array (such as a menu item) containing a 'link_path' key. The renamed function now takes the path to be checked as direct input.

See the API documentation for [drupal_valid_path()](http://api.drupal.org/api/function/drupal_valid_path/7) for more details.

Drupal 6:

``` php
$item = array('link_path' => $form_state['values']['site_frontpage']);
if (!menu_valid_path($item)) {
  // Throw an error.
}
```

Drupal 7:

``` php
if (!drupal_valid_path($form_state['values']['site_frontpage'])) {
  // Throw an error.
}
```

### Language neutral content now has an explicit language associated with it

Issue [\#635094: Unify "language neutral" language codes](/project/drupal/issues/635094 "Status: Closed (fixed)")

In Drupal 7, the LANGUAGE_NONE constant should be used for nodes or other items that do not have a specific language associated with it.

See the API documentation for [LANGUAGE_NONE](http://api.drupal.org/api/constant/LANGUAGE_NONE/7) for more details.

### New API function: format_username() and new hook: hook_username_alter()

Issue [\#192056: User's raw login name should not be output directly](/project/drupal/issues/192056 "Status: Closed (fixed)")

In Drupal 6, the user's login name was output directly (without the ability for modules to alter) to the page in places where calling `theme('username')` was inappropriate (e.g., as part of the value of an "alt" attribute). In Drupal 7, unless a module needs to specifically output the raw login name, it should either call `theme('username')` (everywhere HTML output is needed) or the new function `format_username()` (everywhere HTML output is not wanted, such as the value of an attribute).

Drupal 6:

``` php
function template_preprocess_user_picture(&$variables) {
  ...
  // Prepare the alt text to add to the IMG tag. This will be added to an
  // attribute value, rather than output as HTML, so we can't call
  // theme('username').
  $alt = t("@user's picture", array('@user' => $account->name ? $account->name : variable_get('anonymous', t('Anonymous'))));
  ...
}
```

Drupal 7:

``` php
function template_preprocess_user_picture(&$variables) {
  ...
  // Prepare the alt text to add to the IMG tag. This will be added to an
  // attribute value, rather than output as HTML, so we can't call
  // theme('username').
  $alt = t("@user's picture", array('@user' => format_username($account)));
  ...
}
```

This enables modules to adjust how the user's name is displayed by implementing [hook_username_alter()](http://api.drupal.org/api/function/hook_username_alter/7). `theme('username')` now internally calls `format_username()` to retrieve the plain text display, but then also runs additional code for adding markup, such as linking to the user's profile page.

### Functions called very often that need a drupal_static() variable can use an optimized way of calling that function

Issue [\#619666: Make performance-critical usage of drupal_static() grokkable](/project/drupal/issues/619666 "Status: Closed (fixed)")

Drupal 7 introduced a [standardized drupal_static() function](#static_variable_api) for retrieving a resettable static variable. Most module functions can call this function using a very simple syntax. Module functions called very often (\>100 times per page request) can use a more advanced, but faster syntax:

Examples:

``` php
function user_role_permissions($roles = array()) {
  // Not called >100 times per page request, so use the simple pattern.
  $cache = &drupal_static(__FUNCTION__, array());
  ...
}
function user_access($string, $account = NULL) {
  // Use the advanced drupal_static() pattern, since this is called very often.
  static $drupal_static_fast;
  if (!isset($drupal_static_fast)) {
    $drupal_static_fast['perm'] = &drupal_static(__FUNCTION__);
  }
  $perm = &$drupal_static_fast['perm'];
  ...
}
```

See the [drupal_static() API documentation](http://api.drupal.org/api/function/drupal_static/7) for more information.

### A theme hook name followed by a double underscore ('\_\_') is a default 'pattern'

Issue [\#653622: Make the '\_\_' pattern for theme suggestions easier to use](/project/drupal/issues/653622 "Status: Closed (fixed)")

An advanced feature in Drupal 6 is the ability to define theme hook patterns, allowing the theme system to auto-discover targeted overrides of generic theme functions and templates. None of the code in Drupal 6 core uses this feature, but some popular contributed modules, like [Views](http://drupal.org/project/views), do, and typically they use the convention of 'BASE_HOOK_NAME\_\_SPECIFIC_OVERRIDE', or a '\_\_' followed by a suffix to create a new theme hook based on an existing one. In Drupal 7, the '\_\_' is now a default pattern for all theme hooks and has been made easier to use. The following is an example of how a module that uses this feature in Drupal 6 can be rewritten for Drupal 7. It's based on the Views module, but the code has been simplified for demonstration purposes (the real code in the Views module is much more complex and feature-rich).

Drupal 6:

``` php
function views_theme() {
  return array(
    'views_view' => array(
      ...
      // The 'pattern' key tells Drupal to auto-discover not just a
      // THEMENAME_views_view() function and 'views-view.tpl.php' file in the
      // theme folder, but also any function matching THEMENAME_views_view__*()
      // and template file matching 'views-view--*.tpl.php'.
      'pattern' => 'views_view__',
    ),
  );
}
function views_page($view_name) {
  $view = views_get_view($view_name);
  // Passing an array as the first parameter to theme(), instead of just a hook
  // name as is more common, tells the theme() function to first check if
  // there's a theme implementation of the first hook, and if not, fall back to
  // the more generic hook.
  return theme(array('views_view__' . $view_name, 'views_view'), $view);
}
```

Drupal 7:

``` php
function views_theme() {
  return array(
    'views_view' => array(
      ...
      // A default pattern of the hook name followed by '__' is automatically
      // assumed. It does not need to be specified.
    ),
  );
}
function views_page($view_name) {
  $view = views_get_view($view_name);
  // theme() automatically falls back to the part of the hook name before the
  // '__' if there's no implementation for the full hook name.
  return theme('views_view__' . $view_name, array('view' => $view));
}
```

Drupal 7 still supports the 'pattern' key and an array for the first argument to theme(), but module maintainers are encouraged to upgrade their modules to use the simplified syntax where possible.

### Preprocess functions need to now specify "theme_hook_suggestion(s)" instead of "template_file(s)"

Issue [\#678714: Unify use of theme hook / template suggestions, fix clobbering problems, and improve suggestion discovery performance](/project/drupal/issues/678714 "Status: Closed (fixed)")

In Drupal 6, template preprocess functions can specify alternate templates that can override the default. In Drupal 7, the syntax for this has changed.

Drupal 6:

``` php
function template_preprocess_node(&$variables) {
  ...
  // If the theme includes a template file named 'node-TYPE.tpl.php', it is
  // used instead of the more generic node.tpl.php file.
  $variables['template_files'][] = 'node-'. $variables['node']->type;
}
```

Drupal 7:

``` php
function template_preprocess_node(&$variables) {
  ...
  // If the theme includes a template file named 'node--TYPE.tpl.php', or a
  // function named THEMENAME_node__TYPE(), it is used instead of the more
  // generic node.tpl.php file. Note that '__' instead of '--' is used here.
  // The theme system converts this to '--' when searching for a template that
  // implements this hook.
  $variables['theme_hook_suggestions'][] = 'node__'. $variables['node']->type;
}
```

One note: Hyphens and underscores play a special role in theme suggestions. Theme suggestions should only contain underscores, because within drupal_find_theme_templates(), underscores are converted to hyphens to match template file names, and then converted back to hyphens to match pre-processing and other function names. So if your theme suggestion contains a hyphen, it will end up as an underscore after this conversion, and your function names won't be recognized.

### Use \#theme='links\_\_MODULE' or \#theme='links\_\_MODULE_EXTRA_CONTEXT' when adding links to a render array

Issue [\#588148: theme_links() is not really themeable](/project/drupal/issues/588148 "Status: Closed (outdated)")

Please see [Move node, taxonomy, and comment links into \$node-\>content; Deprecate hook_link()](#node_links) for information about the change to how to add links to these objects and [\#theme recommended for specifying theme function](#poundtheme) about the use of \#theme in render arrays.

Additionally, because [theme_links()](http://api.drupal.org/api/function/theme_links/7) is such a generic theme function used in many different contexts, and theme developers sometimes want to override just a single context, module developers are encouraged to append extra context information when setting \#theme or calling theme() for 'links'. The extra context information takes the form of '\_\_' followed by the module name, optionally followed by module-specific context.

Example:

``` php
function toolbar_view() {
  ...
  $build['toolbar_menu'] = array(
    '#theme' => 'links__toolbar_menu',
    '#links' => $links,
    '#attributes' => array('id' => 'toolbar-menu'),
    '#heading' => array('text' => t('Administrative toolbar'), 'level' => 'h2', 'class' => 'element-invisible'),
  );
  ...
  return $build;
}
```

This allows a theme developer to add a `THEMENAME_links__toolbar_menu()` function to their template.php file which would override the generic `THEMENAME_links()` or `theme_links()` functions. If there is no theme implementation of 'links\_\_toolbar_menu', the theme system automatically routes to the more generic 'links' hook.

For the case of node or comment links, where many different modules are adding links to the same object, the pattern is extended further and an additional '\_\_' is added to further scope the links your module is adding within the overall group. For example, the blog module adds its node links as follows:

``` php
function blog_node_view($node, $view_mode) {
  ...
  $node->content['links']['blog'] = array(
    '#theme' => 'links__node__blog',
    '#links' => $links,
    '#attributes' => array('class' => array('links', 'inline')),
  );
}
```

This allows a theme developer to override the generic node link theming by implementing `THEMENAME_links__node()` (as above) and include the blog-related links as part of that, but if they render the blog node links separately in their node.tpl.php, they can also choose to theme them separately by implementing `THEMENAME_links__node__blog()`.

### Use \#type='link' for adding a single link to a render array, particularly for tables that include operation links like 'edit', 'delete', etc.

Issue [\#602522: Links in renderable arrays and forms (e.g. "Operations") are not alterable](/project/drupal/issues/602522 "Status: Closed (fixed)")

In most cases, if a module needs to add a set of links to a render array, it should do so by adding an element with \#theme set to 'links\_\_MODULE' ([see above](#theme_links_with_context)). However, in some cases, a module needs to add individual links that should not be themed as a set. The most common use-case for this is "operations" links such as "edit" and "delete" that are added to administrative tables, and where each one needs its own table cell in order for rows that have different sets of operations to properly line up. In this case, each link can be added as a render element with \#type='link'.

Drupal 6:

``` php
// Form element
$form['foo']['bar'] = array('#value' => l(t('list terms'), "admin/content/taxonomy/$vocabulary->vid"));
// Table cell
$row[] = l(t('link title'), 'path/to/location');
```

Drupal 7:

``` php
// Form element
$form['foo']['bar'] = array('#type' => 'link', '#title' => t('list terms'), '#href' => "admin/structure/taxonomy/$vocabulary->vid");
// Table cell
  $row[] = array('data' => array('#type' => 'link', '#title' => t('link title'), '#href' => 'path/to/location'));
```

### Added entity_prepare_view() and hook_entity_prepare_view()

Issue [\#636992: Entity loading needs protection from infinite recursion](/project/drupal/issues/636992 "Status: Closed (fixed)")

[entity_prepare_view()](http://api.drupal.org/api/function/entity_prepare_view/7) should now be called during the \_build_content() and \_view_multiple() phases of entity rendering. This invokes <http://api.drupal.org/api/function/hook_entity_prepare_view/7>, to allow modules to load information which cannot be done during ENTITY_load() (i.e. other entities).

### New pattern for cross-database, performant, case-insensitive comparisons

Using LOWER() for case insensitive comparisons on MySQL doesn't allow for the use of indexes. Using LIKE is more performant, however postgresql treats LIKE as case sensitive. To deal with this, the new database layer now maps LIKE to ILIKE in the postgresql driver when using the query builder. For correct escaping of wildcards, db_like() has also been added.

Drupal 6:

``` php
 $result = db_query_range("SELECT value FROM {profile_values} WHERE fid = %d AND LOWER(value) LIKE LOWER('%s%')", $field, $string, 0, 10);
```

Drupal 7:

``` php
$result = db_select('profile_field')
    ->fields('profile_field', array('category'))
    ->condition('category', db_like($string) . '%', 'LIKE')
    ->range(0, 10)
    ->execute();
```

### Comment rendering overhaul

[Issue](/node/523950). Comment rendering was a bowl of spaghetti since forever. It was straightened out in D7 in order to support a nice \$page array which can be manipulated during [hook_page_build()](http://api.drupal.org/api/drupal/modules--system--system.api.php/function/hook_page_build/7) and [hook_page_alter()](http://api.drupal.org/api/drupal/modules--system--system.api.php/function/hook_page_alter/7). In particular, the comment_render() function is gone. See [comment_node_view()](http://api.drupal.org/api/function/comment_node_view/7) and its call to [comment_node_page_additions()](http://api.drupal.org/api/function/comment_node_page_additions/7).

### taxonomy_form_all() removed

[Issue](/node/693362). This has been removed due to lack of usage, and because calling taxonomy_get_tree() on all vocabularies is a critical scalability issue. If selecting any term is required, an autocomplete field should be used instead.

### New hook_hook_info() added

[Issue](/node/588766). A new hook was added in Drupal 7: [hook_hook_info()](http://api.drupal.org/api/function/hook_hook_info/7). This allows a module to declare a group of hooks whose implementations can be placed in .inc files instead of the main .module file. This is currently done in core for the token hooks: as defined by [system_hook_info()](http://api.drupal.org/api/function/system_hook_info/7), `hook_tokens` and `hook_token_info` implementations can reside in `mymodule.tokens.inc`.

Also note that in Drupal 6, there was a completely separate hook called hook_hook_info(), which was renamed to hook_trigger_info() in the [Trigger and Actions API overhaul](#trigger_overhaul).

### Taxonomy synonyms have been removed

Issue: [\#567572: Remove taxonomy synonyms since Field API is better](/project/drupal/issues/567572 "Status: Closed (fixed)")

The taxonomy synonym functionality has been removed, along with the taxonomy synonym table (term_synonym). To replace this functionality, you can add a synonym field to your vocabulary.

### drupal_goto() follows parameters of url()

[(issue)](http://drupal.org/node/216098) [drupal_goto()](http://api.drupal.org/api/function/drupal_goto/7) is now following (almost) the same parameters as [url()](http://api.drupal.org/api/function/url/7).

D6:

``` php
drupal_goto('node/' . $node->nid . '/delete', $destination);
$form_state['redirect'] = array('node/' . $node->nid . '/delete', $destination);
```

D7:

``` php
drupal_goto('node/' . $node->nid . '/delete', array('query' => $destination));
$form_state['redirect'] = array('node/' . $node->nid . '/delete', array('query' => $destination));
```

The only difference is the additional \$http_response_code argument, which allows to specify the HTTP redirection code (integer).

### hook_user_form(), hook_user_register() are gone

[(issue)](http://drupal.org/node/118345) hook_user_form() and hook_user_register() have been removed from User API in favor of re-using existing Form API concepts.

D6:

``` php
function block_user_form(&$edit, $account, $category) {
  if ($category == 'account') {
```

D7:

``` php
function block_form_user_profile_form_alter(&$form, &$form_state) {
  if ($form['#user_category'] == 'account') {
    $account = $form['#user'];
```

### hook_user_validate() and hook_user_submit() are gone

[(issue)](http://drupal.org/node/118345) hook_user_validate() and hook_user_submit() have been removed from User API in favor of re-using existing Form API concepts.

D6:

``` php
function mymodule_user_validate(&$edit, $account, $category) {
  ...
}
```

D7:

``` php
function mymodule_form_alter(&$form, &$form_state, $form_id) {
  if (!($form_id == 'user_register_form' || $form_id == 'user_profile_form')) {
    return;
  }
  $form['#validate'][] = 'mymodule_user_validate';
}
```

See <http://api.drupal.org/api/function/user_profile_form/7>, <http://api.drupal.org/api/function/user_register_form/7>, and <http://api.drupal.org/api/function/user_account_form/7> for details.

### hook_user_after_update() replaced by hook_user_update(), amended by hook_user_presave() for common operations

[(issue)](http://drupal.org/node/118345) hook_user_insert() and hook_user_update() have been amended by hook_user_presave(), which is invoked both for insert and update operations. hook_user_update() is now invoked **after** the user account has been saved.

D6:

``` php
function profile_user_update(&$edit, $account, $category) {
  return profile_save_profile($edit, $account, $category);
}

function profile_user_insert(&$edit, $account, $category) {
  return profile_save_profile($edit, $account, $category, TRUE);
}
```

D7:

``` php
function profile_user_presave(&$edit, $account, $category) {
  if ($account->uid) {
    profile_save_profile($edit, $account, $category);
  }
}

function profile_user_insert(&$edit, $account, $category) {
  profile_save_profile($edit, $account, $category, TRUE);
}
```

See [hook_user_presave()](http://api.drupal.org/api/function/hook_user_presave/7), [hook_user_insert()](http://api.drupal.org/api/function/hook_user_insert/7), and [hook_user_update()](http://api.drupal.org/api/function/hook_user_update/7) for details.

Also see [user_user_presave()](http://api.drupal.org/api/function/user_user_presave/7) for an example.

### Module .info files can have configure line

Issue: [\#598758: Modules page: add link to its settings page for each module](/project/drupal/issues/598758 "Status: Closed (fixed)")

Module .info files can now include a line giving a link to the main configuration page of the module, which will be shown on the Modules page. For more details, see <http://drupal.org/node/542202#configure>

### Forms are no longer automatically rebuilt when \$form_state\['storage'\] is set

[(issue)](http://drupal.org/node/634440) In Drupal 6, if you set \$form_state\['storage'\] in a form submit or validation handler, the form behaved as if \$form_state\['rebuild'\] was TRUE. This is no longer the case in Drupal 7.

### New method for altering the theme used to display a page (global \$custom_theme variable removed)

Issue: [\#553944: Define hook_menu_get_item_alter() as a reliable hook that runs before the page is doomed](/project/drupal/issues/553944 "Status: Closed (fixed)")

In Drupal 6, modules which wanted to change the theme for a particular page or set of pages (either permanently or based on dynamic conditions at runtime) would set the global \$custom_theme variable, typically either in hook_init() or in the page callback.

This method was relatively confusing and led to a number of subtle bugs. The global \$custom_theme variable has therefore been removed in Drupal 7; instead, modules which want to change the theme can do so via one of two methods:

- To set the theme for a particular page or set of pages, use the new 'theme callback' and 'theme arguments' properties in [hook_menu()](http://api.drupal.org/api/function/hook_menu/7); these work in a similar way as other hook_menu() properties (for example, the title callback) and can be used to set a theme based on information about the currently-visited page.
- To set the theme based on dynamic properties that are not appropriate for hook_menu() (for example, to set it based on the current user's role), use the new [hook_custom_theme()](http://api.drupal.org/api/function/hook_custom_theme/7). This hook will override any theme set via other methods.

See the API documentation or the examples below for more information.

Drupal 6.x:

``` php
/**
 * Implements hook_init().
 */
function mymodule_init() {
  global $user, $custom_theme;

  // Set all node pages (including the node itself, as well as pages for
  // editing it, deleting it, etc.) to default to using the 'some_theme'
  // theme, rather than the site's normal default theme.
  if (arg(0) == 'node' && is_numeric(arg(1))) {
    $custom_theme = 'some_theme';
    // However, for editing page nodes, use the 'some_other_theme' theme
    // instead.
    if (arg(2) == 'edit' && ($node = node_load(arg(1))) && $node->type == 'page') {
      $custom_theme = 'some_other_theme';
    }
  }

  // If the current user has a special role assigned to them, display all
  // pages of the site (including those listed above) using the 'special_theme'
  // theme.
  if (in_array(variable_get('mymodule_special_role', 0), array_keys($user->roles))) {
      $custom_theme = 'special_theme';
  }
}
```

Drupal 7.x:

``` php
/**
 * Implements hook_menu_alter().
 */
function mymodule_menu_alter(&$items) {
  // Set the theme callback function for all node pages. As per the
  // standard behavior for hook_menu() properties, this will be
  // inherited by all paths underneath node/Converting 6.x modules to 7.x as well, unless
  // they define their own theme callback.
  $items['node/Converting 6.x modules to 7.x']['theme callback'] = 'mymodule_default_node_theme';

  // Set a different theme callback for node edit pages, and pass
  // along the node object to this function so we can make decisions
  // based on it.
  $items['node/Converting 6.x modules to 7.x/edit']['theme callback'] = 'mymodule_edit_node_theme';
  $items['node/Converting 6.x modules to 7.x/edit']['theme arguments'] = array(1);
}

/**
 * Defaults to using the 'some_theme' theme for node pages.
 */
function mymodule_default_node_theme() {
  return 'some_theme';
}

/**
 * For editing page nodes, uses the 'some_other_theme' theme.
 */
function mymodule_edit_node_theme($node) {
  return $node->type == 'page' ? 'some_other_theme' : mymodule_default_node_theme();
}

/**
 * Implements hook_custom_theme().
 */
function mymodule_custom_theme() {
  global $user;
  // If the current user has a special role assigned to them, then display all
  // pages of the site (including those listed above) using the 'special_theme'
  // theme.
  if (in_array(variable_get('mymodule_special_role', 0), array_keys($user->roles))) {
    return 'special_theme';
  }
}
```

### New update dependency system, affecting the order in which module updates are run

Issue: [\#211182: Updates run in unpredictable order](/project/drupal/issues/211182 "Status: Closed (fixed)")

Previously, when running update.php, Drupal guaranteed that the core System module's update functions always ran first, but otherwise different modules were updated in a random order. This led to difficulty when (for example) a module had an update function that would only work correctly if another module's update functions ran before it.

In Drupal 7, a new hook, hook_update_dependencies(), has been added that allows modules to declare explicit dependencies between their module's update functions and those of other modules. Drupal will now guarantee that these dependencies are respected when determining the order in which updates are run. Note that no other dependencies can be automatically assumed (for example, the System module's updates are *not* automatically guaranteed to run first), so you should use this hook to specifically declare any dependencies that your module requires.

See the API documentation for [hook_update_dependencies()](http://api.drupal.org/api/function/hook_update_dependencies/7) for more information.

### Block tables renamed

Core's block tables have been renamed. Modules that perform operations directly on the tables are required to upgrade to the new table names:

- 'blocks' renamed to 'block'
- 'blocks_roles' renamed to 'block_role'
- 'boxes' renamed to 'block_custom'

### Block deltas are now specified as strings

Block deltas are now declared as strings instead of hard-coded numeric values:

Drupal 6.x:

``` php
/**
 * Implements hook_block().
 */
function logintoboggan_block($op = 'list', $delta = 0, $edit = array()) {
  global $user;

  switch ($op) {
    case 'list' :
      $blocks[0]['info'] = t('LoginToboggan logged in block');
      $blocks[0]['cache'] = BLOCK_NO_CACHE;
      return $blocks;
      break;
    case 'view' :
      $block = array();
      switch ($delta) {
        case 0:
          if ($user->uid) {
            $block['content'] =  theme('lt_loggedinblock');
          }
          return $block;
      }
      break;
  }
}
```

Drupal 7.x:

``` php
/**
 * Implements hook_block_view().
 */
function logintoboggan_block_view($delta = '') {
  global $user;

  $block = array();
  switch ($delta) {
    case 'logintoboggan_logged_in':
      if ($user->uid) {
        $block['content'] =  array(
          '#theme' => 'lt_loggedinblock',
          '#account' => $user,
        );
      }
      break;
  }
  return $block;
}

/**
 * Implements hook_block_info().
 */
function logintoboggan_block_info() {
  $blocks = array();
  $blocks['logintoboggan_logged_in'] = array(
    'info' => t('LoginToboggan logged in block'),
    'cache' => DRUPAL_NO_CACHE,
  );
  return $blocks;
}
```

**IMPORTANT:** the existing block configurations in core's block tables must be updated to reflect this change, as well as the per-user block configurations. It's strongly recommended to use the [update_fix_d7_block_deltas()](http://api.drupal.org/api/function/update_fix_d7_block_deltas/7) helper function:

``` php
/**
 * Removes hardcoded numeric deltas from blocks.
 */
function logintoboggan_update_7000(&$sandbox) {
  // Get an array of the renamed block deltas, organized by module.
  $renamed_deltas = array(
    'logintoboggan' => array(
      '0' => 'logintoboggan_logged_in',
    ),
  );

  update_fix_d7_block_deltas($sandbox, $renamed_deltas);
}
```

### taxonomy_term_view() and taxonomy-term.tpl.php for term display

Taxonomy terms in Drupal 7 are "fieldable" entities. They can now hold more than a name and description, and their fields can be displayed differently depending on the 'view mode'.

[taxonomy_term_view(\$term, \$view_mode)](http://api.drupal.org/api/function/taxonomy_term_view/7) returns a render array for the term display, complying to the display settings for the fields in the view mode.

Drupal core only defines the 'full' view mode for taxonomy terms, used to display the term at the top of taxonomy listing pages (taxonomy/term/\[tid\]). Like with any other entity, contributed modules can define additional view modes using [hook_entity_info_alter()](http://api.drupal.org/api/function/hook_entity_info_alter/7).

Rendering of the term goes through the `taxonomy-term.tpl.php` theme template, which accepts the following template suggestions: `taxonomy-term--[vocabulary_machine_name].tpl.php`, `taxonomy-term--[term_id].tpl.php`.

### Changed Clean URLs and Search settings page path

[This link goes to separate sub-page describing path changes in Drupal 7](/node/719612)

### url() 'query' field must be array

Issue: [\#578520: Make \$query in url() only accept an array](/project/drupal/issues/578520 "Status: Closed (fixed), Assigned to: sun")

In Drupal 6, the 'query' field for the \$options parameter for url() accepted either a URL-encoded query string to append to the link, or an array of query key/value-pairs without any URL encoding. In Drupal 7, the 'query' field must be an array.

In addition, the new boolean field 'https' is available, which will enforce either HTTPS (if true) or HTTP (if false). If this field is not present, the current scheme will be used. HTTPS can only be enforced when the variable 'https' is set to TRUE.

Drupal 6:

``` php
<?php
  url("node/1", array("query" => "a=b&c=d%40e"));
?>
```

Drupal 7:

``` php
<?php
  print url("node/1", array("query" => array("a"=>"b", "c"=>"d@e")));
?>
```

### Function menu_tree_data() now expects an array of links instead of a query results

[(Issue)](http://drupal.org/node/509584) The [menu_tree_data()](http://api.drupal.org/api/function/menu_tree_data/7) function used to expect a query results. Its first argument must now be an array of links.

See the API documentation for [menu_overview_form()](http://api.drupal.org/api/function/menu_overview_form/7) or the examples below for more information.

Drupal 6.x:

``` php
  $sql = "menu_tree_data
    SELECT m.load_functions, m.to_arg_functions, m.access_callback, m.access_arguments, m.page_callback, m.page_arguments, m.title, m.title_callback, m.title_arguments, m.type, m.description, ml.*
    FROM {menu_links} ml LEFT JOIN {menu_router} m ON m.path = ml.router_path
    WHERE ml.menu_name = '%s'
    ORDER BY p1 ASC, p2 ASC, p3 ASC, p4 ASC, p5 ASC, p6 ASC, p7 ASC, p8 ASC, p9 ASC";
  $result = db_query($sql, $menu['menu_name']);
  $tree = menu_tree_data($result);
```

Drupal 7.x:

``` php
  $sql = "
    SELECT m.load_functions, m.to_arg_functions, m.access_callback, m.access_arguments, m.page_callback, m.page_arguments, m.delivery_callback, m.title, m.title_callback, m.title_arguments, m.type, m.description, ml.*
    FROM {menu_links} ml LEFT JOIN {menu_router} m ON m.path = ml.router_path
    WHERE ml.menu_name = :menu
    ORDER BY p1 ASC, p2 ASC, p3 ASC, p4 ASC, p5 ASC, p6 ASC, p7 ASC, p8 ASC, p9 ASC";
  $result = db_query($sql, array(':menu' => $menu['menu_name']), array('fetch' => PDO::FETCH_ASSOC));
  $links = array();
  foreach ($result as $item) {
    $links[] = $item;
  }
  $tree = menu_tree_data($links);
```

### hook_update_index() only runs when searching enabled for a given module

Issue: [\#704866: Search API doc has some problems](/project/drupal/issues/704866 "Status: Closed (fixed)")

In Drupal 7, a particular module's implementation of hook_update_index() only actually runs if search.module is enabled, and also if on the Search configuration page, your module has been enabled as an active Search module.

### Format date types "small" and "large" have been changed to "short" and "long"

[(issue)](http://drupal.org/node/368408) Date length nomenclature in format_date() have changed.

Example - Drupal 6:

``` php
<?php
$shortdate = format_date($log->timestamp, 'small');
$longdate = format_date($log->timestamp, 'large');
?>
```

Drupal 7:

``` php
<?php
$shortdate = format_date($log->timestamp, 'short');
$longdate = format_date($log->timestamp, 'long');
?>
```

### "Boxes" have been renamed to "custom blocks"

[(issue)](http://drupal.org/node/561970) *"boxes"* table has been renamed to *"block_custom"*.  
All occurences of *"\_box\_"* in function names have been changed to *"\_custom_block\_"*

Example - Drupal 6:

``` php
<?php
$block = block_box_get($bid);
?>
```

Drupal 7:

``` php
<?php
$block = block_custom_block_get($bid);
?>
```

Example - Drupal 6:

``` php
<?php
$result = db_fetch_array(db_query("SELECT * FROM {boxes} WHERE bid = %d", $bid));
?>
```

Drupal 7:

``` php
<?php
$result = db_query("SELECT * FROM {block_custom} WHERE bid = :bid", array(':bid' => $bid))->fetchAssoc();
?>
```

### Remove moderate column from node_schema()

[(Issue)](http://drupal.org/node/564462) The moderate column have been removed from node_schema as there is no longer any moderation in core since Drupal 5. The function hook_schema_alter() should be used by contributed modules which still need this column.

Drupal 6.x:

``` php
function mymodule_nodeapi(&$node, $op, $teaser = NULL, $page = NULL) {
  switch ($op) {
    case 'load':
      return db_fetch_object(db_query('SELECT n.moderate FROM {node} n WHERE n.nid = %d', $node->nid));
    ...
  }
```

Drupal 7.x:

``` php
function mymodule_schema_alter(&$schema) {
  // Add moderate to existing node schema.
  $schema['node']['fields']['moderate'] = array(
    'type' => 'int',
    'not null' => TRUE,
    'default' => 0,
    'description' => 'A boolean indicating whether the node is "in moderation"',
  ),
}

function mymodule_node_load($nodes, $types) {
  return db_query('SELECT n.moderate FROM {node} n WHERE n.nid = :nid', array(':nid' => $node->nid))->fetch();
}
```

If you want multiple options with the IN you need to add en array with all the elements

``` php
 $result = db_query("SELECT rid, name FROM {role} WHERE rid NOT IN (:rid)", array(
   ':rid' =>array(1,2,3),
  )
);
```

### theme_pager() no longer takes limit parameter

The limit parameter of theme_pager() has been dropped. This is now controlled via the limit() method of the query object, such as in [forum_get_topics()](http://api.drupal.org/api/function/forum_get_topics/7).

(Note also that all Drupal 7 theme functions now take only two arguments, as described [here](#theme_changes).)

Drupal 6:

``` php
  theme('pager', $tags, $limit, $element, $parameters, $quantity);
```

Drupal 7:

``` php
  theme('pager', array('tags' => $tags, 'element' => $element, 'parameters' => $parameters, 'quantity' => $quantity));
```

### theme_username() parameters changed

theme_username() now takes multiple parameters, but in Drupal 6 it only accepted one, the user object. It is still possible to call it with just the user object, however.

Drupal 6:

``` php
  $account = user_load($uid);
  print theme("username", $user);
```

Drupal 7:

``` php
  $account = user_load($uid);
  print theme("username", array("account" => $account));
```

### form_clean_id() has been renamed to drupal_html_id()

[(Issue)](http://drupal.org/node/464862) form_clean_id() was frequently used in Drupal 6 to create "safe" names for form element IDs and classes. This has been renamed to [drupal_html_id()](http://api.drupal.org/api/drupal/includes--common.inc/function/drupal_html_id/7) because it was often used on things other than form elements.

Drupal 6:

``` php
  '#id' => form_clean_id("edit-$form_id"),
```

Drupal 7:

``` php
 '#id' => drupal_html_id("edit-$form_id"),
```

### New \#type 'text_format' for text format-enabled form elements

[~~(issue)~~](http://drupal.org/node/125315) and [(issue)](http://drupal.org/node/414424) In Drupal 6, you have been assigning text formats (formerly known as input formats) to textareas by wrapping the textarea into a parent element, and adding a format selector sibling element, such as:

``` php
  $form['comment_filter']['comment'] = array(
    '#type' => 'textarea',
    '#title' => t('Comment'),
    '#default_value' => $default,
  );
  if (!isset($edit['format'])) {
    $edit['format'] = FILTER_FORMAT_DEFAULT;
  }
  $form['comment_filter']['format'] = filter_form($edit['format']);
```

There was no standard for naming, parenting the format selector, so it was impossible to identify textareas with text formats attached (compared to plain text input widgets). It was also common to use this construct with a tree structure, so you'd get \['comment_filter'\]\['comment'\] and \['comment_filter'\]\['format'\] values or a non-tree structure so that you get \['comment'\] and \['format'\].

In Drupal 7, this is all strictly defined and automated with the introduction of the new Form API \#type 'text_format'. Just specify `'#type' => 'text_format'` along with the stored `#format` and Drupal will automatically expand the element to a 'value' and a 'format' element later, so the above code becomes:

``` php
  $form['comment'] = array(
    '#type' => 'text_format',
    '#base_type' => 'textarea', // #base_type is optional.
    '#title' => t('Comment'),
    '#default_value' => $default,
    '#format' => isset($edit['format']) ? $edit['format'] : NULL,
  );
```

If no text format is stored or known yet, just assign `NULL`. The user's [default text format](#default-text-formats) will be automatically selected then.

Optionally, you can additionally specify a `#base_type`, which defaults to 'textarea'. This makes it possible to also attach the text format selector to other form element types, such as textfields.

[filter_form()](http://api.drupal.org/api/function/filter_form/6) in D6 additionally allowed to pass an array of custom \#parents to adjust where the text format value will appear. With the new Form API \#type in D7, you can define custom \#parents for both the text value and text format just like for any other form element:

``` php
  $form['comment'] = array(
    '#type' => 'text_format',
    '#default_value' => $default,
    '#format' => isset($edit['format']) ? $edit['format'] : NULL,
    '#parents' => array('customkey', 'comment'),
  );
```

This would make \$form_state\['values'\] look like:

``` php
  $form_state['values']['customkey']['comment']['value'] = $default
  $form_state['values']['customkey']['comment']['format'] = $format
```

### file_check_directory() and file_create_path() replaced with file_prepare_directory()

([issue](http://drupal.org/node/517814)). [file_prepare_directory()](http://api.drupal.org/api/function/file_prepare_directory/7) will create a directory (including [recursive directory creation](#file_check_directory_recursive)) and/or set directory permissions on the directory.

### Block Cache constants renamed to DRUPAL_CACHE

([\#495968: Introduce drupal_render() cache pattern. Start using it for blocks](/project/drupal/issues/495968 "Status: Closed (fixed), Assigned to: moshe weitzman"))  
BLOCK_CACHE constants got renamed.

Before:

``` php
hook_block($op = 'list', $delta = 0, $edit = array()) {
  if ($op == 'list') {
    return array(
      0 => array(
        'info' => t('Mymodule block #2 describes ...')
        'cache' => BLOCK_CACHE_PER_ROLE | BLOCK_CACHE_PER_PAGE);
      ),
    );
  }
}
```

After:

``` php
hook_block_info($delta = 0, $edit = array()) {
  return array(
    0 => array(
      'info' => t('An amazing block provided by Mymodule.'),
      'cache' => DRUPAL_CACHE_PER_ROLE | DRUPAL_CACHE_PER_PAGE,
    ),
  );
}
```

See <http://api.drupal.org/api/function/hook_block_info/7> for the list of constants.

### New language negotiation API introduced

[(issue)](http://drupal.org/node/282191) In Drupal 6.x there are only four *fixed* possibile setups for language negotiation:

No language negotiation  
Language is always the site's default.

Path prefix  
Language is determined through URL's path prefix. If a path prefix is not found the site's default language is used.

Path prefix with language fallback  
Language is determined through URL's path prefix. If a path prefix is not found, first the user preferences and then the user agent's `Accept-Language` request header are inspected to find an indication of the most appropriate language to use; if no language can be determined, the default language is used.

Domain name  
The language is determined through the domain name associated to each language.

To achieve a greater flexibility in setting up language negotiation rules, a new API has been added in Drupal 7.x (the initial version was part of the UNSTABLE-10 release). If your module implements any functionality related to language negotiation, you may wish to make use of this API.

The new language negotiation API is based on two major concepts:

- **language type**, which has been introduced to support a dedicate language for different entities being involved in the page generation process;
- **language provider**, which is an abstraction of the Drupal 6.x language detection methods already cited above.

Drupal's core defines three *built-in language types*:

Interface language  
It is the page's main language. It is used to present translated user interface elements such as titles, labels, help texts and messages.

Content language  
This is used to choose in which language display content available in more than one language (see the multilingual capabilities of the new Field API for details).

URL language  
This is the language associated to URLs: when generating an URL, this value will be used by [url()](http://api.drupal.org/api/function/url/7) as a default if no explicit preference is provided.

Different language types do not necessarily have different values, rather they will often share the same ones, but the fundamental point is that they can have *independent* values if needed.

The new language API allows contributed modules to define additional language types through [hook_language_types_info()](http://api.drupal.org/api/function/hook_language_types_info/7) and alter existing language type definitions through [hook_language_types_info_alter()](http://api.drupal.org/api/function/hook_language_types_info_alter/7).

A language type may be *configurable* or *fixed*: a configurable language type appears in the language *Detection and selection* page. There are also fixed language types that have predetermined (module-defined) negotiation settings and thus do not appear in the configuration page. Here is a code snippet that makes content language, which by default inherits interface language's value, *configurable*:

``` php
<?php
/**
 * Implements hook_language_types_info_alter().
 */
function language_negotiation_language_types_info_alter(&$language_types) {
  $language_types[LANGUAGE_TYPE_CONTENT] = array(
    'name' => t('Content'),
    'description' => t('If a piece of content is available in multiple languages, the one matching the <em>content</em> language will be used.'),
  );
}
?>
```

Every configurable language type will have its own (independent) language switcher block; obviously if two language types are configured the same way, their language switcher blocks will be identical and will act on both language types.

In Drupal 6.x there is only one language type, named just *language*. During language initialization the selected language negotiation settings are used to determine its value. In Drupal 7.x the same process happens for each defined language type, see [drupal_language_initialize()](http://api.drupal.org/api/function/drupal_language_initialize/7) for details.

Every language type can have different language negotiation settings, i.e. every language type can have a different set of *language detection methods* assigned to it. These are called **language providers** and are simple callback functions that implement a particular logic to return a language code. For instance the [URL language provider](http://api.drupal.org/api/function/locale_language_from_url/7) searches for a valid path prefix or domain name in the current request URL. If a language provider does not return a valid language code, the next one associated to the language type is invoked. This way the concept of fallback is generalized and untied from the fixed *path prefix* \> *user preference* \> *browser settings* \> *default language* scheme used in Drupal 6.x.

Also language providers are [module-definable](http://api.drupal.org/api/function/locale_language_negotiation_info/7) through [hook_language_negotiation_info()](http://api.drupal.org/api/function/hook_language_negotiation_info/7) and language providers definitions can be altered through [hook_language_negotiation_info_alter()](http://api.drupal.org/api/function/hook_language_negotiation_info_alter/7). Here is an example snippet that let path prefixes be ignored for administrative paths:

``` php
<?php
/**
 * Implements hook_language_negotiation_info_alter().
 */
function language_negotiation_language_negotiation_info_alter(&$providers) {
  $providers[LOCALE_LANGUAGE_NEGOTIATION_URL]['callbacks']['language'] = 'language_negotiation_from_url';
  $providers[LOCALE_LANGUAGE_NEGOTIATION_URL]['file'] = drupal_get_path('module', 'language_negotiation') . '/language_negotiation.module';
}

/**
 * Identify language via URL prefix or domain excluding administrative paths.
 */
function language_negotiation_from_url($languages) {
  // Use the core URL language provider to get a valid language code.
  require DRUPAL_ROOT . '/includes/locale.inc';
  $langcode = locale_language_from_url($languages);

  // If we have an administrative path just return the default language.
  if (isset($_GET['q']) && strtok($_GET['q'], '/') == 'admin') {
    return language_default()->language;
  }

  return $langcode;
}
?>
```

Language provider definitions may include two more callbacks besides the language provider itself:

- if the language provider can take advantage of a language switcher block, the `switcher` callback will allow it to return the language switch links that suit its logic, see [locale_language_switcher_url()](http://api.drupal.org/api/function/locale_language_switcher_url/7) for an example;
- if the language provider needs to rewrite URLs, it can specify an `url_rewrite` callback which will provide the [rewriting logic](http://api.drupal.org/api/function/locale_language_url_rewrite_url/7).

### WATCHDOG_EMERG was renamed to WATCHDOG_EMERGENCY

[(issue)](http://drupal.org/node/739450) WATCHDOG_EMERG was renamed to WATCHDOG_EMERGENCY for consistency with other watchdog level constants.

### system_retrieve_file() API cleanup

[(issue)](http://drupal.org/node/573300) The signature of system_retrieve_file() changed to support managed files and conform to the file API. It was changed from `system_retrieve_file($url, $destination = NULL, $overwrite = TRUE)` to `system_retrieve_file($url, $destination = NULL, $managed = FALSE, $replace = FILE_EXISTS_RENAME)`

### menu_default_node_menu replaced with per-content type settings

[(issue)](http://drupal.org/node/351249) and [(issue)](http://drupal.org/node/716792) Previously, there was a global menu_default_node_menu setting to hold the parent menu for node parent choosers. This was made per content type, and thus the variable name varies per content type, it is: `'menu_parent_' . $node->type`.

### COMMENT_NODE\_\* constants have new names, but same values

[(issue)](http://drupal.org/node/394374) The constants that hold the values for the comment permissions per node were given new names.

| Drupal 6                | Drupal 7            | Value |
|-------------------------|---------------------|-------|
| COMMENT_NODE_DISABLED   | COMMENT_NODE_HIDDEN | 0     |
| COMMENT_NODE_READ_ONLY  | COMMENT_NODE_CLOSED | 1     |
| COMMENT_NODE_READ_WRITE | COMMENT_NODE_OPEN   | 2     |

### Drupal.parseJson has been removed and replaced with jQuery.parseJSON

[(issue)](http://drupal.org/node/673884) As of jQuery 1.4.1, it provided the ability to parse JSON in a manner that utilizes native browser JSON parsing when available. Drupal 7 switches to use the JSON parsing provided by jQuery rather than providing its own. For more details on jQuery.parseJSON see the [API documentation](http://api.jquery.com/jQuery.parseJSON/).

In Drupal 6:

``` php
 response = Drupal.parseJson(response);
```

In Drupal 7:

``` php
response = jQuery.parseJSON(response);
```

### New 'restrict access' parameter in hook_permission() for labeling unsafe permissions

[(issue)](http://drupal.org/node/248598) In addition to title and description keys (described [above](#descriptions_permissions)), permissions now have an optional 'restrict access' key, which can be provided and set to TRUE to indicate that site administrators should restrict access to this permission to trusted users.

This should be used sparingly, for permissions that have inherent security risks (for example, the "administer filters" and "bypass node access" permissions provided by Drupal core). When set to TRUE, a standard (but themeable) warning message will be associated with the permission and displayed with it on the permission administration page.

Example:

``` php
/**
 * Implements hook_permission().
 */
function mymodule_permission() {
  return array(
    'use PHP in mymodule' => array(
      'title' => t('Use PHP in mymodule'),
      'description' => t('Execute arbitrary PHP code on the mymodule administration pages.'),
      'restrict access' => TRUE,
    ),
  );
}
```

### Removal of FAPI \$form\['#redirect'\] and \$\_REQUEST\['destination'\]

\$form\['#redirect'\] and \$\_REQUEST\['destination'\] are no longer supported. ([issue](http://drupal.org/node/579366)).

\$form\['#redirect'\] has been replaced by \$form_state\['redirect'\], which takes the same values as [drupal_goto()](http://api.drupal.org/api/function/drupal_goto/7)

\$\_REQUEST\['destination'\] has been replaced by \$\_GET\['destination'\].

Drupal 6 form redirect default:

``` php
function my_form(&$form_state) {
  $form['submit'] = array(
    '#type' => 'submit',
    '#value' => t('Push this'),
  );
  $form['#redirect'] = 'node';
  return $form;
}
```

Drupal 7 form redirect default:

``` php
function my_form($form, &$form_state) {
  $form['submit'] = array(
    '#type' => 'submit',
    '#value' => t('Push this'),
  );
  $form_state['redirect'] = 'node';
  return $form;
}
```

### User-configured time zones now serve as the default time zone for PHP date/time functions

Drupal now sets the PHP default time zone on each request to the user-configured time zone or, if user-configured time zones are disabled, to the administrator-configured default time zone ([Issue](http://drupal.org/node/348448)).

In previous versions of Drupal, calls to PHP date/time functions (such as `date()`, `mktime()`, and `strtotime()`) use a time zone determined from the `date.timezone` PHP ini setting or the `TZ` server environment variable.

The following would be a suitable replacement for calls to the PHP `date()` function and uses the default time zone even when user-configured time zones have been enabled: ` format_date($timestamp, 'custom', $format, variable_get('date_default_timezone', date_default_timezone_get()), 'en'); `

### db_is_active() has been removed

([Issue](http://drupal.org/node/688294)) Switch from db_is_active() to proper exception catching.

In Drupal 6 and earlier, if code might run in a situation where a database was not yet available it could call db_is_active() to determine if there was a database to use. In Drupal 7, code should simply run queries as normal and include a try-catch block around the relevant section of code. If an exception is caught for an unavailable or invalid database the code can take appropriate action.

### node body field instances are now handled exclusively by field API

([issue](http://drupal.org/node/553306)) When defining a node type or creating one with node_type_save(), the 'has_body' and 'body_label' keys have been deprecated.

To add a body field, you can instead call node_add_body_field(\$type); which will add the field instance to that node type. See blog.install and forum.install for examples.

### Rename file to file_managed

([Issue](http://drupal.org/node/741578)) Rename file to file_managed.

### New hook_module_implements_alter

([Issue](http://drupal.org/node/692950)) Modules may now alter the list of modules implementing a hook. This means that rather than changing a module's system weight globally, a module can change the order it's called for a specific hook. See [hook_module_implements_alter](http://api.drupal.org/api/function/hook_module_implements_alter/7) for more information and examples.

### Database prefixes are now per connection

([Issue](http://drupal.org/node/195416)) Database prefixes are no longer specified by a global \$db_prefix string/array. Instead, they are specified per-connection by a 'prefix' array key for each connection. The prefix may still be either a string or array depending on what tables are to be prefixed. See the documentation in settings.php for full details.

### Form submit buttons consistently grouped in actions array

([Issue](http://drupal.org/node/482816)) All forms in Drupal 7 core now use an additional 'actions' array key to hold one or more buttons at the bottom of *or elsewhere in* a form, including cache clearing buttons, overview filter forms, etc. Consistent use of 'actions' as the key on this element enables consistent styling in themes and enables other modules to properly alter a form's actions.

All modules implementing hook_form_alter() or hook_form_FORM_ID_alter() to modify, remove, or add to these buttons will have to take the new form actions into account.

D6:

``` php
  $form['submit'] = array(
    '#type' => 'submit',
    '#value' => t('Save'),
  );
  $form['delete'] = array(
    '#type' => 'button',
    '#value' => t('Delete'),
  );
  $form['cancel'] = array(
    '#markup' => l(t('Cancel'), 'foo/bar'),
  );
```

D7:

``` php
  $form['actions'] = array('#type' => 'actions');
  $form['actions']['submit'] = array(
    '#type' => 'submit',
    '#value' => t('Save'),
  );
  $form['actions']['delete'] = array(
    '#type' => 'button',
    '#value' => t('Delete'),
  );
  $form['actions']['cancel'] = array(
    '#markup' => l(t('Cancel'), 'foo/bar'),
  );
```

### New constants for user registration settings, and the default has been changed to "Visitors, but administrator approval is required"

([issue](http://drupal.org/node/174972)) The 'user_register' variable (which defines how and if users are allowed to create their own accounts) previously used integers to refer to its three possible options. In Drupal 7, defined constants have been introduced for these options, which should be used in all code instead. The constants are:

- [USER_REGISTER_ADMINISTRATORS_ONLY](http://api.drupal.org/api/constant/USER_REGISTER_ADMINISTRATORS_ONLY/7)
- [USER_REGISTER_VISITORS](http://api.drupal.org/api/constant/USER_REGISTER_VISITORS/7)
- [USER_REGISTER_VISITORS_ADMINISTRATIVE_APPROVAL](http://api.drupal.org/api/constant/USER_REGISTER_VISITORS_ADMINISTRATIVE_APPROVAL/7)

Also, not specifically an API change, but through Drupal 6, the default user creation setting allowed visitors to create their own accounts, causing many new sites to have many unwanted/spam accounts. In Drupal 7, the default is "Visitors, but administrator approval is required" (USER_REGISTER_VISITORS_ADMINISTRATIVE_APPROVAL). Sites upgraded from Drupal 6 keep the same settings they had in Drupal 6.

Example code for 7.x:

``` php
if (variable_get('user_register', USER_REGISTER_VISITORS_ADMINISTRATIVE_APPROVAL) == USER_REGISTER_VISITORS) {
  // Do something.
}
```

### hook_form_alter and hook_form_FORM_ID_alter run together for each module

([issue](http://drupal.org/node/765860)) In Drupal 6, hook_form_alter() was executed for all modules before hook_form_FORM_ID_alter(). This meant that although hook_form_FORM_ID_alter() was great for code clarity and organization, it actually couldn't be used in places like the node forms, etc, where other modules had already altered using hook_form_alter() and another module wanted to change that using hook_form_FORM_ID_alter(). In Drupal 7, hook_form_alter() and hook_form_FORM_ID_alter() invoke by module and module weight, so a higher weighted module can hook_form_FORM_ID_alter() what a lower-weighted module added with hook_form_alter(). How many forms could a hook_form_alter() alter if a hook_form_alter() could?

### Arguments to xmlrpc() have changed

([issue](http://drupal.org/node/881536)) In order to fix the problem that options could not be passed into the drupal_http_request() call used by xmlrpc() (for example, to set the timeout or custom headers) the arguments to xmlrpc have changed. Now all the XML-RPC methods and parameters are passed in an array as the second argument, while the optional third argument is an array of options for drupal_http_request().

Single method call:

Drupal 6.x (any number of arguments could be passed after the method name):

``` php
$singlecall = xmlrpc($url, 'methodName', $arg1, $arg2, $arg3, ...);
```

Drupal 7.x (any number of arguments can be passed as the array values where the method name is the key):

``` php
$singlecall = xmlrpc($url, array(
  'methodName' => array($arg1, $arg2, $arg3, ...),
));
```

or with options for drupal_http_request():

``` php
$singlecall = xmlrpc($url, array('methodName' => array(...)), $options);
```

Multicall:

Drupal 6.x (an array of arrays of methods and arguments as the second parameter):

``` php
$multicall = xmlrpc($url, array(
  array('firstMethod', $arg1, $arg2),
  array('secondMethod', $arg1, $arg2),
  ...
));
```

Drupal 7.x (same as single call, just more than one element):

``` php
$multicall = xmlrpc($url, array(
  'firstMethod' => array($arg1, $arg2),
  'secondMethod' => array($arg1, $arg2),
  ...
));
```

### Translatable Fields

[(issue)](http://drupal.org/node/367595), [(issue)](http://drupal.org/node/565480) and [(issue)](http://drupal.org/node/657972) Native multilingual capabilities were added to the Field API. The initial commit was part of the UNSTABLE-9 release. See the [Field language API](http://api.drupal.org/api/group/field_language/7) for a complete reference.

### Filter table updates

[(issue)](http://drupal.org/node/685486) In Drupal 7, the {filter} table has a new unique key. So [filter_update_7003()](http://api.drupal.org/api/drupal/modules--filter--filter.install/function/filter_update_7003/7) saves the old {filters} table from Drupal 6 as {d6_upgrade_filter}, before saving the core filters in the new {filter} table. Contrib modules need to also save their filters in the new {filter} in a Drupal 6 to Drupal 7 update function, similar to what is done in filter_update_7003(), and making new unique key values.

### file_directory_path() has been removed

[(Issue)](http://drupal.org/node/895308) `file_directory_path()` has been removed because file paths are now represented as stream wrapper URLs. In most cases, the replacement code will be ` file_default_scheme() . '://' `

However, if any operations will be performed on the path which require a local file system, we cannot rely on `file_default_scheme()`, which may be configured as a remote resource. In these cases you must force usage of the public scheme, which will always be a local file system: ` 'public://' ` Note, when calling functions on a path which are not compatible with stream wrappers, such as `chdir()` or `imagepng()`, you must convert the stream wrapper URL into a real path: ` drupal_realpath('public://...') `

If you need the relative path of `public://`, use ` variable_get('file_public_path', conf_path() . '/files') ` This gives you exactly the same as `file_directory_path()` in D6.

The [handbook page on file API](http://drupal.org/node/555118) goes into more detail about how to use stream wrapper URLs.

### hook_form_BASE_FORM_ID_alter() is invoked for shared form constructors

([issue](http://drupal.org/node/757154)) When registering a shared form ID via [hook_forms()](http://api.drupal.org/api/function/hook_forms/7), such as `example_article_form()` (`example_TYPE_form()`), using the shared form constructor `example_form()`, then Form API only auto-suggested and automatically applied a \#validate handler (if existent) `example_TYPE_form_validate()` and a \#submit handler (if existent) `example_TYPE_form_submit()`, but it did not check whether there are any handlers for the shared base form ID `example_form()`, which is obviously much more likely the case, as the form_ids that using shared form constructors are usually derived from user configuration (and rarely enforced via code).

In D7, Form API additionally checks for the base form ID handlers `example_form_validate()` and `example_form_submit()`, but only if it did not find handlers for the form_id.

In D7, Form API also invokes drupal_alter() for the base form ID; i.e., both the specific `hook_form_FORM_ID_alter()` and the generic `hook_form_BASE_FORM_ID_alter()` are invoked. For example, this allows you to alter the node form regardless of node type by implementing `hook_form_node_form_alter()`; i.e., without ugly checking for (the hereby obsolete) `$form['#node_edit_form']`.

In D7, Form API also auto-suggests a \#theme function based on the shared base form ID; i.e., if no `theme_example_TYPE_form` theme function has been registered, but there is a `theme_example_form` theme function, then the latter is automatically set in `$form['#theme']` -- unless the form constructor manually defined a \#theme value.

### `comment_form` form ID changed to `comment_node_TYPE_form`

([issue](http://drupal.org/node/757154)) Since comments can have different fields attached per node type, the comment form is effectively vastly different for every node type. Therefore, the previously existing form ID `comment_form` has been renamed to `comment_node_TYPE_form`, whereas TYPE refers to `$node->type`. The shared form constructor function `comment_form()` still exists, but the changed behavior of shared form constructors is applied - make sure to read upgrade notes about [hook_form_BASE_FORM_ID_alter()](#hook_form_BASE_FORM_ID_alter).

D6:

``` php
  $output = drupal_get_form('comment_form', $node);
```

D7:

``` php
  $build = drupal_get_form("comment_node_{$node->type}_form", $node);
```

This change also made comment form IDs consistent with node form IDs (`node_TYPE_form`), and additionally made the comment form ID consistent with Comment module's very own registered entity bundle names (`comment_node_TYPE`).

### Text formats (input formats) must be defined

([issue](http://drupal.org/node/358437)) All modules which store text format IDs in their database tables need to update this data to work with the filter system changes in Drupal 7. The essential change is that "0" or invalid text formats should no longer be stored at all; all data must be updated to an actual text format that exists on the site. In the case of empty content that does not exist yet, NULL can be used to indicate no format.

For example, if you module's database table has a 'sometext' column which stores text and a 'sometext_format' column which stores the text format that will be passed in to check_markup() when the content is filtered for display, you will need to perform this update.

For a complete example of such an update function, see [user_update_7010()](http://api.drupal.org/api/function/user_update_7010/7). (Note that if you are following that example exactly in your own code, you will need to write a separate update function afterwards that converts the database column from an integer to a string, due to the change discussed in the section [below](#text_format_string).)

### Text format ('format') identifier is a machine name now

([issue](http://drupal.org/node/934050)) In Drupal 6, text formats were identified by a numeric serial id. The column "format" in the table "filter_format" was of type 'int'. For Drupal 7, all 'format' columns need to be updated to be a string now.

If your module handles references to text formats it needs to take into account that these references are strings, not numerics. Consider this example for storing format identifiers:

Drupal 6:

``` php
$schema = array(
  'example_text_field' => array(
    'type' => 'text',
  ),
  'format' => array(
    'type' => 'int',
    'unsigned' => TRUE,
    'not null' => FALSE,
  ),
);
```

Drupal 7:

``` php
$schema = array(
  'example_text_field' => array(
    'type' => 'text',
  ),
  'format' => array(
    'type' => 'varchar', // Format is a varchar now.
    'length' => 255, // With maximum 255 characters.
    'not null' => FALSE,
  ),
);
```

Note: Existing numeric text format identifiers continue to be numeric. They merely need to be converted into strings for Drupal 7.

Additionally, when creating a new or updating an existing text format, the text format's machine name has to be specified as \$format-\>format:

Drupal 6:

``` php
$format = new stdClass();
$format->name = $name;
db_query("INSERT INTO {filter_formats} (name) VALUES ('%s')", $format->name);
$format->format = db_result(db_query("SELECT MAX(format) AS format FROM {filter_formats}"));
```

Drupal 7:

``` php
$filtered_html_format = array(
  'format' => 'filtered_html',
  'name' => 'Filtered HTML',
);
$filtered_html_format = (object) $filtered_html_format;
filter_format_save($filtered_html_format);
```

### MENU_CALLBACK meaning has changed for breadcrumbs, and some other menu API changes

[(Issue)](http://drupal.org/node/907690) In order to have breadcrumbs work better, the meaning of the MENU_CALLBACK constant changed. In your module's hook_menu(), you should only use 'type' =\> MENU_CALLBACK for items that are real callbacks (i.e., hidden, internal callbacks, typically used for API calls, with no menu or breadcrumbs). Previously, although MENU_CALLBACK was documented to have the same meaning in Drupal 6.x, items with type MENU_CALLBACK still had breadcrumbs. They don't any more, and therefore the menu routing processing is much faster.

In addition, there were some changes to mostly internal-use functions in menu.inc and theme.inc. If you have a module that is doing menu tree building or breadcrumb overrides, you should check the patches in the issue to see what changed. (The primary patch is on comment \#55, and there was one follow-up that didn't change much.)

### The *datetime* field type has been removed in favour of database engine specific types

[Issue](http://drupal.org/node/866340), [Followup](http://drupal.org/node/927828)

While previously modules could define database schema containing fields of type *datetime*, core support for the datetime type has been removed in D7. Supporting a core type of 'datetime' made it artifically appear portable, which in fact has never been the case.

Modules wishing to rely on a database specific datetime type, now have to define them just like any other types that are not supported by core. If the Field API is used, types not supported by core can be provided using the 'mysql_type', 'pgsql_type' and 'sqlite_type' properties in hook_field_schema().  
Drupal 6:

``` php
  $schema['mymodule_table'] = array(
    'description' => 'My table',
    'fields' => array(
      'id' => array(
        'description' => 'The id',
        'type' => 'serial'
      ),
      'calendar_dt' => array(
        'description' => 'Date field',
        'type' => 'datetime',
        'not null' => FALSE,
      ),
    ),
  );
```

Drupal 7:

``` php
  $schema['mymodule_table'] = array(
    'description' => 'My table',
    'fields' => array(
      'id' => array(
        'description' => 'The id',
        'type' => 'serial'
      ),
      'calendar_dt' => array(
        'description' => 'Date field',
        'mysql_type' => 'DATETIME',
        'pgsql_type' => 'timestamp without time zone',
        'not null' => FALSE,
      ),
    ),
  );
```

### Arbitrary user data is now harder to stash in the \$user object

In Drupal 6 you could add nearly anything to the \$user object and it would magically be saved into \$user-\>data and from there into the data column of the users table. This is no longer so easy. If you want to save arbitrary data in the user object, you now have to specifically handle that in [hook_user_presave()](http://api.drupal.org/api/drupal/modules--user--user.api.php/function/hook_user_presave/7).

Drupal 6:

``` php
user_save($account, array('some_random_stuff' => 'surprisingly random');
```

Drupal 7:

``` php
$stuff = array('some_random_stuff' => 'surprisingly_random');
user_save($account, array('mymodule' => $stuff);

...
function mymodule_user_presave(&$edit, $account, $category) {
  // Make sure that our form value 'mymodule_foo' is stored as 'mymodule_bar'.
  if (isset($edit['mymodule']['some_random_stuff'])) {
    $edit['data']['mymodule']['some_random_stuff'] = $edit['mymodule']['some_random_stuff'];
  }
}
```

Note that the whole \$user-\>data concept and the data column of the users table will likely be removed in Drupal 8, so it may be time to just have your application manage its own table for this sort of thing.

See [hook_user_presave()](http://api.drupal.org/api/drupal/modules--user--user.api.php/function/hook_user_presave/7) for an example of this in action.

### Two new functions added: hook_page_build() and hook_page_alter()

[(issue)](http://drupal.org/node/558958) Drupal 7 adds two new hooks: [hook_page_build()](http://api.drupal.org/api/drupal/modules--system--system.api.php/function/hook_page_build/7) and [hook_page_alter()](http://api.drupal.org/api/drupal/modules--system--system.api.php/function/hook_page_alter/7). Both functions provide access to the \$page array, but hook_page_build() runs before hook_page_alter(). If your module only adds elements to the \$page array, use hook_page_build(). If your module alters elements or adds elements that depend on the elements added by other modules, use hook_page_alter().  
The separation between adding elements to the page and altering existing elements was done to avoid conflicts when multiple modules want to access the \$page array. This makes it easy to add elements to \$page without having to worry about the order in which the modules are run. If you want to access existing elements (possibly added by other contrib modules), then use hook_page_alter().

### l() function class attribute

In Drupal 7 class attributes for links created by the [l() function](http://api.drupal.org/api/drupal/includes--common.inc/function/l/7) are now specified with an array. In past versions the classes were given as a string.

Drupal 6:

``` php
$options = array('attributes' => array(
  'class' => 'class-1 class-2 class-3',
  )
);
```

Drupal 7:

``` php
$options = array('attributes' => array(
  'class' => array('class-1', 'class-2', 'class-3'),
  )
);
```

### Javascript and CSS loading changes

Javascript and CSS loading have been affected by a number of issues, notably [\#954804](http://drupal.org/node/954804) and [\#769226](http://drupal.org/node/769226).

- When loading JavaScript provided by core (or any other js files that are defined as libraries), please make sure to use drupal_add_library(), not drupal_add_js(). All the core js files are defined as libraries. If you use drupal_add_js() for these it may actually cause the weighting of files to be corrupted.

- If your javascript or CSS is to be loaded on every page, there's no need to write any code for it at all any more, as it can just be included in the module's .info file. This allows Javascript or CSS to be aggregated in an optimal way, and is the preferred method of adding Javascript or CSS that most visitors will need on a typical site visit:  

  ``` php
  scripts[] = mymodule.js
  stylesheets[all][] = mymodule.css
  ```

  Scripts is an indexed array. Stylesheets are an associative array of files, with their media type (e.g. all, print, screen) as the initial key.

- If your javascript or CSS is required on specific pages, but is not involved with a form, use drupal_add_library() for libraries, or drupal_add_js()/drupal_add_css() as needed.

- If your javascript or CSS is required for a particular form, use the [FAPI \#attached mechanism](http://api.drupal.org/api/drupal/developer--topics--forms_api_reference.html/7#attached) to provide it (see also [drupal_process_attached()](http://api.drupal.org/api/drupal/includes--common.inc/function/drupal_process_attached/7)):  

  ``` php
  '#attached' => array(
    'js' => array(drupal_get_path('module', 'mymodule') . '/mymodule_form_loaded.js'),
    'css' => array(drupal_get_path('module', 'mymodule') . '/mymodule_form_loaded.css'),
  ),
  ```

- If you actually have a set of CSS and js that should be considered a library, and can be provided as a library package to other functions, define it using hook_library() and then add it to pages either by using \#attached\['library'\] or drupal_add_library(). This is the preferred way to deal with libraries which might be used by other modules:  

  ``` php
  function mymodule_library() {
    $libraries['sooper-dooper-jquery'] = array(
      'title' => 'Sooper Dooper jQuery',
      'website' => 'http://sooper.dooper.jquery.example.com',
      'version' => '1.2',
      'js' => array(drupal_get_path('module', 'mymodule') . '/sooper.dooper.js' => array()),
      'css' => array(drupal_get_path('module', 'mymodule') . '/sooper.dooper.css'),
    );
    return $libraries;
  }
  ...
  $form['#attached']['library'] = array(array('mymodule', 'sooper-dooper-jquery'));
  ```

### Node, filter and comment modules tables renamed to singular

[(issue)](http://drupal.org/node/335086) Some database tables have been renamed to the singular for consistency.

In the node module: {node_revisions} table was changed to {node_revision}  
In the filter module: {filters} table was changed to {filter} and {filter_formats} table was changed to {filter_format},  
In the comment module: {comments} table was changed to {comment}.

### 'post comments without approval' permission name changed

[(issue)](http://drupal.org/node/438224) The 'post comments without approval' (D6) permission became 'skip comment approval' in Drupal 7. This is a change to the machine name of this permission.

### New 'properties' element of block information

[(issue)](http://drupal.org/node/601932) With the introduction of the Dashboard in Drupal 7, it became clear that not all blocks should be available for adding to the dashboard. So, a new 'properties' element was added to the return value in [hook_block_info()](http://api.drupal.org/api/drupal/modules--block--block.api.php/function/hook_block_info/7). If you want your module's blocks to be available for the Dashboard, you need to set an 'administrative' property in your hook_block_info(). For example:

``` php
  $blocks['recent'] = array(
    'info' => t('Recent content'),
    'properties' => array('administrative'),
  );
```

### \$element\['#post'\] is gone

[(issue - note: this is only the issue where someone asked where it went, not the issue where it was actually changed - no one seems sure where that was, sorry!)](http://drupal.org/node/734498)

In the Form API, \$form\['#post'\] and \$element\['#post'\] no longer exist. If you had a good, solid reason to use \$form\['#post'\] or \$element\['#post'\], you can use \$form_state\['input'\], which has the same information.

However, processed values are available in \$form_state\['values'\] and \$element\['#value'\] , and the element that triggered the form submission is in \$form_state\['triggering element'\], so you are highly encouraged to use those. Also, information in \$form_state\['input'\] is unsanitized, so never copy it to the database!

### node_load() and other entity loading cache behavior has changed

In Drupal 6, some functions such as node_load() that worked with a cache would explicitly clone the object before returning, so that if the calling function changed the object, it wouldn't affect the cache.

In Drupal 7, the situation is quite a bit more complicated, and you cannot rely on this cloning. The reason is that loading of nodes and other entities is handled by entity_load(), which uses a pluggable entity controller class to do the loading. The default controller class will not clone cacheable objects before returning (whether an entity is cacheable or not is defined by hook_entity_info()), and as the node entity is cacheable, nodes are not cloned -- this is a change from the Drupal 6 behavior. However, the controller class is pluggable, so your module cannot actually rely on nodes not being cloned, for a given Drupal installation.

The upshot of this is that if your module plans to load an entity (node, comment, etc.) and then modify it, you should probably clone the object first to be safe.

### \$form_state\['clicked_button'\] is deprecated, use \$form_state\['triggering_element'\] instead

([Issue](/node/1049462)) If your code uses `$form_state['clicked_button']`, replace it with `$form_state['triggering_element']`.

In most cases there is no difference, it is still reference to the clicked button. However, in Drupal 7, AJAX operations in a form can be triggered without a form button. `$form_state['triggering_element']` holds whatever page element that triggered the AJAX operation, which may be a form button, a link, or anything else.

### Database driver prefix handling has changed

Database drivers that have their own custom prefix handling may need to update for a change introduced by this issue [\#561422: Replace strtr() with str_replace() for db prefixing](/project/drupal/issues/561422 "Status: Closed (outdated)"). See the issue itself for discussion and code changes.
