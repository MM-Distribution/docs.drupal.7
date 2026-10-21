---
title: "Step 4: setting the hostnames"
source_url: "https://www.drupal.org/docs/7/multisite-drupal/step-4-setting-the-hostnames"
page_type: page
last_updated: "Last updated on 30 August 2016"
published: "2014-03-24T10:54:45+00:00"
modified: "2016-08-30T13:47:16+00:00"
breadcrumb: ["Drupal 7", "Multisite Drupal 7"]
fetched: "2026-10-21T06:14:52Z"
raw: "raw/docs/7/multisite-drupal/step-4-setting-the-hostnames.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Step 4: setting the hostnames

## Bulk loop 1

- In /etc/apache2/sites-enabled/drupal7 (In Mageia 2 and Mandriva Linux 2010, it is /etc/httpd/conf/vhosts.d/00_default_vhosts.conf ), add  

  ``` php
  <VirtualHost *:80>
     DocumentRoot /var/www/drupal7
     ServerName example
  </VirtualHost>
  ```

- In /etc/apache2/conf.d/drupal7.conf (in Mageia 2, it is the file /etc/httpd/conf/webapps.d/drupal.conf ), add the line (not needed in Mandriva Linux 2010)  
  `Alias example 127.0.0.1`

- in the file /etc/hosts , add "example " to this line of aliases:  
  `127.0.0.1 example localhost`  
  In Mageia 2 and Mandriva Linux 2010, you can instead go to "Configure your computer" → "Network and internet" → Others → "Host definitions" (drakhosts), choose the line "127.0.0.1", click on "Modify", add the databases' names in the line "Host Aliases", separated by spaces, then click on the 2 successive "OK" buttons.

**End of bulk loop 2**

Relaunch Apache by  
`sudo service apache2 restart`  
In Mageia 2 go instead to "Configure your computer" → System → "Manage system services by enabling or disabling them" (drakxservices), in the line "httpd-prefork", click the "Start" button (In Mandriva Linux 2010, click on "httpd" and on the "Start Service" button). This will stop and relaunch Apache. Wait for it to say "running.". Click on the "OK" button.

## Bulk loop 2

Go with your web browser on the page <http://example/install.php> and follow carefully the instructions. Specially, don't forget to remove the world write permission of /var/www/drupal7/sites/example.com when asked to do so.

**End of bulk loop 2**  
It should work now. You can close MySQL administrator.
