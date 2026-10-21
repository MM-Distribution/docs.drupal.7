---
title: "Guidelines for taxonomy design"
source_url: "https://www.drupal.org/docs/7/organizing-content-with-taxonomies/guidelines-for-taxonomy-design"
page_type: page
last_updated: "Last updated on 22 November 2017"
published: "2006-08-30T22:28:14+00:00"
modified: "2017-11-22T17:30:51+00:00"
breadcrumb: ["Drupal 7", "Organizing content with taxonomy in Drupal 7"]
fetched: "2026-10-21T07:09:01Z"
raw: "raw/docs/7/organizing-content-with-taxonomies/guidelines-for-taxonomy-design.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Guidelines for taxonomy design

In small sites, the taxonomy scheme is usually obvious. But in larger projects -- especially when experts are categorizing content to be read by laypeople -- good taxonomy design can be the difference between an intuitive site and an information architecture nightmare. The importance of good taxonomy design has only increased with the rise of the [Views module](/project/views), which relies on powerful, taxonomy-based Filters.

## General Rules

**1.** Unless a vocabulary is well-known to all anticipated users -- for example, an alphabetical list of world countries -- keep it below 30-40 terms.

**2.** Use parent-child relationships with caution. If your taxonomy relies on these structures, think about dividing up the vocabulary. An unwieldy parent-child scheme is often a sign of poor design.

**Example**

An online art shop has taxonomized its products as follows:

- Europe
  - Lapp
  - Sami
  - Celtic
- Australia
  - Aboriginal

Even though this accurately shows how the shop classifies its items, its insistence on many small categories prevents a user from saying, "show me some European art."

Multiple-select is one way around this, but not the best way. It's better to use *two vocabularies*: one for region, one for culture. Make them both multiple-select, and our art collector can now ask: "What have you got which is Lapp, or Celtic or Chinese?"

**3. Too many terms**

"Perfect" taxonomies are always too complex and you need to fight to make them more manageable (especially if you have just cut up a few parent-child vocabularies into several smaller ones).

The advantage of [Views](/project/views) is that the multiple taxonomy terms start to build context, and that can be captured by Views.

There are not many sites that ever need to show more than 3-4 filters to users, even if there are 5-6 more hidden ones.

Plus, building them into structure adds even more granularity.

**Example**

A site for all the small towns of America, where people are interested in their little town's stuff, using [Book](/handbook/modules/book) for basic structure.

Top level - states - 50 items  
Off each state - counties  
Off each county - settlements

Click the named settlement and get a Views list with filters for news, culture and announcements.

(Hidden filters in the Views filter by State/County/Settlement)

Highly non scary - any users can use that to get what they need.

**4. Clients are not experts on taxonomy, not even their own**

Taxonomy is a communications issue and if there is a budget for the site it's always worth running it past an outsider - but note that they will need to get to understand the purpose of the site and also to an extent the jargon of the subject.

This normally requires at least one decent face to face meeting to force the client to decide what is important, and what can be cut out. Trust me, these decisions will have to be made, and if they are not, then people are probably not thinking carefully enough.

**5. Taxonomy creates legacy issues - so get it right!**

Once you have a load of tagged data, it's hard to make changes to taxonomy structures (apart from adding terms) without rendering existing nodes much harder to find. Trust me, *no one* will go back and edit existing data, not in real life, unless there is massive funding for that purpose.

**6. Taxonomy is trial and error**

It should be the first thing you do on a site, but by adding test data you'll find flaws, and refine and eventually go live with something that works. In between times you solved the CSS and templating...

I once spent 3 days testing different ways to classify cars for one site - the makes/models complexity of past 20 years is a nightmare, and there are several ways to do it, all of which work, some are more user friendly than others!
