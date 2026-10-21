---
title: "Retrieving data"
source_url: "https://www.drupal.org/docs/7/creating-custom-modules/retrieving-data"
page_type: page
last_updated: "Last updated on 21 September 2016"
published: "2011-03-24T19:33:43+00:00"
modified: "2016-09-21T18:04:25+00:00"
breadcrumb: ["Drupal 7", "Creating custom modules in Drupal 7"]
fetched: "2026-10-21T07:22:43Z"
raw: "raw/docs/7/creating-custom-modules/retrieving-data.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Retrieving data

**Main topic described: *Database API***  
**Main function described: *db_select()***

Next we will create a custom function to retrieve the most recent posts. When a node is first created, the time of creation is stored in the database. We'll use this database field to find our data. We could include this code in the hook we will implement in the next tutorial page. Putting this section into a separate function keeps the code cleaner, easier to read and to maintain.

We will call the function `current_posts_contents`. We continue to follow the naming convention by beginning with the module short name. Then we use a descriptive word that is not a Drupal hook. The function begins with getting the time numbers. Here's the first part (without a closing brace because it's not the complete function):

``` php
/**
 * Custom content function. 
 * 
 * Set beginning and end dates, retrieve posts from database
 * saved in that time period.
 * 
 * @return 
 *   A result set of the targeted posts.
 */
function current_posts_contents(){
  //Get today's date.
  $today = getdate();
  //Calculate the date a week ago.
  $start_time = mktime(0, 0, 0,$today['mon'],($today['mday'] - 7), $today['year']);
  //Get all posts from one week ago to the present.
  $end_time = time();
```

This code gets the current time, then calculates the time (in seconds since epoch start, see [mktime](http://www.php.net/manual/en/function.mktime.php) for more information on time format) for midnight a week ago. These functions are straight PHP; you can look them up on the PHP website ([php.net](http://php.net/)) for more details.

Next we use Drupal's Database API to retrieve our list of current nodes. This is the second part of the custom function:

``` php
  //Use Database API to retrieve current posts.
  $query = db_select('node', 'n')
    ->fields('n', array('nid', 'title', 'created'))
    ->condition('status', 1) //Published.
    ->condition('created', array($start_time, $end_time), 'BETWEEN')
    ->orderBy('created', 'DESC') //Most recent first.
    ->execute(); 
  return $query;  
}
```

Built into Drupal is a very robust query builder, using a special object-oriented API. INSERT, UPDATE, and DELETE queries need this special care in order to behave consistently across all different databases. Although our SELECT query doesn't require this structure, this is a good opportunity to become familiar with it. You will see this structure used throughout Drupal.

1.  We build the query using the `db_select` method, which takes a table name ('node') and alias ('n') as arguments.
2.  The `fields` method uses the table assigned the alias 'n' to select the fields listed in the array in the second argument.
3.  The `condition` method takes three arguments. The first is the field, the second the value, the third the operator. If no operator is specified, as in 'status' above, `=` is assumed.
4.  The `orderBy` method sorts according to the field in the first argument, in the order specified by the second argument.
5.  The `execute` method compiles and runs the query and returns a result set/statement object.

Here's the complete function:

``` php
/**
 * Custom content function. 
 * 
 * Set beginning and end dates, retrieve posts from database
 * saved in that time period.
 * 
 * @return 
 *   A result set of the targeted posts.
 */
function current_posts_contents(){
  //Get today's date.
  $today = getdate();
  //Calculate the date a week ago.
  $start_time = mktime(0, 0, 0,$today['mon'],($today['mday'] - 7), $today['year']);
  //Get all posts from one week ago to the present.
  $end_time = time();

  //Use Database API to retrieve current posts.
  $query = db_select('node', 'n')
    ->fields('n', array('nid', 'title', 'created'))
    ->condition('status', 1) //Published.
    ->condition('created', array($start_time, $end_time), 'BETWEEN')
    ->orderBy('created', 'DESC') //Most recent first.
    ->execute(); 
  return $query;  
}
```

(Remember not to include the closing `?>` in your code.)

### See also

- [mktime](http://www.php.net/manual/en/function.mktime.php)
- [php.net](http://php.net/)
- [db_select](http://api.drupal.org/api/drupal/includes--database--database.inc/function/db_select/7)
- [Dynamic queries](http://drupal.org/node/310075)
- [Conditional clauses](http://drupal.org/node/310086)
