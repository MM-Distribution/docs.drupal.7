---
title: "Configurations that work with the Mobile Codes module."
source_url: "https://www.drupal.org/docs/7/mobile/configurations-that-work-with-the-mobile-codes-module"
page_type: page
last_updated: "Last updated on 24 August 2016"
published: "2013-01-21T08:07:10+00:00"
modified: "2016-08-24T09:04:56+00:00"
breadcrumb: ["Drupal 7", "Mobile guide for Drupal 7"]
fetched: "2026-10-21T07:18:34Z"
raw: "raw/docs/7/mobile/configurations-that-work-with-the-mobile-codes-module.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Configurations that work with the Mobile Codes module.

I thought it would be useful to create a list of configuration steps that work with this module:

### Adding a Field to a Node for auto generation Node URL to QR Code

Required Modules: Mobile Codes \| Token Filter

**A) Mobile Codes Text Format**

1.  In the Admin Menu - Navigate to Configuration/Content Authoring/Text Formats
2.  Create a text format possibly called Mobile Codes Formatting
3.  Enable the Mobile Codes filter + Replace Tokens filter
4.  Ensure Filter processing order is a) Replace Tokens b) Mobile Codes

**B) Create Field on Node where Mobile Code is to appear**

1.  Create a text field possibly called Mobile Code.
2.  Insert as Default Value for text field \[mobilecode \#preset="small"\]\[node:url\]\[/mobilecode\].
3.  Set Text Format on field as Filtered text (user selects text format) and choose text format Mobile Codes Formatting as default.

There is no need to change anything on the Manage Display of the field other than where you want the field to show up on the page and adding your own CSS class if needed.

The Token Filter module adds a text filter to convert the \[node:url\] token to the URL of the node.

The Mobile Codes module adds a text filter to convert \[mobilecode \#preset="small"\]\[/mobilecode\] to the QR Code format.

\#preset="small" is the pre-configured size of the Mobile Code output to the screen - See the configuration of the Mobile Codes module to change the settings for this.

**Pre-Configuration of the Modules:**

Token Filter - No configuration needed adds a token conversion filter to text fields. Thats it!

Mobile Codes - You need to configure the settings of this module under Configuration/Content Authoring/ Mobile Codes.

Please feel free to add your own settings that worked for you to this posting.
