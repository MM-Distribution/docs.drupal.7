---
title: "Live_css with .less support"
source_url: "https://www.drupal.org/docs/7/theming/working-with-css/live_css-with-less-support"
page_type: page
last_updated: "Last updated on 6 July 2017"
published: "2012-01-30T13:41:09+00:00"
modified: "2017-07-06T10:07:54+00:00"
breadcrumb: ["Drupal 7", "Theming Drupal 7", "Working with CSS"]
fetched: "2026-10-21T08:15:14Z"
raw: "raw/docs/7/theming/working-with-css/live_css-with-less-support.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Live_css with .less support

Theming in Drupal has come a long way and the tools now available not only make theming easy but you can style your site very quickly.

This guide will outline the use of the live_css ( **<http://drupal.org/project/live_css>** ) module and how to implement .less support ( **<http://lesscss.org/>** ) with the Omega theme ( **<http://drupal.org/project/omega>** )

## Live_css:

This module, once installed, adds a tab to the right side of your monitor. When you click on the tab a css development section opens with a drop down list of all the css files available to use. You can then select the one that you need to use and start playing with your theme. The major advantage of this module is that the results of your styling occur as you are typing. This allows very quick theming and with extreme ease you can try a bunch of different style options for elements.  
The configuration page ( **admin/config/development/live_css** ) allows you to select just the style sheets for your theme or all stylesheets as well as changing the development section color styles (which is fun).

CSS caching will need to be disabled to view these changes, which is fairly standard for theming development and you will need to have write permissions to the .css file you want the changes to effect (which you kinda need anyway if you are theming).

## .less:

live_css comes with .less support so there is no need to add any other modules or tweak any other configuration. You just need to add a .less file to your site. I am outlining the procedure using the Omega theme because Omega is awesome and I highly recommend this theme.

You need to create a subtheme. I want to point out the Drush command here and only the Drush command because of its simplicity. If you do not use Drush - use it! These are the steps I use to create a subtheme using Drush and Omega.

``` php
1- drush dl omega omega_tools
2- drush en -y omega_tools
3- drush omega-subtheme SUBTHEME-NAME-HERE
```

Done. Now I have more time to theme.

But I want to use .less. Why? Because it not only makes the css more structured and a lot easier to use for yourself and other themers who might use it but, just in the writing style that you need to use your code becomes a lot smaller, simpler and practical.

So basically I just add a mystyle.less file in the css folder of the subtheme ( the same place where the global.css file is ) but this just adds the file, it is still not being called to the subtheme. In order to do that, we need to inform the theme through the .info file that this file exists and we want to use it.

Open the .info file of your subtheme. YOUR-SUBTHEME-NAME.info and look for:

``` php
css[global.css][name] = 'Your custom global styles'
css[global.css][description] = 'This file holds all the globally active custom CSS of your theme.'
css[global.css][options][weight] = '10'
```

This is how Omega adds the file to the user interface; copy and paste that code and change it with your new .less file.

``` php
css[global.less][name] = '.less subtheme file'
css[global.less][description] = 'New .less file for less integration with my subtheme'
css[global.less][options][weight] = '10'
```

Change global to the name of your .less file and **FLUSH ALL CACHES**

Now your .less file is recognized by Omega. There is just one more thing to do. Because of the very easy to use Omega interface for configuration of the sections and styles for the site, the .less file (or any other .css file) will not be editable straight away. You first need to select that the subtheme will be using the .less file in the theme configuration settings.

admin/appearance/settings/(THEME NAME GOES HERE )

Then select "toggle styles" in the vertical tabs and granted you have flushed all caches your new .less file will be in the options to enable. Check the checkbox and save. BAM! You now have .less integration with the live_css development environment.

Why is .less important? If you have worked with css3 you will know that to create these new effects the css can start to look very cumbersome. Here is an example creating a gradient with rounded corners and a box shadow.

``` php
.element{
  background: #1e5799; /* Old browsers */
  background: -moz-linear-gradient(top,  #1e5799 0%, #7db9e8 100%); /* FF3.6+ */
  background: -webkit-gradient(linear, left top, left bottom, color-stop(0%,#1e5799), color-stop(100%,#7db9e8)); /* Chrome,Safari4+ */
  background: -webkit-linear-gradient(top,  #1e5799 0%,#7db9e8 100%); /* Chrome10+,Safari5.1+ */
  background: -o-linear-gradient(top,  #1e5799 0%,#7db9e8 100%); /* Opera 11.10+ */
  background: -ms-linear-gradient(top,  #1e5799 0%,#7db9e8 100%); /* IE10+ */
  background: linear-gradient(top,  #1e5799 0%,#7db9e8 100%); /* W3C */
  filter: progid:DXImageTransform.Microsoft.gradient( startColorstr='#1e5799', endColorstr='#7db9e8',GradientType=0 ); /* IE6-9 
*/
   border:1px solid 
  -moz-border-radius-topleft: 5px;
  -moz-border-radius-topright: 5px;
  -moz-border-radius-bottomright: 33px;
  -moz-border-radius-bottomleft: px;
  -webkit-border-radius: 5px 5px 33px px;
  border-radius: 5px 5px 33px px;
  -webkit-box-shadow: 2px 2px 2px 2px #ccc;
  -moz-box-shadow: 2px 2px 2px 2px #ccc;
  box-shadow: 2px 2px 2px 2px #ccc;
}
```

Now this is a cool bit of code and can make you site start to look very clean and who does not want to start using the css3 code? But the code above is just for the css3 and we haven't even begun to have to float:left or margin:0 0 0 10px; to make the design just right. So why would you not want to make that bit of code into this?

``` php
.element{
  .l-gradient;
  .l-border-radius;
  .l-shadow;
  border:1px solid @b-color;
}
```

Not only it is a lot more compact but by declaring all your css styles at the top of the style sheet.

``` php
.l-gradient{
 background: #1e5799; /* Old browsers */
  background: -moz-linear-gradient(top,  #1e5799 0%, #7db9e8 100%); /* FF3.6+ */
  background: -webkit-gradient(linear, left top, left bottom, color-stop(0%,#1e5799), color-stop(100%,#7db9e8)); /*   Chrome,Safari4+ */
  background: -webkit-linear-gradient(top,  #1e5799 0%,#7db9e8 100%); /* Chrome10+,Safari5.1+ */
  background: -o-linear-gradient(top,  #1e5799 0%,#7db9e8 100%); /* Opera 11.10+ */
  background: -ms-linear-gradient(top,  #1e5799 0%,#7db9e8 100%); /* IE10+ */
  background: linear-gradient(top,  #1e5799 0%,#7db9e8 100%); /* W3C */
  filter: progid:DXImageTransform.Microsoft.gradient( startColorstr='#1e5799', endColorstr='#7db9e8',GradientType=0 ); /* IE6-9 
}
```

You can now use it throughout your theme by just calling .l-gradient. You can setup all your colors and simply call them by using @color.

See docs here -\><http://lesscss.org/#docs>.

I see a lot of people use sass which is another option instead of .less but I prefer .less and so have outlined here. If you would like to add sass to this document, please just click the edit button.
