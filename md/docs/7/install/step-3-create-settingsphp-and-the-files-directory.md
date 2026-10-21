---
title: "Step 3: Create settings.php and the files directory"
source_url: "https://www.drupal.org/docs/7/install/step-3-create-settingsphp-and-the-files-directory"
page_type: page
last_updated: "Last updated on 19 August 2018"
published: "2009-08-04T23:36:25+00:00"
modified: "2018-08-19T16:53:24+00:00"
breadcrumb: ["Drupal 7", "Installing Drupal 7"]
fetched: "2026-10-21T05:54:28Z"
raw: "raw/docs/7/install/step-3-create-settingsphp-and-the-files-directory.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Step 3: Create settings.php and the files directory

In order for Drupal to work, you have to tell Drupal where the database is, what the database is called, and the database credentials to access the database. This information is collected when you run the installer and is stored in the **settings.php** file which is located in:

`sites/default`

When you first extract Drupal, it doesn't come with a settings.php file, instead it comes with default.settings.php. When you first install Drupal, it will attempt to copy and rename default.settings.php to settings.php for you. There are some rare instances where you will need to do this manually which are covered in detail further down on this page.

Finally, the purpose of having default.\[config-file\].php is so you can easily update Drupal, without overwriting the entire configuration that runs your site. Yes, there was a time when that happened...

## Automatic settings.php Overview

By default, Drupal will attempt to create and populate the settings.php file automatically when you use install.php to setup the site. The script also changes the permission on the file to secure it once it is finished and then creates a sites/default/files directory for housing all of your non-core files. Unfortunately, some types of shared/local hosting are configured so PHP and Apache run as the same user. This might result in the install script failing to execute the creation and population of the settings.php file, along with setting permissions and creating the files directory. If you get errors referring to the *Settings file* during installation, you will have to manually create the settings.php file and do a few more tasks before you can run install.php. Once it is created with write permissions, the installation script will automatically populate the proper information for your site config. Afterwards, you will have to re-secure the settings.php file.

At this point, jump to the next page step: [Step 4: Run the installation script](/docs/7/install/step-4-run-the-installation-script). If you run into problems with the installation due to the *Settings*, come back here and follow the Manual steps outlined below.

## Manual settings.php Overview

Drupal comes with a sample settings.php configuration file located at: `sites/default/default.settings.php`  
Before you run the installation script (install.php), you need to copy default.settings.php file as a new file called `settings.php` and change its permissions to be writeable. After the installation, you will need to restrict the permissions again.

## Manual settings.php Detailed Instructions

### Step 1 - Navigation & Creation

Navigate to `sites/default` of your root Drupal install.

Copy the `default.settings.php` file and save the new file as `settings.php` in the same directory (see note below about renaming). If you have shell access (command line) run the following command from the directory that contains your Drupal installation files:

``` php
cp sites/default/default.settings.php sites/default/settings.php 
```

***Note:** Do not simply rename the file. The Drupal installer needs both files.*

If you only have FTP access, you will have to download the file to your computer, rename it, then upload it. Some hosting providers have a file manager on the dashboard where the file can be copied and renamed.

### Step 2 - Check the Permissions Are Writeable

By default, the **sites/default** directory and the **settings.php** file should be writeable. You can check that the permissions of **sites/default** and **settings.php** are writeable by issuing the following commands:

``` php
ls -l sites/ 
```

Permission on **sites/default** should be 755 \[drwxr-xr-x\]:

``` php
ls -l sites/default/settings.php 
```

Permission on **settings.php** should be 644 \[-rw-r--r--\]:

If they are anything but writeable, you can issue the following commands:

``` php
chmod 644 sites/default/settings.php 
```

***Note:** If you are in the same group as the web user, then changing the permissions to `664` will be sufficient.*

