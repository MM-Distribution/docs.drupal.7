---
title: "Build a Drupal 7 HTML5 Video Subtitling/Closed-captioning System"
source_url: "https://www.drupal.org/docs/7/howtos/build-a-drupal-7-html5-video-subtitlingclosed-captioning-system"
page_type: page
last_updated: "Last updated on 25 January 2018"
published: "2013-02-25T17:37:26+00:00"
modified: "2018-01-25T23:33:24+00:00"
breadcrumb: ["Drupal 7", "Site building and development HowTos for Drupal 7"]
fetched: "2026-10-21T08:00:16Z"
raw: "raw/docs/7/howtos/build-a-drupal-7-html5-video-subtitlingclosed-captioning-system.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Build a Drupal 7 HTML5 Video Subtitling/Closed-captioning System

## Overview

Why might you want to close-caption or subtitle video content on your site? Well, one reason for subtitling is to provide fully functional internationalization/localization capabilities. One of the many reasons Drupal is the CMS of choice is because of its robust multilingual support. If you are posting multilingual text content on your site, multilingual support can and should extend to all content, including video, through the use of subtitles.

Many visitors to your site—regardless of whether or not your content is internationalized—may use a screen reader or require the use of text captions where audio is used within a video to convey information. It is, therefore, a reasonable accessibility accommodation in many cases to provide closed captions where a video is an essential component of your site.

A third use case involves a site where a video is used to demonstrate a process in detail, but where an audio description is too expensive, time-consuming, or creates significant localization challenges. I have a site where I have hundreds of separate videos, all with stepwise descriptions for completing maintenance or troubleshooting procedures. I needed the non-technical end-user to be able to upload the video and add subtitle text in the node edit page.

As a note, I use the terms “captions” and “subtitles” interchangeably throughout this document. The only real difference is that subtitles usually denote language translations whereas captions denote audio transliteration. For my purposes, there is no difference.

