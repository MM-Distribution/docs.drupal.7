---
title: "Add Google Webmasters Tools verification meta tag via the themes template.php file."
source_url: "https://www.drupal.org/docs/7/howtos/add-google-webmasters-tools-verification-meta-tag-via-the-themes-templatephp-file"
page_type: page
last_updated: "Last updated on 25 January 2018"
published: "2012-01-20T12:53:02+00:00"
modified: "2018-01-25T23:27:16+00:00"
breadcrumb: ["Drupal 7", "Site building and development HowTos for Drupal 7"]
fetched: "2026-10-21T07:59:13Z"
raw: "raw/docs/7/howtos/add-google-webmasters-tools-verification-meta-tag-via-the-themes-templatephp-file.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Add Google Webmasters Tools verification meta tag via the themes template.php file.

This guide refers to the **meta tag verification method** available for [Google Webmaster Tools](https://www.google.com/webmasters/tools/ "Google Webmaster Tools") and these instructions are specific to **Drupal 7**.

You can also add any other meta tag you require using this guide.

**edit:** Since writing this guide a module has popped up that does all this for you. **You can find the [Site verify module here](http://drupal.org/project/site_verify).** However, if you require a more complex approach - see the first comment for an example - or just want to learn a bit more about how it works or simply prefer the DIY approach then please do read on:

What you require:

- Google Webmasters Tools Account - sign up here: <https://www.google.com/webmasters/tools/>
- Custom theme (or a copy of a supplied theme) in either /sites/default/themes/ or /sites/all/themes/
- Google Webmaster Tools Verification Code (meta tag)

**1) Make sure you have your Google Webmaster Tools Verification Code meta tag**. It looks something like this:  
`<meta name="google-site-verification" content="abcdefghijklmnopqrstuvwxyz0123456789" />`

**2) Browse to your themes directory.** If you plan to modify your theme, it is best practice to either create a new custom theme or copy an existing theme (or create a sub-theme) in your sites/default/themes/ folder. If you don't know what I mean, you ought to read up on custom themes for Drupal 7 before continuing with this guide.

**3) In your themes directory, open the template.php file in an editor.** If you don't have such a file, create a blank page and call it template.php.

**4) To add the meta tag we will need to use [template_preprocess_html](http://api.drupal.org/api/drupal/includes--theme.inc/function/template_preprocess_html/7 "template_preprocess_html").**

*Initially, I thought it would be possible by using the [hook_html_head_alter](http://api.drupal.org/api/drupal/modules--system--system.api.php/function/hook_html_head_alter/7 "hook_html_head_alter") but this will only allow **already defined \$head_elements** to be modified or unset, so we need to **first create the element and then add it** using [drupal_add_html_head](http://api.drupal.org/api/drupal/includes--common.inc/function/drupal_add_html_head/7 "drupal_add_html_head")*.

Check your template.php file to see if you already have a YOUR_THEME_NAME_preprocess_html function defined. If yes, you will need to paste the code inside the function into it.  
Make sure your template.php file begins with a `<?php` tag if you have created a new blank file.

**5) Paste the function into the template.php file.** Copy the code below and paste it into your template.php file:

``` php
/**
* Preprocesses the wrapping HTML.
*
* @param array &$variables
*   Template variables.
*/
function YOUR_THEME_NAME_preprocess_html(&$vars) {
  
  // Setup Google Webmasters Verification Meta Tag.
  $google_webmasters_verification = array(
    '#type' => 'html_tag',
    '#tag' => 'meta',
    '#attributes' => array(
      'name' => 'google-site-verification',
      // REPLACE THIS CODE WITH THE ONE GOOGLE SUPPLIED YOU WITH
      'content' => 'abcdefghijklmnopqrstuvwxyz0123456789',
    ),
  );
  
  // Add Google Webmasters Verification Meta Tag to head.
  drupal_add_html_head($google_webmasters_verification, 'google_webmasters_verification');
}
```

**6) CHANGE THE FUNCTION NAME 'YOUR_THEME_NAME' TO YOUR THEME NAME eg: garland_preprocess_html**

**7) EDIT THE CODE**

Check this line of the code and replace the code with the one google supplied you with when you added your site to the Google Webmasters Tools.

``` php
      // REPLACE THIS CODE WITH THE ONE GOOGLE SUPPLIED YOU WITH
      'content' => 'abcdefghijklmnopqrstuvwxyz0123456789',
```

**8) Save your file and clear all caches.**

**9) Reload your site and check your source code to check if your meta tag has been added to the header.**

**10) Done!**

I hope this has helped someone with the same problem as me.
