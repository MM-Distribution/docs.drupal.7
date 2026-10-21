---
title: "Comparison of Links Page modules"
source_url: "https://www.drupal.org/docs/7/extend/comparison-of-contributed-modules/comparison-of-links-page-modules"
page_type: page
last_updated: "Last updated on 30 April 2025"
published: "2008-08-22T00:25:09+00:00"
modified: "2025-04-30T20:53:04+00:00"
breadcrumb: ["Drupal 7", "Extending Drupal 7", "Comparison of contributed modules"]
fetched: "2026-10-21T09:00:01Z"
raw: "raw/docs/7/extend/comparison-of-contributed-modules/comparison-of-links-page-modules.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Comparison of Links Page modules

Many sites have a links page of one form or another; these modules attempt to address some of the problems with links pages. These modules have similar functionality but their structures are quite different. It is unlikely that they will ever merge.

<table style="width:100%;" data-border="1">
<colgroup>
<col style="width: 10%" />
<col style="width: 10%" />
<col style="width: 10%" />
<col style="width: 10%" />
<col style="width: 10%" />
<col style="width: 10%" />
<col style="width: 10%" />
<col style="width: 10%" />
<col style="width: 10%" />
<col style="width: 10%" />
</colgroup>
<thead>
<tr class="header">
<th style="text-align: center;">Feature</th>
<th style="text-align: center;"><a href="http://drupal.org/project/links">Links</a></th>
<th style="text-align: center;"><a href="http://drupal.org/project/weblinks">Web Links</a></th>
<th style="text-align: center;"><a href="http://drupal.org/project/userlink">Userlink</a></th>
<th style="text-align: center;"><a href="http://drupal.org/project/link">Link</a></th>
<th style="text-align: center;"></th>
<th style="text-align: center;"></th>
<th style="text-align: center;"></th>
<th style="text-align: center;"></th>
<th style="text-align: center;"></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<th colspan="10" style="text-align: center;">Drupal-related</th>
</tr>
&#10;<tr class="odd">
<th style="text-align: center;">Drupal 7.x</th>
<td style="text-align: center;"><img src="/misc/watchdog-error.png" /></td>
<td style="text-align: center;">1.0</td>
<td style="text-align: center;"><img src="/misc/watchdog-error.png" /></td>
<td style="text-align: center;"><img src="/misc/watchdog-ok.png" /></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
</tr>
<tr class="even">
<th style="text-align: center;">Drupal 6.x</th>
<td style="text-align: center;"><img src="/misc/watchdog-ok.png" /></td>
<td style="text-align: center;"><img src="/misc/watchdog-ok.png" /></td>
<td style="text-align: center;"><img src="/misc/watchdog-warning.png" /> -dev available</td>
<td style="text-align: center;"><img src="/misc/watchdog-ok.png" /></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
</tr>
<tr class="odd">
<th style="text-align: center;">Last update</th>
<td style="text-align: center;">2013-Sep-30</td>
<td style="text-align: center;">2015-May-12</td>
<td style="text-align: center;">2013-Oct-19</td>
<td style="text-align: center;">2014-Nov-6</td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
</tr>
<tr class="even">
<th style="text-align: center;">Documentation</th>
<td style="text-align: center;"><a href="http://drupalcode.org/project/links.git/blob/HEAD:/README.txt">README.txt</a></td>
<td style="text-align: center;"><a href="http://drupal.org/node/273907">Handbook</a><br />
<a href="http://drupalcode.org/project/weblinks.git/blob/HEAD:/README.txt">README.txt</a></td>
<td style="text-align: center;"><a href="http://drupalcode.org/project/userlink.git/blob/HEAD:/readme.txt">README.txt</a></td>
<td style="text-align: center;"><a href="https://www.drupal.org/documentation/modules/link">Handbook</a></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
</tr>
<tr class="odd">
<th style="text-align: center;">Demonstration</th>
<td style="text-align: center;"><img src="/misc/watchdog-error.png" /></td>
<td style="text-align: center;"><a href="http://nanwich.com/links.html">demo</a></td>
<td style="text-align: center;"><img src="/misc/watchdog-error.png" /></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
</tr>
<tr class="even">
<th style="text-align: center;">Architecture</th>
<td style="text-align: center;">term-based</td>
<td style="text-align: center;">term-based (optional)<sup>a</sup></td>
<td style="text-align: center;">term-based</td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
</tr>
<tr class="odd">
<th style="text-align: center;">Additional database tables</th>
<td style="text-align: center;">3</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
</tr>
<tr class="even">
<th style="text-align: center;">Services provided</th>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
</tr>
<tr class="odd">
<th style="text-align: center;">Multiple vocabularies</th>
<td style="text-align: center;">Yes</td>
<td style="text-align: center;">No - only one used at a time.</td>
<td style="text-align: center;">Yes</td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
</tr>
<tr class="even">
<th style="text-align: center;">Classify entries using taxonomy</th>
<td style="text-align: center;">Required</td>
<td style="text-align: center;">Allowed, not required<sup>a</sup></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
</tr>
<tr class="odd">
<th style="text-align: center;">Check link validity</th>
<td style="text-align: center;"><img src="/misc/watchdog-ok.png" /></td>
<td style="text-align: left;"><ul>
<li>301 update optional</li>
<li>unpublish on error optional</li>
<li>assign to alternate user on user delete optional</li>
</ul></td>
<td style="text-align: center;"><img src="/misc/watchdog-error.png" /></td>
<td style="text-align: center;"><img src="/misc/watchdog-ok.png" /></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
</tr>
<tr class="even">
<th style="text-align: center;">Maximum link length supported</th>
<td style="text-align: center;">16,384<sup>b</sup></td>
<td style="text-align: center;">16,384<sup>b</sup></td>
<td style="text-align: center;">?</td>
<td style="text-align: center;">?</td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
</tr>
<tr class="odd">
<th style="text-align: center;">Click tracking</th>
<td style="text-align: center;"><img src="/misc/watchdog-ok.png" /></td>
<td style="text-align: center;"><img src="/misc/watchdog-ok.png" /><br />
Using "goto" redirect method</td>
<td style="text-align: center;"><img src="/misc/watchdog-error.png" /></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
</tr>
<tr class="even">
<th style="text-align: center;">Commenting on entries</th>
<td style="text-align: center;"><img src="/misc/watchdog-ok.png" /></td>
<td style="text-align: center;"><img src="/misc/watchdog-ok.png" /></td>
<td style="text-align: center;"><img src="/misc/watchdog-ok.png" /></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
</tr>
<tr class="odd">
<th style="text-align: center;">Feature blocks</th>
<td style="text-align: center;"><ul>
<li>Top</li>
<li>Blogroll</li>
</ul></td>
<td style="text-align: center;"><ul>
<li>each term</li>
<li>Recent</li>
<li>Random</li>
<li>Unpublished</li>
<li>Popular</li>
<li>My Links</li>
<li>Contributors</li>
<li>Related links</li>
<li>User's links</li>
</ul></td>
<td style="text-align: center;"><ul>
<li>All Links</li>
<li>My Links</li>
<li>Recent Links</li>
<li>Popular Link Categories</li>
<li>User's Link Categories</li>
</ul></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
</tr>
<tr class="even">
<th style="text-align: center;">Security</th>
<td style="text-align: center;">Drupal core</td>
<td style="text-align: center;">Drupal core</td>
<td style="text-align: center;">Drupal core</td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
</tr>
<tr class="odd">
<th style="text-align: center;">Settings</th>
<td style="text-align: center;">Yes</td>
<td style="text-align: center;">Yes, maybe too many.</td>
<td style="text-align: center;">Yes</td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
</tr>
<tr class="even">
<th style="text-align: center;">Links page description</th>
<td style="text-align: center;"><img src="/misc/watchdog-error.png" /></td>
<td style="text-align: center;"><img src="/misc/watchdog-ok.png" /></td>
<td style="text-align: center;"><img src="/misc/watchdog-error.png" /></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
</tr>
<tr class="odd">
<th style="text-align: center;">Show page ranking</th>
<td style="text-align: center;">?</td>
<td style="text-align: center;"><img src="/misc/watchdog-ok.png" /></td>
<td style="text-align: center;">?</td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
</tr>
<tr class="even">
<th style="text-align: center;">Show empty terms/groups</th>
<td style="text-align: center;"><img src="/misc/watchdog-error.png" /></td>
<td style="text-align: center;"><img src="/misc/watchdog-ok.png" /> with optional "invitation" text</td>
<td style="text-align: center;"><img src="/misc/watchdog-error.png" /></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
</tr>
<tr class="odd">
<th style="text-align: center;">Content filtering</th>
<td style="text-align: center;"><img src="/misc/watchdog-error.png" /></td>
<td style="text-align: center;"><img src="/misc/watchdog-ok.png" /> optional add-on</td>
<td style="text-align: center;"><img src="/misc/watchdog-error.png" /></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
</tr>
<tr class="even">
<th style="text-align: center;">Displays rankings</th>
<td style="text-align: center;"></td>
<td style="text-align: center;"><img src="/misc/watchdog-ok.png" /> optional add-on for Google PR and Alexa traffic rank</td>
<td style="text-align: center;"><img src="/misc/watchdog-error.png" /></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
</tr>
<tr class="odd">
<th style="text-align: center;">Themeability</th>
<td style="text-align: center;">??</td>
<td style="text-align: left;"><ul>
<li>Drupal core node theming</li>
<li>Independent themeing for all feature blocks</li>
<li>Independent themeing for all parts of a link</li>
<li>Multiple CSS files</li>
</ul></td>
<td style="text-align: center;"><ul>
<li>Drupal core node theming</li>
<li>CSS file gets included.</li>
</ul></td>
<td style="text-align: center;"><img src="/misc/watchdog-ok.png" /></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
</tr>
<tr class="even">
<th style="text-align: center;"><a href="http://drupal.org/project/taxonomy_image">Taxonomy Image</a> support</th>
<td style="text-align: center;"><img src="/misc/watchdog-error.png" /></td>
<td style="text-align: center;"><img src="/misc/watchdog-ok.png" /></td>
<td style="text-align: center;"><img src="/misc/watchdog-error.png" /></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
</tr>
<tr class="odd">
<th style="text-align: center;"><a href="http://drupal.org/project/image">Image Attach</a> support</th>
<td style="text-align: center;"><img src="/misc/watchdog-error.png" /></td>
<td style="text-align: center;"><img src="/misc/watchdog-ok.png" /></td>
<td style="text-align: center;"><img src="/misc/watchdog-error.png" /></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
</tr>
<tr class="even">
<th style="text-align: center;">Translation template supplied</th>
<td style="text-align: center;"><img src="/misc/watchdog-ok.png" /></td>
<td style="text-align: center;"><img src="/misc/watchdog-ok.png" /></td>
<td style="text-align: center;"><img src="/misc/watchdog-error.png" /></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
</tr>
<tr class="odd">
<th style="text-align: center;">Conversion function supplied<sup>c</sup></th>
<td style="text-align: center;">Yes</td>
<td style="text-align: center;">N/A</td>
<td style="text-align: center;">No</td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
</tr>
<tr class="even">
<th style="text-align: center;">Allow private links</th>
<td style="text-align: center;">?</td>
<td style="text-align: center;">planned</td>
<td style="text-align: center;">?</td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
</tr>
<tr class="odd">
<th style="text-align: center;">Change content type name</th>
<td style="text-align: center;"><img src="/misc/watchdog-error.png" /></td>
<td style="text-align: center;"><img src="/misc/watchdog-error.png" /></td>
<td style="text-align: center;"><img src="/misc/watchdog-error.png" /></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
</tr>
<tr class="even">
<th style="text-align: center;">Firefox</th>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
</tr>
<tr class="odd">
<th style="text-align: center;">SyncPlaces</th>
<td style="text-align: center;">?</td>
<td style="text-align: center;">XBEL</td>
<td style="text-align: center;">?</td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
</tr>
</tbody>
</table>

