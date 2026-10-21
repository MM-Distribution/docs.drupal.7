---
title: "Making your theme semantically correct"
source_url: "https://www.drupal.org/docs/7/theming/tools-and-best-practices/making-your-theme-semantically-correct"
page_type: page
last_updated: "Last updated on 13 August 2018"
published: "2006-01-10T09:35:59+00:00"
modified: "2018-08-13T13:57:56+00:00"
breadcrumb: ["Drupal 7", "Theming Drupal 7", "Tools and best practices"]
fetched: "2026-10-21T08:54:51Z"
raw: "raw/docs/7/theming/tools-and-best-practices/making-your-theme-semantically-correct.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Making your theme semantically correct

Semantic (X)HTML elements convey meaning. Semantic markup combined with CSS is also the primary way to separate content from presentation. In essence semantic HTML is HTML minus the presentational HTML elements and attributes.

In the bad old days we used HTML for presentation, such as `font`, `strike` and `u` elements. The problem was that those elements didn't tell us anything about the meaning of the content.

### POSH

POSH is the acronym for Plain Old Semantic HTML. POSH gives us an easy to remember acronym that encapsulates the simplicity, best practice and benefits of using semantic markup. You can learn more about [POSH on microformats.org](http://microformats.org/wiki/posh).

### Humans vs Machines

Semantic markup is primarily for machines. While machines may be able to derive meaning from text, they can do this more easily by understanding the context in which the text appears. That context is semantic HTML.

### Validation

It is a primary tenet of semantic (X)HTML that markup is valid.

Online validators look at the headings in the order they are in the content as delivered to the browser. You can place content in one order then use CSS to display the content in another order. The validator will look at the original order.

A common problem is to have a left hand sidebar before all other content and to have the sidebar start with an h2 element. The h2 appears before the h1 for the site name. The theme will fail WCAG (WAI) validation at level AA<a href="#1" id="fn1">1</a>.

### Accessibility

Place content first (content source ordering) then the sub headings and sidebars. In this structure, you can make the page title the h1.

For the visually impaired, the page title is more important than the site name on every page except the home page. When they search for example, they want a site that starts off by saying example.com. When they search for Orange and chilli salmon, they want pages titled Orange and Chilli Salmon, not example.com.

Visually impaired people want the summary in the first paragraph and as the first content downloaded so they can find out if they are at a useful page. Some search engines place a greater weight on the first paragraph in the page. Improvements for visually impaired people should help with SEO. Your mileage may vary. Do not try this at home without adult supervision. Etc. Etc.

### h1 as Site title or Page Title

The [old HTML standard](http://www.w3.org/TR/REC-html40/struct/global.html#h-7.5.5) has an example showing the page subject as the h1 title. The HTML standard says A heading element briefly describes the topic of the section it introduces.. A page title introduces the page, not the site, on every page except the home page.

It is therefore legitimate to use h1 for the site name on the home page and h1 for the page title on other pages. If the home page uses the site name as the page title then it briefly describes the topic ... it introduces.

Drupal allows you to use a page-front.tpl.php file or use of the \$is_front variable in conditional statements. Many Drupal themes make use of this to show the Site name in an h1 on the homepage (and/or other pages with no page title) and in a div or span for all other pages.

## POSH Reference

This is a list of semantic (X)HTML elements with notes on usage. Please feel free to add to this or debate my explanations.

### Block Elements

div

Provides meaningful divisions. Frequently nested and used to group related elements and content such as headers, sidebars, content area and footers.

h1-h6

The six levels of headings are used to introduce and describe sections of content. It is common practice to use only one h1 element on any one page—a page has one main heading and many sub sections with h2 and/or h3 headings.

p

The paragraph element is used to markup and delineate a block of text.

blockquote

Indicates a large or substantial quote.

address

Indicates contact information for a document or a major part of a document. May be used in conjunction with the [hCard microformat](http://microformats.org/wiki/hcard-examples).

### List Elements

ul, ol, li

Lists are used to represent grouped information best represented as a list. Often used to markup menus (a list of links). ol represents ordered list while ul represents unordered lists. li represents a single list item. Lists can be nested.

dl, dd, dt

Indicates a list of terms (dt) with their accompanying definitions (dd). Often used to markup FAQ's.

### Inline Elements

a

Typically used with an href attribute to indicate an external resource or an anchored location within the same document.

abbr

Indicates a shortened form of a term or phrase. Often attributed with a title.

acronym

Used to markup acronyms, initialisms, and alphabetisms. Often attributed with a title.

em

Used to indicate emphasis. Emphasized text is in some way more significant than the text surrounding it.

strong

Used to indicate stronger emphasis. Similar to em but stronger.

cite

Indicates bibliographical information, personal quotations or references.

code

Indicates a sample of computer programming code.

dfn

Defines the first instance of a term in a document. The semantic value of dfn is debatable.

del

Indicates information which has been deleted from a document. Semantic replacement for the deprecated strike element.

ins

The opposite of del. Indicates inserted text added during revisions.

samp

Sample output from computer programs or scripts. Sample output may or may not be code.

span

Generic inline element used where a semantic element would be inappropriate. Span elements are considered to have no semantic value.

q

Indicates an inline quotation.

kbd

Indicates text to be entered by the user. Rarely used, but useful in circumstances where you are demonstrating the use of a program, along with code and samp.

sub, sup

Superscripting and subscripting of text. Often used to indicate footnote references.

var

Along with code, samp, kbd, the “variable” element indicates a variable (or program argument).

### Form Elements

label

The label element is used to describe form elements.

### Table Elements

table

Used to markup indicates tabular data.

thead

Defines a header region for a data table, which would normally contain the headers (th) for each column.

tfoot

Defines a footer region for a data table, which should include information referential to the columns of data.

tbody

The content region of a table.

caption

Describes the table. Essentially a heading for the table.

th

Table heading for rows columns. Indicate the type of information within the row or column.

td

A data cell, in which content is placed which corresponds to both the headers for the row and column.

View a [default rendering of XHTML structural tags](http://adaptivethemes.com/xhtml-elements-browser-test.html) (for browser comparison).

Footnotes:

<http://www.w3.org/TR/WCAG10-HTML-TECHS/#document-headers> [↑](#fn1)
