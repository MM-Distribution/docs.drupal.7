---
title: "About taxonomy"
source_url: "https://www.drupal.org/docs/7/organizing-content-with-taxonomies/about-taxonomies"
page_type: page
last_updated: "Last updated on 24 May 2018"
published: "2010-04-18T23:15:53+00:00"
modified: "2018-05-24T15:45:26+00:00"
breadcrumb: ["Drupal 7", "Organizing content with taxonomy in Drupal 7"]
fetched: "2026-10-21T07:07:43Z"
raw: "raw/docs/7/organizing-content-with-taxonomies/about-taxonomies.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# About taxonomy

[Taxonomy](http://en.wikipedia.org/wiki/Taxonomy) is the practice and science of classifying things. In Drupal, the Taxonomy module allows you to classify your website content, and it can be an important part of your information architecture.

## Planning taxonomy

The first step in establishing a taxonomy is creating a new vocabulary. Next you provide the terms that fall within that vocabulary. The arrangement can be "flat," as in a tagging system, or hierarchical, with parents and children.

Here's how you might create a taxonomy for a site arranged by musical genre:

Vocabulary = Music  
Term = Classical  
Sub-term = Concertos

Sub-term = Sonatas

Sub-term = Symphonies

Term = Jazz  
Sub-term = Swing

Sub-term = Fusion

Sometimes you will want to create a "controlled vocabulary," where content authors can assign terms that have been predetermined. If so, you will need to add those terms to your vocabulary in advance.

An alternative model for organizing information is the use of "tags." User-defined tags can be added to Drupal content on the fly. In **Drupal 7**, a ready-to-use "Tags" vocabulary is included by default, so users can immediately begin adding tags to their content.

By using multiple vocabularies it is possible to classify an individual node in many ways. For example, a node representing a musical work might have a genre vocabulary and a time-period vocabulary (including terms such as: seventeenth century, eighteenth century). The node might also be identified using a vocabulary term, such as "sonata". Adding a vocabulary for "composers", might lead to the following combination of terms: as an "early-eighteenth-century" "sonata" by "Bach", and it could be located by any of these three terms.

### Taxonomy principles

- Each vocabulary consists of a set of terms.
- A site can have an unlimited number of vocabularies.
- Each vocabulary has an associated ID number. Each taxonomy term has an associated ID number.
- Each vocabulary can contain an unlimited number of terms.
- Within a vocabulary, terms can be ordered into hierarchies. All vocabularies can be arranged into a hierarchy without taking additional steps, if you find this useful.
- In Drupal 7, you don't need to predefine the type of vocabulary in order to create a "tagging" vocabulary. In Drupal 6, vocabularies should be designated as "free tagging" or "tags" and "multiple select" should be chosen (in Drupal 6).
- In Drupal 6, vocabularies can be set to allow terms to have *related terms*. This function is similar to "See also" in a dictionary. In Drupal 7, this can be replicated by adding a "term reference" field to the vocabulary. For more on the use of Fields with Taxonomy, see [the handbook on Field UI](http://drupal.org/handbook/modules/field-ui).
- In Drupal 6, vocabularies define whether users may attach only a single term to a node or whether users may attach multiple terms to a node. In Drupal 7, this is controlled in the settings of each "term reference" field.

## Using the Taxonomy module

In Drupal 7, the Taxonomy module is turned on, by default. In earlier versions of Drupal, you can enable the Taxonomy module on the *modules* page (*Administer \> Site building \> Modules*).

- In **Drupal 7** settings for the Taxonomy module can be found at *Administer \> Structure \> Taxonomy*
- In **Drupal 6** settings for the Taxonomy module can be found at *Administer \> Content Management \> Taxonomy*

### Working with Taxonomy

Vocabularies are managed on the *Taxonomy* page.

- In **Drupal 7**, it's found under *Administration \> Structure* (i.e., <http://yoururl/admin/structure/taxonomy>)
- In **Drupal 6**, it's found at *Administer \> Content management \> Taxonomy* - (i.e., <http://example.com/admin/content/taxonomy>).

#### Adding a vocabulary

- Choose a name for your vocabulary.
- Give your vocabulary a description. Modules may use this description in different ways. (For example, a module may show the description when users hover over a link.)
- In Drupal 7, vocabularies are only assigned to content types through the addition of a "term reference" field for that content type. One step in setting the "term reference" field will be to choose the vocabulary from which the term will be chosen. In Drupal 6, you can tie your vocabulary to particular content type: "story" or "book page". Once you've assigned a vocabulary to a content type, content creators will be able to choose to assign a term from that list to their content.
- You can also give your vocabulary "help text" to help your users choose. Note that when creating a new content type, existing vocabularies do not have the new content type selected; you need to edit them to add the type.
- Vocabularies can have hierarchies of terms. In Drupal 7 and 6, you simply arrange items to create a hierarchy.
- In Drupal 6
  - You can allow "related terms."
  - If you allow "free tagging," when your users create content they can make up their own terms as they go along, instead of having to choose from a list.
  - By choosing "multiple select," you can allow your users to put a post into more than one category at once by tagging it with more than one vocabulary term.
  - You may also require that when your users create content of a certain "content type" they assign at least one of this vocabulary's terms.
  - You can decide the order in which your vocabulary will appear in lists by assigning a "weight" to it. A term that is weighted 2 is "lighter" than a term that is weighted 6 so the term weighted 2 will appear higher on the list.
- Finally, you can delete the vocabulary altogether, thereby also deleting all its terms, but not the nodes to which they were assigned.

#### Working with Terms

To view or manage the terms of each vocabulary, click on its *list terms* link. On the *list terms* page you can edit each term by clicking the *edit* link. Now, on the *edit term* page you have several kinds of choices.

- You can put the term in its place in the hierarchy by choosing the term's "parent" .
- You must assign your term a name as a "nameless term" does not exist.
- In Drupal 6
  - You can list synonyms for your term and this creates what is known as a "thesaurus".
  - You can select from this vocabulary one or more terms with which you'd like your term to be related (select multiple terms by using the standard conventions of your operating system, like shift-click and control-click).
- You can decide the order in which your term will appear in lists by assigning it a "weight".
- You can delete a term altogether.

To add new terms to your vocabulary, click its *add terms* link. The *list terms* page also has an *add terms* link that does the same thing. When you add new terms you have the same options as when you edit them.

### Using Categories in Menus

The menus on your site can call for items that match specific taxonomy terms. To create a menu using Taxonomy, follow these steps:

- Find the number given to your taxonomy term (to find the term number, go to the *categories* page, *"list terms"* for the category to which your term belongs, and hover over the term. You'll see the number.)
- Go to the *menus* page (*Administer \> Site building \> Menus*)
- Select *Add item,*
- When you fill in the *Path* field you add your term as follows:  
  `taxonomy/term/1`  
  If the term "Sonatas" is term 1, this would call for all the nodes of that category.

In Drupal 6, you could also combine terms or add a *depth* parameter to the path. Note that the following does *not* work in Drupal 7:

- If the term "Bach" is term 2, this could call for only those sonatas written by Bach:  
  `taxonomy/term/1,2`
- Or if Brahms is term 3 and this will call for everything that has to do with either Bach *or* Brahms:  
  `taxonomy/term/2+3`
- If you are using a *hierarchical* taxonomy, and want all nodes tagged with child terms to show up also, you can create an URL link like `taxonomy/term/2/2` where the second parameter is the *depth* that the tree will be recursed into, or `taxonomy/term/2/all` for *all* child terms.

(In Drupal 7, you can no longer specify paths such as "taxonomy/term/1,2", "taxonomy/term/1+2","taxonomy/term/2/2" or "taxonomy/term/2/all". Function taxonomy_term_page (Drupal 7) does not parse the string as it did in Drupal 6.)

Several [contributed modules](/project/Modules/category/71) make powerful use of the categories (taxonomy) module, exploiting and extending what it can do.
