---
title: "Avoid hardcoding"
source_url: "https://www.drupal.org/docs/7/site-building-best-practices/avoid-hardcoding"
page_type: page
last_updated: "Last updated on 7 January 2018"
published: "2011-02-06T04:54:00+00:00"
modified: "2018-01-07T06:37:41+00:00"
breadcrumb: ["Drupal 7", "Drupal 7 site building best practices"]
fetched: "2026-10-21T07:10:50Z"
raw: "raw/docs/7/site-building-best-practices/avoid-hardcoding.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Avoid hardcoding

*The temptation to hardcode happens to the best of us - that's why even the best of us are at risk of being burned by it.*

## Hardcoding defined

Hardcoding is the practice of making code tailored to handle very specific cases. Here are some examples of hardcoding as applies to Drupal:

- Inserting an SQL query into a .tpl file
- Writing a script that queries the database to make some changes to nodes
- Using a regular expression on the output of a theming function to change one HTML class into another

The above examples might work some or even all of the time. However, like hacking core, efficacy alone is not sufficient to make them compatible with the "Drupal Way". Even when hardcoding works - and it often doesn't work as expected - it comes at the cost of that code's ability to handle a more general set of situations.

### Why you should avoid hardcoding

Nobody would hardcode their Drupal site if it seemed like a bad idea to them. However, there are a large number of posted fixes on Drupal.org that rely on hardcoding in some way. That's because hardcoding is often attractive to coders who are in a hurry or are just learning. They see a way to save a lot of time, and in the short run, they're right. The problem is that there are hidden costs to hardcoding that can *cost* a lot of time.

Comments like "don't put code into the theming layer" or "use the hook system" are common, and represent *prescriptive* warnings against hardcoding. However, it can be hard for new Drupallers to find *descriptive* information about why hardcoding is usually a bad idea.

So, here are some specific examples where practicing hardcoding might cause problems down the road:

- #### You're developing a theme.

  You added a custom SQL query to retrieve and display information about the number of saved items a user has. Now you want to use that theme on a different Drupal install. What if the other install has a different set of table names, or is using a different module to store user information that requires a different sequence of joins? Your custom query is now useless.

- #### You design a hand-crafted function to retrieve and display user information.

  This ends up being very processor intensive, and your client wants to cache their results. What happens if you didn't originally anticipate the need to work with existing Drupal caching mechanisms?

- #### You need to change the site theme based on what banner ad shows up on the site.

  However, your code to choose a random banner ad is placed in the site's page.tpl file. This means that you won't know what banner ad is going to be shown until the page has already rendered to the point your function is called. What if the HTML before that needs to change?

- #### You have five variants on your site's theme, using different template files.

  Each of them has a hand-coded query you developed. If that query needs to change, you now need to make the same edit in six places - oops, did I say five? I must've forgotten that the site's mobile theme is in a totally different folder. You won't forget something like that, right?

- #### Someone else starts working with your code.

  If you used a hardcoded solution, do they have any idea what is going on, even if they're experienced in Drupal? Remember, if this is anything other than your personal blog, someone else may become involved with the project. Even if it is just your blog, how do you know how much you'll remember about your code a year from now?

Remember, the primary way that hardcoding fails is by failure to anticipate factors. To go from a page request to a served Drupal page requires that your server execute hundreds of functions. By using existing Drupal hooks, you're existing within the normal, expected flow of those operations. Do you thoroughly understand all the ways in which those functions interact? If not, your choice to operate outside the Drupal framework poses some uncertain amount of risk to your site/yourself/your pets.

### Exceptions

Despite all of the above, hardcoding is different from hacking core in one crucial way: sometimes, there are legitimate reasons to hardcode. Drupal developers will have to do it from time to time. Sometimes, you know that you'll only ever need to pick out a handful of cases and it is an efficient way to do that. An example might be displaying a Halloween theme on a specific node ID that you'll only use once a year. Using a module to add a form option to choose a theme would be undesirable if you knew you'd almost never use it.

If you are going to hardcode, exercise caution, and always ask for advice if you're uncertain about whether to do it at all. Or if you're certain, because that's even *more* dangerous.
