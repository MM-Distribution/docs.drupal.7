---
title: "Configuring cron jobs using the cron command"
source_url: "https://www.drupal.org/docs/7/setting-up-cron/configuring-cron-jobs-using-the-cron-command"
page_type: page
last_updated: "Last updated on 19 May 2021"
published: "2005-05-27T00:45:44+00:00"
modified: "2021-05-19T17:46:29+00:00"
breadcrumb: ["Drupal 7", "Setting up cron for Drupal 7"]
fetched: "2026-10-21T06:23:24Z"
raw: "raw/docs/7/setting-up-cron/configuring-cron-jobs-using-the-cron-command.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Configuring cron jobs using the cron command

Cron is a daemon that executes commands at specified intervals. These commands are called "cron jobs." Cron is available on Unix, Linux and Mac servers. Windows servers use a [Scheduled Task](http://drupal.org/node/31506) to execute commands.

For a modest personal site, you might set up this cron job to run once a day. For a more active site, you might want to run that job more often—perhaps every few hours or every hour. This regular visit will tell Drupal to perform its periodic tasks, and this will help keep your system running smoothly.

## Cron URL

Each Drupal version has a different URL, you must request for cron to trigger. For Drupal 7 and later, the URL contains a "secret key" (see below for hard-coding it) to prevent external abuse. The secret URL can be found at each of these pages:

- **Status report** — `Reports Administration > Reports > Status (/admin/reports/status)`
- **Cron configuration** — `Administration > Configuration > System > Cron (/admin/config/system/cron)`

**URL format:**

|                      |                                                  |
|----------------------|--------------------------------------------------|
| Drupal core version  | URL                                              |
| Drupal 8             | `http://www.example.com/cron/<key>`              |
| Drupal 7             | `http://www.example.com/cron.php?cron_key=<key>` |
| Drupal 6 and earlier | `http://www.example.com/cron.php`                |

## The cron command

In the following example, the crontab command shown below will activate the cron tasks automatically on the hour:

`0 * * * * wget -O - -q -t 1 http://CRON_URL`

`http://CRON_URL` is replaced with a URL which is different for each Drupal version. See above.

In the above sample, the `0 * * * *` represents when the task should happen. The first figure represents minutes – in this case, on the "zero" minute, or top of the hour. The other figures represent, respectively, hour, day, month and day of the week. A `*` is a wildcard, meaning "every time." The minimum is every one minute `* * * * *`.

The rest of the line `wget -O - -q -t 1` basically tells the server to request a url, so that the server executes the cron script. 

Another option is to use Drupal console, for example:

`30 * * * * /var/www/html/vendor/bin/drupal --root=/var/www/html/docroot cron:execute > /dev/null 2>&1`

executes cron once per hour at 30 minutes after the hour, with all output (stdout and stderr) silenced by`> /dev/null 2>&1`.

**Examples**

|                  |                |
|------------------|----------------|
| When             | Setting        |
| Every 1 minute   | `* * * * *`    |
| Every 15 minutes | `*/15 * * * *` |
| Every 30 minutes | `*/30 * * * *` |
| Every 1 hour     | `0 * * * *`    |
| Every 6 hours    | `0 */6 * * *`  |
| Every 12 hours   | `0 */12 * * *` |
| Once a day       | `4 0 * * *`    |
| Once a week      | `4 0 * * 0`    |
| Once a month     | `4 0 1 * *`    |

Here is a diagram of the general crontab syntax, for illustration:

``` php
# +---------------- minute (0 - 59)
# |  +------------- hour (0 - 23)
# |  |  +---------- day of month (1 - 31)
# |  |  |  +------- month (1 - 12)
# |  |  |  |  +---- day of week (0 - 6) (Sunday=0)
# |  |  |  |  |
  *  *  *  *  *  command to be executed
```

Thus, the cron command example above means "ping <http://www.example.com/cron.php> at the zero minute on every hour of every day of every month of every day of the week."

### How Drupal uses cron

Every Drupal install requires regular actions to handle maintenance tasks such as cleaning up log files and checking for updates. Cron.php is the file that Drupal uses to run the maintenance process.

For instance, if your site were *[www.example.com](http://www.example.com)*, loading the URL *<http://www.example.com/cron.php>* in your browser would run the maintenance.

This page is automatically set up when you install Drupal. Simply loading the URL will run the maintenance. Nothing more is required.

### How to set up a cron job

Cron jobs are scheduled by setting up a "crontab." A crontab is a text file that contains the commands to be run. This file can be created and edited either through the command line interface, or, if you manage your website through a web-based control panel such as [cpanel](http://www.cpanel.net/support/docs/11/cpanel/advanced_cron_jobs.html), Plesk, or [Virtualmin and Webmin](/node/2526018 "Configuring cron jobs with Virtualmin and Webmin"), you will use the web interface.

In order to schedule your cron job in Plesk for Linux, go to Settings \> Scheduled Tasks in the General Group. Select the system user account on whose behalf the task will be executed (usually the domain ftp user). Click "Schedule New Task". Specify when to run your command. You can schedule the time using the UNIX crontab entry form as specified in this article. Then, specify which command to run, using the same format as specified in this article. Then, Click OK.

Otherwise, check with your hosting company for detailed instructions if you are using a web-based control panel.

To edit a crontab through the command line, type:

`crontab -e`

If this fails, see the [Troubleshooting Cron](#help) section below.

Add ONE of the following lines:

``` php
45 * * * *  /usr/bin/lynx -source http://example.com/cron.php 

45 * * * * /usr/bin/wget -O - -q -t 1 http://www.example.com/cron.php 

45 * * * * curl -s http://example.com/cron.php 
```

This would have a [lynx](http://lynx.isc.org/), [wget](http://www.gnu.org/software/wget/wget.html), or [curl](http://curl.haxx.se) visit your cron page 45 minutes after every hour.

Three options are provided in case either wget, lynx or curl are not installed on the server. Any will do the job well, except as noted below.

Note that the lynx option above is not working with https sites as recently as 7/4/2018. The test site is Drupal 8.5.3 hosted on Go Daddy/Linux, where a previously working cron job is no longer working after the site was switched from http to https. The server email message indicated: "lynx: Can't access startfile". The cron job was changed from the lynx option to the wget option and is operating as intended with Drupal's cron and Scheduler's lightweight cron (admin/config/content/scheduler/cron).

[Learn more about the crontab file syntax here](http://www.adminschoice.com/crontab-quick-reference) to set up the cron job to run more or less often.

There are many ways to configure a cron job. If you have full access to crontab features, you should be able to simply paste in one of the above example commands – *be sure to replace "example.com" with your own web domain or docroot*.

If you're on shared hosting, you should be able to find cron job configuration somewhere in your hosting control panel. Some hosts even have cron "wizards" that walk you through the cron configuration, making it much easier if cron is new to you. On a Windows system you can accomplish the same thing with scheduled tasks to launch Internet Explorer pointed to the URL.

Some hosting companies do not permit local loopback, so using wget, curl or lynx will not work. If this is the case, and they run PHP as a CGI (check with your hosting company to see if this is the case), the following will run the cron locally:-

`/usr/bin/php /home/sites/example.com/public_html/cron.php`

### Some hosting companies don’t allow access to cron

If your hosting company restricts access to cron, you have many options.

- Ask the company to give you access, or to set up a cron job for you
- Ask someone else with access to a server to set up a cron job for you. Any Unix, Linux, or Mac server with access to the internet can have a cron job to regularly visit your site. There are also some companies that offer cron services.
- Use the [Poor Man's Cron module](/project/poormanscron).
- Use webcron services like [EasyCron](https://www.easycron.com). You may find other providers of [cron job services](http://www.cronjobservices.com/). Many are free,but with restrictions.

Cron doesn't guarantee your commands will run at the specified interval. But Drupal will try its best to come as close as possible. The more you visit cron.php, the more accurate cron will be.  

### Troubleshooting cron jobs

Make sure your web site is **not** in maintenance mode.

If you receive a permission denied error after starting crontab -e, you may need to use sudo:

`sudo crontab -e`

You may need to adjust the path to wget, lynx or curl in your crontab. For example, the cron example listed above contains the line:

`45 * * * * /usr/bin/lynx -source http://example.com/cron.php`

However, Lynx may be in a different location on your server, or not installed at all. To find out where Lynx is installed, enter:

`whereis lynx`

or

`which lynx`

If it is not located at /usr/bin/lynx, adjust the path as needed. The same applies for wget and curl. If none are installed, ask a server administrator for help.

It may be necessary to change **<http://example.com/cron.php>** to the location of your Drupal installation. For example, if you have Drupal installed in a subdirectory, it might be <http://www.example.com/drupal/cron.php>).

### Example scripts

Drupal ships with two example scripts in the scripts directory, cron-curl.sh and cron-lynx.sh. You can call these scripts from cron as well:

`45 * * * * /home/www/drupal/scripts/cron-lynx.sh`

Note that the scripts will need to be updated with the path to your directory and URL.

### Running cron as an authenticated user (D6 and earlier only)

If triggering cron.php via the methods above, cron tasks will run as the anonymous user. For most cases this should be fine, but if Drupal cron has been customized to include tasks that must run as a certain site user (e.g. Custom logic has been implemented in hook_cron that requires special user permissions), the following script may be useful. This script authenticates a user of your choosing before calling cron.php.

Note that as of Drupal 7, cron *always* runs as an anonymous user, so this will not work in Drupal 7 and later versions!

Note that this script should be called instead of cron.php within your server's cron configuration and must be executable by appropriate system user on your server.

``` php
#!/bin/sh
# Reference http://drupal.org/node/479948#comment-1673488 by pearlbear

SITE=https://dev.example.com/
USERNAME=user.name
PASS=ChangeMe!!12

COOKIES=/tmp/cron-cookies.txt
WGETPARAMS="--quiet -O /dev/null --no-check-certificate --save-cookies $COOKIES --keep-session-cookies --load-cookies $COOKIES"
# if you run drupal in a default language different than English you need to modify this
LOGIN="Log%20in"

wget $WGETPARAMS "${SITE}user"
wget $WGETPARAMS --post-data="name=$USERNAME&pass=$PASS&op=$LOGIN&form_id=user_login" "${SITE}user"
wget $WGETPARAMS "${SITE}cron.php"
```

### Running Drupal cron tasks from Drush

Visit: <https://docs.drush.org/en/8.x/cron/>

### Hard-coding cron's "secret key"

The key at the end of the url is automatically generated on site install, if you want to give it a manual value, use the following indications :

#### Drupal 7

Edit settings.php :

    $conf['cron_key'] = 'your value';

#### Drupal 8

Use the following drush command:

    drush state-set system.cron_key foobar

### Security notes

It is possible to run cron.php directly via scripts/drupal.sh with Drupal 6. Drupal.sh allows a Drupal page to be executed from a shell script. To do so, add the following cron job to run as the Apache user:

`/full/path/to/drupal.sh --root /full/path/to/site/root/ http://default/cron.php`

Note that <http://default/cron.php> is NOT shown as an example, it should be used as is, without changes.

Taking this approach allows cron.php to be blocked to prevent remote access.

To block remote access to cron.php, in the server's .htaccess file or vhost configuration file add this section:

``` php
    <Files cron.php>
        Order Deny,Allow
        Deny from all
        Allow from localhost
        Allow from 127.0.0.1
        Allow from xx.xx.xx.xx <-- your IP address
    </Files>
```

If you take this approach and use drupal.sh to call cron.php, it is probably best not to use the root user to run the cron job. A non-privileged user account, or the Apache account user, for example http-service or www-data, is a better choice. To do so, call crontab -e when logged in as a non-privileged user, or for the Apache account on a Debian server, for example, you can add a user parameter:

`sudo crontab -e -u www-data`

The downside to this method is that any URLs generated by cron jobs using this method will not be properly formed, starting with "<http://default/>".

#### Multiple sites

If you run many sites, you can use this tip to make managing your cron jobs easier. To minimize the clutter, create an /etc/cron.5min directory and has crontab read this directory every five minutes.

`*/5 * * * * root run-parts /etc/cron.5min`

Then place multiple individual files into the /etc/cron.5min directory, one for each site. The files can be named "site1", "site2", etc. -- note that *run-parts* may fail to detect files which contain a dot (.) in their name. To make sure that all of your files are visible to cron, type this at a shell prompt:

`$ sudo run-parts --test /etc/cron.5min`  
and make sure that all of your files are listed.

Each of the files in /etc/cron.5min should contain one line:

`/usr/bin/lynx -source http://(full site URL)/cron.php > /dev/null 2>&1`  
or, alternatively, one of the *curl* or *wget* commands specified above.

If this doesn't work, try putting another line at the start of each file:

`#!/bin/sh`  
and make sure that the files are executable by doing

`$ sudo chmod u+x /etc/cron.5min/*`

For more information about using cron in a multisite configuration, see the [Multisite Cron](/node/237503) section of this guide.

#### SSL

When using SSL, add one additional argument when calling wget: --no-check-certificate. Do not put “--no-check-certificate” between the -0 and the -.

`45 * * * * /usr/bin/wget --no-check-certificate --quiet -O - https://example.com/cron.php`

#### Configuring an editor for cron

You can specify which text editor (emacs, vi, nano, etc.) you want to use to edit the crontab. If you want to change your editor permanently to nano, type:

`export EDITOR=nano`

If you want to use nano for just this time, type:

`env EDITOR=nano crontab -e`

#### Proxy

If your server is behind a proxy, you might need to add `--no-proxy` to the command. Also in the example below, the Shield module is used, with the username and password "login" and "login_pasword":

`05 * * * * /usr/bin/wget --no-proxy -O - -q -t 1 http://login:login_pasword@example.com/cron/CRON_URL`
