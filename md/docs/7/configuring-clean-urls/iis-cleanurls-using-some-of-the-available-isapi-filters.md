---
title: "IIS CleanURLs using some of the available ISAPI filters."
source_url: "https://www.drupal.org/docs/7/configuring-clean-urls/iis-cleanurls-using-some-of-the-available-isapi-filters"
page_type: page
last_updated: "Last updated on 20 December 2016"
published: "2006-01-25T23:52:41+00:00"
modified: "2016-12-20T13:08:17+00:00"
breadcrumb: ["Drupal 7", "Configuring clean URLs in Drupal 7"]
fetched: "2026-10-21T06:50:56Z"
raw: "raw/docs/7/configuring-clean-urls/iis-cleanurls-using-some-of-the-available-isapi-filters.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# IIS CleanURLs using some of the available ISAPI filters.

There is a free version called [ISAPI_Rewrite Lite](http://www.isapirewrite.com/) that should get clean URLs working for IIS.

### General configuration:

1.  Make sure `IIS_WPG` and `NETWORK SERVICE` have access to the .htaccess file - otherwise ISAPI_Rewrite cannot read the configuration httpd.ini (2.x) or .htaccess (3.x) files.
2.  **D5:** Add `$conf['clean_url'] = 1` to your settings.php - to manually enable clean urls.
3.  **D6:** There are no changes required - it simply works.

### ISAPI_Rewrite 3.x:

You don't need to change the standard Drupal .htaccess file. Helicon ISAPI_Rewrite 3.x was designed to maintain maximum Apache mod_rewrite compatibility. Use the latest version of ISAPI_Rewrite 3.x (\>=3.1.0.56 is required) with Drupal. If you cannot get it working out if the box - enable the `LogLevel` (<http://www.helicontech.com/isapi_rewrite/doc/LogLevel.htm>) setting and try to figure out what's broken in ISAPI_Rewrite.

### ISAPI_Rewrite 2.x: Configuration example if Drupal is installed in webservers root

``` php
[ISAPI_Rewrite]

# Accept an url with the following directories and pass them through unchanged.
RewriteRule /(?:misc|files|modules|themes|sites|uploads)/(.*) $0 [I,L]

# Make URLs sane
RewriteRule /cron\.php $0 [I,L]
RewriteRule /index\.php.* $0 [I,L]
RewriteRule /install\.php.* $0 [I,L]
RewriteRule /update\.php.* $0 [I,L]
RewriteRule /xmlrpc\.php $0 [I,L]

# activate rewriting for custom modules (for e.g. banner.module)
RewriteRule /banner_db\.php $0 [I,L]
RewriteRule /banner_file\.php $0 [I,L]

# deactivate rewriting for custom modules (for e.g. robotstxt.module)
RewriteRule /robots\.txt.* $0 [I,L]

RewriteRule /(.*)\?(.*) /index.php\?q=$1&$2 [I,L]
RewriteRule /(.*) /index.php\?q=$1 [I,L]
```

### ISAPI_Rewrite 2.x: Configuration example if Drupal is installed in a subdirectory (Requires ISAPI_Rewrite \>=2.9 Build 63)

``` php
[ISAPI_Rewrite]

# You must change/remove prefixes if Drupal is not installed in a subdirectory
# Specify namespaces with UriMatchPrefix - DO NOT CHANGE ORDER
UriMatchPrefix /drupal

# Accept an url with the following directories and pass them through unchanged.
RewriteRule /(?:misc|files|modules|themes|sites|uploads)/(.*) $0 [I,L]

# Make URLs sane
RewriteRule /cron\.php $0 [I,L]
RewriteRule /index\.php.* $0 [I,L]
RewriteRule /install\.php.* $0 [I,L]
RewriteRule /update\.php.* $0 [I,L]
RewriteRule /xmlrpc\.php $0 [I,L]

# activate rewriting for custom modules (for e.g. banner.module)
RewriteRule /banner_db\.php $0 [I,L]
RewriteRule /banner_file\.php $0 [I,L]

# deactivate rewriting for custom modules (for e.g. robotstxt.module)
RewriteRule /robots\.txt.* $0 [I,L]

# specify namespaces with UriFormatPrefix - DO NOT CHANGE ORDER
UriFormatPrefix /drupal

RewriteRule /(.*)\?(.*) /index.php\?q=$1&$2 [I,L]
RewriteRule /(.*) /index.php\?q=$1 [I,L]

# reset namespaces to default
UriMatchPrefix
UriFormatPrefix
```

## Translating Apache's rewrite rules

RewriteCond %{REQUEST_FILENAME} !-f  
RewriteCond %{REQUEST_FILENAME} !-d

In plain English: If the REQUEST_FILENAME variable does not exist (not an existing file and not an existing directory) then apply the rule:  
RewriteRule ^(.\*)\$ index.php?q=\$1 \[L,QSA\]"

After much research, this exact functionality does not appear to exist in any ISAPI module for IIS. I think the following solution will help solve this issue. It probably works with most "ISAPI rewrite" modules (they just need the "stop the rewriting process" option).

With this approach you basically **revert the "Apache Rewrite" logic**. First define rules for **known files/folders** (like /themes/ ..etc..). Have those "matching rules" **exit**, so rules processing stops before going to the next rule. With mod_rewrite.dll you can do that with the option \[l\].

Here is what my rules file looks (so far) like (using mod_rewrite.dll):  
RewriteRule ^/index.php\\q\\(.\*)\$ /index.php?q=\$1 \[l\]  
RewriteRule ^/themes/(.\*)\$ /themes/\$1 \[l\]  
RewriteRule ^/misc/(.\*)\$ /misc/\$1 \[l\]  
RewriteRule ^/(.\*)\$ /index.php?q=\$1 \[l\]

Remember, you have to add an "existing" rule for all known folders/files before hitting the final rule. The first rule is to avoid recursion and exit immediately if the URL already has index.php?q=.

------------------------------------------------------------------------

To better understand the Apache rules here are the definitions of the main options:  
'last\|L' (last rule)  
Stop the rewriting process here and don't apply any more rewriting rules. Use this flag to prevent the currently rewritten URL from being rewritten further by following rules.

'qsappend\|QSA' (query string append)  
This flag forces the rewriting engine to append a query string part in the substitution string to the existing one instead of replacing it. Use this when you want to add more data to the query string via a rewrite rule.

REQUEST_FILENAME  
The full local filesystem path to the file or script matching the request.

'-d' (is directory)  
Treats the TestString as a pathname and tests if it exists and is a directory.  
'-f' (is regular file)  
Treats the TestString as a pathname and tests if it exists and is a regular file.

Note: Getting Apache running on MS Windows is not that bad (I had been delaying it for years). In reality, it's a matter of a few hours to get going. <http://www.sitebuddy.com> aims to save you time in that endeavor.
