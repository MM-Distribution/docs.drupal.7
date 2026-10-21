---
title: "Cascading select using views"
source_url: "https://www.drupal.org/docs/7/howtos/cascading-select-using-views"
page_type: page
last_updated: "Last updated on 25 January 2018"
published: "2011-04-08T17:05:18+00:00"
modified: "2018-01-25T23:39:26+00:00"
breadcrumb: ["Drupal 7", "Site building and development HowTos for Drupal 7"]
fetched: "2026-10-21T08:01:02Z"
raw: "raw/docs/7/howtos/cascading-select-using-views.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Cascading select using views

## Introduction

This how-to describes by example how to provide a cascading select (e.g. dropdowns)  
using the [Views module](/project/views "Go to Views project page")  
with Attachment displays. Like this, we can use the whole power of Views to select and display the items of a given level.

This how-to is based on [J. Ayen Green](/user/367108 "Go to J. Ayen Green's drupal.org profile")'s  
book "[Drupal 6 Attachment Views](https://www.packtpub.com/drupal-6-attachment-views/book "Go to Drupal 6 Attachment Views bock on packtpub.com")". Thanks!

*This how-to serves as a proof of concept, it needs fine-tuning to be production-ready.*

### What

We use an **incident support agent example** (with dropdowns):

1.  User selects an incident (problem) category
2.  User selects a subcategory ([screenshot](http://dl.dropbox.com/u/25126912/CascadingSelectUsingViews/casc-select-ex-incident-00-1-select.png "Opens incidents example screenshot 'select'"))
3.  User selects a subcategory
4.  Possible solutions and a form are displayed for a given subcategory ([screenshot](http://dl.dropbox.com/u/25126912/CascadingSelectUsingViews/casc-select-ex-incident-00-2-result.png "Opens incidents example screenshot 'result'"))

*Note: solutions and/or a form can be displayed at any level.*

### How

1.  Add forms using the [Webform module](/project/webform "Go to Webform project page")
2.  Add content types "Incident solution"
3.  Add content types "Incident item"
4.  Create an incident tree using the [References module](/project/references "Go to References project page")
5.  Add a view "incident" using the [Views module](/project/views "Go to Views project page")
    - Add a Page display for the 1st level
    - Add an Attachment display for the 2nd level
    - Add an Attachment display for the 3rd level
    - Modify the templates
    - Add an Attachment display for the solutions
    - Add an Attachment display for the form

## Requirements

- [Views module](/project/views "Go to Views project page")
- [References module](/project/references "Go to References project page")
- [Node Reference URL Widget module](/project/nodereference_url "Go to Node Reference URL Widget project page") *(optional)*
- [Webform module](/project/webform "Go to Webform project page")
- [Webform validation module](/project/webform_validation "Go to Webform validation project page") *(optional)*
- [CAPTCHA module](/project/captcha "Go to CAPTCHA project page") *(optional)*
- *Note: you are expected to have a working knowledge of the above modules.*

## Instructions

([All screenshots as a gallery.](http://www.dropbox.com/gallery/25126912/1/CascadingSelectUsingViews?h=767b74 "Opens incidents example screenshots gallery"))

1.  Add forms using the [Webform module](/project/webform "Go to Webform project page") ([screenshot](http://dl.dropbox.com/u/25126912/CascadingSelectUsingViews/casc-select-ex-incident-01-add-webform.png "Opens incidents example screenshot of this step"))
2.  Add content types "Incident solution" ([screenshot](http://dl.dropbox.com/u/25126912/CascadingSelectUsingViews/casc-select-ex-incident-02-add-content-type-solution.png "Opens incidents example screenshot of this step"))
3.  Add content types "Incident item" ([screenshot](http://dl.dropbox.com/u/25126912/CascadingSelectUsingViews/casc-select-ex-incident-03-add-content-type-item.png "Opens incidents example screenshot of this step"))
4.  Create an incident tree with incident items (nodes of type "Incident item") using the node reference relationship "Parent" (the field type is provided by the [References module](/project/references "Go to References project page")) ([screenshot](http://dl.dropbox.com/u/25126912/CascadingSelectUsingViews/casc-select-ex-incident-04-item-list.png "Opens incidents example screenshot of this step"))
    - ROOT
      - Cat 1
        - Subcat 1.1
          - Subsubcat 1.1.1
          - Subsubcat 1.1.2
        - Subcat 1.2
        - Subcat 1.3
        - Subcat 1.4
        - Subcat 1.5
      - Cat 2
        - Subcat 2.1
      - Cat 3
        - Subcat 3.1
      - Cat 4
        - Subcat 4.1
        - Subcat 4.2
5.  Add a view "incident" using the [Views module](/project/views "Go to Views project page") ([screenshot](http://dl.dropbox.com/u/25126912/CascadingSelectUsingViews/casc-select-ex-incident-05-add-view.png "Opens incidents example screenshot of this step"))
    - Configure view defaults (used for the 3 levels) ([screenshot](http://dl.dropbox.com/u/25126912/CascadingSelectUsingViews/casc-select-ex-incident-06-view-config-defaults.png "Opens incidents example screenshot of this step"))
    - Add and configure a Page display for the 1st level ([screenshot](http://dl.dropbox.com/u/25126912/CascadingSelectUsingViews/casc-select-ex-incident-07-view-config-level-1-01-overview.png "Opens incidents example screenshot of this step"))
      - *For Fields configuration see 3rd level.*
    - Add and configure an Attachment display for the 2nd level ([screenshot](http://dl.dropbox.com/u/25126912/CascadingSelectUsingViews/casc-select-ex-incident-08-view-config-level-2-01-overview.png "Opens incidents example screenshot of this step"))
      - *For Relationships, Fields, and Arguments configuration see 3rd level.*
    - Add and configure an Attachment display for the 3rd level ([screenshot](http://dl.dropbox.com/u/25126912/CascadingSelectUsingViews/casc-select-ex-incident-09-view-config-level-3-01-overview.png "Opens incidents example screenshot of this step"))
      - We use the following URL structure: `incidents/<current item id>/<level 1 id>/<level 2 id>/<level 3 id>`
      - Relationships
        - parent ([screenshot](http://dl.dropbox.com/u/25126912/CascadingSelectUsingViews/casc-select-ex-incident-09-view-config-level-3-02-relationship-parent.png "Opens incidents example screenshot of this step"))
        - grandparent ([screenshot](http://dl.dropbox.com/u/25126912/CascadingSelectUsingViews/casc-select-ex-incident-09-view-config-level-3-03-relationship-grandparent.png "Opens incidents example screenshot of this step"))
      - Fields
        - grandparent id ([screenshot](http://dl.dropbox.com/u/25126912/CascadingSelectUsingViews/casc-select-ex-incident-09-view-config-level-3-04-fields-grandparent-id.png "Opens incidents example screenshot of this step"))
        - parent id ([screenshot](http://dl.dropbox.com/u/25126912/CascadingSelectUsingViews/casc-select-ex-incident-09-view-config-level-3-05-fields-parent-id.png "Opens incidents example screenshot of this step"))
        - node id ([screenshot](http://dl.dropbox.com/u/25126912/CascadingSelectUsingViews/casc-select-ex-incident-09-view-config-level-3-06-fields-node-id.png "Opens incidents example screenshot of this step"))
        - node title ([screenshot](http://dl.dropbox.com/u/25126912/CascadingSelectUsingViews/casc-select-ex-incident-09-view-config-level-3-07-fields-node-title.png "Opens incidents example screenshot of this step"))
      - Arguments
        - Global: Null ([screenshot](http://dl.dropbox.com/u/25126912/CascadingSelectUsingViews/casc-select-ex-incident-09-view-config-level-3-08-arguments-null-current-id.png "Opens incidents example screenshot of this step"))
        - Global: Null ([screenshot](http://dl.dropbox.com/u/25126912/CascadingSelectUsingViews/casc-select-ex-incident-09-view-config-level-3-09-arguments-null-level-1.png "Opens incidents example screenshot of this step"))
        - Node id (of parent) `incidents/<current item id>/<level 1 id>/<strong><level 2 id></strong>/<level 3 id>` ([screenshot](http://dl.dropbox.com/u/25126912/CascadingSelectUsingViews/casc-select-ex-incident-09-view-config-level-3-10-arguments-parent.png "Opens incidents example screenshot of this step"))
      - Result before using modified templates: [screenshot](http://dl.dropbox.com/u/25126912/CascadingSelectUsingViews/casc-select-ex-incident-09-view-config-level-3-11-result-without-template.png "Opens incidents example screenshot of this step")
    - Modify the templates ([screenshot](http://dl.dropbox.com/u/25126912/CascadingSelectUsingViews/casc-select-ex-incident-10-view-theme-information.png "Opens incidents example screenshot of this step"))
      - Add templates to your theme's templates folder
        - *Note: For your displays' fields set all "\* HTML element" to "- None -" and exclude given fields from the display.*

        - *Note: The example files are intended for a multilingual site, adjust the templates if you use a single language.*

        - `views-view-unformatted--incident--level-3.tpl.php`  

          ``` php
          <?php 
            global $base_url;
            global $language;
            $uri_wo_lingo = substr(request_uri(),4);
            /* TODO: treat case when no language given */
          ?>
          <?php if (!empty($title)): ?>
            <h3><?php print $title; ?></h3>
          <?php endif; ?>
          <form class="views-dropdown-form">
          <select onchange="window.location='<?php print $base_url . '/' . $language->language; ?>/'+this.value">
          <option value="<?php print $uri_wo_lingo; ?>"><?php print t('Select...'); ?></option>
          <?php foreach ($rows as $id => $row): ?>
          <?php print $row; ?>
          <?php endforeach; ?>
          </select>
          </form>
          <noscript>JavaScript is disabled, please enable it to use functionality!</noscript>
                        
          ```

        - `views-view-fields--incident--level-3.tpl.php`  

          ``` php
          <?php 
          $level = 3; // adjust this to match the template
          $view_path = 'incidents/';
          $uri_relevant_part = strrev(stristr(strrev(request_uri()),strrev($view_path),TRUE)); // remove unnecessary parts from URI
          $link_relevant_part = strrev(stristr(strrev($fields['nid']->content),strrev($view_path),TRUE)); // remove unnecessary parts from link
          $uri_array = explode('/',$uri_relevant_part);
          $link_array = explode('/',$link_relevant_part);
          ?>
          <option value="<?php print $fields['nid']->content; ?>"<?php if (isset($uri_array[$level]) && ($link_array[$level] == $uri_array[$level])) print ' selected="true"'; ?>>
          <?php print $fields['title']->content; ?>
          </option>
                        
          ```
    - Add and configure an Attachment display for the solutions ([screenshot](http://dl.dropbox.com/u/25126912/CascadingSelectUsingViews/casc-select-ex-incident-11-view-config-solutions-01-overview.png "Opens incidents example screenshot of this step"))
      - Relationships
        - solutions ([screenshot](http://dl.dropbox.com/u/25126912/CascadingSelectUsingViews/casc-select-ex-incident-11-view-config-solutions-02-relationships.png "Opens incidents example screenshot of this step"))
      - Fields
        - node title ([screenshot](http://dl.dropbox.com/u/25126912/CascadingSelectUsingViews/casc-select-ex-incident-11-view-config-solutions-03-fields.png "Opens incidents example screenshot of this step"))
      - Arguments
        - Node id (of incident current item) `incidents/<strong><current item id></strong>/<level 1 id>/<level 2 id>/<level 3 id>` ([screenshot](http://dl.dropbox.com/u/25126912/CascadingSelectUsingViews/casc-select-ex-incident-11-view-config-solutions-04-arguments.png "Opens incidents example screenshot of this step"))
    - Add and configure an Attachment display for the form ([screenshot](http://dl.dropbox.com/u/25126912/CascadingSelectUsingViews/casc-select-ex-incident-12-view-config-form-01-overview.png "Opens incidents example screenshot of this step"))
      - Relationships
        - form ([screenshot](http://dl.dropbox.com/u/25126912/CascadingSelectUsingViews/casc-select-ex-incident-12-view-config-form-02-relationships.png "Opens incidents example screenshot of this step"))
      - Fields
        - webform form body ([screenshot](http://dl.dropbox.com/u/25126912/CascadingSelectUsingViews/casc-select-ex-incident-12-view-config-form-03-fields.png "Opens incidents example screenshot of this step"))
      - Arguments
        - Node id (of incident current item) `incidents/<strong><current item id></strong>/<level 1 id>/<level 2 id>/<level 3 id>` ([screenshot](http://dl.dropbox.com/u/25126912/CascadingSelectUsingViews/casc-select-ex-incident-12-view-config-form-04-arguments.png "Opens incidents example screenshot of this step"))
6.  Try it :-)
    - Select ([screenshot](http://dl.dropbox.com/u/25126912/CascadingSelectUsingViews/casc-select-ex-incident-00-1-select.png "Opens incidents example screenshot 'select'"))
    - Result ([screenshot](http://dl.dropbox.com/u/25126912/CascadingSelectUsingViews/casc-select-ex-incident-00-2-result.png "Opens incidents example screenshot 'result'"))
