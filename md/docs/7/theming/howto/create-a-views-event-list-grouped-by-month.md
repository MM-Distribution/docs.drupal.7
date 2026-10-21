---
title: "Create a Views event list grouped by month"
source_url: "https://www.drupal.org/docs/7/theming/howto/create-a-views-event-list-grouped-by-month"
page_type: page
last_updated: "Last updated on 16 January 2019"
published: "2009-03-02T05:30:45+00:00"
modified: "2019-01-16T14:43:56+00:00"
breadcrumb: ["Drupal 7", "Theming Drupal 7", "Theming HowTos"]
fetched: "2026-10-21T08:48:26Z"
raw: "raw/docs/7/theming/howto/create-a-views-event-list-grouped-by-month.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Create a Views event list grouped by month

Views has a feature called *grouping*, which allows you to split a list of results into arbitrary categories. Basically, if several items fall under the same category then they'll form their own list. For grouping to work though, your view must have a couple of fields, luckily you can use any available field for your groups.

Drupal 6  
Modules used:

- [CCK 6.x-2.x](/project/cck)
- [Views 6.x-2.x](/project/views)
- [Date 6.x-2.x](/project/date)

Drupal 7

- [Views 7.x-3.5](/project/views)
- [Date 7.x-2.6](/project/date)

## Create a content type for your events

Create a new content type (if D6 use CCK) and name it *Event*. Add a new field named *Date* and choose *Date* as the type. Configure the field as you require.

## Create a new view

Using Views, add a view named *Events*.

Choose a style for the view, preferably *table*.

Add the fields *Node: Title* and *Content: Date*, these will be visible fields so configure them to look presentable.

Even though we just added the date field, we need to add it a second time so it can be used for grouping. This field should not be presented alongside the other fields, so in the settings check "Exclude from display" and set the label to *none*.

The reason we need a second field for the date is because we're going to modify its output to return only a month and year.

Now click on the settings icon for the *Style* option and under *Grouping field* select our hidden date field. Also **ensure that the *Use rendered output to group rows *and *Remove tags from rendered output *are both checked.******

You may also want to add a filter for *Node: Published* and *Node: Type*.

To Group by and display current and future dates only:

- add a filter criteria to filter on the "Date: Date (Node)"  filter.
- On the Configure extra settings for filter criterion Date:Date(node), set the Date selection form element to Text and Filter granularity to your desired setting, for future date/time, I usually set it to Day or Hour or Minute.
- Under the Date Field(s) section, select the Date field on the node that you want to filter by.
- Under the Configue filter criterion: Date: Date(node)
  - Set the Operator to "is greater than or equal to" and then select "Enter a relative date". 
  - in the Relative Date section, enter "now"
  - This should be done for both the Start Date and the End Date sections

If you preview the view you should notice that each node has been separated into its own group, and each group is headed with a unique date. Since the dates are all unique we don't get any actual groups.

What we need to do now is modify the hidden date field so it only returns the month and year.

Ensure your view has a page or block display type and save it.

## Override the date field output

There are two approaches that can be made: create a custom date format and custom date type or create a views field template. The first approach avoids the issue of adding an unnecessary template file to the theme directory and allows the user to set the date format in the UI. The second approach is a helpful intro into working with Views templates.

**Approach \#1: Custom Date Type**  
Add a new Date format under admin/config/regional/date-time/formats and for the Format string enter "F Y"  
Add a new Date type under admin/config/regional/date-time and select the new date format just created

In the *Events* view, select the Date field and change the value of *Choose how users view dates and times:* to your newly created date type. Now when you load the final view you should get a nice grouped list.

**Approach \#2: Custom Views Field Template**

To find out which file we need to copy for theming our field we need to click on the *Theme: Information* link, this gives us a list of potential file names for various parts of the view. From the list, find the identifier of our hidden field and look at the second suggested file name, in my case it's called: "*views-view-field--field-date-value-1.tpl.php*". Yours may or may not be different.

To use this file we need to copy the file named "views-view-field.tpl.php" from "sites/all/modules/views/theme" and paste it into our own theme directory. Immediately rename the file to the suggested file name above, include all the hyphens.

Open the new file and replace `<?php print $output ?>` with:

``` php
<?php print date('F Y', strtotime($row->node_data_field_date_field_date_value)); ?>
```

F = Month  
Y = Year

Now when you load the final view you should get a nice grouped list.

## Customizations

How to customise the date output: <http://php.net/manual/en/function.date.php>

How to change the look of the text: <http://v1.reinspire.net/blog/2005/09/15/css_font_styling/>

## Caution

If you wonder why your output is not grouping things together, disable Theme developer, and see if that helps.

In case it saves others from scratching their heads, here's something to note about this example:

The reason you write a template is that the grouping field does its comparison based on the output of the template rather than the raw data. This was apparently done to implement things like granular date grouping relatively easily.

One BIG side effect of this is that any tools that monkey with the output, say... THEME DEVELOPER ... will cause what seem like equivalent date strings to be different. More specifically, the output will be wrapped in a tag, that includes a thmr attribute that increments.