The system I describe below will send, format, and output text information in the [WEBVTT](http://dev.w3.org/html5/webvtt/) format. Please take a look at the linked example from the W3C site; this is the format we will be using here. This is one of several captioning and subtitling formats available as of this writing. The HTML5 specification supports caption and subtitle output from the WEBVTT source through the `<track>` element. I will discuss this later.

Currently, there does not appear to be any existing modules or detailed processes for creating fieldable, scalable captions/subtitles within a Drupal site. The following text describes in detail how to create such a system using several modules with a few modifications to theme templates. I realize that these modifications are somewhat hackish and would probably be better executed through theme functions in a module; however, I don’t have the time or know-how at the moment to create such a module. If you do, please feel free to update this document and publish your code, or your approach, if different than the one I describe.

**Note:** The attached resource pack zip file contains a PDF of these instructions with screenshots, a text file with exported view code used here, and the two template files.

## Modules Used

I used a combination of several modules. You may be able to substitute other modules (video, for instance) to fit your needs. These worked for me. You may be able to make this work in Drupal 6; all three modules are available for D6 also.

- Video.js 7x-2.2
- Views 7.x-3.5
- Views Data Export 7.x-3.0-beta6

## Installation and Setup

### Create the Movie content type and the Content Container content type

1.  First, install, enable, and configure your modules. I did not use any particular configuration options for the Video.js module.

2.  Create a content type (see Figures 1a and 1b. **These are included in the PDF in the attached resource pack**) to hold your videos and captions/subtitles. Mine is called **Movie.**

    a.  Add a **File** field to hold your movie. Mine is called **Movie**. The widget will default to **File**. Save this field.

    b.  Use the default **Field Settings** when prompted. Click **Save Field Settings**.

    c.  On the field **Edit** page, specify the types of video you will be using in the **Allowed file extensions** box. I added mp4, mov, flv, f4v, ogg, 3gp, avi; these seem to cover most HTML5 use scenarios.

    d.  Click the **Manage Display** tab. For the **Movie** field, select **\<Hidden\>** for the **Label**. For **Format**, select **Video.js : HTML5 Video Player**.

    e.  Now add a new text field to the Movie content type, labeled **Time 1**. This will hold the time for the first subtitle. This is just a plain text field, with all of the default settings. When you have saved this, click the **Manage Display** tab.  Since the time field will only be used by Video.js to add the subtitles at the appropriate time, select **\<Hidden\>** for **Format**.

    f.  Repeat the above step (e), for as many subtitles as you anticipate using. I will use no more than 25. **Note**: When adding the text field, you may notice you have the option to add an unlimited number of values**. Do not do this**. We need to create distinct fields so we can order them and reference them separately through a view, later.

    g. Add another text field to the Movie content type, with the label **Text 1**. This will hold the text for the first subtitle. Set the length to the maximum number of characters you anticipate using. Mine is set to 510. Select **Filtered text**.  You may need to configure and enable the Full HTML setting under **Configuration \> Text Formats**. Be sure to include here any HTML elements you want to use in your subtitles, \<em\> or \<strong\>, for instance. You can leave the **Manage Display** settings set to default values. I grouped my text fields here under a collapsing fieldset called **View Procedure Text**.  This hides the subtitles on the node view page but allows the user to optionally view them if they want to see all of the subtitles listed in order. You can hide these fields on the page using the content type display settings if you like, but they will still output as subtitles.

    h. Repeat the above step (g), for as many subtitles as you anticipate using. I will use no more than 25. When adding the text field, you may notice you have the option to add an unlimited number of values**. Do not do this**. We need to create distinct fields so we can order them and reference them separately through a view, discussed later.

    i.  Add any other optional fields you would like to display on the same page as your video content.

3.  Create a content type called **Content Container** (see Figure 1c). This is not strictly necessary for creating movies with subtitles, but in my case, we may have many instances where we refer to a single movie and its associated content again and again, in different contexts. We do this by using a node or entity reference field where we reuse the **Movie** content output through a different content type page (here called **Content Container**). This means there is only one source movie node to keep track of. **Note:** I am explaining this here because I refer to **Content Container** in code in my videojs.tpl.php override later. The code will still work on the **Movie** content type even if you don’t create the **Content Container** content type, however.

    a. Add an entity reference field to the content type called **Media Reference**. It should be a select list. For **Entity Selection**, choose **Simple**. Choose **Movie** as the type of content to reference.

### Create some test content.

See Figure 2 for an example.

1.  Click **Add content** from the admin **Dashboard**.
2.  Click **Movie.**
3.  Add a title. Mine is called “Test of HTML5 Video.”
4.  Add a time in the **Time 1** field. WEBVTT expects a very specific time format for this field. It should be formatted HH:MM.SS where: HH is hours, with a leading 0 if necessary; MM is minutes, with a leading 0 if necessary; and SS is seconds, with a leading 0 if necessary. There is some flexibility in these time formats, as you will see if you look at the W3C spec. In general, they should correspond to the time format of your video clip. My clip is only a few seconds long, however, I have followed the HH:MM.SS format and this works reliably.
5.  Enter the start time in HH:MM.SS format, followed by two dashes and a greater-than sign (--\>), followed by the end time, like so: **00:00.00 --\> 00:05.00.**
6.  Add some text to the **Text 1** field. I entered “1. This is a test of subtitles with the H.264 video format for HTML5.” Make sure you select **Full HTML** for the text format--this will allow you to use formatting for your subtitles.
7.  Repeat as necessary for each subtitle you would like to add. Make sure that your start/end times do not overlap.
8.  Add some test content. I used an mp4 file, but you can use any file types supported by the Video.js module.

### Create the view to provide the subtitles feed for each node.

We are going to be using the **Views** and the **Views Data Export** modules to “feed” the WEBVTT-formatted time and text information from our **Movie** content type into the actual video contained within our **Movie** page. Let’s go ahead and build our WEBVTT source view now.

1.  Create a new view; see figure 2a for details. Mine is called **Captions**. Select the following options on the Add new view page:

    a\. Show **Content** of type **Movie** sorted by **Unsorted**.

    b\. Under **Display** select **Unformatted list** of **fields**.

    c\. Enter **1** for **Items to display**.

    d\. Uncheck **Use a pager**.

    e\. Click **Continue & edit.**

2.  Under **Displays** add a **Data export** display.

    a\. Under **Data Export Settings \> Path**, add this path: **/feed/%/datafeed.vtt**

    It is important that you enter this path exactly. We will be using an argument to build the feed for each page, and the last section of the path must end in the .vtt extension, so the video player can read the source “file” it is being fed**. Save** the view. Do this first so the **undefined path** error message goes away.

    b\. Click on **Format \> CSV** **file** (the default format). Change the format to **TXT** (plain text). When the style options window opens, accept the defaults (**Provide as file** should be unchecked). Click **Apply**.

    c\. Under **Fields**, delete the **Content: Title** field. Now add a **Global: Custom tex**t field. Click on the **Global: Custom text** field and in the text box, add **WEBVTT**. This is the header that the HTML5 player is looking for to identify a subtitle source.

    d\. Now add a second field, **Content: Time 1.** This is the display time field we created in our **Movie** content type. The formatter should be set to **Plain text.**

    e\. Go ahead and add a third field, **Content: Text 1**. This is the text we want to display at the time attached to the **Time 1** field. For the formatter, specify **Default**. We can use HTML tags to style individual words in our subtitles using this feature; there are also some unique features in the HTML5 spec: using cues, etc.

    f\. Repeat steps d and e for as many **Time** and **Text** fields as you anticipate needing for your **Movie** content type. **Note:** Make sure the **Global** field is the first field in the view, followed by the first **Time** field and the first **Text** field. The second **Time** field will follow the first **Text** field, and the second **Text** field will follow the second **Time** field. Proceed in this order.

    g\. For the last field in your view, add the **Content: Nid** field. This will hold the node ID of the node we are viewing. Select **Exclude from display** when configuring the field. This will allow us to use the Node ID of the page we are viewing as an argument for the WEBVTT feed we are constructing, but we don’t want it to display in our video.

    h\. Now go to the **Advanced** panel of the **Data export** display. Under **Contextual Filters**, select **Content: Nid.** In the configuration box, select the **Show “Page not found”** option, under **When the filter value is not in the URL.**

    i\. ** **Finally, add **Content: Type (=Movie)** under **Filter Criteria. Content: Published (Yes)** should appear in the view by default. If not, add it.

    j\. **Save** the view.

    k\. Now in **Preview with contextual filters:** field add the node ID number of the **Movie** content that you created and click **Update preview.** You should see something ***somewhat similar*** to the screenshot in Figure 3b. ***Yours should look different, however, probably with some extra formatting between the lines, that looks like this:*** \[\]. This is because we have not yet customized the theme template for the view. We’ll do this next.

### Add a custom Views Data Export template to your theme folder.

1.  Still in the **Data export** display of our view, click on **Theme: Information** at the bottom-right corner of the page. This will open a box with many different theming options. Some of these are based on template files found in the **Views Data Export** module, and after looking through these files, I found that **views-data-export-txt-body.tpl** contained the page elements I wanted to modify.
2.  To create an override template that will only affect the output of this view, I followed the **Theme: Information** page’s suggestions and called it **views-data-export-txt-body--captions.tpl**. This is specific enough to cover all of the data exported from this view, but not from another view using the TXT setting of the **Views Data Export** display. Save this file **views-data-export-txt-body--captions.tpl.php** in your theme folder.
3.  See the screenshot of the final code below (Figure 4a). If possible, I will post the PHP template files described here with this document. You will want to use the code exactly as it appears; the spacing of the variables in the template make a difference in the final “plain text” output that WEBVTT is expecting. Line numbers are included for clarity.
4.  Now, back in the **Captions view, Data export display, Theming information page**, scroll to the bottom. Click the **Rescan template files** button. When the scan is complete, you should see the name of your overriding file listed in bold, in the second **Alternative Style** section (see Figure 4b). If you don’t, make sure that your template is in the proper theme folder and clear your caches. If you are using a **templates** folder within your theme, put the overriding file in there.
5.  In the **Preview with contextual filters: field**, your preview (with the node ID of the content you created entered) should now look exactly like Figure 3b. ***You should see lines of plain text with no extra formatting or strange characters between them***

#### Code from views-data-export-txt-body--captions.tpl.php

``` php
<?php
/**
 * @file views-view-table.tpl.php
 * Template to display a view as a table.
 *
 * - $title : The title of this group of rows.  May be empty.
 * - $rows: An array of row items. Each row is an array of content
 *   keyed by field ID.
 * - $header: an array of haeaders(labels) for fields.
 * - $themed_rows: a array of rows with themed fields.
 * @ingroup views_templates
 */

foreach ($themed_rows as $count => $row):
  foreach ($row as $field => $content):
?>

<?php print $content; ?>
<?php endforeach;?>
<?php endforeach;?>
```

### Create a video.js override template.

1.  Okay, almost done. The last thing to do is create a video.js override template in your theme folder. This part probably would have been done better as a theme template function or as a separate module but it still works pretty well. Call the file videojs.tpl.php. This is from the video.js template file found in the video.js module. There’s a screenshot of the code I used below (Figure 5). The comments explain where I added custom code.

    a\. Essentially, this code uses the HTML5

    element to add subtitles (line 32, kind=”subtitles”; change this to “captions” for closed captions) to any page where the video.js theme template is called. The WEBVTT-formatted source for the subtitles is specified in `src=<?php print(‘/feed/’ .$tnodeid . ‘datafeed.vtt’);?>` . The variable `$tnodeid` is passing in either the node ID (line 16) if the content is of the type Movie, or (lines 18-24) passes in the value of the referenced node, if it is contained in the Content Container content type (field_media_reference_target_id is the column containing the node reference target id).

    b\. The view Captions view, Data export display, uses the node ID argument to provide the correct content for each page request, formatted as a WEBVTT “file,” hence the .vtt ending specified in the `src` attribute.

#### Code from videojs.tpl.php

``` php
<?php
/**
 * @file
 * Provide the HTML output of the Video.js video player.
 */

$attrs = '';
if (!empty($autoplay)) {
$attrs .= ' autoplay="autoplay"';
}
if (!empty($poster)) {
  $attrs .= ' poster="'. check_plain($poster) .'"';
}

//Get the Node ID for the Movie node content type, for standalone use
if (arg(0) == 'node' && is_numeric(arg(1))) $nodeid = arg(1);
// Query the database to test if the node ID of the Content Container is the same as the Movie node
$result = db_query("SELECT field_media_reference_target_id
FROM field_data_field_media_reference
WHERE entity_id = :nodeid", array(':nodeid' => $nodeid));
// If it returns a number, that must be the node ID of the referenced media type, so set $tnodeid to that
$tnodeid = $result->fetchField();
// If query returns zero, then the node must be of type Movie, so set $tnodeid to the second arugment (nid)
if ($tnodeid == 0) $tnodeid = arg(1);


// The code below passes in a dynamic path for the subtitles "file" (src), in this case, a view. The view uses an argument of node id ($tnodeid) to load the correct text for each page. 
if (!empty($items)): ?>
<video id="<?php print $player_id; ?>-video" data-setup="{}" class="video-js vjs-default-skin" width="<?php print($width) ?>" height="<?php print($height) ?>" controls="controls" preload="auto"<?php echo $attrs; ?>>
<track class="subtitles" srclang="en" label="English" kind="subtitles" src=<?php print('/feed/' . $tnodeid . '/datafeed.vtt');?> default />
<?php foreach ($items as $item): ?>
  <source src="<?php print(file_create_url($item['uri'])) ?>" type="<?php print check_plain($item['videotype']) ?>" />
<?php endforeach; ?>
</video>
<?php endif;
```

### Check your test content.

Go to the test content display you created earlier. When you click the play button on the video, or possibly even when you load the page, you should see your subtitles/captions display. Below is a screenshot (Figure 6) showing the final result.

### Conclusion.

I hope this helps somebody out there! I realize there are probably much better ways to do this, so please feel free to update or edit this document, or post your methods. It would be great to see this functionality in a module if anyone would like to take that on.

### Appendix: HTML5 Video Track Element Resources

- W3C: <http://www.w3.org/wiki/HTML/Elements/track>
- HTML5 Rocks: <http://www.html5rocks.com/en/tutorials/track/basics/>
- Longtail Video: [http://www.longtailvideo.com/blog/27621/whats-new-in-html5-the-track-ele...](http://www.longtailvideo.com/blog/27621/whats-new-in-html5-the-track-element)
