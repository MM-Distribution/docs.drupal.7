---
title: "Control/modify display settings (author and date) on posts"
source_url: "https://www.drupal.org/docs/7/howtos/controlmodify-display-settings-author-and-date-on-posts"
page_type: page
last_updated: "Last updated on 17 April 2020"
published: "2011-02-25T15:26:27+00:00"
modified: "2020-04-17T09:19:46+00:00"
breadcrumb: ["Drupal 7", "Site building and development HowTos for Drupal 7"]
fetched: "2026-10-21T08:01:33Z"
raw: "raw/docs/7/howtos/controlmodify-display-settings-author-and-date-on-posts.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Control/modify display settings (author and date) on posts

When you create an article or page in Drupal 7, by default, it displays Author and Date information after the title, something like:

*published by admin on Thu, 02/17/2011 - 11:08*

If you don't want to see this information, disable the **Display Settings** option for the corresponding content type with these steps:

1\. Log-in as Admin and choose Structure, Content types and click edit (under Operations) for the corresponding content type (e.g. Article).  
2. Click **Display Settings** and un-check **Display author and date information** check box.  
3. Save settings by clicking the **Save Content Type** button.

Now, the author and date information will not be displayed for the corresponding content type.

How about if you want to display the date information but not the author information, e.g. you want to see something like:

*Posted: February 23, 2011*

To accomplish this,

1\. Enable Display Settings for the corresponding content type.  
2. Edit the node.tpl.php file of the corresponding theme you are using, e.g. themes\bartik\templates\node.tpl.php and located the following command:  
`print $submitted; `

3\. Now replace this command with the following code:  
`// print $submitted;`  
`if ($submitted) {`  
`echo "Posted: " . date( "F j, Y",$node->created);`  
`} `

4\. Save the file and you should see the submitted information in the desired format. Of course, you can use a different date format or add additional node details.

## Modules

Modules that let you perform the operations above without programming skills:

- [Display Suite](/project/ds) provides separate display options for node Author and Date, under the Manage display settings of a content type
- [Submitted By](http://drupal.org/project/submitted_by) adds a fieldset to your node edit form called Appearance that lets you use the [token](https://www.drupal.org/project/token) module to insert the text you want to display.
