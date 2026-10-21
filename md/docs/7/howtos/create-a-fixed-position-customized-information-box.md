---
title: "Create a fixed position customized information box"
source_url: "https://www.drupal.org/docs/7/howtos/create-a-fixed-position-customized-information-box"
page_type: page
last_updated: "Last updated on 25 January 2018"
published: "2012-12-19T18:21:45+00:00"
modified: "2018-01-25T23:43:54+00:00"
breadcrumb: ["Drupal 7", "Site building and development HowTos for Drupal 7"]
fetched: "2026-10-21T08:02:50Z"
raw: "raw/docs/7/howtos/create-a-fixed-position-customized-information-box.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Create a fixed position customized information box

Create a fixed position customized information box similar to the Devel Themer module for specific users, but with your own information.

I find on some Drupal sites that I want to see information all the time behind the scenes, but I don't want the client to see. I added simple code to allow me to do just that. While it is true that I can use the Devel or Devel Themer modules, there is some information that I want which is not provided by Devel, so creating my own custom code works. This code can be embedded into a block, module, or in just the page.tpl.php (or any page template suggestions).

Now, to make things simpler in this tutorial, I embedded inline CSS, but you can obviously add this to any CSS file.

``` php

global $user;
$username = $user->name ;
                                if($username=="developer")
                                {
                                // Generate all your Drupal and PHP variables
                                    $nid = arg(1);
                                    $alias = drupal_get_path_alias();
                              // Print out your HTML div tag with inline CSS or CSS class attribute
                                    echo ('
                                        <div style=" position:fixed; top:65%; left:85%; background:#333; opacity:.9; border:2px solid #FF9; border-radius:10px; padding:20px; width:150px; height:150px; color:yellow; padding-top:15px;  ">
                                        <h5>Developers Only:</h5>
                                        <a style=" color:cyan;" href="' . $base_url . '/node/' . $nid . '/edit">
                                            Edit This Page</a><br/>
                                            <p>alias: ' . $alias . '</p>
                                        </div>
                                        ');

                                    
                                }
                                
```

In this code, I get the username of the logged in user:

``` php
                                global $user;
                                $username = $user->name ;
```

From there, I create my Drupal data and CSS/HTML. You can add any Drupal code and print it out including theme info, module info, taxonomy, views, blocks.

``` php
if($username=="developer") {
```

You can customize this for any username using IF conditionals or PHP switch commands. For more than one user, create an array and use a PHP in_array() function to display different DIVs to different users.

For my CSS, I fix the box to the lower right-hand corner of my screen and add some opacity for a nice effect.
