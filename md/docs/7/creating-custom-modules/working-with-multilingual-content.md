---
title: "Working with multilingual content"
source_url: "https://www.drupal.org/docs/7/creating-custom-modules/working-with-multilingual-content"
page_type: page
last_updated: "Last updated on 22 September 2016"
published: "2008-09-04T16:22:37+00:00"
modified: "2016-09-22T09:06:23+00:00"
breadcrumb: ["Drupal 7", "Creating custom modules in Drupal 7"]
fetched: "2026-10-21T07:49:40Z"
raw: "raw/docs/7/creating-custom-modules/working-with-multilingual-content.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Working with multilingual content

As of Drupal 6, the core content translation module enables multilingual content.

Features include:

- Enables the designation of a language for each piece of content
- Enables content to be translated
- Enables flagging of content translations as needing updating

Handbook page: <http://drupal.org/handbook/modules/translation>

### Main methods for working with multilingual content

Here are some of the main functions useful when working with multilingual content:

- [translation_node_get_translations()](http://api.drupal.org/api/function/translation_node_get_translations/6 "Get all nodes in a translation set, represented by $tnid")
- [translation_path_get_translations()](http://api.drupal.org/api/function/translation_path_get_translations/6 "Return paths of all translations of a node, based on its Drupal path")
- [translation_supported_type()](http://api.drupal.org/api/function/translation_supported_type/6 "Returns whether the given content type has support for translations.")

### Data structure and concepts

At the data level, content translation has introduced three new fields in the node table:

- *language*: The {languages}.language of this node.
- *tnid*: The translation set id for this node, which equals the node id of the source post in each set.
- *translate*: A boolean indicating whether this translation page needs to be updated.

Nodes that are translations of each other are considered to be part of a "translation set", distinguished by a common `$node->tnid` value. A translation set is considered to have a "source" node--the first version from which others were translated. The source translation is the node with a nid equal to the tnid for the set.

If the source translation is deleted, another translation in the set is designated as the new source translation. Preference is given to translations that are not marked as needing updating.

### Preparing your content for translation

When an existing piece of content is being translated, `hook_nodeapi()` is called with the 'prepare translation', op, allowing modules to set appropriate node properties before a node editing form is presented to the user.

In the node object passed to this nodeapi op, the original version of the node is passed in a `$node->translation_source` object. Typically, 'prepare translation' nodeapi implementations will test the `$node->translation_source` object and set properties of the `$node` object accordingly.

Say you have a module that adds a field, 'place', to nodes. A minimal `hook_nodeapi()` implementation might look like this:

``` php
function mymodule_nodeapi(&$node, $op, $a3 = NULL, $a4 = NULL) {
  switch ($op) {
    case 'insert':
      ...
    case 'update':
      ...
    case 'delete':
      ...
    case 'load':
      ...
    case 'prepare translation':
      $node->place = $node->translation_source->place;
      break;
  }
}
```

### Aggregating content across translations

Some of the key module development challenges raised by content translation relate to handling node data across translations.

Say you have ranking of content in a multilingual context where each node might have several versions, one per language. By default, all nodes are separate, so e.g. votes on members of a translation set will be tallied separately. How do you determine the sum votes across the translation set?

The right approach to this sort of problem will take some analysis. Options might include:

- *Change the way data are saved.* For some usages, you may wish to save data for all members of a translation set any time any one member is updated. Example: whenever a node is voted on, increment the vote for all other members of its translation set. Alternate: whenever a node is being voted on, assign its vote to the source translation of a translation set, such that the source translation receives all votes and other members of the set get none.
- *Change the presentation of data.* Sometimes the original data will be important to retain and values need to be altered only on presentation. Example: register votes separately for each member of a translation set but, when any member is being viewed, calculate its vote as the sum of all votes for members of the translation set.
- *Provide new aggregation options across a translation set* Rather than or in addition to changing the presentation of individual pieces of content, it may be useful to provide lists aggregated across a translation set. Example: provide a view field that aggregates votes for a translation set rather than individual nodes.

### Using the tnid as a primary identifier

In some cases it may make sense to use the tnid, if set, rather than the nid as a primary identifier for content.

Any approach that does so will need to respond to changes in tnid.

When a node in a translation set is deleted (see [translation_remove_from_set()](http://api.drupal.org/api/function/translation_remove_from_set)), one of two things can happen:

- If there is only one member left, it gets a tnid of 0.
- If the node deleted is the source translation, a new source translation is chosen and existing members of the translation set updated accordingly.

Any approach relying on the tnid needs to respond to this change. Usually what's needed is:

If the tnid has been converted to 0, use nid instead.

If the source translation has changed, update data with the old tnid to use the new one.
