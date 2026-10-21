---
title: "Configuring cron jobs with Mac OS X Server 10.5.x and later"
source_url: "https://www.drupal.org/docs/7/setting-up-cron-for-drupal/configuring-cron-jobs-with-mac-os-x-server-105x-and-later"
page_type: page
last_updated: "Last updated on 5 August 2016"
published: "2009-08-29T05:09:31+00:00"
modified: "2016-08-05T14:28:27+00:00"
breadcrumb: ["Drupal 7", "Setting up cron for Drupal 7"]
fetched: "2026-10-21T06:25:13Z"
raw: "raw/docs/7/setting-up-cron-for-drupal/configuring-cron-jobs-with-mac-os-x-server-105x-and-later.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Configuring cron jobs with Mac OS X Server 10.5.x and later

Drupal documentation refers to running **cron** jobs periodically. But OS X Server (at least Leopard Server) has a kernel bug that results in a log message from **cron** jobs to the effect “Could not setup Mach task special port 9: (os/kern) no access”. Not a joyful message to come across, though it appears to be harmless.

In addition, OS X doesn’t come with **wget**, so the suggested **cron** call in the Drupal docs doesn’t work anyhow.

To avoid both of these problems, put a call to **curl** in a **launchd** daemon .plist file (e.g. **/Library/LaunchDaemons/drupal-cron-call.plist**), thusly:

``` php
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>Label</key>
    <string>com.{domain-name}.drupal-cron</string>
  <key>UserName</key>
    <string>nobody</string>
  <key>GroupName</key>
    <string>_www</string>
  <key>ProgramArguments</key>
    <array>
      <string>/usr/bin/curl</string>
      <string>-s</string>
      <string>http://localhost/{drupal-subdirectory/}cron.php</string>
    </array>
  <key>RunAtLoad</key>
    <true/>
  <key>StartCalendarInterval</key>
    <dict>
      <key>Minute</key>
      <integer>09</integer>
    </dict>
  </dict>
</plist>
```

Then **launchctl load /Library/LaunchDaemons/drupal-cron-call.plist** and enjoy.

Notes:

- “<http://localhost/>{drupal-subdirectory/}cron.php” might be replaced with “http://{domain-name}/cron.php” for a production server.

- Be sure to replace **{domain-name}** and/or **{drupal-subdirectory/}** placeholders (in sample .plist file above) with appropriate values.

- For non-production environments, **StartCalendarInterval**, which always runs at nine minutes past the hour in this example, should perhaps be replaced with **StartInterval**, which always runs after a specified number of seconds have elapsed (since the last run). For production environments, it’s nice to run **cron** by the clock, but development computers may be asleep during arbitrary times and thus benefit from the elapsed-time approach. To change this, replace:  

  ``` php
    <key>StartCalendarInterval</key>
      <dict>
        <key>Minute</key>
        <integer>09</integer>
      </dict>
  ```

  with:

  ``` php
    <key>StartInterval</key>
      <integer>3600</integer>
  ```

  (This example runs every hour.)
