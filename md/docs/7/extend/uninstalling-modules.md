---
title: "Uninstalling modules"
source_url: "https://www.drupal.org/docs/7/extend/uninstalling-modules"
page_type: page
last_updated: "Last updated on 19 August 2018"
published: "2008-04-24T16:29:24+00:00"
modified: "2018-08-19T17:17:52+00:00"
breadcrumb: ["Drupal 7", "Extending Drupal 7"]
fetched: "2026-10-21T06:08:25Z"
raw: "raw/docs/7/extend/uninstalling-modules.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Uninstalling modules

Uninstalling a module is easy, but it can be very dangerous. Data associated with the module might be deleted and leave your site in a non-functional state. Hence, remember to create a backup of your database before uninstalling. 

Below we go through an example uninstalling the Views module. It is chosen because it shows that module dependency matters when uninstalling, not because Views is likely to be uninstalled.

### Disabling a module

- Go to the modules administration page (/admin/modules)

  ![](/files/uninstalling-01.png)

- Scroll down until you find the modules that you'd like to remove.

     [![](/files/uninstalling-02.png)](http://www.drupal.org/files/uninstalling-02-full.png)

- In this case, you'll want to disable all of the “Views” set of modules. In order to disable a module, click to uncheck the “enabled” checkbox that's next to it. If a module box is greyed out, that means you cannot yet disable it. This is because there is another module that requires that module to be active.

  [![](/files/uninstalling-05.png)](http://www.drupal.org/files/uninstalling-05-full.png)

- In this case, Views RSS and Views UI must be disabled first before the Views module can be disabled. Uncheck those boxes first, then click on “Save configuration”

  [![](/files/uninstalling-04.png)](http://www.drupal.org/files/uninstalling-04-full.png)

- Once the page refreshes, the checkbox next to the Views module will no longer be greyed out. Repeat the process with the Views module, and everything will be disabled.  

  [![](/files/uninstalling-06.png)](http://www.drupal.org/files/uninstalling-06-full.png)

### Uninstalling a module

Not all modules have specific uninstall functions programmed in. A module will only show up on the uninstall tab if it has this feature. If it doesn't, skip this step and simply delete its files.

- Click on the “uninstall” tab at the top of the modules page. It will look like this:

  [![](/files/uninstalling-08.png)](http://www.drupal.org/files/uninstalling-08-full.png)

- Click on the checkbox next to the desired module (in this case Views) and click the uninstall button.

  [![](/files/uninstalling-09.png)](http://www.drupal.org/files/uninstalling-09-full.png)

- Next, you'll have a screen verifying your intention to uninstall this module.

    [![](/files/uninstalling-11.png)](http://www.drupal.org/files/uninstalling-11.png)

- Click on the uninstall button again, and you'll get a screen with green text verifying that the module is uninstalled.

  [![](/files/uninstalling-12.png)](http://www.drupal.org/files/uninstalling-12-full.png)

### Remove/delete module files

Removal of module files is similar to the process of uploading module files.

#### Using FTP

1.  Use the same FTP client software as used in the uploading process, and use the same connection information.
2.  Navigate to the same directory
3.  Instead of uploading files from your own computer, delete the directory containing the desired module. 

#### **Using command line / SSH**

1.  Use the same SSH client software as used in the uploading process, and use the same connection information.
2.  Navigate to the same directory.
3.  Instead of using the wget command to upload files, use the command “`rm -rf [module folder name]`”. In the Views example, you would type “`rm -rf views`”.

#### Remark:

A module without an uninstaller may leave tables or fields in your database. A module like this must be dealt with manually in order to completely remove it from your database, which is best practice to keep your site clean if you definitely do not want to use this module again. There may be an obviously named table or set of tables in your database which can be easily deleted, but the only way to know for sure is to examine the module installation file to see what was added in the first place. Always create a backup snapshot of your database before attempting this!
