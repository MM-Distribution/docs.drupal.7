---
title: "Comparison of Rotator / Slider modules"
source_url: "https://www.drupal.org/docs/7/extend/comparison-of-contributed-modules/comparison-of-rotator-slider-modules"
page_type: page
last_updated: "Last updated on 30 April 2025"
published: "2009-03-30T19:59:26+00:00"
modified: "2025-04-30T20:53:04+00:00"
breadcrumb: ["Drupal 7", "Extending Drupal 7", "Comparison of contributed modules"]
fetched: "2026-10-21T09:01:33Z"
raw: "raw/docs/7/extend/comparison-of-contributed-modules/comparison-of-rotator-slider-modules.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Comparison of Rotator / Slider modules

This page came about as a result of this post that lists [Tabs and Slideshow Modules](http://groups.drupal.org/node/20384) in the Similar Module Review group. The linked post lists several modules that provide either tabbed content or rotating content.  
There are two general use cases here:

- A device to provide access to large amounts of regular site content from one area of the page (tabbed content).
- A device to showcase featured content, often on the home page, in an eye-catching manner (rotating/sliding content).

This comparison page is limited to the latter use case. It is open to discussion whether the ideal eventual outcome of any consolidation between the best features of the best of the modules would be a package that includes both types of feature.

Also, note a caution about misusing carousels: <http://shouldiuseacarousel.com/>

### Most popular modules overview

There are many modules that provide some sort of slideshow / rotator functionality, so it can be difficult to decide which one to use. The most popular are shown below; there may be other less popular modules which meet your specific needs more fully, but looking first at the most popular is a good place to start. The actual number of installs for all the rotator/slider modules is shown in the table further down the page (Note: the number of installs changes weekly, and so you should check the actual number of installs on the individual project pages).

- [Views Slideshow](http://drupal.org/project/views_slideshow) a Views style plugin using jquery cycle. Provides an extensible API that allows other cycles, rotators, and carousels to plug into the module, so they don't need to recreate the Views functionality.
- [jCarousel](http://drupal.org/project/jcarousel) This module allows developers and themers to make use of the jCarousel jQuery plugin. It includes a developer API that other modules can use, as well as Views integration in the 2.0 version so that you can turn any list of content or images into a carousel.
- [Flex slider](http://drupal.org/project/flexslider) provides a client-side automatic adaptation of the slides size according to the window size (Responsive). Can work with the Views module. Poor documentation.

### Other available modules overview

The following modules do not have as many installs as those listed above, but they all provide some sort of slideshow / rotator functionality.

- [Dynamic display block](http://drupal.org/project/ddblock) Enables you to create and present blocks of content in a dynamic and attractive way. Uses the jQuery Cycle Plug-in.
- [Views Slideshow Liquid Slider](http://drupal.org/project/views_slideshow_liquid_slider) A fully responsive, HTML5 jQuery content slider for both web and mobile devices.
- [Backstretch](https://drupal.org/project/backstretch) This module provides a field formatter and Context integration for jQuery Backstretch - A simple jQuery plugin that allows you to add a dynamically-resized, slideshow-capable background image to any page or element.
- [Content Glider](http://drupal.org/project/content_glider) Another jQuery plugin for image slider, very easy to use.
- [Juicebox](https://drupal.org/project/juicebox) This module provides an integration between the Juicebox HTML5 responsive gallery library and Drupal. Juicebox is in many ways the successor of Simpleviewer and offers a powerful and flexible image gallery front-end.
- [Views Nivo Slider](http://drupal.org/project/views_nivo_slider) a Views style plugin using the Nivo style slider. Drupal 6 version requires imagecache, imagefield and jquery update.
- [Views Slideshow: Dynamic display block](http://drupal.org/project/views_slideshow_ddblock) a Views slideshow plugin which enables you to present slideshows in an attractive way.
- [Views Slideshow Xtra](http://drupal.org/project/views_slideshow_xtra) is an enhancement module for Views Slideshow, providing the ability to create animated slideshow overlays. This module can also help automate the creation of any Drupal 7 Views Slideshow, using the Views Slideshow Xtra Example sub-module, which creates a Slide content type, a default Slideshow View, and example Slide nodes.
- [Views Slideshow: ImageFlow](http://drupal.org/project/views_slideshow_imageflow) offers an ImageFlow option to Views Slideshow, similar to Apple's CoverFlow.
- [Slideshow Creator](http://drupal.org/project/slideshow_creator) adds an input format filter to allow you to add slideshow creation code to the body of a node and other text fields.
- [Featured Content Slider](http://drupal.org/project/content_slider) - select nodes based on content type and create up to 3 blocks of featured content.
- [Views Fraction Slider](http://drupal.org/project/views_fractionslider) - select fields base formatting and allows you to animate multiple elements per slide. Set different animation methods like fade or (from) left, delays and easing for each element, or simple set some defaults in the plugin options. You also have full layout/design control through html and css (every html-element can be animated).
- [Slider](http://drupal.org/project/slider) - create a "slider" content type with a multi-value nodereference field to create carousel-style sliders of the referenced nodes.
- [Ajax Slideshow](http://drupal.org/project/ajax_slideshow) - Sequential presentation of any of the site nodes, using various effects. The slideshow is ajax-based which means the page load-time is agnostic to the amount of content included.
- [Media Nivo Slider](http://drupal.org/project/media-nivo-slider) - Provides the ability to expose the content of a Media Gallery to a Nivo Slider block.
- [Nivo formatter](http://drupal.org/project/nivo_formatter) - Nivo formatter is an image field formatter that transform any image field  
  to awesome Nivo Slider image gallery.
- [Nivo Slider](http://drupal.org/project/nivo_slider) - Nivo Slider is a stand-alone solution for creating a simple slideshow for your website.
- [Owl Carousel](http://drupal.org/project/owl-carousel) - Owl Carousel provides a modern feature rich responsive slider.
- [ResponsiveSlides](https://drupal.org/project/responsiveslides) - Provides a responsive slideshow style option for Views using the super-lightweight (1kb) ResponsiveSlides.js plugin.
- [Views Ticker](https://drupal.org/project/views_ticker) - Provides a style for Views module to display scrolling tickers. Horiztonal, vertical, fade in/out, and a "typing" style are provided.
- [Views Slideshow Cycle2](https://www.drupal.org/sandbox/peter/2498091) - Updates Views Slideshow from Cycle to Cycle2. You get responsive design, lazy loading, and a few other improvements. Views Slideshow Cycle2 uses [jQuery Cycle2](https://www.drupal.org/sandbox/peter/2499419), a module you can use from any module or theme code. Beta testers welcome.
- [Slick Carousel](https://www.drupal.org/project/slick) - A full-featured views and field formatter that handles responsive images and video.
- [Extra Block Types (EBT): Slideshow](https://www.drupal.org/project/ebt_slideshow) - module provides ability to add an EBT block with FlexSlider.
- [Extra Block Types (EBT): Slick Slider](https://www.drupal.org/project/ebt_slick_slider) - module provides ability to add an EBT block with Slick Slider.
- [Extra Block Types (EBT): Carousel](https://www.drupal.org/project/ebt_carousel) - module provides ability to add an EBT block with provides ability to add a block with Tiny Slider.
- [Mega Slider (MD Slider)](https://www.drupal.org/project/md_slider) Easy solution for any slider on your website. Mega Slider (MD Slider) is responsive slider module with touch-swipe navigation. Friendly admin user interface and powerful timeline manager, you can add text, image or video and create fancy slider. Highly customizable slider for Drupal ^9 \|\| ^10.

### Deprecated modules

- [Coda Slider](http://drupal.org/project/codaslider) - A nice jQuery plugin for image slider and support thumbnail navigator. Deprecated - maintainer recommends Content Glider instead.
- [Views Carousel](http://drupal.org/project/viewscarousel) - a Views style plugin using the jCarousel jQuery plugin for the rotation, suitable for e.g. a scrollable thumbnail viewer. Deprecated - maintainer recommends jcarousel
- [Views Rotator](http://drupal.org/project/views_rotator) - a Views style plugin using the Cycle jQuery plugin with a small number of options for controlling transition behaviour. Deprecated - maintainer recommends Views Slideshow instead.
- [Views Cycle](http://drupal.org/project/views_cycle) - a Views style plugin using the Cycle jQuery plugin, with an option for tabs, several transition effect options and other transition behavior settings. Deprecated - maintainer recommends Views Slideshow instead.
- [EasySlider](http://drupal.org/project/easySlider) - create a list-style view with a block display and the view results are displayed in a carousel style slider. Maintainer recommends Views Slideshows instead.
- [Node Carousel](http://drupal.org/project/nodecarousel) - create carousels of nodes based on nodequeue or custom values using a hook in your own module. Maintainer recommends Views Carousel instead.
- [CCK Multimage](http://drupal.org/project/cck_multimage) - a fork of the abandoned CCK Slideshow module which creates slideshows from multivalue imagefields. Only available for Drupal 5
- [Fancy Slide](http://drupal.org/project/fancy_slide) - create slideshows with thumbnails, descriptions and a selection of transition effects by using the imagecache module and optionally a nodequeue. Not supported anymore. Only available for Drupal 6.

### Other modules that could be included:

- [Views Accordion](http://drupal.org/project/views_accordion) - a Views style plugin using the Accordion jQuery plugin
- [Imagefield Dewslider](http://drupal.org/project/imagefield_dewslider) - Image Field formatter for Dewslider
- [Field Slideshow](/project/field_slideshow) - Field formatter for a slideshow powered with jCycle and, optionally, jCarousel.

### Other modules won't be included:

- [Couloir Slideshow](http://drupal.org/project/couloir_slideshow) - this seems more like a Lightbox gallery type solution... without the Lightbox.
- [Frontpage Slideshow](http://drupal.org/project/fpss) - this requires a paid 3rd party library.

## Module documentation/demo comparison

<table style="width:100%;">
<colgroup>
<col style="width: 10%" />
<col style="width: 10%" />
<col style="width: 10%" />
<col style="width: 10%" />
<col style="width: 10%" />
<col style="width: 10%" />
<col style="width: 10%" />
<col style="width: 10%" />
<col style="width: 10%" />
<col style="width: 10%" />
</colgroup>
<thead>
<tr class="header">
<th>Module</th>
<th>5.x</th>
<th>6.x</th>
<th>7.x</th>
<th>8.x</th>
<th>9.x</th>
<th>10.x</th>
<th>Installs</th>
<th>Documentation</th>
<th>Demo Site</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
</tr>
<tr class="even">
<td><a href="http://drupal.org/project/views_slideshow">Views Slideshow</a></td>
<td><img src="/misc/watchdog-ok.png" alt="Yes" /></td>
<td><img src="/misc/watchdog-ok.png" alt="Yes" /></td>
<td><img src="/misc/watchdog-ok.png" alt="Yes" /></td>
<td><img src="/misc/watchdog-ok.png" alt="Yes" /></td>
<td><img src="/misc/watchdog-ok.png" alt="Yes" /></td>
<td><img src="/misc/watchdog-ok.png" alt="Yes" /></td>
<td>128,754</td>
<td><a href="http://drupal.org/node/755010">Documentation</a><br />
<a href="http://drupalcode.org/project/views_slideshow.git/blob/refs/heads/6.x-1.x:/README.txt">README.txt</a></td>
<td> </td>
</tr>
<tr class="odd">
<td><a href="http://drupal.org/project/flexslider">Flex Slider</a></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td><img src="/misc/watchdog-ok.png" alt="Yes" /></td>
<td><img src="/misc/watchdog-ok.png" alt="Yes" /></td>
<td><img src="/misc/watchdog-ok.png" alt="Yes" /></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td>72,995</td>
<td><a href="http://coldfrontlabs.ca/blog/using-flex-slider-drupal-7">Documentation</a></td>
<td><a href="http://flex.madebymufffin.com/demo/">http://flex.madebymufffin.com/demo/</a></td>
</tr>
<tr class="even">
<td><a href="https://drupal.org/project/slick">Slick Carousel</a></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td><img src="/misc/watchdog-ok.png" alt="Yes" /></td>
<td><img src="/misc/watchdog-ok.png" alt="Yes" /></td>
<td><img src="/misc/watchdog-ok.png" alt="Yes" /></td>
<td><img src="/misc/watchdog-ok.png" alt="Yes" /></td>
<td>65,478</td>
<td><a href="http://kenwheeler.github.io/slick">Documentation</a></td>
<td><a href="http://kenwheeler.github.io/slick">http://kenwheeler.github.io/slick</a></td>
</tr>
<tr class="odd">
<td><a href="https://www.drupal.org/project/jcarousel">jCarousel</a></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td><img src="/misc/watchdog-ok.png" alt="Yes" /></td>
<td><img src="/misc/watchdog-ok.png" alt="Yes" /></td>
<td><img src="/misc/watchdog-ok.png" alt="Yes" /></td>
<td><img src="/misc/watchdog-ok.png" alt="Yes" /></td>
<td><img src="/misc/watchdog-ok.png" alt="Yes" /></td>
<td>27,089</td>
<td> </td>
<td> </td>
</tr>
<tr class="even">
<td><a href="http://drupal.org/project/nivo_slider">Nivo Slider</a></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td><img src="/misc/watchdog-ok.png" alt="Yes" /></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td>16,293</td>
<td><a href="http://drupal.org/node/1348680">Documentation</a></td>
<td><a href="http://nivo.dev7studios.com">http://nivo.dev7studios.com</a></td>
</tr>
<tr class="odd">
<td><a href="https://drupal.org/project/owlcarousel">Owl Carousel</a></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td><img src="/misc/watchdog-ok.png" alt="Yes" /></td>
<td><img src="/misc/watchdog-ok.png" alt="Yes" /></td>
<td><img src="/misc/watchdog-ok.png" alt="Yes" /></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td>18,624</td>
<td><a href="http://legomenon.io/article/drupal-7-configuration-owl-carousel">Documentation</a></td>
<td><a href="http://owlgraphic.com/owlcarousel">http://owlgraphic.com/owlcarousel</a></td>
</tr>
<tr class="even">
<td><a href="http://drupal.org/project/views_nivo_slider">Views Nivo Slider</a></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td><img src="/misc/watchdog-ok.png" alt="Yes" /></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td>7,286</td>
<td><a href="http://www.brightwebsitedesign.com/how-to-install-and-set-up-nivo-slider-on-drupal">Documentation</a></td>
<td><a href="http://nivo.dev7studios.com/">http://nivo.dev7studios.com/</a></td>
</tr>
<tr class="odd">
<td><a href="http://drupal.org/project/ddblock">Dynamic display block</a></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td><img src="/misc/watchdog-ok.png" alt="Yes" /></td>
<td><img src="/misc/watchdog-ok.png" alt="Yes" /></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td>2,270</td>
<td><a href="http://drupal.org/project/ddblock"></a> <a href="http://ddblock.myalbums.biz">ddblock.myalbums.biz</a><br />
<a href="http://drupal.org/node/293714">Handbook page</a><br />
<a href="http://drupalcode.org/project/ddblock.git/blob/HEAD:/README.txt">README.txt</a></td>
<td><a href="http://ddblock.myalbums.biz">http://ddblock.myalbums.biz</a></td>
</tr>
<tr class="even">
<td><a href="https://drupal.org/project/views_ticker">Views Ticker</a></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td><img src="/misc/watchdog-ok.png" alt="Yes" /></td>
<td><img src="/misc/watchdog-ok.png" alt="Yes" /></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td>4,747</td>
<td><a href="http://drupalcode.org/project/views_ticker.git/blob/HEAD:/README.txt">README.txt</a></td>
<td><a href="http://viewsticker.inettity.com/">http://viewsticker.inettity.com/</a></td>
</tr>
<tr class="odd">
<td><a href="http://drupal.org/project/views_slideshow_ddblock">Views Slideshow: Dynamic display block</a></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td><img src="/misc/watchdog-ok.png" alt="Yes" /></td>
<td>dev</td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td>941</td>
<td><a href="http://drupalcode.org/viewvc/drupal/contributions/modules/views_slideshow_ddblock/README.txt?revision=1.2&amp;view=markup">README.txt (V1.x)</a><br />
<a href="http://drupalcode.org/viewvc/drupal/contributions/modules/views_slideshow_ddblock/README.txt?view=markup">README.txt (V2.x)</a><br />
<a href="http://ddblock.myalbums.biz/node/970">Tutorial (V1.x)</a><br />
<a href="http://ddblock.myalbums.biz/node/1787">Tutorial (V2.x)</a></td>
<td><a href="http://ddblock.myalbums.biz">http://ddblock.myalbums.biz</a></td>
</tr>
<tr class="even">
<td><a href="http://drupal.org/project/slideshow_creator">Slideshow Creator</a></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td><img src="/misc/watchdog-ok.png" alt="Yes" /></td>
<td><img src="/misc/watchdog-ok.png" alt="Yes" /></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td>558</td>
<td><a href="http://drupal.org/node/237049">Documentation</a></td>
<td><a href="http://wingedhearts.org/grounded/carpetpython">http://wingedhearts.org/grounded/carpetpython</a></td>
</tr>
<tr class="odd">
<td><a href="http://drupal.org/project/nivo_formatter">Nivo Formatter</a></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td>beta1</td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td>932</td>
<td><a href="http://drupalcode.org/project/nivo_formatter.git/blob_plain/refs/heads/master:/README.txt">README.txt</a></td>
<td><a href="http://nivo.dev7studios.com">http://nivo.dev7studios.com</a></td>
</tr>
<tr class="even">
<td><a href="http://drupal.org/project/media_nivo_slider">Media Nivo Slider</a></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td><img src="/misc/watchdog-ok.png" alt="Yes" /></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td>1,274</td>
<td><a href="http://drupal.org/project/media_nivo_slider">Documentation</a></td>
<td><a href="http://nivo.dev7studios.com/">http://nivo.dev7studios.com/</a></td>
</tr>
<tr class="odd">
<td><a href="https://www.drupal.org/project/ebt_slideshow">Extra Block Types (EBT): Slideshow</a></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td><img src="/misc/watchdog-ok.png" alt="Yes" /></td>
<td><img src="/misc/watchdog-ok.png" alt="Yes" /></td>
<td><img src="/misc/watchdog-ok.png" alt="Yes" /></td>
<td>148</td>
<td><a href="https://flexslider.woothemes.com/">Documentation FlexSlider</a><br />
<a href="https://drupalbook.org/ebt">Documentation EBT</a></td>
<td><a href="https://drupalbook.org/ebt/demo/slideshow">Demo EBT Slideshow</a></td>
</tr>
<tr class="even">
<td><a href="https://www.drupal.org/project/ebt_slick_slider">Extra Block Types (EBT): Slick Slider</a></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td><img src="/misc/watchdog-ok.png" alt="Yes" /></td>
<td><img src="/misc/watchdog-ok.png" alt="Yes" /></td>
<td><img src="/misc/watchdog-ok.png" alt="Yes" /></td>
<td>70</td>
<td><a href="https://kenwheeler.github.io/slick/">Documentation Slick Slider</a><br />
<a href="https://drupalbook.org/ebt">Documentation EBT</a></td>
<td><a href="https://drupalbook.org/ebt/demo/slick-slider">Demo EBT Slick Slider</a></td>
</tr>
<tr class="odd">
<td><a href="https://www.drupal.org/project/ebt_carousel">Extra Block Types (EBT): Carousel</a></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td><img src="/misc/watchdog-ok.png" alt="Yes" /></td>
<td><img src="/misc/watchdog-ok.png" alt="Yes" /></td>
<td><img src="/misc/watchdog-ok.png" alt="Yes" /></td>
<td>66</td>
<td><a href="https://github.com/ganlanyuan/tiny-slider">Documentation Tiny Slider</a><br />
<a href="https://drupalbook.org/ebt">Documentation EBT</a></td>
<td><a href="http://ganlanyuan.github.io/tiny-slider/demo/">Demo Tiny Slider</a><br />
<a href="https://drupalbook.org/ebt/demo/carousel"><br />
Demo EBT Carousel<br />
</a></td>
</tr>
<tr class="even">
<td><a href="http://drupal.org/project/content_slider">Featured Content Slider</a></td>
<td><img src="/misc/watchdog-ok.png" alt="Yes" /></td>
<td><img src="/misc/watchdog-ok.png" alt="Yes" /></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td>257</td>
<td><a href="http://drupalcode.org/project/content_slider.git/blob/HEAD:/README.TXT">README.txt</a></td>
<td><a href="http://www.iGadgets.be/">www.iGadgets.be/ (Example site)</a></td>
</tr>
<tr class="odd">
<td><a href="http://drupal.org/project/viewscarousel">Views Carousel</a></td>
<td>dev</td>
<td>dev</td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td>219</td>
<td><a href="http://drupal.org/node/324777">Handbook page</a><br />
<a href="http://drupalcode.org/project/viewscarousel.git/blob/HEAD:/README.txt">README.txt</a></td>
<td><a href="http://sorgalla.com/jcarousel/">http://sorgalla.com/jcarousel/</a></td>
</tr>
<tr class="even">
<td><a href="https://drupal.org/project/responsiveslides">ResponsiveSlides</a></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td><img src="/misc/watchdog-ok.png" alt="Yes" /></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td>50</td>
<td><a href="http://responsiveslides.com/">Documentation</a></td>
<td><a href="http://drastikbydesign.com/demo/responsiveslides-demo">http://drastikbydesign.com/demo/responsiveslides-demo</a></td>
</tr>
<tr class="odd">
<td><a href="http://drupal.org/project/views_slideshow_liquid_slider">Liquid Slider</a></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td><img src="/misc/watchdog-ok.png" alt="Yes" /></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td>154</td>
<td><a href="http://liquidslider.kevinbatdorf.com/#/documentation.html">Documentation</a></td>
<td><a href="http://liquidslider.kevinbatdorf.com/">http://liquidslider.kevinbatdorf.com/</a></td>
</tr>
<tr class="even">
<td><a href="http://drupal.org/project/views_slideshow_imageflow">Views Slideshow: ImageFlow</a></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td><img src="/misc/watchdog-ok.png" alt="Yes" /></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td>87</td>
<td><a href="http://drupalcode.org/project/views_slideshow_imageflow.git/blob/refs/heads/6.x-1.x:/README.txt">README.txt</a></td>
<td><a href="http://finnrudolph.de/ImageFlow">http://finnrudolph.de/ImageFlow</a></td>
</tr>
<tr class="odd">
<td><a href="http://drupal.org/project/slider">Slider</a></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td><img src="/misc/watchdog-ok.png" alt="Yes" /></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td>33</td>
<td><a href="http://drupalcode.org/project/slider.git/blob/HEAD:/README.txt">README.txt</a></td>
<td><a href="http://jqueryfordesigners.com/demo/coda-slider.html">http://jqueryfordesigners.com/demo/coda-slider.html</a></td>
</tr>
<tr class="even">
<td><a href="http://drupal.org/project/ajax_slideshow">Ajax Slideshow</a></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td><img src="/misc/watchdog-ok.png" alt="Yes" /></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td>24</td>
<td><a href="http://www.dofinity.com/he/node/596">dofinity's page</a><br />
<a href="http://drupalcode.org/viewvc/drupal/contributions/modules/ajax_slideshow/README.txt?revision=1.4&amp;view=markup">README.txt</a></td>
<td><a href="http://67.222.4.219/slideshow-front">news.com</a></td>
</tr>
<tr class="odd">
<td><a href="http://drupal.org/project/fancy_slide">Fancy Slide</a></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td><img src="/misc/watchdog-ok.png" alt="Yes" /></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td>23</td>
<td><a href="http://drupalcode.org/project/fancy_slide.git/blob/HEAD:/README.txt">README.txt</a></td>
<td><a href="http://fancy-slide.drupaldemos.org/" title="Fancy Slide Demo Site">http://fancy-slide.drupaldemos.org</a></td>
</tr>
</tbody>
</table>

## Module feature comparison

This feature comparison is based on a spreadsheet done by stephthegeek.  
For the purposes of discussion and comparison of these modules, the word tab refers to "the bit that you click on to switch to the next piece of content". In many of the rotator modules this is refered to as a thumbnail.

<table style="width:100%;">
<colgroup>
<col style="width: 14%" />
<col style="width: 14%" />
<col style="width: 14%" />
<col style="width: 14%" />
<col style="width: 14%" />
<col style="width: 14%" />
<col style="width: 14%" />
</colgroup>
<thead>
<tr class="header">
<th width="90px">Module</th>
<th>Tabs</th>
<th width="65px">Tab content</th>
<th width="60px">Main content</th>
<th>Nav links</th>
<th width="70px">Behaviour options</th>
<th>Styles included</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><a href="http://drupal.org/project/ddblock">Dynamic display block</a></td>
<td><img src="/misc/watchdog-ok.png" alt="Yes" /></td>
<td>Pagers with Numbers, prev/next, links, images, custom and scrollable pager</td>
<td>Image folder, node, nodequeue, blocks, views</td>
<td><img src="/misc/watchdog-ok.png" alt="Yes" /></td>
<td>Speed, timeout, all jcycle effects, custom, etc.</td>
<td>15 free ddblock themes, commercial themes available.</td>
</tr>
<tr class="even">
<td><a href="http://drupal.org/project/views_slideshow">Views Slideshow</a></td>
<td><img src="/misc/watchdog-ok.png" alt="Yes" /></td>
<td>Title and teaser of the node</td>
<td>Output of a View</td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td>Speed, fade effect, sort order</td>
<td>None</td>
</tr>
<tr class="odd">
<td><a href="http://drupal.org/project/views_slideshow_ddblock">Views Slideshow: Dynamic display block</a></td>
<td><img src="/misc/watchdog-ok.png" alt="Yes" /></td>
<td>Pagers with Numbers, prev/next, links, images, custom and scrollable pager</td>
<td>Output of a View (Mapped fields)</td>
<td><img src="/misc/watchdog-ok.png" alt="Yes" /></td>
<td>Speed, timeout, all jcycle effects, custom, etc.</td>
<td>6 free slideshow themes, commercial themes available.</td>
</tr>
<tr class="even">
<td><a href="http://drupal.org/project/views_slideshow_imageflow">Views Slideshow: ImageFlow</a></td>
<td><img src="/misc/watchdog-ok.png" alt="Yes" /></td>
<td>Image and Link</td>
<td>Output of a View (Images only)</td>
<td><img src="/misc/watchdog-ok.png" alt="Yes" /></td>
<td>Slider, Aspect Ratio, Cursor, Start Position</td>
<td>None</td>
</tr>
<tr class="odd">
<td><a href="http://drupal.org/project/slideshow_creator">Slideshow Creator</a></td>
<td><img src="/misc/watchdog-ok.png" alt="Yes" /></td>
<td>Next/Prev</td>
<td>Images that you manually select</td>
<td><img src="/misc/watchdog-ok.png" alt="Yes" /></td>
<td>Allows you to place slideshows anywhere within any text field. With speed, timeout, all jcycle effects, etc.</td>
<td>Style with html surrounding the slideshow and with css.</td>
</tr>
<tr class="even">
<td><a href="http://drupal.org/project/content_slider">Featured Content Slider</a></td>
<td><img src="/misc/watchdog-ok.png" alt="Yes" /></td>
<td>Numbers</td>
<td>Nodes of a chosen type</td>
<td><img src="/misc/watchdog-ok.png" alt="Yes" /></td>
<td>Animation speed, animation direction</td>
<td>None</td>
</tr>
<tr class="odd">
<td colspan="7"><h3 id="s-carousel-style-modules">Carousel style modules</h3></td>
</tr>
<tr class="even">
<td><a href="http://drupal.org/project/views_slideshow_liquid_slider">Views Slideshow Liquid Slider</a></td>
<td><img src="/misc/watchdog-ok.png" alt="Yes" /></td>
<td>Defined by Views Field</td>
<td>Output of a View</td>
<td><img src="/misc/watchdog-ok.png" alt="Yes" /></td>
<td>Duration, auto adjust height, responsive</td>
<td>Style with html surrounding the slideshow and with css.</td>
</tr>
<tr class="odd">
<td><a href="http://drupal.org/project/slider">Slider</a></td>
<td><img src="/misc/watchdog-ok.png" alt="Yes" /></td>
<td>Node titles</td>
<td>Nodes from a multi-value CCK noderef field</td>
<td><img src="/misc/watchdog-ok.png" alt="Yes" /></td>
<td>None</td>
<td>None</td>
</tr>
<tr class="even">
<td><a href="http://drupal.org/project/viewscarousel">Views Carousel</a></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td></td>
<td>Output of a View</td>
<td><img src="/misc/watchdog-ok.png" alt="Yes" /></td>
<td>Speed, orientation, easing effect</td>
<td>Two skins provided</td>
</tr>
<tr class="odd">
<td><a href="http://drupal.org/project/nodecarousel">Node Carousel</a></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td></td>
<td>Based on nodequeue or custom content</td>
<td>Optional</td>
<td>Speed, orientation</td>
<td>None</td>
</tr>
<tr class="even">
<td><a href="http://drupal.org/project/ajax_slideshow">Ajax Slideshow</a></td>
<td><img src="/misc/watchdog-ok.png" alt="Yes" /></td>
<td>Titles, Numbers, Images, Any field brought by views, Prev/Next, Custom</td>
<td>Any set of nodes or views object (controlled by a view)</td>
<td><img src="/misc/watchdog-ok.png" alt="Yes" /></td>
<td>transition type, transition speed, slide duration, w/wo navigation, w/wo border, viewport height, content source, w/wo teaser, advanced options.</td>
<td>node template based</td>
</tr>
<tr class="odd">
<td><a href="http://drupal.org/project/fancy_slide">Fancy Slide</a></td>
<td><img src="/misc/watchdog-ok.png" alt="Yes" /></td>
<td>Thumbnails to move to a given slide</td>
<td>Images from a node or a nodequeue</td>
<td>Optional</td>
<td>Slide duration, transition, transition duration, transition direction, manual/automatic advancement</td>
<td>Defaults provided</td>
</tr>
<tr class="even">
<td><a href="http://drupal.org/project/nivo_formatter">Nivo Formatter</a></td>
<td><img src="/misc/watchdog-ok.png" alt="Yes" /></td>
<td>Thumbnails, Next/Prev, Dot</td>
<td>Images from a Image Field</td>
<td>Optional</td>
<td>sliceDown, sliceDownLeft, sliceUp ,sliceUpLeft, sliceUpDown, sliceUpDownLeft, fold, fade, random, slideInRight, slideInLeft, boxRandom, boxRain, boxRainReverse, boxRainGrow, boxRainGrowReverse, speed, ...</td>
<td>3 Defaults provided, Nivo Slider themes.</td>
</tr>
<tr class="odd">
<td><a href="http://drupal.org/project/nivo_slider">Nivo Slider</a></td>
<td><img src="/misc/watchdog-ok.png" alt="Yes" /></td>
<td>Next/Prev, Numerical, Keyboard</td>
<td>Images uploaded through the module</td>
<td>Optional</td>
<td>sliceDown, sliceDownLeft, sliceUp ,sliceUpLeft, sliceUpDown, sliceUpDownLeft, fold, fade, random, slideInRight, slideInLeft, boxRandom, boxRain, boxRainReverse, boxRainGrow, boxRainGrowReverse</td>
<td>Includes the three default Nivo Slider themes</td>
</tr>
<tr class="even">
<td><a href="http://drupal.org/project/views_ticker">Views Ticker</a></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td></td>
<td>Output of a view</td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td>Speed, Direction, length of pause</td>
<td>Horizontal, vertical, BBC (typewriter-like), Fade</td>
</tr>
</tbody>
</table>

## Detailed analysis

#### Dynamic display block

Benefits over other modules:

- Multiple input possibilities: Images from a folder, node, Nodequeue, Blocks (e.g recent comments), Views
- 15 example themes available with number pager, prev/next pager, link pager, image pager and image/link and scrollable pager
- Commercial slideshow themes available
- Examples available of different settings
- Well documented
- In advanced slideshows you make fields available to the ddblock themes via preprocess functions (flexible)

Disadvantages or areas in need of improvement:

- Ajax loading of content
- In advanced slideshows you have to make fields available to the ddblock themes via preprocess functions

Of note:

- Uses the jQuery Cycle plugin

In summary:  
Flexible module with multiple input options. Multiple pager options. Most needed settings of jQuery Cycle plugin configurable in configuration page, otherwise you can use custom jQuery Cycle plugin settings field to set other settings. Can work together with jQuery Easing plugin. For tabbed content easy to combine with Quicktabs module.

#### Views Rotator

Benefits over other modules:

- Simple to install (doesn't require downloading a plugin as it's included in the module)
- Very clean and smooth UX
- This useful feature is achieved in very few lines of code - the module files are few and short.

Disadvantages or areas in need of improvement:

- The options are very limited.
- It includes the jQuery Cycle plugin at the start of its own js file, but given that there currently is no real solution for jQuery Plugin management in Drupal as yet, it's probably no worse than any other way of doing it.

Of note:

- This is a Views style plugin
- Uses the jQuery Cycle plugin

In summary:  
This is quite a minimalist approach to the rotating Views idea. There are no transition effect options and - most significantly - no tabs. Otherwise, it is a very clean solution.

#### Views Cycle

Benefits over other modules:

- Optional tabs that can be configured to hold the output of any field from your View.
- Offers all the transition effects that come with the full jQuery Cycle plugin as options
- If using tabs, you can choose whether the transition happens on hover or click of the tabs.
- Straight-forward configuration

Disadvantages or areas in need of improvement:

- Need to download the jQuery Cycle plugin separately, which some may find awkward.
- No prev/next links
- The skin that's provided with the module is quite buggy. Also, regardless of skin option, the output behaves strangely with regard to the ordered/unordered list of the main content - the first item gets its bullet or number displayed and the others don't.

Of note:

- This is a Views style plugin
- Uses the jQuery Cycle plugin

In summary:  
Views Cycle is a pretty powerful variation on the rotatable Views theme. The configurable tabs are a huge plus. Unfortunately they don't as yet work with combined fields - see [this issue](http://drupal.org/node/415026).

#### Views Slideshow

Benefits over the other modules:

- Extensible API
- Has an option for tabs
- Seems like it is highly configurable for different use cases.

Disadvantages or areas in need of improvement:

- Configuration options are quite confusing
- Lacking the generous selection of transition effects that Views Cycle provides, this module only provides fade or nothing, though that's probably enough for most people's needs. (However, as future plugins to Views Slideshow are made available, this should be alleviated.)
- Tab content is not configurable

Of note:

- This is a Views style plugin
- Uses its own js for the rotation
- Has an API that allows other plugins to extend the functionality

In summary:  
This module seems a little rough around the edges and could do with some clearer directions on the configuration screen. "Slideshow Mode: Thumbnail hover" means that you can have tabs that trigger the rotation, they do this on hover, and they contain the title and teaser of the node. When tried with a View that was outputting just title and an imagefield, the thumbnails contained the title and the imagefield and the rotating content consisted of title and teaser, which is not the expected behaviour. There's also a "Mouse hover" option which has one single radio button, "hover", but it seems there would be other options if the "Hover Intent" module were installed and enabled. Overall, highly configurable but not a very intuitive interface.

#### Views slideshow: Dynamic display block

Benefits over other modules:

- Mapping of field to slideshow themes. (v2.x)
- 6 example themes available with number pager, prev/next pager, link pager, image pager and image/link pager and scrollable pager or a combination of these (v1.x - v2.x)
- Commercial slideshow themes available (v2.x)
- Example module available with different pager settings (v2.x)
- Well documented (v1.x - v2.x)
- Possibility to make fields available to the slideshow themes via preprocess functions (flexible) (v1.x - v2.x)
- For more information see [project page](http://drupal.org/project/views_slideshow_ddblock).

Disadvantages or areas in need of improvement:

- Ajax loading of content

Of note:

- Uses the jQuery Cycle plugin

In summary:  
Flexible module with several available slideshow layouts. Multiple pager options. Most needed settings of jQuery Cycle plugin configurable in configuration page, otherwise you can use custom jQuery Cycle plugin settings field to set other settings. Can work together with jQuery Easing plugin. For tabbed content easy to combine with Quicktabs module.

#### Views Slideshow: ImageFlow

Benefits over other modules:

- Implements a CoverFlow-like slideshow
- Uses the API offered by Views Slideshow and Drupal.behaviors, so it's lightweight

Disadvantages or areas in need of improvement:

- Requires a third-party JavaScript plugin, which has a small fee for commercial uses
- The "reflection" option normally offered by the plugin is not currently available

#### Slideshow Creator

Of note:

- Uses jQuery Plugin module to add the Cycle plugin.
- Allows slideshows to be placed anywhere within text content by use of an input filter.
- Allows slideshows to consist of arbitrary images or entire directories of images.

In summary:  
This module involves creating a new input format so that you can place code like this into your node body: ` [slideshow: 2, img=|http://drupal.org/sites/all/themes/bluebeach/logos/drupal.org.png|drupal.org|Drupal|The ultimate CMS. Download it now!|Drupal|, img=|http://www.mysql.com/common/logos/mysql_100x52-64.gif|http://www.mysql.com|MySQL|Free and reliable SQL server and client.|_self|, dir=|files/|yes||Generic Photos|Aren't they great?||] `

#### Featured Content Slider

Of note:

- Creates up to 3 blocks of sliding nodes
- Uses its own js code which is not jQuery

In summary:  
This pulls nodes of a given type into a slider block. You can create up to 3 blocks using different node types for each. The JavaScript code suggests there is ajax loading functionality. Also, the js code is needlessly bulky as it does not leverage jQuery at all, never mind jQuery plugins. Otherwise, a fairly smooth UX.

#### Slider

Of note:

- Uses its own js in conjunction with jQuery.scroll.js to achieve a carousel effect.

In summary:  
There's a fair bit of set-up involved here to create a slideshow and it's based on CCK multi-value nodereference fields. Not very flexible.

#### Easy Slider

Of note:

- Uses the Easy Slider jQuery plugin, which ships with the module.

In summary:  
Very similar to Slider, except that it works with Views.

#### Views Carousel

Benefits over the other modules:

- Easy set-up
- Provides good basic styles

Disadvantages or areas in need of improvement:

- Easing effect option is a textfield with directions sending user to a jQuery docs page for options; one has to scroll down and search to eventually find this: 'There are two built-in values, "linear" and "swing".' - one would expect more options when being sent all the way to another site to find out what they are.

Of note:

- This is a Views style plugin
- Uses the jCarousel jQuery plugin

In summary:  
A good, clean UI with straight-forward configuration options, an exemplary implementation of the jCarousel jQuery plugin for Drupal sites.

#### Node Carousel

Benefits over the other modules:

- Apparently has an AJAX option (untested)

Disadvantages or areas in need of improvement:

- The module is not well maintained and the documentation is out of date.
- No functional 6.x version available - looks like development simply stopped on this before it was ready
- No Views integration

Of note:

- Works with Nodequeue
- Uses the jCarousel jQuery plugin

In summary:  
There is either a git tagging problem or a lack of adequate documentation: - the jcarousel plugin does not come with this module although it exists in git, and there are no instructions as to where to get it or where to put it. With the plugin in the module directory, Nodecarousel did not do anything. Also there were numerous php notices.

#### Ajax Slideshow

Benefits over other modules:

- Ajax-based slideshow which means scalability. The slideshow content can grow bigger without negatively impacting the page load-time.
- Slides can contain any content item (node) rather than images only
- Content and sequence ease of control due to the utilization of the views module for managing the slide set.
- Plug & Play – standard installation and the slideshow is up.

Disadvantages or areas in need of improvement:

- Need to implement additional out-of-the-box tabs styles.

Of note:

- Uses Views and JQuery plugins

In summary:  
Straightforward, easy to install and manage module that allows sequential presentation of any set of content items. Performance is not dependent on the number of content items selected.

#### Fancy Slide

Features:

- Input from either a single node or from a nodequeue.
- Large number of settings.
- Integrates with imagecache to resize images automatically.
- Control bar with automatic thumbnails and image descriptions.
- 'Pluggable' transitions to provide the possibility to add further transitions using jQuery.
- Theme functions exposed to theme developers to build straight into themes.

Areas in need of improvement:

- No views integration.

In summary:

An early but stable slideshow module that aims to provide a nicer, fancier interface to the end user than other offerings, while maintaining an array of customisation options. More work is needed to bring views integration to the module.

## Bottom line

You often remarks like this in project descriptions and issue queues:  
- "EasySlider is being developed into a views plugin"  
- "I'm thinking of rejiggering it as a views extension" (Nodecarousel)  
- "I am planing its integration with Views" (Featured Content Slider)  
There has already been so much duplicated effort here, it's time for that to stop and for some consolidation to happen. Within the somewhat broad use case of eye-catching, rotating content, there are two distinct use cases, meaning justification for at MOST two modules here:

1.  Passive user: throw featured content at them while they're on your front page
2.  Active user: allow users to navigate / scroll through content to find what they're looking for (e.g. thumbnail images in a gallery)

Two modules that exemplify these two use cases are well {Views Cycle OR Views Rotator} and Views Slideshow respectively. There's no reason why features from Views Rotator / Views Cycle / Views Slideshow couldn't be incorporated into one module and likewise with all the carousel/slider-type modules for the latter use case.

There is also a strong need for a standard way of including jQuery plugins, as per [this thread](http://drupal.org/node/315100). Wouldn't it be awesome if you could just choose "jQuery plugin" as your Views style and then in the settings for that style you would choose which plugin to use, e.g. Cycle, Accordion or Carousel. Of course there are different config options for each of those but... maybe getting closer to that ideal isn't too wacky an idea.
