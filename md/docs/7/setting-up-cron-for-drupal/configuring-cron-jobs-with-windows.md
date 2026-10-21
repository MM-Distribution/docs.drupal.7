---
title: "Configuring cron jobs with Windows"
source_url: "https://www.drupal.org/docs/7/setting-up-cron-for-drupal/configuring-cron-jobs-with-windows"
page_type: page
last_updated: "Last updated on 19 December 2016"
published: "2005-09-18T00:36:30+00:00"
modified: "2016-12-19T06:40:25+00:00"
breadcrumb: ["Drupal 7", "Setting up cron for Drupal 7"]
fetched: "2026-10-21T06:26:30Z"
raw: "raw/docs/7/setting-up-cron-for-drupal/configuring-cron-jobs-with-windows.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Configuring cron jobs with Windows

To setup a Windows machine to run cron.php at a specific time follow the specific instructions below. This can be useful if you are not familiar with Linux/Unix, or if your web host does not offer the ability to run cron jobs; you can run them remotely from your own computer.

Note: These instructions were written for Windows XP but should be similar in other versions of Windows.

**Creating a Scheduled Task**

1.  Open Scheduler
2.  Go to **Start \> Programs \> Accessories \> System Tools \> Scheduled Tasks**
3.  Double-click **Add Scheduled Task**
4.  The Scheduled Task Wizard will appear. Click **Next**.
5.  Select the program to run. Choose your ***browser*** from the list (for example, Internet Explorer or Mozilla Firefox). Click **Next**.
6.  Give the task a **Name**, such as *Drupal Cron Job*, and choose the Frequency with which to perform the task (for example, **Daily**)). Click **Next**.
7.  Choose specific **date and time options** (this step will vary, depending on the option selected in the previous step). When finished, click **Next**.
8.  Enter your **password** if prompted. Change the **username** if required (for example, you'd like the task to run under a user with fewer privileges security reasons). Click **Next**.
9.  On the final page, select the checkbox **Open advanced properties for this task when I click Finish** and click **Finish**.

**Configuring the task**

1.  Go to the task's setting page either by checking the checkbox at the end of the last step, or by double-clicking on the task.
2.  In the **Run** box, after the text that is there now (for example, *C:\PROGRA~1\MOZILL~1\firefox.exe*), enter a space and then type the address of your website's cron.php page in double quotations (for example, **C:\PROGRA~1\MOZILL~1\firefox.exe <http://www.example.com/cron.php>**
3.  To set a frequency more often than Daily (for example, hourly), click the **Schedule** tab, then click **Advanced**. Here you can set options such as **Repeat** task, every **1 hour** for **23 hours**. Click **Ok,**when finished.
4.  Change the **start time** on the task to **one minute of the current time**. This will allow you to test the task and make sure that it is working.
5.  When all settings have been configured to your liking, click **Apply** and **OK** (note: you may be prompted for your password)

**Command-line version**

Another way to perform the above commands is by using the **[schtasks](http://www.microsoft.com/resources/documentation/windows/xp/all/proddocs/en-us/schtasks.mspx?mfr=true)** (or **at** in Windows 2000) command from the command line. To duplicate the example above, which runs Firefox hourly to execute <http://www.example.com/cron.php>, open a command prompt (**Start \> Programs \> Accessories \> Command Prompt**) and enter:

`schtasks /create /tn "Drupal Cron Job" /tr "C:\PROGRA~1\MOZILL~1\firefox.exe http://www.example.com/cron.php" /sc hourly`

Enter your password if prompted.

**Using wget for Windows to run cron**

If for whatever reason you'd rather not deal with a browser window popping up on the machine, you can use wget, the Windows port of which works more or less the same as it does in UNIX. curl and lynx also has windows ports, but wget is probably the easiest to set up and use.

Grab a copy of wget from your choice of either [the author's site](http://www.christopherlewis.com/WGet/WGetFiles.htm) or from [SourceForge](http://gnuwin32.sourceforge.net/packages/wget.htm). Install it to the location of your choice.

Follow the steps for **Creating A Scheduled Task** above, except select wget.exe as the program to run (you may need to click the Browse button to locate it if you installed from a .zip file, for example). When you get to the Advanced Properties dialog, paste in the following after the program path:

`-O - -q -t 1 http://www.example.com/cron.php`

Adjust the rest of the options as described above and test it.

**Using curl with cmd.exe in Windows 7 (or Vista) with Task Scheduler**

- Start Computer Management (Windows Key, right-click Computer, select Manage...)
- In the right column, select **Create Job...**
- Fill in **General** tab.
- Under **Triggers** tab, select **New...**, then set the desired schedule, with a repeat set in Advanced Options.
- Under **Actions** tab, select **Start a program**, the program is CMD.EXE. For the optional argument, enter **/C "curl \[link provided on the status report page\]".**

If you have already installed [mysysgit](http://code.google.com/p/msysgit/downloads/list), curl is already present and in the path.

**Under Windows 7 (or Vista), using schtasks and curl**

Assuming you have already installed [mysysgit](http://code.google.com/p/msysgit/downloads/list) as described above...  
Run cmd.exe as Administrator, then enter the command:

``` php
C:\Windows\system32>schtasks /create /sc HOURLY /tn DevCron /tr "cmd.exe 'curl -
-silent --compressed http://[[hostname]]/cron.php?cron_key=VOYz8P63mnytd0mHVwFE
1jrXfRfNYU9KZiKB1Ou1Rh8'" /ru SYSTEM
```

Where \[\[hostname\]\] is the TLDN to the document root, /tn is the task name desired (here it's DevCron).

The above command yields a job that will run every hour, indefinitely.

**Using external webcron service**

If anyone finds above methods hard to manage, an easier way to schedule repeatedly executed tasks is using webcron service (e. g. [EasyCron](https://www.easycron.com)). Just via a browser, you can set up a webcron and it will periodically trigger your script.
