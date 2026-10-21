---
title: "Template (theme hook) suggestions"
source_url: "https://www.drupal.org/docs/7/theming/template-theme-hook-suggestions"
page_type: page
last_updated: "Last updated on 20 November 2021"
published: "2011-03-11T20:25:31+00:00"
modified: "2021-11-20T00:04:51+00:00"
breadcrumb: ["Drupal 7", "Theming Drupal 7"]
fetched: "2026-10-21T06:05:04Z"
raw: "raw/docs/7/theming/template-theme-hook-suggestions.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Template (theme hook) suggestions

A theme hook suggestion is an alternate template (.tpl.php) file that you have created to override the base or original template file.

For Drupal 8, see [Twig template naming conventions](https://www.drupal.org/node/2354645).

## Theme debug mode

As of [Drupal 7.33](https://www.drupal.org/drupal-7.33-release-notes), Drupal core has a [theme debug mode](https://www.drupal.org/node/223440#theme-debug) that can be enabled and disabled via the `theme_debug` variable and is very helpful when working with template suggestions.

## Custom Theme Hook Suggestions

Custom suggestions beyond the ones listed below can be created. See the page [Working with template suggestions](/node/223440#custom-suggestions).

## Default Theme Hook Suggestions in Core

### block--\[region\|\[module\|--delta\]\].tpl.php

base template: *block.tpl.php*

Theme hook suggestions are made based on these factors, listed from the most specific template to the least. Drupal will use the most specific template it finds:

1.  block--*module--delta*.tpl.php
2.  block--*module*.tpl.php
3.  block--*region*.tpl.php

"module" being the name of the module and "delta", the internal id assigned to the block by the module.

For example, *"block--block--1.tpl.php"* would be used for the first user-submitted block added from the block administration screen since it was created by the block module with the id of 1. "region" will take effect for specific regions. An example of a region-specific template would be "*block--sidebar_first.tpl.php*".

If you had a block created by a custom module called "custom" and a delta of "my-block", the theme hook suggestion would be called "*block--custom--my-block.tpl.php.*"

Also one more example with Views, if you have a block created by views with a view name "front_news" and display id "block_1" then the theme hook suggestion would be: *block--views--front-news-block-1.tpl.php* (notice, when you have underscores in a display id or in a view name - you have to transform them into a single dash)

Be aware that module names are case sensitive in this context. For instance if your module is called 'MyModule', the most general theme hook suggestion for this module would be "*block--MyModule.tpl.php.*"

See [block.tpl.php](https://api.drupal.org/api/drupal/modules!block!block.tpl.php/7) in the Drupal API documentation for more information.

### comment--node-\[type\].tpl.php

base template: *comment.tpl.php*

Support was added to create comment--node-*type*.tpl.php files, to format comments of a certain node *type* differently than other comments in the site. For example, a comment made on an article-type node would be "comment--node-article.tpl.php".

See [comment.tpl.php](https://api.drupal.org/api/drupal/modules!comment!comment.tpl.php/7) in the Drupal API documentation for more information.

### comment-wrapper--node-\[type\].tpl.php

base template: *comment-wrapper.tpl.php*

Similar to the above but for the wrapper template.

See [comment-wrapper.tpl.php](https://api.drupal.org/api/drupal/modules!comment!comment-wrapper.tpl.php/7) in the Drupal API documentation for more information.

### field--\[type\|name\[--content-type\]\|content-type\].tpl.php

base template: *field.tpl.php*

Theme hook suggestions are made based on these factors, listed from the most specific template to the least. Drupal will use the most specific template it finds:

1.  field--*field-name*--*content-type*.tpl.php
2.  field--*content-type*.tpl.php
3.  field--*field-name*.tpl.php
4.  field--*field-type*.tpl.php

Note that underscores in a Field's machine name are replaced by hyphens. Also remember to include "field-" in custom field names, e.g: field--field-phone.tpl.php.

See [field.tpl.php](https://api.drupal.org/api/drupal/modules!field!theme!field.tpl.php/7) in the Drupal API documentation for more information.

### forums--\[\[container\|topic\]--forumID\].tpl.php

base template: *forums.tpl.php*

Theme hook suggestions are made based on these factors, listed from the most specific template to the least. Drupal will use the most specific template it finds:

For forum containers:

1.  forums--containers--*forumID*.tpl.php
2.  forums--*forumID*.tpl.php
3.  forums--containers.tpl.php

For forum topics:

1.  forums--topics--*forumID*.tpl.php
2.  forums--*forumID*.tpl.php
3.  forums--topics.tpl.php

See [forums.tpl.php](https://api.drupal.org/api/drupal/modules!forum!forums.tpl.php/7) in the Drupal API documentation for more information.

### html.tpl.php

base template: *html.tpl.php*

The following are some examples of how you may override the base template:

1.  html--internalviewpath.tpl.php
2.  html--node--id.tpl.php

See [html.tpl.php](https://api.drupal.org/api/drupal/modules%21system%21html.tpl.php/7.x) in the Drupal API documentation for more information.

### maintenance-page--\[offline\].tpl.php

base template: *maintenance-page.tpl.php*

This applies when the database fails. Useful for presenting a friendlier page without error messages. [Theming the maintenance page](/node/195435) must be properly setup first.

See [maintenance-page.tpl.php](https://api.drupal.org/api/drupal/modules!system!maintenance-page.tpl.php/7) in the Drupal API documentation for more information.

### node--\[type\|nodeid\].tpl.php

base template: *node.tpl.php*

Theme hook suggestions are made based on these factors, listed from the most specific template to the least. Drupal will use the most specific template it finds:

1.  node--nodeid.tpl.php
2.  node--type.tpl.php
3.  node.tpl.php

See [node.tpl.php](https://api.drupal.org/api/drupal/modules!node!node.tpl.php/7) in the Drupal API documentation for more information.

### page--\[front\|internal/path\].tpl.php

base template: *page.tpl.php*

The suggestions are numerous. The one that takes precedence is for the front page. The rest is based on the internal path of the current page. Do not confuse the internal path to path aliases which are not accounted for. *Keep in mind that the commonly-used [Pathauto module](http://drupal.org/project/pathauto) uses path aliases.*

The front page can be set at *"Administration \> Configuration \> System \> Site information."* In Drupal 6, at *"Administrator \> Site configuration \> Site information."* Anything set there will trigger the suggestion of "page--front.tpl.php" for it.

The list of suggested template files is in order of specificity based on internal paths. One suggestion is made for every element of the current path, though numeric elements are not carried to subsequent suggestions. For example, "<http://www.example.com/node/1/edit>" would result in the following suggestions:

1.  page--node--edit.tpl.php
2.  page--node--1.tpl.php
3.  page--node.tpl.php
4.  page.tpl.php

Also see [page.tpl.php](http://api.drupal.org/api/drupal/modules--system--page.tpl.php/7) in the Drupal API documentation for more information.

#### How Drupal determines page theme hook suggestions based on path

Here is another explanation based on the [theme_get_suggestions()](http://api.drupal.org/api/drupal/includes--theme.inc/function/theme_get_suggestions/7) function:

The list of possible templates for a given page is generated by Drupal through the [theme_get_suggestions()](http://api.drupal.org/api/drupal/includes--theme.inc/function/theme_get_suggestions/7) function, which is called by the [template_preprocess_page()](http://api.drupal.org/api/drupal/includes--theme.inc/function/template_preprocess_page/7) function.

The [Drupal path](http://drupal.org/node/19828) of the page is first broken up into its components. As mentioned above, the Drupal path is not any of its aliases: there is one and only one Drupal path for a page. For the examples "<http://www.example.com/node/1/edit>" and "<http://www.example.com/mysitename?q=node/1/edit>", the Drupal path is node/1/edit, and its components are "node", 1, and "edit".

Next, the prefix is set to "page". Then, for every component, the following logic is followed:

1.  If the component is a number, add the prefix plus "\_\_%" to the list of suggestions.
2.  Regardless of whether the component is a number or not, add the prefix plus "\_\_" plus the component to the list of suggestions.
3.  If the component is *not* a number, append "\_\_" plus the component to the prefix.

After the list of components is iterated through, if the page is the front page (as set through *"Administration \> Configuration \> System \> Site information."*), then "page\_\_front" is added to the list of suggestions.

Note that eventually, to turn a suggestion into an actual file name, "\_\_" gets turned into "--", and ".tpl.php" gets appended to the suggestion. Thus, for node/1/edit, we get the following list of suggestions:

1.  page.tpl.php (this is always a suggestion)
2.  page--node.tpl.php (and prefix is set to page\_\_node)
3.  page--node--%.tpl.php
4.  page--node--1.tpl.php (prefix is not changed because the component is a number)
5.  page--node--edit.tpl.php (and prefix is set to page\_\_node\_\_edit)
6.  page--front.tpl.php (but only if node/1/edit is the front page)

When the page is actually rendered, the *last* suggestion is checked. If it exists, that suggestion is used. Otherwise the next suggestion up is checked, and so on. Of course, if none of the overriding suggestions exist, page.tpl.php is the final suggestion. This also explains why page--front.tpl.php, if it exists, overrides any other suggestion for the front page: it is always the last suggestion for the page designated as the front page.

### poll-results--\[block\].tpl.php

base template: *poll-results.tpl.php*

The theme function that generates poll results are shared for nodes and blocks. The default is to use it for nodes but a suggestion is made for rendering them inside block regions. This suggestion is used by default and the template file is located at "modules/poll/poll-results--block.tpl.php".

See [poll-results.tpl.php](https://api.drupal.org/api/drupal/modules!poll!poll-results.tpl.php/7) in the Drupal API documentation for more information.

### poll-vote--\[block\].tpl.php

base template: *poll-vote.tpl.php*

Similar to poll-results--\[block\].tpl.php but for generating the voting form. You must provide your own template for it to take effect.

See [poll-vote.tpl.php](https://api.drupal.org/api/drupal/modules!poll!poll-vote.tpl.php/7) in the Drupal API documentation for more information.

### poll-bar--\[block\].tpl.php

base template: *poll-bar.tpl.php*

Same as poll-vote--\[block\].tpl.php but for generating individual bars.

See [poll-bar.tpl.php](https://api.drupal.org/api/drupal/modules!poll!poll-bar.tpl.php/7) in the Drupal API documentation for more information.

### profile-wrapper--\[field\].tpl.php

base template: *profile-wrapper.tpl.php*

The profile wrapper template is used when browsing the member listings page. When browsing specific fields, a suggestion is made with the field name. For example, <http://drupal.org/profile/country/Belgium> would suggest "profile-wrapper--country.tpl.php".

See [profile-wrapper.tpl.php](https://api.drupal.org/api/drupal/modules!profile!profile-wrapper.tpl.php/7) in the Drupal API documentation for more information.

### region--\[region\].tpl.php

base template: *region.tpl.php*

The region template is used when a page region has content, either from the Block system or a function like [hook_page_build()](http://api.drupal.org/api/drupal/modules--system--system.api.php/function/hook_page_build/7). Possible region names are determined by the theme's [.info file](http://drupal.org/node/171205#regions).

See [region.tpl.php](https://api.drupal.org/api/drupal/modules!system!region.tpl.php/7) in the Drupal API documentation for more information.

### search-results--\[searchType\].tpl.php

base template: *search-results.tpl.php*

search-results.tpl.php is the default wrapper for search results. Depending on type of search different suggestions are made. For example, "example.com/search/node/Search+Term" would result in "search-results--node.tpl.php" being used. Compare that with "example.com/search/user/bob" resulting in "search-results--user.tpl.php". Modules can extend search types adding more suggestions of their type.

See [search-results.tpl.php](https://api.drupal.org/api/drupal/modules!search!search-results.tpl.php/7) in the Drupal API documentation for more information.

### search-result--\[searchType\].tpl.php

base template: *search-result.tpl.php*

The same as above but for individual search results.

### taxonomy-term--\[vocabulary-machine-name\|tid\].tpl.php

base template: *taxonomy-term.tpl.php*

Theme hook suggestions are made based on these factors, listed from the most specific template to the least. Drupal will use the most specific template it finds:

1.  taxonomy-term--tid.tpl.php
2.  taxonomy-term--vocabulary-machine-name.tpl.php
3.  taxonomy-term.tpl.php

Note that underscores in a vocabulary's machine name are replaced by hyphens.

See [taxonomy-term.tpl.php](https://api.drupal.org/api/drupal/modules!taxonomy!taxonomy-term.tpl.php/7) in the Drupal API documentation for more information.

## Add a `page.tpl.php` depending on content type.

In Drupal 7, you do this by having this code in the function `THEME_preprocess_page` (where `THEME` is the name of the theme) in the theme's `template.php`.

``` php
function THEME_preprocess_page(&$variables) {
  if (isset($variables['node']->type)) {
   // If the content type's machine name is "my_machine_name" the file
   // name will be "page--my-machine-name.tpl.php".
   $variables['theme_hook_suggestions'][] = 'page__' . $variables['node']->type;
   }
} 
```

Add the if-statement at the end if this function already exists in the theme's `template.php`, otherwise, add the functions.

## Cache issue

When working with theme hook suggestion, there is a possibility that Drupal use its cache rather than the new templates as suggested. Remove the cache if you experience this problem. To clear the cache, choose one of the methods described in [Clearing Drupal's cache](http://drupal.org/node/42055).
