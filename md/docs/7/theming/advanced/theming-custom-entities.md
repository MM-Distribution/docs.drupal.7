---
title: "Theming Custom Entities"
source_url: "https://www.drupal.org/docs/7/theming/advanced/theming-custom-entities"
page_type: page
last_updated: "Last updated on 30 November 2019"
published: "2011-08-03T20:09:58+00:00"
modified: "2019-11-30T11:00:13+00:00"
breadcrumb: ["Drupal 7", "Theming Drupal 7", "Advanced theming"]
fetched: "2026-10-21T08:17:03Z"
raw: "raw/docs/7/theming/advanced/theming-custom-entities.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Theming Custom Entities

There are three pieces, or more specifically functions, that are required to theme the output of a custom entity: hook_menu(), Page Callback, and the MODULE_theme() Hook.

## hook_menu()

In order to access our entities, Menu paths must be created for tasks such as adding, editing, viewing and deleting entities. Adding, Editing and Deleting entities are related to Drupal's Forms API and beyond the scope of this tutorial. While these other menu definitions are required, we will focus solely on the menu definition for the 'view' task.

The hook_menu() allows us to define the path necessary to view a particular entity, the callback function that handles the request, the page title and the access requirements (amongst others).

See also: [hook_menu()](http://api.drupal.org/api/drupal/developer--hooks--core.php/function/hook_menu/6)

In the code below, pay particular attention to the page callback key/value pair. This entry in the array tells Drupal that requests for <http://mysite.com/my_entity/>\$my_entity_id should be handled by the function my_entity_page_view. Drupal will simply hand the request off to this function along with the variables we specify.

``` php
<?php
/**
 * Implements hook_menu().
 * Defines the menu callback for viewing our entity. Note that 
 * 'page callback' will point to a function name in our module. 
 * When a user requests the "my_entity/$my_entity_id" path 
 * (e.g., http://mysite.com/my_entity/1), Drupal sees the 
 * '%my_entity' wildcard and loads the entity by calling 
 * my_entity_load($my_entity_id). Then Drupal calls this 
 * callback and sends the loaded entity as a first argument.
 */
function my_module_menu() {
  $items['my_entity/%my_entity'] = array(
    'title callback'   => 'my_entity_page_title',
    'title arguments'  => array(1),
    'page callback'    => 'my_entity_page_view',
    'page arguments'   => array(1),
    'access arguments' => array('view entities'),
    'type'             => MENU_CALLBACK,
  );
  return $items;
}
?>
```

## Page Callback

In the my_module_menu() hook above, we indicated that requests to view an individual entity will be handled by a callback named my_entity_page_view. Now we need to define that callback. The code below is pretty simple and most of what you see is comments that explain what each section of the code does.

The code takes the entity identified by \$my_entity_id as the first argument and the view mode (full or teaser) as the second. Drupal will pass the view mode argument and you can use its value to make decisions about what to display and how to display it but for now we will ignore it for the sake of simplicity. What we really want to understand is how to tell Drupal to use a custom template file to theme the output of the entity.

The first section of the code sets the \$my_entity-\>content property to an empty array to clear out any previously rendered content. This property is where the what gets rendered in the template will be stored. In other words, this is the Render Array that Drupal will use to build the output of the entity.

In the middle section of the code, we use Drupal's hooks to add any custom fields to the entity. When you add fields to an entity through the Admin GUI, this is the code that retrieves the field definitions and their values and attaches them to the entity for display. During this step, the output for the fields is rendered and stored in the \#markup property of the field. It is possible to create custom templates for the output of each field but an explanation of how to do so is beyond the scope of this article.

And finally, in the last section of the code, we tell Drupal which template file to use to render the output of the entity. By default, Drupal will use the BLOCK template to theme the output. We need to over-ride the default and point Drupal to the name of our custom template. It is not necessary to indicate the full path or full name of the file. Drupal can figure that out on its own. We simply point to the theme in the Theme Registry we wish to use.

It is important to note that the order in which these tasks are performed appears to be important. The fields must be rendered and attached to the entity *before* the theme is specified.

``` php
<?php
/**
 * This is the callback we defined to be executed when a user 
 * requests http://mysite.com/my_entity/1 (1 is just an example ID, 
 * it could be anything). This function will set up the data and 
 * prepare the render array(s). You will specify the template to 
 * use in this callback. The critical thing to note below is the 
 * order in which field_attach_prepare_view, entity_prepare_view 
 * and field_attach_view are called. These functions must be called 
 * in this order and they must be called before you specify which 
 * theme to use.
 */
function my_entity_page_view($entity, $view_mode='full') {
  $entity_type = $entity->entityType();
  $entity_id = entity_id($entity_type, $entity);

  //
  // Remove previously built content, if exists
  //
  $entity->content = array();

  $entity->title = filter_xss($entity->title);

  //
  // Build the fields content
  //
  field_attach_prepare_view($entity_type, array($entity_id => $entity), $view_mode);
  entity_prepare_view($entity_type, array($entity_id => $entity));
  
  $entity->content += field_attach_view($entity_type, $entity, $view_mode);
 
   // Specify the theme to use and set the #element. Note that the key 
   // you use to pass the entity object must match the key you set in the 
   // variables in my_module_theme(). So in the case below, we use the key 
   // named #element because in my_module_theme() we set the following code:
   //
   // array(
   //   'my_entity' => array(
   //     'variables' => array('element' => null),
   //     'template' => 'my_entity'
   //   ),
   // );
   //
  $entity->content += array(
    '#theme'     => $entity_type,
    '#element'   => $entity,
    '#view_mode' => $view_mode,
    '#language'  => LANGUAGE_NONE,
  );
  
  return $entity->content;
}
?>
```

## MODULE_theme() Hook

So far we have defined the menu item path and callback for our entity. The only two pieces remaining are to create an entry in the Theme Registry which points to our template, then to create the template file.

The function below implements the MODULE_theme() hook to create this module's Theme Registry entries. The array that is returned has as its keys, the name of the Theme Registry entry, which must match the value specified in:

``` php
<?php
$entity->content += array(
  '#theme' => 'my_entity'
);
?>
```

``` php
<?php
/**
 * Adds our theme specifications to the Theme Registry.
 */
function my_module_theme($existing, $type, $theme, $path) {
  return array(
    'my_entity' => array(
      'variables' => array('element' => null),
      'template' => 'my_entity_template'
    ),
  );
}
?>
```

So the \#theme key in \$entity-\>content points to the Theme Registry entry. The template key in the Theme Registry entry points to the name of the actual template file. The value of this key should be set to the {my_entity_template}.tpl.php portion of the template file. It is simply the name of the template file minus the .tpl.php extension.

After adding the code above, be sure to empty all caches and rebuild the Theme Registry. I use Devel to do this very easily from a sidebar link.

## The Template File

Now all that remains is creating the template file. Just create a new file in /sites/all/themes/my_theme/{my_entity_template}.tpl.php. When someone requests <http://mysite.com/my_entity/>\$my_entity_id, Drupal will use your template to render the output. The code below is some sample code from the entity theme but it can be whatever you want it to be.

``` php
<?php 
  // In a real module variables should be manipulated in a preprocess function.
  $content = $element->content;
?>

<div class="<?php print $classes; ?>">
  <?php print render($content['title']); ?>
  <p class="meta">
    <?php print render($content['field_date']); ?><br />
    <?php print render($content['field_author']); ?>
  </p>

  <figure>
    <?php print render($content['field_image']); ?>
    <figcaption><?php print render($content['field_description']); ?></figcaption>
  </figure>
</div>
```
