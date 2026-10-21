---
title: "Responsive web design"
source_url: "https://www.drupal.org/docs/7/mobile/responsive-web-design"
page_type: page
last_updated: "Last updated on 10 January 2024"
published: "2011-12-29T15:09:51+00:00"
modified: "2024-01-10T05:39:13+00:00"
breadcrumb: ["Drupal 7", "Mobile guide for Drupal 7"]
fetched: "2026-10-21T07:17:48Z"
raw: "raw/docs/7/mobile/responsive-web-design.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Responsive web design

This page lists resources for Responsive Web Design, a strategy for optimizing the display of a web site using CSS and JavaScript to respond to different device capabilities.

## Background information

- [A List Apart: Responsive Web Design - Ethan Marcotte](https://www.alistapart.com/articles/responsive-web-design/)
- [Drupal Responsive Design & Mobile First Design Strategy](https://www.daymuse.com/blogs/mobile-first-design-drupal)
- [Mobile First - Luke Wroblewski](https://www.lukew.com/ff/entry.asp?933)
- [Why Design Mobile First?](https://needmoredesigns.com/blog/why-design-mobile-first)
- [Head First Mobile Web](https://www.oreilly.com/library/view/head-first-mobile/9781449324773/)
- [Detection tutorial](https://www.html5rocks.com/en/tutorials/detection)

### Terms

- Browser detection: determining the identity of the user agent (web browser) being used to visit that page.
- Device detection: determining the hardware that user agent is running on.
- Feature detection: determining the capabilities of the user agent in question
- Capability detection: combining aspects of feature, device and bandwidth detection, to test the overall capabilities of the viewport in question.

### Current Preferred Approach

Feature detection is currently considered best practice and most [Future Friendly](http://futurefriend.ly)

Browser detection is less used due to browsers being able to “pretend” to be another browser by editing their User Agent string.

Device detection becomes unmanageable as the number of devices grows.

The features of the viewports (what it can actually do) are more important for adjusting the display of information than the name of the viewport of the platform it runs on.

### Solutions

- [Modernizr](http://www.modernizr.com/) combines feature detection with conditional resource loading.
- [Modernizr 7.x-3.x](http://drupal.org/project/modernizr) supports Modernizr.load() — any theme or module can use it.
- [Categorizr](http://www.brettjankord.com/2012/01/16/categorizr-a-modern-device-detection-script/) – A server-side device detection script
- [Agent IQ](http://www.agent-iq.com) - A server-side device detection script
- [Detector](http://detector.dmolsen.com/) - A server-side device detection script
- [Mobile Tools](https://www.drupal.org/project/mobile_tools), to assist in making adjustments to your site based on the visitor's device
- [Mobile Switch](https://www.drupal.org/project/mobile_switch)
- [Mobile Theme](https://www.drupal.org/project/mobile_theme)

## Testing Tools for desktop, laptop & mobile

- <http://quirktools.com/screenfly>
- <http://ipadpeek.com/>
- Responsive Design Testing Tool - <http://mattkersley.com/responsive/>
- Opera Mobile Emulator - <http://www.opera.com/developer/tools/mobile/>
- Responsinator: <http://www.responsinator.com>

## Responsive grid systems

- 1140 CSS Grid <http://cssgrid.net>
- Bootstrap <http://getbootstrap.com>
- Tailwindcss <https://tailwindcss.com/>
- Columnal <http://www.columnal.com>
- Fluid Baseline Grid <http://fluidbaselinegrid.com>
- Foundation <http://foundation.zurb.com>
- Golden Grid System <http://goldengridsystem.com>
- Gridset <http://www.gridsetapp.com/>
- Skeleton <http://www.getskeleton.com>
- Susy <http://susy.oddbird.net>
- Singularity <http://singularity.gs>
- Zen Grids <http://zengrids.com>
- Yahoo Pure.CSS <http://purecss.io/>

## Responsive themes

### Drupal 6 & 7

- AdaptiveTheme <http://drupal.org/project/adaptivetheme>
- Omega <http://drupal.org/project/omega>
- Zen (7.x-5.x) <http://drupal.org/project/zen>
- Zero Point <https://www.drupal.org/project/zeropoint>

### Drupal 7

- ABC <https://www.drupal.org/project/abc>
- Arctica <http://drupal.org/project/arctica>
- Aurora <http://drupal.org/project/aurora>
- Boilerplate <http://drupal.org/project/boilerplate>
- Bootstrap <http://drupal.org/project/bootstrap>
- Corked Screwer <http://drupal.org/project/corkedscrewer>
- Foundation <http://drupal.org/project/zurb-foundation>
- Mojo <http://drupal.org/project/mojo>
- Sasson <http://drupal.org/project/sasson>
- Square Grid <http://drupal.org/project/squaregrid>
- Groundwork <http://drupal.org/project/groundwork>
- Corporate Clean <http://drupal.org/project/corporateclean>
- Mayo <http://drupal.org/project/mayo>
- Professional Theme <http://drupal.org/project/professional_theme>
- Mix and Match <http://drupal.org/project/mix_and_match>
- Premium Responsive <http://drupal.org/project/responsive>
- Yahoo Pure.CSS Framework <https://www.drupal.org/project/pure_css>
- **Drupal 7 Responsive Theme Search**: [https://www.drupal.org/project/project_theme?f%5B0%5D=&f%5B1%5D=&f%5B2%5...](https://www.drupal.org/project/project_theme?f%5B0%5D=&f%5B1%5D=&f%5B2%5D=drupal_core%3A103&f%5B3%5D=sm_field_project_type%3Afull&text=responsive&solrsort=iss_project_release_usage+desc&op=Search)

## Responsive theme generators

- <http://responsify.it/>

## Responsive tables

- [Responsive tables - ZURB](http://www.zurb.com/playground/responsive-tables)
- [Responsive Data Tables - Chris Coyier](http://css-tricks.com/responsive-data-tables)
- [A Responsive Design Approach for Complex, Multicolumn Data Tables](http://filamentgroup.com/lab/responsive_design_approach_for_complex_multicolumn_data_tables)

## Responsive images

Jason Grisby has an excellent series of posts on the problems of responsive images: <http://blog.cloudfour.com/responsive-imgs/>

Jeremy Keith’s [two golden rules](http://adactio.com/journal/4997) for dealing with responsive images:

1.  The small image should be default.
2.  Don’t load multiple images.

### Possible solutions

- [Responsive Images: Experimenting with Context-Aware Image Sizing](http://filamentgroup.com/lab/responsive_images_experimenting_with_context_aware_image_sizing)
- [Adaptive Images](http://adaptive-images.com/)
- [Responsive Images: How they Almost Worked and What We Need](http://www.alistapart.com/articles/responsive-images-how-they-almost-worked-and-what-we-need)
- [Proposed `<picture>` element and polyfill](http://www.w3.org/community/respimg/2012/03/15/polyfilling-picture-without-the-overhead)
- [Foresite.js](https://github.com/adamdbradley/foresight.js)
- [Responsive images - a Drupal implementation](http://fourkitchens.com/blog/2013/02/07/responsive-images-drupal-implementation)

### Drupal modules

- [Picture](http://drupal.org/project/picture) is part of Drupal 8 core and is backported to Drupal 7. It follows responsive design principles. In order to use it, select the 'Picture' instead of 'Image' formatter when managing the display of a content-type.
- Adaptive Image <http://drupal.org/project/adaptive_image>
- Adaptive Image Styles <http://drupal.org/project/ais>
- Client-side adaptive image <http://drupal.org/project/cs_adaptive_image>
- Responsive Images <http://drupal.org/project/responsive_images> (not maintained any more)
- Responsive images and styles <http://drupal.org/project/resp_img> (replaced by “Picture”)
- Fluid html grid that can be used with responsive design techniques <http://drupal.org/project/views_fluid_grid>

### Responsive thumbnail galleries

- [How to Build a Responsive Thumbnail Gallery](http://designshack.net/articles/css/how-to-build-a-responsive-thumbnail-gallery)

### Responsive background images

- [Better background images for responsive web design](http://elliotjaystocks.com/blog/better-background-images-for-responsive-web-design)
- [Anystretch jQuery plugin](https://github.com/danmillar/jquery-anystretch)

## Responsive slideshows

- Example of a "lightweight" slideshow: <http://yiibu.com/articles/rethinking-the-mobile-web/page-3.html#slideshow>
- Flexslider module <http://drupal.org/project/flexslider> (based on <http://flex.madebymufffin.com>)
- Full screen image slideshow: <http://buildinternet.com/project/supersized>

## Responsive videos

- CSS only <http://amobil.se/2011/11/responsive-embeds/>
- FitVids module <http://drupal.org/project/fitvids> (based on <http://fitvidsjs.com>)

## Responsive text

- FitText module <http://drupal.org/project/fit_text> (based on <http://fittextjs.com>)
- Responsive Typography, reference of core concepts by Tim Brown - <http://nicewebtype.com/notes/responsive-typography/>

## Responsive navigation menus

Simple navigation menus lend themselves to larger display platforms (laptops) as well as smaller displays (smartphones). In general, drop down menus are not often used on smaller displays (smartphones) since visual space is limited.

Usually, you find drop down menus converted to stacked vertical lists when the display detected is a smartphone.

Excellent background info:

- [Responsive navigation patterns](http://bradfrostweb.com/blog/web/responsive-nav-patterns)
- [Mobile dropdown jQuery plugin](https://github.com/joggink/jquerymobiledropdown)

### Possible Solutions

A common method to provide a more sophisticated menu system for both large and small displays is to use conditional menu blocks. Be aware that complex, lengthy menus do not lend themselves to small displays.

### Drupal Modules

- [Menu Block Module](http://drupal.org/project/menu_block)
- [Better Jump Menus](http://drupal.org/project/jump_menu) to easily create hierarchical select jump menus
- [Superfish](http://drupal.org/project/superfish)
