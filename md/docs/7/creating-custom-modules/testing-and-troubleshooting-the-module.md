---
title: "Testing and troubleshooting the module"
source_url: "https://www.drupal.org/docs/7/creating-custom-modules/testing-and-troubleshooting-the-module"
page_type: page
last_updated: "Last updated on 22 December 2016"
published: "2011-03-24T19:48:54+00:00"
modified: "2016-12-22T06:07:27+00:00"
breadcrumb: ["Drupal 7", "Creating custom modules in Drupal 7"]
fetched: "2026-10-21T07:23:14Z"
raw: "raw/docs/7/creating-custom-modules/testing-and-troubleshooting-the-module.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Testing and troubleshooting the module

It's time to enable and fully test your module!

### Enable the module

Go to *Modules*, or `http://example.com/admin/modules`, and scroll down to the bottom of the list in the 'Other' category. You should see the module 'Current posts.' Click the checkbox to enable *Current posts*, and save your configuration. Now you should see a link to *Help* beside the module name. Click it to see the help text you entered in `current_posts_help`.

### Enable the block

Next, navigate to *Structure \> Blocks*, or `http://example.com/admin/structure/block`. Scroll down to the bottom of the list. Among the disabled blocks, you should find the name, 'Current posts'. Set its location for one of the page regions and save. Navigate to another page like your homepage to see your block. Congratulations! You have written a working module.

### Troubleshooting

If you get a "white screen" or a PHP error when you enable this module, it probably means you have a syntax error in your `.module` file. Be sure all your punctuation is correct, semi-colons, commas, etc. All in the right places, and that you have all the hook names and module short names spelled correctly. (In the case of a white screen, you may be able to find out what the PHP error was by looking in your Apache error log. Or you can try [changing PHP's error reporting level](http://drupal.org/node/1056468).)

If you cannot find and fix the syntax error, nothing on your site will display, because Drupal will try to load your module on every page request. The easiest way to get your site working again is to delete the module's folder or move it out of the site, in which case Drupal will figure out that it shouldn't load this module after all, and your site should work again.

### Clear caches

Drupal caches a lot of data, and if you are not seeing changes appear, that could be why. In this phase of the module, the caches shouldn't be an issue, but they will be as we proceed. To get all the troubleshooting instructions in one place, we'll give you the instructions here that you'll need later.

To clear the caches, go to *Configuration \> Performance* or `http://example.com/admin/config/development/performance`, and click the *Clear all caches* button.
