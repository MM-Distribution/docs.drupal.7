---
title: "Enable submit via Enter key on Ajax forms"
source_url: "https://www.drupal.org/docs/7/theming/howto/enable-submit-via-enter-key-on-ajax-forms"
page_type: page
last_updated: "Last updated on 8 September 2016"
published: "2012-01-13T06:01:42+00:00"
modified: "2016-09-08T14:07:08+00:00"
breadcrumb: ["Drupal 7", "Theming Drupal 7", "Theming HowTos"]
fetched: "2026-10-21T08:50:27Z"
raw: "raw/docs/7/theming/howto/enable-submit-via-enter-key-on-ajax-forms.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Enable submit via Enter key on Ajax forms

See [first comment](http://drupal.org/node/1403614#comment-5468080) for alternative method.

Users often submit forms by pressing the Enter key while the cursor is positioned in a text field. This is a convenient feature to quickly submit a form from the place of last edit (especially on forms that are very long) instead of having to scroll down to the Save button, position the mouse over it and click. An issue I ran into with Drupal 7 is that this is no longer working in node forms, because of the extensive use of Ajax. The Enter key is pressed after editing a text field and nothing happens. After searching quite a bit, I found a solution:

add the following function to template.php, clear cache and then test it out:

``` php
function YOURTHEME_form_alter(&$form, &$form_state, $form_id) {
  if ($form_id == 'YOURFORMID') {
      $form['YOURINPUTNAME']['#attributes']['onkeypress'][]='if(event.keyCode==13){this.form.submit();}';
  }
}
```

This can be enabled for multiple inputs. As an example, if you are using the Garland theme and want to add the abitilty to submit the node form by pressing Enter in both the "Title field" and the "Authored by" field for a content type "Page" the code would look like this:

``` php
function garland_form_alter(&$form, &$form_state, $form_id) {
  if ($form_id == 'page_node_form') {
      $form['title']['#attributes']['onkeypress'][]='if(event.keyCode==13){this.form.submit();}';
      $form['name']['#attributes']['onkeypress'][]='if(event.keyCode==13){this.form.submit();}';
  }
}
```

If someone knows a better way of doing this, please add it. Also, if there is a way to generate attributes for all inputs of a certain class in a form (i.e. all inputs with class "form-text") it would be helpful to list that.

The only issue I have come accross is that pressing Enter key to submit with this technique is not properly registered with the [Content locking (anti-concurrent editing)](https://drupal.org/project/content_lock) optional module. You will receive a warning of you have "Use javascript to detect leaving the node form" enabled with that module.

Happy efficient form submitting :)
