---
title: "Step 2: Create the database"
source_url: "https://www.drupal.org/docs/7/install/step-2-create-the-database"
page_type: page
last_updated: "Last updated on 29 January 2018"
published: "2008-04-25T05:24:59+00:00"
modified: "2018-01-29T16:07:56+00:00"
breadcrumb: ["Drupal 7", "Installing Drupal 7"]
fetched: "2026-10-21T05:54:13Z"
raw: "raw/docs/7/install/step-2-create-the-database.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Step 2: Create the database

Before running the installation script, you must create an empty database and database user (a user name assigned the rights to use the Drupal database).

This page provides direction for creating your Drupal database using one of the following methods:

- [Web browser-based control panel](#controlpanel) (such as "CPanel" or "Plesk")
- [phpMyAdmin](#phpmyadmin)
- [Creating the database directly](#direct) (advanced users)
  - [Create a database using MySQL/MariaDB commands](#mysql_commands)
  - [Create a database using PostgreSQL commands](#postgresql)

### Selection of characters in MySQL/MariaDB database name

- If you use capital letters in the database name, they will be converted to lower case.
- Allowed characters are a..z, 0..9, and "\_" (underscore).

## Create a database and user via a browser-based control panel

Most web hosting accounts provide a Web-based control panel to help you administer your site. These tools include easy-to-use features for creating a new database, and for creating a "user" with rights to the database. To create a database using a browser-based control panel consult the documentation or ask your web host service provider.

When you create the user for your database, you may see a page where you can specify the privileges that user will have for various operations on the database. In most web control panels' "database wizard", if you simply check "All" privileges for the user you create (and then uncheck "Grant" if it is listed as a privilege) your user will be set up correctly.

Take note of the username, password, database name and hostname (for example, are you installing in `http://example.com`, or in `http://drupal.example.com`, or `http://example.com/blog` etc.) as you create the database. You will enter these items into fields in your browser when running the install script

Note that in many cases when creating databases and users via a web-based interface, the username you use to log into your control panel is added as a prefix to the database name and possibly to the database username as well. For example, if you log into your site's control panel as "webadmin" and create a database named "drupal7db" and a user for that database named "d7user", when running the Install script (see next page) the database and user may need to be typed in as "webadmin_drupal7db" and "webadmin_d7user". (This is because many hosting accounts are on shared servers, and on one server each database and user name must be unique across all accounts on the server.)

If you used the procedure in this section to create your database and user using a web-based interface, continue to the [Step 3: Create the settings.php file page](https://drupal.org/node/540242) of the Installation Guide.

## <span id="phpmyadmin">Create a database and user using phpMyAdmin</span>

The most secure method to use when creating a database with phpMyAdmin is to create a user that has all privileges to the new database, but no privileges to the other databases. This is more secure than using a general username and password for all of your sites on the same server, as it limits access to your databases if someone gets hold of your database logins.

***Note:** This procedure assumes that you have root access to phpMyAdmin, and that you're using phpMyAdmin 3.5.x.*

1.  Sign in to phpMyAdmin as the root user.
2.  Click *Users*, and then click *Add user*.  
    ***Note:** You can use the root user credential as well.*.
3.  In the *User name* field, enter the username that you want to use.
4.  In the *Host* field, select *Local*, which is a more secure setting, unless you'll be accessing the database with this user from another server.
5.  Enter or generate a password for the user.
6.  In the Database for User section, select *Create database with same name and grant all privileges*.
7.  Make sure you select COLLATION `utf8_general_ci` or `utf8_unicode_ci`
8.  Click *Go* to create the user.

phpMyAdmin creates the new database with the same name as the user account. If you want to have a different name for the database and the user:

1.  Click *Databases*, and then click the link for the database that you want to rename.
2.  Click *Operations*.
3.  In the *Rename database to* section, enter the new database name.
4.  Click *Go* in the *Rename database to* section.

If you need more details about using phpMyAdmin, check out [the official wiki](http://wiki.cihar.com/).

Take note of the username, password, database name and hostname (for example, are you installing in `http://example.com`, or in `http://drupal.example.com`, or `http://example.com/blog`) as you create the database. You will enter these items into fields in your browser when running the install script.

In many cases, when creating databases and users using a web interface, the username that you use to sign in to your control panel is added as a prefix to the database name, and possibly to the database username as well. For example, if you sign into your site's control panel as "webadmin" and create a database named "drupal7db" and a user for that database named "d7user", when running the Install script the database and user may need to be typed in as "webadmin_drupal7db" and "webadmin_d7user". (This is because many hosting accounts are on shared servers, and on one server each database and username must be unique across all accounts on the server.)

If you used the procedure in this section to create your database and user using phpMyAdmin, continue to the [Step 3: Create the settings.php file page](https://drupal.org/node/540242) of the Installation Guide.

## Create a database from the command line

If you do not use a Web control panel or are experienced with and prefer to use MySQL, MariaDB or PostgreSQL commands, you can use the information in the following sections.

Additional information about privileges, and instructions to create a database using the command line are available in the INSTALL.mysql.txt file for MySQL/MariaDB and in the INSTALL.pgsql.txt file for PostgreSQL.

### <span id="mysql_commands">Create a database using MySQL/MariaDB commands</span>

***Note:** The database should be created with UTF-8 (Unicode) encoding, for example utf8_general_ci.*

For information on installing and configuring MySQL see <http://dev.mysql.com/doc/refman/5.7/en/index.html>

For information on installing and configuring MariaDB, see <https://mariadb.com/kb/en/>

In the following examples, 'username' is an example MySQL/MariaDB user who will have the CREATE and GRANT privileges and 'databasename' is the name of the new database Use the appropriate names for your system.

1.  Create a new database for your site (change the `username` and `databasename`):

    `mysql -u username -p -e "CREATE DATABASE databasename CHARACTER SET utf8 COLLATE utf8_general_ci";`

    MySQL/MariaDB prompts for the 'username' database password, and creates the initial database files.

2.  Log in and set the access database rights:

    `mysql -u username -p`

    MySQL/MariaDB prompts for the 'username' database password.

3.  At the MySQL/MariaDB prompt, create the user and set the permissions using the following command:

    `CREATE USER username@localhost IDENTIFIED BY 'password';`

    `GRANT SELECT, INSERT, UPDATE, DELETE, CREATE, DROP, INDEX, ALTER, CREATE TEMPORARY TABLES ON databasename.* TO 'username'@'localhost' IDENTIFIED BY 'password'; `

    In this case:

    - databasename is the name of your database
    - 'username' is the username of your MySQL or MariaDB user account
    - 'localhost' is the host where Drupal is installed
    - 'password' is the password required for that username

    Be sure to use backticks ( `` ` `` ) around the database name if you used a MySQL or MariaDB escape character (\_ or %) in your database name.

    For example, because the underscore character is a wildcard, drupal_test_account.\* should be \`drupal\\test\\account\`.\* for security. Otherwise the underscores would match any character and could accidentally give access to other similarly named databases.

    **Note 1:** Unless the database user/host combination for your Drupal installation has all of the privileges listed above (except possibly CREATE TEMPORARY TABLES, which is currently only used by Drupal core automated tests and some contributed modules), you will not be able to install or run Drupal.

    **Note 2:** If you need to restore a dump created with Drush, you will need to add `LOCK TABLES` privilege, unless it won't work.

    For further information on the GRANT statement see <http://dev.mysql.com/doc/refman/5.0/en/grant.html>

4.  If successful, MySQL/MariaDB will reply with:

    `Query OK, 0 rows affected`

5.  Now exit the MYSQL/MariaDB prompt by typing:  
    `exit`  
    The server will answer by saying  
    `Bye`

### <span id="postgresql">Create a database using PostgreSQL</span>

The database must be created with UTF-8 (Unicode) encoding.

1.  **Create a database user**  
    This step is only necessary if you don't already have a user setup (e.g. by your host) or you want to create new user for use with Drupal only. The following command creates a new user named 'username' (you should substitute this with the desired username), and prompts for a password for that user:

    ``` php
    createuser --pwprompt --encrypted --no-adduser --no-createdb username
    ```

    If everything works correctly, you'll see a `CREATE USER` notice.

2.  **Create the database**

    This step is only necessary if you don't already have a database setup (e.g. by your host) or you want to create new database for use with Drupal only. The following command creates a new database named "databasename" (you should substitute this with the desired database name), which is owned by previously created "username":

    `createdb --encoding=UNICODE --owner=username databasename`

    If everything works correctly, you'll see a `CREATE DATABASE` notice.
