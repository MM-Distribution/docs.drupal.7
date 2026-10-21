---
title: "Comparison of CCK/Taxonomy Modules"
source_url: "https://www.drupal.org/docs/7/extend/comparison-of-contributed-modules/comparison-of-ccktaxonomy-modules"
page_type: page
last_updated: "Last updated on 30 April 2025"
published: "2008-01-22T07:57:50+00:00"
modified: "2025-04-30T20:53:04+00:00"
breadcrumb: ["Drupal 7", "Extending Drupal 7", "Comparison of contributed modules"]
fetched: "2026-10-21T08:57:41Z"
raw: "raw/docs/7/extend/comparison-of-contributed-modules/comparison-of-ccktaxonomy-modules.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Comparison of CCK/Taxonomy Modules

"[There is more than one way to do it](http://en.wikipedia.org/wiki/There_is_more_than_one_way_to_do_it)™." This philosophy isn’t limited to Perl; it generally extends to open source software itself. Likewise, there are four modules that are intended to integrate taxonomy fields into the Content Construction Kit (CCK) for Drupal; these modules have been identified to have similar or overlapping functionality. Below is a list of the 4 modules.

<table data-border="1">
<colgroup>
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr class="header">
<th>Name / Project link</th>
<th style="text-align: center;">Jump</th>
<th>5.x</th>
<th>6.x</th>
<th>7.x</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><a href="http://drupal.org/project/taxonomy_super_select">Taxonomy Super Select</a></td>
<td style="text-align: center;"><a href="#tss"><img src="/misc/watchdog-error.png" title="Only local images are allowed." data-orig-src="http://nanwich.info/files/lullacons/lullacons_pack1/arrow-single-right-green.png" alt="Only local images are allowed." /></a></td>
<td><img src="/misc/watchdog-ok.png" /></td>
<td><img src="/misc/watchdog-ok.png" /></td>
<td><img src="/misc/watchdog-error.png" /></td>
</tr>
<tr class="even">
<td><a href="http://drupal.org/project/content_taxonomy">Content Taxonomy</a><br />
<em>No further development</em></td>
<td style="text-align: center;"><a href="#content_tax"><img src="/misc/watchdog-error.png" title="Only local images are allowed." data-orig-src="http://nanwich.info/files/lullacons/lullacons_pack1/arrow-single-right-green.png" alt="Only local images are allowed." /></a></td>
<td><img src="/misc/watchdog-ok.png" /></td>
<td><img src="/misc/watchdog-ok.png" /></td>
<td><img src="/misc/watchdog-ok.png" /></td>
</tr>
<tr class="odd">
<td><a href="http://drupal.org/project/cck_taxonomy">CCK Taxonomy Fields</a><br />
<em>currently abandoned</em></td>
<td style="text-align: center;"><a href="#cck_tax"><img src="/misc/watchdog-error.png" title="Only local images are allowed." data-orig-src="http://nanwich.info/files/lullacons/lullacons_pack1/arrow-single-right-green.png" alt="Only local images are allowed." /></a></td>
<td><img src="/misc/watchdog-ok.png" /></td>
<td><img src="/misc/watchdog-error.png" /></td>
<td><img src="/misc/watchdog-error.png" /></td>
</tr>
<tr class="even">
<td><a href="http://drupal.org/project/cck_taxonomy_ssu">CCK Taxonomy Super Select Ultra</a></td>
<td style="text-align: center;"><a href="#tss_ultra"><img src="/misc/watchdog-error.png" title="Only local images are allowed." data-orig-src="http://nanwich.info/files/lullacons/lullacons_pack1/arrow-single-right-green.png" alt="Only local images are allowed." /></a></td>
<td><img src="/misc/watchdog-ok.png" /></td>
<td><img src="/misc/watchdog-error.png" /></td>
<td><img src="/misc/watchdog-error.png" /></td>
</tr>
</tbody>
</table>

This document serves to compare and contrast these modules in order to make it easier for site owners to choose one to suit their site development needs. The following issues are addressed for each module:

- ease of installation and ease of use
- list of any dependencies or companion modules associated with each module (CCK, Taxonomy, Views, API modules, externally hosted code, etc.)
- features and functionality
- pros and cons
- list of access permissions
- evaluation of the documentation/handbook (if any)
- status of the most stable release (development, alpha, beta, official)
- if it is still in development, an evaluation for its potential for successful completion
- a brief examination of the its issue queues for any glaring or recurring problems

### Content Taxonomy

Content Taxonomy comes with three modules in addition to the main module. It only depends on the Content module (the main CCK module), the core Taxonomy module (obviously), and in addition to the default "Select List" widget, it also supports the widgets "autocomplete," "options," and "activeselect." "Activeselect" depends on another third party module Activeselect, since it's not a default widget. The amount of widgets it supports is even greater than the core Taxonomy module, even allowing autocomplete on non-freetagging vocabularies. It can optionally support Views (another third party module) if you have Views installed, but Views itself also has taxonomy support.