<sup>a</sup> Weblinks currently will use the core Taxonomy module, if it is available, however the module works fine without classifying links.

<sup>b</sup> This is limited solely by the database implementation of the "TEXT" type.

<sup>c</sup> Web Links provides conversions from Links, Janode, and LinksDB.

### Links Design

This module grew out of the old 4.6 Weblink module, which is still included with the package.

There is a specified road map for the Links package, but it seems to be slow in coming. Many parts of the package are not yet implemented.

The maintainer has been asked to update this.

### Weblinks Design

Many, if not most, web sites have some kind of links page. These are often hand-coded and quickly fall into disrepair. Site users can usually not submit links to be included, except through email, and they may never show up. The Web Links module takes care of all of these problems.

Web Links are nodes, with full node features (including Views). The module produces a "catalog" of all of the links in user-specified formats that can be customized to the admin's design. With appropriate permissions, anyone may be allowed to submit links that can be included immediately, or after the admin approves (publishes) them. And the module may optionally be directed to verify the continuing validity of the links, identifying those with problems, or even unpublishing them. The module may also update a link that has been redirected (301).

Click tracking is now available, and there is a "Popular Links" block to go with it.

In addition to displaying a links page, the module provides an administrator overview page. There is a variety of blocks available. There are many options for theming the output and there are three CSS files for examples.

