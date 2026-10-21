---
title: "Writing theme .info files"
source_url: "https://www.drupal.org/docs/7/theming/writing-theme-info-files"
page_type: page
last_updated: "Last updated on 2 July 2019"
published: "2007-08-28T16:09:46+00:00"
modified: "2019-07-02T10:45:15+00:00"
breadcrumb: ["Drupal 7", "Theming Drupal 7"]
fetched: "2026-10-21T06:01:11Z"
raw: "raw/docs/7/theming/writing-theme-info-files.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Writing theme .info files

The .info file is a static text file for defining and configuring a theme. Each line in the .info file is a key-value pair with the key on the left and the value on the right, with an "equals sign" between them *(e.g. `name = my_theme`)*. Semicolons are used to comment out a line. Some keys use a special syntax with square brackets for building a list of associated values, referred to as an "array". If you are unfamiliar with arrays, have a look at the default .info files that come with Drupal and read the explanations of the examples that follow. Even though the .info file extension is not natively opened by an Application, you can use TextEdit on a Mac or Notepad on a Windows computer in order to view, edit, and save your changes.

Note that this page describes .info files used for Drupal **themes** and not **modules**. For information about the structure of .info files for Drupal modules, see [Writing .info files](/node/542202) in the [Module developer's guide](/developing/modules).

## Example

The following example shows the Drupal 7 .info file for the Garland theme:

``` php
name = Garland 
description = A multi-column theme which can be configured to modify colors and switch between fixed and fluid width layouts. 
package = Core
version = VERSION
core = 7.x
stylesheets[all][] = style.css
stylesheets[print][] = print.css
settings[garland_width] = fluid
```

## Theme name requirements

The name should start with an alphabetic character, can contain numbers and underscores, but not hyphens, spaces or punctuation. The name will be used by Drupal in forming various [functions in PHP](http://us3.php.net/manual/en/language.functions.php) and therefore it has the same limitations.

Do not choose names that are already used by installed modules, as all installed components must have unique names.

One of the best practices is to use prefixes when naming a site's custom theme, to guarantee unique names for themes. A site named example.com might use theme names such as ***ex_themename***.

Because the .info file is cached, you must [clear the cache](/node/337176) before any changes are displayed in your site.

The .info file can also specify which theme settings should be accessed from the Drupal administration interface, as you will soon see.

## Encoding

The file must be saved as UTF-8 without a Byte Order Mark (BOM).

## Contents

Drupal understands the keys listed below. Drupal will use [default values](/node/171206) for the optional keys not present in the .info file. *See the [examples](#example) set for core themes.*

- [name](#name) *required*
- [description](#description) *recommended*
- [screenshot](#screenshot)
- package
- [version](#version) *discouraged*
- [core](#core) *required*
- [base theme](#base-theme)
- [regions](#regions)
- [features](#features)
- [theme settings](#theme-settings)
- [stylesheets](#stylesheets)
- [scripts](#scripts)
- [php](#php)

name *(required)*  
The human readable name can now be set independently from the internal "machine" readable name. This imposes fewer restrictions on the allowed characters.

``` php
name = A fantasy name 
```

description *(recommended)*  
A short description of the theme. This description is displayed on the theme select page at "Administer \> Site building \> themes".

``` php
description = Tableless multi-column theme designed for blogs. 
```

screenshot  
The optional screenshot key tells Drupal where to find the theme's thumbnail image, used on the theme selection page (admin/build/themes). If this key is omitted from the .info file, Drupal uses the "screenshot.png" file in the theme's directory.

Use this key only if your thumbnail file is not called "screenshot.png" or if you want to place it in a directory outside of your theme's base directory (e.g. `screenshot = images/screenshot.png`).

``` php
screenshot = screenshot.png 
```

*More details on [creating a screenshot for the administration page](/node/11637).*

version *(discouraged)*  
The version string will automatically be added by drupal.org when a release is created and a tarball packaged. So you may omit this value for contributed themes. However, if your theme is not being hosted on the drupal.org infrastructure, you can give your theme whatever version string makes sense.

``` php
version = 1.0 
```

core *(required)*  
From 6.x onward, all .info files for *modules and themes* **must indicate** what major version of Drupal core they are compatible with. The value set here is compared with the [DRUPAL_CORE_COMPATIBILITY](http://api.drupal.org/api/constant/DRUPAL_CORE_COMPATIBILITY/7.x) constant. *If it does not match, the theme will be disabled.*

``` php
core = 7.x 
```

*The [drupal.org packaging script](http://drupalcode.org/project/drupalorg.git/blob/refs/heads/6.x-3.x:/drupalorg_project/plugins/release_packager/DrupalorgProjectPackageRelease.class.php) automatically sets this value based on the Drupal core compatibility setting on each release node. So people downloading packaged themes from drupal.org will always get the right thing. However, for sites that deploy Drupal directly from git, it helps if you commit this change to the .info file for your theme. This is also a good way to indicate to users of each theme what version of core the HEAD of git is compatible with at any given time.*

base theme  
Sub-themes can declare a base theme. This allows for theme inheritance, meaning the resources from the "base theme" will cascade and be reused inside the sub-theme. Sub-themes can declare other sub-themes as their base, allowing multiple levels of inheritance. Use the internal "machine" readable name of the base theme. The following is used in Minnelli, the sub-theme of Garland.

``` php
base theme = garland 
```

*More details are available on the page [Sub-themes, their structure and inheritance](/node/225125).*

regions  
The block regions available to the theme are defined by specifying the key of '`regions`' followed by the internal "machine" readable name *in square brackets* and the human readable name as the value, e.g., `regions[theRegion] = The region name`.

If no regions are defined, the following values are assumed.

    Drupal 7 default regions:

``` php
regions[header] = Header 
regions[highlighted] = Highlighted 
regions[help] = Help 
regions[content] = Content 
regions[sidebar_first] = Left sidebar 
regions[sidebar_second] = Right sidebar 
regions[footer] = Footer 
```

You can override the values for your specific needs.

*If you override regions in Drupal 7, you are obliged to declare the line regions\[content\] = Content. If you want any of the default regions in your theme, you have to declare them as well.  
More details are available on the page [Blocks, content and their regions](/node/171224).*

features  
Various page elements output by the theme can be toggled on and off on the theme's configuration page. The "features" keys control which of these check boxes display on the theme's configuration page. This is useful for suppressing check boxes for elements not defined or used by a theme. To suppress a check box, omit the entry for it. However, if none is defined, all the checkboxes will display due to the assumed defaults.

The example below lists all the available elements controlled by the features key.

Drupal 7 features

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

*More details are available on the page [Custom theme settings](/node/221905)*.

theme settings  
You can use theme settings placed in .info file, to set the features by default "checked" or "unchecked" in your theme. By placing:

`settings[toggle_"feature"] = 0 ` to uncheck the setting

Where "feature" is example logo, favicon etc. that were mentioned earlier.

Example default settings:

Drupal 7

``` php
settings[toggle_logo] = 1 
settings[toggle_name] = 1 
settings[toggle_slogan] = 1 
settings[toggle_node_user_picture] = 1 
settings[toggle_comment_user_picture] = 1 
settings[toggle_comment_user_verification] = 1 
settings[toggle_favicon] = 1 
settings[toggle_main_menu] = 1 
settings[toggle_secondary_menu] = 1 
```

*More details about [Advanced theme settings.](/node/177868)*

stylesheets  
Traditionally, themes default to using style.css automatically and could add additional stylesheets by calling [drupal_add_css()](http://api.drupal.org/api/function/drupal_add_css) in their template.php file. Starting in Drupal 6, themes can also add style sheets through their .info file.

``` php
stylesheets[all][] = theStyle.css 
```

Starting in Drupal 7, themes no longer default to using style.css if it is not specified in the .info file.

*More details are available in the [style sheets](/node/171209) section.*

scripts  
Traditionally, themes could add Javascript by calling [drupal_add_js()](http://api.drupal.org/api/function/drupal_add_js) in their template.php file. Starting in 6.x, if a file named script.js exists in the theme directory then it is automatically included. However, in Drupal 7, this behavior has been changed again so that script.js is only included if it has been specified in the .info file:

``` php
scripts[] = myscript.js 
```

*More details are available in the [JavaScript & jQuery](/node/171213) section.*

php  
This defines the minimum **PHP version** the theme will support. The default value is derived from the [DRUPAL_MINIMUM_PHP](http://api.drupal.org/api/constant/DRUPAL_MINIMUM_PHP) constant, which is the minimum required version for the rest of core. This can be redefined for a newer version if needed. For most themes, this should not be added.

``` php
php = 5.6 
```

**Example .info files from core themes**

Garland:  
![theme administration display](/files/info_display.png)

``` php
name = Garland
description = A multi-column theme which can be configured to modify colors and switch between fixed and fluid width layouts.
package = Core
version = VERSION
core = 7.x
stylesheets[all][] = style.css
stylesheets[print][] = print.css
settings[garland_width] = fluid

; Information added by drupal.org packaging script on 2013-04-03
version = "7.22"
project = "drupal"
datestamp = "1365027012"
```

Minnelli *sub-theme of Garland.*:

``` php
name = Minnelli
description = Tableless, recolorable, multi-column, fixed width theme.
version = VERSION
core = 7.x
base theme = garland
stylesheets[all][] = minnelli.css

; Information added by drupal.org packaging script on 2009-09-02
version = "7.x-dev"
core = "7.x"
project = "drupal"
datestamp = "1251850064"
```

*Note that everything from the line "; Information added by drupal.org packaging script on 2008-02-13" and down is added by the drupal.org packaging script. You should never manually add the project and datestamp keys. The version key added manually (in the first section) allows sites to use your theme when taken directly from git.*
