---
title: "Comparison of Node/Entity Ordering Modules"
source_url: "https://www.drupal.org/docs/7/extend/comparison-of-contributed-modules/comparison-of-nodeentity-ordering-modules"
page_type: page
last_updated: "Last updated on 4 March 2026"
published: "2009-03-11T15:38:29+00:00"
modified: "2026-03-04T23:00:53+00:00"
breadcrumb: ["Drupal 7", "Extending Drupal 7", "Comparison of contributed modules"]
fetched: "2026-10-21T09:00:47Z"
raw: "raw/docs/7/extend/comparison-of-contributed-modules/comparison-of-nodeentity-ordering-modules.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Comparison of Node/Entity Ordering Modules

The standard ordering for lists of nodes and or entities in Drupal is first by the "sticky" attribute and then by the created date. Many content modules have some facility to change this ordering, but only for their content type. The modules described here attempt to provide a more controllable ordering in a variety of ways.

### Outline Designer

The Outline Designer is an enhancement to the core-optional books module packaged with Drupal. It provides a drastically improved UI as well as additional functionality that can help books be a more attractive, simple option then fully configuring other projects. This in use with projects like Menu Block can help you structure site outlines and node hierarchies rapidly. This project has been created as part of the [ELMS initiative](https://elms.psu.edu/).

For more information please see the [Outline Designer project page](/project/outline_designer).

### Weight

The Weight module uses the "sticky" attribute by altering its value to include the node's weight. This has the advantage of making the standard node ordering automatic with no further changes. The disadvantage is that modules that check the sticky attribute for 0 or 1 (FALSE or TRUE) may not work properly, although the module will decode the two values upon a full node load.

The Drupal 8 version of the module provides a weight field that can be added to any fieldable entity. The weight field can be used to provide customized sorting.

For more information please see the [Weight project page](/project/weight).

### Nodeorder

Using taxonomy, individual nodes can be classified multiple ways. See [Taxonomy: A way to organize content](http://drupal.org/handbook/modules/taxonomy) for a comprehensive description. To continue the analogy from there, Nodeorder allows you to say that "this node should appear towards the top of the list of *composers* but towards the bottom of the list of *seventeenth century*."

Upon installation, Nodeorder adds a column called weight_in_tid to the term_node table. On each Vocabulary's edit page, Nodeorder adds an "Orderable" checkbox. If this is checked, users with the correct permissions will be able to order nodes within any of the terms in that vocabulary.

For more information please see the [Nodeorder project page](/project/nodeorder).

### Nodequeue

Provides a simple UI to manually order any queue. Additionally, it allows nodes to be added and removed from queues without needing edit permissions to the node. Nodes can be added to queues either from a queue management tab or by links on the node teaser. Nodequeue provides a robust Smartqueue API so module developers can create customized queues that are specific to particular users, or to Organic Groups.

For more information please see the [Nodequeue project page](/project/nodequeue)

### Entityqueue

A rewrite of Nodequeue for Drupal 7 and Drupal 8 based on entities.

The Entityqueue module allows users to create queues of any entity type. Each queue is implemented as an Entityreference field, that can hold a single entity type. For instance you can create a queue of:

- Nodes
- Users
- Taxonomy terms

Entityqueue provides Views integration, by adding an Entityqueue relationship to your view, and adding a sort for Entityqueue position.

For more information please see the [Entityqueue project page](/project/entityqueue).

### DraggableViews

Rows of a table or an HTML list can be moved via drag-and-drop to build hierarchical structures. Child nodes of parents can be hidden via javascript .

The default implementation uses a database table to save the information.

For more information please see the [DraggableViews project page](/project/draggableviews).

### Flag Weights

**This module has very few users.**

Flag Weights module is an add-on to the excellent [Flag module](/project/flag), that adds the ability to set a weight against each flagged item. The module does not provide any UI as such, other than integrating with the [Draggable Views](/project/draggableviews) module to allow drag-and-drop reordering or flagged content. This might be used for prioritizing a wish list, etc.

For more information please see the [Flag Weights project page](/project/flag_weights).

### Sortable Grid Views Plugin

**This module is no longer supported.**

Provides a simple UI to manually order any grid styled view where items can be moved via drag-and-drop. Sortable Grid Views Plugin is very similar in its goals to Draggable views, yet a lot simpler as there is no hierarchy management. It doesn't depend on Draggable Views though.

For more information please see the [Sortable Grid Views Plugin project page](/project/sgrid).

### JQGRID - View integration

**This module has very few users.**

This module provides views integration for the jqGRid jQuery plugin, which provides advanced interaction controls to HTML tables such as dynamic pagination, on-the-fly filtering, and column sorting and inline editing.

This module also support AJAX to handle very large tables.

For more information please see the [JQGRID - View integration project page](/project/jqgrid).

### Nodeflow

**This module is seeking new maintainers.**

This module provides:

1.  Birds-eye view of all nodes published on your front page and all nodes waiting to be published giving editors complete control
2.  Drag and drop interface to sort nodes
3.  Drag and drop interface between tables to quickly publish nodes
4.  Locking selected nodes into selected positions
5.  Schedule nodes to be published in the future within the same interface.
6.  Shows all users currently online on the page.

For more information please see the [Nodeflow project page](/project/nodeflow).

**Scroll down for a table comparing some of the modules (added blank space because the table was covered by the Site Building Guide block/menu on the right).**

## Drupal-related comparison

<table style="width:100%;" data-border="1">
<colgroup>
<col style="width: 14%" />
<col style="width: 14%" />
<col style="width: 14%" />
<col style="width: 14%" />
<col style="width: 14%" />
<col style="width: 14%" />
<col style="width: 14%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Feature</td>
<td><a href="/project/outline_designer">Outline Designer</a></td>
<td><a href="/project/weight">Weight</a></td>
<td><a href="/project/nodeorder">Nodeorder</a></td>
<td><a href="/project/nodequeue">Nodequeue</a></td>
<td><a href="/project/entityqueue">Entityqueue</a></td>
<td><a href="/project/draggableviews">DraggableViews</a></td>
</tr>
<tr class="even">
<td>Drupal 8.x</td>
<td><img src="/misc/watchdog-error.png" /></td>
<td><img src="/misc/watchdog-ok.png" /></td>
<td>beta</td>
<td><img src="/misc/watchdog-error.png" /></td>
<td><img src="/misc/watchdog-ok.png" /></td>
<td><img src="/misc/watchdog-ok.png" /></td>
</tr>
<tr class="odd">
<td>Drupal 7.x</td>
<td><img src="/misc/watchdog-ok.png" /></td>
<td><img src="/misc/watchdog-ok.png" /></td>
<td><img src="/misc/watchdog-ok.png" /></td>
<td><img src="/misc/watchdog-ok.png" /></td>
<td><img src="/misc/watchdog-ok.png" /></td>
<td><img src="/misc/watchdog-ok.png" /></td>
</tr>
<tr class="even">
<td>Drupal 6.x</td>
<td><img src="/misc/watchdog-ok.png" /></td>
<td><img src="/misc/watchdog-ok.png" /></td>
<td><img src="/misc/watchdog-ok.png" /></td>
<td><img src="/misc/watchdog-ok.png" /></td>
<td><img src="/misc/watchdog-error.png" /></td>
<td><img src="/misc/watchdog-ok.png" /></td>
</tr>
<tr class="odd">
<td>Last official release (as of July 2018)</td>
<td>2016-Jun-07</td>
<td>2015-Dec-09</td>
<td>2018-May-02</td>
<td>2016-Jun-14</td>
<td>2018-Mar-09</td>
<td>2016-Oct-21</td>
</tr>
<tr class="even">
<td>Usage (as of July 2018)</td>
<td><a href="/project/usage/outline_designer">~1000</a></td>
<td><a href="/project/usage/weight">~46000</a></td>
<td><a href="/project/usage/nodeorder">~4100</a></td>
<td><a href="/project/usage/nodequeue">~42000</a></td>
<td><a href="/project/usage/entityqueue">~12000</a></td>
<td><a href="/project/usage/draggableviews">~61000</a></td>
</tr>
<tr class="odd">
<td>Documentation</td>
<td><a href="http://drupal.org/node/275286">Handbook</a></td>
<td><a href="http://drupal.org/node/307797">Handbook</a></td>
<td>README.txt</td>
<td><a href="http://drupal.org/node/293117">Handbook</a></td>
<td>No - or see nodequeue</td>
<td><a href="http://drupal.org/node/283498">Handbook</a></td>
</tr>
<tr class="even">
<td>Demonstration</td>
<td><a href="https://www.youtube.com/watch?v=WMXlawXG3l0">Video</a></td>
<td>No</td>
<td>No</td>
<td><a href="https://www.youtube.com/watch?v=s3oCr5iWeTc">Video</a></td>
<td>No</td>
<td><a href="https://www.youtube.com/watch?v=pxetnlKzZBE">Video (D7)</a><br />
<a href="https://www.youtube.com/watch?v=F_Hy0NrGAo0">Video (D8)</a></td>
</tr>
<tr class="odd">
<td>Architecture</td>
<td>Upgrades Book outline interface</td>
<td>Sticky-encoding</td>
<td>Adds a field to term_node table</td>
<td>?</td>
<td>?</td>
<td>Views style plugin</td>
</tr>
<tr class="even">
<td>Additional database tables</td>
<td>0 - purely usability / functionality upgrade</td>
<td>2 - weight_settings &amp; weight_weights</td>
<td>0 - adds a field to term_node table</td>
<td>Yes</td>
<td>Yes</td>
<td>1 - used for none FieldAPI implemenation</td>
</tr>
</tbody>
</table>

## Services provided

|                                    |                                                                                        |                                                                                        |                                 |                                                                                                                                |                                                                                                                                |                                           |
|------------------------------------|----------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|---------------------------------|--------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------|
| Feature                            | [Outline Designer](/project/outline_designer)                                          | [Weight](/project/weight)                                                              | [Nodeorder](/project/nodeorder) | [Nodequeue](/project/nodequeue)                                                                                                | [Entityqueue](/project/entityqueue)                                                                                            | [DraggableViews](/project/draggableviews) |
| Reordering page                    | Drag and drop, duplication of book outlines, AJAX version of book module, context menu | Uses core node admin page / Drag and drop                                              | Drag and drop                   | Drag and drop                                                                                                                  | Drag and drop                                                                                                                  | Any view                                  |
| Feature blocks                     | Inherited from book module                                                             | N/A                                                                                    | None                            |                                                                                                                                |                                                                                                                                | Inherited from views                      |
| Supports Managing Translated Nodes | ?                                                                                      | ?                                                                                      | ?                               | Yes, either by tying translations to the original or by ignoring translations and letting admins manage them as separate nodes | Yes, either by tying translations to the original or by ignoring translations and letting admins manage them as separate nodes | ?                                         |
| Security                           | Drupal core-optional books module                                                      | Drupal core, 'assign node weight', 'administer nodes', 'administer site configuration' | Drupal core                     | Separates permissions for ordering nodes from editing them                                                                     | Separates permissions for ordering nodes from editing them                                                                     | Views permission, plus 'Allow Reordering' |
| Settings                           | Yes                                                                                    | Yes                                                                                    | Yes                             | Yes                                                                                                                            | Yes                                                                                                                            | Yes                                       |
| Views support                      | ![](/misc/watchdog-ok.png)                                                             | ![](/misc/watchdog-ok.png)                                                             | ![](/misc/watchdog-ok.png)      | ![](/misc/watchdog-ok.png)                                                                                                     | ![](/misc/watchdog-ok.png)                                                                                                     | ![](/misc/watchdog-ok.png)                |
| Translation template supplied      | ![](/misc/watchdog-error.png)                                                          | ![](/misc/watchdog-ok.png)                                                             | ![](/misc/watchdog-error.png)   | ![](/misc/watchdog-ok.png)                                                                                                     | ![](/misc/watchdog-ok.png)                                                                                                     | ![](/misc/watchdog-error.png)             |
