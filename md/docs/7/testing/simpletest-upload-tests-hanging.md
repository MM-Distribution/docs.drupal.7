---
title: "SimpleTest upload tests hanging"
source_url: "https://www.drupal.org/docs/7/testing/simpletest-upload-tests-hanging"
page_type: page
last_updated: "Last updated on 10 January 2017"
published: "2009-06-25T03:36:28+00:00"
modified: "2017-01-10T21:28:15+00:00"
breadcrumb: ["Drupal 7", "Automated testing for Drupal 7"]
fetched: "2026-10-21T08:10:50Z"
raw: "raw/docs/7/testing/simpletest-upload-tests-hanging.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# SimpleTest upload tests hanging

#### The Symptom

SimpleTests involving file uploading of any kind result in the test never finishing on Mac OS X covering Leopard and possibly other versions as well.

**The Problem**

It appears that the stock cURL that comes with Mac OS X is broken. As of the 10.5.7 release, this appears to be cURL 7.16.3.

#### Solutions

One option is to compile cURL and PHP from source in place. However, it's easier and more manageable to install your development environment using MacPorts. You can run both environments side by side on different ports, setup to run at different times, or to completely supersede the stock Apache+PHP setup.

If you already have MacPorts installed and current, this process will take 20-30 minutes. If this is your first MacPorts install, the process may require an hour depending on the speed of your computer.

First, [install MacPorts](http://www.macports.org/install.php).

\*[More verbose instruction set \[off-site\]](http://2tbsp.com/content/install_apache_2_and_php_5_macports)

Update cURL with SSL support:  
`sudo port install curl +ssl`

Install Apache 2:  
`sudo port install apache2`

Install PHP 5:  
`sudo port install php5 +apache2 +mysql5 +pear`

Configure Apache

``` php
sudo cp /opt/local/etc/php5/php.ini-dist /opt/local/etc/php5/php.ini
sudo cp /opt/local/apache2/conf/httpd.conf.sample /opt/local/apache2/conf/httpd.conf
```

Activate the PHP 5 Module

``` php
cd /opt/local/apache2/modules
sudo /opt/local/apache2/bin/apxs -a -e -n "php5" libphp5.so
```

You will need to add the following within the `<IfModule mime_module>` block in httpd.conf:

``` php
AddType application/x-httpd-php .php
AddType application/x-httpd-php-source .phps
```

You will probably also want to add index.php to the line in the `<IfModule dir_module` block.

Finish configuring Apache as seen fit.

**Starting & Stopping Apache**  
Apache will be managed by [launchd](http://launchd.macosforge.org/). Start apache with:  
`sudo launchctl load -w /Library/LaunchDaemons/org.macports.apache2.plist`  
This will also have Apache automatically start if the machine is rebooted.

Stop apache with:  
`sudo launchctl unload -w /Library/LaunchDaemons/org.macports.apache2.plist`  
This will also stop Apache from automatically starting.
