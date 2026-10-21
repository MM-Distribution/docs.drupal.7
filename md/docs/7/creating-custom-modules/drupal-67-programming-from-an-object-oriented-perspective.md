---
title: "Drupal 6/7 programming from an object-oriented perspective"
source_url: "https://www.drupal.org/docs/7/creating-custom-modules/drupal-67-programming-from-an-object-oriented-perspective"
page_type: page
last_updated: "Last updated on 23 December 2016"
published: "2005-04-04T19:52:42+00:00"
modified: "2016-12-23T07:19:17+00:00"
breadcrumb: ["Drupal 7", "Creating custom modules in Drupal 7"]
fetched: "2026-10-21T07:27:41Z"
raw: "raw/docs/7/creating-custom-modules/drupal-67-programming-from-an-object-oriented-perspective.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Drupal 6/7 programming from an object-oriented perspective

***Note:** This page is about Drupal 7's (and prior versions') architecture. Drupal 8 changed a great deal and now uses actual OOP practices.*

Drupal often gets criticized by those who look to its source code and API expecting to find certain familiar aspects of object-oriented programming (OOP). For example, the word "class" does not appear in Drupal code as often as some might expect. Some have viewed this as a deficiency.

Although Drupal does not make thorough use of the native OOP features of PHP, the Drupal code base and API does reflect some principles found in object-oriented programming and design. This article describes the architecture of Drupal from an OOP perspective, so that programmers familiar with OOP can evaluate Drupal in light of object-oriented design principles, and hopefully feel more at home in the Drupal code base. In the future, as both PHP and Drupal become more mature, Drupal may increasingly adopt the native OOP features of PHP.

## Motivations for Current Design

Back as far as version 4.6 of Drupal, the decision was made not to use PHP's [class](http://us3.php.net/manual/en/language.oop5.php) construct. This decision was made for several reasons.

