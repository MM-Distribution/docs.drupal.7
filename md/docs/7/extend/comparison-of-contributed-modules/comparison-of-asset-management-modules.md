---
title: "Comparison of Asset Management modules"
source_url: "https://www.drupal.org/docs/7/extend/comparison-of-contributed-modules/comparison-of-asset-management-modules"
page_type: page
last_updated: "Last updated on 30 April 2025"
published: "2013-04-12T21:31:00+00:00"
modified: "2025-04-30T20:53:04+00:00"
breadcrumb: ["Drupal 7", "Extending Drupal 7", "Comparison of contributed modules"]
fetched: "2026-10-21T08:57:10Z"
raw: "raw/docs/7/extend/comparison-of-contributed-modules/comparison-of-asset-management-modules.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Comparison of Asset Management modules

These are modules that allow you to manage (multi)media assets. Modules that manage only images are left out because they are already compared in another handbook page.

|                                   |                                             |                                                                 |                                                        |
|-----------------------------------|---------------------------------------------|-----------------------------------------------------------------|--------------------------------------------------------|
| Name                              | [Media](//drupal.org/project/media)         | [Scald](//drupal.org/project/scald)                             | [Asset](//drupal.org/project/asset)                    |
| Since (all/7.x)                   | Mar 2005 (Jun 2010)                         | Jul 2008 (May 2012)                                             | May 2007 (Jul 2012)                                    |
| Installs                          | 186K                                        | 4.4K                                                            | 800                                                    |
| Dependency                        | Views, CTools, File Entity (2.x), Image     | Views, CTools, Image                                            | Views, CTools, Entity API, Field UI, Field SQL Storage |
| D6                                | no                                          | beta                                                            | no                                                     |
| Tests                             | yes (62 assertions 1.x, 992 assertions 2.x) | yes (514 assertions)                                            | no                                                     |
| Community                         | active: 14 participants                     | active: 5 participants                                          | active: 5 participants                                 |
| D7                                | 1.x stable, 2.x alpha                       | stable                                                          | beta                                                   |
| D8                                | File Entity (1)                             | [Media Entity](https://www.drupal.org/project/media_entity) (1) | ?                                                      |
| WYSIWYG integration               | WYSIWYG or CKEditor module                  | any module (CKEditor preferred)                                 | CKEditor module                                        |
| Richtext editors                  | editors supported by WYSIWYG                | any editor                                                      | CKEditor                                               |
| Embedded view modes               | only images, others with contrib            | yes                                                             | yes                                                    |
| Flexible embedded view modes      | no (patch)                                  | yes                                                             | yes                                                    |
| Override embed                    | no (patch)                                  | legend/caption, alignment                                       | many fields                                            |
| Fieldable entities                | yes                                         | yes                                                             | yes                                                    |
| Media library                     | yes                                         | yes                                                             | yes                                                    |
| Asset editing on content          | no                                          | yes                                                             | yes                                                    |
| Inline editing in WYSIWYG         | partial (textfield only)                    | yes                                                             | partial (textfield only)                               |
| Media reusability                 | yes                                         | yes                                                             | yes                                                    |
| Media usage tracking              | yes (in unstable7)                          | yes, built-in                                                   | no                                                     |
| Media derivatives                 | no (possible with contrib)                  | yes (built-in)                                                  | no                                                     |
| Responsive                        | yes (Picture integration)                   | yes (Picture integration)                                       | no                                                     |
| Access control/License management | no (possible with contrib)                  | yes (built-in)                                                  | no                                                     |
| Exportable config                 | partial                                     | yes                                                             | yes (through field/entity API)                         |
| Distribution                      | [Media Dev](//drupal.org/project/media_dev) | [Scald Galaxy](//drupal.org/project/scald_galaxy)               | no                                                     |

\(1\) In Drupal 8 there will be some generic modules like Entity Browser, Entity Embed etc. that work independently on the entity type (File entity, Scald atom etc.)
