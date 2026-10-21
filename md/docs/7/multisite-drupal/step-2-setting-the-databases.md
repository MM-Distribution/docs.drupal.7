---
title: "Step 2: setting the databases"
source_url: "https://www.drupal.org/docs/7/multisite-drupal/step-2-setting-the-databases"
page_type: page
last_updated: "Last updated on 30 August 2016"
published: "2014-03-24T10:49:51+00:00"
modified: "2016-08-30T13:47:16+00:00"
breadcrumb: ["Drupal 7", "Multisite Drupal 7"]
fetched: "2026-10-21T06:14:21Z"
raw: "raw/docs/7/multisite-drupal/step-2-setting-the-databases.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Step 2: setting the databases

MySQL administrator calls "schema" what Drupal and PhpMyAdmin call "database".

## Bulk loop 1

- Create an empty database schema with MySQL administrator. In Ubuntu 10 and 11, you'll find MySQL administrator in Applications→Programming. (In Mandriva 2010: "Applications launcher menu" → Development → Databases). Give this schema a name related to your website name. It cannot contain spaces, slashes, nor dots. Be aware that some share hosting services require that all your schemas names and database usernames begin by a fix part (for instance derived from your main site name) followed by an underscore. If you don't want to change your schema's name or username when putting your Drupal site alive, check your hosting service rules now. As said, we will call the schema "company_example". To create it, click on “Catalogs” and right-click in the left bottom part of the window called schemata, then choose “Create schema”.
- We will use for the schema "company_example" the user name already used for the schema "drupal7" of the Drupal website. If you've forgot it, look in /var/www/drupal7/sites/default/settings.php for a line like  
  ` 'username' => 'company_drupal',`  
  Let's suppose the main username of Drupal in MySQL is "company_drupal". If the website you're created in for a human client, it's more secure providing its database a different MySQL user, so that he won't be able to modify the other websites databases. In this case, we suggest 2 users have write access to the database: the general user "company_drupal", so that you can do modifications on the websites without changing user between the websites, and the MySQL user specific to that website, let's say "company_example". (So "company_example" is both the name of the schema and of its user.) To add a new user, in MySQL aministrator, click on "User administration"→"New user", and name it "company_example", then in the left bottom part of the window called "User accounts", right-click on the user name, choose "Add host" and add the host "localhost". Give this user a password (don't forget it).
- So let's suppose the user representing Drupal for the schema "company_example" is company_example. Grant company_example@localhost the SELECT, INSERT, UPDATE, DELETE, CREATE, DROP, INDEX, ALTER, CREATE_TMP_TABLE and LOCK_TABLES privileges to this new schema. To do so, in MySQL administrator:User administration, in the bottom left part of the window called "User accounts", click on company_example, then on "@localhost", then in the right part of the window, on tab "Schema privileges", in the "Schema part", click on "company_example", in the "Available privileges" part, choose the above mentioned privileges and move them to the "Assigned privileges" thanks to the left arrow in between. Then click on "Apply changes". The same way, grant the same privileges to your general MySQL user "company_drupal".

**End of bulk loop 1**
