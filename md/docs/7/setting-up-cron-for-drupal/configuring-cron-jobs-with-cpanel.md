---
title: "Configuring cron jobs with cPanel"
source_url: "https://www.drupal.org/docs/7/setting-up-cron-for-drupal/configuring-cron-jobs-with-cpanel"
page_type: page
last_updated: "Last updated on 5 August 2016"
published: "2009-02-04T19:59:51+00:00"
modified: "2016-08-05T14:28:27+00:00"
breadcrumb: ["Drupal 7", "Setting up cron for Drupal 7"]
fetched: "2026-10-21T06:26:46Z"
raw: "raw/docs/7/setting-up-cron-for-drupal/configuring-cron-jobs-with-cpanel.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Configuring cron jobs with cPanel

cPanel controls domains and has an option to configure cron jobs. Here is everything you need to configure cron jobs in cPanel.

cPanel formats pages based on styles. This document is based on the sundaymorning style. The location of options might vary if you use a different style. You can change the style using the Change Style option in cPanel. In the sundaymorning and Crimson smoke themes, you select Advanced then Cron jobs.  
![Part of the cPanel main screen showing the advanced section containing the cron jobs icon](/files/Configuring%20cron%20jobs%20in%20cPanel%20Advanced.png)

WHM, Web Host Manager, is the cPanel product for controlling domains in a Virtual Private Server. If there is no cron option in your cPanel, you may have to add cron in WHM. Cron may be in different places in the various Cpanel themes.

You may be offered the option of standard or an “advanced” Unix style user interface. You may see an error message similar to the following.  
`/usr/bin/crontab permissions are wrong. Please set to 4755`

The Unix style interface dumps you in a page where you can enter a command the same as described on the main Configuring cron jobs page.

The standard page lets you select the number of minutes, hours, days, or months from selection lists and add the final part of the command.

The following image shows the add new cron job section of the cron page including the drop down selection boxes and the final text box for your command. Some of the boxes are explained next.

![The cPanel cron jobs screen showing the add new cron job section](/files/Configuring%20cron%20jobs%20in%20cPanel%20Add%20new%20cron%20job.png)

The Common Settings drop down lets you select every hour, every day, and other useful options. Select `Once a day (0 0 * * *)` as an example. That sets the minute and hour options to zero indicating midnight. The same selection sets day, month, and weekday to \* to indicate every day of every month on every day of the week.

You can then change the minute or hour to a less busy time. For example, some Australian sites are busy at midnight handling requests from America where it is the start of the business day.

An easy way to start the Drupal cron job is to execute the file in some way. Lynx is a text based Web browser that accepts a URL as a parameter. You can start Lynx from cron and specify the Drupal cron job in the source parameter.

The following image shows the final command to run `/usr/bin/lynx` every day at 6 am using `http://petermoulding.com/cron.php` as the source. This makes the Web server at <http://petermoulding.com/> execute cron.php. Cron.php is the Drupal cron command.

![The cPanel cron jobs screen showing the command section](/files/Configuring%20cron%20jobs%20in%20cPanel%20command.png)

The following image shows the command in the edit option. You can see the relationship between the components of the command and the previously mentioned drop down boxes.

![The cPanel cron jobs screen showing the command in the edit option](/files/Configuring%20cron%20jobs%20in%20cPanel%20edit.png)

## Drupal 7

For Drupal 7 you have to add a security string as specified in a Drupal 7 administration page. Go to `Administration › Reports › Status report` and look for a string similar to the following example. Use the full string in the cPanel cron command box.  
`http://example.com/cron.php?cron_key=DH7AVdT0uGeN-WfZLkgfutDfDeYrqELjjTZrnulm3RY`

