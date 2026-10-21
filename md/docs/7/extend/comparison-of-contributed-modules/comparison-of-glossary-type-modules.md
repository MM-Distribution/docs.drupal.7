---
title: "Comparison of Glossary-type modules"
source_url: "https://www.drupal.org/docs/7/extend/comparison-of-contributed-modules/comparison-of-glossary-type-modules"
page_type: page
last_updated: "Last updated on 30 April 2025"
published: "2008-06-04T09:30:03+00:00"
modified: "2025-04-30T20:53:04+00:00"
breadcrumb: ["Drupal 7", "Extending Drupal 7", "Comparison of contributed modules"]
fetched: "2026-10-21T08:59:14Z"
raw: "raw/docs/7/extend/comparison-of-contributed-modules/comparison-of-glossary-type-modules.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Comparison of Glossary-type modules

### Choosing between glossary-type modules

There are several glossary-type modules available, all of which are designed for slightly different needs. This page is here to help you choose which module you should probably be using, or if you should really write your own.

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
<th>Feature</th>
<th><a href="http://drupal.org/project/glossary">Glossary</a></th>
<th><a href="http://drupal.org/project/g2">G2</a></th>
<th><a href="http://drupal.org/project/glossify">Glossify</a></th>
<th><a href="http://drupal.org/project/lexicon">Lexicon</a></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<th colspan="5">Drupal-related</th>
</tr>
&#10;<tr class="odd">
<th>Drupal 8.x</th>
<td>-dev</td>
<td>-dev</td>
<td>-beta</td>
<td></td>
</tr>
<tr class="even">
<th>Drupal 7.x</th>
<td>-dev</td>
<td>-dev</td>
<td>-beta</td>
<td>Yes</td>
</tr>
<tr class="odd">
<th>Drupal 6.x</th>
<td>Yes</td>
<td>Yes</td>
<td>-beta</td>
<td>Yes</td>
</tr>
<tr class="even">
<th>Drupal 5.x</th>
<td>Yes</td>
<td>Yes<sup>*</sup></td>
<td></td>
<td>No</td>
</tr>
<tr class="odd">
<th>Drupal 4.7.x</th>
<td>-dev</td>
<td>Yes</td>
<td></td>
<td>No</td>
</tr>
<tr class="even">
<th>Drupal 4.6.x</th>
<td>-dev</td>
<td>No</td>
<td></td>
<td>No</td>
</tr>
<tr class="odd">
<th>Documentation</th>
<td><a href="http://drupal.org/node/196880">Handbook</a><br />
<a href="http://cvs.drupal.org/viewvc.py/drupal/contributions/modules/glossary/README.txt?view=markup">README.txt</a></td>
<td><a href="http://wiki.audean.com/g2/start">external to DO</a><br />
<a href="http://cvs.drupal.org/viewvc.py/drupal/contributions/modules/g2/README.txt?view=markup">README.txt</a></td>
<td><a href="http://drupalcode.org/project/glossify.git/blob/refs/heads/6.x-3.x:/README.txt">README.txt</a></td>
<td><a href="http://drupalcode.org/project/lexicon.git/blob/HEAD:/README.txt">README.txt</a></td>
</tr>
<tr class="even">
<th>AJAX</th>
<td>No</td>
<td>Entry selector</td>
<td></td>
<td>No</td>
</tr>
<tr class="odd">
<th>Architecture</th>
<td>term-based</td>
<td>node-based</td>
<td>term&amp;node-based</td>
<td>term-based</td>
</tr>
<tr class="even">
<th>Services provided</th>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<th>Multiple glossaries on one site</th>
<td>Yes</td>
<td>No</td>
<td></td>
<td>Yes</td>
</tr>
<tr class="even">
<th>RSS feeds on entries</th>
<td>Yes, Drupal core</td>
<td>No</td>
<td></td>
<td>Yes, Drupal core</td>
</tr>
<tr class="odd">
<th>RSS feeds on additional vocabularies</th>
<td>No</td>
<td>Yes, Drupal core</td>
<td></td>
<td>No</td>
</tr>
<tr class="even">
<th>Classify entries using taxonomy</th>
<td>No</td>
<td>Yes, Drupal core</td>
<td></td>
<td>No</td>
</tr>
<tr class="odd">
<th>Commenting on entries</th>
<td>No</td>
<td>Yes, Drupal core</td>
<td></td>
<td>No</td>
</tr>
<tr class="even">
<th>Private editorial information</th>
<td>No</td>
<td>Yes</td>
<td></td>
<td>No</td>
</tr>
<tr class="odd">
<th>Feature blocks</th>
<td>Search glossary<br />
<br />
Random / Term of the Day</td>
<td>alphabar<br />
<br />
latest<br />
<br />
top<br />
<br />
random<br />
<br />
word of the day</td>
<td></td>
<td>Random term block</td>
</tr>
<tr class="even">
<th>XML-RPC services provided</th>
<td>No</td>
<td>alphabar<br />
<br />
latest<br />
<br />
top<br />
<br />
random<br />
<br />
word of the day</td>
<td></td>
<td>No</td>
</tr>
<tr class="odd">
<th>Security</th>
<td>Drupal core</td>
<td>Drupal core<br />
<br />
XML-RPC access control<br />
<br />
XML-RPC throttling</td>
<td></td>
<td>Drupal core</td>
</tr>
<tr class="even">
<th>Alphabar maintenance</th>
<td>automatic</td>
<td>manual</td>
<td></td>
<td>automatic</td>
</tr>
<tr class="odd">
<th>Content filtering</th>
<td>automatic</td>
<td>dfn elements</td>
<td></td>
<td>automatic</td>
</tr>
<tr class="even">
<th>Performance</th>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<th>Memory needs/number of entries</th>
<td>proportional</td>
<td>constant</td>
<td></td>
<td>proportional</td>
</tr>
<tr class="even">
<th>Speed on small glossaries</th>
<td>faster</td>
<td>slower</td>
<td></td>
<td>faster</td>
</tr>
<tr class="odd">
<th>Speed on large glossaries</th>
<td>slower with size</td>
<td>remains constant</td>
<td></td>
<td>slower with size</td>
</tr>
<tr class="even">
<th>Themeability</th>
<td>search form<br />
<br />
node overview</td>
<td>Drupal core node themeing<br />
<br />
Independent themeing for all 5 feature blocks<br />
<br />
Independent themeing for all parts of a term definition</td>
<td></td>
<td>overridable tpl files for all output</td>
</tr>
<tr class="odd">
<th>Translation template supplied</th>
<td>Yes</td>
<td>No</td>
<td></td>
<td>No</td>
</tr>
</tbody>
</table>

