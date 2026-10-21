---
title: "Subscribe a user to specific OG group using Rules"
source_url: "https://www.drupal.org/docs/7/howtos/subscribe-a-user-to-specific-og-group-using-rules"
page_type: page
last_updated: "Last updated on 1 November 2016"
published: "2014-07-18T17:40:13+00:00"
modified: "2016-11-01T16:31:15+00:00"
breadcrumb: ["Drupal 7", "Site building and development HowTos for Drupal 7"]
fetched: "2026-10-21T08:07:29Z"
raw: "raw/docs/7/howtos/subscribe-a-user-to-specific-og-group-using-rules.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Subscribe a user to specific OG group using Rules

The following export is from pandaPowder's comment in OG issues:  
<https://www.drupal.org/node/1944508#comment-7738077>

Works with OG 7.x-2.7 and Rules 7.x-2.7

Use the Import function of Rules (<http://domain.com/admin/config/workflow/rules/reaction/import>)and paste the code below. You can then modify to your group name and ID.

``` php
{ "rules_start_first_course_on_create" : {
    "LABEL" : "Start First Course  on create",
    "PLUGIN" : "reaction rule",
    "TAGS" : [ "groups" ],
    "REQUIRES" : [ "rules", "og" ],
    "ON" : [ "user_insert" ],
    "DO" : [
      { "variable_add" : {
          "USING" : { "type" : "node", "value" : "71" },
          "PROVIDE" : { "variable_added" : { "foundation_course" : "Foundation Course" } }
        }
      },
      { "og_subcribe_user" : { "user" : [ "account" ], "group" : [ "foundation-course" ] } }
    ]
  }
}
```

This simple export helped tremendously because I was getting lost in the weeds of Rules and took me two days of Google-ing to find.
