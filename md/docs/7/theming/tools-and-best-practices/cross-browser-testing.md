---
title: "Cross-browser testing"
source_url: "https://www.drupal.org/docs/7/theming/tools-and-best-practices/cross-browser-testing"
page_type: page
last_updated: "Last updated on 26 November 2016"
published: "2010-11-25T12:25:56+00:00"
modified: "2016-11-26T13:28:33+00:00"
breadcrumb: ["Drupal 7", "Theming Drupal 7", "Tools and best practices"]
fetched: "2026-10-21T08:53:49Z"
raw: "raw/docs/7/theming/tools-and-best-practices/cross-browser-testing.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Cross-browser testing

Cross-browser testing refers to the practice of testing your theme in multiple browsers to ensure that each browser renders pages as intended. At times, different rendering agents (Gecko, WebKit, etc.) render pages in a different manner. First, make sure that your theme follows [Core Theme Candidate Requirements](/node/769692). These tips should allow you, the themer, to avoid these issues.

## Target browsers

Selecting target browsers for your theme mainly comes down to audience. It's good practice to review the list of top browsers by market share (see [W3Schools](http://www.w3schools.com/browsers/browsers_stats.asp) for statistics and trends). Browser versions can also play a role in design, as older browser versions tend not to support some of the newer specifications. Many people still use Internet Explorer 6 which does not always follow current web standards.

At times, due to costs, time or other constraints, it may be feasible to provide only partial support for a certain browser. One example of this would be not including CSS 3 transitions in Internet Explorer 6. This degraded support is fine for a theme. In addition, you might want to consider alerting the user to the fact that he or she is running an outdated browser. However, as stated above, some people may not have a choice in the matter.

## Local browser testing

Many browsers allow you to download older, unsupported versions of their browser. For example, older versions of Firefox's 3.x branch can be found [here](http://releases.mozilla.org/pub/mozilla.org/firefox/releases/). When downloading these older versions, do be careful to limit your usage, as these versions may have security vulnerabilities. If you are worried about viruses on the web, another option would be to run the older versions in a sandboxed environment using [Sandboxie](http://www.sandboxie.com/) or other similar programs. Finally, the best way to isolate your computer from your testing programs would be to install the older browsers in a [virtual machine](http://en.wikipedia.org/wiki/Virtual_machine).

### Internet Explorer

Usually, when a newer version of Internet Explorer is installed on a computer, the older version is removed. However, for web developers, this can be a problem as they cannot check their site in previous versions. One possible solution would be to use [modern.IE](https://www.modern.ie) to test IE 6 through 11 locally through the use of Virtual Machines.

## Remote browser testing

If you do not want to install multiple browsers on your computer, there are online services which allow you to view your website with other browsers. However, a disadvantage of most of these services is that you need to have a public web server on which your test Drupal installation with your theme can run on.

A comprehensive browser testing tool [BrowserStack](http://www.browserstack.com) is available at a reasonable price for unlimited interactive testing of public or private/local hosted sites. They provide Mac and Windows virtual machines with several versions of browsers and even mobile device emulators for real-time interactive previewing of your sites. They offer a free trial version with a time limit.

Another option to test your theme would be to use [Adobe BrowserLab](https://browserlab.adobe.com/en-us/index.html#). However, you must have a CS5 Live license in order to use the service.

One option for previewing your theme's output in static screenshots of various browsers rendering your page is a service like [Browsershots](http://browsershots.org/). This service allows you to check your theme from multiple browsers and operating systems. However, you cannot click on screenshots, move through your pages or use dynamic page elements. In addition, every day, you can only check a particular site a limited number of times before it requires you to purchase a paid membership.

There are many other services which can be used. Some of these require payment while others allow for free trials. A list of these services can be found [here](http://www.lofitrading.com/15-highly-useful-resources-for-cross-browser-testing/) and [here](http://jpedroribeiro.com/2010/06/cross-browser-testing-resources/).
