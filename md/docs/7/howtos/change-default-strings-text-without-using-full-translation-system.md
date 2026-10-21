---
title: "Change default strings (text) without using full translation system"
source_url: "https://www.drupal.org/docs/7/howtos/change-default-strings-text-without-using-full-translation-system"
page_type: page
last_updated: "Last updated on 18 January 2025"
published: "2009-07-17T05:18:33+00:00"
modified: "2025-01-18T20:46:56+00:00"
breadcrumb: ["Drupal 7", "Site building and development HowTos for Drupal 7"]
fetched: "2026-10-21T08:01:17Z"
raw: "raw/docs/7/howtos/change-default-strings-text-without-using-full-translation-system.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Change default strings (text) without using full translation system

**Note**: Drupal 10/11 page can be found at [https://www.drupal.org/docs/administering-a-drupal-site/configuration-ma...](https://www.drupal.org/docs/administering-a-drupal-site/configuration-management/override-strings-in-the-interface-without-using-full-translation-system)

## Methods

1.  Edit `settings.php` file
2.  String Overrides module
3.  Use `hook_boot()`

## Method 1: Edit settings.php file

### Pros

- A quick method for a small number of strings.
- Less accessible in cases where you want to retain some control even after granting administrator access.

### Cons

- No admin pages require access to files on the server (FTP / SFTP / SSH). Difficult to delegate changes to non-developers.

### Procedure

1.  Edit `settings.php` for the site in question.
    - You'll need to either download the file, edit it, and re-upload it, or edit it in place on the server. Of course, make a backup.
    - Either way, you'll probably need to temporarily change the permissions of the file and its containing folder to give you "write access". Be sure to take note of the permissions and change them back to what they were afterward.
    - The default settings file is in `drupal_root_folder/sites/default/settings.php`

2.  Look for this code at the bottom (Drupal 6):  

    ``` php
    # $conf['locale_custom_strings_en'] = array(
    #   'forum'      => 'Discussion board',
    #   '@count min' => '@count minutes',
    # );
    ```

3.  Remove the comment marks ('#') and add string replacement assignments:  

    ``` php
     $conf['locale_custom_strings_en'] = array(
       'Old string 1'      => 'New string 1',
       'Old string 2'      => 'New string 2',
     );
    ```

For Drupal 7 the code is the same except for an additional set of square brackets:

``` php
 $conf['locale_custom_strings_en'][''] = array(
   'Old string 1'      => 'New string 1',
   'Old string 2'      => 'New string 2',
 );
```

In order to override other languages, you can do it like below. Pay attention that the input string has to be English and the output the translated new string. Multiple languages can be placed below each other in one settings.php file.

``` php
 $conf['locale_custom_strings_en'][''] = array(
   ...
 );
 $conf['locale_custom_strings_nl'][''] = array( // nl Is the Dutch language code
   'Old English string 1'      => 'New Dutch string 1',
   'Old English string 2'      => 'New Dutch string 2',
 );
```

## Method 2: String Overrides module

(<http://drupal.org/project/stringoverrides>)

### Pros

- Admin page for managing string replacements.
- Uses access permissions. Easier to delegate management of replacements.

### Cons

- Yet another module to install, update, and administer.
- The possible performance hit and more difficult to deploy (stores replacements in the database).
- Uses access permissions. Harder to restrict changes when you have to give administrator access to others.

### Procedure

1.  Install and enable the module.
2.  Follow the instructions/documentation for adding string replacements.

## Method 3: hook_boot() (tested with d7)

### Procedure

1.  Implement the hook_boot()
2.  Use the same array as in the `settings.php`.

``` php
/**
 * Implements hook_boot().
 */
function mymodule_boot(){
  global $conf;
  $conf['locale_custom_strings_en'][''] = array(
   'Old string 1'      => 'New string 1',
   'Old string 2'      => 'New string 2',
 );
}
```
