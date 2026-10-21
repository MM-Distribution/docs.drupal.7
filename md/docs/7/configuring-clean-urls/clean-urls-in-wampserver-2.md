---
title: "Clean URLs in Wampserver 2"
source_url: "https://www.drupal.org/docs/7/configuring-clean-urls/clean-urls-in-wampserver-2"
page_type: page
last_updated: "Last updated on 16 October 2016"
published: "2016-10-15T18:01:59+00:00"
modified: "2016-10-16T08:07:51+00:00"
breadcrumb: ["Drupal 7", "Configuring clean URLs in Drupal 7"]
fetched: "2026-10-21T06:52:13Z"
raw: "raw/docs/7/configuring-clean-urls/clean-urls-in-wampserver-2.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Clean URLs in Wampserver 2

This procedure is nearly like configuring Clean URLs in XAMPP, but with a couple spots where things go elsewhere. Note that this presumes the standard **Wampserver 2** download from <http://www.wampserver.com/en/download.php>, that it has installed, and that your basic Apache, MySQL, and PHP set-ups are working correctly.

## Step by Step:

1.  **Install Drupal as outlined elsewhere:**  
    Be sure to note the base directory you install the Drupal software into. Check Site Configuration \>\> Clean URLs to see whether Clean URLs are enabled or disabled. If they're enabled, you're done. If disabled, and Drupal warns of a misconfiguration, follow the steps below.

2.  **Editing Apache's httpd.conf file:** Search for the mod_rewrites load module line in the file and remove the "#" at the first character.  

    ``` php
    #
    # LoadModule rewrite_module modules/mod_rewrite.so
    #
    ```

    Cut and paste the line just before or just after the mod_cache load module line like this:

    ``` php
    #
    # About 75 lines of load module code
    #
    LoadModule autoindex_module modules/mod_autoindex.so
    #
    #LoadModule cache_module modules/mod_cache.so
    LoadModule rewrite_module modules/mod_rewrite.so
    #
    #LoadModule cern_meta_module modules/mod_cern_meta.so
    #
    # The remainder of the file follows from here.
    ```

3.  Refresh or reload the Site Configuration \>\> Clean URLS page again. Has the warning changed? If so, and it says you can enable the Clean URLS option, enable it, and you're done.

4.  **Editing the Alias in Wampserver:** Here's where you need the installation directory you wrote down in Step 1. Locate the file named **drupal.conf** in the "alias" sub-directory immediately below the Wampserver installation directory. (If you installed Wampserver into **c:\wamp**, you want **c:\wamp\alias\drupal.conf**.) Load the file into a text editor. You should have a single paragraph with a fresh install of Wampserver and Drupal. Edit the file so it reads like this:  

    ``` php
    Alias /drupal "{Drupal installation directory/}drupal/"
      <Directory "{Drupal installation directory/}drupal">
          Options Indexes FollowSymLinks MultiViews
          AllowOverride All
          Order allow,deny
          Allow from all
      </Directory>
    ```

5.  Recheck and/or reload the Site Configuration \>\> Clean URLs page. The option to Enable Clean URLs should be enabled, so you can click "Enable" and press "Save Configuration."

It's worth mentioning that you may need to set one more configuration line in the **.htaccess** file in the Drupal base directory. Load the file from Step 2 into your text editor, and search for the lines like those listed below:

``` php
  # Modify the RewriteBase if you are using Drupal in a subdirectory or in a
  # VirtualDocumentRoot and the rewrite rules are not working properly.
  # For example if your site is at http://example.com/drupal uncomment and
  # modify the following line:
  # RewriteBase drupal
  #
  # If your site is running in a VirtualDocumentRoot at http://example.com/,
  # uncomment the following line:
  # RewriteBase /
```

Follow the instructions and edit the line as needed.

Finally, restart the web server.

At this point, you should have clean URLs enabled, and working correctly.
