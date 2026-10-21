---
title: "Best practices"
source_url: "https://www.drupal.org/docs/7/site-building-best-practices/best-practices"
page_type: page
last_updated: "Last updated on 28 February 2025"
published: "2005-02-19T01:29:54+00:00"
modified: "2025-02-28T19:02:43+00:00"
breadcrumb: ["Drupal 7", "Drupal 7 site building best practices"]
fetched: "2026-10-21T07:10:03Z"
raw: "raw/docs/7/site-building-best-practices/best-practices.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Best practices

Setting up and maintaining a content management system (CMS) like Drupal takes both time and effort, following some basic best practices can protect that investment. These guidelines are merely suggestions, in the end, it is up to you to decide what is appropriate for your site.

The following list contains some quick pointers, links to more detailed best practices are listed at the bottom of this page.

- **Plan your initial site.** Drupal provides a good toolset to help you build your site, but you should still develop a plan. Choosing a good theme and a robust Drupal distribution can jump-start the setup process, but good wireframes and proper planning can help avoid significant misunderstandings and ensure those initial steps are in the right direction.
- **Back up your site.** Back up both the database and the files on the webserver. *Test your backups to ensure they will actually work when needed.* Create a secondary copy of the website and test restoring your backups to that secondary development environment.
- **Stay informed.** Be aware of the major Drupal upgrades that will apply to your website, including security releases to core and contributed modules.
- **Plan for the future.** You should regularly revisit and reevaluate your site structure and components to stay current with upgrades and security fixes. Create a secondary copy of the website to try out new major version releases of Drupal core and contributed modules for long term stability and optimization, and also to test patches that can resolve bugs and security issues over the short term. Plan to bring all website components up to date, establish a regular update cycle that makes sense for your situation.
- **Get involved in the community.** This will help you follow development trends and while helping others, you may just come across a cool idea that solves your own problem. It is also one of the best ways to help strengthen your Drupal skills.
- **Avoid using PHP snippets.** A PHP snippet entered by an unauthorized user can expose your entire website to attack. An outsider who gains PHP access to your site will be able to read and write anything that is in your database, and pretty much do anything they want. You should be careful not to grant permission to use the PHP format to anyone other than trusted site developers, and *disable the PHP module if you are not using it*. Drupal gives you a great deal of power and flexibility when using PHP code in blocks and content. Unfortunately, a stray character or a missing semi-colon breaks PHP. Drupal then attempts to evaluate this broken code on any requested page, the PHP interpreter chokes on it and therefore your whole site is broken. When creating a block that uses the PHP input format, you can avoid the risk of having the block take down your entire website by first testing the code inside a temporary story or page node. Use the PHP input format, write the code, and then Preview to debug your code. When you are satisfied that your code is working, copy then paste the code into the block.
- **Securing file permissions and ownership.** It is always preferred to configure server file systems with the minimal required file permissions, to run the application. For more on file permissions refer: <https://www.drupal.org/node/244924>
- **Comparing similar modules** instead of installing the first module you find. For example, when looking for a breadcrumbs solution a quick google search for "comparison of breadcrumb modules" will bring you these 2 very useful pages: <https://www.drupal.org/node/533448> and <https://groups.drupal.org/node/79839>

**If you're looking for advanced, programmer-type best practices, refer to the [Programming Best Practices](/node/287350 "Programming best practices | Drupal.org") pages.**
