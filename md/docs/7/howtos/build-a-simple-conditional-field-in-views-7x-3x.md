---
title: "Build a simple conditional field in Views 7.x-3.x"
source_url: "https://www.drupal.org/docs/7/howtos/build-a-simple-conditional-field-in-views-7x-3x"
page_type: page
last_updated: "Last updated on 25 January 2018"
published: "2013-03-06T13:11:05+00:00"
modified: "2018-01-25T23:35:03+00:00"
breadcrumb: ["Drupal 7", "Site building and development HowTos for Drupal 7"]
fetched: "2026-10-21T08:00:31Z"
raw: "raw/docs/7/howtos/build-a-simple-conditional-field-in-views-7x-3x.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Build a simple conditional field in Views 7.x-3.x

You can make conditional fields in views without using additional modules like Views PHP.

In this example, we make the path for a node title automatically link to the node path, to a URL link or to a file path, depending on the content type. Note that this is just an illustration of a concept which can be changed depending on the requirements.

### Example

|           |                                |
|-----------|--------------------------------|
| Type      | Paths                          |
| Node path | /content/node-title            |
| URL       | <http://www.drupal.org>        |
| File path | /sites/all/files/this-file.pdf |

### Create the content types

1.  Create three content types: News, News URL, News PDF
2.  For each content type, create the following fields:
    - News: title, body
    - News URL: fields: title, field_url (link field)
    - News PDF: fields: title, field_pdf (file field)

### Add Sample Contents

- News: Node Title (title), Some Text.. (body)
- News URL: URL Title (title), <http://www.drupal.org> (field_url)
- News PDF: PDF Title (title), upload a pdf file (field_pdf)

### Configure Views

1.  Create a view, block or page
2.  Add the following fields: Content: Title, Content: URL, Content: PDF
3.  Add additional fields: Global: Custom Text, Content: Path
4.  Arrange the above fields to:
    - Content: PDF
    - Content: URL
    - Content: Path
    - Global: Custom Text
    - Content: Title

### Configure fields

1.  Content: PDF
    - Exclude from display
    - Formatter: URL to path
    - check hide if empty
2.  Content: URL
    - Exclude from display
    - Formatter: URL, as plain text
    - No Result Behavior put \[field_pdf\]
3.  Content: Path
    - Exclude from display
    - Rewrite Results, check Use absolute link (begins with "http://")
4.  Global: Custom Text
    - Exclude from display
    - Text: put \[field_url\]
    - No Result Behavior put \[path\]
5.  Content: Title
    - Uncheck **Link this field to the original piece of content**
    - Rewrite Results: check **Output this field as a link**, on path, put \[nothing\], check **Use absolute path**

The output should be:

- [Node Title](http://example.com/content/node-title)
- [URL Title](http://example.com)
- [PDF Title](http://example.com/sites/all/files/this-file.pdf)
