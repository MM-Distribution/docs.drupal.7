---
title: "What is PDO?"
source_url: "https://www.drupal.org/docs/7/system-requirements/what-is-pdo"
page_type: page
last_updated: "Last updated on 24 March 2025"
published: "2009-08-14T23:22:22+00:00"
modified: "2025-03-24T16:27:30+00:00"
breadcrumb: ["Drupal 7", "Drupal 7 system requirements"]
fetched: "2026-10-21T05:52:55Z"
raw: "raw/docs/7/system-requirements/what-is-pdo.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# What is PDO?

PDO is an acronym for PHP Data Objects. PDO is a lean, consistent way to access databases. This means developers can write portable code much easier. PDO is not an abstraction layer like PearDB. PDO is a more like a data access layer which uses a unified API (Application Programming Interface).

## How to enable PDO

To enable PDO, configure --enable-pdo and --with-pdo-sqlite --with-pdo-mysql or whatever database needs supporting by PDO (see the [PHP manual](http://www.php.net/manual/en/pdo.installation.php#94605) for more information).

### Windows users

- **For Apache**, you will need to make sure php_pdo.dll and php_pdo_mysql.dll exist in the php/ext directory, un-comment or add the appropriate lines in php.ini, and restart the web server.

  Under Windows, it may no longer be required to enable PDO when using newer versions of PHP, namely, PHP version 5.3 and later. This refers to php_pdo.dll. However, you still need to activate php_pdo_mysql.dll for MySQL or for whichever database you're using.

- **For IIS**, PDO DLLs are not enabled by default. The preferred method for enabling them is to go to the Control Panel \| Add/Remove Programs, highlight your PHP installation and click "Change" (Change/Remove - XP). Specify "FastCGI", then modify the installed extensions to include these two, then restart your server.

### Macintosh users

#### Method 1

**OS X 10.5**: Detailed, step-by-step instructions are available here:

- [Getting PHP + GD + pdo_mysql working on OS X 10.5 (aka recompiling everything)](http://drewish.com/node/110)
- [Getting PHP + GD + PostgreSQL working on OS X 10.5 (aka recompiling everything)](http://drewish.com/content/2008/12/getting_php_gd_postgresql_working_on_osx_105_aka_recompiling_everything)

**OS X 10.6**: OS 10.6 comes with the PDO extension enabled by default. (For instructions on configuring your development environment, see: [  
Drupal 6 on OS X 10.6](http://drewish.com/content/2009/09/drupal_6_on_snow_leopard)

#### Method 2

[MAMP](http://www.mamp.info/en/index.html) comes pre-configured with the PDO extension. For more information, see: [HowTo: Create a local environment using MAMP](http://drupal.org/node/66187).

### Linux users

PDO is enabled by default as of php 5.1.0 on most linux systems. There is [documentation to enable PDO for a mysql specific-driver](http://www.php.net/manual/en/ref.pdo-mysql.php).

#### Ubuntu

As with most Linux systems, PDO support is present in PHP5 in all recent Ubuntu distributions, and certainly in PHP 5.2 which is required for Drupal 7. If you find that PDO support is not enabled, install the following packages and restart the server.

``` php
sudo apt-get install php5-common php5-mysql
sudo /etc/init.d/apache2 reload
```

Before restarting the server, make sure that `extension=pdo.so` and `extension=pdo_mysql.so` are being loaded, either in the php.ini file or in their own .ini files inside /etc/php5/conf.d.

#### CentOS

If you find that PDO support is not enabled, do the following through SSH

`yum update php-mysql`  
If bash tells you that pdo-mysql is not installed, then  
`yum install php-mysql`

then restart your httpd/apache. When you try run the drupal installation script, you should be able to setup your MySQL database

#### Through WHM

1.  Go to Software \> Easy Apache \> Exhaustive Options List
2.  Select PDO and PDO MYSQL
3.  Save

## Troubleshooting

***Do not* use the PECL PDO installer.** The project is horribly outdated and abandoned. (See <http://pecl.php.net/package/PDO>.) Cases have been reported where PECL PDO support seems enabled but it doesn't work correctly. One symptom was the inability to install Drupal 7.

If you have already installed PECL PDO, you will need to remove it and then reinstall the version from PHP core, or ask your hosting provider to do so.

On Debian and Ubuntu, the required commands are:

``` php
sudo pecl uninstall pdo_mysql
sudo pecl uninstall pdo
sudo apt-get install --reinstall php5-common php5-mysql
sudo /etc/init.d/apache2 reload
```
