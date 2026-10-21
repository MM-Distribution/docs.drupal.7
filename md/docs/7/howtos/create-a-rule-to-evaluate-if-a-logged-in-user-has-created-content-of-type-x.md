---
title: "Create a Rule to Evaluate If a Logged-in User Has Created Content of Type X"
source_url: "https://www.drupal.org/docs/7/howtos/create-a-rule-to-evaluate-if-a-logged-in-user-has-created-content-of-type-x"
page_type: page
last_updated: "Last updated on 8 December 2016"
published: "2013-07-28T11:35:18+00:00"
modified: "2016-12-08T10:26:58+00:00"
breadcrumb: ["Drupal 7", "Site building and development HowTos for Drupal 7"]
fetched: "2026-10-21T08:02:19Z"
raw: "raw/docs/7/howtos/create-a-rule-to-evaluate-if-a-logged-in-user-has-created-content-of-type-x.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Create a Rule to Evaluate If a Logged-in User Has Created Content of Type X

I recently encountered a situation where I wanted to redirect a user to create a custom content type on login if that content doesn't already exist for the user. Profile2 and Account both provide token support for these fields through Rules, so depending on your needs and how your content is related to the user, you might be able to use these. For my custom type, I was unable to use tokens, so I had written some custom PHP to test if content exists of a certain content type for a given user. Here's what worked for me:

1\. Create a rule (you must download and install the contrib [Rules](https://drupal.org/project/rules) module to do this). I called mine "Redirect User at Login."  
2. Select React on Event \> User \> User has logged in.  
3. From Conditions, select the condition to add: PHP \> Execute custom PHP code.  
4. On the Add a new condition page, in the PHP code, Value field, enter (**without** PHP brackets):

``` php
global $user;
$result = db_query("SELECT COUNT(nid) FROM node JOIN users ON node.uid = users.uid WHERE node.status = :status AND users.uid = :uid AND node.type = :type", array(":status"=> 1, ":uid" => $user->uid, ":type" => 'configuration_1'))->fetchField();
if ($result >= 1){ 
return FALSE;
}
else{
return TRUE;
}
```

In this code, the SQL query checks the database for a user who has created one or more nodes of the type configuration_1. If one or more nodes exist for this user, the condition evaluates to false, and the user will not be redirected to the node/add page. If no nodes exist for the user, the code returns true, and the user will be redirected. Node status "1" means the node is published. Be sure to declare the global \$user variable before the query.

5\. When you have saved the code, go to Actions, Add action. Select System \> Page Redirect. Now add the URL of the page you want to redirect the user to. In my case, it's node/add/configuration-1.

Save your rule and set the weight so that it is triggered in the proper order in relation to any other rules you may have. Make sure the rule is set to Active. Test the rule. You're good to go.
