---
title: "Native mobile apps"
source_url: "https://www.drupal.org/docs/7/mobile/native-mobile-apps"
page_type: page
last_updated: "Last updated on 22 September 2016"
published: "2011-12-29T14:51:33+00:00"
modified: "2016-09-22T01:57:11+00:00"
breadcrumb: ["Drupal 7", "Mobile guide for Drupal 7"]
fetched: "2026-10-21T07:17:02Z"
raw: "raw/docs/7/mobile/native-mobile-apps.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Native mobile apps

## Native Mobile Application Development

Drupal isn't just a web-based content management system - you can use Drupal as the backend for mobile application development. Drupal can contain your content, business logic, user management, and search functionality, and your app can be a front end that talks to Drupal using the Services module.

## Native Mobile Application Capabilities

Building a native mobile application gives you two different things that mobile web applications don't have - distribution through mobile app stores and access to native functionality. Some things you can get with a native mobile application are:

- Charge for app in Google Play or App Store
- In app purchase and subscriptions through the App Store, Google Play, or other app stores
- In app advertising from native mobile app networks
- Access to the device's camera for images or video
- Access to the device's file system for caching
- Access to the device's contacts
- Native map functionality
- Device's accelerometer, gyroscope, compass, and map
- Background location awareness (on iOS 5)
- Image filters (such as sepia, halftone, etc.) (on iOS 5)

Many of these things will be available to mobile web applications in the future, but native mobile applications are the only way to get many of these things right now.

## Mobile Application Strategy

Before starting your mobile application development project, it helps to determine which platforms you want to target, and whether you want to use platform-specific capabilities within your app. For instance, with iOS, you can have a mobile application that gets activated when your users cross a location boundary. Or on Android, your mobile application can be integrated with other Android applications using the Android Intent framework. Sometimes, you can access this functionality through cross-platform native mobile application development tools, but then you lose many of the advantages of cross-platform development.

You should also consider what technical skills your team has before choosing a solution. Android applications are typically written in Java, and iOS applications are written in Objective-C. These languages are significantly different from a typical Drupal developer skillset of PHP/SQL/HTML/CSS/JS - to reuse existing language skills, consider using either Titanium or PhoneGap to develop your mobile applications.

## Developing Native Apps for iPhone/iPad/iPhone Touch

Apple's devices run the iOS operating system, and native apps running on iOS are generally written in Objective-C or Swift. You will need a Mac for iOS development that is capable of running Apple's XCode IDE. Connecting to a Drupal site running the Services module is very straightforward, especially with one of two HTTP libraries:

