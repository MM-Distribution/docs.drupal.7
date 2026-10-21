---
title: "Setting up the files directory"
source_url: "https://www.drupal.org/docs/7/install/setting-up-the-files-directory"
page_type: page
last_updated: "Last updated on 7 May 2020"
published: "2009-03-07T22:15:54+00:00"
modified: "2020-05-07T13:17:43+00:00"
breadcrumb: ["Drupal 7", "Installing Drupal 7"]
fetched: "2026-10-21T05:54:59Z"
raw: "raw/docs/7/install/setting-up-the-files-directory.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Setting up the files directory

**In most cases, Drupal will create the files directory for you. If Drupal can't create the directory (which most probably is due to lack of required permissions), follow the instructions below.**

After installing Drupal, you will need to make sure the directory files can be accessed by your Web server. If it does not have the correct permissions, you may get an error message stating that "sites/default/files does not exist ..."

Here’s how:

1.  In the folder `sites/default` create a new directory called `files`.
2.  Grant read, write and execute permissions on the new directory to the Web server.

Most FTP programs will allow you to create the new directory and set its permissions.

Once you've completed these steps confirm the appropriate permissions have been assigned by navigating to Administer -\> Reports -\> Status report. Scroll to the section labelled, "File system" and confirm your settings are now correct.

### Troubleshooting Apache-based Web Servers

If the directory files is not "owned" by the Web server there are two ways to proceed. These instructions assume you have shell access to the Web server. If you do not have shell access, please contact your hosting provider for additional support.

Ideally you will be able to change the "owner" of the directory files to match the name of the Web server. On a Unix or Linux-based server you may verify "who" the Web server is running as by issuing the following commands.

For Apache 2.x:

``` php
$ ps aux |grep apache
```

For Apache 1.x:

``` php
$ ps aux |grep httpd 
```

Depending on your Web server one of these commands will return a series of lines like this:

``` php
www-data 13612 0.1 0.9 50640 20340 ? S 12:29 0:08 /usr/sbin/apache2 -k start 
```

The first column in the returned text is the "user" that your Web server is operating as. In this case the user is www-data. To make your files directory writeable by the Web server you need to reassign its ownership using the following command:

``` php
$ chown -R www-data sites/default/files
```

If you do not have sufficient permissions on your server to change the ownership of the folder, the next best option is to provide group-write access to the folder with the following command:

``` php
$ chmod -R 0770 sites/default/files 
```

You should also be able to adjust the directory's permissions using an FTP program as outlined above.

Once you've completed these steps confirm the appropriate permissions have been assigned by navigating to Administer -\> Reports -\> Status report. Scroll to the section labelled, "File system" and confirm your settings are now correct.

### Warning

The most dangerous and least secure option is to assign write access to "everyone." This option should be avoided at all costs. If the steps outlined above do not work, please consider adjusting your hosting configuration (e.g. add your Web server to the appropriate group) instead of granting write access to "everyone."

### SELinux enabled environment

If you have SELinux enabled (Fedora, RHEL, CentOS, Scientific Linux), you have to allow write by SELinux too, as even you set the correct permissions, the write does not proceed because SELinux. Run these commands as root:

``` php
chcon -Rt public_content_rw_t sites/default/files 
setsebool -P allow_httpd_anon_write=1 
```

### Unix and FileZilla file permissions

We programmers assume you users know all about this. If you don't, here's the upshot.

Every **user** (human, etc) has an account on the computer. If it's a different computer, your account on it might be very different. In fact some programs like MySQL and Drupal have their own unattached user/permissions system where your username and password can be completely different. This section is about your Unix computer account, which you used to connect and mess around with your files on your Unix server.

The computer also has **groups** of users, like maybe the other people in your department or your classroom or platoon or rank. This way, they can give, or take away, permissions to a whole group of people at once.

Now there's three users that are important: you, the web server, and everybody else. Usually the web server's account name is www or \_www or nobody or daemon or apache. Everything that Drupal and PHP do, they do as this user. Usually no actual person logs in as www, it's reserved for the server, and magic makes the server assume the www user identity. Even if Atilla the Hun comes surfing to your web server, what he does, he does as www as far as the files are concerned.

So you have to make sure that each of you can do what you need to do:

- **you** should probably be able to read and write the files in the website you're making
- **www** (drupal) needs to be able to read all the files, and needs to be able to write inside the **files** directory.
- **everybody else** probably should not be allowed any access at all.

Each file, and each directory (folder), has permissions on it telling who can mess with it, and how:

`r` means **Read** permission, you can see what's inside. For a directory, it means you can see what files are inside. You might not have permission to do anything with those files, but at least you can see their names, and see what permissions you have with them.

`w` means **Write** permission, you can change the data in it. For a directory, it means you can add and remove and rename files in it. If you can't delete a file, it's not cuz because you can't write the file, it's cuz because you can't write its directory.

`x` means **Execute** permission. For a directory, that means you can use it to get at files inside. Even if you don't have read permission! If you know the name of the file, and you have x permission, you can use that file or directory (and directories beneath, if any).

Each file remembers three kinds of people who can mess with it:

- the **User** is one particular user, usually whoever created it, the 'owner'.
- the **Group** is some group, oh, you can often change this if you're the User. (If you are both the User and the Group, you only get the User permissions.)
- the **Other** is the rest of all the users, excluding the User and the Group.

This isn't always convenient; sometimes you want only three different users to access it, or two groups, or whatever, but this is the way it's worked since before 1980. Usually, you can figure out a way to make it work for you and the server.

OK so if you see permissions like this:

``` php
rwx rwx rwx nancy staff
```

that means that the **User** named **Nancy** can **read & write & execute** it, and so can the **Group** named **Staff**, and so can **everybody** else.

This however:

``` php
rwx --- --- nancy staff
```

means that **Nancy** can do **everything**, but nobody else can. Very private. And this:

``` php
rw- r-- --- nancy staff
```

means that Nancy can read and write, the staff can just read and everybody else is locked out. Programmers often abbreviate this into 3 digits where:

``` php
r = 4
w = 2
x = 1
```

and you add them to get a single digit, so `rw- r-- ---` turns into: **640**. Compact but confusing if you're not used to it. You'll see these commonly:

``` php
rw = 6 (common on files you can change)
rx = 5 (common on directories you can't change)
rwx = 7 (common on directories you can do anything with)
```

So probably you'll need some situation where you and the server can get at what you have to get at, and everybody else is locked out. Remember that you can lock people out by simply removing x permission from a directory at the top - you don't have to change every file.
