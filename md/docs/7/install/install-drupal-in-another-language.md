---
title: "Install Drupal in another language"
source_url: "https://www.drupal.org/docs/7/install/install-drupal-in-another-language"
page_type: page
last_updated: "Last updated on 5 February 2018"
published: "2010-09-12T09:57:04+00:00"
modified: "2018-02-05T10:32:49+00:00"
breadcrumb: ["Drupal 7", "Installing Drupal 7"]
fetched: "2026-10-21T05:55:15Z"
raw: "raw/docs/7/install/install-drupal-in-another-language.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Install Drupal in another language

To install and use Drupal in a language other than English without additional module requirements, complete the appropriate section based on when you install additional languages:

***Note:** Ensure that there is a Drupal version is available in your language of choice at [https://localize.drupal.org/](https://localize.drupal.org). Not all languages are available for every version of Drupal, but if yours is available, follow these steps to install Drupal in your language.*

### Installing a language before installing Drupal

1.  Download the language file from the [translation server](https://localize.drupal.org/download).
2.  You will find a directory named `translations` inside the directory of the profile you will be using. Normally you use standard profile, so you can use `profiles/standard/translations`. Move the downloaded `.po` file inside this folder.
3.  Install Drupal as per usual by visiting `http://[site_URL]/install.php`.

### Installing a language after installing Drupal

1.  Download the language file from the [translation server](https://localize.drupal.org/download).
2.  You will find a directory named `translations` inside the directory of the profile you will be using. Normally, you use standard profile so you can use `profiles/standard/translations`. Move the downloaded `.po` file inside this folder.
3.  Go to *Modules*, and then ensure that the Locale module is enabled.
4.  Go to *Configuration*, and then click *Languages*.
5.  Click *Add languages*, select your language, and then click *Save configuration*.
6.  After your language is added, you can make it default by selecting the language from the list, and then clicking *Save configuration*.

### Automating installation and updates

After you start to add modules and themes to the site, downloading and keeping translations updated manually can be tedious. It's suggested that you use the [Localization update](https://drupal.org/project/l10n_update) module to import the translation files automatically.

## Drupal language resources

- [Multilingual guide for Drupal 7](/docs/7/multilingual)
- [Search for Multilingual modules](/project/project_module)

For more useful materials on configuring a multilingual site in Drupal, see [Resource Guide: Configuring a Multilingual Site](/resource-guides/configuring-multilingual-site).
