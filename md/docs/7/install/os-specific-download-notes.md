---
title: "OS specific download notes"
source_url: "https://www.drupal.org/docs/7/install/os-specific-download-notes"
page_type: page
last_updated: "Last updated on 18 November 2019"
published: "2010-04-22T19:05:08+00:00"
modified: "2019-11-18T11:48:41+00:00"
breadcrumb: ["Drupal 7", "Installing Drupal 7"]
fetched: "2026-10-21T05:55:46Z"
raw: "raw/docs/7/install/os-specific-download-notes.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# OS specific download notes

Follow the links below to download and install Drupal 7 on specific operating systems:

- [OS X](#osx)
- [Windows](#windows)
- [SELinux](#linux)

### OS X download notes

If you are installing on a Mac server, or are creating a test site on your Mac, you may also want review these handbook pages during installation:

- [Installing Drupal 7 on Mac OS X 10.5 (Leopard)](http://drupal.org/node/369107)
- [Installing using CVS repository](http://drupal.org/node/22676) - This page can be helpful especially if you're unsure of the web server's document root or the location of your public HTML directory.

### Windows download notes

***Note:** By default, Windows cannot uncompress files saved in the `.tar.gz` format. This page assumes that you've downloaded and installed the freely available [7-Zip](http://www.7-zip.org) utility to extract `.tar.gz` files. A number of other file compression utilities are also available.*

To download Drupal on your Windows computer:

1.  On the [Drupal project download page](http://drupal.org/project/drupal) find the version that you want to download. In this case, select the first Drupal 7 version under the section 'Official Releases.' Click *Download* and save the file without opening it.

2.  Right-click the `.tar.gz` Drupal installation file, and then select *7-Zip \>\> Extract here*.

    The utility extracts a `.tar` file.

3.  Right-click the `.tar` file, and then select *7-Zip \>\> Extract here*.

    You will now see the final Drupal folder. Drag the folder to where you need it to be in the file hierarchy.

    ***Notes:***

    - *If you extract the files into a folder other than your web site's folder, copy the contents of the Drupal folder into the appropriate web folder, rather than cutting/pasting them. (This will ensure the files will inherit the appropriate permissions for the web server.)*
    - *If you're using Apache instead of IIS, skip the remaining steps on this page.*

4.  In the `sites/default` folder, create a folder called `files` and grant modify permissions for it to IIS_WPG (IIS6) or IIS_IUSRS (IIS7).

5.  Recent versions of Drupal 7 come with a `web.config` file for IIS which contains the same rules as the  `.htaccess` file used on \*nix.

<!-- -->

### SELinux download notes

To install on a Fedora-based distro (RHEL, CentOS, etc.) there are two main options:

- Install from the repository through a `yum install drupal` command. (In Fedora 23, it is `dnf install drupal7`)
- Install it yourself.

The installation instructions will vary a bit depending on your choice, as will the version you wind up with in some cases.

To be compliant with FHS guidelines on architecture independent system components (<http://www.pathname.com/fhs/pub/fhs-2.3.html#THEUSRHIERARCHY>) vs transient data placement (<http://www.pathname.com/fhs/pub/fhs-2.3.html#THEVARHIERARCHY>) and to enforce Fedora-ish system segregation Fedora and its derivatives place the code part of systems like Drupal and WikiMedia in /usr/share and the data elements (like files/ and images/) in /var/www. These parts are bound together through a series of symlinks, as the original development concept behind Drupal and other such systems did not take the FHS into account (there is a pretty big generation/culture gap between core Unix developers and web developers -- and embedding code to this extent inside of what used to be public data files (.html files becoming .php files and totally bypassing cgi-bin) was never thought of when the FHS was originally conceived). This can be confusing for newcomers.

In either case, the placement of the Drupal code (all those `.php` files) in the filesystem is irrelevant to the function of SELinux. Apache's daemon, httpd, has a context group within the Fedora SELinux policy structure. Any files or directories that Apache needs to interact with must be placed in an httpd\_\* type context. Yum will handle this for you if you do a `yum install drupal` install and the stickiness of the /var/www filesystem hierarchy will do it for you if you unpack it directly into a sub-directory there. However, installation cases outside of this where SELinux is set to enforce but the default SELinux policies are either grossly underdeveloped (Ubuntu, for example) or nonexistant (Slackware / LFS + SELinux -- yes, some people do this) will have to make the change on their own:

``` php
chcon -R -t httpd_sys_content_t /path/to/drupal/files 
```

The other area where SELinux can trip one up is basic policy permissions for allowing Apache to do things like send email (to prevent compromised systems from becoming proxy spam-generators -- a problem far more common than most Ubuntu new administrators seem to be aware), make calls across network sockets to database servers (a wonderful way to bypass password protections and steal user data from a site), or directly alter files on behalf of scripts (an entry to the first two). To enable this small list of abilities but keep your system otherwise locked down with an SELinux policy set to "enforce" run the following three commands:

``` php
# setsebool -P httpd_can_network_connect_db=1 # setsebool -P httpd_can_sendmail=1 # setsebool -P httpd_unified=1
```

Unfortunately, in an excited rush to get things up quickly most people who opt for the increased security that SELinux provides by choosing a Fedora-based distro usually toss all their gains at the first sign of SELinux conflicts by turning SELinux off instead of digging further (because learning 4 more file security attributes is hard -- and admittedly, SELinux is rarely explained so simply in currently available resources).

Outside of granting Apache permission to do things Drupal needs to work correctly (those three setsebool commands) and then telling SELinux where these permissions should apply (the chcon command above), the installation process is no different from any other system. It is useful to remember if you run into an FHS-compliant installation where /var/www/html/drupalxx is largely empty but for a few symlinks and data folders (like config/) that all of the code is over in /usr/share and conceptually nothing has really changed.

Also, if you use LDAP, you may be interested:  
`# setsebool httpd_can_connect_ldap on`

tl;dr reference on rpm-based Systems: <http://zxq9.com/archives/442>
