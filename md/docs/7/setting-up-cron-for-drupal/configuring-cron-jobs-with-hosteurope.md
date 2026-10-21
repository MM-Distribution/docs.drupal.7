---
title: "Configuring cron jobs with hosteurope"
source_url: "https://www.drupal.org/docs/7/setting-up-cron-for-drupal/configuring-cron-jobs-with-hosteurope"
page_type: page
last_updated: "Last updated on 5 August 2016"
published: "2013-06-04T14:15:07+00:00"
modified: "2016-08-05T14:28:27+00:00"
breadcrumb: ["Drupal 7", "Setting up cron for Drupal 7"]
fetched: "2026-10-21T06:27:01Z"
raw: "raw/docs/7/setting-up-cron-for-drupal/configuring-cron-jobs-with-hosteurope.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Configuring cron jobs with hosteurope

## Setting up a cronjob at hosteurope

This Document shows one way to set up a cronjob at hosteurope. There may be other ways, this one works.

### 1. Grab your FTP-Account

#### Edit /scripts/cron-lynx.sh

Be sure that FTP works as expected and you can connect to your installed drupal-site via an ftp-client (like cyberduck, filezilla or some other, terminal-ftp will do it, too). Connect to your drupal-site, navigate to /scripts and open file `cron-lynx.sh` for editing. In cyberduck just doubleclick the file, an approbiate editor should launch. Other ftp-clients will need you to download `cron-lynx.sh` to your desktop.

You should see something like this:

``` php
#!/bin/sh

/usr/bin/lynx -source http://example.com/cron.php > /dev/null 2>&1
```

The first line is for the operating-system to tell it that this file will be interpreted by shell. Just leave it. The next line is the standard-drupal suggestion for lynx-based cronjobs. Comment this line out by putting a `#` sign in front of it (or simply delete it) and write this:

`lynx -dump http://[your-website-url]/cron.php?cron_key=[your-cron-key] > /dev/null`

Replace `[your-website-url]` with your actual website address, e.g. "<http://example.com>" (without "" and without \[\]) and `[your-cron-key]` which you can get from `http://[your-website-url]/admin/config/system/cron`.

Save your changes to file `cron-lynx.sh` and put it over the existing ftp-file (overwrite it).

#### Set file permissions

Next, set proper file permissions on this file `cron-lynx.sh`. Depending on your ftp-client you can set permissions on this file per ocal-numbers or per clicks on values or both.

Whatever method your ftp-client offers, the result should be:

- Octal-Number: 750
- which is this in a permissions matrix:  
  |       |      |       |         |
  |-------|------|-------|---------|
  |       | read | write | execute |
  | owner | x    | x     | x       |
  | group | x    |       | x       |
  | other |      |       |         |

That's for the FTP-Part.

## 2. Grab your KIS-account

Go to `https://kis.hosteurope.de` and log yourself in, using your username and password for your server, virtualserver or webpackage. Select your webhosting-product and navigate to `Cronjobs` in the lower half of the administration menu.

Click on "Neuen Cronjob definieren" and fill in following data:

Aktiviert  
Ja

Befehl  
path-to-your-cron-lynx.sh-file, beginning at root directory of your webhosting product

Kommentar  
Any comment you like

Benutzer  
same user that the file belongs to. if unsure, let the default

Minuten  
\*/15

this means: every 15 minutes. you can change this to your preferred value. beware "15" is not the same as "\*/15". "15" means "every 15th minute", e.g. every hour quarter-past.

Stunden  
\*

Tage  
\*

Monate  
Alle

Wochentage  
Unabhängig vom Wochentag

Don't forget to save this form. And your'e done.

## Check result

Check your drupal status report at `http://yoursite.com/admin/reports/dblog` to see if there are any errors related to cron. If not, everything works fine. If an error occurs, try to find the reason, walk through this steps carefully again and fix typos.
