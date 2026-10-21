---
title: "Multi-site on Windows - using XAMPP"
source_url: "https://www.drupal.org/docs/7/multisite/multi-site-on-windows-using-xampp"
page_type: page
last_updated: "Last updated on 31 October 2023"
published: "2012-07-13T04:19:20+00:00"
modified: "2023-10-31T12:38:45+00:00"
breadcrumb: ["Drupal 7", "Multisite Drupal 7"]
fetched: "2026-10-21T06:12:49Z"
raw: "raw/docs/7/multisite/multi-site-on-windows-using-xampp.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Multi-site on Windows - using XAMPP

It is **not** recommended to use XAMPP, use a [Docker-based solution](https://www.drupal.org/docs/develop/local-server-setup/docker-based-development-environments/docker-based-solutions-overview) such as DDEV or Lando instead.

## My setup

XAMPP runs on the same computer as my browser.

## Remarks

- **Important Safety Notice:**  
  The safe operation of the web server, that can be accessed from the internet, **is not guaranteed** by XAMPP, which is a **development** system!
- The same configuration on another webserver (e.g. apache, but **not** XAMPP) is ok!

## ToDo-List

**Follow it *step by step*!**

1.  Download [XAMPP](https://www.apachefriends.org/) and install it at '`C:\xampp`' (and **NOT** at '`C:\Program Files\xampp\`' or similar!).

2.  Check for '`httpd.conf`' file at '`C:\xampp\apache\conf`' and  
    change

    ``` php
    # Virtual hosts
    #Include "conf/extra/httpd-vhosts.conf"
    ```

    to

    ``` php
    # Virtual hosts
    Include "conf/extra/httpd-vhosts.conf"
    ```

    only, if the "**\#**" was in that row!

3.  Now open '`httpd-vhosts.conf`' from '`C:\xampp\apache\conf\extra`' and add these lines  

    ``` php
    <VirtualHost *:80>
        ServerAdmin postmaster@host.localhost
        DocumentRoot "C:/xampp/htdocs"
        ServerName localhost
        ServerAlias www.localhost
        ErrorLog "logs/host.localhost-error.log"
        CustomLog "logs/host.localhost-access.log" combined
    </VirtualHost>

    <VirtualHost *:80>
        ServerAdmin postmaster@dummy-host.localhost
        DocumentRoot "C:/xampp/htdocs/drupal"
        ServerName dummy-host.localhost
        ServerAlias www.dummy-host.localhost
        ErrorLog "logs/dummy-host.localhost-error.log"
        CustomLog "logs/dummy-host.localhost-access.log" combined
    </VirtualHost>

    <VirtualHost *:80>
        ServerAdmin postmaster@dummy-host2.localhost
        DocumentRoot "C:/xampp/htdocs/drupal"
        ServerName dummy-host2.localhost
        ServerAlias www.dummy-host2.localhost
        ErrorLog "logs/dummy-host2.localhost-error.log"
        CustomLog "logs/dummy-host2.localhost-access.log" combined
    </VirtualHost>
    ```

    If the file contains `NameVirtualHost *:80` with a leading "#", remove the hash ("#").

4.  Restart/reload your web server.

5.  Now open file '`%windir%\system32\drivers\etc\hosts`' and add these 4 lines at end of file  

    ``` php
    127.0.0.1    dummy-host.localhost
    127.0.0.1    dummy-host2.localhost
    127.0.0.1    www.dummy-host.localhost
    127.0.0.1    www.dummy-host2.localhost
    ```

6.  Now download [the latest recommended Drupal release](https://drupal.org/project/drupal),  
    create a folder name "`drupal`" inside '`C:\xampp\htdocs\`'  
    and put **all** content of this drupal release (including the folder structure and its content) in this folder.  
    Now you can find e.g. the file '`C:\xampp\htdocs\drupal\sites\default\default.settings.php`', you need it.

7.  Create 2 folder name  
    a.) `dummy-host.localhost`  
    and  
    b.) `dummy-host2.localhost`  
    inside of '`C:\xampp\htdocs\drupal\sites\`'

8.  Create 2 databases for 2 drupal sites (e.g. with name `dummyhost` and `dummyhost2`) using `http://127.0.0.1/phpmyadmin/`.

9.  Open url  
    a.) `http://dummy-host.localhost/`  
    and  
    b.) `http://dummy-host2.localhost/`  
    and install them as standard drupal installation process (<http://drupal.org/documentation/install>).

10. Now Drupal "multisite installation" is done, you should look at  
    a.) `http://dummy-host.localhost/`  
    and  
    b.) `http://dummy-host2.localhost/`  
    for further installation.
