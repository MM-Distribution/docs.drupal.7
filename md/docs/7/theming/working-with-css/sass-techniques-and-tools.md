---
title: "Sass techniques and tools"
source_url: "https://www.drupal.org/docs/7/theming/working-with-css/sass-techniques-and-tools"
page_type: page
last_updated: "Last updated on 11 March 2021"
published: "2013-02-10T08:47:32+00:00"
modified: "2021-03-11T21:35:31+00:00"
breadcrumb: ["Drupal 7", "Theming Drupal 7", "Working with CSS"]
fetched: "2026-10-21T08:15:29Z"
raw: "raw/docs/7/theming/working-with-css/sass-techniques-and-tools.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Sass techniques and tools

[Sass](http://sass-lang.com/) is a meta-language on top of CSS that’s used to describe the style of a document cleanly and structurally, with more power than flat CSS allows.

Sass provides a simpler, more elegant syntax for CSS and implements various features that are useful for creating manageable stylesheets -- such as variables, functions, nested rules and more. See the [Sass documentation](http://sass-lang.com/) for details.

**Compass** is an open-source Sass framework. It includes common design patterns such as setting vertical rhythm and converting between pixels and ems, as well as tools like automatic browser-prefixing of CSS3 rules. Compass is an extension to Sass, but is not required

Compass is often used with Sass -- and suggested below -- because it can automatically compile your Sass using the `compass watch` command. For more information, see the [Compass documentation](http://compass-style.org/).

Here is an article on [Sass CSS preprocessor](http://noeticforce.com/sass-css-preprocessor-framework-getting-started-guide) that talks about everything you need to get started with Sass.

Given below are quick instructions on Sass installation -

### Sass installation

#### Linux

1\. Sass is written in Ruby. Install Ruby, if you don't already have it installed:

`sudo apt-get install ruby1.9.1`

2\. Install Sass:

`sudo gem install sass`

3\. Install Compass (optional):

`sudo gem install compass`

#### Windows

1\. Sass is written in Ruby. [Install Ruby](http://rubyinstaller.org/downloads/ "Ruby"), if you don't already have it installed.

2\. Install Sass:

`gem install sass`

3\. Install Compass (optional):

`gem install compass`

#### Mac OS X

1\. Sass is written in Ruby. Install Ruby, if you don't already have it installed:

`sudo apt-get install ruby1.9.1`

2\. Install Sass:

`sudo gem install sass`

3\. Install Compass (optional):

`sudo gem install compass`

### Creating a project with compass

Go to the directory where you would like to create your project. For a custom theme, this will be sites/all/themes:

`cd path/to/where-you-want-your-project`

Create a folder with your project name and install your project inside of it:

`compass create project-name`

> **(Optional)** You can modify, relocate or change the name of css and javascript directory by editing config.fb file.

#### Automatically watching and compiling changes with compass

Change directory to be inside your project folder:

`cd path/to/project`

Use Compass to automatically compile changed Sass files:

`compass watch`  
or (shortcut)  
`compass watch path/to/project`

Alternatively, to manually compile:

`compass compile [options]`

For specific Compass options and more commands see [Compass command line documentation](http://compass-style.org/help/documentation/command-line) and [production CSS with Compass documentation](http://compass-style.org/help/tutorials/production-css/).

### Some useful examples of Sass

#### Variables

Use variables to store something like a color or width and then use it throughout your stylesheets. Sass also supports basic math operations with variables.

### .SCSS syntax

``` php
$blue: #3bbfce;
$width: 100px;
.main{
  color: $blue;
  width: $width;
}

.footer {
  width: $width / 2;
}
```

### .CSS output

``` php
.main{
  color: #3bbfce;
  width: 100px;
}

.footer {
  width: 50px;
}
```

#### Nesting in Sass

Sass avoids repetition by nesting selectors within one another. The same thing works with properties.

### .SCSS syntax

``` php
#navigation #main-menu ul {
  background: #e5e5e5;
  border: 1px solid #e2e2e2;
  li {
    padding: 5px 10px 5px 10px;
    &:hover {
      background: #ccc;
      a {
        color: #fff;
      }
    }
    a {
      text-decoration: none;
      text-shadow: 1px 2px rgb(211, 200, 200);
   }
  }
}
```

### .CSS output

``` php
#main-menu ul {
  background: #e5e5e5;
  border: 1px solid #e2e2e2;
}

#navigation #main-menu ul li {
  padding: 5px 10px 5px 10px;
}

#navigation #main-menu ul li:hover {
  background: #ccc;
}

#navigation #main-menu ul li:hover a {
  color: #fff;
}

#navigation #main-menu ul li a {
  text-decoration: none;
  text-shadow: 1px 2px #d3c8c8;
}
```

#### Mixins in Sass

Even more useful than variables, mixins allow you to re-use whole chunks of CSS, properties or selectors. You can even give them arguments.

### .SCSS syntax

``` php
@mixin left($dist) {
  float: left;
  margin-left: $dist;
}

#data {
  @include left(10px);
}
```

### .CSS output

``` php
#data {
  float: left;
  margin-left: 10px;
}
```
