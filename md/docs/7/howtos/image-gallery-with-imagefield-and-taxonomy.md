---
title: "Image gallery with Imagefield and Taxonomy"
source_url: "https://www.drupal.org/docs/7/howtos/image-gallery-with-imagefield-and-taxonomy"
page_type: page
last_updated: "Last updated on 26 January 2018"
published: "2012-12-11T11:49:23+00:00"
modified: "2018-01-26T00:04:44+00:00"
breadcrumb: ["Drupal 7", "Site building and development HowTos for Drupal 7"]
fetched: "2026-10-21T08:06:27Z"
raw: "raw/docs/7/howtos/image-gallery-with-imagefield-and-taxonomy.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Image gallery with Imagefield and Taxonomy

**Background**: Upgrading site from Drupal 5 to 7. The D5 site used image module that came with a ready to use image gallery. We had hundreds of pictures. Each picture was associated with one taxonomy term (image gallery).

**Use case:** An image gallery grouped by taxonomy term and has the latest posted image (thumbnail) as the album cover. This image links to a page which is in a grid of thumbnails of images pertaining to a specific taxonomy term. Individual thumbnails link to individual nodes that may have one or multiple images per node that open in a Colorbox. The node itself has images in a grid rather than default drupal vertical stacking of images.

**Step 1:** Create a Taxonomy Vocabulary: Image Gallery and add whatever terms to suit your image gallery.

**Step 2:** Create an Image content type with Title, Body, Image field and a Term Reference to the Image gallery vocabulary. Be sure to allow unlimited images for the image field or whatever you require.

**Step 3:** Display Image nodes as a grid of images:  
You will require: EVA: Entity Views Attachment <http://drupal.org/project/eva>

Create a view: I called it Image node grid (or whatever)  
Add-\> EVA Field

Format: Grid \| Settings (default)  
Show: Fields \| Settings (default)

Fields  
Content: Image (your image field)

(Image) Formatter: Image or Colorbox if you wish  
Content image style: thumbnail or medium as per your requirements  
Multiple field settings: Display all images

Filter criteria  
Content: Published (Yes)  
Content: Type (= Image)

Sort criteria  
Content: Post date (desc)

Entity content settings  
Entity type: Node  
Bundles: Image (tells this view to attach itself to Image nodes)

Advanced -\> Contextual filters  
When the filter value is NOT available  
Content: Nid -\> Provide default value -\> Type -\> Content ID from URL

When the filter value IS available or a default is provided  
Specify validation criteria -\> Validator Content Content types -\> Image (Your image content type)

Now go to the Image content type Structure -\> Content Type -\>Image (your image content type) -\>Manage Display -\>Hide the image field

When you visit an image node you will see the Title, Body and multiple images displayed as a grid.

**Step 4:** Create a few image nodes with single and multiple images per node.

**Step 5:** The Image Gallery Album Cover page.(your gallery landing page)

Create a Taxonomy view:

**In the Advanced section of the view**  
Create a Relationship: Taxonomy term: Content using the Image Gallery (the vocabulary you created in Taxonomy)- This will help display content in a taxonomy view

Create a Relationship -\> Taxonomy term: Representative node, Representative sort criteria -\> Content Post Date ( This will help display a single image per taxonomy term )

Use aggregation: Yes (once aggregation is activated an Aggregation settings link will appear under each item in the Fields, Filter and sort criterion sections of the view)

Now detail out the rest of the view:

Title: Image Gallery (or whatever)

Format: Grid \| Settings – Group by Taxonomy term  
Show: Fields \| Settings

Fields  
Taxonomy term: Name  
Taxonomy term: Term ID (hidden and used to link to the taxonomy term page)  
Content: Image (your image field)  
Relationship: Representative Node  
Formatter: Image  
Image style: thumbnail  
Link to: nothing,  
Multiple field settings: check Display all values (checkbox)  
Simple separator: "comma”,  
Display 1 value starting from 0 (this ensures only the first image of multiple images on the node will be displayed)  
Rewrite results -\> Output this field as a link -\> Link path = taxonomy/term/\[tid\] - where \[tid\] is the token for Taxonomy term: Term ID

Click the Aggregation settings for this image field and Choose Aggregation type: Group results together, keep the rest of the settings as default and Apply

Add whatever other fields you may want.

Filter criteria  
Content: Published (Yes)  
Content: Type (= Image) \| Choose the Relationship -\> Representative node

Sort criteria  
Taxonomy term: Weight (asc)

Page settings  
Path: /gallery  
Menu: Normal: Gallery

Use pager: Display all items \| All items (This ensures all the taxonomy terms are displayed)  
More link: No

Advanced  
Relationships (as explained above)  
Use aggregation: Yes (as explained above)

That's it you should have your landing gallery page grouped by taxonomy term and with one image that will eventually lead to the taxonomy term page (Read on).

**Step 6:** Display all images per taxonomy term in a grid of thumbnails

Enable the Taxonomy term View which is disabled by default.

Title: None

Format  
Format: Grid \| Settings (defaults)  
Show: Fields \| Settings (defaults)

Fields  
Content: Image  
Formatter: Image, Image style: thumbnail, Link image to: Content  
Multiple field settings: Display all values in the same row, Simple separator: “comma” Display: 1 value

Content: Title

Sort criteria  
Content: Post date (desc)

Use pager: Display all items \| All items

All other settings as per default values of the view

The Media and Media gallery is a much slicker option and I would have liked to migrate my data to Media and Media gallery if there was a way to do it.
