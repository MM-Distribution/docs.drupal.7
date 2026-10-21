---
title: "Show a block depending on node type and node id"
source_url: "https://www.drupal.org/docs/7/theming/howto/show-a-block-depending-on-node-type-and-node-id"
page_type: page
last_updated: "Last updated on 18 September 2016"
published: "2007-02-02T17:57:30+00:00"
modified: "2016-09-18T21:06:02+00:00"
breadcrumb: ["Drupal 7", "Theming Drupal 7", "Theming HowTos"]
fetched: "2026-10-21T08:51:44Z"
raw: "raw/docs/7/theming/howto/show-a-block-depending-on-node-type-and-node-id.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Show a block depending on node type and node id

**Warning: These techniques require the use of the [PHP filter module](https://www.drupal.org/documentation/modules/php) which can have security implications and potentially cause performance issues.**

The following snippets allow you to configure a block to be shown or hidden depending on node id (nid) or node type. You can modify the arrays in the snippet to match your needs. Just modify and paste the appropriate snippet in the Block Visibility section when configuring a block.

## How to use these snippets

1.  Go to your blocks administration section: "Home » Administer » Structure » Blocks".
2.  Click 'Add block' to add a new block, or click 'Configure' on an existing block.
3.  Under "Page specific visibility settings" select "Show if the following PHP code returns TRUE (PHP-mode, experts only)."
4.  Paste the snippet in the text area just below. (NOTE: Remember to keep the *\<?php ?\>* tags.)

**Modifying Arrays:**  
Node Type Array  
\$types = array('page' =\> 1);

**Node ID Array**  
\$nodes = array(1, 2);

### Show a block based on \$nid

The following will show the configured block in:  
Example: <http://www.example.com/node/1>  
Example: <http://www.example.com/node/2>

**NOTE:** For Drupal 7, replace **\$node = node_load(array('nid' =\> \$nid));** with **\$node = node_load(\$nid)** ; in the example code shown on this page.

``` php
<?php 
// Only show block from types array and nodes array 
$match = FALSE; 

// Which node types 
$types = array('page' => 1); 
// Which nodes (by nid) 
$nodes = array(1, 2); 

if (arg(0) == 'node' && is_numeric(arg(1))) { 
  $nid = arg(1); 
  $node = node_load(array('nid' => $nid)); 
  $type = $node->type; 
  if (isset($types[$type]) && in_array($nid, $nodes)) { 
    $match = TRUE; 
  } 
} 
return $match; ?> 
```

### Show a block for only certain node types

``` php
<?php 
// Only show if $match is true 
$match = false; 

// Which node types 
$types = array( 'book', 'news', 'anothernodetype' );
 
// Match current node type with array of types 
if (arg(0) == 'node' && is_numeric(arg(1))) { 
  $nid = arg(1); 
  $node = node_load(array('nid' => $nid)); 
  $type = $node->type; 
  $match |= in_array($type, $types); 
} 
return $match; ?> 
```

### Hide blocks from certain node types

``` php
<?php 
// Only show if $match is true 
$match = true; 

// Which node types to NOT show block 
$types = array('book', 'news', 'anothernodetype' ); 

// Match current node type with array of types 
if (arg(0) == 'node' && is_numeric(arg(1))) { 
  $nid = arg(1); 
  $node = node_load(array('nid' => $nid)); 
  $type = $node->type; 
  if(in_array($type, $types)) { $match = false; } 
} 
return $match; ?>
```

### Take different actions depending on node type

``` php
<?php 
// Replace 'nodetype-x' with the node types you need 
$nodetypes = array('nodetype-1', 'nodetype-2', 'nodetype-3'); 

if (in_array($node->type, $nodetypes)) { 
  // Begin your code for if the node's type was listed in the array 
  print $something; 
  // End code for if the node type was listed in the array 
} else { 
  // Begin your code for if the node type wasn't listed in the array 
  print $somethingelse; 
  // End code for if the node type wasn't listed in the array 
} ?> 
```
