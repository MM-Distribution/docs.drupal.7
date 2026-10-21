---
title: "Create a new custom theme with CSS alone"
source_url: "https://www.drupal.org/docs/7/theming/howto/create-a-new-custom-theme-with-css-alone"
page_type: page
last_updated: "Last updated on 10 August 2022"
published: "2009-03-07T20:58:35+00:00"
modified: "2022-08-10T10:23:10+00:00"
breadcrumb: ["Drupal 7", "Theming Drupal 7", "Theming HowTos"]
fetched: "2026-10-21T08:48:42Z"
raw: "raw/docs/7/theming/howto/create-a-new-custom-theme-with-css-alone.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Create a new custom theme with CSS alone

> In Drupal 6 and Drupal 7, there are many improvements in core that make it easy for CSS web designers to create themes without having to deal with any PHP code. The [Stark theme](http://drupal.org/project/stark) was created to help designers see the pure xhtml code output by Drupal, and is included in Drupal 7's core. Designers can now create beautiful themes that use nothing but CSS files.

This theming how-to will show you, in a few simple steps, how to create your own CSS-only theme for Drupal 6 or 7. *(Please note Stark should not be used as a basetheme in Drupal 8 or 9. Future core updates may break your site. Instead, subtheme core's Stable 9 or any number of contributed basethemes.)*

For a collection of useful materials for themers, see [Theming and Front End Development with Drupal](/theming).

## **Step 1**: Create the theme folder and .info file

The first step in creating a theme for Drupal is creating a folder for your theme to reside in, and a .info file to tell Drupal about your theme.

To create the folder:

1.  Create your folder in the `/sites/all/themes` directory.
2.  Name your folder `yourthemename`, all lowercase.

To create the .info file:

1.  Create a document in Notepad or your favorite plain text editor, and paste in the following information (changing where necessary\*):  

    ``` php
    name = yourthemename
    description = Description of yourtheme.
    core = 6.x
    engine = phptemplate
    stylesheets[all][] = style.css
    stylesheets[all][] = layout.css
    regions[left] = Left sidebar
    regions[right] = Right sidebar
    regions[content] = Content
    regions[header] = Header
    regions[footer] = Footer
    ```

2.  Save this document in the theme folder you created above, and name it yourthemename.info (all lowercase).

\*Notes on the .info file:

- You can easily [add more stylesheets](http://drupal.org/node/171209) to your theme.
- You can also easily [add more regions](http://drupal.org/node/171224) to your theme.
- Change the `core = 6.x` line to `core = 7.x` if you're creating a theme for Drupal 7.

## **Step 2**: Creating the Stylesheets

If you look at Stark's only stylesheet, [layout.css](http://cvs.drupal.org/viewvc.py/drupal/contributions/themes/stark/layout.css?view=log), you'll notice there are very few CSS rules:

``` php
#sidebar-left,
#main,
#sidebar-right {
  float: left;
  display: inline;
  position: relative;
}

#sidebar-left,
#sidebar-right {
  width: 20%;
}

body.one-sidebar #main {
  width: 80%;
}

body.two-sidebars #main {
  width: 60%;
}

body.sidebar-left #main-squeeze {
  margin-left: 20px;
}

body.sidebar-right #main-squeeze {
  margin-right: 20px;
}

body.two-sidebars #main-squeeze {
  margin: 0 20px;
}
```

The code simply lays out the content of the default Drupal installation in a logical way. This is about as simple as a theme can get. From here, you can build out your theme in many different ways.

The first step should be to layout the regions and graphic design of your page. You should do this in your own layout.css file.

Next, you can create a style.css file for other styles.

A common practice, for ease of code-maintenance, however, is to also create other CSS files including, but not limited to, html-elements.css, print.css, and ie.css. For each additional CSS file you create, you should add a line in `yourthemename.info` in the following format, below the other CSS stylesheet declarations:

`stylesheets[all][] = newstylesheetname.css`

## **Step 3**: Design, and have fun!

There's really nothing else to do, if you're creating a CSS-only theme...

If you want, you can view the [core PHP template files](http://drupal.org/node/190815) you're using in your theming. The main files you might want to view include:

- page.tpl.php (for the overall page layout)
- node.tpl.php (for all the 'nodes' or main content sections of a page)
- block.tpl.php (for the blocks, in whichever regions you place them)
- comment.tpl.php (for all comments on your site)

You can copy these PHP template files to your theme folder, then modify them to your liking, if you desire to change the way the html is structured.

*Note that the code on this page is for a Drupal 6 theme. A Drupal 7 theme would be somewhat different. For example, in Drupal 7 `#sidebar-left` and `#sidebar-right` would be `#sidebar-first` and `#sidebar-second`. For more information on updating a Drupal 6 theme for Drupal 7, see [Converting 6.x themes to 7.x](http://drupal.org/update/theme/6/7).*
