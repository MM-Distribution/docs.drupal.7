---
title: "Step 3: setting the subdirectories"
source_url: "https://www.drupal.org/docs/7/multisite-drupal/step-3-setting-the-subdirectories"
page_type: page
last_updated: "Last updated on 30 August 2016"
published: "2014-03-24T10:52:06+00:00"
modified: "2016-08-30T13:47:16+00:00"
breadcrumb: ["Drupal 7", "Multisite Drupal 7"]
fetched: "2026-10-21T06:14:37Z"
raw: "raw/docs/7/multisite-drupal/step-3-setting-the-subdirectories.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Step 3: setting the subdirectories

## Bulk loop 2

- Copy directory /var/www/drupal7/sites/default as /var/www/drupal7/sites/example.com  .

- Give read and write permissions to everybody for that directory and for /var/www/drupal7/sites/example.com/files/ .

- If the file /var/www/drupal7/sites/example.com/settings.php doesn't exist yet, copy /var/www/drupal7/sites/example.com/default.settings.php to /var/www/drupal7/sites/example.com/settings.php .

- Search the line beginning by "\$databases" and modify that paragraph like this:  

  ``` php
  $databases['default']['default'] = array(
     'driver' => 'mysql',
     'database' => 'company_example',
     'username' => 'company_example',
     'password' => 'my_password',
     'host' => 'localhost',
     'prefix' => '',
     'collation' => 'utf8_general_ci',
  );
  ```

  replacing the 1st occurrence of "company_example" by the database schema's name, "my_password" by your password, and, if you have created another database user representing Drupal in the schema, replace also "company_example" by its name. If you have installed mysqli, replace "mysql" by "mysqli".

**End of bulk loop 2**  
Copy /var/www/drupal7/sites/example.sites.php to /var/www/drupal7/sites/sites.php .

## Bulk loop 3

- At the end of /var/www/drupal7/sites/sites.php , add the following line:  
  `$sites['example'] = 'example.com';`  
  replacing "example" by the website short name, and "example.com" by the directory name.

**End of bulk loop 3**
