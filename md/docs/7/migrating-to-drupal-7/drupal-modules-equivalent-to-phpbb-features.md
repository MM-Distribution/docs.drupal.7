---
title: "Drupal modules equivalent to phpBB features"
source_url: "https://www.drupal.org/docs/7/migrating-to-drupal-7/drupal-modules-equivalent-to-phpbb-features"
page_type: page
last_updated: "Last updated on 11 April 2017"
published: "2006-04-16T07:24:03+00:00"
modified: "2017-04-11T06:42:15+00:00"
breadcrumb: ["Drupal 7", "Migrating to Drupal 7"]
fetched: "2026-10-21T06:53:00Z"
raw: "raw/docs/7/migrating-to-drupal-7/drupal-modules-equivalent-to-phpbb-features.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Drupal modules equivalent to phpBB features

Many people switching over from phpBB wonder if a native Drupal forum has the same functionality.

While a Drupal forum will never be the same as a phpBB forum, there exist numerous contributed modules that can do most of what phpBB does, and potentially more.

This page aims to list such modules so that a former phpBB admin can find their way more easily within the maze of Drupal modules.

This list is not exhaustive. It will be completed progressively. If you have any question that you would like to be answered within this page, then [open a support request within the phpbb2drupal project](http://drupal.org/node/add/project_issue/phpbb2drupal/support). You could also see [Adding functionality to your forum with contribs](http://drupal.org/node/227121).

## Forum Theming and integration

[Advanced Forum](http://drupal.org/project/advanced_forum) makes a more forum like style available for themes and also integration with many other modules for additional features.

## Thread splitting

This feature is not yet well supported within Drupal. There exist, however, a promising module prototype that would allow an admin to move a comment from one place to another, either within a thread or to another thread, or to create a new thread (new node).  
See the [Comment mover](http://drupal.org/node/57166) module.

## Private Forums

Currently, the best Drupal solution for having private forums (i.e. forums where only a specific 'role' - e.g. Moderators - can post and view the topics), is to use the [forum access](http://drupal.org/project/forum_access) module along with [Access Control Lists](http://drupal.org/project/acl). An alternative approach is to use [taxonomy access](http://drupal.org/project/taxonomy_access).

Concurrently, there is a feature request that would allow for the equivalent of private forums with only the Drupal core. See the [Make posting/viewing permission more granular](http://drupal.org/node/10426) issue.

## Private Messaging

[Privatemsg](http://drupal.org/project/privatemsg) is the module to use for Private messaging. The phpbb2drupal module also supports importing existing phpbb messages.

## Email notification

phpBB allows you to receive email notifications when a reply is posted to a thread.

Once again, a Drupal forum has no such feature out of the box, but a number of contributed modules give you alternative ways to achieve the same:

- [Comment notify](http://drupal.org/project/comment_notify) is a simple solution that works well. However there are also other options:
- [Comment RSS](http://drupal.org/project/commentrss): This module adds comment RSS serving capabilties to Drupal, which is suitable for some tracking of comments for your users.
- [Notify](http://drupal.org/project/notify): The notify module allows users to subscribe to periodic emails which include all new or revised content and/or comments much like the daily news letters sent by some websites.
- [Organic groups](http://drupal.org/project/og): Enable users to create and manage their own 'groups'. Each group can have subscribers, and maintains a group home page where subscribers communicate amongst themselves. Organic groups is a fairly complex module: it provides email notification of new content posted on each group, according to the user's settings, but it also gives you much more than that.
- [Subscriptions](http://drupal.org/project/subscriptions): This module enables users to subscribe to be notified of changes to nodes or taxonomies, such as new comments in specific forums, or additions to some category of blog. Once enabled, all nodes will have an additional link that allows the user to change their subscriptions. *This module is probably the closest to phpBB email notification feature.*

## Editing posts

There are scores of contribution modules that makes editing posts easier. [Browse the contribution modules for the most appropriate filter/editor for your site](http://drupal.org/project/Modules/category/63).

In particular:

- [BUEditor](http://drupal.org/project/bueditor): BUEditor allows you to add tagging buttons to the textarea without turning it into a fully featured wysiwyg.
- For Drupal 6 [Smileys](http://drupal.org/project/smileys) and for Drupal 7 [Smiley](http://drupal.org/project/smiley): These are both filters that substitute ASCII smileys with images.
- [Quote](http://drupal.org/project/quote): Adds a "quote" button below a post/comment, this then opens the edit form with the post/comment quoted, with quote mark-up.
