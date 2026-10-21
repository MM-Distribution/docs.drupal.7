---
title: "Multi-site in subdirectories"
source_url: "https://www.drupal.org/docs/7/multisite-drupal/multi-site-in-subdirectories"
page_type: page
last_updated: "Last updated on 18 May 2017"
published: "2016-05-14T15:06:44+00:00"
modified: "2017-05-18T08:11:05+00:00"
breadcrumb: ["Drupal 7", "Multisite Drupal 7"]
fetched: "2026-10-21T06:11:16Z"
raw: "raw/docs/7/multisite-drupal/multi-site-in-subdirectories.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Multi-site in subdirectories

if you don't know what multi-site is about, read [the general multi-site documentation](/documentation/install/multi-site) first.

## Background

The most common use case is subsite multi-site: One site for each domain `sub1.example.com`, `sub2.example.com` and so on. However, some times you want subdirectory multi-site: One site for each directory `example.com/site1`, `example.com/site2` and so on. Either you can't create a subsite/subdomain (because you don't have access to DNS) or you don't want to for example for SEO considerations.

When you are attempting to get Drupal multi-site working using subdirectory URLs rather than subdomain or different domain URLs, you may encounter problems. You'll start out by making a directory such as `sites/example.com.site1`, and putting a settings.php file there. If this works for you, great! But it probably will not, until you create a symbolic link for each site.

The reason it works without symbolic links for some sites is different behavior between webservers. It seems Apache always needs the symlinks, while IIS doesn't. (This should be confirmed and also tested for other webservers.)

## Making symlinks

PS! All command examples below are written for Linux, but should work on Mac OS X too.

So it didn't work without the symlinks ... You have to make a symbolic link that makes "the document root" for `example.com/site1` (and `example.com/site2`) the same as the document root for `example.com`.

For example, if your document root for example.com is `/var/www/example.com` and you want `example.com/site1` and `example.com/site2` to use multisite (based on the existing example.com site):

1.  Verify that Drupal is installed at `/var/www/example.com/`

2.  Verify that there is a `settings.php` for each site - check `/var/www/example.com/sites/example.com.site1/` and `/var/www/example.com/sites/example.com.site2/`

3.  Create symbolic links in `/var/www/example.com`:  

    ``` php
    cd /var/www/example.com
    ln -s . site1
    ln -s . site2
    ```

It should be noted that you instead of symbolic links, can use aliases in the webserver configuration.

``` php
Alias /site1/ /var/www/example.com/
Alias /site2/ /var/www/example.com/
```

## Testing that it works

After making the symbolic links, visit `example.com/site1` and `example.com/site2` to install Drupal as normal for each subdirectory.

PS! If you get a "Symbolic link not allowed or link target not accessible" error when visiting the URLs, several things can be wrong:

- The webserver isn't configured correctly for symbolic links. For Apache check the `Options` directive. You must allow symbolic links with `+FollowSymlinks` and maybe relax security with `-SymLinksIfOwnerMatch.`

- The symbolic links has wrong owner and group - adjust it with  

  ``` php
  chown -h proper-user:proper-group site1
  chown -h proper-user:proper-group site2
  ```

## Clean URL problems

If you have problems with clean URLs for the subdirectory multi-site installations, the reason is normally because you have activated a RewriteBase line in your `.htaccess` file. Since the multi-site installations share the `.htaccess` file, that RewriteBase line forces you duplicate the RewriteCond and RewriteRule lines for each multi-site installations. In other words, try adding the following stanza immediately before the existing rewrite rule (for Drupal 7):

``` php
RewriteCond %{REQUEST_FILENAME} !-f
RewriteCond %{REQUEST_FILENAME} !-d
RewriteCond %{REQUEST_URI} !=/favicon.ico
RewriteCond %{REQUEST_URI} ^/site1
RewriteRule ^ site1/index.php [L]

RewriteCond %{REQUEST_FILENAME} !-f
RewriteCond %{REQUEST_FILENAME} !-d
RewriteCond %{REQUEST_URI} !=/favicon.ico
RewriteCond %{REQUEST_URI} ^/site2
RewriteRule ^ site2/index.php [L]
```

That block should go right after the `RewriteBase /` line, and before the other RewriteCond lines. What that does is catch incoming URLs that contain the site1 or site2 prefix and route them to the symlinked index.php file so that Drupal finds the right settings file.

## Avoid infinite symlink recursion

An unintended side effect of subdirectory multi-sites is infinite symlink recursion which search engine crawlers may follow, thus hurting SEO and creating unwanted traffic on your site. To see the problem visit `example.com/site1/site1/site1/site1` One can fix this using one neat redirect line in .htaccess:

``` php
RedirectMatch 301 /(site1|site2)/(site1|site2)/(.*) http://example.com/$1/$3
```

(This can be extended to any number of subsites - just add the directory names with pipes between like above.)

This covers any scenario of unwanted paths strung together and will redirect to the appropriate page i.e. **example.com/site1**/site1/site2/site2/site1/**technology/software** will 301 redirect to example.com/site1/technology/software, ensuring that only the latter gets indexed.