Several FTP tools like [Filezilla](http://filezilla-project.org "Filezilla"), [Transmit](https://panic.com/transmit/), and [Fetch](http://fetchsoftworks.com/) etc. allow you to change file permissions, using a 'file attribute' or 'get info' command. In this case the file permission should be set to 644. If your FTP client has checkboxes for setting permissions, check both the Read and Write boxes for "Owner", "Group", and "Others" (but leave the Execute boxes unchecked). For some situations, you may need a permission of 664. Some hosting providers allow a similar operation through the dashboard file manager.

### Step 3 - Try the Install

At this point, give the install a go. See if you can get through the installation by running http://\[yoursite\]/install.php. If you are successful, the first page you will want to visit is **Reports** -\> **Status report** (admin/reports/status)

On the reports page, look for a line that says: **File system**. If it says anything other than "Writeable", you will need to follow Step 4 below.

Next, look for a line that says: **Configuration file**. If it says anything other than "Protected", then you will need to re-secure the configuration files as described in **Step 5** below.

### Step 4 - Create the Files Directory

The installation should have created the sites/default/files directory for you, but in the off chance it didn't, you will need to create it manually and set the right permissions on it.

``` php
mkdir sites/default/files 
```

*Note:On most linux systems, a newly created directory is already setup with the 755 permission.* In case it isn't, you can issue the command:

``` php
chmod 755 sites/default/files 
```

This sets the files directory to 755 \[drwxr-xr-x\].

If your site is hosted with an Apache web server, you may need to also give the Apache user write permissions to this folder, so that the web server can save file uploads and regenerate aggregated CSS and JavaScript in this directory. While you may be tempted to use `chmod 777` to achieve this, that allows any user on the server to write to this directory.

To avoid that security vulnerability, it is better to allow the user Apache runs as to write to this directory. You can achieve this by giving the Apache group write permissions to the folder. Typically this is the `apache` or `www-data` user group, though it varies based on your web server's operating system or distribution.

Once you have determined with group your Apache web server uses, change the group assigned to the files directory and give that group write permissions to the directory and all files beneath it. For example, if the Apache user group is `www-data`, you'd run the following:

``` php
chgrp -R www-data sites/default/files
chmod -R g+w sites/default/files
```

Now, the `www-data` group can write to the files directory. You need to make one more change to the directory to ensure our changes above persist. We will use the [setgid](https://en.wikipedia.org/wiki/Setuid) bit to ensure any new files created in this directory are also given the correct group.

``` php
chmod 2775 sites/default/files
```

The 2 is the setgid bit, which means that the group id will be preserved for any new files created in this directory. What that means is that `www-data` will always be the group on any files added to this directory, thereby ensuring that web server and the user will both always have write permissions to any new files that are placed in this directory.

Using the above steps ensures that your files directory is writable by the web server, but secure from writes from unauthorized users.

### Step 5 - Post Install Permission Check

After the installation script has run, Drupal tries to set the permissions automatically to:

555 (read-execute) \[dr-xr-xr-x\] for the sites/default folder.  
and  
444 (read-only) \[-r--r--r--\] for the settings.php

If not, you will need to manually set them:

``` php
chmod 555 sites/default 
```

``` php
chmod 444 sites/default/settings.php 
```

These permissions are correct, and should not be changed, because changing these opens up a security risk.

## OS specific instructions

### Fedora Linux settings.php notes

If you have clean Fedora (or RHEL, CentOS, Scientific Linux) you have SELinux enabled by default after clean installation. There are few more steps to be done to be able to finish Drupal installation on SELinux enabled site to gain more security by SELinux.

If you don't want to use SELinux you may simply disable it, but this is not recommended as SELinux is able to block some exploits. Also you may turn SELinux into permissive mode to go through creating the `settings.php` file (because even if you have set the permissions for writing to `settings.php`, the install script will think you don't because SELinux is active and is blocking writing to `settings.php` file).

To go through installation, do this (as root):

1.  Enable allow_httpd_anon_write boolean:  

    ``` php
    setsebool allow_httpd_anon_write=1 
    ```

2.  Change type of default directory and settings.php to public_content_rw_t (whole command is in one line):  

    ``` php
    chcon -t public_content_rw_t sites/default sites/default/settings.php sites/default/files 
    ```

After the installation finishes, revert previous settings to benefit from SELinux:

1.  Disable allow_httpd_anon_write boolean:  

    ``` php
    setsebool allow_httpd_anon_write=0 
    ```

2.  Reset security context:  

    ``` php
    chcon -R -t httpd_sys_content_t sites/default 
    ```

### Windows (IIS) settings.php notes

On a Windows computer using Internet Information Server (IIS), complete the following steps:

1.  Right-click `sites\default\settings.php`.
2.  Grant **Write** permissions to IUSR_MachineName (IIS6) or IUSR (IIS7).

***Note:** On Windows Server 2008, you can also do this from the command line by running the following command from your `sites\default` directory:*

``` php
icacls settings.php /grant IUSR:W 
```

The installer will change the file back to **Read Only** after installation, but you should verify this after installation.

For more information about modifying Windows file permissions, see the [Troubleshooting FAQ](/node/202491).