Drupal 7 also includes a reworked [Poormanscron](http://drupal.org/project/poormanscron) at `Administration › Configuration › System › Cron`. Poormanscron only works when people visit your Web. Low activity Web sites still need the cron in cPanel.

Poormanscron gives you limited control of when cron runs, you can say once per day but not when, sending you back to the cPanel cron if want to restrict the cron activity to a specific time range. In this case you have to set the Drupal cron to `never` so there is no cron activity outside of your cPanel cron.

## Many Web sites on one server

When you have many Web sites on one server, you might want to spread the cron jobs out by a few minutes to reduce the concentration of activity. I have cron jobs separated by 3 minutes from midnight until 6:00 am.

You can look in your activity logs to pick the best time. cPanel offers Webalizer, Awstats, and Analog with Webalizer as the default. Look at the activity for the Web site where the Drupal cron.php runs, not the site where cron runs. Cron performs very little work. Cron.php does the hard work.

## Lynx or Wget or Curl

The Web site for Lynx is <http://lynx.isc.org/>. The Web site for Wget is <http://www.gnu.org/software/wget/>. Lynx is a Web browser and does not require parameters to read cron.php. Lynx is the easiest way to activate cron.php but Lynx is not installed by default in all versions of Linux.

Some people use wget. Wget is installed by default in Ubuntu Linux. Wget gets files and needs special parameters to get a Web page. Note that wget is not semantic. The decorative upper case `-O` is a different option to the regular case `-o`.

`-O -` tells wget where to put the output file and the second dash, `-` tells wget the output location is the screen. This complicated non semantic option specification makes wget behave the same as the default lynx. If you do not use the `-O -`, you have to specify a location for the retrieved file and make sure the location has the right permissions.

Linux and Unix have a waste bin named `/dev/null`. `-O /dev/null` tells wget to send the output to be discarded.

`-q` tells wget to be quiet and not produce messages.

`-t 1` means retry once if the first request times out. The default without the t option is 20 retries. `-t 0` can send wget into an infinite loop retrying if the requested URL is missing.

The result is:  
`wget -O /dev/null -q -t 1 http://example.com/cron.php?cron_key=DH7AVdT0uGeN-WfZLkgfutDfDeYrqELjjTZrnulm3RY`

Curl is installed by default in Ubuntu Linux. Use Curl in the following way.  
`curl "http://example.com/cron.php?cron_key=DH7AVdT0uGeN-WfZLkgfutDfDeYrqELjjTZrnulm3RY"`

## One Web site

cPanel can control many Web sites. If you only have one Web site, you can try this approach as suggested by [Lamcraft](/user/1237716). Instead of using the command `http://example.com/cron.php`, you can use the file path `php /home/example/public_html/cron.php`.

This approach works because there is only one Web site, one settings.php file, and one database. Drupal cron.php will default to that Web site. If you use Drupal multisite or the Domain module, cron will run for only the one site and you have to use the `http://example.com/cron.php` for all the other sites.

`php` tells Linux to run the specified file as a PHP command line execution (CLI mode). `/example/` is the directory set up for your account. `/public_html` may be `/www` if your account is on Red Hat or Fedora Linux.

## Developing cron jobs

Are you developing modules that use hook_cron() to perform work during cron jobs? You might be interested in the following notes.

### Semiclean

Semiclean, <http://drupal.org/project/semiclean>, can reset the cron runtime date/time indicator Drupal uses to stop cron running multiple times.

### Long running cron jobs

Poormanscron and the Drupal 7 equivalent run frequently. There is code to stop them running twice at the same time. Regular cron is safer because you can tell it to run just once every hour or day. What happens when you have to run one cron job every 5 minutes, perhaps a stock update, and another cron job runs once per day, perhaps a stock analysis, and lasts for 20 minutes?

Cron.php should run every 5 minutes until the long running cron job starts then cron should stop running new cron jobs until the long running job finishes. You miss out on the 5 minute stock updates until the 20 minute stock analysis is finished.

You could set up the long running job as a separate cron job. You could have sites/all/modules/stock_analysis/stock_analysis_cron_job.php as a separate job fired by a separate cron job in cPanel. You would write stock_analysis_cron_job.php in a similar way to writing Web services. The services module has documentation on writing services, <http://drupal.org/node/113697>, and an independent cron job is just a Drupal style Web service that does not need input.
