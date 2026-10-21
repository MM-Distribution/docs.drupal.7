---
title: "Comparison of Question and Answer modules"
source_url: "https://www.drupal.org/docs/7/extend/comparison-of-contributed-modules/comparison-of-question-and-answer-modules"
page_type: page
last_updated: "Last updated on 30 April 2025"
published: "2010-04-22T08:01:45+00:00"
modified: "2025-04-30T20:53:04+00:00"
breadcrumb: ["Drupal 7", "Extending Drupal 7", "Comparison of contributed modules"]
fetched: "2026-10-21T09:01:18Z"
raw: "raw/docs/7/extend/comparison-of-contributed-modules/comparison-of-question-and-answer-modules.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Comparison of Question and Answer modules

**NOTE: A more up to date review can be found [here](http://groups.drupal.org/node/156669).**

There are many ways to create Question / Answer functionality using Drupal.

### Presenting lists of questions/answers

If your requirement is only to *present* content in question/answer format then you could consider using [Views](http://drupal.org/project/views) and [CCK](http://www.drupal.org/project/cck) in Drupal 5/6, or using the inbuilt Fields API in Drupal 7. Create separate text fields for the question and answer elements, and attach these to the appropriate node type. Then decide how the question and answer fields should appear in different contexts (for example, in teaser view you could show only the question, with a "Click here to see the answer link", whereas the full node view shows both question and answer fields).

Alternatively, you could check out the [FAQ](http://www.drupal.org/project/faq) module, which creates a new node type and comes with several pre-formatted lists to present question and answers.

### Creating a question answering workflow

If you want to create a workflow whereby users can ask a question, and other users (or site administrators) can answer those questions and optionally publish the response then there are a number of modules available. These vary in their approach, complexity, and number of features, as compared in the following table:

<table style="width:100%;" data-border="1">
<colgroup>
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 16%" />
</colgroup>
<thead>
<tr class="header">
<th style="text-align: center;">Feature</th>
<th style="text-align: center;"><a href="http://drupal.org/project/question">Question</a></th>
<th style="text-align: center;"><a href="http://drupal.org/project/faq_ask">FAQ_Ask</a></th>
<th style="text-align: center;"><a href="http://drupal.org/project/answers">Answers</a></th>
<th style="text-align: center;"><a href="http://drupal.org/project/topic">Topic / Answers</a></th>
<th style="text-align: center;"><a href="http://drupal.org/project/question_answer">Question/Answer</a></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<th colspan="6" style="text-align: center;">Drupal-related</th>
</tr>
<tr class="header">
<th style="text-align: center;"></th>
<th style="text-align: center;"></th>
<th style="text-align: center;"></th>
<th style="text-align: center;"></th>
<th style="text-align: center;"></th>
<th style="text-align: center;"></th>
</tr>
&#10;<tr class="odd">
<td style="text-align: center;">Drupal 7.x</td>
<td style="text-align: center;"><img src="/misc/watchdog-warning.png" /> -dev</td>
<td style="text-align: center;"><img src="/misc/watchdog-error.png" /></td>
<td style="text-align: center;"><img src="/misc/watchdog-ok.png" /></td>
<td style="text-align: center;"><img src="/misc/watchdog-error.png" /></td>
<td style="text-align: center;"><img src="/misc/watchdog-ok.png" /></td>
</tr>
<tr class="even">
<td style="text-align: center;">Drupal 6.x</td>
<td style="text-align: center;"><img src="/misc/watchdog-ok.png" /></td>
<td style="text-align: center;"><img src="/misc/watchdog-ok.png" /></td>
<td style="text-align: center;"><img src="/misc/watchdog-ok.png" /></td>
<td style="text-align: center;"><img src="/misc/watchdog-error.png" /></td>
<td style="text-align: center;"><img src="/misc/watchdog-ok.png" /></td>
</tr>
<tr class="odd">
<td style="text-align: center;">Dependencies</td>
<td style="text-align: center;">None</td>
<td style="text-align: center;"><a href="http://www.drupal.org/project/faq">FAQ</a> module, <a href="http://www.drupal.org/project/helpers_database">Helpers_database</a> module</td>
<td style="text-align: center;">Drupal 6: Features, Nodereference Count, Node Reference URL Widget, CCK, Strongarm, Views attach, Views, Voting API, Vote Up/Down, Chaos tool suite
Drupal 7: Entity Views Attachment, Features, List, References, Nodereference Count, Node Reference URL Widget, Strongarm, Views</td>
<td style="text-align: center;">None</td>
<td style="text-align: center;">CCK and CTools in D6 version. VotingAPI/Views integration.</td>
</tr>
<tr class="even">
<td style="text-align: center;">Documentation</td>
<td style="text-align: center;"><a href="http://drupal.org/node/763884">Handbook</a></td>
<td style="text-align: center;"><a href="http://drupal.org/node/192806">Handbook</a></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
<td style="text-align: center;"><a href="http://drupal.org/node/955460">Handbook</a></td>
</tr>
<tr class="odd">
<td style="text-align: center;">Architecture</td>
<td style="text-align: center;">Questions saved in separate database table.<br />
Question/Answer pairs saved as nodes.</td>
<td style="text-align: center;">Questions saved as (unpublished) FAQ nodes.<br />
Question/Answer pairs saved as (published) FAQ nodes.</td>
<td style="text-align: center;">Questions and Answers are nodes. Attachment of answers to question node through EVA module. Extra module to select best answer and integration with user points.</td>
<td style="text-align: center;"> </td>
<td style="text-align: center;">Question as node, Answers as comments, CCK field to store the selected answer.</td>
</tr>
</tbody>
</table>
