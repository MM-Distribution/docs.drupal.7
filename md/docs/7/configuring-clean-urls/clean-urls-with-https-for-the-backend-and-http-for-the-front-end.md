---
title: "Clean URLs with https for the backend and http for the front end"
source_url: "https://www.drupal.org/docs/7/configuring-clean-urls/clean-urls-with-https-for-the-backend-and-http-for-the-front-end"
page_type: page
last_updated: "Last updated on 18 March 2018"
published: "2012-10-05T14:36:13+00:00"
modified: "2018-03-18T21:45:22+00:00"
breadcrumb: ["Drupal 7", "Configuring clean URLs in Drupal 7"]
fetched: "2026-10-21T06:52:29Z"
raw: "raw/docs/7/configuring-clean-urls/clean-urls-with-https-for-the-backend-and-http-for-the-front-end.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Clean URLs with https for the backend and http for the front end

This write up needs (technical) review. Don't just copy and paste this code unless you have at least some understanding of the matter.

In Drupal 7 in order to run https(SSL) for the admin backend and run a normal http on the front I had to do the following. This code is intended for if the backend is running on a subdomain/ subdirectory on SSL with a different URL address then the http address of the front end, and with clean URLs enabled.

In settings.php:

``` php
if ($_SERVER['SERVER_PORT'] == 443) {
$base_url = 'https://address_1.com/subdirectory';
} else {
$base_url = 'http://subdomain.address_2.com';
}
```

The first \$base_url is the one where you have your admin backend. The second is for your website front end. What this does is when you type the address check whether we are on a https or a http connection. Then the if the address match the \$base_url either become a https or a http connection and go to the \$base_url that is set.

Now this will work fine as is without the Clean URL enabled. However when you enable Clean URL it stops working. The reason is that we have to set the rewritebase, but where do we set the rewritebase to? If we set it to the subdirectory for the back end then the front end URLs error out. If we set it to the front end then the back end URLs error out. If we leave it as is the front end will work, but the backend won't work. According to the Drupal Docs this can be solved as follows:

In the Drupal .htaccess in your subdirectory where you have Drupal installed replace:

``` php
RewriteCond %{REQUEST_FILENAME} !-f
RewriteCond %{REQUEST_FILENAME} !-d
RewriteCond %{REQUEST_URI} !=/favicon.ico
RewriteRule ^ index.php [L]
```

With:

``` php
RewriteCond %{REQUEST_FILENAME} !-f
RewriteCond %{REQUEST_FILENAME} !-d
RewriteCond %{REQUEST_URI} ^/subdirectory/(.*)$
RewriteRule ^(.*)$ /subdirectory/index.php?q=$1 [L,QSA]

RewriteCond %{REQUEST_FILENAME} !-f
RewriteCond %{REQUEST_FILENAME} !-d
RewriteCond %{REQUEST_URI} !=/favicon.ico
RewriteRule ^ index.php [L]
```

The order of the rules is important. If you turn them around it won't work.

You should now be able to access the https(SSL) side for your back end and the http side for the front end of the website with clean URLs.
