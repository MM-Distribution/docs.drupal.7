---
title: "Step 1: Download and extract Drupal"
source_url: "https://www.drupal.org/docs/7/install/step-1-download-and-extract-drupal"
page_type: page
last_updated: "Last updated on 14 June 2020"
published: "2008-04-25T05:11:23+00:00"
modified: "2020-06-14T11:00:14+00:00"
breadcrumb: ["Drupal 7", "Installing Drupal 7"]
fetched: "2026-10-21T05:53:57Z"
raw: "raw/docs/7/install/step-1-download-and-extract-drupal.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Step 1: Download and extract Drupal

You can download and extract Drupal in five different ways:

- [using Drush](#drush)
- [from the command line](#download-extract)
- [using FTP](#ftp)
- [using Git](#git)
- [using composer](https://www.drupal.org/node/2718229)

To *install* a Drupal site in a language other than English, check if your language is supported at [localize.drupal.org](https://localize.drupal.org/translate/projects/drupal).  
You can also add additional languages after the installation.

So, follow one of the methods below for downloading, and then...

### Before continuing to the next page ...

The base URL for your Drupal installation is set in your web server's configuration file. You need to know this URL before proceeding to the next steps of the installation.  
If you are installing Drupal on your local machine, the base URL may be `http://localhost`.  
If you're installing Drupal to a web server, your base URL may be a specific domain name, such as `http://example.com`.

## Drush

[Drush](/project/drush) is a command line tool to maintain and administer Drupal sites. It offers the most convenient way of downloading Drupal by using a single command: `pm-download` (or its alias `dl`):

`drush dl drupal-7`

This command will download the recommended version into the current folder. Check `drush help dl` to see additional options such as how to download a specific version.

To download the development version of Drupal 7:

`drush dl drupal-7.x`

## From the command line

### Downloading

Log into your server on using *ssh* and navigate to the directory from which you will be serving your Drupal site.  
On many \*nix computers the path from the server's root will be /var/www/html, so `cd /var/www/html`. On a shared server, or a server that hosts multiple domains, the path will be different (try `cd ~/www` or `cd ~/public_html`). If you are unsure of the directory, ask your hosting provider for assistance.

Download Drupal from the command line, for example using *wget* or *curl*.  
The commands are, respectively:

``` php
wget https://ftp.drupal.org/files/projects/drupal-7.x.tar.gz
```

or

``` php
curl -O https://ftp.drupal.org/files/projects/drupal-7.x.tar.gz
```

***Note:** The curl command option is the upper case letter "O" and not the numeral that stands for zero.*

Replace `https://ftp.drupal.org/files/projects/drupal-7.x.tar.gz` with the link for the version you want to install.  
The links to the recommended versions are available on [Drupal Core](/project/drupal) project page, where you can copy them from the *Download* column.  
All other versions are available on the [Releases for Drupal core](/node/3060/release) page.

### Extracting files

Type the following command and replace "7.x" with your downloaded version's number:

`tar -xvzf drupal-7.x.tar.gz`

Then remove the compressed version of the file by using the following command:

`rm drupal-7.x.tar.gz`

### Moving to its intended location

Now you need to move the contents of the *drupal-7.x* directory one level "up" into the web server's document root or your public HTML directory:

`mv drupal-7.x/* drupal-7.x/.htaccess ./`

For Drupal 7, also add:  
`mv drupal-7.x/.gitignore ./`

Alternative, you can extract the the tar archive directly into the correct directory by typing:  
`tar --strip-components=1 -xvzf drupal-7.x.tar.gz`

The files from the directory you downloaded and decompressed have now been moved up a level into your web directory, and you can delete the (now empty) drupal-7.x directory:

`rmdir drupal-7.x`

## Using FTP

You can download Drupal using your favorite FTP-tool.

1.  Download a Drupal tar.gz or zip file to your local computer from <https://www.drupal.org/project/drupal> by clicking on the link for the version you want to install.
2.  When you download the file, your browser will ask you what to do with it. Choose "Extract" and extract it to your local computer. Or, save the file and extract it using your computer's software (7-zip for example) that deals with archive files. The exact steps to do this differ by software, but you should end up with a folder/directory called something like "drupal-7.32" on your local computer.
3.  Use FTP to transfer the entire contents of this folder, including hidden files like .htaccess, to your hosting account's HTML document root. Details of how to do this depend on your FTP software.

## Using Git

The Drupal project page has great [version control instructions](https://www.drupal.org/project/drupal/git-instructions), which starts with setting up repository for the first time by cloning Drupal.

If you do not have composer installed follow their [documentation](https://getcomposer.org/doc/00-intro.md).
