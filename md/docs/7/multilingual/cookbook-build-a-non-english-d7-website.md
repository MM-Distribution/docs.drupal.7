---
title: "Cookbook: Build a non-English D7 website"
source_url: "https://www.drupal.org/docs/7/multilingual/cookbook-build-a-non-english-d7-website"
page_type: page
last_updated: "Last updated on 27 April 2018"
published: "2014-08-03T16:24:48+00:00"
modified: "2018-04-27T18:44:48+00:00"
breadcrumb: ["Drupal 7", "Multilingual guide for Drupal 7"]
fetched: "2026-10-21T06:09:58Z"
raw: "raw/docs/7/multilingual/cookbook-build-a-non-english-d7-website.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Cookbook: Build a non-English D7 website

This **[Cookbook](http://en.wikipedia.org/wiki/Cookbook#Usage_outside_the_world_of_food "Cookbook in Wikipedia")** shows, how you can build **a new website** using Drupal 7 **with only ONE (non-English) language**. The administration language remains English, because this is the language on [www.drupal.org](https://www.drupal.org/).

***Remarks***

- The intention of this cookbook is to explain the building of a non-English website as **a working demo**. All visitors of this website (except for the admins) only see this ONE language!

- I assume that we are installing this development server on a Windows client, for this purpose the Steps 1 and 2 of the [Quick install Drupal with XAMPP on Windows](/node/2347717) are done for *Drupal 7*. The homepage of this website will be <http://127.0.0.1/drupal7/>.

  **But:** XAMPP should **only** be used as a **development server** (<https://www.apachefriends.org/about.html>)!

- If you use another system of installation of the websever or another webserver or another OS on your computer, you have to read your homepath of the webserver instead of "*C:\xampp\htdocs\drupal7\\*"!

## *Cookbook:*

**Follow it *step by step*[1)](#note1 "Look at this note!")!**

## Step 1: Install Drupal 7

Install **Drupal 7** as told in the [Installation Guide](https://www.drupal.org/documentation/install) on [www.drupal.org](https://www.drupal.org/).

For your first try of this cookbook use a fresh installed **Drupal 7** (**Recommended** release) from <https://www.drupal.org/project/drupal> with **Default profile** in the path "*C:\xampp\htdocs\drupal7\\*" and then start with the next step.

## Step 2: Install SEO supplements

I recommend the following key **modules** to install[2)](#note2 "Look at this note!"):

1.  **Token** from <https://www.drupal.org/project/token>
2.  **Pathauto** from <https://www.drupal.org/project/pathauto>
3.  **Subpathauto** from <https://www.drupal.org/project/subpathauto>
4.  **Pathologic** from <https://www.drupal.org/project/pathologic>
5.  **Transliteration** from <https://www.drupal.org/project/transliteration>

They ensure that the paths are displayed in the form "*<http://www.example.com/content/hello>*", not as "*<http://www.example.com/node/532>*" and are listed accordingly in the respective side's \<head\> area.

Download these modules and unpack them to the path "*C:\xampp\htdocs\drupal7\sites\all\modules\\*".

Then put a tick "Enabled" for these modules at "<http://127.0.0.1/drupal7/admin/modules>" and then click "*Save configuration*".

Now you have to configure these modules:

1.  At <http://127.0.0.1/drupal7/admin/config/search/path/settings> put a tick "Transliterate prior to creating alias" and then click "*Save configuration*".
2.  At <http://127.0.0.1/drupal7/admin/config/search/path/subpaths> you can administer the subpaths, then click "*Save configuration*".
3.  At <http://127.0.0.1/drupal7/admin/config/content/formats> configure **all** text formats ("Filtered HTML", "Full HTML" **and** "*Plain text*") like:
    - Put a tick "Correct URLs with Pathologic",
    - at "Filter processing order" drop "Correct URLs with Pathologic" down to be the last row,
    - at "Filter settings" within the tab "Correct URLs with Pathologic" set "Processed URL format" to "Path relative to server root (`/foo/bar`)" and add the two lines "<http://127.0.0.1/drupal7/>" and "/" in the field "All base paths for this site",
    - then click "*Save configuration*".

For information, refer to the appropriate help.

## Step 3: For a non-English website

For a functional **non-English** language site[2)](#note2 "Look at this note!") you should install some **additions**:

1.  **Locale** (core-module)
2.  **Administration language** from <https://www.drupal.org/project/admin_language>[3)](#note3 "Look at this note!")
3.  **Localization update** from <https://www.drupal.org/project/l10n_update>

The **Locale** module allows your Drupal site to be presented in languages other than the default English.  
The module **Localization update** automatically loads down the installed translations of the Drupal interface, so it guarantees and updated the **non-English** translation of the website **interface** (in other CMS called "*frontend*" and "*backend*").

In the administration of the website (Admin menu and the admin pages) the module **Administration language** serves the English language. This allows that all descriptions on <https://www.drupal.org/documentation> can be followed without any translation work.

Download the non-core-modules and unpack them to the path "*C:\xampp\htdocs\drupal7\sites\all\modules\\*".

Then put a tick "Enabled" for these modules at "<http://127.0.0.1/drupal7/admin/modules>" and then click "*Save configuration*".

**Hint:**  
At this moment, do **not add** a language[4)](#note4 "Look at this note!")!

Now you have to configure one module:

1.  At <http://127.0.0.1/drupal7/admin/config/regional/language/update> at "Update mode" put a tick "Edited translations are kept, only previously imported ones are overwritten and new translations are added", at "Store downloaded files" type in "*sites/all/translations*" and then click "*Save configuration*".

For information, refer to the appropriate help or the files README.txt of the installed modules

## Last Step: Add your language and the language settings[4)](#note4 "Look at this note!")

Goto <http://127.0.0.1/drupal7/admin/config/regional/language/add> and select the language of your website in the field **Language name** and then click "*Add language*".

In the column "Default" set the bullet to your new language and then click "*Save configuration*".

Now we need to do some configuration:

1.  Adjust the **Regional settings** at <http://127.0.0.1/drupal7/admin/config/regional/settings>.
2.  At <http://127.0.0.1/drupal7/admin/config/regional/date-time/formats/add> you can add new **Time-formats** (e.g. for the German Medium date-format: "*D., d.m.Y - H:i*", this shows dates like "Sun., 03.08.2014 - 16:03"), if you need them in the next configuration step.
3.  At <http://127.0.0.1/drupal7/admin/config/regional/date-time/locale> click on "Edit" in the row with your new language.  
    Select the correct date format in the column "Format" of every row.  
    Then click "*Save configuration*".
4.  At <http://127.0.0.1/drupal7/admin/config/regional/language/admin_language> select the option you want, I normally **enable** all options. Then click "*Save configuration*".

## Hint

Now you can build your website like the [Site Building Guide](https://www.drupal.org/documentation/build) shows on [www.drupal.org](https://www.drupal.org/).

Good luck!

------------------------------------------------------------------------

## Notes

<span id="note1">1)</span> = These steps will change significantly in **Drupal 8**!

<span id="note2">2)</span> = But in a multilingual website for the visitor is recommended to choose a different approach.

<span id="note3">3)</span> = This module is for a non-English website in fact **not necessary**, but for me is the default for all non-English spoken websites. Thereby the administration language remains English, because this is the language on [www.drupal.org](http://www.drupal.org).

<span id="note4">4)</span> = We do this here at the end of this cookbook in order not to change the flow of this cookbook through translations.
