---
title: "Web-based mobile apps"
source_url: "https://www.drupal.org/docs/7/mobile/web-based-mobile-apps"
page_type: page
last_updated: "Last updated on 24 August 2016"
published: "2011-12-29T14:58:33+00:00"
modified: "2016-08-24T09:05:01+00:00"
breadcrumb: ["Drupal 7", "Mobile guide for Drupal 7"]
fetched: "2026-10-21T07:17:32Z"
raw: "raw/docs/7/mobile/web-based-mobile-apps.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Web-based mobile apps

Web apps are HTML5, CSS, and JavaScript-based apps running in mobile browsers. There are two different ways of building mobile web applications that work with Drupal - integrated with Drupal at the theme layer, or a standalone mobile web app that talks to Drupal using web services. Either approach will work for building mobile web applications, but it is easier to get started by integrating the mobile web app into Drupal as a theme.

## Mobile Web Toolkits

Several different mobile web application toolkits exist, with varying degrees of support for smartphones, tablets, and feature phones. The two general approaches to building a mobile web application toolkit are to work from HTML5/CSS (jQuery Mobile, jQTouch), and to work from Javascript (Sencha Touch, Enyo). The HTML5/CSS toolkits are somewhat easier to adapt to Drupal. The Javascript frameworks don't integrate with Drupal at the theming layer, so the process for development is similar to building a native mobile app.

- [jQuery Mobile](http://jquerymobile.com/)
- [Enyo JS](http://enyojs.com/)
- [Sencha Touch](http://www.sencha.com/products/touch)
- [jQTouch](http://www.jqtouch.com/)
- [Jo](http://joapp.com/)
- [jqMobi](http://www.jqmobi.com/)
- [DrupalGap](http://www.drupalgap.org/ "Build Web Applications for Drupal with DrupalGap")

## jQuery Mobile and Drupal

jQuery Mobile is not only one of the most popular mobile web application frameworks, it's also the easiest to get integrated with Drupal, because there are several modules and themes:

- [jQuery Mobile Theme](http://drupal.org/project/mobile_jquery)
- [jQuery Mobile UI module](http://drupal.org/project/jquerymobile_ui)
- [Google Analytics for jQuery Mobile](http://drupal.org/project/ga_jquerymobile) - fixes Google Analytics reporting for jQuery Mobile projects, works with the Google Analytics module
- [jQuery Mobile Views Integration](http://drupal.org/project/views_jqm) - creates jQuery Mobile list markup from Drupal views
- [DrupalGap](https://drupal.org/project/drupalgap "Build Mobile Applications for Drupal with DrupalGap") - Application Development Kit for Drupal with jQuery Mobile

## Additional Resources for jQuery Mobile and Drupal

- [drupal.api.js](http://github.com/travist/drupal.api.js) - An object oriented JavaScript API library to interact with Services 3.x. Great for use within Drupal Mobile applications such as PhoneGap, etc.
- [Building a mobile site in 45 minutes using Mobile Tools and Jquery Mobile](http://2012.fldrupalcamp.org/sites/default/files/slides/drupal-jqm.pdf) - presentation by Michael Herchel at Florida Drupal Camp 2012
- [jQuery Mobile](http://drupalcampnh.org/sessions/jquery-mobile) - presentation by Jason Savino on the Mobile jQuery theme and the jQuery Mobile module at DrupalCamp New Hampshire 2011
- [Building a mobile Drupal site](http://fleetthought.com/presentation-building-mobile-drupal-site) - presentation by Mark Jarrell at DrupalCamp Nashville 2011
- [Drupal on the go with jQuery Mobile](http://chicago2011.drupal.org/sessions/drupal-go-jquery-mobile) - presentation by Tim Cosgrove and Brian McMurray at DrupalCon Chicago 2011
- [960.gs on jQuery Mobile](http://jeromeetienne.github.com/jquery-mobile-960/) - not a Drupal module, but still useful if you are planning to build web applications for tablets with jQuery Mobile
- [jDrupal](http://www.jdrupal.org) - JavaScript Library for Drupal REST (Services)

## Converting D7's default XHTML to HTML5

The easiest way to convert Drupal 7’s default XHTML markup into HTML5 is to use a theme that is written in HTML5. If you are building your own custom theme for a site, consider using a HTML5 base theme as it will have done all the hard work to convert the default markup into HTML5 for you.

Search Drupal.org for [HTML5 themes](http://drupal.org/project/themes?filters=bs_project_sandbox%3A0&solrsort=sis_project_release_usage%20desc&text=html5).

If you would like additional parts of Drupal to be converted to HTML5 (like Drupal’s search forms, etc.), you can try the [HTML5 Tools](http://drupal.org/project/html5_tools) module. This module should work with any HTML5 theme.