Installation and usage are relatively easy. Upon enabling, Taxonomy Fields would be available on the "Add field" page for a content type, depending on what widget modules you enabled. Once they are added, they replace existing fields provided by the Taxonomy module. Unfortunately, there is a funky reciprocal relationship problem; a vocabulary is normally limited to a few content types (or only one), but Content Taxonomy lets you choose any vocabulary to be added on to as a CCK field. It should respect Taxonomy settings and only let users choose a vocabulary that is meant for the content type they're configuring. Thus a user has to be careful to make sure that this vocabulary-content type relationship is valid in both ways. This is perhaps the only logical problem for Content Taxonomy. Aside from that, users can choose the depth of the taxonomy tree displayed (it can be unlimited), specific terms to be displayed (if the vocabulary is a tree), whether not it's required, whether not multiple values are allowed, default values, where the taxonomy information is stored (as a tag, in CCK table, or both), and etc. In other words, Content Taxonomy replicates some of core Taxonomy's functionality. It should simply honor the settings set in core Taxonomy.

#### At a glance

- **Dependency**: Taxonomy and Content. Optionally Activeselect (if installed) and Views (if installed).
- **Access permissions**: Content Taxonomy does not provide any additional access permissions on its own.
- **Documentation**: There are no documentation or handbook pages on Content Taxonomy, but given its straight-forward easiness, there's no need for any.
- **Release**: Content Taxonomy has no official releases. There are only development snapshots, but they're relatively stable.
- **Issues**: There are quite a few issues in Content Taxonomy's issue queue. In the past two weeks, there are 6 bug reported. The queue is quite active, however; there are patches pending review.
- **Development**: Content Taxonomy is still apparently in development. But once small edges are ironed out, it should have an official release. There are quite a number of users of Content Taxonomy.
- **Note: Synchronizing Terms with CCK**:Content Taxonomy currently only syncs taxonomy in one direction - that is, the CCK field can inject terms into the taxonomy tables, but if you already have taxonomy terms assigned, they won't show up in the CCK field - so this is currently most useful on a new site unless you're willing to figure out how to sync the taxonomy table into CCK.

#### Screenshots

- The widgets Content Taxonomy provides, depending how which modules you enabled.  
  ![](/files/content_taxonomy_1.png)
- Settings for widgets.  
  ![](/files/content_taxonomy_2.png)
- More settings.  
  ![](/files/content_taxonomy_3.png)
- Appearance of the autocomplete widget.  
  ![](/files/content_taxonomy_4.png)
- Appearance of the options widget.  
  ![](/files/content_taxonomy_5.png)
- Appearance of the select list widget.  
  ![](/files/content_taxonomy_6.png)

### CCK Taxonomy Fields

CCK Taxonomy Fields comes with only one main module. It depends on the Content module (the main CCK module), the core Taxonomy module (obviously), and Views. Views is not optional; it is mandatory.

Installation and usage are relatively easy. Upon enabling, CCK Taxonomy Fields would be available on the "Add field" page for a content type, depending on what vocabularies you have defined. Once they are added, they coexist with existing fields provided by the Taxonomy module. Unfortunately, CCK Taxonomy Fields suffers from the same problem Content Taxonomy suffers from: you can add a taxonomy field for a vocabulary that is not meant for a particular content type. However, the author, Robert Douglass, states that this is intentionally designed that way, so that the whole taxonomy mechanism can be sidestepped. In addition to that, you also cannot choose different widgets or act on a freetagging vocabulary, which is something Content Taxonomy can do. Unlike Content Taxonomy, however, CCK Taxonomy Fields simply honors the settings set in core Taxonomy, which is a great plus. This means CCK Taxonomy Fields is a great drop-in module to simply bring core Taxonomy-defined fields into the world of CCK fields.

#### At a glance

- **Dependency**: Taxonomy, Content, and Views.
- **Access permissions**: CCK Taxonomy Fields does not provide any additional access permissions on its own.
- **Documentation**: There are no documentation or handbook pages on CCK Taxonomy Fields, but given its straight-forward easiness, there's no need for any.
- **Release**: CCK Taxonomy Fields has a stable, official release.
- **Issues**: There is one bug in the issue queue that involves filters and CCK Taxonomy in the past three weeks. It seems to have something to do with the upgrade path.
- **Development**: CCK Taxonomy Fields is pretty mature.

#### Screenshots

- Fields are based on vocabularies in CCK Taxonomy, unlike Content Taxonomy, whose fields are based on widget types.  
  ![](/files/cck_taxonomy_1.png)
- There are few options to tinker with in CCK Taxonomy.  
  ![](/files/cck_taxonomy_2.png)
- What the field actually looks like during node editing.  
  ![](/files/cck_taxonomy_3.png)
- What the field actually looks like during node viewing without any custom theming.  
  ![](/files/cck_taxonomy_4.png)

