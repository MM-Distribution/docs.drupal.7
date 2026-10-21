---
title: "Adding File Encryption to existing Drupal 7 site"
source_url: "https://www.drupal.org/docs/7/howtos/adding-file-encryption-to-existing-drupal-7-site"
page_type: page
last_updated: "Last updated on 21 December 2016"
published: "2014-10-29T21:28:42+00:00"
modified: "2016-12-21T06:26:11+00:00"
breadcrumb: ["Drupal 7", "Site building and development HowTos for Drupal 7"]
fetched: "2026-10-21T07:59:44Z"
raw: "raw/docs/7/howtos/adding-file-encryption-to-existing-drupal-7-site.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Adding File Encryption to existing Drupal 7 site

## Background

A site has been set-up a while ago - pre-Snowden - and there is a sense of improving security in general.  
The site is used for company communication and to share information and files across management.  
A number of files have been stored already un-encrypted. All uploaded files will have to be re-loaded and the file field in the Content Type will have to be revised.

### 1. Reading up

- Secure files using Encrypted Files - <https://www.drupal.org/node/1957124>
- Encrypting and decrypting content in Drupal - <https://groups.drupal.org/node/258513> - "There are at least two modules to do encryption in Drupal. This page compares those modules to help people choose a good one."

### 2. Install modules

1.  Encrypted Files - <http://drupal.org/project/encrypted_files> - be aware this is a 7.x-2.0-beta1 version from 2015-Aug-21 (Aug. 2015) - 2,308 sites currently report using this module. - All issues 19 open, 26 total
2.  AES Encryption - <http://drupal.org/project/aes> - (Oct. 2014) 7.x-1.8 2014-Mar-28 - 4,170 sites currently report using this module. - All issues 18 open, 95 total

***Just a warning:*** If you need to read up on how to install modules <http://drupal.org/documentation/install/modules-themes/modules-7>, you may not be experienced enough to do this project on a live site. If you use this on a sandbox site to practice - go ahead.  
Keep permissions down to User-1 or at least to well trusted admin staff.

### 3. Configuration

**AES settings - ...../admin/config/system/aes**

1.  Create AES passwords - if you activate this, all users will be able to see their passwords in their user account. However, this also means that all admin users with the permission to access user accounts can see their password. Drupal is set up for the passwords to be stored in a format that would require database access and then some effort to retrieve and decrypt users passwords. It is not impossible, but in most cases with multiple admin users allowed to access user accounts they would not necessarily have access to the database. In short - activating this option will make it much easier to retrieve users password by user-1 and all other admin users with permission to access user accounts. On balance I would not activate this option.
2.  AES implementation: Mcrypt extension - provided you have it activated
3.  Method for viewing passwords:
4.  Cipher: Rijndeal 128/192/256 (higher is better))
5.  Key storage method: Database or File - Database for this example - File option see above for explanation
6.  Path to keyfile: left blank for this test
7.  Key: left blank for this test
8.  Confirm key: left blank for this test

Encrypted Files - settings via AES above - adds a file field option in the file field to allow the choice of adding a password to each file or to store the encrypted file in a directory ".../public_html/sites/default/files/private/encrypted-files".  
Note that the directory path requires private files to be activated "...../private/encrypted-files" - for more details - <https://www.drupal.org/documentation/modules/file>.

### 4. Creating a Content Type

**..../admin/structure/types/add** -  
choose a name (***encry_test*** for this example) and add all settings as required - from ***Automatic title generation*** to ***Menu settings*** and possibly more settings like multi-lingual and notification if enabled, etc.  
**Save**  
then add a ***File Field*** - ......./admin/structure/types/manage/encry_test/fields

1.  Add new field: "encry_test" (Name of the Field)
2.  \- select a field type - : "File"
3.  Media file selector: Password Protected File
4.  A password-protected file uses a user selected password. If the uploaded and password-protected file has to be shared, the uploading user would have to transfer her/his password to the sharing user. This option seems more sensible for cloud-type storing of own files. The files can be stored.
5.  Media file selector: File - to be used here
6.  Press - Save

Next page - ***Field settings***

1.  Enable Display field - ticked to be used here
2.  Files displayed by default - ticked to be used here
3.  Upload destination - default is Public files
    - o Encrypted Files
    - o Public files
    - o Private files
4.  Tick Encrypted Files. This means the uploaded files are stored in an encrypted format. If, for example, someone managed to hack your FTP access and would get to ".../public_html/sites/default/files/private/encrypted-files" s/he could download the file but it would be in an encrypted format and thus useless. S/he would now require the key either stored in your database with (hopefully) different credentials than your FTP access - or access to your file where the key is stored - that should be in a remote location (outside the root of this site) for obvious reasons.
5.  Press - Save field settings

Next page - ***Encry_test settings***  
Review some of the settings you did and add more like (\* means an entry is required))

1.  Label\*
2.  Required field - here we tick it, as the sole purpose of this ContentType is to upload and reference files - so this field is required - meaning a file has to be chosen for uploading.
3.  Help text (optional - "Upload files to be stored with encryption in the private file area.")
4.  Allowed file extensions\* - you need to specify which file extensions will be allowed - default is txt only. We use - bmp doc docx dot dotx eps jpg pdf png pps ppsx ppt pptx tif txt xls xlsx - no leading dot, separated with a blank or a coma.
5.  File directory - if you want to store it in a specific sub-directory
6.  Maximum upload size - to restrict what users upload
7.  Enable Description field - if you want to allow users to add text as the link item rather than the file name.

While on the "Manage Field" page you may want to delete the Body Field in case all you want is to upload files. - For this example Body Field was deleted.

## II. Changing the already uploaded files to be encrypted.

The files are uploaded via a Content Type containing the title and just a file field.  
Fields with content (=active nodes) cannot be changed. There are currently 26 nodes with files. We will try to do the following:

1.  add a second (new) File Field to the existing Content Type (with the file location the encrypted files area.
2.  on this site subscriptions are activated and the Content Type concerned is one of the subscribed items by default. We therefore disable subscriptions for the duration of the changes.
3.  open each node of the Content Type and upload the same file using the second (new) File Field. This way we have the reference to the file we need to upload in the first (old/existing) File Field.
4.  The uploaded files are displayed to the user through a View. The view needs to be changed to include the second (new) File Field and remove the first.
5.  When all 26 nodes are done we will delete the first (old/existing) File Field and delete the un-encrypted old files using FTP.
6.  Database check to see that the reference to the first (old/existing) File Field are entirely removed. If not cleaning up of the db.
7.  The uploaded files are displayed to the user through a View. The view needs to be changed to include the second File Field and remove the first.

## Conclusion:

It worked.  
Almost forgot - disabled subscriptions have been enabled again.

## Note of warning

**Encrypted Files** also adds the option of storing all files as ***Private, encrypted files*** - under ***..../admin/config/media/file-system***.  
If you activate this, you may find that images you upload will not be visible any more, as they are encrypted. So, during uploading with IMCE and placing them with an editor on a page (and on the page after saving) they are not showing up.  
I still need to experiment with this, therefore for now I returned my setting to "***Private local files served by Drupal.***"
