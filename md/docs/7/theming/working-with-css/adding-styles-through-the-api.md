---
title: "Adding styles through the API"
source_url: "https://www.drupal.org/docs/7/theming/working-with-css/adding-styles-through-the-api"
page_type: page
last_updated: "Last updated on 27 February 2019"
published: "2008-02-23T21:57:41+00:00"
modified: "2019-02-27T21:05:57+00:00"
breadcrumb: ["Drupal 7", "Theming Drupal 7", "Working with CSS"]
fetched: "2026-10-21T08:14:59Z"
raw: "raw/docs/7/theming/working-with-css/adding-styles-through-the-api.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Adding styles through the API

Adding [styles through the .info file](/node/171209) should be sufficient for most themes. Since the .info file is static, style sheets cannot be added dynamically. Depending on how the theme handles style sheets, it may not matter altogether. When in doubt, use the .info file.

There are two API functions for working with style sheets, [drupal_add_css](http://api.drupal.org/api/function/drupal_add_css/6) and [drupal_get_css](http://api.drupal.org/api/function/drupal_get_css/6). Here is an example to dynamically add styles sheets.

*Change the "template" prefix to the name of your theme.*

``` php
function template_preprocess_page(&$variables) {
  $front_style = path_to_theme() .'/front-page.css';
  $path_style = path_to_theme() .'/path-'. arg(0) .'.css';

  if (file_exists($front_style) && $variables['is_front']) {
    $include_style = $front_style;
  }
  elseif (file_exists($path_style)) {
    $include_style = $path_style;
  }

  if (isset($include_style)) {
    $options = array(
      'group' => CSS_THEME,
      'preprocess' => FALSE,
    );
    drupal_add_css($include_style, $options);
    $variables['styles'] = drupal_get_css();
  }
}
```

The above example would include the style sheet "front-page.css" on the front page or many others based on the internal path. For example, <http://example.com/admin> would pickup on "path-admin.css".

*A few notes:*

- *Depending on where and when the style is added, drupal_get_css may need to be called in order to include the added styles. They are initially retrieved in [template_preprocess_page](http://api.drupal.org/api/function/template_preprocess_page/6). See [Preprocessors and variables](/node/223430) for details on the order of the preprocessors.*
- *There is a parameter in drupal_add_css to aggregate the added file. Consider disabling it like the above example when the inclusion of the style sheet is very dynamic, since files added to the larger aggregate will force a new aggregated CSS file to be recreated. In effect, it can slow down the retrieval of the page and consume more bandwidth.*

### Where To Add Code

This code can be added in the template.php file in your theme directory.  
There may already be a function there called "phptemplate_preprocess_page".  
Just include it within the body of your XXX\_\_preprocess_page function.

You just have to use the same variable name that is passed in by reference within your function. For example, if your function signature looks like ...  
`function template_preprocess_page(&$vars)`  
then you should use  
`$vars `  
inside the function.

Or if the function looks like this:  
`function template_preprocess_page(&$variables)`  
then you should use  
`$variables`  
inside the function.