### Taxonomy Super Select

Taxonomy Super Select comes with only one main module. It only depends on the core Taxonomy module, not even requiring CCK.

Installation and usage are relatively easy. Upon enabling, Taxonomy Super Select adds on options to settings pages for individual taxonomy vocabularies. Therefore, there is no entanglement between the relationship of a vocabulary itself and its corresponding CCK field, because CCK isn't even involved. Unlike Content Taxonomy, Taxonomy Super Select judges which widget is better for you, depending on the vocabulary. It can elegantly handle any kind of vocabulary settings a user can throw at it, and it would come up with a good, enhanced interface for it. Taxonomy Super Select achieves the ultimate integration with core Taxonomy by not integrating with CCK fields at all. For those merely wanting to change taxonomy selection widgets for nodes, Taxonomy Super Select is blissfully simple. ~~The only limitation Taxonomy Super Select has is that it can only work up to five levels of nesting on tree vocabularies; the author needs technical help regarding this.~~ *This has been fixed.*

#### At a glance

- **Dependency**: Only Taxonomy.
- **Access permissions**: Taxonomy Super Select does not provide any additional access permissions on its own, nor does it need any.
- **Documentation**: There are no documentation ~~or handbook pages~~ ([handbook here](http://drupal.org/node/191954)) on Taxonomy Super Select, but given its straight-forward easiness, there's no need for any.
- **Release**: Taxonomy Super Select has a stable, official release.
- **Issues**: ~~In the past three weeks on the issue queue, there have been two instances of an issue where Taxonomy Super Select would stop working mysteriously, after which it would only work on free tagging vocabularies.~~ *Most issues have been fixed, except a few feature requests for free tagging.*
- **Development**: ~~Taxonomy Super Select is in its first official release, so there may be a few things to iron out.~~

#### Screenshots

- Less is more: the only additional options that are tacked into vocabulary editing pages provided by core Taxonomy. (click to enlarge)  
  [![](/files/taxonomy_super_select_1.png)](/files/taxonomy_super_select_1.png)
- All your vocabulary and user interface belong to us. (as seen when viewing a node, click to enlarge)  
  [![](/files/taxonomy_super_select_2.png)](/files/taxonomy_super_select_2.png)

### CCK Taxonomy Super Select Ultra

CCK Taxonomy Super Select Ultra comes with only one main module. It depends on the Content module (the main CCK module) and the core Taxonomy module (obviously). It aims to combine CCK Taxonomy with Taxonomy Super Select.

Installation and usage are relatively easy. Upon enabling, CCK Taxonomy Super Select Ultra would be available on the "Add field" page for a content type, depending on what vocabularies you have defined. Once they are added, they coexist with existing fields provided by the Taxonomy module. CCK Taxonomy Super Select Ultra combines the CCK integration offered by CCK Taxonomy with the user interface and widget sweetness of Taxonomy Super Select. It also inherits the weakness (or feature, depending on your viewpoint) of CCK Taxonomy: you can apply CCK Taxonomy Super Select Ultra fields to vocabularies that are not meant for that content type. Likewise, it inherits the honoring quality of both CCK Taxonomy and Taxonomy Super Select, respecting the settings set in core Taxonomy.

#### At a glance

- **Dependency**: Taxonomy and Content.
- **Access permissions**: CCK Taxonomy Super Select Ultra does not provide any additional access permissions on its own.
- **Documentation**: There are no handbook pages on CCK Taxonomy Super Select Ultra, but a detailed readme file is included.
- **Release**: CCK Taxonomy Super Select Ultra has a stable, official release.
- **Issues**: There are two minor bug reports on the issue queue for the past four weeks.
- **Development**: CCK Taxonomy Super Select Ultra is in its first official release, so there may be a few things to iron out.

#### Screenshots

- Like father, like son. CCK Taxonomy Super Select Ultra inherits the simplicity in configuring from Taxonomy Super Select. (click to enlarge)  
  [![](/files/cck_taxonomy_super_select_ultra_1.png)](/files/cck_taxonomy_super_select_ultra_1.png)
- Original core Taxonomy field (top) versus CCK Taxonomy Super Select Ultra field (bottom), during node editing.  
  ![](/files/cck_taxonomy_super_select_ultra_2.png)

### The Verdict

There's so many choices, so what to use? There's actually more than one answer. Each answer is based on the pros and cons of each module.

- If you need to bridge taxonomy fields to CCK and you want the freedom to choose widgets for yourself, **Content Taxonomy** is your best choice.
- If all you need is to CCK-ify taxonomy fields and you like, and want the user interface that Taxonomy Super Select provides, then **CCK Taxonomy Super Select Ultra** is for you.
- If you don't need the user interface fanciness and all you need is to simply bridge taxonomy fields to CCK with no other user interface objections, **CCK Taxonomy** is what you want.
- If all you need is a better user interface and you don't need CCK, **Taxonomy Super Select** is it.