A conversion program from the Links, Janode, and LinksDB packages to Web Links package is available.

This module is approaching the ability to become an API, and is being looked at for changing to that. The long range goal is to be based on CCK and Views with an API and add-on modules to extend the functions.

### Link Design

The [Link](http://drupal.org/project/link) module provides a link field type for site builders who want to have a link field in an entity.

### Node Links Design

The maintainer has been asked to update this.

### Userlink Design

[Userlink](http://drupal.org/project/userlink) was designed to be a small, simple module for maintaining links. It is tied a bit too tightly with taxonomy in regards to the custom blocks that it provides, but taxonomy is not a requirement.

Ideally, Userlink will go away soon. It has only gotten upgraded to 5.x and 6.x because folks have provided patches to upgrade the thing. The [Link](http://drupal.org/project/link) module provides a CCK field URL, and it probably makes sense for all of these modules to migrate towards using it. If the 6.x patch for Userlink to do a straight upgrade hadn't been so good, the project would have eventually moved towards a CCK/Link/Views implementation.

Who wants to merge projects? Web Links seems to be the most popular, but it is loaded up with code. Can we join forces, simplify the base modules, and make it easy to extend? With CCK and Views and having a node-based "web link" there should be very little need for specialized "Web Links" only add-ons.

### Janode Design

[Request for participation](http://drupal.org/node/286571) in the Janode issue queue.

### LinksDB Design

This module is deprecated in favor of [Web Links](http://drupal.org/project/weblinks). A conversion function is available.
