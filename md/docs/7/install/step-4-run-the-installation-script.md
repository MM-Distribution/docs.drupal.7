---
title: "Step 4: Run the installation script"
source_url: "https://www.drupal.org/docs/7/install/step-4-run-the-installation-script"
page_type: page
last_updated: "Last updated on 5 February 2018"
published: "2008-04-25T05:30:41+00:00"
modified: "2018-02-05T10:21:53+00:00"
breadcrumb: ["Drupal 7", "Installing Drupal 7"]
fetched: "2026-10-21T05:54:44Z"
raw: "raw/docs/7/install/step-4-run-the-installation-script.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Step 4: Run the installation script

To run the Drupal install script, point your browser to the base URL of your website. 

The *base URL* means the document root (directory) where you placed your Drupal files (and is defined in your web server configuration file). If you have installed Drupal on a web host this will likely be a domain name such as `http://www.example.com`. If you installed Drupal in a subfolder, you should point your browser to the subfolder (for example, `http://example.com/subfolder`). If you installed Drupal on your desktop machine, the URL might be `http://localhost/drupal`.

If the installation process does not simply appear by entering the base URL of your site, add the file name `install.php` to the end of your site's URL (for example, `http://www.example.com/install.php`).

### Installation process

After you run `install.php`, you'll be guided through several pages:

![](/files/installer_0.png)

1.  Choose which profile to use for the installation (standard or minimal or your chosen distribution).

    Most people should select the "standard" option. The standard option comes with default content types already enabled, such as *Article* and *Page*, and with appropriate publishing options already set. (Of course you can later edit these default content types and their settings, or add additional ones.) The standard profile also has a useful collection of modules pre-enabled for you.

    The "minimal" option is targeted toward more experienced Drupal site creators who wish to set up their own content types with associated publishing options. The minimal profile has only three modules enabled: [Block](/handbook/modules/block), [Database logging](/handbook/modules/dblog), and [Update status](/handbook/modules/update).

    More info about [built-in installation profiles](/node/1127786).

    Choose the 'name of your distribution', if you have downloaded a distribution and not a normal drupal at step one.

    ![](/files/profiles_0.png)

2.  If you want to install using a language other than the default English, click the *Learn how to install Drupal in other languages* link.

    ![](/files/language.png)

3.  If your installation directory is not yet configured properly, you'll be informed on this page. You can correct the settings individually and either refresh the browser screen or click 'Try again' to see whether there are any errors left.

    ![](/files/requirements.png)

    Reported errors can include:

    - **Missing directories and/or incorrect permissions**  
      The installer will attempt to automatically set up a number of directories, but this may fail due to permission settings. In this case you will find the missing directories listed.

      - `sites/default/files`
      - `sites/default/private`
      - `sites/default/private/files`

      These directories should be set to the following permissions:

      ``` php
      chmod o+w sites/default/files
      ```

      OR

      ``` php
      chmod 777 sites/default/files
      ```

    - **Missing `settings.php` or incorrect permissions**  
      If `settings.php` is missing or not accessible, follow the instructions in [Step 3: Create the settings.php file](/documentation/install/settings-file). Note that you will need *both* the `default.settings.php` and `settings.php` files.

4.  Enter the database name, the username, and the password for the database that you created in [Step 2: Create the database](/documentation/install/create-database). This username and password information allows Drupal to access your database so the install script can create tables. Note that this is *not* the username and password for administering Drupal; these will be created in the next step.

    ![](/files/dbconfig.png)

    The *Advanced options* allow you to change the database host ('localhost' is usually used in this entry: `wamp/bin/apache/Apache2.2.11/bin/php.ini` as an example of the location on a Windows computer running [WAMP](http://www.wampserver.com/en/)). You can also change the port and the table prefix. You only need to change the port if you are using a non-standard port number. The table prefix is useful if you are installing multiple instances of Drupal tables that share the same database.

    Click *Save and continue* at the bottom of the page.

5.  A progress bar will appear and display notes from the installer regarding the progress of the installation. If no errors are encountered, the next page will automatically load in your browser.

6.  After the installer completes, input the information for the first user account (which will be automatically assigned full administration permissions) and provide basic website settings.

    - In the *Site name* field enter the name you wish to use for the site. You can also edit it later through the administration interface.

    - In the *Site e-mail address* field, enter the e-mail address that will be used by Drupal when it sends out notifications such as registration information.

    - In the *Site maintenance account* field, enter the *Username*, *E-mail address*, and *password* for the main administration account.

      Note that as of Drupal 7 there is a distinction between the main administration account that you set up on this page, and the "Administrator" *site administrator* user role that you will see when you visit the "Roles" and "Permissions" pages in the administration interface. The account you set up in the *Site maintenance account* section during installation is a super-user who has overall control over every aspect of the management and configuration of the site. (For those of you familiar with the account from earlier versions of Drupal, this will be `http://www.example.com/user/1`.)  
      ![](/files/siteinfo_0.png)

    - In the *Server settings* field, select your *Default country* and *Default time zone*.

    - In the *Update notifications* field, leave both check boxes selected if you want your Drupal server to alert you when updates are required. Often updates relate to security issues and are important to perform. However, if you have restricted Internet connectivity (for example, if you are behind a corporate firewall) you may want to leave these settings unselected and then test them later.  
      ![](/files/siteinfo2_0.png)

    Click "Save and continue". On success you will see the *Drupal installation complete* screen. If there are any error messages, review and correct them now.  
    ![](/files/complete.png)

### Secure your site

After the installation is complete, you will want to change the permissions on the `settings.php` file back so that it is protected:

``` php
chmod u=rw,o=r,a=r sites/default/settings.php
```

OR

``` php
chmod 644 sites/default/settings.php
```

If you make manual changes to the `settings.php` file later, be sure to protect it again after making your modifications.

***Important:** Failing to remove write permissions to the `settings.php` file is a security risk.*

*Although the default location for the `settings.php` file is at `sites/default/settings.php`, it may be in another location if you use the multisite setup.*
