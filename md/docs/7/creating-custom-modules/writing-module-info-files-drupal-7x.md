---
title: "Writing module .info files (Drupal 7.x)"
source_url: "https://www.drupal.org/docs/7/creating-custom-modules/writing-module-info-files-drupal-7x"
page_type: page
last_updated: "Last updated on 22 April 2020"
published: "2009-08-06T22:02:43+00:00"
modified: "2020-04-22T17:57:56+00:00"
breadcrumb: ["Drupal 7", "Creating custom modules in Drupal 7"]
fetched: "2026-10-21T07:21:25Z"
raw: "raw/docs/7/creating-custom-modules/writing-module-info-files-drupal-7x.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Writing module .info files (Drupal 7.x)

## Overview

Drupal uses .info files to store metadata about themes and modules.

For modules, the .info file is used for:

- rendering information on the Drupal Web GUI administration pages;
- providing criteria to control module activation and deactivation;
- notifying Drupal about the existence of a module;
- specifying the module's dependencies on other Drupal projects
- general administrative purposes in other contexts.

This .info file is required for the system to recognize the presence of a module.

## Example

The following is a sample .info file:

``` php
name = Really Neat Widget
description = Provides a really neat widget for your site's sidebar.
core = 7.x
package = Views
dependencies[] = views:views
dependencies[] = panels:panels
files[] = tests/example.test
configure = admin/config/content/example
```

The .info file should have the same name as the .module file and reside in the same directory. For example, if your module is named **example.module** then your .info file should be named **example.info**.

This file is in standard .ini file format, which defines properties in key/value pairs separated by an equals sign (key = value). You may use quotation marks to wrap the value. Quoted values may contain newlines.

.info files may contain comments. A semi-colon \[**;**\] placed at the beginning of a line makes that line a comment, and that line will not be parsed.

**Note: Whenever you create or change your .info file, you will need to clear your site's cache for your changes to take effect.**

## Properties

The .info file can contain the following properties:

### Contents

