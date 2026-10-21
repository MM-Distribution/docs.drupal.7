---
title: "Theme coding conventions"
source_url: "https://www.drupal.org/docs/7/theming/tools-and-best-practices/theme-coding-conventions"
page_type: page
last_updated: "Last updated on 30 October 2017"
published: "2003-06-14T14:40:58+00:00"
modified: "2017-10-30T13:19:32+00:00"
breadcrumb: ["Drupal 7", "Theming Drupal 7", "Tools and best practices"]
fetched: "2026-10-21T08:53:02Z"
raw: "raw/docs/7/theming/tools-and-best-practices/theme-coding-conventions.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Theme coding conventions

## Coding standards

These coding standards are used for the development of Drupal core themes and modules.

- [CSS Coding standards](/node/1886770).
- [JavaScript Coding standards](/node/172169).
- [Twig Coding standards](/node/1823416).

## Code conventions

Theme authors should take care to write clean, well structured code just like a developer for any other project. Doing so makes the code easier to read, understand and maintain. While different organizations have different conventions, it's usually best to follow the Drupal standards as this helps when collaborating or asking for help.

- Add 2 spaces for indents; rather than a tabbed indent (This maintains consistency and is consistent with Drupal's coding standards)

- Match the indentation of *long* opening and closing block HTML tags

- Avoid curly brackets. Use [php´s alternative syntax for control structures](http://php.net/manual/en/control-structures.alternative-syntax.php):

  Not this:

  ``` php
    ...
  <?php if ($footer) { ?>
    <?php print $footer; ?>
  <?php } else { ?>
    <?php print $header; ?>
  <?php } ?>
    ...
     
  ```

  but this:

  ``` php
    ...
  <?php if ($footer): ?>
    <?php print $footer; ?>
  <?php else: ?>
    <?php print $header; ?>
  <?php endif; ?>
    ...
     
  ```

- Distinguish between PHP and HTML indentation.

  Not this:

  ``` php
    ...
  <?php if ($header): ?>
  <div id="header">
    <?php print $header; ?>
  </div>
  <?php endif; ?>
     ...
      
  ```

  but this:

  ``` php
    ...
  <?php if ($header): ?>
    <div id="header">
      <?php print $header; ?>
    </div>
  <?php endif; ?>
    ...
      
  ```

  This makes it much easier to find matching opening and closing tags defined with different indentation.

- Prefer PHP in HTML to HTML in PHP in templates. For example,

  not this:

  ``` php
  if (!$page) {
    print "<h2><a href='$node_url'>$title</a></h2>";
  }

  if ($submitted) {
    print "<span class='submitted'>$submitted</span>";
  }
      
  ```

  but this:

  ``` php
  <?php if (!$page): ?>
    <h2><a href="<?php print $node_url; ?>"><?php print $title; ?></a></h2>
  <?php endif; ?>

  <?php if ($submitted): ?>
    <span class="submitted"><?php print $submitted; ?></span>
  <?php endif; ?>
      
  ```

  After all, PHP is a HTML-embedded scripting language, and not the other way around.

- Separate logic from presentation.

  You sometimes see:

  ``` php
  Price: <?php print $price; ?>
  Tax: <?php print $price * 0.075; ?>
  ```

  Move the calculation up the code before you start the presentation of the data. The business logic part of the script would contain:  
  `<?php $tax = $price * 0.075; ?>`

  and the presentation part:

  ``` php
  Price: <?php print $price; ?>
  Tax: <?php print $tax; ?>
  ```

- Avoid Drupal functions in templates.

  Not this:

  ``` php
  ...
  <h2><?php print variable_get('our_title', 'Default title'); ?></h2>
  ...
  ```

  This should preferably be performed in a template.php file (or a preprocess hook) and exposed as a variable to the .tpl.php file.

  In the template.php (or preprocess hook):

  ``` php
  $variables['title'] = variable_get('our_title', 'Default title');
  ```

  In the .tpl.php file:

  ``` php
  ...
  <?php if (!empty($title)): ?>
    <h2><?php print $title; ?></h2>
  <?php endif; ?>
  ...
  ```

- Always put a semicolon at the end of your small PHP printing statements:  

  ``` php
        <?php print $tax; ?> -- YES
        <?php print $tax ?> -- NO
      
  ```

- In more extended sections of PHP code, follow the [Drupal coding standards](http://drupal.org/coding-standards).
