---
title: "Getting started with Drupal 7 administration"
source_url: "https://www.drupal.org/docs/7/administering-drupal-7-site/getting-started-with-drupal-7-administration"
page_type: page
last_updated: "Last updated on 29 September 2018"
published: "2010-01-06T04:54:11+00:00"
modified: "2018-09-29T06:30:58+00:00"
breadcrumb: ["Drupal 7", "Administering Drupal 7 site"]
fetched: "2026-10-21T05:58:36Z"
raw: "raw/docs/7/administering-drupal-7-site/getting-started-with-drupal-7-administration.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Getting started with Drupal 7 administration

This section is an introduction to site administration for new Drupal 7 users. It covers the use of the administrator account and offers suggestions on where to start.

## Understanding the administrator account

At the end of the installation process, the person who performed the installation is automatically logged in to the site with the administrator account. You may see the administrator account referred to as User 1. This administrative account is automatically given all privileges for managing content and administering the site. The best practice is to only give a developer or the highest level of site admin access to this account. You can always grant users permission by assigning them to certain roles, so there is no reason to share this account.

## Where to start

Here are some starting points for what you can do following installation:

1.  **Check your site's status:** Navigate to the *Status report* page by going to *Reports \> Status report* through the administration toolbar at the top of the page to get an overview of your site's current status. Items with a red background are issues that need immediate attention (see [Reports](/getting-started/admin/reports) for more information). An example of this would be a required security update for Drupal core or an installed module, or an unprotected settings.php file (see [Securing file permissions and ownership](https://www.drupal.org/node/244924) for more information). The Status report page may also indicate that "Cron has not run" and give you an option for running it manually. Cron.php is a script that needs to be run regularly for your site to continue to function properly. See [Configuring cron jobs](http://drupal.org/cron) for information on how to have your system automatically run the cron script.
2.  **Configure your site information:** You can change basic settings, such as the site name, slogan, e-mail address, or the default front-page path, by navigating to the Site Information page (*Administer \> Configuration \> System: Site information* or `http://example.com/admin/config/system/site-information`).
3.  **User management:** To add new users or manage existing users, go to the *People* page (*Administer \> People* or `http://example.com/admin/people`. You can manage user roles and permissions by clicking on the "Permissions" tab on this page. To change the process by which users apply for accounts, visit the "People and Permissions" page (*Administer \> Configuration \> People: Account settings* or `http://example.com/admin/config/people/accounts`). Please see the [Users, Roles, and Permissions](/node/120614) page for more information on this topic.
4.  **Add additional functionality:** Modules can be used to add extra features to Drupal. The standard Drupal installation comes with a number of modules that are ready to be enabled. In addition, you can download community-contributed modules to add even more features. Navigate to the *Modules* page (*Administer \> Modules* or `http://example.com/admin/modules`) to administer the modules that were included. Additional modules can be found in the [Modules section](/project/Modules) of Drupal.org. Please see the [Installing contributed modules (Drupal 7)](/node/895232) page for more information on this topic.
5.  **Customizing the site appearance:** You can change the site's appearance by installing new themes or editing theme settings by navigating to the *Appearance* administration page (*Administer \> Appearance* or `http://example.com/admin/appearance`). Visit [Adding Modules and Themes](/node/120641) in the Drupal Cookbook for more information on how to add themes, or take a look at the [Theming Guide](/theme-guide) if you are interested in creating your own custom theme.
6.  **Posting content:** By default with a regular installation, Drupal 7 has two content types enabled. "Articles" are generally used for posting frequently updated content (for example, to the front page). The "Basic page" content type is generally used for creating the equivalent of static pages (more permanent site pages). Navigate to the "Content" administration page (*Administer \> Content* or `http://example.com/admin/content`), then click the "Add new content" link to add content to the site. You can also define your own content types by clicking the "Add content type" link at the top of the Content types administration page (*Administer \> Structure \> Content types* or `http://example.com/admin/structure/types`). Visit the Drupal Cookbook page on [Creating content](/node/120635) for more details.

Below are additional articles on navigating specific aspects of Drupal 7's user interface.
