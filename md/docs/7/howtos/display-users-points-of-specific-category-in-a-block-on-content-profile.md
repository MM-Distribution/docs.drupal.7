---
title: "Display User's Points of Specific Category in a Block on Content Profile"
source_url: "https://www.drupal.org/docs/7/howtos/display-users-points-of-specific-category-in-a-block-on-content-profile"
page_type: page
last_updated: "Last updated on 1 November 2016"
published: "2013-03-16T21:19:38+00:00"
modified: "2016-11-01T16:31:17+00:00"
breadcrumb: ["Drupal 7", "Site building and development HowTos for Drupal 7"]
fetched: "2026-10-21T08:03:52Z"
raw: "raw/docs/7/howtos/display-users-points-of-specific-category-in-a-block-on-content-profile.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Display User's Points of Specific Category in a Block on Content Profile

Modules used:

- Content Profile
- UserPoints
- Views 3
- Views Custom Field (or Views PHP)

Enable the listed modules and set up Content Profile as usual.

Create a Node View and add the argument Node: Title. Choose "Provide default argument", then "User ID from URL". Add a field from the group "Customfield" and select "Customfield: PHP code". For the Value, copy & paste the following:

``` php
if (arg(0) == 'user' && arg(1)) {
    $account = user_load((int) arg(1));
    $uid  = $account->uid;
    $up = userpoints_get_current_points($uid, 1);
    print $up;
}
```

Where it says "userpoints_get_current_points(\$uid, 1);", the number "1" is the taxonomy ID of the UserPoints category you want to display.  
Add the filter "Content Type" and select your Content Profile type.

Add a Block display, then save and head to the Blocks page.

On the Blocks page, edit the view you just created and choose "Show if the following PHP code returns TRUE", and copy & paste this code:

``` php
if ((arg(0) == 'user') && is_numeric(arg(1)) && (arg(2) == NULL)) {
   return TRUE;
}
else {
   return FALSE;
}
```

Place the block in a region, and you're done!

Note: To add more than one category, you don't have to add a new field for each one. Just add more categories by copying this part of the code:

``` php
    $up = userpoints_get_current_points($uid, 1);
    print $up;
```

and change the category number "1" to the term ID of each of the categories you want to display and change the variable "\$up" to "\$up1", "\$up2", or whatever. To find the term ID of the UserPoints category, I just hover over the edit link for each term.
