---
title: "Increase upload size in your php.ini"
source_url: "https://www.drupal.org/docs/7/managing-site-performance-and-scalability/increase-upload-size-in-your-phpini"
page_type: page
last_updated: "Last updated on 28 March 2022"
published: "2006-11-12T18:55:23+00:00"
modified: "2022-03-28T20:38:22+00:00"
breadcrumb: ["Drupal 7", "Managing Drupal 7 site performance and scalability"]
fetched: "2026-10-21T07:00:14Z"
raw: "raw/docs/7/managing-site-performance-and-scalability/increase-upload-size-in-your-phpini.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Increase upload size in your php.ini

**Note 1**: The file `php.ini` is not part of Drupal. It is a part of the PHP configuration. To locate it, look up your PHP configuration. If you're on shared hosting, you may not have access to it.

**Note 2**: Increasing PHP upload size is different from increasing PHP memory limit. You can learn how to increase memory limit [here](http://drupal.org/node/207036).

Drupal's limits on upload file size are determined by your server's PHP settings (as well as Drupal 6's specified settings that can be set at Admin \> Site Configuration \> File Upload). The default values for PHP will restrict you to a maximum 2 MB upload file size.

On the settings page for the upload module, Drupal calculates and displays the maximum file size that you can set based upon two PHP settings: 'post_max_size' and 'upload_max_filesize'. Since 'post_max_size' is the limit for all the content of your post, many people choose 'post_max_size' to be a multiple of 'upload_max_filesize' to allow multiple files to be uploaded, but this is not essential. The upload module limits the size of a single attachment to be less than either post_max_size, or upload_max_filesize, whichever is smaller. The default PHP values are 2 MB for upload_max_filesize, and 8 MB for post_max_size.

Depending on your host, changing these two PHP variables can be done in a number of places with the most likely being `php.ini` or .htaccess (depending on your hosting situation).

For example, to increase the limit on uploaded files to 10 MB:

- Add the below to the relevant php.ini file (recommended, if you have access). Note that for some hosts this is a system-wide setting. However, for hosts running PHP as a CGI script with suexec (for example) you may be able to put these directives in a **php.ini** file in your Drupal root directory.
  - `upload_max_filesize = 10M`
  - `post_max_size = 10M`
- Add the below to your .htaccess file in your Drupal root directory.
  - `php_value upload_max_filesize 10M`
  - `php_value post_max_size 10M`

The PHP documentation states that the memory_limit setting also affects file uploading. Generally speaking, memory_limit should be larger than post_max_size. If this is an issue, see the page on how to [Increase memory available to PHP (3 methods)](https://www.drupal.org/docs/7/managing-site-performance/increase-php-memory-limit)

Drupal also allows/enforces its own size limits, independently of what PHP allows. These are found in Drupal 6 at "Administer » Site configuration » File uploads" ( /admin/settings/uploads ). In Drupal 7 size limit is controlled on per-field basis. The Drupal settings cannot be larger than those permitted by PHP, but may be smaller if you haven't updated them, so remember to check there also, after updating the php.ini.
