---
title: "Making a Guestbook, a Gallery, a Status Wall, Chat Room ..."
source_url: "https://www.drupal.org/docs/7/howtos/making-a-guestbook-a-gallery-a-status-wall-chat-room"
page_type: page
last_updated: "Last updated on 26 January 2018"
published: "2011-04-28T16:31:22+00:00"
modified: "2018-01-26T00:06:25+00:00"
breadcrumb: ["Drupal 7", "Site building and development HowTos for Drupal 7"]
fetched: "2026-10-21T08:06:42Z"
raw: "raw/docs/7/howtos/making-a-guestbook-a-gallery-a-status-wall-chat-room.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Making a Guestbook, a Gallery, a Status Wall, Chat Room ...

If you are already using the following modules, you can easily make a guestbook or an <http://drupal.org/project/facebook_status> alternative without additional modules.

You need:  
<http://drupal.org/project/panels>  
<http://drupal.org/project/content_profile>  
<http://drupal.org/project/page_manager_redirect>  
<http://drupal.org/project/panels_tabs>  
<http://drupal.org/project/comment_upload> if you need photos

1\. Create a content type guestbook  
2. Make this content type a content profile node  
3. Make a mini Panel with user context showing only comments and comment form for this content type  
5. Place the mini panel in the user panel and make the setting as Tab - <http://drupal.org/project/panels_tabs>  
4. Make a Redirect Panel <http://drupal.org/project/page_manager_redirect> which redirects to the user's profile when someone  
wants to view a node of that type to the corresponding tab e.g. [http://www.example.com/user/%author:uid#guestbook](http://www.example.com/user/%author:uid#guestbook)  
5. activate <http://drupal.org/project/comment_upload> if you want to attach photos to a comment

The principle is that guestbook entries or facebook statuses are comments.

What do you think?

I am sure there are other ways as well. The good thing about the above approach is that you can do very complex visibility rules within panels using UR relationship, OG, Context ...

An example <http://www.global50plus.at/pfeifenmacher-david-wagner#g-stebuch>

The comment form is hidden for anonymous users, but comments are visible.
