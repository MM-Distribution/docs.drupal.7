---
title: "Mobile-specific website"
source_url: "https://www.drupal.org/docs/7/mobile/mobile-specific-website"
page_type: page
last_updated: "Last updated on 24 August 2016"
published: "2011-12-29T15:08:43+00:00"
modified: "2016-08-24T09:05:01+00:00"
breadcrumb: ["Drupal 7", "Mobile guide for Drupal 7"]
fetched: "2026-10-21T07:17:17Z"
raw: "raw/docs/7/mobile/mobile-specific-website.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Mobile-specific website

For some projects, you may want to have a mobile web site that uses different markup and layout from the desktop site - for instance, it may be easier to manage two web sites than to create a responsive layout for your desktop site, or you want to use a mobile web framework like jQuery Mobile or Sensa Touch for mobile users.

## Mobile Tools module

The most useful module for building separate desktop and mobile sites for Drupal is [Mobile Tools](http://drupal.org/project/mobile_tools), which has many different features:

- **Web Browser detection** - is the user on a desktop browser or a mobile browser?
- **Mobile domain redirection** - route users to the correct domain.
- **Mobile-only themes** - different devices may get different themes.
- **Mobile site availability** - let mobile users on full site know there is a mobile version.
- **Mobile contex**t - offer different functionality to mobile users.

There are a few modules available that have limited scope relative to the Mobile Tools module. Their functionality may match your website’s requirements.

- [Mobile Theme module](http://drupal.org/project/mobile_theme)
- [Switchtheme module](http://drupal.org/project/switchtheme)

## Browser Detection - Browscap module

The [Browscap](http://browsers.garykeith.com/) project maintains a list of web browsers on both mobile and desktop devices along with their capabilities. The [Browscap](http://drupal.org/project/browscap) Drupal module integrates with the Browscap project to make this web browser data available to other Drupal modules. Three modules which use the Browscap module are [Mobile Tools](http://drupal.org/project/mobile_tools), [Switch Theme](http://drupal.org/project/switchtheme) and [Mobile Switch](/project/mobile_switch).

## Mobile Detection and Caching

Mobile device detection gets more complicated when you are using caching, especially with an external cache such as Varnish.

- [Mobile Detection with Varnish and Drupal](http://fangel.github.com/mobile-detection-varnish-drupal/) - interesting discussion written by Morten Fangel of issues faced when returning different HTML content to mobile and desktop browsers with Varnish.

## Mobile themes

When doing domain switching between a desktop and mobile website, it is usually makes sense to use a separate theme for the mobile website. Here are a few mobile themes available on drupal.org:

- [mobile](http://drupal.org/project/mobile)
- [iUi](http://drupal.org/project/iui) (D6 only)
- [Nokia mobile](http://drupal.org/project/nokia_mobile) (D6 only)
