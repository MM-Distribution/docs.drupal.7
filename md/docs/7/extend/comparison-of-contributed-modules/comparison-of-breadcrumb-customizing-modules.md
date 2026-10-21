---
title: "Comparison of Breadcrumb customizing modules"
source_url: "https://www.drupal.org/docs/7/extend/comparison-of-contributed-modules/comparison-of-breadcrumb-customizing-modules"
page_type: page
last_updated: "Last updated on 30 April 2025"
published: "2009-07-28T15:16:09+00:00"
modified: "2025-04-30T20:53:04+00:00"
breadcrumb: ["Drupal 7", "Extending Drupal 7", "Comparison of contributed modules"]
fetched: "2026-10-21T08:57:26Z"
raw: "raw/docs/7/extend/comparison-of-contributed-modules/comparison-of-breadcrumb-customizing-modules.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Comparison of Breadcrumb customizing modules

## Modules that influence the generation of a breadcrumb trail

Comparison of modules that customize the breadcrumb and make nodes and other content appear to be under a chosen menu item:

[Hansel](/project/hansel) (7.x)    
Hansel provides custom breadcrumbs which are build by user defined rules. These rules are independent from the menu system. Rules can have logic switches and can add links to the breadcrumbs.  

[Node Breadcrumb](/project/node_breadcrumb) (7.x)    
Allows you to create rules which indicate menu location of nodes (and the breadcrumb), either with the admin UI, or with PHP code.  

[Taxonomy Breadcrumb](/project/taxonomy_breadcrumb) (7.x, 8.x)    
Automatically add term links (taxonomy/term/tid) to breadcrumb of nodes  

[Custom Breadcrumbs](/project/custom_breadcrumbs) (7.x, 8.x, 9.x)    
Customization only for entire content types, manual enter of breadcrumb links  

[Menu Breadcrumb](/project/menu_breadcrumb) (7.x, 8.x, 9.x)    
Use your site's menu(s) to generate breadcrumbs.

[Menu Trails](/project/menutrails) (not maintained)    
Customization by content types and taxonomy terms. This module's main function is to implement primary/secondary links which keep the current menu trail "active" or highlighted.  

[Crumbs](/project/crumbs) (7.x)    
Builds a breadcrumb trail by finding the parent of the current page, then the parent of the parent, etc, until it arrives at the home page. Each step is based on a series of user-prioritized plugins representing menu hierarchy, taxonomy, system path, alias, pathauto rules, nodereference fields, custom token paths per entity bundle, and additional rules that can be defined in custom modules.  

[Menu position](/project/menu_position) (7.x, 8.x)    
Allows for the creation of rules that will dynamically add the current page into the menu system (and thus breadcrumbs) at the requested spots. Currently, the Menu position module provides "content type", "pages", "taxonomy", "vocabulary" and "language" plug-ins that allows conditions to be added to rules.  

[Breadcrumbs by path](/project/breadcrumbs_by_path) (7.x)    
Breadcrumbs by path uses the current URL (path alias) and the current page's title to automatically extract the breadcrumb's segments and its respective links  

[Easy Breadcrumb](/project/easy_breadcrumb) (7.x, 8.x)    
Easy Breadcrumb uses the current URL (path alias) and the current page's title to automatically extract the breadcrumb's segments and its respective links  

[Path Breadcrumbs](/project/path_breadcrumbs) (7.x)    
Path Breadcrumbs module helps you to create breadcrumbs for **any page**  
with any selection rules and load any entity from the URL.  

## Modules that add functionality to an existing breadcrumb

[Crumbdown](/project/crumbdown)    
Adds dropdown submenus to some breadcrumb items. Depends on Crumbs. Currently not actively developed. D6 only.  

 

 

