---
title: "Contributed versus custom code and everything in between"
source_url: "https://www.drupal.org/docs/7/site-building-best-practices/contributed-versus-custom-code-and-everything-in-between"
page_type: page
last_updated: "Last updated on 5 September 2025"
published: "2017-11-03T14:44:39+00:00"
modified: "2025-09-05T20:48:19+00:00"
breadcrumb: ["Drupal 7", "Drupal 7 site building best practices"]
fetched: "2026-10-21T07:12:23Z"
raw: "raw/docs/7/site-building-best-practices/contributed-versus-custom-code-and-everything-in-between.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Contributed versus custom code and everything in between

Drupal core offers common functionality out of the box but the more specific the demands of your web application, the more likely you need to extend Drupal with contributed modules or write custom code.

When building and maintaining a Drupal application we should try to find a balance between:

- not writing too much custom code that needs lots of development time and might turn into an unmaintainable mess, especially if it needs to be maintained by others than its creator
- not installing too many contributed modules that might result in an [over-engineered](https://stackoverflow.com/a/1001150/523688 "design - What is "over-engineering" as applied to software? - Stack Overflow") application (code for functionalities you don't need).

Nice to read what we shouldn't do, but then, what should we do? Below guidelines help you to walk the thin line between the two *don'ts* just described above and show that contributed versus custom code is not necessarily a black or white decision but contains shades of grey.

Based on the requirements, make an analysis of your project on what potential modules to use and what functionalities you might have to write custom code for.  This results in specifications. Working [Agile](https://en.wikipedia.org/wiki/Agile_software_development "Agile software development - Wikipedia") you will always be able to make adjustments along the way to either [requirements or specifications](https://softwareengineering.stackexchange.com/a/121292 "What is the difference between requirements and specifications? - Software Engineering Stack Exchange").

## Preference order in choosing modules

For a particular functionality in your web application, the following order is recommended for choosing the right solution.

![](/files/Code%20Development%20Flow.png)

### **Use the already installed modules first and consider to accomplish your functionality with configuration instead of code**

To [avoid too many modules](https://www.drupal.org/docs/7/site-building-best-practices/avoiding-too-many-modules) some new features can be built with configuration only. A typical example is a list of data that can be accomplished with the [Views](https://www.drupal.org/project/views) module (in Drupal 8 part of core).

### **Extend using the Drupal API or the API of already installed modules**

An example is writing a [Views handler](https://api.drupal.org/api/views/views.api.php/group/views_handlers/7.x-3.x). While this article initially appears to be in contradiction, it is actually similar to the [Invented Here](http://mikecr.it/ramblings/drupal-and-invented-here) approach where you extend code that already is present. Keep in mind that custom code is usually not plain PHP but extends the Drupal API, whether provided by core or contributed modules (for example Rules).

### **Use a contributed module**

If the required functionality cannot be accomplished with the existing code (or extending it through an API), choose a contributed module.

[Checklist on Google Forms](https://goo.gl/forms/RFvhrykp1bUyggID2 "Review a Drupal.org contributed module") with the below questions to answer (as [PDF](https://www.drupal.org/files/Review%20of%20a%20Drupal.org%20contributed%20module%20-%20Google%20Forms.pdf) instead). You can receive your answers on your provided email address to use when you are requested to review a module (e.g. in JIRA).

**Some considerations to select a module to use (in no particular order):**

- Use a mainstream multi-purpose module that can be reused for other solutions as well. Examples are [Rules](https://www.drupal.org/project/rules) to define logic or [Display Suite](https://www.drupal.org/project/ds) to flexibly control output and layout.

- If the above is not feasible use a module that does what you need and not much more. In case it does offer too many features for your needs, consider to [propose a patch](https://www.drupal.org/patch/submit) with the possibility to put unwanted features in submodules that can be disabled.

- Does the module [provide alter hooks](https://www.drupal.org/docs/7/creating-custom-modules/creating-drupal-7-hooks)? If it doesn't, consider [providing a patch](https://www.drupal.org/patch/submit) in the issue queue that extends the module with it.

- How many sites report this module to be installed? Look at the statistics to have a breakdown per version to get an impression of the growth of the latest. Consider young modules take some time to be "discovered" and might have only a few or even no site installs reported despite being of good quality. In that case, it's worth checking the other modules by the same author.

- When was the last commit?

- Is it actively maintained? Do not rely on the indicated status only but check if there are no old issues in *Reviewed and Tested By Community (RTBC)* or *Needs review (NR)* status?

- How many bugs are there in the issue queue for the version you plan to install?

- If on Drupal 7 [is there a Drupal 8 version](https://www.drupal.org/docs/7/site-building-best-practices/building-drupal-7-with-drupal-8-in-mind) in case we need to upgrade in the future?

- Is there a stable version?

- Is it covered by the [security advisory policy](https://www.drupal.org/security-advisory-policy)? If it does it means the author went through a one-time code quality [review process](/node/539608) to get permission to mark their projects as covered for security advisories.

- Is there documentation? Apart from a link to a manual of some sort, preferably on Drupal.org, it does also include the project page itself (is it clear?) and the presence of a README.txt and UPGRADE.txt if applicable.

- If there is a demo, check it out. It shows the author cared about promoting their work.

- Code quality: How does it perform when we apply [Code Sniffer](https://www.drupal.org/node/1419988) on the code? Open an issue 'Code Sniffer suggestions' and [provide a patch](https://www.drupal.org/patch/submit). Alternatively, r[eview a Drupal project online](https://pareview.sh/ "PAReview").

- Is there a unit test included in the code for [D7](https://www.drupal.org/docs/7/testing/unit-testing-with-simpletest "Unit Testing with SimpleTest | Drupal.org") or [D8](https://www.drupal.org/docs/8/phpunit "PHPUnit in Drupal 8 | Drupal.org") and turned on? Check the *Automated testing* tab on the project page to find out. If so, it is less likely bugs will slip in during ongoing development as each supplied patch is automatically tested against it (does it break functionalities?).

- For specific functionality make sure to also check the published [sandbox modules](https://www.drupal.org/search/site/the?f%5B0%5D=&f%5B1%5D=&f%5B2%5D=&f%5B3%5D=&f%5B4%5D=sm_field_project_type%3Asandbox&f%5B5%5D=&f%5B6%5D=ss_meta_type%3Amodule&solrsort=ds_created+desc). They are often overlooked but contain some well-coded gems. Some developers do not promote their code into full projects to avoid the maintenance burden of feature and support requests or having to write documentation. Do not hesitate to ask the maintainer to publish it as a full project. Once it is, it is more likely been found and used by others, and receive the attention to keep it maintained.

For more inspiration: [\#2186377: Highlight projects that follow Best Practices](/project/drupalorg/issues/2186377 "Status: Needs work")

### **Extend a contributed module**

Sometimes you find a module that can be extended to do what is needed. Instead of writing custom code this is preferred mainly because:

- No code needs to be written from scratch.

- Community members can review and improve the code.

- Security issues are more likely to be spotted.

- It forces your developers to write reusable generic code that results in a more solid solution than with site-specific code. It is more likely you can adopt the same solution for similar use cases that come up in the future.

- If the developer leaves your company the code is more likely to receive continued maintenance and will probably be easier to be maintained by the other developers. If possible make sure at least two of your developers are involved as maintainers.

There are basically three ways to extend the functionality of a contributed module:

- If you think your new functionality or improvement will be desired by many of the module's users create a feature request in the issue queue. Then [provide a patch](https://www.drupal.org/patch/submit) that adds the new feature directly. Make sure that a module upgrade will not break anything or changes the expected behavior or output for existing websites.
- If the new functionality is more specific provide a patch that adds it as a sub-module that can be enabled only if needed.
-  If the new functionality is very specific write a module that extends the functionality with a dependency on the base module to avoid code duplication. It can be installed only if needed. Ask the maintainer to mention the extension module on their project page to make sure people can find your new module.

### **Write a contributed module**

If no contributed module is available instead of writing custom code it is preferred to publish the code as a contributed module (full project or sandbox) for the same reasons as mentioned previously.

Feel free to mirror host your module elsewhere (for example [GitHub.com](https://github.com/)) besides Drupal.org if you prefer forking over patching. That way you still take advantage of Drupal's automatically built releases and be able to push out new releases to users that check for updates.

### **Write custom code**

Of course, if extending and overriding contrib takes much more time than pure "stand-alone" custom code, consider using the [Invented Here](http://mikecr.it/ramblings/drupal-and-invented-here) approach. But still, if your solution is pretty generic it is maybe worth to contribute to Drupal.org, even as a sandbox module. If others need the same lightweight solution, it is there for them.

Also if the needed code cannot be built as a generic solution (with maybe a site-specific configuration) but is site-specific then write a custom module. Even then consider splitting it up in a contributed generic part and a site-specific implementation using alter hooks. Writing custom code should in most cases be the last resort.

Apart from theming (for example templates and preprocess functions) ideally custom code should stay limited to alter hooks, some definitions of a Views handler or Rules action. Maybe a custom entity if you have requirements for your content that do not fit the node entity or others provided by a contributed module (for example [the ones of Drupal Commerce](https://drupalcommerce.org/developer-guide/core-architecture/entities)). Also then, you should consider making it generic enough to publish it as a contributed module.

## Do not hack any code that makes part of the project (core or contributed) but override it if you need to alter its behavior

See also [Never hack core](https://www.drupal.org/docs/7/site-building-best-practices/never-hack-core).

If you hack the code directly it will be overwritten once you upgrade the code to a newer version. The recommended way is to [use hooks](https://www.drupal.org/docs/8/creating-custom-modules/understanding-hooks). If the code does not allow for that you can either:

- [provide a patch](https://www.drupal.org/patch/submit) in the issue queue of the project adding or changing the desired functionality directly

- [provide a patch](https://www.drupal.org/patch/submit) for the project adding an alter hook that you then use in custom code.

In that case, you can put the applied patch file in the relevant module folder of your project until the change has been committed in the stable version. The patch will not be removed if the module gets upgraded and is an indication that probably a code change should be applied to the module to work as before. You can extend that with [other](https://www.drupal.org/project/patch_manager) [solutions](https://bitbucket.org/davereid/drush-patchfile) to track the patches you applied in your web application.

## Use stable versions if possible

Using a development version is not recommended mainly because it is not representing a fixed state. If you upgrade to the latest dev version and it causes issues, it is cumbersome to roll back (although possible [using commit hashes](https://stackoverflow.com/a/4114122/523688) or saving the older version as a backup before the upgrade).

Using a [sandbox module](https://www.drupal.org/docs/8/extending-drupal-8/installing-sandbox-modules) is possible. This might still be preferred over creating custom code (see preference order above). If you find a good sandbox module request the maintainer to release it as a full project in the issue queue. Some companies only allow for stable full modules to be used in their projects.

## Bottom line

If you have doubts about keeping your future application maintainable while avoiding over-engineering, maybe you should consider solutions other than Drupal and make an analysis with those. Consider also to adjust either the [requirements](https://softwareengineering.stackexchange.com/a/121292 "What is the difference between requirements and specifications? - Software Engineering Stack Exchange") or the budget.

## Other resources

- [The most important decision in developing a Drupal site: contributed vs. custom development – CivicActions](https://guidebook.civicactions.com/en/latest/practice-areas/engineering/drupal/most-important-decision-in-developing-a-drupal-site-contributed-vs-custom-development/)
- [Go custom or use a contributed module? \| Web Omelette](https://www.webomelette.com/go-custom-or-use-contributed-module)
- [Understanding Views versus custom code \| Drupal.org](https://www.drupal.org/docs/7/modules/views/understanding-views-versus-custom-code)
- [How and Why to Patch a Drupal Module \| Phase2](https://www.phase2technology.com/blog/how-and-why-patch-drupal-module)
- [Drupal and "Invented Here" \| Mike Crittenden](http://mikecr.it/ramblings/drupal-and-invented-here)
- [Chris Jansen and Jeffrey A. McGuire: Challenges in Getting your Open Source Company to Contribute - YouTube](https://www.youtube.com/watch?v=Uhx4cRn2_jo#t=28m32s "Starts video at most interesting part")
