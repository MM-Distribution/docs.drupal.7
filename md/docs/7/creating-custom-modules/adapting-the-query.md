---
title: "Adapting the query"
source_url: "https://www.drupal.org/docs/7/creating-custom-modules/adapting-the-query"
page_type: page
last_updated: "Last updated on 21 September 2016"
published: "2011-04-06T14:21:28+00:00"
modified: "2016-09-21T18:04:25+00:00"
breadcrumb: ["Drupal 7", "Creating custom modules in Drupal 7"]
fetched: "2026-10-21T07:24:31Z"
raw: "raw/docs/7/creating-custom-modules/adapting-the-query.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Adapting the query

**Main topic described: *Database API***

The new page function will do almost the same work as `current_posts_block_view`, which derives its data from our custom function, `current_posts_contents`. Now the benefit of writing a separate function for our database query becomes apparent. All we need to do is edit it to take an argument and adjust some of the query code, and it will be ready to go for the page.

Here's the edited code:

``` php
function current_posts_contents($display){   //$display argument is new.
  //Get today's date.
  $today = getdate();
  //Calculate midnight a week ago.
  $start_time = mktime(0, 0, 0,$today['mon'],($today['mday'] - 7), $today['year']);
  //Get all posts from one week ago to the present.
  $end_time = time();
  
  $max_num = variable_get('current_posts_max', 3);
  
  //Use Database API to retrieve current posts.
  $query = db_select('node', 'n')
    ->fields('n', array('nid', 'title', 'created'))
    ->condition('status', 1) //Published.
    ->condition('created', array($start_time, $end_time), 'BETWEEN')
    ->orderBy('created', 'DESC'); //Most recent first. Query paused here.
 
   if ($display == 'block'){ 
  // Restrict the range if called with 'block' argument.
    $query->range(0, $max_num);
  } //Now proceeds to execute().
  //If called by page, query proceeds directly to execute().
  
  return $query->execute();
}
```

First of all, we add the `$display` argument to the function. Then, in the query statements, we pause building the query by adding a semi-colon after the `orderBy` method. We then get the function's argument value and decide how to continue. If the argument is from the block, we pick up the query object and restrict the range, then proceed to execute. If it's from the page, we exclude the `range()` method and proceed straight to execute, thus including all the available posts.

### Editing `current_posts_block_view`

To make this code work as it did in the `current_posts_block_view` function before the change, we must add one word to one line of code:

``` php
$result = current_posts_contents('block');
```

Adding the word 'block' as an argument to the function call is all it takes.