**Check the comparison tables below (moved, so sidebar doesn't clobber).**

 

↓

↓

 

 

 

 

 

 

 

 

 

 

 

↓

 

 

 

 

 

 

 

 

↓

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

↓

 

 

**Comparison table for Drupal 7.x and above.**  

 

<table height="1252" width="936">
<colgroup>
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 9%" />
</colgroup>
<thead>
<tr class="header">
<th>Feature</th>
<th style="text-align: center;"><a href="http://drupal.org/project/custom_breadcrumbs"><em>Custom Breadcrumbs</em></a></th>
<th style="text-align: center;"><a href="http://drupal.org/project/menu_breadcrumb"><em>Menu Breadcrumb</em></a></th>
<th style="text-align: center;"><a href="https://drupal.org/project/path_breadcrumbs"><em>Path Breadcrumbs</em></a></th>
<th style="text-align: center;"><a href="http://drupal.org/project/popup"><em>Popup</em></a></th>
<th style="text-align: center;"><a href="http://drupal.org/project/clickpath"><em>Clickpath</em></a></th>
<th style="text-align: center;"><a href="http://drupal.org/project/hansel"><em>Hansel</em></a></th>
<th style="text-align: center;"><a href="http://drupal.org/project/crumbs"><em>Crumbs</em></a></th>
<th data-valign="top"></th>
<th style="text-align: center;"><a href="http://drupal.org/project/breadcrumb"><em>Breadcrumb</em></a></th>
<th style="text-align: center;"><a href="http://drupal.org/project/menu_position"><em>Menu position</em></a></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="11"><em><strong>Drupal-related</strong></em></td>
</tr>
<tr class="even">
<td>Drupal 8.x</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">-</td>
<td data-valign="top"></td>
<td style="text-align: center;"><a href="http://drupal.org/node/481564">Planned</a></td>
<td></td>
</tr>
<tr class="odd">
<td><strong>Drupal 7.x</strong></td>
<td style="text-align: center;"><img src="/misc/watchdog-ok.png" /></td>
<td style="text-align: center;"><img src="/misc/watchdog-ok.png" /></td>
<td style="text-align: center;"><img src="/misc/watchdog-ok.png" /></td>
<td style="text-align: center;"><img src="/misc/watchdog-ok.png" /></td>
<td style="text-align: center;"><img src="/misc/watchdog-ok.png" /></td>
<td style="text-align: center;"><img src="/misc/watchdog-ok.png" /></td>
<td style="text-align: center;"><img src="/misc/watchdog-ok.png" /></td>
<td data-valign="top"></td>
<td style="text-align: center;"> <img src="/misc/watchdog-error.png" /></td>
<td style="text-align: center;"><img src="/misc/watchdog-ok.png" /></td>
</tr>
<tr class="even">
<td><strong>Drupal 6.x</strong></td>
<td style="text-align: center;"><img src="/misc/watchdog-ok.png" /></td>
<td style="text-align: center;"><img src="/misc/watchdog-ok.png" /></td>
<td style="text-align: center;">-</td>
<td style="text-align: center;"><img src="/misc/watchdog-ok.png" /></td>
<td style="text-align: center;"><img src="/misc/watchdog-ok.png" /></td>
<td style="text-align: center;"><img src="/misc/watchdog-ok.png" /></td>
<td style="text-align: center;">"unstable"</td>
<td data-valign="top"></td>
<td style="text-align: center;"> <img src="/misc/watchdog-error.png" /></td>
<td style="text-align: center;"><img src="/misc/watchdog-error.png" /></td>
</tr>
<tr class="odd">
<td>Drupal 5.x</td>
<td style="text-align: center;"><img src="/misc/watchdog-ok.png" /></td>
<td style="text-align: center;"><img src="/misc/watchdog-error.png" /></td>
<td style="text-align: center;">-</td>
<td style="text-align: center;"><img src="/misc/watchdog-error.png" /></td>
<td style="text-align: center;"><img src="/misc/watchdog-error.png" /></td>
<td style="text-align: center;"><img src="/misc/watchdog-error.png" /></td>
<td style="text-align: center;"><img src="/misc/watchdog-error.png" /></td>
<td data-valign="top"></td>
<td style="text-align: center;"> <img src="/misc/watchdog-error.png" /></td>
<td style="text-align: center;"><img src="/misc/watchdog-error.png" /></td>
</tr>
<tr class="even">
<td>Usage</td>
<td style="text-align: center;">&gt;49k</td>
<td style="text-align: center;">&gt;40k</td>
<td style="text-align: center;">&gt;13k</td>
<td style="text-align: center;">&gt;7k</td>
<td style="text-align: center;">&lt;300</td>
<td style="text-align: center;">&gt;1k</td>
<td style="text-align: center;">&gt;15k</td>
<td data-valign="top"></td>
<td style="text-align: center;">&lt;600</td>
<td style="text-align: center;">&gt;23k</td>
</tr>
<tr class="odd">
<td><strong><a href="#fn-lastupdate" id="ln-lastupdate">*</a></strong>Last update</td>
<td style="text-align: center;"><p>September 9,<br />
<br />
2014</p></td>
<td style="text-align: center;">October 8,<br />
<br />
2013</td>
<td style="text-align: center;">June 24,<br />
<br />
2014</td>
<td style="text-align: center;">July 6, 2014</td>
<td style="text-align: center;">April 4, 2010</td>
<td style="text-align: center;">October 30, 2014</td>
<td style="text-align: center;">October 2,<br />
<br />
2014</td>
<td data-valign="top"></td>
<td style="text-align: center;">February 24, 2011</td>
<td style="text-align: center;">February 22,<br />
<br />
2012</td>
</tr>
<tr class="even">
<td>Documentation / README</td>
<td style="text-align: center;"><a href="http://drupalcode.org/project/custom_breadcrumbs.git/blob_plain/refs/heads/6.x-2.x:/README.txt"><strong>Readme</strong></a></td>
<td style="text-align: center;"> </td>
<td style="text-align: center;"><a href="https://drupal.org/node/2061939">FAQ</a>,<br />
<br />
<a href="http://codekarate.com/daily-dose-of-drupal/drupal-7-path-breadcrumbs-module">Video</a></td>
<td style="text-align: center;"><a href="http://drupal.org/node/842100">Page</a></td>
<td style="text-align: center;"> </td>
<td style="text-align: center;"> </td>
<td style="text-align: center;"><a href="http://drupal.org/node/1004394">Doc</a></td>
<td data-valign="top"></td>
<td style="text-align: center;"> </td>
<td style="text-align: center;"> </td>
</tr>
<tr class="odd">
<td>Demo / screenshot</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;"><a href="http://drupal.org/files/images/menu_breadcrumb_screenshot_crop.png"><strong>settings screen</strong></a></td>
<td style="text-align: center;"><a href="http://codekarate.com/daily-dose-of-drupal/drupal-7-path-breadcrumbs-module">Video</a>,<br />
<br />
<a href="https://drupal.org/project/path_breadcrumbs">screenshots</a></td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;"><a href="http://www.flickr.com/photos/bertboerland/sets/72157623924447201/">screenshots</a></td>
<td style="text-align: center;">-</td>
<td data-valign="top"></td>
<td style="text-align: center;"> </td>
<td style="text-align: center;"><a href="http://drupal.org/files/images/menu_position_0.png">screenshot</a></td>
</tr>
<tr class="even">
<td colspan="11"><em><strong>Functionality</strong></em></td>
</tr>
<tr class="odd">
<td>API, Hooks, classes available</td>
<td style="text-align: center;"> </td>
<td style="text-align: center;"> </td>
<td style="text-align: center;"><a href="http://drupalcode.org/project/path_breadcrumbs.git/blob/refs/heads/7.x-3.x:/path_breadcrumbs.api.php">API</a>,<br />
<br />
<a href="https://drupal.org/project/path_breadcrumbs">CTools Plugins</a></td>
<td style="text-align: center;"> </td>
<td style="text-align: center;"> </td>
<td style="text-align: center;"><a href="http://drupal.org/project/hansel">Yes</a></td>
<td style="text-align: center;"><a href="http://drupal.org/project/crumbs">Plugins</a></td>
<td data-valign="top"></td>
<td style="text-align: center;"> </td>
<td style="text-align: center;"><img src="/misc/watchdog-ok.png" /></td>
</tr>
<tr class="even">
<td>User defined rules</td>
<td style="text-align: center;"><img src="/misc/watchdog-ok.png" /></td>
<td style="text-align: center;"><img src="/misc/watchdog-ok.png" /></td>
<td style="text-align: center;"><img src="/misc/watchdog-ok.png" /></td>
<td style="text-align: center;">?</td>
<td style="text-align: center;">?</td>
<td style="text-align: center;">?</td>
<td style="text-align: center;"> <img src="/misc/watchdog-ok.png" /></td>
<td data-valign="top"></td>
<td style="text-align: center;">?</td>
<td style="text-align: center;"><img src="/misc/watchdog-ok.png" /></td>
</tr>
<tr class="odd">
<td> Admin UI</td>
<td style="text-align: center;"><img src="/misc/watchdog-ok.png" /></td>
<td style="text-align: center;"> </td>
<td style="text-align: center;"><img src="/misc/watchdog-ok.png" /></td>
<td style="text-align: center;"> </td>
<td style="text-align: center;"> </td>
<td style="text-align: center;"> </td>
<td style="text-align: center;"> <img src="/misc/watchdog-ok.png" /></td>
<td data-valign="top"></td>
<td style="text-align: center;"> </td>
<td style="text-align: center;"><img src="/misc/watchdog-ok.png" /></td>
</tr>
<tr class="even">
<td>Token support</td>
<td style="text-align: center;"><img src="/misc/watchdog-ok.png" /></td>
<td style="text-align: center;"> <img src="/misc/watchdog-ok.png" /></td>
<td style="text-align: center;"><img src="/misc/watchdog-ok.png" /></td>
<td style="text-align: center;"><img src="/misc/watchdog-error.png" /></td>
<td style="text-align: center;"><img src="/misc/watchdog-error.png" /></td>
<td style="text-align: center;"><img src="/misc/watchdog-ok.png" /></td>
<td style="text-align: center;"> <img src="/misc/watchdog-ok.png" /></td>
<td data-valign="top"></td>
<td style="text-align: center;"> <img src="/misc/watchdog-error.png" /></td>
<td style="text-align: center;"><img src="/misc/watchdog-error.png" /></td>
</tr>
<tr class="odd">
<td>Additional database tables</td>
<td style="text-align: center;"> </td>
<td style="text-align: center;"> </td>
<td style="text-align: center;"> </td>
<td style="text-align: center;"> </td>
<td style="text-align: center;"> </td>
<td style="text-align: center;"> </td>
<td style="text-align: center;"> </td>
<td data-valign="top"></td>
<td style="text-align: center;"> </td>
<td></td>
</tr>
<tr class="even">
<td colspan="10"><em><strong>Breadcrumbs based on ...</strong></em></td>
<td></td>
</tr>
<tr class="odd">
<td>Menu hierarchy</td>
<td style="text-align: center;">?</td>
<td style="text-align: center;"> <img src="/misc/watchdog-ok.png" /></td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">?</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">?</td>
<td style="text-align: center;"> <img src="/misc/watchdog-ok.png" /></td>
<td data-valign="top"></td>
<td style="text-align: center;">?</td>
<td style="text-align: center;">?</td>
</tr>
<tr class="even">
<td>Taxonomy</td>
<td style="text-align: center;">?</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;"><img src="/misc/watchdog-ok.png" /></td>
<td style="text-align: center;">?</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">?</td>
<td style="text-align: center;"> <img src="/misc/watchdog-ok.png" /></td>
<td data-valign="top"></td>
<td style="text-align: center;">?</td>
<td style="text-align: center;">?</td>
</tr>
<tr class="odd">
<td>Path alias</td>
<td style="text-align: center;">?</td>
<td style="text-align: center;">?</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">?</td>
<td style="text-align: center;">?</td>
<td style="text-align: center;">?</td>
<td style="text-align: center;"> <img src="/misc/watchdog-ok.png" /></td>
<td data-valign="top"></td>
<td style="text-align: center;">?</td>
<td style="text-align: center;">?</td>
</tr>
<tr class="even">
<td>Node reference / entity reference</td>
<td style="text-align: center;">?</td>
<td style="text-align: center;">?</td>
<td style="text-align: center;"><img src="/misc/watchdog-ok.png" /></td>
<td style="text-align: center;">?</td>
<td style="text-align: center;">?</td>
<td style="text-align: center;">?</td>
<td style="text-align: center;"> <img src="/misc/watchdog-ok.png" /></td>
<td data-valign="top"></td>
<td style="text-align: center;">?</td>
<td style="text-align: center;">?</td>
</tr>
<tr class="odd">
<td>Organic groups</td>
<td style="text-align: center;">?</td>
<td style="text-align: center;">?</td>
<td style="text-align: center;"><img src="/misc/watchdog-ok.png" /></td>
<td style="text-align: center;">?</td>
<td style="text-align: center;">?</td>
<td style="text-align: center;">?</td>
<td style="text-align: center;"> <img src="/misc/watchdog-ok.png" /></td>
<td data-valign="top"></td>
<td style="text-align: center;">?</td>
<td style="text-align: center;">?</td>
</tr>
<tr class="even">
<td>Click history</td>
<td style="text-align: center;">?</td>
<td style="text-align: center;">?</td>
<td style="text-align: center;">?</td>
<td style="text-align: center;">?</td>
<td style="text-align: center;"> <img src="/misc/watchdog-ok.png" /></td>
<td style="text-align: center;">?</td>
<td style="text-align: center;"><img src="/misc/watchdog-error.png" /></td>
<td data-valign="top"></td>
<td style="text-align: center;">?</td>
<td style="text-align: center;">?</td>
</tr>
<tr class="odd">
<td>Admin defined rules</td>
<td style="text-align: center;">?</td>
<td style="text-align: center;">?</td>
<td style="text-align: center;"> <img src="/misc/watchdog-ok.png" /></td>
<td style="text-align: center;">?</td>
<td style="text-align: center;">?</td>
<td style="text-align: center;"> <img src="/misc/watchdog-ok.png" /></td>
<td style="text-align: center;"> <img src="/misc/watchdog-ok.png" /></td>
<td data-valign="top"></td>
<td style="text-align: center;">?</td>
<td style="text-align: center;"> <img src="/misc/watchdog-ok.png" /></td>
</tr>
<tr class="even">
<td>Code-defined rules</td>
<td style="text-align: center;">?</td>
<td style="text-align: center;">?</td>
<td style="text-align: center;"> <img src="/misc/watchdog-ok.png" /></td>
<td style="text-align: center;">?</td>
<td style="text-align: center;">?</td>
<td style="text-align: center;">?</td>
<td style="text-align: center;"> <img src="/misc/watchdog-ok.png" /></td>
<td data-valign="top"></td>
<td style="text-align: center;">?</td>
<td style="text-align: center;">?</td>
</tr>
<tr class="odd">
<td>Prioritization of rules</td>
<td style="text-align: center;">?</td>
<td style="text-align: center;">?</td>
<td style="text-align: center;"> <img src="/misc/watchdog-ok.png" /></td>
<td style="text-align: center;">?</td>
<td style="text-align: center;">?</td>
<td style="text-align: center;">?</td>
<td style="text-align: center;">fine-grained hierarchical prioritization with wildcards via admin weights UI</td>
<td data-valign="top"><br />
<br />
</td>
<td style="text-align: center;">?</td>
<td style="text-align: center;">?</td>
</tr>
<tr class="even">
<td><em><strong>Notes</strong></em></td>
<td style="text-align: center;"> </td>
<td style="text-align: center;"> </td>
<td style="text-align: center;">Page Manager friendly UI. Ctools based. Cacheable.</td>
<td style="text-align: center;"> </td>
<td style="text-align: center;"> </td>
<td style="text-align: center;"> </td>
<td style="text-align: center;"> </td>
<td data-valign="top"><br />
<br />
</td>
<td style="text-align: center;">See: <a href="http://drupal.org/node/481564">#481564</a></td>
<td style="text-align: center;"><p>Makes you breadcrumbs and menus consistent.</p>
<p>Due to the usage of the menu system it’s less flexible than other modules.</p></td>
</tr>
</tbody>
</table>

**<a href="#ln-lastupdate" id="fn-lastupdate">*</a>Note:** The most recent update to **any** of these modules' "Last update" dates was [December 16, 2014](https://drupal.org/node/533448/revisions/2630504/view).

 

**Comparison table for Drupal 6.x and below.**  

| Feature                                           | [*Menu Trails*](http://drupal.org/project/menutrails)                                                | [*Taxonomy Breadcrumb*](http://drupal.org/project/taxonomy_breadcrumb) | [*Node Hierarchy*](http://drupal.org/project/nodehierarchy) | [*Node breadcrumb*](http://drupal.org/project/node_breadcrumb)                                                                 | [*TrailScout*](http://drupal.org/project/trailscout) |     |
|---------------------------------------------------|------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------|-------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------|-----|
| ***Drupal-related***                              |                                                                                                      |                                                                        |                                                             |                                                                                                                                |                                                      |     |
| Drupal 8.x                                        | \-                                                                                                   | ![](/misc/watchdog-error.png)                                          | \-                                                          | \-                                                                                                                             | \-                                                   |     |
| **Drupal 7.x**                                    | ![](/misc/watchdog-error.png)                                                                        | ![](/misc/watchdog-error.png)                                          | ![](/misc/watchdog-error.png)                               | ![](/misc/watchdog-error.png)                                                                                                  | ![](/misc/watchdog-error.png)                        |     |
| **Drupal 6.x**                                    | ![](/misc/watchdog-ok.png)                                                                           | ![](/misc/watchdog-ok.png)                                             | ![](/misc/watchdog-ok.png)                                  | ![](/misc/watchdog-ok.png)                                                                                                     | ![](/misc/watchdog-error.png)                        |     |
| Drupal 5.x                                        | ![](/misc/watchdog-ok.png)                                                                           | ![](/misc/watchdog-ok.png)                                             | ![](/misc/watchdog-ok.png)                                  | ![](/misc/watchdog-ok.png)                                                                                                     | ![](/misc/watchdog-ok.png)                           |     |
| Usage                                             | \>8k                                                                                                 | \>7k                                                                   | \>4k                                                        | \<1k                                                                                                                           | \<100                                                |     |
| **<span id="ln-lastupdate">\*</span>**Last update | March 16, 2010                                                                                       | April 16, 2010                                                         | June 13, 2013                                               | December 10, 2014                                                                                                              | September 26, 2014                                   |     |
| Documentation / README                            | [**Readme**](http://drupalcode.org/project/menutrails.git/blob_plain/refs/heads/6.x-1.x:/README.TXT) |                                                                        | [Page](http://drupal.org/node/302253)                       |                                                                                                                                | [Desc](http://vacilando.net/ts)                      |     |
| Demo / screenshot                                 | [**screenshots**](http://chapterthreellc.com/node/72)                                                | \-                                                                     | \-                                                          | [screenshots](http://drupalcode.org/project/node_breadcrumb.git/blob_plain/refs/heads/6.x-1.x:/screenshot_node_breadcrumb.png) | [demo](http://www.vacilando.eu/ts)                   |     |
| ***Functionality***                               |                                                                                                      |                                                                        |                                                             |                                                                                                                                |                                                      |     |
| API, Hooks, classes available                     |                                                                                                      |                                                                        |                                                             |                                                                                                                                |                                                      |     |
| User defined rules                                | ?                                                                                                    | ?                                                                      | ?                                                           | ![](/misc/watchdog-ok.png)                                                                                                     | ?                                                    |     |
|  Admin UI                                         |                                                                                                      |                                                                        |                                                             | ![](/misc/watchdog-ok.png)                                                                                                     |                                                      |     |
| Token support                                     | ![](/misc/watchdog-ok.png)                                                                           | [No](http://drupal.org/node/411642)                                    |  ![](/misc/watchdog-ok.png)                                 |  ![](/misc/watchdog-error.png)                                                                                                 | ![](/misc/watchdog-error.png)                        |     |
| Additional database tables                        |                                                                                                      |                                                                        |                                                             |                                                                                                                                |                                                      |     |
| ***Breadcrumbs based on ...***                    |                                                                                                      |                                                                        |                                                             |                                                                                                                                |                                                      |     |
| Menu hierarchy                                    | \-                                                                                                   | \-                                                                     | \-                                                          | ?                                                                                                                              | ?                                                    |     |
| Taxonomy                                          | \-                                                                                                   |  ![](/misc/watchdog-ok.png)                                            | ?                                                           | ?                                                                                                                              | ?                                                    |     |
| Path alias                                        | ?                                                                                                    | ?                                                                      | ?                                                           | ?                                                                                                                              | ?                                                    |     |
| Node reference / entity reference                 | ?                                                                                                    | ?                                                                      | ?                                                           | ?                                                                                                                              | ?                                                    |     |
| Organic groups                                    | ?                                                                                                    | ?                                                                      | ?                                                           | ?                                                                                                                              | ?                                                    |     |
| Click history                                     | ?                                                                                                    | ?                                                                      | ?                                                           | ?                                                                                                                              | ?                                                    |     |
| Admin defined rules                               | ?                                                                                                    | ?                                                                      | ?                                                           | ?                                                                                                                              | ?                                                    |     |
| Code-defined rules                                | ?                                                                                                    | ?                                                                      | ?                                                           | ?                                                                                                                              | ?                                                    |     |
| Prioritization of rules                           | ?                                                                                                    | ?                                                                      | ?                                                           | ?                                                                                                                              | ?                                                    |     |
| ***Notes***                                       |                                                                                                      |                                                                        |                                                             |                                                                                                                                |                                                      |     |

**<span id="fn-lastupdate">\*</span>Note:** The most recent update to **any** of these modules' "Last update" dates was [December 16, 2014](https://drupal.org/node/533448/revisions/2630504/view).

Suggested web-browser add-ons to easier edit above tables: [Xinha](https://code.google.com/p/xinha/), [Write Area](https://addons.mozilla.org/en-US/firefox/addon/write-area/).

See also: [Comparison of Breadcrumb Modules](https://groups.drupal.org/node/79839) in the [Similar Module Review](https://groups.drupal.org/similar-module-review) Drupal group.
