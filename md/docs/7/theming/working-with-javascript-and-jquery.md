---
title: "Working with JavaScript and jQuery"
source_url: "https://www.drupal.org/docs/7/theming/working-with-javascript-and-jquery"
page_type: page
last_updated: "Last updated on 26 June 2017"
published: "2007-08-28T16:24:27+00:00"
modified: "2017-06-26T20:40:15+00:00"
breadcrumb: ["Drupal 7", "Theming Drupal 7"]
fetched: "2026-10-21T06:04:17Z"
raw: "raw/docs/7/theming/working-with-javascript-and-jquery.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Working with JavaScript and jQuery

Using JavaScript adds dynamic presentation effects to a theme. In addition to custom JavaScript files many Drupal developers find jQuery useful. [jQuery](http://jquery.com/) is a lightweight JavaScript library which is built into Drupal. jQuery contains all the common DOM, event, effects, and Ajax functions.

Drupal 7 includes jQuery 1.4.4 and jQuery UI 1.8.7. Drupal 6.0 to 6.2 included jQuery 1.2.3 while Drupal 6.3 includes an update to jQuery 1.2.6. For use in module development which requires a later version of jQuery, apply the [jQuery update](http://drupal.org/project/jquery_update) module. When JavaScript is added to a page through Drupal, jQuery is automatically added to the page.

For **Drupal 8** see [JavaScript API in Drupal 8](/node/2269515)

More comprehensive information on the JavaScript APIs and the use of JavaScript in Drupal can be found in the [Developer Guide](//drupal.org/node/121997).

For more information about jQuery visit the [jQuery API](http://api.jquery.com/) and [Documentation](http://docs.jquery.com/) site.

Drupalize.Me offers a free, 11-minute video introduction to using jQuery in Drupal 6&7...  
[Intro to jQuery in Drupal](https://drupalize.me/videos/jquery-overview "Intro to jQuery in Drupal")

## Adding JavaScript

There are two ways for Themes to easily add JavaScript to a page.

### In .info File

JavaScript files can be added to a theme's .info file using the scripts tag. For example, to add the script foo.js to every page on a Drupal site add the following to the theme's .info file.

``` php
scripts[] = foo.js
```

[Clear the theme cache](http://drupal.org/node/337176) for this change to take effect

Scripts added in a theme's .info file is added at the theme level of ordering and will come after core/library JavaScript and module JavaScript. This ordering is important because it allows the theme JavaScript an opportunity to act on the page after the JavaScript providing the functionality within the page.

In Drupal 6 there is a default script file, named script.js that can be added to a theme without specifying it in the .info file. If that script is included in the theme it will be automatically added to all pages. In Drupal 7 all script files need to be specified.

### In template.php

Alternatively, scripts can be added in the template.php file using [drupal_add_js()](http://api.drupal.org/drupal_add_js) or, in Drupal 7, [drupal_add_library()](http://api.drupal.org/drupal_add_library). For example, adding a script in the root directory of a theme named foo.js would go like:

In Drupal 6:

``` php
function example_preprocess_page(&$variables) {
  drupal_add_js(drupal_get_path('theme', 'example'). '/foo.js', 'theme');
  // We need to rebuild the scripts variable with the new script included.
  $variables['scripts'] = drupal_get_js();
}
```

In Drupal 7:

``` php
function example_preprocess_html(&$variables) {
  $options = array(
    'group' => JS_THEME,
  );
  drupal_add_js(drupal_get_path('theme', 'example'). '/foo.js', $options);
}
```

*Note, in Drupal 7 the \$scripts variable does not need to be rebuilt. \$scripts is built in [template_process_html](http://api.drupal.org/template_process_html) which happens after this function.*

Drupal 7 includes library management. Libraries are collections of JavaScript, CSS, and dependent libraries. For example, Drupal 7 includes jQuery UI. jQuery UI is a component library with internal dependencies. When ui.autocomplete is included it needs ui.core and ui.position to be included as well. Drupal libraries takes care of this for us. Adding ui.autocomplete with all of its CSS, JS, and dependencies can be accomplished with the following code:

``` php
drupal_add_library('system', 'ui.autocomplete');
```

This one command includes jquery.ui.autocomplete.js, jquery.ui.autocomplete.css, and the dependencies of jquery.ui.position.js, jquery.ui.widget.js, jquery.ui.core.js, jquery.ui.core.css, and jquery.ui.theme.css. For more information on [drupal_add_library see the API documentation](http://api.drupal.org/drupal_add_library).

## JavaScript closures

It's best practice to wrap your code in a closure. A closure is nothing more than a function that helps limit the scope of variables so you don't accidentally overwrite global variables.

``` php
// Define a new function.
(function () {
  // Variables defined in here will not affect the global scope.
  var window = "Whoops, at least I only broke my code.";
  console.log(window);
// The extra set of parenthesis here says run the function we just defined.
}());
// Our wacky code inside the closure doesn't affect everyone else.
console.log(window);
```

A closure can have one other benefit, if we pass `jQuery` in as a parameter we can map it to the `$` shortcut allowing us to use use `$()` without worrying if [`jQuery.noConflict()`](http://api.jquery.com/jQuery.noConflict/) has been called.

``` php
// We define a function that takes one parameter named $.
(function ($) {
  // Use jQuery with the shortcut:
  console.log($.browser);
// Here we immediately call the function with jQuery as the parameter.
}(jQuery));
```

Note that there are two acceptable syntaxes for closures: the parenthesis that closes the first parenthesis can come either before or after the `(jQuery)`.

The .ready() function also has the ability to alias the jQuery object:

``` php
jQuery(document).ready(function($) {
  // Code that uses jQuery's $ can follow here.
});
```

In Drupal 7 `jQuery.noConflict()` is called to make it easier to use other JS libraries, so you'll either have to type out `jQuery()` or have the closure rename it for you. More examples can be found on [jQuery's api site](http://api.jquery.com/jQuery.noConflict/).

## JavaScript behaviors / JavaScript on AJAX forms

Drupal uses a "behaviors" system to provide a single mechanism for attaching JavaScript functionality to elements on a page. The benefit of having a single place for the behaviors is that they can be applied consistently when the page is first loaded and then when new content is added during AHAH/AJAX requests. In Drupal 7 behaviors have two functions, one called when content is added to the page and the other called when it is removed.

Behaviors are registered by setting them as properties of `Drupal.behaviors`. Drupal will call each and pass in a DOM element as the first parameter (in Drupal 7 a settings object will be passed as the second parameter). For the sake of efficiency the behavior function should do two things:

In Drupal 7 use the [jQuery Once plugin](http://plugins.jquery.com/once/) that's bundled with core:  
`jQuery('.foo', context).once('foo').css('color', 'red');`

- Limit the scope of searches to the context element and its children. This is done by passing context parameter along to jQuery:  
  `jQuery('.foo', context);`
- Avoid processing the same element multiple times.  
  In Drupal 6 assign a marker class to the element and use that class to restrict selectors:  
  `jQuery('.foo:not(.foo-processed)', context).addClass('foo-processed').css('color', 'red');`

As a simple example lets look at how you'd go about finding all the `https` links on a page and adding some additional text marking them as secure, turning `<a href="https://example.com">Example</a>` into `<a href="https://example.com">Example (Secure!)</a>`. This should make the importance of only running the code once apparent, if our code ran twice the link would end up reading "Example (Secure!) (Secure!)".

In Drupal 6 it would be done like this:

``` php
// Using the closure to map jQuery to $. 
(function ($) {

// Store our function as a property of Drupal.behaviors.
Drupal.behaviors.myModuleSecureLink = function (context) {
  // Find all the secure links inside context that do not have our processed
  // class.
  $('a[href^="https://"]:not(.secureLink-processed)', context)
    // Add the class to any matched elements so we avoid them in the future.
    .addClass('secureLink-processed')
    // Then stick some text into the link denoting it as secure.
    .append(' (Secure!)');
};

// You could add additional behaviors here.
Drupal.behaviors.myModuleMagic = function(context) {};

}(jQuery));
```

In Drupal 7 it's a little different because behaviors can be attached when content is added to the page and detached when it is removed:

``` php
// Using the closure to map jQuery to $. 
(function ($) {

// Store our function as a property of Drupal.behaviors.
Drupal.behaviors.myModuleSecureLink = {
  attach: function (context, settings) {
    // Find all the secure links inside context that do not have our processed
    // class.
    $('a[href^="https://"]', context)
      // Only process elements once.
      .once('secureLink')
      // Then stick some text into the link denoting it as secure.
      .append(' (Secure!)');
  }
};

// You could add additional behaviors here.
Drupal.behaviors.myModuleMagic = {
  attach: function (context, settings) { },
  detach: function (context, settings) { }
};

}(jQuery));
```

**JavaScript on your AJAX form**

Attach jQuery to Drupal.behaviors, that way it can be run anytime new DOM elements are inserted. One example, if you're using AJAX in Views, each time a section of the page reloads, it will reload/run jQuery.

Here's how to do it!

``` php
(function($) {
Drupal.behaviors.myBehavior = {
  attach: function (context, settings) {

    //code starts
    $("body").click(function() {
      alert("Hello World");
    });
    //code ends

  }
};
})(jQuery);
```

Clicking anywhere on your website, now alerts - Hello World.

## JavaScript theming

Drupal provides a theming mechanism for JavaScript code in a similar manner to the way theming works within the rest of Drupal. This enables themes to customize the markup generated by JavaScript.

Modules provide theme functions for their markup. For example, the following code uses the theme function `powered` (This displays a "powered by Drupal" icon):

``` php
Drupal.theme.prototype.powered = function(color, height, width) {
  return '<img src="/misc/powered-'+ color +'-'+ height +'x'+ width +'.png" />';
}
```

When a module wants to insert the markup it would do so in a matter like:

``` php
$('.footer').append(Drupal.theme('powered', 'black', 135, 42));
```

This will place an image in any elements with the class *footer* with the following markup:

``` php
<img src="http://drupal.org/misc/powered-black-135x42.png" />
```

When a theme wants to provide a different markup it can do so by providing an alternate theme function. Following our example the following function provides a theme function for the theme.

``` php
Drupal.theme.powered = function(color, height, width) {
  return '<div class="powered-'+ color +'-'+ height +'x'+ width +'"></div>';
}
```

While the modules theme function is at `Drupal.theme.prototype.powered` the theme's is at `Drupal.theme.powered`. Including this function in the themes JavaScript will cause the markup generated by the snippet:

``` php
$('.footer').append(Drupal.theme('powered', 'black', 135, 42));
```

to be:

``` php
<div class="powered-black-135x42"></div>
```

JavaScript theme functions are entirely free in their return value. They can vary from simple strings to complex data types like objects, arrays, and jQuery elements. Refer to the original (default) theme function to see what your custom theme function should return.

Cross reference to related community documentation (Drupal.org "Developer Guide" as well as "Theming Guide"):

1.  Create a new file in your theme directory(i.e. /sites/all/themes/\[mytheme\]/), called script.js
2.  Insert this into your theme .info file(i.e. /sites/all/themes/\[mytheme\]/\[mytheme\].info):  
    scripts\[\] = script.js
3.  Insert the following into script.js (the file you created in step 1):

- Developer Guide - For more information on using JavaScript and jQuery in Drupal, see the [JavaScript section](http://drupal.org/node/121997) of the developer guide. Also, join the JavaScript group on Groups.Drupal.org to get advice on JavaScript and jQuery: <http://groups.drupal.org/javascript>
- Theming Guide - [Working with JavaScript and jQuery](http://drupal.org/node/171213) for links to two buildamodule.com tutorial videos
