---
title: "SimpleTest [Browser] on Vista"
source_url: "https://www.drupal.org/docs/7/testing/simpletest-browser-on-vista"
page_type: page
last_updated: "Last updated on 30 November 2016"
published: "2008-09-05T00:47:49+00:00"
modified: "2016-11-30T11:05:14+00:00"
breadcrumb: ["Drupal 7", "Automated testing for Drupal 7"]
fetched: "2026-10-21T08:11:06Z"
raw: "raw/docs/7/testing/simpletest-browser-on-vista.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# SimpleTest [Browser] on Vista

**The Symptom**

\[Browser\] based SimpleTests are failing when run on your localhost (or any system) running Windows Vista.

**The Problem**

Windows Vista has added a line to its hosts file that blocks SimpleTest's Browser from fetching pages via the following code in SimpleTest's socket.php file

``` php
    function _openSocket($host, $port, &$error_number, &$error, $timeout) {
        return @fsockopen($host, $port, $error_number, $error, $timeout);
    }
```

**The Solution**

1\. Run notepad as Administrator (find the icon for notepad, right-click-\>run as Administrator)  
2. Navigate to your hosts file (c:\windows\system32\drivers\etc\hosts)  
3. Find the line that looks like:

``` php
::1             localhost
```

and remove it, or comment it out with a \#

4\. Restart apache  
5. Enjoy working SimpleTest \[browser\] tests
