---
title: "Primary and Secondary links renamed to Main and Secondary menu"
source_url: "https://www.drupal.org/docs/7/theming/overriding-themable-output/primary-and-secondary-links-renamed-to-main-and-secondary"
page_type: page
last_updated: "Last updated on 31 August 2016"
published: "2010-04-22T18:41:45+00:00"
modified: "2016-08-31T14:15:55+00:00"
breadcrumb: ["Drupal 7", "Theming Drupal 7", "Overriding themable output"]
fetched: "2026-10-21T08:20:55Z"
raw: "raw/docs/7/theming/overriding-themable-output/primary-and-secondary-links-renamed-to-main-and-secondary.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Primary and Secondary links renamed to Main and Secondary menu

Primary and Secondary links have been renamed to Main and Secondary menu. Themes which support these options will need to be updated to use the new variable names:

**6.x: page.tpl.php**

``` php
<div id="menu">
  <?php if (isset($secondary_links)) { ?><?php print theme('links', $secondary_links, array('class' => 'links', 'id' => 'subnavlist')); ?><?php } ?>
  <?php if (isset($primary_links)) { ?><?php print theme('links', $primary_links, array('class' => 'links', 'id' => 'navlist')) ?><?php } ?>
</div>
```

**7.x: page.tpl.php**

``` php
<?php if ($main_menu || $secondary_menu): ?>
  <div id="navigation"><div class="section">
      <?php print theme('links__system_main_menu', array('links' => $main_menu, 'attributes' => array('id' => 'main-menu', 'class' => array('links', 'inline', 'clearfix')), 'heading' => t('Main menu'))); ?>
      <?php print theme('links__system_secondary_menu', array('links' => $secondary_menu, 'attributes' => array('id' => 'secondary-menu', 'class' => array('links', 'inline', 'clearfix')), 'heading' => t('Secondary menu'))); ?>
  </div></div> <!-- /.section, /#navigation -->
<?php endif; ?>
```

You will also need to make the appropriate variable name changes if your theme's theme.info is defining features\[\]. Defining renamed or replaced features may cause all features to render as blank or empty arrays.

**6.x: theme.info - features\[\]**

``` php
features[] = primary_links
features[] = secondary_links
```

**7.x: theme.info - features\[\]**

``` php
features[] = main_menu
features[] = secondary_menu
```

Also, if your theme.info is defining **features\[\] = mission** please note that this feature has been removed and replaced with a variable named \$mission which can be output in your page template.
