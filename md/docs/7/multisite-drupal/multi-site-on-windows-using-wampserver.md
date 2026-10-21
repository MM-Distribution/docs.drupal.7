---
title: "Multi-site on Windows - using WampServer"
source_url: "https://www.drupal.org/docs/7/multisite-drupal/multi-site-on-windows-using-wampserver"
page_type: page
last_updated: "Last updated on 30 August 2016"
published: "2009-08-13T03:58:22+00:00"
modified: "2016-08-30T13:47:11+00:00"
breadcrumb: ["Drupal 7", "Multisite Drupal 7"]
fetched: "2026-10-21T06:12:33Z"
raw: "raw/docs/7/multisite-drupal/multi-site-on-windows-using-wampserver.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Multi-site on Windows - using WampServer

This page describes how to set up a multi-site Drupal install using Windows and Apache, via the [WampServer](http://www.wampserver.com/en/) package. The instructions cover how to set up live production sites as well as local development sites, and setting up new sites as well as making copies of existing sites.

Topics covered include: Installing and configuring WAMPServer, configuring and troubleshooting Apache and MySQL, creating databases, users and permissions in PHPMyAdmin, creating DNS entries and/or hosts file entries, creating sites directories, and installing multiple Drupal instances.

Before we begin, here are some notes for two use cases where the instructions are slightly different. If they do not apply to you, skip ahead to *First Step: Installing WAMPServer*.

### (Optional) Adding a new site to an existing Drupal WAMPServer instance

You may use these instructions to add an additional site to an *existing* single site WAMPServer Drupal install. In that case, follow along but skip any steps you've already done for your existing installation, like installing WAMPServer and configuring your first site. You do still have to add a new database and database user, DNS/hosts entries, extra site directories and the Drupal install steps. Depending on your Apache configuration, you may also have to turn on Virtual Hosting if you were not using it before, and configure the virtual hosts for localhost and your existing sites in the virtual host steps.

### (Optional) Migrating or copying existing sites instead of installing new ones

These instructions will also help you migrate an existing site to a multi-site WAMPServer install. A common use case for this is making a local development server on your Windows machine, where you can test changes to a copy of your production site hosted on a server somewhere. In that case, follow the instructions here but instead of creating empty databases in PHPMyAdmin, you will be creating an empty database then loading in a SQL backup taken from your production server. Instead of downloading a stock Drupal version from drupal.org and unpacking it, you will most likely use an existing copy of your Drupal files, copied from your existing server. Or you might use source control software such as git or svn to get a copy of the files on your local machine. In that case the location of the files should be substituted for*c:\wamp\www\drupal-7.0* in the examples here.

## First Step: Installing WAMPServer

WAMPServer is a free Apache/PHP/MySQL stack for Windows.

If you do not already have WAMPServer installed, you should download and install it from here:

- [WAMPServer](http://www.wampserver.com/en/) - includes Apache, PHP, and MySQL.

WAMPServer comes in both 32-bit and 64-bit editions. Choose the 32-bit or 64-bit version depending on whether you have the 32-bit or 64-bit edition of Windows. If you are not sure which edition you have, check your *System Type* in Start-\>Control Panel-\>System . If you are still not sure, or if you are running Windows XP, just choose the 32-bit edition, which works on both types of Windows.

The default install location for WAMPServer is *c:\wamp*. If you install into another folder, substitute that for *c:\wamp* in the examples here!

If you are running a firewall or Internet security software, you will have to click **Allow** several times during installation. At the end of the installation, make sure **Launch WAMPServer** is checked and click **Finish**.

You should now have the WAMPServer Manager icon in your task bar (the icons kept at the bottom right, by the clock). The icon may be hidden, in which case you must press the *Show hidden icons* button (which looks like an arrow) to see it. The WAMPServer icon looks like the letter W, and is Green when the server is running, and Red when the server is stopped. Clicking the WAMPServer icon will open a menu with access to the WAMPServer web pages, information about your server, and the *PHPMyAdmin* database administration tool.

While you are setting up WAMPServer, turn on The *rewrite* module. You will need that enabled later for [Clean URLs](/getting-started/clean-urls).

1.  Click the WAMPServer Manager icon in your taskbar, and choose **Apache - Modules - Rewrite Module** so that it is checked.

## Create a database for each of your sites

You must create a new database for each of the sites you are installing in PHPMyAdmin. While the sites share the Drupal codebase (PHP files), they each require their own MySQL database. (unless you [Share a database across multiple sites](/node/2622)).

Follow these steps for each site's database:

1.  Click the WAMPServer Manager icon in your taskbar, and choose **phpMyAdmin** to open the PHPMyAdmin database administration tool.

2.  (optional) If you set a password for your MySQL root user, log in with it now, otherwise PHPMyAdmin logs in with the default local root username, with no password, connecting from localhost.

3.  Click on the *Databases* link at the top of the page. A list of existing databases on your MySQL server is shown. At the bottom of this page is a text box titled *Create New Database*.

4.  Type the name of your first database into the text box (e.g.: **site1**).

5.  From the *collation* dropdown, choose **utf8** - **utf8-general-ci**.

6.  Click **Create**. PHPMyAdmin will load a new page and should report success and show the SQL command that it ran. For our *site1* example, PHPMyAdmin outputs something this:  

    > *Database site1 has been created.*
    >
    > ``` php
    > CREATE DATABASE `site1` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
    > ```

7.  If you wish to add more databases after this one, click the **localhost** link at the top of the page to get back to the PHPMyAdmin start page, then click **Databases** again and add the next database.

Use this procedure to set up a database for each site. Each database must have a unique name, and ideally you would name the database after the site, so it's clear which site it belongs to.

If you are migrating an existing site, you will want to use PHPMyAdmin's *Import* function to load the .sql or .sql.gz file that contains your existing site's database backup into place.

If you like, you can create a user or several users so that you can limit permissions to the database for each site, and ensure Drupal and contrib modules don't have super-user access to your MySQL database. This is definitely a very good idea on production servers or production websites. For local or development sites, you can also get away with using WAMPServer's default root user (username: root, no password, connecting from localhost only).

## Optional: Create MySQL usernames and passwords to access the sites

Create one or more MySQL users using the following steps:

1.  In PHPMyAdmin, click the **Privileges** link at the top of the page.

2.  Click **Add New User**

3.  Enter a *Username* (e.g.: **site1_user**)

4.  Set the *Host* dropdown to be **Local**.

5.  Click **Generate** to generate a strong random password, or type and confirm a password. If you generate a random password, it is displayed - **copy and paste it somewhere safe, you will need the username and the password to install Drupal!**.

6.  Leave everything else alone and click **Go** at the bottom of the page. PHPMyAdmin should tell you the user is added, and display the SQL commands it used:  

    > You have added a new user.
    >
    > ``` php
    > CREATE USER 'site1_user'@'localhost' IDENTIFIED BY '***';
    >
    > GRANT USAGE ON * . * TO 'site1_user'@'localhost' IDENTIFIED BY '***' WITH MAX_QUERIES_PER_HOUR 0 MAX_CONNECTIONS_PER_HOUR 0 MAX_UPDATES_PER_HOUR 0 MAX_USER_CONNECTIONS 0 ;
    > ```

7.  Scroll down to the section **Database-specific privileges**. From the dropdown, select the database name you wish to give permissions to. (e.g.: site1). As soon as you select the database, PHPMyAdmin will load a page titled something like: *Edit Privileges: User 'site1_user'@'localhost' - Database site1*.

8.  Click **Check All** to check all the privilege checkboxes, and click **Go**.

9.  PHPMyAdmin responds with:  

    > You have updated the privileges for 'site1_user'@'localhost'.
    >
    > ``` php
    > GRANT ALL PRIVILEGES ON `site1` . * TO 'site1_user'@'localhost' WITH GRANT OPTION ;
    > ```

You can repeat the process for as many users as you like. You may also assign permissions for more than one database to a user. Remember to keep a note of each database name, username, and password for the installation!

If your server is a production server, you should probably also set a password for MySQL's *root* user. You can edit the user in the **Privileges** and change its password. After you do so, PHPMyAdmin will ask you to re-authenticate using the password.

## Download and unpack Drupal

Download Drupal core from <http://drupal.org/project/drupal> and place the .zip or .tar.gz file into WAMPServer's *c:\wamp\www* folder. (You'll need a tool like [7-zip](http://www.7-zip.org) to unpack the Drupal tar.gz or .zip file). Once you unpack the file, you will have a Drupal folder with the version number in your c:\wamp\www folder (e.g. c:\wamp\www\drupal-7.0). This Drupal codebase appears on your WAMPServer at <http://localhost/drupal-7.0>, but because you are doing a multi-site install, you will not access it at this URL, but instead use Apache virtual hosts to add multiple URLs that point here, using other site names (e.g. <http://site1.example.com> and <http://site2.example.com>)

If you are migrating an existing site from another server, you probably want to copy the Drupal files from that server, so you have a complete set of modules, themes, and site files. You could do this by FTP, by making a .zip or .tar.gz backup file and transferring that, or by using source control such as Subversion or git. If you place the existing Drupal files somewhere other than *c:\wamp\www\drupal7.0*, substitute the correct path in the rest of this page's examples.

## Enable and configure Apache Virtual Hosts

A *Virtual Host* is an Apache configuration directive that describes a web site to host. You can have as many Virtual Hosts on an Apache server as you like. Based on what URL the web surfer asks for, Apache can figure out the correct web site to serve them. With a multi-site install, you will always be setting up at least two distinct URLs for accessing your website. For our example multi-site install with two sites, our two virtual hosts are going to be: <http://site1.example.com> and <http://site2.example.com>. We also set up a virtual host that matches the default configuration, and load that on <http://localhost>, so that WAMPServer's shortcuts will still work!

First, enable Virtual Hosts in Apache's configuration file:

1.  click the WAMPServer administration tool in your taskbar, and choose **Apache - httpd.conf**. The Apache configuration file (httpd.conf) will open in Notepad.

2.  Scroll to the end of the file and you will find a section titled *Supplemental Configuration*.

3.  Find the section:  

    ``` php
    # Virtual hosts
    #Include conf/extra/httpd-vhosts.conf
    ```

4.  remove the **\#** (comment indicator) in front of the second line, so it now looks like this:

    ``` php
    # Virtual hosts
    Include conf/extra/httpd-vhosts.conf
    ```

5.  Save the file.

Next, locate and edit the *httpd-vhosts.conf* file. It should be in a folder named **C:\wamp\bin\apache\Apache2.2.17\conf\extra**, but with the correct Apache version to match what was installed with your WAMPServer. The best way to find this file is to just explore through c:\wamp\bin\apache until you find the *conf* folder, then look in the *extra* subfolder.

Replace the example \<VirtualHost\> examples with the following, adjusted to match your site names. These examples use site1.example.com and site2.example.com, and you will need to adjust yours to match your site names

``` php
<VirtualHost *:80>
    ServerAdmin webmaster@site1.example.com
    DocumentRoot "C:/wamp/www/drupal-7.0"
    ServerName site1.example.com
    ServerAlias www.site1.example.com
    ErrorLog "c:/wamp/logs/site1.example.com-error.log"
    CustomLog "c:/wamp/logs/site1.example.com-access.log" common
</VirtualHost>

<VirtualHost *:80>
    ServerAdmin webmaster@site2.example.com
    DocumentRoot "C:/wamp/www/drupal-7.0"
    ServerName site2.example.com
    ServerAlias www.site2.example.com
    ErrorLog "c:/wamp/logs/site2.example.com-error.log"
    CustomLog "c:/wamp/logs/site2.example.com-access.log" common
</VirtualHost>

<VirtualHost *:80>
    ServerAdmin webmaster@site2.example.com
    DocumentRoot "C:/wamp/www"
    ServerName localhost
    ErrorLog "c:/wamp/logs/error.log"
    CustomLog "c:/wamp/logs/access.log" common
</VirtualHost>
```

Save the file again.

## Restart WAMPServer and fix any problems

You need to restart Apache so it will see your changes. If anything is wrong, Apache will not start up again, or will not allow you to see the localhost page from the WAMPServer administrator. You must then check Apache's error log and correct the problem, then restart WAMPServer again until it is able to start successfully:

1.  Click the WAMPServer icon in the taskbar and choose **Restart All Services**.
2.  You will notice the WAMPServer icon turn red (meaning the servers are stopped) and then it should turn green again. If the icon stays red, something is wrong with one of the configuration files you changed, and Apache cannot start. There may also be problems after Apache does start, even if the icon is green.
3.  From the WAMPServer menu, choose **Apache - Apache Error Log** then look at the bottom of the log file for error messages. These will usually start with the word: *Warning -*
4.  When everything is working properly, you should be able to see the WAMPServer status page by choosing **localhost** from the WAMPServer menu. This should open your server's home page, showing version numbers and status. If instead you see a white screen with a "Permission Denied" message, it means something is wrong with your configuration, and Apache stopped reading the configuration files (resulting in your localhost page not loading).
5.  Fix any problems, restart Apache, and check the error log until you see no errors at the bottom and you can open the localhost web page successfully.

## Add DNS entries or hosts file entries for each site address

There are two ways to make <http://site1.example.com> and <http://site2.example.com> come up in your web browser:

1.  If this is a production site, or is going to be accessed by others on the Internet, you should add real DNS entries at your registrar, pointing to your computer's external IP address. This is a good option if your computer is a server. You may need to also configure your firewall or router to forward port 80 from the external IP to your computer. (If you are not sure of your external IP address, visit <http://www.whatismyipaddress.com>.
2.  If this is just a test or development site, and you only need to get to it from your local computer, then it is often easier to add fake DNS entries in your *hosts file*. The hosts file is a text file where you can specify fake DNS entries that will work like real DNS entries, but only on your local computer. This will allow you to point a browser at <http://site1.example.com> and have site1.example.com resolve to your computer's localhost address, 127.0.0.1, resulting in you seeing the web page. Remember though that you will not be able to see the site on other computers with this technique.

To add hosts file entries, you can use Notepad. But, the hosts file is a system file, so you have to run Notepad as administrator in Windows 2003 or later. The location of the hosts file is usually **c:\windows\system32\drivers\etc\hosts**, unless your Windows directory is somewhere other than *c:\windows*:

1.  (Windows Vista and later, or Windows Server 2003 and later): Open Notepad as the administrator: **Start - All Programs - Accessories - *Right Click* Notepad** and choose **Run as Administrator**. A User Account Control dialog will appear, asking if you wish to allow Notepad to make changes to your computer. Choose **Yes**.

2.  (Windows XP and earlier):

3.  Choose **Open** from the File menu, and into the Filename box type: **c:\windows\system32\drivers\etc\hosts** and click **Open**. The hosts file will open.

4.  Below the last line *127.0.0.1 localhost*, add lines for each site name, pointing at the localhost IP. The bottom of your hosts file should look like this, substituting *site1.example.com* and *site2.example.com* with your actual site names.  

    ``` php
    127.0.0.1     localhost
    127.0.0.1     site1.example.com www.site1.example.com
    127.0.0.1     site2.example.com www.site2.example.com
    ```

5.  Save the file. If you get a Permission Denied error, it means you forgot to run Notepad as Administrator. Open a new Notepad with the right click-"run as administrator" procedure as described above, then try again.

## Create a site folder for each Drupal site

For each site you are going to host from this Drupal codebase, you need to create a folder in *c:\wamp\www\drupal-7.0\sites\\*. The Drupal installer will create a settings.php file there pointing to each site's database.

Repeat the following for each site:

1.  Create a folder named the same as the URL of the site in the sites folder, e.g. *c:\wamp\www\drupal-7.0\sites\site1.example.com*, with **Right click - New Folder**. Leave the folder empty, because Drupal's installer will create and then write protect a settings.php file for you inside it in the installation step at the end.
2.  A useful new feature in Drupal 7 is the ability to configure aliases for the sites folder using the *sites.php* file. These aliases allow you to use a sites folder and settings.php that do not necessarily match the URL you will be using. To do so, you copy the *default.sites.php* file to be named *sites.php*, and then add an alias to it. You might want to do this if you are using a production Drupal codebase (from git or svn for instance) as a local test site. For example, you might want to use sites directory and settings file *site1.example.com* but access it as a test site on your local machine using URL *<http://site1.local>*. Rather than create a whole new settings directory for *site1.local* with its own settings.php, You could instead add an entry in sites.php that looks like so:  
    `$sites['sites1.local'] = 'site1.example.com';`. For more information on this feature, see the inline comments in *example.sites.php*.
3.  If you are moving or copying an existing site which already has a *settings.php* file, open it and confirm that the database name, database username, and database password are correct for your WAMPServer install.

Once you have created an empty folder for each site under c:\wamp\www\drupal-7.0\sites, you are ready to install Drupal!

## Installing Drupal

For each site you have configured, install Drupal as follows:

1.  Point your web browser at the site URL (e.g. <http://site1.example.com>).
2.  You should see the Drupal installer page, asking you to select an installation profile. If your site already had a settings.php file and it's got the correct database settings, you will see your site and you are finished. Otherwise, continue in the Drupal installer:
3.  Choose an Installation Profile, and then a language, on the first two screens.
4.  The *Set up database* screen appears. Enter the database name, database username, and database password that you made a note of earlier, while creating the database and database users. (e.g.: database name: **site1**, database username: **site1_user**, database password: **SITE1_DATABASE_PASSWORD**). If you did not create users and are just going to use the WAMPServer defaults, use database username of **root** and no password.
5.  If the database is empty, Drupal will continue on with a fresh installation.
6.  If the database contains an existing Drupal installation, the installer will save settings.php with the correct database information, then show an error message titled *Drupal already installed*. If you click **View your existing site** you will be taken to your site's homepage, which should now work correctly!

Repeating the above steps for each site you configured (e.g. site1.example.com, then site2.example.com, and so on) will install/configure the Drupal databases for each site, leaving you with separate sites hosted out from the same Drupal codebase.

As each site's installation is completed, Drupal 7 creates a *settings.php* file and a *files* folder under the site directory (in our example site1.example.com site, this would be *c:\wamp\www\drupal-7.0\sites\site1.example.com*).

If you would like to have modules or themes that are for only one site, then you will need to create "modules" and "themes" folders inside the sites directory and place the modules and themes in those.

For modules and themes you are going to have shared between all the Drupal sites in this multi-site installation, place them in the *modules* and *themes* that already exist in the *c:\wamp\www\drupal-7.0\sites\all\\* folder.
