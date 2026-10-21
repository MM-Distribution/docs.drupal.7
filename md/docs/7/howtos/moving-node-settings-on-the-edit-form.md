---
title: "Moving node settings on the edit form"
source_url: "https://www.drupal.org/docs/7/howtos/moving-node-settings-on-the-edit-form"
page_type: page
last_updated: "Last updated on 26 January 2018"
published: "2014-10-08T06:06:26+00:00"
modified: "2018-01-26T00:09:18+00:00"
breadcrumb: ["Drupal 7", "Site building and development HowTos for Drupal 7"]
fetched: "2026-10-21T08:07:14Z"
raw: "raw/docs/7/howtos/moving-node-settings-on-the-edit-form.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Moving node settings on the edit form

Drupal 7, together with [Display Suite](/project/ds) forms and the [Fieldgroup module](/project/fieldgroup), gives developers the awesome ability to group fields together in snazzy formats like Horizontal- and Vertical tabs, Accordions, Multipage groups, etc.

That's enough to make you salivate and will make your users love you!

Unfortunately, this little field group sits stubbornly at the bottom of the form, with no representatives on the manage fields page (except the path URL alias option that does nothing on the form, at least on my install):

![ Menu settings, URL path settings, Revision information, Authoring information and Publishing options](/files/fieldset_2.png)

Time to despair? NO!

**Create a custom field group to hold your stubborn tabs**, say with machine name "group_adv_vert". You can also create multiple groups and split them up if you'd like (I've used "group_wizard" as the other group in the example below).

Now, within your custom module or theme, implement [hook_form_FORM_ID_alter](https://api.drupal.org/api/drupal/modules%21system%21system.api.php/function/hook_form_FORM_ID_alter/7) like so:

``` php
function MY_MODULE_OR_THEME_NAME_form_FORM_ID_alter(&$form, &$form_state, $form_id){

    // Move the Menu tab:
    $form['#group_children']['menu'] = 'group_wizard';
    $form['menu']['#group'] = 'group_wizard';

    // Move the Author tab:
    $form['#group_children']['author'] = 'group_adv_vert';
    $form['author']['#group'] = 'group_adv_vert';
    $form['author']['#weight'] = 0; // Just to change the order within this new group, not required

    // Move the Publishing options tab:
    $form['#group_children']['options'] = 'group_adv_vert';
    $form['options']['#group'] = 'group_adv_vert';
    $form['options']['#weight'] = 1; 

    // Move the Revision tab:
    $form['#group_children']['revision_information'] = 'group_adv_vert';
    $form['revision_information']['#group'] = 'group_adv_vert';
    $form['revision_information']['#weight'] = 2;

    // Path is a little MORE stubborn, so we have to change its grouping after the form is built:
    $form['#after_build'][] = 'MY_MODULE_OR_THEME_NAME_after_build';

    // And very importantly, hide the original containing group of these now moved tabs 
    // (otherwise path alias will render twice, for some reason)
    // You can use this same method to more or less safely hide other form fields too 
    $form['additional_settings']['#access'] = false;

}

function MY_MODULE_OR_THEME_NAME_after_build($form, &$form_state){

    // At last, the incredibly stubborn URL alias settings are finally moved
    $form['#group_children']['path'] = 'group_adv_vert';
    $form['path']['#group'] = 'group_adv_vert';

    return $form;
}
```

Now go make form sushi!
