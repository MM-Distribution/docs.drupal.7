---
title: "How to edit ALT tag on your site logo"
source_url: "https://www.drupal.org/docs/7/theming/howto/how-to-edit-alt-tag-on-your-site-logo"
page_type: page
last_updated: "Last updated on 26 September 2016"
published: "2014-06-06T17:32:56+00:00"
modified: "2016-09-26T08:08:31+00:00"
breadcrumb: ["Drupal 7", "Theming Drupal 7", "Theming HowTos"]
fetched: "2026-10-21T08:50:42Z"
raw: "raw/docs/7/theming/howto/how-to-edit-alt-tag-on-your-site-logo.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# How to edit ALT tag on your site logo

By default, users don't have control over the Alt text that gets used with their site logo. To write a custom Alt text for your logo, you need to do the following:

 

1.  Start with a copy of your theme's page.tpl.php file to edit

2.  Locate the code that is rendering your logo. It will look something like the following:  

    ``` php
    <?php if ($logo): ?> <a href="<?php print $front_page; ?>" title="<?php print t('Home'); ?>" rel="home" id="logo"> <img src="<?php print $logo; ?>" alt="<?php print t('Home'); ?>" /> </a> <?php endif; ?>
    ```

3.  Locate the img tag, followed by the print \$logo text. Here's your logo image. Following that is the alt tag, which currently has the value of "Home".`<img src="<?php print $logo; ?>" alt="<?php print t('Home'); ?>" />`

4.  You can remove the current snippet and add you own ALT tag, such as: `<img src="<?php print $logo; ?>" alt="My Site Logo" />`

5.  You can also keep the existing snippet and add your own text afterwards, such as: `<img src="<?php print $logo; ?>" alt="<?php print t('Home'); ?> and my custom alt text" />`