\* <sub>*G2's support for 5.x is intended as a bridge from 4.7 to 6.x.*</sub>

Obviously, in all cases, a "No" actually means: "roll your own", as in all Open Source software.

### Rationale for G2 specificities

G2 is not intended as a direct replacement for the glossary module already available with Drupal for quite some time now.

A more detailed [comparison for choosing a glossary-type module](http://wiki.audean.com/g2/choosing) can be found at audean.

- Optimization for large glossaries: this is the need expressed by OSInet, which funded development, to support its 5000+ term glossary of computing, for which glossary.module, even when coupled with flexinode to bind blob content to terms, is not really efficient enough.
- Single glossary: multiple glossaries were not necessary to the initial sponsor
- Explicit linking to terms with dfn elements:
  - limits system workload
  - allows invisible marking of entries made of other entries. Think: XML-RPC, points to XML and to RPC with glossary.module and various wiki filters, but can point to "XML-RPC" with G2. Wrapping XML-RPC in quotes is necessary to allow linking to this entry in glossary, but the quotes remain visible, degrading the UI.
  - allows redactor-level choice of:
    - whether to link to an entry: Glossary typically links if the term matches, which is not always meaningful ("and" can be present in a glossary and you don't want "and" to be linked from in all nodes on the site).
    - where to link to an entry: glossary allows only a predefined set of positions (first, last or all matches).
- nodes vs terms: this is the most salient difference.
  - Using custom node types in G2 allows large definitions, with the complete Drupal feature set for nodes.
  - Using terms (glossary.module) allows definitions to be bound to custom nodes instead of being nodes on their own.
- Alphabar maintenance: large glossaries will, most of the time, use all available initials, so the processing cost of maintaining it is not justifiable.

### Glossary Design

- Customizable

- - Administrator options.

  - - Glossary display.

    - Alphabet / Alphabar.

    - Input Formats.

    - - Indicator style.
      - Link type.
      - Choice of HTML elements.
      - Term matching flexibility.

  - Liberal CSS usage.

  - Multiple glossaries.

  - Add-on modules.

- Taxonomy options.

- - Related terms link to each other.
  - Synonyms will filter the same.

- Drupal filter. Cacheable.

- Translation template provided.

The Glossary module has largely been designed by its users. Many, if not most, of its features have been added and refined by the input of the community. It is actively maintained and there have been performance efforts to make sure it runs as fast as possible. Considerable work has been done to make sure that i18n (internationalization) can be effectively used with Glossary.

Glossary uses Taxonomy to define its terms. While most sites have a smaller glossary than the one G2 was designed for, there are also sites with larger glossaries. The ability to handle multiple vocabularies as glossaries gives Glossary additional flexibility.

The Glossary module acts as a Drupal filter, locating terms within administrator-selectable content and adding additional HTML to them to show or (optionally) link the term's definition to the end-user as they view the content. The terms may be marked with a superscript or icon that links to the term or the term may be converted to an "acronym," "abbr," "cite," or "dfn" element with browser help tips. If the [Hovertips and Clicktips](http://drupal.org/project/hovertip) module is installed, it may be used to provide hovertips. There are also three mechanisms for marking a section of the content to not be filtered. Matching of terms may be selected as whole words or substrings, and may be either case-sensitive or not.

Since Glossary filters content, the first time a piece of content is shown, there will be a small delay while the filtering is done. The filtered content is then cached, so the next time, the filtering is unnecessary and the delay does not occur.

When a user clicks on a linked term, they will go to the entire glossary or the individual term, depending on which option the administrator chose. When displaying the entire glossary, there is an alphabar on top, which fills in automatically. The administrator may define his/her own alphabet for those who use some language other than English. The terms are then organized by the first letter of the term's name. Each section may be separated by a CSS-themable separator. At the bottom of the display, if the user has the appropriate permissions, are shortcut links to the vocabulary and module settings pages.

Within the glossary display, each term may be followed by a link that will initiate a search for the term, if the search module is enabled. For those who have the proper permission, there will also be a link to edit the term itself.

The type of glossary indicator that is used is specified for each input format, so, for example, "Filtered HTML" may use a superscript type of indicator, while "Full HTML" may use a hovertip. Additionally, each input format also selects which vocabularies are to be used. So one may, again for example, specify that "Filtered HTML" filter for Bible verses, while "Full HTML" filters for technical terms.

Since Glossary is taxonomy-based, that opens the range of taxonomy-based modules to work together. For example, [Taxonomy Image](http://drupal.org/project/taxonomy_image) may be used to show images for the terms and [Taxonomy Delegate](http://drupal.org/project/taxonomy_delegate) may be used to delegate vocabulary maintenance to sub-administrators or editors.

### Lexicon

The Lexicon module started out as a fork of the Glossary module for Drupal 6.x improving the output to be XHTML strict compliant for use in a project for the Dutch government. Soon after the release of Drupal 7.0 a 7.x version of the module was released and has been improved since then.
