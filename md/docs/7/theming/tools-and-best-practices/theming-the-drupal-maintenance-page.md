---
title: "Theming the Drupal maintenance page"
source_url: "https://www.drupal.org/docs/7/theming/tools-and-best-practices/theming-the-drupal-maintenance-page"
page_type: page
last_updated: "Last updated on 20 February 2026"
published: "2007-11-26T16:15:45+00:00"
modified: "2026-02-20T15:53:45+00:00"
breadcrumb: ["Drupal 7", "Theming Drupal 7", "Tools and best practices"]
fetched: "2026-10-21T08:53:17Z"
raw: "raw/docs/7/theming/tools-and-best-practices/theming-the-drupal-maintenance-page.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Theming the Drupal maintenance page

## What is the maintenance page?

The maintenance page is used when the site is set in off-line mode or the site is inoperable due to technical problems, such as a database failure. You can enable this mode from "*Administer \> Site configuration \> Site maintenance*". This mode will also trigger during a database failure. By default, the core theme Minnelli is used in this mode even if another theme is selected. However, you might like to include a maintenance page from within your own site.

## Overriding template files in Drupal

Creating a custom theme in Drupal is a practice of overriding existing template (.tpl.php) files. You can find template files included with the core distribution and you can either copy these files into your theme folder, or create new files with the same name. Drupal will first choose your theme's template files before the core ones. In this way, you can override the default templates. For example, there is a `maintenance-page--offline.tpl.php` file which exists in Drupal core, that you can duplicate into your own theme.

Sometimes you can use template suggestions, which means example files don't exist with Drupal, but if you include a file with the suggested name, Drupal will pick it up. For example `maintenance-page.tpl.php` doesn't exist in core, but you can create a file with that name and Drupal will recognize it.

In this case there are two maintenance page files that you can create. You can duplicate your theme's `page.tpl.php` twice and name them:

1.  `maintenance-page.tpl.php`: This file controls the page that is displayed when the site is in "maintenance mode" but the database connection and database are still functioning correctly.
2.  `maintenance-page--offline.tpl.php`: This file controls the page that is displayed when Drupal cannot access the database (for whatever reason). *\[Note - broken since Drupal 7. Requires a patch since Drupal 8: <https://www.drupal.org/project/drupal/issues/2720109>\]*

### Step 1: Override the maintenance page template

Copy your main `page.tpl.php` and rename it to `maintenance-page.tpl.php` or copy the template located in `modules/system/maintenance-page.tpl.php` to your theme and edit so it matches the rest of your site.

### Step 2: Indicate in your settings.php file

In the case of a database failure, your maintenance page setting must be indicated in configuration files so this can operate without access to the database. Specify your maintenance page in your `settings.php` file, which is usually located at `sites/default` or `sites/yourdomain.com` (if you are on a multi-site installation).

#### Option 1

In the `settings.php` file, enable the `$conf` variable with the internal name of your theme:

``` php
  $conf['maintenance_theme'] = 'themeName';
```

#### Option 2

In the `settings.php` file, numerous configurations are disabled with a \# (*hash*) symbol at the start of the line. You can remove the \# symbol at the start of the line to uncomment and enable that configuration.

Therefore, instead of adding the line as in Option 1 above to the `settings.php` file, you can also uncomment the relevant lines in `settings.php`. In that case, you have to uncomment 3 separate lines:

- The array declaration (`# $conf = array(`)
- The maintenance theme setting (`# 'maintenance_theme' => 'minnelli',`)
- The closing parenthesis (`# );`)

Verify the changes by setting the site into off-line mode then log out.

To account for database failures, try turning off your database. Any function call that depends on the database should be checked first with [db_is_active](http://api.drupal.org/api/function/db_is_active/6). The variable \$db_is_active can also be used from the template.

As an alternative to disabling your database, force a database connection failure. Examples for both methods can be found [here](http://drupal.org/node/195435#comment-1452608 "Examples for disabling the database or simulating database failure.").

### Step 3: Create the maintenance offline page in the case of database failure

To prevent warnings about the database connection from appearing, copy your `page.tpl.php` file and rename it `maintenance-page--offline.tpl.php`. Change the `$content` variable with your custom message. Note, this template file is a [template suggestion](/node/223440) based on `maintenance-page.tpl.php` so they both need to exist in the same folder.

At the top of `maintenance-page--offline.tpl.php`, you might also want to set the following variables detailed in step 4.

### Step 4: Hard code site settings

In this mode, your database is inaccessible, therefore some key settings about your site are not available. If you want this page to use the same theme and other settings that the site would normally use, you must replicate those settings by using hard-coded values.

Copy these variables into the `maintenance-page--offline.tpl.php` file:

- `$head_title` - the value used in the HTML `<title>` tag. Defaults to "Site off-line \| Drupal"
- `$site_name` - the value used in the page's `<h1>` tag. Defaults to "Drupal". If "Site name" is turned off in your theme configuration, then you'll want to clear this variable (see example below).
- `$logo` - if you're using a custom logo override in the theme settings. Use the full path of the custom logo, relative to the base directory of the Drupal installation. If you used the standard override upload function in the theme configuration for your custom logo, your logo will be stored in `sites/all/files/` (see example below).
- `$site_slogan` - your site's slogan. If "Site slogan" is turned off in your theme configuration but you still have a site slogan defined in Site Information, then you'll want to clear this variable (see example below).

Example additions at the top of `maintenance-page--offline.tpl.php`:

``` php
  $head_title = 'mysite.com :: Site-offline';
  $logo = 'sites/all/files/customLogo.png';

  // If your theme is set to display the site name, uncomment this line and replace the value:
  // $site_name = 'Your Site Name';

  // If your theme is set to *not* display the site name, uncomment this line:
  unset($site_name);

  // If your theme is set to display the site slogan, uncomment this line and replace the value:
  $site_slogan = 'My Site Slogan';

  // If your theme is set to *not* display the site slogan, uncomment this line:
  // unset($site_slogan);

  // Main message. Note HTML markup.
  $content = '
```

`The site is currently not available due to technical problems. Please try again later. Thank you for your understanding.`

------------------------------------------------------------------------

`If you are the maintainer of this site, please check your database settings.`

`'; `

A `maintenance.css` file is included in this mode. It is located in `modules/system/maintenance.css`. You can override this file with the instructions provided in the [style sheets section](/node/171209#styles-override-module).

*Notes:*

- *The initial install and updating of your site depends on the core themes, Minnelli and Garland. It cannot be changed for these modes.*
- *The theme registry is not cached when set to off-line mode.*
- *Ensure that the theme used as maintenance theme is enabled (Administer \> Site building \> Themes).*
