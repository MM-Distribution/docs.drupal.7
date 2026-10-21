---
title: "PHP requirements for Drupal 7"
source_url: "https://www.drupal.org/docs/7/system-requirements/php-requirements-for-drupal-7"
page_type: page
last_updated: "Last updated on 4 December 2024"
published: "2012-09-13T00:43:09+00:00"
modified: "2024-12-04T15:41:20+00:00"
breadcrumb: ["Drupal 7", "Drupal 7 system requirements"]
fetched: "2026-10-21T05:52:40Z"
raw: "raw/docs/7/system-requirements/php-requirements-for-drupal-7.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# PHP requirements for Drupal 7

Below you will find some more detailed notes regarding the PHP requirements for Drupal 7. Individual modules may have specific requirements and configurations needed; please double check module documentation as well.

For information on Drupal 8 (or later), see the [current Drupal PHP requirements](/docs/system-requirements/php-requirements).

## PHP version required and supported

The table below show which versions of PHP is supported by Drupal 7.

|                 |                                                                                                             |                                                                                                       |
|-----------------|-------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|
| PHP version     | Supported by Drupal                                                                                         | Recommended for Drupal 7?                                                                             |
| 5.3 / 5.4 / 5.5 | No                                                                                                          |                                                                                                       |
| 5.6             | Yes                                                                                                         | ![](/misc/watchdog-warning.png) No (see note 1 and 2 below)                                           |
| 7.0             | Yes                                                                                                         | ![](/misc/watchdog-warning.png) No (see note 1 and 2 below)                                           |
| 7.1             | Yes                                                                                                         | ![](/misc/watchdog-warning.png) No (see note 1 and 2 below)                                           |
| 7.2             | Yes                                                                                                         | ![](/misc/watchdog-warning.png) No (see note 1 and 2 below)                                           |
| 7.3             | Yes                                                                                                         | ![](/misc/watchdog-warning.png) No (see note 1 and 2 below)                                           |
| 7.4             | Yes                                                                                                         | ![](/misc/watchdog-warning.png) No (see note 1 and 2 below)                                           |
| 8.0             | Yes                                                                                                         | ![](/misc/watchdog-warning.png) No (see note 1 and 2 below)                                           |
| 8.1             | Yes, as of Drupal 7.92                                                                                      | ![](/misc/watchdog-ok.png) Yes (see note 3 below) [See issue 3224299](/project/drupal/issues/3224299) |
| 8.2             | Yes, as of Drupal 7.94                                                                                      | ![](/misc/watchdog-ok.png) Yes [See issue 3304807](/project/drupal/issues/3304807)                    |
| 8.3             | Yes, as of Drupal 7.103                                                                                     | ![](/misc/watchdog-ok.png) Yes [See issue 3380823](/project/drupal/issues/3380823)                    |
| 8.4             | ![](/misc/watchdog-error.png) No, will not get support; [see issue 3380823](/project/drupal/issues/3380823) |                                                                                                       |

