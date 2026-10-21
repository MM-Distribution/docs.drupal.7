---
title: "Telling Drupal about your module"
source_url: "https://www.drupal.org/docs/7/creating-custom-modules/telling-drupal-about-your-module"
page_type: page
last_updated: "Last updated on 19 February 2019"
published: "2011-02-27T19:49:05+00:00"
modified: "2019-02-19T19:07:17+00:00"
breadcrumb: ["Drupal 7", "Creating custom modules in Drupal 7"]
fetched: "2026-10-21T07:21:10Z"
raw: "raw/docs/7/creating-custom-modules/telling-drupal-about-your-module.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Telling Drupal about your module

**Main topic described: *.info files***

All modules must have a “*modulename*.info” file, which contains meta information about the module.

The general format is:

``` php
name = Module Name 
description = A description of what your module does. 
core = 7.x 
```

For our module, we will replace “Module Name” in the example above with the name of our module, “Current Posts”. Without this file, the module **will not show up in the module listing**. Here is our specific example:

``` php
name = Current Posts 
description = A block module that lists links to recent posts. 
core = 7.x 
package = My Modules 
```

Add the source above to a file named `current_posts.info` and save it into the module’s directory at `sites/all/modules/current_posts`.

Note: If you copy and paste this code block, ensure that the description data does not contain a line break (turn off word-wrap on your text-editor to be sure). Otherwise, the .info file will not parse correctly.

### .Info File Details

The details of what to put in a .info file can be found on the [Writing .info files](http://drupal.org/node/542202) page.

### Check

Your module should now appear in the module list in your site. Go to *Modules* and scroll down to the bottom of the list in the “My Modules” category. You should see the module “Current Posts” or otherwise the name of the module you chose.

(Make sure you created a “*modulename*.module” file as described in the tutorial’s previous step.)

### See also

- [Ini file formatting: PHP.net parse_ini_file documentation](http://php.net/parse_ini_file).
- [Writing .info files (Drupal 7.x)](http://drupal.org/node/542202).