First, PHP's support for object-oriented constructs was much less mature at the time of Drupal's design. Drupal was built on PHP 4, and most of the improvements in PHP 5 relate to its [object-oriented features](http://www.php.net/manual/en/migration5.oop.php).

Second, Drupal code is highly compartmentalized into modules, each of which defines its own set of functions. The inclusion of files is handled inside functions as well; PHP's performance suffers if unneeded code is included, so Drupal attempts to load as little code as possible per request. This is a critical consideration, especially in the absence of a [PHP accelerator](http://www.zend.com/store/products/zend-platform/index.php): the act of compiling the code accounts for more than half of the time to complete a Drupal page request. Functions are therefore defined inside other functions in Drupal, with respect to the runtime scope. While this is perfectly legal for bare functions, PHP does not allow the same kind of nesting with class declarations. This means that the inclusion of files defining classes must be "top-level," and not inside any function, which leads either to slower code (always including the files defining classes) or a large amount of logic in the main index.php file.

Finally, Drupal attempts to adopt some OOP design aspects that PHP's OOP system does not yet support, or did not support at the time of adoption.

For instance, the Drupal [theme system](http://api.drupal.org/api/group/themeable) relies on an OOP concept similar to [Objective-C's "categories"](https://developer.apple.com/library/ios/documentation/Cocoa/Conceptual/ProgrammingWithObjectiveC/CustomizingExistingClasses/CustomizingExistingClasses.html#//apple_ref/doc/uid/TP40011210-CH6-SW2), (this concept is also similarly known as 'open classes' in Ruby, 'modifying object prototypes' in Javascript, or 'extension methods' in C#).

In Drupal 7, some of this has changed: Drupal 7, for the first time, requires PHP 5, and there are now a few modules in Drupal that use PHP's class system. However, the central structure of Drupal remains the same, and most of Drupal still does not use the PHP class construct.

## OOP Concepts in Drupal

Despite the lack of explicitly-declared classes in Drupal, many object-oriented paradigms are still used in its design. There are many sets of "essential features" that are said to be necessary to classify a system as object-oriented; we will look at one of the [more popular definitions](http://en.wikipedia.org/wiki/Object-oriented_programming) and examine some ways in which the central architecture of Drupal exhibits those characteristics.

### Objects

There are many constructs in Drupal that fit the description of an "object". Some of the more prominent Drupal components that could be considered objects are modules, themes, nodes, and users.

Nodes are the basic content building blocks of a Drupal site, and bundle together the data that makes up a "page" or "story" on a typical site. The methods that operate on this object are defined in node.module, usually called by the node_invoke() function. User objects similarly package data together, bringing together information about each account on the site, profile information, and session tracking. In both cases, the data structure is defined by a database table instead of a class. Drupal exploits the relational nature of its supported databases to allow other modules to extend the objects with additional data fields.

Modules and themes are object-like as well, filling the "controller" role in many ways. Each module is a source file, but also bundles together related functions and follows a pattern of defining Drupal hooks.

### Abstraction

Drupal's [hook system](http://api.drupal.org/api/group/hooks) is the basis for its interface abstraction. Hooks define the operations that can be performed on or by a module. If a module implements a hook, it enters into a contract to perform a particular task or return a particular type of information when the hook is invoked. The calling code need not know anything about the module or the way the hook is implemented in order to get useful work done by invoking the hook.

### Encapsulation

Like most other object-oriented systems, Drupal does not have a way of strictly limiting access to an object's inner workings, but rather relies on convention to accomplish this. Since Drupal code is based around functions, which share a single namespace, this namespace is subdivided by the use of prefixes. By following this simple convention, each module can declare its own functions and variables without the worry of conflict with others.

Convention also delineates the public API of a class from its internal implementation. Internal functions are prefixed by an underscore to indicate that they should not be called by outside modules. For example, \_user_categories() is a private function which is subject to change without notice, while user_save() is part of the public interface to the user object and can be called with the expectation that the user object will be saved to the database (even though the method of doing this is private).

### Polymorphism

Nodes are polymorphic in the classical sense. If a module needs to display a node, for example, it can call node_build() on that node, followed by drupal_render(), to get an HTML representation. The actual rendering, though, will depend on which type of node is passed to the function; this is directly analogous to having the class of an object determine its behavior when a message is sent to it. Drupal itself handles the same introspection tasks required of an OOP language's runtime library.

Furthermore, the rendering of the node in this example can be affected by the active theme. Themes are polymorphic in the same way; the theme is passed a "render this node" message, and responds to it in a different way depending on the implementation of the active theme, though the interface is constant.

### Inheritance

Modules and themes can also be thought of as classes that inherit their behavior from an abstract base class (although both can also define whatever functions they please). In the case of themes, the behavior of the abstract base class is determined by the functions in theme.inc and the default theming implementations in enabled modules. A theme can either override the default rendering of any interface component or let the default rendering be used. Modules similarly have the selection of all Drupal hooks to override at will, and may pick and choose which ones to implement.

## Design Patterns in Drupal

Much of Drupal's internal structure is more complicated than simple inheritance and polymorphism, however. The more interesting features of the system result from using established software design patterns. Many of the patterns detailed in the seminal "Gang of Four" (Gamma, Helm, Johnson, and Vlissides) [Design Patterns book](http://en.wikipedia.org/wiki/Design_Patterns) can be observed in Drupal, for instance.

### Singleton

If we are to think of modules and themes as objects, then they follow the singleton pattern. In general, these objects do not encapsulate data; what separates one module from another is the set of functions it contains, so it should be thought of as a class with a singleton instance.

### Decorator

Drupal makes extensive use of the decorator pattern. The polymorphism of node objects was discussed earlier, but this is only a small piece of the power of the node system. More interesting is the use of the various node hooks (hook_node_load(), hook_node_view(), etc.), which allow arbitrary modules to extend the behavior of all nodes.

This feature allows for a wide variety of behaviors to be added to nodes without the need for subclassing. For instance, a basic story node has only a few pieces of associated data: title, author, body, teaser, and a handful of metadata. A common need is for files to be uploaded and attached to a node, so one could design a new node type that had the story node's features plus the ability to attach files. Drupal's upload module satisfies this need in a much more modular fashion by using the node API to grant every node that requests it the ability to have attached files.

This behavior could be imitated by the use of decorators, wrapping them around each node object. More simply, languages that support categories, like Objective-C, could augment the common base class of all node objects to add the new behavior. Drupal's implementation is a simple ramification of the hook system and the presence of node_invoke().

### Observer

The above interaction is also similar to the use of observers in object-oriented systems. This Observer pattern is pervasive throughout Drupal, as many of Drupal's hooks essentially allow modules to register as observers of Drupal's objects. For instance, when a modification is made to a vocabulary in Drupal's taxonomy system, a taxonomy hook such as hook_taxonomy_vocabulary_update() is called in all modules that implement it. By implementing the hook, the modules have registered as observers of the vocabulary object; any changes to it can then be acted on as is appropriate.

### Bridge

The Drupal [database abstraction layer](http://api.drupal.org/api/group/database) is implemented in a fashion similar to the Bridge design pattern. Modules need to be written in a way that is independent of the database system being used, and the abstraction layer provides for this. New database layers can be written that conform to the API defined by the bridge, adding support for additional database systems without the need to modify module code.

### Chain of Responsibility

Drupal's [menu system](http://api.drupal.org/api/group/menu) follows the Chain of Responsibility pattern. On each page request, the menu system determines whether there is a module to handle the request, whether the user has access to the resource requested, and which function will be called to do the work. To do this, a message is passed to the menu item corresponding to the path of the request. If the menu item cannot handle the request, it is passed up the chain. This continues until a module handles the request, a module denies access to the user, or the chain is exhausted.

### Command

Many of Drupal's hooks use the Command pattern to reduce the number of functions that are necessary to implement, passing the operation as a parameter along with the arguments. In fact, the hook system itself uses this pattern, so that modules do not have to define every hook, but rather just the ones they care to implement.

## Why Not to Use Classes

The above hopefully clarifies the ways in which Drupal embodies various OOP concepts. Why, then, doesn't Drupal move in the direction of using classes to solve these problems in the future? Some of the reasons are historical, and were discussed earlier. Others, though, become clearer now that we have stepped through some of the design patterns used in Drupal.

A good example is the extensibility of the theme system. A theme defines functions for each of the interface elements it wants to display in a special way. As noted earlier, this makes themes seem like a good candidate to inherit from an abstract base class that defines the default rendering of the elements.

What happens, though, when a module is added that adds a new interface element? The theme should be able to override the rendering of this element as well, but if a base class is defined, the new module has no way of adding another method to that class. Complicated patterns could be set up to emulate this behavior, but Drupal's theme architecture quite elegantly handles the situation using its own function dispatch system. In this case and others like it, the classes that on the surface would seem to simplify the system would end up making it more cumbersome and difficult to extend.

### Room for Improvement

While Drupal does reflect many object-oriented practices, there are some aspects of OOP that could be brought to bear on the project in more powerful ways.

Encapsulation, while adequate in theory, is not applied consistently enough across the code base. Modules should more rigorously define which functions are public and which are private; the tendency right now is to publish most functions in the public namespace even if the interface is volatile. This problem is exacerbated by Drupal's policy of foregoing backward compatibility in exchange for cleaner APIs whenever necessary. This policy has led to some very good code, but would need to be exercised much less often if better encapsulation conventions were followed.

Inheritance is also weak in the system. While, as noted above, all modules share a common set of behavior, it is difficult to extend this to new modules. One can create new modules easily that augment the behavior of existing ones, but there is not a way to override just some of a module's behavior. The impact of this can be marginalized by breaking large modules into smaller "a la carte" bundles of functionality, so that undesired aspects of a module may be more easily left out of the system.

### Multiple Paradigms

Drupal is on the surface a procedural system, because it is built in a procedural language (PHP without classes). The paradigm behind a piece of software is not entirely dependent on its representation in code, however. Drupal is not afraid to borrow concepts from many disparate programming paradigms where it is convenient. A great deal of the power of Drupal comes from its underlying relational database, and relational programming techniques that mirror it. The fact that Drupal's work, much like that of any web application, consists of many reactions to discrete and rapid page requests should make the behavior of the system resonate with proponents of event-driven programming. To an aspect-oriented programmer, the invocation of hooks in arbitrary modules may look strikingly similar to a pointcut. And, as should be abundantly clear by now, Drupal is no stranger to object-oriented concepts either.
