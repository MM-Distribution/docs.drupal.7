---
title: "Migrating a site"
source_url: "https://www.drupal.org/docs/7/backing-up-and-migrating-a-site/migrating-a-site"
page_type: page
last_updated: "Last updated on 28 September 2018"
published: "2010-04-20T21:21:00+00:00"
modified: "2018-09-28T14:26:53+00:00"
breadcrumb: ["Drupal 7", "Backing up and migrating a Drupal 7 site"]
fetched: "2026-10-21T06:57:54Z"
raw: "raw/docs/7/backing-up-and-migrating-a-site/migrating-a-site.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Migrating a site

You need to migrate your Drupal site if you change hosts, or if you maintain separate development and live sites. This is an outline of the process – perhaps only a check list – but it includes some steps that are not well described elsewhere. You need to adjust these steps depending on the modules you use and your server environments.

This procedure covers single sites. Multi-site migration (on [Windows/Apache](http://drupal.org/node/547860) and on [Linux](http://drupal.org/node/290768) ) is covered elsewhere.

### Before You Start

**Document** any differences in your PHP installation on the two servers - Bugs, features, modules, configurations, versions.  
… and for MySQL  
… and for Apache  
or your alternatives, of course.

Get a decent tool set and understand how to use it to upload and download files, manage compressed files, change permissions and ownerships, work with MySQL etc. On both machines. There are Drupal tools that cover some of these steps, for instance backing up and restoring the data, but they do not cover everything. Clearly you should use a tool if it helps in your case,or do it the hard way otherwise! The [Backup & Migrate module](/project/backup_migrate) is usually a good choice for easily creating file and database archives.

[Checklist for migrating to a new site](http://drupal.org/node/333675) - you must ensure that the target site supports all the features (mod_rewrite, AllowOverride) that Drupal requires. If you move from a good host to a less-good host and things stop working, it might not be that your migration failed, but just that the destination wasn't set up right.

### On the old site

1.  Consider **updating** Drupal core and modules before the migration
2.  **Document** the modules used, their versions and paths etc. For Drupal 6, the contributed module [Site Documentation](/project/sitedoc "Site Documentation Project") can ease this task.
3.  Document the temporary directory folder to be used in admin/settings/file-system and either prepare to edit this after restoring the database or make sure the same path exists on both sites.
4.  Set site in maintenance mode: in Administer → Site maintenance, choose "**Off line**".
5.  **Turn off clean URLs** (Administer → "Clean URLs") Remember that, from now on, you'll enter the administrator part through `www.example.com/?q=user` ("user" should *not* be replaced by any user name.)
6.  Clear data from the **cache tables**. These are unnecessary for transfer and cause confusion when tidying up the data. The devel module and admin menu module contain links to do this easily, otherwise visit `www.example.com/admin/settings/performance` and click the "Clear cached data" button at the bottom of the page.
7.  **Export your database**. You can use MySQL Administrator, phpMyAdmin or MySQL command line tool mysqldump for exporting, which produces a text file with a .sql extension. You don't need to download explicitly because the file will be created on the computer your interface (MySQL Administrator, or your browser if you use phpMyAdmin) is running.
    - In MySQL Administrator, first connect giving your password, then choose "Backup" on the left, choose the database you want to save from the "Databases" list, click on the big arrow. This will move the database name into the "Backup content" rectangle on the right. Then click on the "Start backup" button in the right bottom corner. Choose the folder you want to save it in, playing with the path bar on the top and the "Folders" list on the left. Then click the "OK" button.
8.  If your old site is public (on the web), consider setting your site on line: Administer → Site maintenance, choose "**On line**". Of course, all the modifications made on the old server from now on (readers' comments, forums posts, etc.) will be lost. Therefore, if you set back your old website on line and if it's public (on the web), consider blocking new comments to avoid users frustrations: Administer → Permissions.
9.  Copy the whole **Drupal** code – core, modules, themes, and download them if necessary or, better, transfer them directly to the new server. You could choose to use new copies instead of the new site.
10. Copy the **files** directory and any similar directories (such as image galleries) and download them if necessary, or, better, transfer them directly to the new server.

### In between

These steps can be performed on your own computer, which can be different from both the old and the new servers. Nevertheless, if you can perform these tasks easily either on the old or on the new server, you don't need to have the files pass in transit through a third computer.

The data in the database may contain some hard coded links which will not necessarily work on the new site ( it depends on what you are doing ). You can use SQL queries on the reconstructed database to change these, or you can edit at this intermediate stage with a text editor - the .sql file is human readable text. Using a text search has the benefit that you may find unexpected areas to change in the fields and tables you were not aware of. It can be slow. Consider:

1.  The files list (field "filepath" in table "files")
2.  The site URL itself - many of the node links and references refer to the full site URL. There are also references in many log files. It is not always appropriate to change to the new site name, so you need to think about this for each table
3.  Variations on the above. For instance the messaging module stores the site URL for each message in the messaging store. I believe the imagefield module has a list like the filelist.
4.  What facilities you have to create new databases (see Import Your SQL data, below)
5.  The database name. Your hosting company may require that all your database names begin with "yourName\_". Moreover, they may limit the numbers of characters.
6.  This command can strip data out of a database dump,which generally shouldn’t be migrated when moving a Drupal database from one site to another.  
    `` sed -E -e "/^INSERT INTO \`(cache|watchdog|sessions)/d" < /path/to/dump.sql > /path/to/dump-stripped.sql ``  
    You will need to tweak the regular expression a bit if your database uses a table prefix.

If you are moving a live site from one host or server to another you will need to adjust your DNS settings to point to the new server.

### On the new site

Now you need to reverse the process on the new site.

1.  Upload or copy the whole **Drupal** code – core, modules, themes – to the new site. Or reconstruct from fresh copies if you prefer. Some people install a new Drupal core first to test the server environment
2.  Upload or copy the **files directory** and any similar directories (such as image galleries) to the location you chose when editing the .sql file
3.  Create the empty database Drupal will use. Your hosting company may require that all your database user begin with "yourName\_". In some configuration, the database manager provided in CPanel has (stupidly) enable to manage databases created directly with phpMyAdmin, so you won't be able to give any user the right to use it. If you're sure you are not concerned with this problem, you can of course create and fill the database at the same time (See below).
4.  Upload and import your **SQL data**. If you cannot create databases yourself, you may have to use some other tool on your host's control panel or get someone to do this for you. If this is the case, remove any “create database” lines from the .sql file (but a "create database if not exists" line doesn't matter). You will probably find that the database is too big to upload using phpMyAdmin. Some hosting providers give access to MySQL Administrator, which accepts big files. If you have an SSH access, a 3rd solution is to use MySQL from a text console: "mysql --user=user_name --password=your_password database_name" and inside the “source” command: "source database_backup.sql".
5.  Create the database user Drupal will use. Your hosting company may require that all your database users begin with "yourName\_". Moreover, they may limit the numbers of characters. Grant this user the SELECT, INSERT, UPDATE, DELETE, CREATE, DROP, INDEX, ALTER, CREATE_TMP_TABLE and LOCK_TABLES privileges for the said database.
6.  Make changes to the “Database settings” section of the **settings.php** file, to ensure that they are pointing to the new database, with the right user (which may be different that the one you used on the old computer) and the right password. You may also have to adjust the “base URL” if you are moving between a sub-domain and a domain level. If you are moving the site to a new domain, or to localhost, also check that "\$cookie_domain" is not set to your old domain.
7.  Some people will need to make changes to the rewrite rules and**.** **htaccess** files
8.  Attempt to **log on** to the new site. You will probably find that you are locked out by a combination of site maintenance mode and the non-clean URLs. In that case navigate to newsite/?q=user to login, then turn on clean URLs. (Should the Clean URL test fail at this stage, try to go online first - step 14 - and then run the Clean URL test again).
9.  You will need to make adjustments to the **site information** (Administer → Site configuration → Site information), which contains an email address, and change the **files** directory (`www.example.com/admin/settings/file-system`) to the location where the files now reside. Also change the temp folder to the correct location on the new server, if it is different.
10. Adjust **modules** as necessary for different versions. For example, I had an unintended upgrade from PHP 5.2.8 to 5.3.0 and some modules stopped working. This produced large swathes of error messages at odd points. I searched for all the error messages online to see whether each was known, which helped solve most problems. I had to make the following changes:
    - Set date.timezone = UTC in the php.ini file (and note that there may be two of these files, one for command line use and one for Apache use – you need the Apache one)
    - Apply patch 6.x-2.x-549884-30.patch to the date module
    - Use 6.x-3.x-dev instead of 6.x-3.0-alpha3 for the admin_menu module
    - Delete the coder module, which would not work with Drush (but I am not sure that this was part of the same problem)
11. Check the **status report**: Administer → Reports → Status report. And run Cron manually by clicking if suggested by Drupal.
12. Your new site will now look and function virtually identically to the old one – you might consider changing the **theme** or theme color on one of them as a strong visual reminder of which is which
13. Adjust the **performance** parameters according to your needs: Administer → Site configuration → Performance.
14. After checking everything you can turn off site-maintenance mode: in Administer → Site configuration → Site maintenance, choose "**On line**".
15. Set up the **cron** job, as explained [there](http://drupal.org/cron " configure cron jobs"). Note that this cron can run on any computer online, including your personal computer, not necessarily the server where your Drupal is running. Just check the chosen computer is usually turned on and online at the time(s) you programmed the cron job. If your hosting provider doesn't allow you to use cron and you don't have any computer to do the job, use [Poormanscron](http://drupal.org/project/poormanscron " Poormanscron") module or [EasyCron](https://drupal.org/project/EasyCron " WebCron") module.
16. If your new Drupal site is intended to be public, i.e. To be on the world wide web, it's now time to set the **DNS** (domain name server) to the IP (internet protocol number) of your new server. For this, contact your domain name registrar. If your new hosting provider manages it for you, contact them instead. If your Drupal site was already on the web and you're migrating from a public server to another one, then you may want or have to change registrar too. In this case, first read carefully the contract with the new registrar. Then it's recommended to update the DNS in the old registrar's database (so that it points towards the new server) *before* changing registrar. Depending on the TLD (top level domain), it's probable you'll then need a code called "EPP code", "authorization code", or "Auth code". Ask it to your old registrar, or to your old hosting service if the latter used to manage the DNS for you. Then give this code to the new registrar (possibly via the new hosting provider) and wait, usually 5 d (five days). If you're sure you can do it within the transfer delay, you can launch the registrar changing process before all the other steps, but if it happens the transfer is done before you've finished, your website will be unavailable to the public during that time.

### Troubleshooting

#### In case you cannot export your database

In case you cannot export your database (for instance, your hard disk crashed and you cannot boot on it any longer), the you can copy the databases directory (in Mageia 4, it is /var/lib/mysql/mysql ) and the configuration file (in Mageia 4, it is /etc/my.cnf) and copy them at the right place on the new computer, with the same ownership and rights: the Linux/Unix user of Apache (In Mageia 4, it is called mysql.) should have read and write access to the databases, and read access to the configuration file. For Mageia, see [MariaDB](https://wiki.mageia.org/en/MariaDB "Mageia wiki").

#### Blank page

If you get a blank page, it may be that you didn't copy the theme needed by the site at the right place. In case of a sub-theme, you need both the main theme and the sub-theme.  
You can see [Blank pages or "white screen of death" (WSOD)](https://drupal.org/node/158043 "Drupal.org") and the next page.

#### No user login

If you cannot log in, try <http://example.com/?q=user/login> . Then go to <http://example.com/?q=admin/config/search/clean-urls> , check the "Enable clean URLs" box and click on the "Save configuration" button. But if you get a message saying that clean URLs cannot be enabled, it may be that you didn't copy the .htaccess file at the root of your Drupal installation (at the same time, check if .gitignore file is there too). If you have full control on Apache, you should check if Apache module called mod_rewrite is loaded (for this, go with your browser to a php file containing just the line`<?` `php phpinfo(); ?>`) and if Apache configuration file contains the directive  
`RewriteEngine on`.  
In Mageia 4, it is in /etc/httpd/conf/sites.d/drupal.conf .

#### Error messages

If you get error messages, read them carefully. If you are sure all the needed modules are at the right place and are not older than the ones of the first installation, going with your browser to <http://example.com/update.php> may help. If you couldn't log in as administrator, then you will be denied the right to **update the modules**. In this case, in sites/example.com/settings.php , look for the line  
`$update_free_access = FALSE;`,  
replace "FALSE" by "TRUE" and you will be able to update the modules without being the site administrator: go to <http://example.com/update.php> again. Since letting anybody run update.php is dangerous, don't forget to restore the  
`$update_free_access = FALSE;`  
line once the problem is solved.
