---
title: "Creating a sub-theme"
source_url: "https://www.drupal.org/docs/7/theming/creating-a-sub-theme"
page_type: page
last_updated: "Last updated on 26 March 2021"
published: "2008-02-22T00:02:09+00:00"
modified: "2021-03-26T18:14:16+00:00"
breadcrumb: ["Drupal 7", "Theming Drupal 7"]
fetched: "2026-10-21T06:02:59Z"
raw: "raw/docs/7/theming/creating-a-sub-theme.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Creating a sub-theme

Sub-themes are just like any other theme, with one difference: They inherit the parent theme's resources. There are no limits on the chaining capabilities connecting sub-themes for their parents. A sub-theme can be a child of another sub-theme, and it can be branched and organized however you see fit. This is what gives sub-themes great potential.

![sub-themes and dependencies](/files/sub-theme_branching.png)

Imagine starting with a base theme designed as wireframes, then applying and refining all the details from a sub-theme. Then, from the same wireframe, testing out alternate designs by branching out another sub-theme. Working on a multi-site installation, but you need a cohesive look and feel? With sub-theming, a lot of the design resources can be shared. Site-specific changes can be set to a specific sub-theme, but any shared resources can be edited once to be applied across all the installations. With careful planning, the possibilities are endless.

### Creating a sub-theme

A sub-theme must have a different internal name (i.e., the name used by Drupal) from its parent theme. This name must not contain any spaces or other special characters. **The name of your sub-theme must start with an alphabetic character and can only contain lowercase letters, numbers and underscores**. Let's suppose this sub-theme internal name is "my_subtheme".

#### Folder *my_subtheme*

The sub-theme to-be should be located in its own directory. This folder should have the same name as the internal name of the sub-theme (e.g., *my_subtheme*).

The sub-theme folder should be located inside the folder sites/*example.com*/themes/ ("*example.com*" stands for your site name) or, if you want to use your sub-theme for several sites, inside sites/all/themes/ (e.g., sites/*example.com*/themes/*my_subtheme* or sites/all/themes/*my_subtheme*).

#### File *my_subtheme*.info

To declare your theme to be a sub-theme of another, you must put a *my_subtheme*.info file inside your my_subtheme folder (remember that "*my_subtheme*" stands for your sub-theme internal name). The easiest way is usually to copy the *theme_name*.info file from the parent theme ("*theme_name*" stands for the internal name of the parent theme), and to rename it as *my_subtheme*.info. Then you need to add the following line to *my_subtheme*.info file to declare its parent or "base theme.": change "`theme_name`" to the internal name of the parent theme (that is, the name of the parent theme's .info file, usually all lower case).

`base theme = theme_name`

It is also a good idea to modify the human-readable name of your sub-theme by altering the line beginning by `name =`` `, and the description of your sub-theme by altering the line beginning by `description =`` `. For instance:

``` php
name = My Subtheme
description = This is a sub-theme of theme Bartik, made by John for the web site example.com (red, responsive).
core = 7.x
base theme = bartik
```

As the sections below indicate, the sub-theme inherits *most* properties of the base theme. The important exceptions are regions, core version, and color info. You probably want to copy the regions section of your base theme's info file, along with its core version declaration. If your base theme supports the color module and you'd like your sub-theme to support it, you probably also want to copy the color folder from your base theme and add the line from your base theme's info file to your sub-themes info file that looks like

`stylesheets[all][] = css/colors.css`

and then copy the `colors.css` from your base theme to the css folder of your sub-theme.

### Style sheet inheritance

All [style sheets](/node/171209) defined in the parent theme will be inherited.

**Overriding inherited style sheets:** Specify a style sheet with the same filename in the sub-theme. For instance, to override style.css inherited from a parent theme, add the following line to your sub-theme's .info file:

`stylesheets[all][] = style.css`

You will also need to create the style.css stylesheet file; if you simply wish to disable the imported styles, you can create an empty file.

### JavaScript inheritance

All [JavaScript](/node/171213) files defined in the parent theme will be inherited.

**Overriding inherited JavaScript:** Specify a JavaScript file with the same filename in the sub-theme's .info file. For instance, to override script.js inherited from a parent theme, add the following line to your sub-theme's .info file:

`scripts[] = script.js`

You will also need to create the script.js file; if you simply wish to disable the imported scripts, you can create an empty file.

### To set Toggle Display of Theme

**Overriding or adding features:** Specify a new feature in sub-theme's .info file. Add the following lines to your sub-theme's .info file:

``` php
features[] = logo
features[] = name
features[] = slogan
features[] = node_user_picture
features[] = comment_user_picture
features[] = comment_user_verification
features[] = favicon
features[] = main_menu
features[] = secondary_menu 
```

For more detail click here: [Theme settings](/node/221905)

### Template.php function inheritance

Anything defined in the parent theme's template.php file will be inherited. This includes [theme function overrides](/node/173880#function-override), [preprocess functions](/node/223430) and anything else in that file. Each sub-theme should also have its own template.php file, where you can add additional functions or override functions from the parent theme.

There are two main types of functions in template.php: [theme function overrides](/node/173880#function-override) and [preprocess functions](/node/223430). The template system handles these two types in very different ways.

Theme functions are called through theme('\[hook\]', \$var, ...). When a sub-theme overrides a theme function, no other version of that theme function is called.

On the other hand, preprocess functions are called before processing a .tpl file. For instance, \[theme\]\_preprocess_page is called before page.tpl.php is rendered. Unlike theme functions, *preprocess functions are not overridden in a sub-theme*. Instead, the parent theme preprocess function will be called first, and the sub-theme preprocess function will be called next.

There is no way to prevent all functions in the parent theme from being inherited. As stated above, it is possible to override parent theme functions. However, the only way to remove a parent theme's preprocess function is through hook_theme_registry_alter().

### Page, node, block and other template (.tpl.php) file inheritance

Drupal provides a large set of files that themes can use to inherit properties. By specifying a particular file name and or structure, this allows the theme to override or inherit a template. For more information on this review [working with template suggestions](http://drupal.org/node/223440)

**Drupal 7:** Any .tpl.php files from the parent theme will be inherited. You can add template files with more specificity — for instance, node--blog.tpl.php building on an inherited node.tpl.php.

A single hyphen is still used to separate words: for example, "user-picture.tpl.php" or "node--long-content-type-name.tpl.php", so the double hyphen always indicates a more targeted override of what comes before the "--". See Converting 6.x themes to 7.x for more info.

**Overriding inherited .tpl.php templates:** Add a template file with the same name in your sub-theme folder to have it override the template from the parent theme.

### Screen shots, logo and favicon inheritance

The parent theme's screen shot will be inherited. The parent theme's logo (logo.png/logo.jpg) will **not** be inherited. The parent theme's favicon (favicon.ico) will **not** be inherited.

**Overriding inherited screen shots:** Specify a new image file in your sub-theme's .info file.

### Region inheritance

Sub-themes do not inherit custom regions from a parent theme. If you are using custom regions, you should copy the region declarations from the parent theme's .info file. Be sure your sub-theme's page.tpl.php file matches the sub-theme's region settings.

### Features inheritance

In Drupal 7, features are not inherited from the base theme. If you are using features other than the default, you should copy the features declarations from the parent theme's .info file.

### Color inheritance

[Color.module support](/node/108459) within the color directory is **not** inherited.

### Theme settings inheritance

Theme settings set via [advanced theme settings](/node/177868)' theme-settings.php is **not** inherited, unless you copy the settings declarations from the parent theme's .info file.
