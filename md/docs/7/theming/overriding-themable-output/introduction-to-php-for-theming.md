---
title: "Introduction to PHP for theming"
source_url: "https://www.drupal.org/docs/7/theming/overriding-themable-output/introduction-to-php-for-theming"
page_type: page
last_updated: "Last updated on 8 October 2016"
published: "2008-12-19T00:55:30+00:00"
modified: "2016-10-08T22:05:02+00:00"
breadcrumb: ["Drupal 7", "Theming Drupal 7", "Overriding themable output"]
fetched: "2026-10-21T08:18:05Z"
raw: "raw/docs/7/theming/overriding-themable-output/introduction-to-php-for-theming.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Introduction to PHP for theming

Teaching PHP is beyond the scope of the Drupal documentation, but this page will introduce you to some of the most basic techniques which are important to working with themes.

## Discovering your data

*Both of the techniques described below use a lot of resources and **can expose internal information to the public**. Therefore, you should never use either technique on a production site.*

### Option 1: Use a PHP Function

You can use a PHP function to see all of the variables that have been passed to your template file. To do so, you can add the following code to the top of any template (.tpl.php) file in your theme.

``` php
<?php
$vars = get_defined_vars();
print_r($vars);
?>
```

### Option 2: Use the Theme Developer module

The [Theme Developer module](http://drupal.org/project/devel_themer) will let you access to a live, interactive display of the variables that were used to create any part of a page, but it also includes numerous functions for outputting debugging data while you are working. *Only -dev releases are available at this time.*

## Using the information you get

Once you have used one of the techniques above, you will be able to see numerous variables and arrays(). If you wish, you can refer directly to any of these in your template.

For example, to display the title, you would add the following code to your .tpl.php file:

`<?php print $title; ?>`

To display the node title along with a link to the node and some heading formatting, add the following code:

``` php
<h2 class="title">
  <a href="<?php print $node_url; ?>" title="<?php print $title; ?>"><?php print $title; ?></a>
</h2>
```

## Arrays

The output from the print_r technique shown above will probably contain a number of arrays. For example, if you are using a taxonomy you might see something like this:

`[taxonomy] => Array`

An array allows a group of related data to be stored in an organized way. If you only want one item from an array to be displayed you can specify that item using its related "key".

For example, suppose the `print_r` technique showed you the following array:

``` php
[location] => Array
        (
            [lid] => 3
            [name] => My Place
            [street] => 235 King Edward Avenue
            [additional] => 
            [city] => Ottawa
            [province] => ON
            [postal_code] => K1N 7L8
            [country] => ca
            [latitude] => 45.431993
            [longitude] => -75.688390
            [source] => 3
            [is_primary] => 0
            [province_name] => Ontario
            [country_name] => Canada
        )
```

If you just wanted to display the city, you could add the following code to your .tpl.php file:

`<?php print $location['city']; ?>`

There are many other ways to manipulate your content using PHP. For more information, consult one of the PHP references on the web.
