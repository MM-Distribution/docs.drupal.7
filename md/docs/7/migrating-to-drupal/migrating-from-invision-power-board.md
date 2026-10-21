---
title: "Migrating from Invision Power Board"
source_url: "https://www.drupal.org/docs/7/migrating-to-drupal/migrating-from-invision-power-board"
page_type: page
last_updated: "Last updated on 12 August 2016"
published: "2005-08-03T13:43:14+00:00"
modified: "2016-08-12T19:16:19+00:00"
breadcrumb: ["Drupal 7", "Migrating to Drupal 7"]
fetched: "2026-10-21T06:54:02Z"
raw: "raw/docs/7/migrating-to-drupal/migrating-from-invision-power-board.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Migrating from Invision Power Board

This is a 'How To' guide on importing users from an existing Invision Power Board database to your Drupal database. The following steps presume you are doing this through phpMyAdmin, though it may work with other methods.

Currently, the members will have to request new passwords, as the Invision passwords are hashed with a salt (more info [here](http://docs.invisionpower.com/kb/article.php?id=194 "Password Info")). Boris Mann and myself will be working on carrying the correct passwords over too, and I will update this once the work is finished.

## Step One: Export Invision Tables

**Log in to your phpMyAdmin where your Invision database resides.**  
In most cases just visit "example.com/cpanel", click 'MySQL' databases, and then the 'phpMyAdmin' link.

**Export 'ibf_members' and 'ibf_members_converge' tables (one at a time).**  
To export, select your Invision database, then click the name of the table on the left. Up top, click the 'Export' tab, check the 'save as file' checkbox, and click "Go."

## Step Two: Import Invision Tables into Drupal Database

**Select your Invision Database, and Import each table seperately.**  
Once you are in the Drupal database, click the 'SQL' tab up top, click 'Browse', and then click the bottom-most "Go" button. Do this for each Invision table that you previously exported (two total).

## Step Three: Moving the Data You Need To Drupal

**Run SQL statements to import the data.**  
While in your Drupal database, click on the 'SQL' tab once again. Enter the following code, and click "Go" after each one:

**Now you need to update your sequences table so that new users' UID will be higher than the last UID of the new users you just imported. To do this, follow these steps:**  
1)Select your 'users' table by click it in the left sidebar.

2)Click the 'Browse' tab up top.  
3)Click the 'UID' link in your database twice to sort that columb by decending order. Write down the highest number.  
4)Select your 'sequences' table.  
5)Click 'Browse'.  
6)Click the little pencil icon next to 'users_uid' to edit it.  
7)Update the number (bottom right text box in the "ID" row) to the number you wrote down. Click 'Go'.

## Finished

Your users, their email, and joined date have been successfully imported, and your Drupal database has been updated. The users will now have to request a new password. Drupal will ask them for their username and email (the ones they entered in Invision), and it will send them a new password that they can use to login. They can then change that password.

As I stated earlier, we are working on converting the passwords as well so that will not be necessary, and once that is done, this will be updated.

Take care and have fun!
