---
title: "Architectural view of theming"
source_url: "https://www.drupal.org/docs/7/theming/overriding-themable-output/architectural-view-of-theming"
page_type: page
last_updated: "Last updated on 27 September 2016"
published: "2007-08-28T15:38:11+00:00"
modified: "2016-09-27T00:37:36+00:00"
breadcrumb: ["Drupal 7", "Theming Drupal 7", "Overriding themable output"]
fetched: "2026-10-21T08:22:44Z"
raw: "raw/docs/7/theming/overriding-themable-output/architectural-view-of-theming.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Architectural view of theming

<https://www.drupal.org/docs/7/theming/core-templates>This page provides background information on the underlying architecture of theming. It will be of interest to people who need a deeper understanding of how overrides work.

A common software practice is to compartmentalize the programming layer from the presentation layer. There are [numerous reasons](http://en.wikipedia.org/wiki/Separation_of_concerns) for this, the most obvious being that the skill set required for programming the back-end [business logic](http://en.wikipedia.org/wiki/Business_logic) is very different from creating a visually appealing and effective user interface. As a theme developer, you can control certain aspects of the available data, but it is limited to the output and presentation. Only Drupal core and modules should work with input. For example, a module can implement a form with a default look and feel and handle user input, saving it to the database. The theme's role is only to override the look and feel.

This abstraction in Drupal is achieved through the **[theme](http://api.drupal.org/api/function/theme)** function. It is a conduit to the theming subsystem. It allows theme engines to provide an optional middle layer for tagging languages such as [PHPTAL](/project/phptal) or [Smarty](/project/smarty). It also allows themes to control all presentation markup. Theme engines are optional as are tagging languages. PHPTemplate is the default engine. As the name suggests, it uses the language PHP when outputting variables mixed in with the *x*HTML markup.

*Starting with Drupal 6, the requirements for creating theme engines have been lowered substantially.*

![technology stack](/files/theme_tech_stack_0.png)

All layers can implement a themed representation of the output, but (with a few exceptions) only within the theming layers can overrides occur. Theme engines can override themed output from core and modules, while themes can override everything else.

Note that the PHPTemplate engine does not override any output but other theme engines can. There is a special case where a module can influence the output or override absolutely everything, but it is for very special cases and should not interfere in most situations. For example, the [Theme Developer](/project/devel_themer) module does this to [aid theme development](/node/209561). More details will be discussed in a [later section](/node/173880).

You can ignore most of this if your theme will be [styled entirely through CSS](/node/171209), but when the markup needs to be altered it is important to know how to [get to the source of the output so it can be altered](/node/173880).

- *Note that the Drupal core and countless modules always use [themable functions](http://api.drupal.org/api/group/themeable/7) and [template files](http://api.drupal.org/api/search/6/.tpl.php) to output the presentation markup. *Never hack on files outside your theme folder* as that would lead to complications when there is a need to update. Doing this is known as "forking". The power of open source lies in having the community manage bug fixes and add new features. Once you start a fork you create a closed system, and you lose the leverage of the community. Drupal provides all the functionality to override the presentation layer. If you ever have to hack on files outside the theme, either you are doing something wrong or you have found a bug. In the latter case, please file a [bug report](/node/317). Or even better, [provide a patch file](/patch) to fix the problem.*
- *For those familiar with the PHPTemplate engine in previous incarnations, almost all the functionality has been moved deeper into core. The job of PHPTemplate now is to only discover theme functions and templates on behalf of the theme. It is less of an engine and more of a theme helper. PHPTemplate was originally written by [Adrian Rossouw](/user/1337) for 4.7. The changes in 6 were the work of [Earl Miles](/user/26979). [An extended forum discussion](/node/7133) provides some of the reasoning behind the initial creation of the engine and the [issue queue for the new direction](/node/130987) in 6.*
