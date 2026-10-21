---
title: "Installing themes"
source_url: "https://www.drupal.org/docs/7/extend/installing-themes"
page_type: page
last_updated: "Last updated on 5 February 2018"
published: "2007-09-16T07:44:53+00:00"
modified: "2018-02-05T13:58:51+00:00"
breadcrumb: ["Drupal 7", "Extending Drupal 7"]
fetched: "2026-10-21T06:07:54Z"
raw: "raw/docs/7/extend/installing-themes.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Installing themes

1.  **Download the theme.**  
    You can find themes on <http://drupal.org/project/themes>, as well as some external sites. Make sure the version of the theme matches your version of Drupal. Note that themes labeled "DEV" are in a development stage. They may be written for a previous/current/future version of Drupal, and they are considered unstable and should be handled with care.
2.  **Extract the files.**  
    When you first get the theme, it will appear in a compressed file format such as 'tar.gz'. On Windows, use a program like 7-Zip to extract it. On the Mac, you can use Stuffit Expander. To extract the file using the Unix command line:  
    `tar -zxvf themename-drupalversionnumber.tar.gz`  
    You should see a list of files extracted into a folder.
3.  **Upload the folder.**  
    FTP/Copy/SCP your files to the desired themes folder in your Drupal installation. Since the *themes folder at the top level of Drupal is reserved for Drupal core themes*, you should create a **sites/all/themes/** directory for contributed (non-core) themes and put uploaded themes there. If you are running a [multi-site installation](/node/346385) of Drupal, you can create a themes folder under sites/my.site.folder and put themes there that are specific to a particular site in your installation. Themes that will be shared between all sites should be placed in sites/all/themes.
4.  **Read the directions.**  
    If the theme has an installation file (usually INSTALL.txt and/or README.txt), read it for specific instructions. There are themes that require special treatment to function properly.
5.  **Enable the theme.**  
    Go to "Appearance" on the main Administration menu of your site. Check the 'Enabled' box next to the theme.
6.  **Optional: Make it the active, default theme.**  
    Check the 'default' box to make this the chosen theme for your site. Enabled alone will allow users to select the theme, if you have allowed that permission.
7.  **Click the 'Save Configuration' button at the bottom.**

If you run into problems, check the themes issue queue and search the forums. If your problem hasn't already been addressed, post a question and someone will try to help you out.