*(1) We do not recommend using unsupported versions of PHP. See the [minimum recommended PHP version](http://php.net/supported-versions.php) for Drupal 7.  
(2) Some vendors like RedHat/CentOS and Ubuntu LTS offer extended support for these versions of PHP, **check with your vendor.**  
(3) The latest Drupal 7 version is recommended to get full PHP 8 support.*

Please report PHP compatibility issues for contributed modules in their issue queue. Work is ongoing to extend PHP 8.x support on all the contributed modules.

## File and folder permissions

Drupal and PHP should have read and write access to the */sites/default/files* directory. This area is used to store cached files (compressed CSS and JavaScript) and any file uploads through the Drupal interface. The exact permissions of this directory depend on how your PHP installation is configured. Generally speaking, read-write-execute for all, nobody user, (777) is not recommended as a security risk. PHP can be run under as the specific user account on the server using [suPHP](http://www.suphp.org/Home.html) rather than a generic user (www) or nobody.

## PHP configuration settings

### Required PHP configuration settings

PHP *needs* the following <a href="http://www.php.net/manual/en/configuration.php" id="php_configuration">configuration</a> [directives](http://www.php.net/manual/en/configuration.directives.php) for Drupal to work (only directives that differ from the default [php.ini-development](https://git.php.net/?p=php-src.git;a=blob;f=php.ini-development) / [php.ini-production](https://git.php.net/?p=php-src.git;a=blob;f=php.ini-production)):

- error_reporting set to E_ALL & ~E_NOTICE. Work is ongoing to change this to E_ALL for Drupal 7.
- [safe_mode](http://www.php.net/manual/en/features.safe-mode.php): off. Safe mode may interfere with file and image uploads. This is applicable for only for PHP versions below 5.3.0, as of PHP 5.4.0 Safe Mode has been removed
- [Tokenizer functions](http://www.php.net/manual/en/ref.tokenizer.php) require the tokenizer extension to be enabled. (Read more [\#357970: Undefined function token_get_all](/project/drupal/issues/357970 "Status: Closed (fixed)"))

### Recommended PHP configuration settings

Setting: **session.cache_limiter = nocache**

Setting: **session.auto_start = 0**

Setting: **expose_php = off**  
Reason: Shows current PHP version in all header requests, security disclosure, [see here](http://phpsec.org/projects/phpsecinfo/tests/expose_php.html)  
Example: X-Powered-By: PHP/5.3.8

Setting: **allow_url_fopen = off**  
Reason: This is a security issue: [see here](http://phpsec.org/projects/phpsecinfo/tests/allow_url_fopen.html)

Setting: **magic_quotes_gpc = off**  
Reason: Forces quotes in variables - This feature has been *deprecated* as of PHP 5.3.0 and *removed* as of PHP 5.4.0.

Setting: **register_globals = off**  
Reason: Security issue - having this enabled subjects PHP variables to input from any source:  
This feature has been *deprecated* as of PHP 5.3.0 and *removed* as of PHP 5.4.0.

Setting: **display_errors = Off**  
Reason: Hides errors output to display (website) we want to send to log file instead.

### Memory requirements

PHP memory requirements can vary significantly depending on the modules in use on your site. Drupal 7 core requires [32MB](http://api.drupal.org/api/constant/DRUPAL_MINIMUM_PHP_MEMORY_LIMIT/7).

Warning messages will be shown if the PHP configuration does not meet these requirements. However, while these values may be sufficient for a default Drupal installation, a production site with a number of commonly used modules enabled could require more memory. Typically 128 MB or 256 MB are found in production systems. Some installations may require much more, especially with media-rich implementations. If you are using a hosting service it is important to verify that your host can provide sufficient memory for the set of modules you are deploying or may deploy in the future. (See [Increase PHP memory limit](http://drupal.org/node/207036) for additional information on modifying the PHP memory limit.)

### Enable caching

Within the Drupal interface, it is highly recommended that caching be enabled under *admin/config/development/performance*. This will help increase the performance of your Drupal installation and the end user experience. For more details see [Caching to improve performance](https://drupal.org/node/326504).

## Extensions

### Database extensions

The PHP extension for connecting to your chosen database must be installed and enabled. Drupal's currently supported database connectors are: [mysql](http://www.php.net/manual/en/ref.mysql.php) (the original MySQL extension), [mysqli](http://www.php.net/manual/en/mysqli.summary.php) (an improved connector for newer MySQL installations), and [pgsql](http://www.php.net/manual/en/ref.pgsql.php) (for PostgreSQL). Note: PHP 5.x no longer enables the mysql extension by default. Please read the links above for installing and enabling your chosen connector.

### PHP Data Objects (PDO)

PDO must be [activated for Drupal 7 to install and run correctly](/node/549702). The extension is normally enabled by default in a standard PHP installation. NB! The PECL version of PDO is not compatible with Drupal 7 and cannot be used.

### XML extension

PHP [XML extension](http://www.php.net/manual/en/ref.xml.php) (for Blog API, Drupal, and Ping modules). This extension is [enabled by default](http://www.php.net/manual/en/ref.xml.php#xml.installation) in a standard PHP installation; the Windows version of PHP has built-in support for this extension. Enabling the XML extension also enables PHP DOM. DOM is now a systems requirement.

### Image library

An image library for PHP such as the [GD library](http://www.php.net/gd) is needed for image manipulation (resizing user pictures, image and imagecache modules). GD is included with PHP 4.3 and higher and usually enabled by default. GD is a *required* extension in Drupal 7 and later. [ImageMagick](http://www.imagemagick.org/script/index.php) is also supported for basic image manipulations in Drupal core but there is much less support from contributed modules.  
If you have administrator rights on a Debian/Ubuntu server, and GD is *not* already available (see your [phpinfo](http://drupal.org/node/59680)) it can usually be installed by running the following command:  
`sudo apt-get install php-gd`  
or on Redhat/Centos:  
`sudo yum install php-gd`  
See the [ImageMagick install instructions](http://www.imagemagick.org/script/binary-releases.php) for your platform if you want that.

### OpenSSL

The [PHP OpenSSL](https://php.net/manual/en/book.openssl.php) extension is recommended to allow Drupal to make outgoing requests using HTTPS. Some platforms provide a separate OpenSSL package, e.g. php-openssl.

There is also ongoing work to make Drupal core's Update Manager module check for updates using HTTPS, which would make this an even stronger recommendation or possibly a requirement. See [\#1538118: Update status does not verify the identity or authenticity of the release history URL](/project/drupal/issues/1538118 "Status: Closed (fixed)") and <https://groups.drupal.org/node/506128>.

### JSON

Drupal 7 and 8 require PHP compiled with JSON. JSON support is normally compiled as part of PHP core, but in case you're getting errors like `PHP Fatal error: Call to undefined function Drupal\\Component\\Serialization\\json_encode() in ... core/lib/Drupal/Component/Serialization/Json.php` try [adding the JSON extension](http://ca2.php.net/manual/en/json.installation.php).

### cURL

The [PHP cURL](http://php.net/manual/en/book.curl.php) extension is required for the SimpleTest module in Drupal 7 and 8, as well as Aggregator and some contributed modules. Many Linux distributions and development stacks will have it enabled by default, but if your system doesn't, here are instructions on how to enable it for various platforms are below.

#### Windows - XAMPP

Open `C:/xampp/php/php.ini` in a text editor.

Uncomment the `extension=php_curl.dll` line by removing the preceding ";".

#### Linux - Ubuntu/Debian

Run `sudo apt-get update && sudo apt-get install php-curl`.

If you need to enable it, run `sudo phpenmod curl`.

### Mbstring

The [PHP mbstring](http://php.net/manual/en/intro.mbstring.php) extension provides multibyte specific string functions used for Drupal installation in other languages except English and also multilingual sites in Drupal. It helps deal with multibyte encodings in PHP and also handles Unicode based encodign like UTF-8 or UCS-2.

It can be installed in Linux systems depending on OS, eg: for Debian based system:

`sudo apt-get install php-mbstring`

### APC

Recent versions of APC (apparently since 3.1.6) set 'Enable internal debugging in APC' as the default. This generates large numbers of PHP messages that can make diagnosing other problems more difficult. This option can be disabled during installation by explicitly entering `no` to the prompt - hitting 'enter' will enable the option in spite of the wording of the prompt.

Also, see [Drupal 7-specific](#7) information relating to APC.

### ssh extension

The `ssh` [PECL extension](https://pecl.php.net/package/ssh2) is an optional add-on to your PHP setup. While it is not required for normal Drupal function, when absent, both the `Add new module` and `Add new theme` links in your drupal's administration will fail with the admittedly uninformative message:`"Your server does not support installing modules and themes from this interface. "`

## Other

### .htaccess settings

Some of the memory settings are contained in the default .htaccess file that ships with Drupal, so you shouldn't need to set them explicitly. Note, however, that setting PHP configuration options from .htaccess only works under the following conditions:

- With Apache (or a compatible web server)
- If the .htaccess file is actually read, i.e. [AllowOverride All](http://httpd.apache.org/docs/current/mod/core.html#allowoverride) in the main Apache configuration (usually httpd.conf) is enabled
- If PHP is installed as an Apache module

In some shared hosting environments, access to these settings is restricted. If you cannot make these changes yourself, please ask your hosting provider to adjust them for you.

### Other interfaces

See the [PHP manual](http://www.php.net/manual/en/configuration.changes.php#configuration.changes.other) for how to change configuration settings for other interfaces to PHP.

### Secure Random Number Generation

See discussion on [Drupal 7 issue](/node/2550519)

### xdebug

If using xdebug:

Setting: **xdebug.show_exception_trace = 0**  
Reason: Could cause Drupal's installer to crash

Setting: **xdebug.max_nesting_level = 256**  
Reason: Using the default max_nesting_level of 100 (in xdebug versions \< 2.3) causes some pages to crash.

### PHP requirements details

See [the phpinfo() page on Drupal.org](http://drupal.org/node/59680) to learn how to use phpinfo to get the details of your system. For example, phpinfo will tell you if you have a database already installed and what versions of PHP, MySQL, etc. your system is running. Phpinfo will also tell you what PHP variables are set as well as many other helpful things.

It is often possible to update to a newer version of PHP than ships with your Linux distribution. For RHEL, we recommend [IUS Community Project](https://ius.io/), and for Debian, <https://deb.sury.org/>.

The Drupal 7 Update manager can install/update modules and themes via SSH if the required libraries have been installed on the server. If SSH is *not* already available (see your [phpinfo](http://drupal.org/node/59680)) it can usually be installed by executing:  
`apt-get install libssh2-php`.

- Drupal 7 may require the time parameter (`max_execution_time`) to be at least 30 seconds.

- APC installation guides sometimes recommend setting `apc.include_once_override=1`. This causes Drupal 7 to fail (white screen, error 500) as reported in [Do not enable apc.include_once_override](https://www.drupal.org/requirements#comment-4347398).

- The following PHP extensions are required for Drupal 7:  

  ``` php
  $required_extensions = array( 'date', 'dom', 'filter', 'gd', 'hash', 'json', 'pcre', 'pdo', 'session', 'SimpleXML', 'SPL', 'xml', ); 
  ```

### Summary of the required settings in the *php.ini* file

|                |                                                    |                                 |
|----------------|----------------------------------------------------|---------------------------------|
| section        |                                                    |                                 |
| PHP version    |                                                    | Min rec 5.4                     |
| core           | allow_url_fopen                                    | must be OFF or nonexistent      |
| core           | display_errors                                     | off                             |
| core           | max_execution_time                                 | min 30 seconds                  |
| core           | expose_php                                         | must be OFF or nonexistent      |
| core           | memory_limit                                       | 32MB                            |
| ctype          | ctype functions                                    |                                 |
| cURL           | cURL support                                       |                                 |
| cURL           | libSSH Version                                     | required for install update     |
| date           | date/time support                                  | enabled                         |
| dom            | DOM/XML                                            | enabled                         |
| fileinfo       | fileinfo support                                   |                                 |
| filter         | Input Validation and Filtering                     | enabled                         |
| gd             | GD Support                                         | enabled                         |
| ?              | magic_quotes_gpc                                   | must be OFF or nonexistent      |
| ?              | magic_quotes_runtime                               | must be disabled or nonexistent |
| ?              | safe_mode                                          | must be disabled or nonexistent |
| ?              | register_globals                                   | must be OFF or nonexistent      |
| hash           | hash support                                       | enabled                         |
| openssl        | openssl support                                    | enabled                         |
| json           | json support                                       | enabled                         |
| pcre           | PCRE (Perl Compatible Regular Expressions) Support | enabled                         |
| pdo            | PHP Data Objects(PDO)                              | (specific for your database)    |
| pecl           | PECL version of PDO                                | not compatible                  |
| session        | Session Support                                    | enabled                         |
| session        | session.auto_start                                 | 0                               |
| session        | session.cache_limiter                              | nocache                         |
| SimpleXML      | Schema support                                     | enabled                         |
| SPL            | SPL support                                        | lots                            |
| Suhosin        | APC.include-once-override                          | avoid                           |
| Tokenizer      | Tokenizer Support                                  |                                 |
| XML            | XML Support                                        | enabled                         |
| XML            | XML Namespace Support                              | enabled                         |
| Zend OPcache   | Opcode caching                                     |                                 |
| Zend OPcache   | PHP 5.5+ opcache.save_comments                     |                                 |
| Zend OPcache   | PHP 5.5+ opcache.load_comments                     |                                 |
| MODULE TESTING | memory_limit                                       |                                 |