- [name](#name) *required*
- [description](#description) *recommended*
- [core](#core) *required*
- [stylesheets](#stylesheets)
- [scripts](#scripts)
- [files](#files)
- [dependencies](#dependencies)
- [package](#package)
- [php](#php)
- [version](#version) *discouraged*
- [configure](#configure)
- [required](#required)
- [hidden](#hidden)
- [project](#project) *Discouraged, packaging use only*
- [project status url](#project%20status%20url) *Only used for custom modules not submitted to drupal.org*

name *(Required)*  
This displays the name of your module, which will appear on the Modules page. Since module names are proper names, it should be capitalized as a proper name (e.g., "Really Neat Widget", not "really neat widget" or "Really neat widget"), and it should be a human-readable name (not really_neat_widget). If your module name includes an acronym (CSS, WYSIWYG, UI, etc.) or a third-party trade name (jQuery, JavaScript), of course follow the standard capitalization for those.

``` php
name = Really Neat Widget
```

description *(Recommended)*  
A short, preferably one-line description that will tell the administrator what this module does on the module administration page. Remember, overly long descriptions can make this page difficult to work with, so please try to be concise. This field is limited to 255 characters.

``` php
description = Provides a really neat widget for your site's sidebar.
```

Descriptions can contain links to documentation and sources. The following example shows a link to the author. It could be a link to a documentation node on Drupal.org. This is useful when the online documentation is better than the readme file and when you want to read about a module before switching it on.  
`description = Domain manager by <a href="http://petermoulding.com">Peter Moulding .com</a>.`

core *(Required)*  
The version of Drupal that your module is for. For Drupal 7 this would be 7.x, etc. Note that modules cannot specify the minor version of a branch of Drupal. 6.x is correct; 6.2 is not.

``` php
core = 7.x
```

stylesheets *(Optional)*  
Drupal 7 allows you to add CSS files in the module's .info file if it should be added on every page, just like theme .info files do. Here is an example from the node module's .info file:

``` php
stylesheets[all][] = node.css
```

scripts *(Optional)*  
You can add Javascript in the module's .info file if it should be added on every page. This allows Javascript to be aggregated in an optimal way, and is the preferred method of adding Javascript that most visitors will need on a typical site visit:

``` php
scripts[] = somescript.js
```

For more information see [Managing JavaScript in Drupal 7](/node/756722).

files *(Optional)*  
Drupal supports a dynamic-loading code registry. To support it, all modules must declare any code files containing class or interface declarations in the .info file, like so:

``` php
name = Really Neat Widget
...
files[] = tests/example.test
```

When a module is enabled, Drupal will rescan all declared files and index all the classes and interfaces that it finds. Classes will be loaded automatically by PHP when they are first accessed.

Currently this mechanism does not natively support [namespaced](http://php.net/manual/en/language.namespaces.rationale.php) classes.

dependencies *(Optional)*  
An array of other modules that your module requires. If these modules are not present, your module cannot be enabled. If these modules are present but not enabled, the administrator will be prompted with a list of additional modules to enable and may choose to enable the required modules as well, or cancel at that point.

As of Drupal 7.40, dependencies on modules that are hosted on drupal.org should be namespaced to the project they are part of, in the format:

`dependencies[] = {project}:{module}`

The string value of each dependency must be the project's name as it appears in the url on Drupal.org (i.e: drupal.org/project/views) then the `:` character then the module name as it appears in the .module file of the release. The string should be lower case and spaces are not allowed.

Because this namespacing pattern is only available in Drupal 7.40 and above, you should include a dependency on Drupal 7.40, as in the following code.

``` php
dependencies[] = drupal:taxonomy
dependencies[] = drupal:comment
dependencies[] = ubercart:uc_product
dependencies[] = drupal:system (>= 7.40)
```

In addition, test_dependencies\[\] can be used to indicate dependencies which are optional but recommended. At this writing they are supported only by Drupal.org's automated testing system. They cause the testbots to check out the projects suggested. Generally any modules that you have listed in the 'dependencies' array in the getInfo() function of your module's tests should be added as test_dependencies\[\].

Test dependencies should be defined with the same namespace rules as regular dependencies.

``` php
test_dependencies[] = autoload:autoload
```

### Project dependencies

*Project dependencies require Drupal 7.40 or higher. Modules using project dependencies will not be able to install in previous versions. See the original issue at [\#2205271](/node/2205271).*

Sometimes the name of a module and it's parent project are not the same thing. For example the "date_api" module is part of the [Date](https://www.drupal.org/project/date) project. So a module might depend upon "date_api", but not "date" with a dependencies line like this:

``` php
dependencies[] = date_api
```

This would work as long as the Date project has already been downloaded onto the given site. But when needing to reference sub-modules under a parent project it is better to specify the parent project as well. So a more descriptive version is:

``` php
dependencies[] = date:date_api
```

Indicating that the `date_api` sub-module within the `date` project is needed. This allows external tools such as [Drush](/project/drush) to install dependencies by downloading the parent project and enabling only the needed sub-module.

### Version dependencies

If you need to specify that a certain module's version number is required Drupal 7 provides a way for this in the dependencies\[\] field. Version numbers are *optional* and only necessary if the module absolutely requires another module's specific version or branch.

The syntax for version-specific dependencies is:

``` php
dependencies[] = module_name (major.minor)
```

Where *major* is the numeric major version number and *minor* is the numeric or alphanumeric minor version number. *x* can be used to denote any minor version. Some examples follow.

``` php
name = Really Neat Widget
description = An example module
dependencies[] = exampleapi (1.x)

test_dependencies[] = autoload (>7.x-1.5)
...
```

In the above .info code, the "Example" module requires an "Example API" module with the major version of 1 and any minor version.

``` php
dependencies[] = exampleapi (1.0)
```

This means that the module requires the 1.0 (and only the 1.0) version of the Example API module.

``` php
dependencies[] = exampleapi (1.x)
```

The above module requires any minor version of the module in the 1.x branch (1.0, 1.1, 1.2-beta4, etc.)

The dependencies\[\] property in the .info file can also optionally specify version ranges or exact versions:

- = or == equals (optional: equals is the default)
- \> greater than
- \< lesser than
- \>= greater than or equal to
- \<= lesser than or equal to
- != not equal to

> **Note:** When using composer, '\>' and '\>=' are translated to '^' meaning any version above until the next major version. See issue [3123327](https://www.drupal.org/project/project_composer/issues/3123327) for the reasoning.

``` php
dependencies[] = exampleapi (>1.0)
```

The above module requires any version greater than version 1.0.

You can optionally specify the core version number as well:

``` php
dependencies[] = exampleapi (>7.x-1.5)
```

The above module requires a 7.x version compatible version of the module and a version greater than 1.5.

Additionally, multiple version dependencies can be specified as comma-separated values within the parentheses:

``` php
dependencies[] = exampleapi (>1.0, <=3.2, !=3.0)
```

This facility can be used to specify a minimal core version by using `system` as the module name:

``` php
dependencies[] = system (>=7.53)
```

This makes the module require at least Drupal 7.53.

package *(Optional)*  
If your module comes with other modules or is meant to be used exclusively with other modules, enter the name of the package here. If left blank, the module will be listed as 'Other'. In general, this property should only be used by large multi-module packages, or by modules meant to extend these packages, such as Fields, Views, Commerce, Organic Groups, and the like. All other modules should leave this blank. As a guideline, four or more modules that depend on each other (or all on a single module) make a good candidate for a package. Fewer probably do not. An exception to this rule is the "Development" package, which should be used for any modules which are code development tool modules.

If present, the package string groups modules together on the module administration page (admin/modules); the string should therefore be the heading you would like your modules to appear under, and it needs to be consistent (in spelling and capitalization) in all .info files in which it appears. It should not use punctuation and it should follow the Drupal capitalization standard as noted above.

Capitalization is important because package string is case sensitive, and using `package = fields` in one module and `package = Fields` in another would yield two different packages on the module administration page. This can be highly confusing as Seven (the default administrative theme) capitalizes fieldset legends, making `fields` and `Fields` indistinguishable. Using `package = Fields` is the correct way.

``` php
package = Views
```

Suggested examples of appropriate items for the package field:

- Administration
- Commerce
- Development
- Fields
- Media
- User interface
- Views
- Voting (if it uses/requires VotingAPI)

The [Package names for contributed modules wiki](http://groups.drupal.org/node/97054) tries to track current package names; this does not mean they are recommended.

php *(Optional)*  
As of version 6.x, module and themes may specify a minimum PHP version that they require. They may do so by adding a line similar to the following to their .info file:

``` php
php = 5.3
```

That specifies that the module/theme will not work with a version of PHP earlier than 5.3. That is useful if the module makes use of features added in later versions of PHP (improved XML handling, object iterators, JSON, etc.). If no version is specified, it is assumed to be the same as the required PHP version for Drupal core. Modules should generally not specify a required version unless they specifically need a higher later version of PHP than is required by core. See the PHP Manual for further details on PHP version strings.

version *(Discouraged)*  
The version string will be added by drupal.org when a release is created and a tarball packaged. However, if your module is not being hosted on the drupal.org infrastructure, you can give your module whatever version string makes sense (eg. see [Release naming conventions](https://drupal.org/node/1015226)).

Users getting their modules directly from git will not have a version string, since the .info files checked into git do not define a version. These users are encouraged to use the [git deploy](/project/git_deploy) module to provide accurate version strings for the admin/build/modules page for modules in directories checked out directly from git.

Because Drupal core uses a slightly different packaging process than contributed modules, the core modules have a version line predefined. This is an exception to the rule, not the model for contributed modules.

configure *(Optional)*  
As of version 7.x, the path of the module's (main) configuration page.  
If a module is enabled, a "Configure" and "Permissions" link appear. This will be the path of the "Configure" link for this particular module on the modules overview page.

``` php
configure = admin/config/content/example
```

required *(Optional)*  
As of version 7.x, modules and themes may specify that they are absolutely required and should never be disabled by adding `required = TRUE`. These modules will be enabled automatically during install. In most cases it should only be used with the Drupal core required modules (e.g. Node, User, etc.).

hidden *(Optional)*  
As of version 7.x, modules and themes may specify that they should not be visible on the modules page by adding `hidden = TRUE`. This is commonly used with testing modules used with SimpleTest where end-users should never enable the testing modules.

project *(Discouraged, packaging use only)*  
Module maintainers should not use this at all. The packaging script on drupal.org will automatically place a string here to identify what project the module came from. This is primarily for the [Update status](/project/update_status) module, so that Drupal installations can monitor versions of installed packages and notify administrators when new versions are available.

project status url *(Only used for custom modules not submitted to drupal.org)*  
Allows module maintainers to define a URL to check for updates to their module using the [Update status](/project/update_status) module. No module released on drupal.org should define this parameter. URL should point to an XML feed that accepts requests in the form of `http://my.domain.com/projects/{project}/{core}`. In that example, `project status url` should be set to `http://my.domain.com/projects`.

For more information on info file formatting, see the [drupal_parse_info_file() documentation](http://api.drupal.org/api/function/drupal_parse_info_file/7).

## Troubleshooting

**I added the core = 7.x line, but my module still says "This version is incompatible with the 7.x version of Drupal core" on the modules page. What gives?**

Be aware that the "dependencies" format changed between Drupal 5.x and 6.x.

Wrong:

``` php
name = Really Neat Widget
...
dependencies = foo bar   ; 5.x dependency format.
core = 6.x
```

Correct:

``` php
name = Really Neat Widget
...
; Note the [], and that each of the dependencies is on its own line:
dependencies[] = foo
dependencies[] = bar
core = 7.x
```

### Description and Non-ASCII Characters

Note that if you want to use accented characters or other non-ASCII characters in your .info file's description field, you should include the HTML escaped notation, e.g., `&ouml;` for the "ö" character or `&copy;` for the "©" character.

## See also

- [Let Drupal 8 know about your module with an .info.yml file](https://www.drupal.org/node/2000204)
- [Drupal 6 themes .info files](http://drupal.org/node/171205 "Drupal 6 themes .info files")
- [Drupal 6 modules .info files](http://drupal.org/node/231036 "Drupal 6 modules .info files")
