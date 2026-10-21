---
title: "FAQ using Views"
source_url: "https://www.drupal.org/docs/7/howtos/faq-using-views"
page_type: page
last_updated: "Last updated on 25 January 2018"
published: "2011-07-11T19:55:43+00:00"
modified: "2018-01-25T23:54:22+00:00"
breadcrumb: ["Drupal 7", "Site building and development HowTos for Drupal 7"]
fetched: "2026-10-21T08:04:23Z"
raw: "raw/docs/7/howtos/faq-using-views.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# FAQ using Views

Here is a recipe for creating an FAQ using nodes and Views. I did this in Drupal 7 but it should work in D6 also, although some steps will be different due to the new D7 user interface.  
I am using the Administration Menu module with the Administration menu Toolbar style submodule enabled, and my directions to navigate to pages reflect that.  
You will need the Token module installed.

## Step 1: Create the FAQ content type

![FAQ Content Type](/files/FAQ_Content_Type.png)

1.  Go to Structure -\> Content types -\> Add content type.
2.  Give the content type the name "FAQ".
3.  Change the title field label to "Question"
4.  I recommend unchecking "Promoted to front page" and "Display author and date information" and disabling comments.
5.  Save the content type and go to "Manage fields"
6.  Delete the body field.
7.  Add a new field called "Answer" of type long text (i.e., an HTML text area)
8.  Here are the settings I used for the Answer field:
    - Check required field
    - 20 Rows
    - Text processing: Filtered text
    - Number of values: 1
9.  If you want to be able to control exactly what order the FAQs are shown in, you could also add an integer field called "Sort order".

## Step 2: Create some FAQ nodes

![FAQ Nodes](/files/FAQ_Nodes.png)

1.  Go to Content -\> Add content -\> FAQ.
2.  Fill in the question and answer fields and save.

## Step 3: Create Views

![FAQ Views](/files/FAQ_View.png)  
Now we will create two views (actually two displays in one view): one for the table of contents and one for the full-body list of the FAQs. One display will be a page and the other can be an attachment or a block. I found using a block makes it easier to apply the desired CSS, since using an attachment marks up the page as one view inside another.

### Initial view configuration

Here is where there is a difference between D6 and D7. In Drupal 7 I needed to make the table of contents the block view and make the full-body faq list the page view since the block is rendered above the page display. I believe (but haven't confirmed) in D6 you would do the reverse: the table of contents would be the page view.

1.  Go to Views-\> Add new view
2.  On the configuration page that takes you to:
    1.  Call the view "FAQ".
    2.  Show **content** of type **FAQ** sorted by **(your desired sort order)**
    3.  Create a page
        - Page title: Frequently asked questions
        - Path: faq
        - Display format: **HTML list** of **fields**
        - Items to display: (leave blank)
        - Create a menu link (if desired) in the desired menu (probably Main) with Link text: FAQ
    4.  Create a block
        - Block title: (Title of your choice)
        - Formatted list of titles
        - Items per page: (leave blank)
    5.  Continue and edit

### Table of contents display configuration

This will create a list of the questions that link to the full FAQ node farther down on the page.  
In the "Fields" section

1.  Add field: Global: View result counter
2.  Check "Exclude from display"
3.  Starting value: 1
4.  Edit field: Title
5.  Uncheck "Create a label"
6.  Under "Rewrite results", check "Output this field as a link" and set link path as faq#\[counter\]

In Drupal 6 the result counter field will need to come before the title.

### Full-body display

In the "Fields" section

1.  Add field: Global: View result counter
2.  Check "Exclude from display"
3.  Starting value: 1
4.  Edit field (or create if not there): Title
5.  Uncheck "Create a label"
6.  Under "Rewrite results", check "Rewrite the output of this field" and set Text to \<a name="\[counter\]"\>\[title\]\</a\>
7.  Add field: Content: Answer
8.  Uncheck "Create a label"
9.  (Optional: link back to top of page) Add field: Global: custom text
10. Uncheck "Create a label"
11. Set Text to \<a href="faq#main-content"\>Back to Top\</a\>

## Step 4: Configure block

1.  Go to Structure-\>Blocks
2.  Find your new block and move it into the Content section (assuming your theme has a region called "content")
3.  Show the block only on the lists pages: faq
4.  Save block
