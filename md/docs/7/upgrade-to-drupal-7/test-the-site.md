---
title: "Test the site"
source_url: "https://www.drupal.org/docs/7/upgrade-to-drupal-7/test-the-site"
page_type: page
last_updated: "Last updated on 18 August 2016"
published: "2005-11-09T19:25:31+00:00"
modified: "2016-08-18T20:23:23+00:00"
breadcrumb: ["Drupal 7", "Upgrade to Drupal 7"]
fetched: "2026-10-21T06:20:18Z"
raw: "raw/docs/7/upgrade-to-drupal-7/test-the-site.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Test the site

Once your upgrade is complete, it is important to test your site for functionality and for potential problems that visitors to your site may see.

**I. Test your new version of Drupal**  
You should test your site to make sure it works. We recommend that you try the most common tasks your users do on the site. A good way to to see what your users like to do on your site is to review your site administration logs at  
**Administer \>\> Logs**.

For a more thorough review we recommend you review the administration help in your site at **Administer \>\> Help**. Each page of help documentation has links to the most important pages for each module.

**II. Prevent file not found errors**  
After you upgrade your site you should check your site for bad links, to prevent file not found errors. The http error number for these pages is 404. You can use a simple tool to check the links on your site. You will see errors in you Drupal Administrator logs as well as your web server error logs. Perform the following commands through the administrator menu on your site:

- Enable contributed image module  
  **Administer \>\> Site building \>\> Modules**
- Set permissions so images can be written for userid running link check.  
  **Administer \>\> User management \>\> Access control**
- Enable the menu module  
  **Administer \>\> Site building \>\> Modules**
- Disable the logout menu  
  **Administer \>\> Site building \>\> Menus**

From a command line on a computer connected to the Internet run wget with the following options:

The cookie this command is referring to is the cookie downloaded from your browser when you last logged into your Drupal site as an admin.

`wget -r --delete-after --cookies=off --header='Cookie: PHPSESSID=xxx' http://example.com`

-r to recursively crawl the site. --delete-after, --cookies=off tells the crawler not to use a cookie. --header=’Cookie: PHPSESSID=XXXX’ tells the Drupal site that session information will be passed in the http header. This should be repeated 2 more times; once for a regular userid, and once for an anonymous userid. After the link check is done check your Drupal admin logs and your webserver error logs. Look in your browser preferences to see what cookies you have for your URL.

**III. Invite users to test**  
Your users are your best source of feedback. They will tell you quickly which parts of your site are not working like they expect them to. Send an email informing users that your test site is available for them and instruct them how to give feedback. You may wish to install the [feedback module](http://drupal.org/project/feedback) to assist with user feedback.
