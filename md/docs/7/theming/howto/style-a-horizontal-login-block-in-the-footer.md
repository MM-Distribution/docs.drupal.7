---
title: "Style a horizontal login block in the footer"
source_url: "https://www.drupal.org/docs/7/theming/howto/style-a-horizontal-login-block-in-the-footer"
page_type: page
last_updated: "Last updated on 8 September 2016"
published: "2008-05-17T15:11:33+00:00"
modified: "2016-09-08T14:07:13+00:00"
breadcrumb: ["Drupal 7", "Theming Drupal 7", "Theming HowTos"]
fetched: "2026-10-21T08:52:15Z"
raw: "raw/docs/7/theming/howto/style-a-horizontal-login-block-in-the-footer.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Style a horizontal login block in the footer

It's quite simple to restyle the standard user login block so it appears all on one line. You can then put it your footer, and it's out of the way on sites where most users don't need to (or can't) log in.

## Drupal 7

``` php
/**
 * User login block in footer.
 */
#block-user-login {
  margin: 2em auto;
  text-align: center;
}
#block-user-login .block-title {
  display: inline-block;
  margin-bottom: 0.5em;
  text-align: center;
}
#block-user-login .content * {
  display: inline;
}
#block-user-login .form-item {
  margin-left: 1em;
}
#block-user-login .form-actions {
  margin-left: 1em;
}
```

## Drupal 6

``` php
/**
* user login block in footer
*/
#block-user-0 {
  margin: 2em 0 1em;
}
#block-user-0 *
{
  display: inline;
  color: white; /* match the text colour of your theme here */
}
#edit-user-login-block {
  display:none; /* rehide hidden form element */
}
#block-user-0 h2 {
  font-size: 92%; /* match .content font size... change this for your theme */
}
#block-user-0 .form-item {
  margin-left: 1em;
}
```