- [**AFNetworking**](https://github.com/AFNetworking/AFNetworking)
- [**ASIHTTPRequest**](https://github.com/pokeb/asi-http-request)
- [**Alamofire(Swift)**](https://github.com/Alamofire/Alamofire)

[Waterwheel Swift](https://github.com/kylebrowning/drupal-ios-sdk) provides a layer of abstraction on top of AlamoFire for working with Drupal nodes, files, users, and views. 

Things to consider when developing a native RESTful iOS app are caching strategies, using asynchronous methods to download data and then refreshing data as downloads complete, pre-fetching data on application load, and managing network timeout issues.

For more information about developing native mobile apps for the iPhone or iPad:

Links for these projects

- [Waterwheel Swift (7 and 8 Obj-c and Swift demo included)](https://github.com/acquia/waterwheel-swift)
- [Drupal 7 Map App Example Project for iPhone and iPad](http://www.jefflinwood.com/2012/03/drupal-7-map-app-example-project-for-iphone-and-ipad/) - Simple iOS app that uses Drupal 7, MapKit, and AFNetworking by Jeff Linwood

Other Examples/Projects

DrupalRESTKit : <https://github.com/vivekvpandya/DrupalRESTKit>

Tips&Tricks AFNetworking : <https://github.com/vivekvpandya/TipsAndTricksAFNetworkingDrupal>

Tips&Tricks NSURLSessionAPI : <https://github.com/vivekvpandya/TipsAndTricksCFNetworkingDrupal>

Demo : <https://www.youtube.com/watch?v=iny71Kwgn_I>

## Developing Native Apps for Android

- [DrupalCloud](https://github.com/INsReady/DrupalCloud) - Android library for Drupal Services by [INsReady Inc. (引锐信息科技有限公司)](http://drupal.org/node/1327988)
- [My Android application for TShirtSlayer](http://dgtlmoon.com/drupal-android-xmlrpc-application) - discussion of an Android, Drupal, XML-RPC app, with a [source repository on GitHub](https://github.com/dgtlmoon/tshirtslayer_android)
- [Building Android Apps with Drupal](https://www.youtube.com/watch?v=9rY1sTvGYYM) - Presentation at DrupalCon Denver 2012 by [Jingsheng Wang](http://drupal.org/user/228712)
- [Architect your business with Drupal and Android](http://chicago2011.drupal.org/sessions/architect-your-business-drupal-and-android) - Business and strategy presentation from DrupalCon Chicago 2011 by [Jingsheng Wang](http://drupal.org/user/228712)
- Developing Native Apps with Titanium

[Appcelerator Titanium](http://www.appcelerator.com/) is a mobile application development tool that uses Javascript as the development language. Titanium produces both iOS and Android applications from one code base.

- [Introduction to Using Titanium with Drupal Services](http://fldrupalcamp.org/program/sessions/introduction-to-using-titanium-with-drupal-services) - presentation by Stephen Barker at Florida DrupalCamp 2012
- [Rapid native mobile app development with Drupal and Titanium / PhoneGap](http://2012.pnwdrupalsummit.org/sessions/rapid-native-mobile-app-development-drupal-and-titanium-phonegap) - presentation by Scott Falconer at the Pacific Northwest Drupal Summit 2012
- [Titanium API Group](http://groups.drupal.org/titanium-api) Discussion Group for Drupal and Titanium
- [Developing Apps for iPhone/iPad/Android using Drupal as Base System](http://chicago2011.drupal.org/sessions/developing-apps-iphone-ipad-android-using-drupal-base-system) - Presentation on using Titanium to build iPhone and Android apps for Drupal by Sumit Kataria
- [Creating an iPhone App for a Drupal Website](http://zengenuity.com/blog/a/201105/creating-iphone-app-drupal-website)- case study about building an iPhone app for Drupal using Titanium
- [DrupalCon Chicago 2011 App Source Code](https://github.com/palantirnet/drupalcon_mobile) - large example Titanium application for Drupal
- [Mobilizing DrupalCon Chicago](http://www.palantir.net/blog/mobilizing-drupalcon-chicago) - Larry Garfield shares a case study about building the DrupalCon Chicago 2011 app with Titanium

## Developing Native Apps with PhoneGap

[PhoneGap](http://www.phonegap.com/) is a native application wrapper for mobile web content that also provides access to device-level services. PhoneGap supports the iOS, Android, Windows Phone, and BlackBerry mobile application operating systems, and can run on both smartphones and tablet devices.

Several projects for integrating Drupal with PhoneGap exist:

- [Drupal Plugin for PhoneGap for iOS](https://github.com/jefflinwood/Drupal-Plugin-for-PhoneGap-for-iOS), which makes the Drupal iOS SDK accessible through PhoneGap.
- [PhoneGap module](http://drupal.org/project/phonegap) which provides both an Android application and a Drupal 7 module for creating/browsing nodes from PhoneGap
- [DrupalGap](http://drupal.org/project/drupalgap) - An open source mobile application development kit for Drupal websites, with PhoneGap and jQueryMobile.

## Additional Resources

Several different ways of integrating Views into mobile applications exist - depending on what you are trying to accomplish, you may want to consider one of these modules

- Web services
  - [Services module](http://drupal.org/project/services)
  - [Content API module](http://drupal.org/project/contentapi) - provides additional ways of accessing content through Services
- Using Drupal Views
  - [Services Views](http://drupal.org/project/services_views) - provides a Views resource for the Services module
  - [Views Datasource](http://drupal.org/project/views_datasource) - provides representations in JSON, XML, RDF, xHTML microformats, Atom, and several other formats
  - [Views Atom](http://drupal.org/project/views_atom) - Creates an Atom-formatted View for the "Feed" display type
