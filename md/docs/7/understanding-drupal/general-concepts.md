---
title: "General concepts"
source_url: "https://www.drupal.org/docs/7/understanding-drupal/general-concepts"
page_type: page
last_updated: "Last updated on 16 October 2022"
published: "2005-04-01T17:31:14+00:00"
modified: "2022-10-16T20:31:17+00:00"
breadcrumb: ["Drupal 7", "Understanding Drupal 7"]
fetched: "2026-10-21T05:50:06Z"
raw: "raw/docs/7/understanding-drupal/general-concepts.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# General concepts

This page discusses some general concepts that will be useful as you begin to explore Drupal. For more details on these concepts, follow the links to additional documentation.

### Node (Content)

A *node* is the generic term for any piece of content on your web site. The *content type* of the node will define what fields (or specific information) that node displays. For example, a basic *Page* content type has (minimally) two fields: title and body. Other examples content types are: *Book* (which may have fields like Title, Author, Summary, Review, Price), *Profile* (which may have fields like Name, Job Title, Department, Email, Phone Number) and *Product* (which may have fields like Name, Price, Height, Width, Weight, Make, Model, Year).

The word "node" is not meant in the mathematical sense as part of a network.

For more useful materials on content administration in Drupal, see [Resource Guide: Tools for Content Administration in Drupal](/resource-guides/content-administration).

### Entity types

An *entity type* is a useful abstraction to group fields together. Entity types are used to store and display data, which can be nodes (content), comments, taxonomy terms, user profiles or something custom developed.

Read more about Entities in the [Entity API](http://drupal.org/node/1261744 "An Introduction to Entities") documentation.

### Comment

Comments are another type of content you can have on your site (as long as the core Comment module is enabled.). Each comment is typically a small piece of content that a user submits and is attached to a particular node. For example, each piece of discussion attached to a particular forum topic node is a comment.

Read more about comment administering [here](https://www.drupal.org/node/777676)

### Taxonomy

Drupal has a system for classifying content known as *taxonomy*. This is provided by the core Taxonomy module. You can define your own *vocabularies* (groups of *taxonomy terms*) and add terms to each vocabulary. Each vocabulary can then be attached to one or more content types, and in this way, nodes on your site can be grouped into categories, tagged, or classified in any way you choose.

Read more about this concept in the [taxonomy module](http://drupal.org/documentation/modules/taxonomy) documentation.

### User

A user is a type of entity which represents a real-world website user. By default, a user has a set of properties including their username, password, role, and e-mail address. However, they may also have other properties provided by other modules and can be extended with new fields. For example, you could add a new "Link" field for a user's Twitter address.

### Module

A module is software (code) that extends Drupal functionality. Modules fall into one of three categories:

- **Core** modules are those included with the main download of Drupal. These can be turned on or off without downloading additional components. Examples include *Blog, Book, Poll*, or *Taxonomy*.
- **Contributed** modules are downloaded from the Modules download section of drupal.org, and installed within your Drupal installation. Examples include *Panels, Views* or *Metatag*.
- **Custom** modules are modules you write yourself. This requires a thorough understanding of Drupal, PHP programming, and Drupal's API.

For a collection of useful materials about module development, see [Module Development with Drupal](/module-development).

### Regions & Blocks

Pages on your Drupal site are laid out in *Regions*. These can include the header, footer, sidebars, featured top, featured bottom, main content regions etc... Your theme may define additional regions.

*Blocks* are discrete chunks of information that are displayed in the regions of your site's pages. Blocks can take the form of static chunks of HTML or text, menus (which are for site navigation), the output from modules (e.g. hot forum topics), or dynamic listings that you've created yourself (e.g. a list of upcoming events).

### Menus

There are four standard menus in Drupal 7:

- The **Main** menu is built by site administrators and displayed automatically in the page header of many themes (and if not, you can enable their blocks to display them).
- **Management** is the administration menu, and is presented in the Admin toolbar.
- **Navigation** is a catch-all menu that usually contains links supplied by modules on your site.
- **User** menu contains links to the User account and the logout link.

You can also create your own custom menus and display them by enabling their associated blocks.

You can customize menus in several ways, such as reordering menu items by setting their “weight” or simply dragging them into place, renaming menu items, and changing the link title (the tooltip that appears when you mouse over a menu item). You can move a menu item into a different menu by editing the Parent property of the menu item.

You can also add custom menu items to a menu, from the Add menu item tab of the Menu administration screen. To create a menu item, you will need to provide the path to the content.

In all cases a menu item will only be shown to a visitor if they have the rights to view the page it links to. For example, the admin menu item is not shown to visitors who are not logged in.

### Theme

The *Theme layer* is separate from the data layer, the functionality extension layer (module) and Core. Theme controls the appearance (look and feel) of your site, or how your site is displayed, including the graphic look, layout, and colors. A theme consists of one or more PHP template files that define the HTML output of your site's pages, along with one or more CSS files that define the layout, fonts, colors, and other styles.

For a collection of useful materials for themes, see [Theming and Front End Development with Drupal](/theming).

### Views

Although not all sites have Views, most sites include the Views module because of the excellent tools it provides. Views allows people to choose a list of nodes or other entities and present them as pages, blocks, RSS feeds, or other formats. The main use case for views is to create dynamically updating lists of content (for example, a listing of latest news), based on properties of that content (in the case of the news listing, that the content type is “News” and sorted by publication date).

### Views Layout

Views can be created as a page or blocks. View's data can be themed by creating custom templates. Templates can be created to display output, style output and field content. In display output, the user can override the default order of views content structure. In Styled output user can theme the entire HTML structure of view content and for field output for customizing field data.

### Database

Drupal stores information in a database. Within this database, each type of information has its own database table. For example, the basic information about the nodes of your site are stored in the Node table, and each field stores its data in a separate table (which Drupal creates automatically). Comments and Users also have their own database tables, as do roles, permissions, and other settings.

The most common database for Drupal is MySQL. However, you can also run Drupal on other database systems, such as PostgreSQL, as well.

### Path

When you visit a URL within your Drupal site, the part of the URL after your base site address is known as the *path*.

When you visit a path in your Drupal site, Drupal figures out what information should be sent to your browser by checking its list of menu items and routes. Generally, Drupal allows each module to define paths that the module will be responsible for, and when you choose to visit a particular path Drupal asks the module what should be displayed on the page.

For example, the page you are now viewing is <http://drupal.org/node/19828> - the path is "node/19828". The module that is responsible for this path is the core Node module, so when you visit this page, Drupal lets the Node module determine what to display.

### Bootstrap

The [bootstrap](http://api.drupal.org/api/drupal/includes!bootstrap.inc/function/drupal_bootstrap/7) is the CPU (central processing unit) of Drupal. In other interactive software environments this is sometimes called the event loop. Drupal's core is somewhat similar as it sits around waiting for a *path* request, and then starts processing that request.

### Permissions

*Permissions* can be set to control what users have access to view and/or edit particular areas of a site. These permissions pertain to registered users (i.e. administrators, content editors, site members) and non-registered users. Permissions can be set to be very specific and granular, making for a powerful feature to use when developing a site's structure.

## See also

[Drupal Terminology](https://www.drupal.org/node/176052)
