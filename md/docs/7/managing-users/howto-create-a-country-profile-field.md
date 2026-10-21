---
title: "HowTo Create a 'country' profile field"
source_url: "https://www.drupal.org/docs/7/managing-users/howto-create-a-country-profile-field"
page_type: page
last_updated: "Last updated on 30 September 2016"
published: "2007-02-13T05:37:03+00:00"
modified: "2016-09-30T21:04:16+00:00"
breadcrumb: ["Drupal 7", "Managing users in Drupal 7"]
fetched: "2026-10-21T07:03:51Z"
raw: "raw/docs/7/managing-users/howto-create-a-country-profile-field.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# HowTo Create a 'country' profile field

This page describes how to create a 'country' field in your users' profiles, similar to the one on Drupal.org, that lets you easily find users in any country.

**Note:** Since Drupal 7.x, you will find user fields in *Administration \> Configuration \> People \> Account settings* and then in *Manage Fields* tab.

1.  Create a new profile field.
2.  Go to the profile settings page (administer \> settings \> profiles ?q=admin/user/profile)
3.  Select the 'list selection' type of form field.
    - Category (required): It can be a category you already have or a new one. (Suggested: Personal Information)
    - Title (required): Anything is OK. (Suggested: Country)
    - Form name (required): Anything is ok, as long as it is unique. (Suggested: profile_country)
    - Explanation (optional): Usually, country is self explanatory, but you may want to write a note here to your users about this field.
    - Selection options:  
      Defining a comprehensive list of sovereign states is a contentious diplomatic and political issue. Several lists exist on the Web:
      - The ISO International Standard list of country names and two-letter country codes (ISO standard 3166-1) is available in English and French in various formats. See <http://www.iso.org/iso/country_codes.htm>
      - Wikipedia provides a list of sovereign states (<http://en.wikipedia.org/wiki/List_of_sovereign_states>), with links to the same list in languages other than English on the left.
    - Weight: Select whatever you like (this is the weight in the category selected above).
    - Visibility: Select one of the 'Public Field' options.
    - Page title (required): You must put something here. (Suggested: People who live in)
    - Check boxes: Check 'the user must enter a value' to make this field required. Check 'visible in user registration form' to make it part of user registration.
4.  Click on 'Save field.'

Due to the constantly changing nature of this data, it is often best to compose your own data from up-to-date information provided in the above links.

### Country Codes API

There's a module (Country Codes API: <http://drupal.org/project/countries_api> ) that provides PHP API calls for translating country codes into official short names" by mechfish at <http://drupal.org/node/402198#comment-1551426>
