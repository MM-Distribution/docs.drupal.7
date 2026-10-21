---
title: "Why test"
source_url: "https://www.drupal.org/docs/7/testing/why-test"
page_type: page
last_updated: "Last updated on 30 November 2016"
published: "2007-12-27T06:01:40+00:00"
modified: "2016-11-30T11:16:05+00:00"
breadcrumb: ["Drupal 7", "Automated testing for Drupal 7"]
fetched: "2026-10-21T08:12:24Z"
raw: "raw/docs/7/testing/why-test.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Why test

You should write SimpleTests for your modules to ensure quality. SimpleTests allow you, the developer, to quickly test your module after changes to make sure it still works. After all, have you really tested **all** possibilities for error? Of course not; it would be very tedious and time-consuming. So, the logical thing to do is to write a SimpleTest for it.

### Incompatibilities

Say, on your issue queue, you get a report that your module is incompatible with another one. What can you do? You can install that module, run your tests, and see which ones report errors. This will allow you to trace bugs much more efficiently.

### Errors

Say that you make an error in your module that causes it to not function properly, but you overlook it. This is BAD. You may even try to make a stable release of it in its broken state, while you're ignorant of the problem. A SimpleTest will allow you to run automated tests on your module to make sure that, indeed, everything still functions properly.

### Others

This is an open source community, and helping others is the core of what Drupal is about. What if somebody else is using your module on their site, and they get an error? If you have a SimpleTest file included, they can run automated tests on your module and give you the results, helping you to debug. This way, you get fewer support requests, because people may find that it's something in their setup that's causing the problem.

## What to test?

What should be tested? Well, it can test anything that your module does. Perhaps your module prints a message after a user has viewed a node of type x. Well then, create a SimpleTest that creates a node of type x, views it, and confirms that the message shows up. Anything that your module does, SimpleTest should be able to test to make sure it's working properly: it is up to you to write these tests.
