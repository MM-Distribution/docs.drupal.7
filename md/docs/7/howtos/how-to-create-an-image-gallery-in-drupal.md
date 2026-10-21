---
title: "How to Create an Image Gallery in Drupal"
source_url: "https://www.drupal.org/docs/7/howtos/how-to-create-an-image-gallery-in-drupal"
page_type: page
last_updated: "Last updated on 25 January 2018"
published: "2013-12-08T16:16:19+00:00"
modified: "2018-01-25T23:58:44+00:00"
breadcrumb: ["Drupal 7", "Site building and development HowTos for Drupal 7"]
fetched: "2026-10-21T08:05:10Z"
raw: "raw/docs/7/howtos/how-to-create-an-image-gallery-in-drupal.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# How to Create an Image Gallery in Drupal

Here is one way to to make an image gallery in Drupal 7 (the same theory will hold for Drupal 6 and, I presume, Drupal 8). This will create an "Image Gallery" content type, with images within each gallery re-orderable by 'drag and drop'. Here we go.

### You will need:

- Drupal 7
- [Multi-upload File Field Widget](https://drupal.org/project/multiupload_filefield_widget "Drupal Multi-upload file field widget - bulk upload files") (to allow your file fields to upload multiple files in one batch)
- [Multi-upload Image Field Widget](https://drupal.org/project/multiupload_imagefield_widget " mulit-upload image field widget - bulk upload images") (to allow the above to upload multiple images in one batch)
- [Colorbox](http://www.drupal.org/project/colorbox "Drupal Colorbox - open images in an overlay") (make sure you have [Libraries](http://www.drupal.org/project/libraries) installed)
- Some rudimentary CSS

### Technique:

- First off, enable the modules listed above.
- Then we need to create a content type. In this case, we'll call it "Image Gallery".
- Next, we need to create an image field inside this content type.
  - Choose "Image" as the field type and "Multiupload" as the widget type.
  - Set the number of allowed values for this field to "Unlimited".
- Create some image presets (admin/config/media/image-styles), such as:
  - Gallery Thumbnail (150px x 150px) - used on the gallery page to list the images in that gallery.
  - Gallery Full Size (1000px wide) - used in an overlay when Gallery Thumbnail images are clicked on.
- Go to your "Manage Display" page for this content type and for "Full Content" set the following displays for the image field
  - Label = Hidden
  - Image = Colorbox
    - On the Colorbox settings, set "Content Image Style" as "Gallery Thumbnail" and "Colorbox Image Style" as the "Gallery Full Size"
    - There are some other options here as well. Feel free to experiment.
    - Click "Update".
  - Click "Save".

Now you are ready to create an image gallery. You may need some CSS to float the images left/right and set some margins/padding.

You can then use [Views](http://www.drupal.org/project/views " use views to create lists") to list the galleries and link each item in the list to its corresponding gallery.
