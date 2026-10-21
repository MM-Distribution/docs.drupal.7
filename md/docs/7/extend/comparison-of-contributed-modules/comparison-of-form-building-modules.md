---
title: "Comparison of Form Building Modules"
source_url: "https://www.drupal.org/docs/7/extend/comparison-of-contributed-modules/comparison-of-form-building-modules"
page_type: page
last_updated: "Last updated on 30 April 2025"
published: "2013-09-06T12:57:44+00:00"
modified: "2025-04-30T20:53:04+00:00"
breadcrumb: ["Drupal 7", "Extending Drupal 7", "Comparison of contributed modules"]
fetched: "2026-10-21T08:58:58Z"
raw: "raw/docs/7/extend/comparison-of-contributed-modules/comparison-of-form-building-modules.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Comparison of Form Building Modules

Drupal has a lot of modules aimed at helping site builders and users add forms to their sites. What follows is a rough comparison of three of them for Drupal 8 and five of them for Drupal 7. Please add any missed or new information about the ones listed.

## Drupal 8

### [Contact Storage](https://www.drupal.org/project/contact_storage)

Contact Storage module will provide storage for Contact messages which are fully-fledged entities in Drupal 8. This plus core contact module aim to provide functionality equivalent to the base-features of Webform or Entity Form.

### [Webform](https://www.drupal.org/project/webform)

Webform 8.x-5.x is a completely new code base, that takes a different, but familiar approach to solving the challenges of building rich, flexible, and maintainable client facing forms for a Drupal website. Webform 8-x-5.x includes many new features and leverages improvements in Drupal 8, including OO design patterns, extendable plugins, and automated tests.

Please visit the Webform 8.x-5.x documentation pages for an [introduction](/node/2834423), [features overview](/node/2837024), [video tutorials](/node/2834424), and a [roadmap](/node/2843422).

Like Webform in Drupal 7, it does not use Drupal 8 Field module field types.

### [eForm](https://www.drupal.org/project/eform)

The EForm module (Entity Form in Drupal 7) enables you to create front-end forms (fieldable entities) which contain standard Drupal fields. Eform's maintainer is considering whether the module is needed anymore with core Contact and Contact Storage taking a similar approach. [Is this module still needed?](https://www.drupal.org/node/2809179)

Also see [Differences between the Webform module and Contact module](https://www.drupal.org/docs/8/modules/webform/webform-frequently-asked-questions/differences-between-the-webform-module-and), which provides a side-by-side feature comparison.

### [Entityforms](http://drupal.org/project/entityform)

The Entityforms module seems to be the same as web form but using the Entity API. It uses the normal entity/field api as a kind of form builder. You can have as many 'Forms' as you like (each 'form' is a different bundle on the Entity Form entity) and you can add whatever fields you want.

#### Pros

- Entityforms can make a wide variety of forms with lots of different fields available.
- Entityform is already being ported to Drupal 8.
- Entityforms uses the entity API which guarantees it will work with:
  - Views
  - Rules
  - Entity Reference
  - Organic Groups
  - Every field module in Drupal, including: Date, File, Geofield, Name, Address, Media and many more...
- Other tools for Entities will work with the module, for example: Entity Operations.
- Integrates with field group
- Integrates with Conditional Fields
- Entityform is fairly well established.

#### Cons

- Entityforms cannot (without some magic) be used to edit nodes or comments.
- You can only have one form for each bundle.
- Any form can only edit one submission entity at a time.

### [Flexiform](http://drupal.org/project/flexiform)

Flexiform's main purpose is to provide a UI for building forms to add/edit other entities. Flexiform allows you as a site builder to configure as many different forms as you like to edit whatever entities you want. With its pluggable Builder and Element system, it could possible to configure multi-step forms for any entity on your website. Flexiform also uses a relationship system similar to CTools to allow you to edit multiple entities with one form.

Flexiform can provide a complete separation between how content is stored and how content is edited.

The flexiform_webform sub-module provides basically the same functionality as Entity Forms, so a combination of Entityform and flexiform would be a good one.

#### Pros

- Flexiform can make a wide variety of forms with lots of different fields available.
- Flexiform uses the entity API which guarantees it will work with:
  - Views
  - Rules
  - Entity Reference
  - Organic Groups
  - Every field module in Drupal, including: Date, File, Geofield, Name, Address, Media and many more...
- Integrates with field group
- Flexiform can be used to edit or add any entity.
- Flexiform can pull multiple entities into one form using relationships. For example, creating a user edit form the has fields from various profile2 is easy with flexiform.
- **\[WIP\]**Flexiform will be allow you to configure multi step forms.
- Flexiform can have an unlimited number of forms for one entity type. If you want 3 different ways to submit a feedback form, but want the responses from that form to be treated as the same thing (in one view for example) this is easy with flexiform.
- Flexiform can override existing node forms allowing site builders to edit existing system forms without resorting to code and hook_form_alter().
- Flexiform has a pluggable element system, its easy to add any element you want with a bit of code!
- Flexiform allows you to add blocks of custom html anywhere on your form.
- Flexiform is already being ported to Drupal 8.
- The maintainers of flexiform already use it one several large, high-traffic websites. Including Event booking systems and University Management software.

#### Cons

- Flexiform is a young module that hasn't gained much traction in the community yet.
- Some features are still a little rough round the edges, although patches are always welcome.
- The list of elements available is not yet comprehensive (see [\#1451452: Add flexiform element handler for entity properties that are not FieldAPI fields e.g. Node Title](/project/flexiform/issues/1451452 "Status: Closed (fixed)")) patches are always welcome.

### [Form Builder](http://drupal.org/project/form_builder)

Form Builder provides a UI for constructing Drupal Form API forms. It therefore has all the flexibility of the Drupal Form API (that's alot of flexibility!), however it does not provide any way to save the submissions. It's a bit different from the other 3 as it just exports the code for you to add the form to your site somewhere, but leaves the site builder to program the validation and submission mechanisms.

### [Quick Forms](https://drupal.org/project/qforms)

Lightweight alternative to Webform. Created mostly for the use by developers with extensibility in mind.
