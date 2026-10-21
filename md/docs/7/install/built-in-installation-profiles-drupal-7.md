---
title: "Built-in Installation Profiles"
source_url: "https://www.drupal.org/docs/7/install/built-in-installation-profiles-drupal-7"
page_type: page
last_updated: "Last updated on 5 February 2018"
published: "2011-04-14T22:07:16+00:00"
modified: "2018-02-05T10:42:15+00:00"
breadcrumb: ["Drupal 7", "Installing Drupal 7"]
fetched: "2026-10-21T05:55:30Z"
raw: "raw/docs/7/install/built-in-installation-profiles-drupal-7.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Built-in Installation Profiles

Drupal includes installation profiles that control what's included as you get started. Select from either the Standard or the Minimal profile.

- The **Standard** profile has several core modules enabled. It has more default configuration set up, including several default admin tools. This profile does more to show what core can do, and can save site building time by having defaults for common use cases.
- The **Minimal** profile has only a few very basic modules installed. This profile is useful if you only want very specific features, or if it will take more work to undo the defaults provided with the Standard profile.

## Details

The following table lists the modules enabled by the Standard profile, as compared to the Minimal profile:

| Module            | Minimal | Standard |
|-------------------|---------|----------|
| Block             | x       | x        |
| Color             |         | x        |
| Comment           |         | x        |
| Contextual Links  |         | x        |
| Dashboard         |         | x        |
| Database Logging  | x       | x        |
| Field             | x       | x        |
| Field SQL storage | x       | x        |
| Field UI          |         | x        |
| File              |         | x        |
| Filter            | x       | x        |
| Help              |         | x        |
| Image             |         | x        |
| List              |         | x        |
| Menu              |         | x        |
| Node              | x       | x        |
| Number            |         | x        |
| Options           |         | x        |
| Overlay           |         | x        |
| Path              |         | x        |
| RDF               |         | x        |
| Search            |         | x        |
| Shortcut          |         | x        |
| System            | x       | x        |
| Taxonomy          |         | x        |
| Text              | x       | x        |
| Toolbar           |         | x        |
| User              | x       | x        |

Modules enabled by profile

***Note:** There are core modules not enabled in either profile, and those are not included in the table. It is correct to say that Database Logging and Block are the only two modules that are enabled in Minimal. The other modules are required by Drupal. Update Status depends on the user choosing updates during installation.*

## Structure

### Content types

- **Minimal** - There are no content types to start.
- **Standard** - 2 premade content types, Basic Page, and Article
  - *Basic Page* - not promoted to front page, comments disabled, author and date not set to display, rdf mapping 'foaf:Document'
  - *Article* - a default taxonomy named "Tags" enabled. Set to display author and date info, comments enabled. Comes with an image field. The image field has an rdf mapping of 'og:image', 'rdfs:seeAlso' and the tags field has a rdf mapping of 'dc:subject'

### Menus

- **Both** - 4 default menus. The Navigation and Management menu blocks appear by default in Bartik's first sidebar, and the user menu is printed in the upper right.
- **Minimal** - The menu module is not enabled. Menus cannot be added or edited under Structure \> Menus until the Menu module is enabled.
- **Standard** - Default home link in the Main Menu

### Blocks

- **Minimal** - The default Bartik theme has the following blocks enabled:
  - System help in the Help section
  - Main page content in the Content section
  - Navigation, User login, and Management in the Sidebar first section
- **Standard** - The default Bartik theme has the following blocks enabled:
  - System help in the Help section
  - Main page content in the Content section
  - Search, Navigation, User login in the Sidebar first section
  - Powered by Drupal in the Footer

### Appearance

- **Minimal** - Bartik is the default theme and the default admin theme
- **Standard**
  - Bartik is the default theme
  - Seven is set as the admin theme, and set to appear when editing or creating content
  - Global and Bartik initial theme settings are the same.

## Configuration

### Account settings

- **Minimal** - No default roles, and no default admin role
- **Standard** - There is a default role for administrator, who is set as the default admin role. User pictures are enabled.

### Text formats

- **Minimal** - One text format: Plain text (default with Drupal)
- **Standard** - Three text formats: Plain text, Full HTML, and Filtered HTML

### Media

- **Minimal** - Image module is disabled
- **Standard** - Three default styles: thumbnail, medium, and large

### Database tables installed

- **Minimal** - 48 tables installed in the database
- **Standard** - 73 tables installed in the database
