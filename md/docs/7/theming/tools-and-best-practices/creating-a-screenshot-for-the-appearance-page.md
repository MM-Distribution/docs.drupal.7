---
title: "Creating a screenshot for the appearance page"
source_url: "https://www.drupal.org/docs/7/theming/tools-and-best-practices/creating-a-screenshot-for-the-appearance-page"
page_type: page
last_updated: "Last updated on 8 September 2016"
published: "2009-12-01T14:25:57+00:00"
modified: "2016-09-08T13:40:05+00:00"
breadcrumb: ["Drupal 7", "Theming Drupal 7", "Tools and best practices"]
fetched: "2026-10-21T08:54:19Z"
raw: "raw/docs/7/theming/tools-and-best-practices/creating-a-screenshot-for-the-appearance-page.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Creating a screenshot for the appearance page

Every theme for Drupal 7 needs a screenshot in the form of a screenshot.png placed in the theme directory. These are displayed in the theme listing within a Drupal installation (i.e. at Administer \> Appearance). It is best that screenshots are consistent. The guidelines for core theme screenshots are (starting from a blank Drupal site):

1.  Log in as the first user.

2.  Make sure the following modules are enabled: *block*, *comment*, *image*, *menu*, *search* and *taxonomy*.

3.  Turn on the features that the theme supports (logo, site name, slogan).

4.  Set the site name to the name of the theme and set the slogan to a brief tagline or description of your theme.

5.  Create the following article node:  

    > Title:  
    > **Donec felis eros, blandit non**
    >
    > Image:  
    > <http://commons.wikimedia.org/wiki/File:Earth_and_Moon.jpg>
    >
    > Body:  
    > Morbi id lacus. Etiam malesuada diam ut libero. Sed blandit, justo nec euismod laoreet, nunc nulla iaculis elit, vitae. Donec dolor. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos hymenaeos. Vivamus vestibulum felis \<a href="#"\>nec libero. Duis lobortis\</a\>. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Nunc venenatis pretium magna. Donec dictum ultrices massa. Donec vestibulum porttitor purus. Mauris nibh ligula, porta non, porttitor sed, fermentum id, dolor. Donec eu lectus et elit porttitor rutrum. Aenean justo. Phasellus augue tortor, mattis nonummy, aliquam euismod, cursus eget, ipsum. Sed ultricies bibendum ante. Maecenas rhoncus tincidunt eros.
    >
    > Tags:  
    > Earth, Moon, Latin
    >
    > Menu settings:  
    > Provide a menu link, Menu link title: Link 1

6.  Add at least 5 main menu and, if needed, some secondary menu links. We suggest "Link 2", "Link 3", "Link 4", and "Link 5"; you can link them to "user/1".

7.  Make sure the Search block is enabled.

8.  You should fill up the site more. For example, add a comment to the story node or add some blocks.

9.  Look at the node, and make sure the tabs are visible. Take a screenshot.

10. The screenshot should show the entire page and be about ~900x675 (4:3 ratio) resized to exactly 600x450. The image is displayed at 300x225 but for retina displays, you need to provide an image that doubles the regular resolution. Try to show many useful page elements (menu, tabs, title, links). Don't include browser chrome (toolbar, status bar, scrollbar, etc).

11. Apply a standard 'sharpen' filter to the thumbnail for clarity.

12. Save as a PNG, in paletted colorspace to cut down on size.

Example:  
![garland screenshot](/files/garland-7-screenshot.png)

### Screenshots for Drupal.org display

For Drupal.org project thumbnails (displayed at <http://drupal.org/project/Themes> and on the individual theme project pages), use the guidelines above except that:

- Try to keep the image small: save as paletted PNG or as a JPEG with 10-20% compression. This reduces the load time of the theme list on Drupal.org.
- To add the image to your project, click the Edit tab on the project node and expand the "Attached Images" section. Browse to find your screenshot locally and add it. A thumbnail will be created and added to the upper right corner of the project page once you submit your changes.

If you need to change the image you have uploaded, click the thumbnail on your project page (this takes you to the image node) and then click the Edit tab. You may then upload a new picture which will replace the existing one.
