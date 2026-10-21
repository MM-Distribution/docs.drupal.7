---
title: "Add a term to a vocabulary"
source_url: "https://www.drupal.org/docs/7/organizing-content-with-taxonomies/add-a-term-to-a-vocabulary"
page_type: page
last_updated: "Last updated on 22 August 2016"
published: "2005-05-23T00:27:33+00:00"
modified: "2016-08-22T20:50:05+00:00"
breadcrumb: ["Drupal 7", "Organizing content with taxonomy in Drupal 7"]
fetched: "2026-10-21T07:08:15Z"
raw: "raw/docs/7/organizing-content-with-taxonomies/add-a-term-to-a-vocabulary.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Add a term to a vocabulary

Once you have finished defining the vocabulary, you may populate it with terms using Add. Add terms to a vocabulary by navigating to admin/structure/taxonomy/\[your-vocabulary-name\]/add. From there, Drupal will prompt for:

- **Term name** (Required) -- The name for this term. Example: Technology.
- **Description** (Optional) -- Description of the term (this item may be used by some modules and feeds).

Advanced options:

- **Parents** (Optional): Select the term(s) under which this term is a subset.
- **Related terms** (Optional, D6 only): Choose any terms that are related to the one you are creating.
- **Synonyms** (Optional, D6 only): Enter synonyms for this term, one synonym per line. Synonyms can be used for variant spellings, acronyms, and other terms that have the same meaning as the added term, but which are not explicitly listed in this thesaurus, i.e. unauthorized terms (this item not used by many Drupal modules).
- **Weight** (Optional): The weight is used to sort the terms of this vocabulary; by default they will be sorted alphabetically.
- **URL Alias** (Optional, D7): Default is "/taxonomy/term/" but here you can specify an alias like "term1" and the final url will be "/term1".
