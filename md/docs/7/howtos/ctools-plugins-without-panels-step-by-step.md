---
title: "CTools Plugins without Panels, step by step"
source_url: "https://www.drupal.org/docs/7/howtos/ctools-plugins-without-panels-step-by-step"
page_type: page
last_updated: "Last updated on 25 January 2018"
published: "2014-03-11T15:24:08+00:00"
modified: "2018-01-25T23:37:00+00:00"
breadcrumb: ["Drupal 7", "Site building and development HowTos for Drupal 7"]
fetched: "2026-10-21T08:00:46Z"
raw: "raw/docs/7/howtos/ctools-plugins-without-panels-step-by-step.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# CTools Plugins without Panels, step by step

CTools plugins and Panels are great and play together very well. It's almost as if they were made for each other--weren't they? However, I recently worked on a project where CTools plugins were an excellent solution for some of our needs, but Panels were verboten. I didn't find much documentation on that, so this page provides a detailed how-to for incorporating a CTools plugin in a regular Drupal block. It also shows how to pass arguments to a plugin render callback. Though the title says without Panels, I will begin with the implementation of a CTools plugin that displays a Twitter feed in a Panel, then expand on how to make it work in a Block.

The first step in getting our plugin going is to include CTools as a dependency in our module's .info file. I've included panels here as well, but this is not necessary if all you want to do is stick a plugin in a block. You will need to include panels if you want to use your plugin in the Panels UI.

``` php
dependencies[] = ctools
dependencies[] = panels
```

Next, we need to tell CTools where our plugin lives. This is accomplished by implementing hook_ctools_plugin_directory() in our module's .module file

``` php
function MYMODULE_ctools_plugin_directory($module, $plugin) {
  if (($module == 'ctools') && ($plugin == 'content_types')) {
    return 'plugins/content_types';
  }
}
```

With that out of the way, we are now ready to create our actual plugin. Within our module directory, we create a plugins directory and create a content_types directory under that. We're also going to want a place for .tpl.php files, so we'll add a templates directory while we're at it. With that done, our module's directory structure looks like so

``` php
MYMODULE/
    plugins/
        content_types/
        templates/
    MYMODULE.info
    MYMODULE.module     
```

We now implement our plugin in a .inc file in the content_types/ directory. Since our plugin is doing a Twitter feed, I've called this twitter.inc

``` php
$plugin = array(
  'title' => t('Twitter feed'),
  'description' => t('Twitter feed'),
  'category' => 'Widgets',
  'icon' => '',
  'render callback' => 'twitter_block',
  'defaults' => array(),
);

// render callback
function twitter_block() {
  // Add twitter widget javascript
  drupal_add_js('http://platform.twitter.com/widgets.js', 'external');
  $url = TWITTER_USER
  $widget_id = TWITTER_WIDGET_ID;
  $data = array();

  $data['url'] = $url;
  $data['widget_id'] = $widget_id;

  $content = array(
    '#theme' => 'twitter_block',
    '#content' => $data,
  );

  $block = new stdClass();
  $block->content = $content;
  $block->title = '';
  $block->id = 'twitter_block';

  return $block;
}
```

Let's break that down a little.

The \$plugins array tells CTools about our plugin. The first four items will show up in the Panels UI, and the render_callback attribute tells CTools what code to use to output the contents of the plugin.

Now, let's add a hook_theme() to our .module file. This will take the content returned by the twitter_block() function above, and pass it along to a file called twitter.tpl.php in our modules templates directory.

``` php
function MY_MODULE_theme() {
  return array(
    'twitter_block' => array(
      'render element' => 'data',
      'template' => 'plugins/templates/twitter'
    ),
  );
}
```

Next, create a twitter.tpl.php file in our templates directory

``` php
<h2 style="font-size:1.2em">Twitter feed</h2>
<div id="twitter" style="padding:2px;border:1px solid blue;">
  <div class="twitter-feed">
    <a class="twitter-timeline" href="https://twitter.com/<?php print $data['#content']['url']; ?>"
       data-widget-id="<?php print $data['#content']['widget_id']; ?>"
       width="100%"
       height="<?php print $data['#content']['height']; ?>"
      >
      Tweets from @<?php print $data['#content']['url']; ?>
    </a>
  </div>
</div>
```

For a Panels implementation, we're done. This is a very simple example, but you can get a lot fancier inside of that .inc file and get a whole lot of bang for the very little buck for a module that only implements two simple hooks. We can now go to /admin/structure/pages to build a page and add our plugin as a content item in a region on that page. But, as mentioned, my problem was that I wasn't allowed to use Panels, so here's where it gets a little more interesting. We're now going to create a block and have our plugin show up inside of that. This is a complete idiot page, so we start by telling Drupal about our block.

``` php
function MYMODULE_block_info() {
  $blocks = array();
  $blocks['my_twitter_block'] = array(
    'info' => t('My Twitter block'),
    'region' => 'sidebar_first',
    'status' => 1,
  );
  return $blocks;
}
```

This code will automatically insert the block in the sidebar_first region, without having to go through the Block UI. If you want to insert your block manually, just get rid of the region and status attributes. Now that Drupal knows about our block, all that's left is to provide a way to display it. For this, we need hook_block_view(), and this is where things get interesting.

``` php
function MYMODULE_block_view($delta = '') {
  ctools_include('content');

  $block = array();

  switch ($delta) {
    case 'my_twitter_block':
      // assemble the params for ctools_content_render()
      $type = 'twitter';
      $subtype = 'twitter';
      $conf = NULL;
      $keywords = $contexts = array();
      $args = array(
         'user_id' => TWITTER_USER,
         'widget_id' => TWITTER_WIDGET_ID
      );

      $data = ctools_content_render($type, $subtype, $conf, $keywords, $args, $contexts);

      // pass the plugin content to our .tpl.php file via hook_theme()
      $content = theme('twitter_block', $data->content);

      $block['subject'] = '';
      $block['content'] = array(
        // put the themed content into our block markup
        '#markup' => $content,
      );
      break;
  }

  // voila!
  return($block);
}
```

First, we call ctools_include('content'). This will get us access to the ctools_content_render() function that will execute our plugin's render callback. A fun part of this is that we get to pass arguments to ctools_content_render() so we don't have to hard code anything in our plugin. In our example here, ctools_content_render() will look for a plugin called 'twitter.inc', per the \$type parameter, find the plugin's render callback specified in the \$plugin array, pass it the \$args array with our 'user_id' and 'widget_id' arguments, and return the plugin content, which we then pass along to our .tpl.php file via hook_theme(), and put the themed content into our block markup.

All that's left now is to modify our render callback slightly to use the arguments we're passing to ctools_content_render():

``` php
function twitter_block($type, $subtype, $args) {
  // Add twitter widget javascript
  drupal_add_js('http://platform.twitter.com/widgets.js', 'external');
  $url = $args['user_id'];
  $widget_id = $args['widget_id'];
  $data = array();
  // ...
}
```

And that's it. When our block loads, it will get its content from our CTools plugin.
