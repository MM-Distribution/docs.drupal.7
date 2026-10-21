---
title: "[Drupal 7] Form API"
source_url: "https://www.drupal.org/docs/7/api/drupal-7-form-api"
page_type: guide
published: "2016-10-14T20:44:07+00:00"
modified: "2026-02-24T08:21:17+00:00"
breadcrumb: ["Drupal 7", "Drupal 7 APIs"]
fetched: "2026-10-21T07:57:09Z"
raw: "raw/docs/7/api/drupal-7-form-api.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# [Drupal 7] Form API

This guide covers **Drupal 7 (Legacy)**. For the most recent standards and best practices, see the modern guide version: [**Form API**](https://www.drupal.org/docs/develop/drupal-apis/form-api)

Collecting and processing user-submitted data is important.

Placing a form on a webpage and getting user responses are easy - getting them *securely* is harder. Drupal provides a standard, easy to use, easy to extend and *secure* way of adding forms to your Drupal website: Form API (FAPI).

This guide describes what you can do using the Form API.

Make sure you [use your form values safely](https://www.drupal.org/docs/7/security/writing-secure-code/handle-text-in-a-secure-fashion).

See also [Form API Reference](https://api.drupal.org/api/drupal/developer!topics!forms_api_reference.html/7.x).

## [Creating a builder function to generate a form](/docs/7/api/form-api/creating-a-builder-function-to-generate-a-form)

Form workflow usually follows these stages:

## [Form API Internal Workflow Illustration](/docs/7/api/form-api/form-api-internal-workflow-illustration)

This workflow actually includes some of the nodeapi hooks as well as FAPI workflow to help illustrate the places where form elements can be

## [Forms API - Modify Form widgets with hook_field_widget_form_alter()](/docs/7/api/form-api/forms-api-modify-form-widgets-with-hook_field_widget_form_alter)

Widgets are the parts that make up forms, like textarea widgets, file upload widgets etc.

## [Forms API - Modify Forms with hook_form_alter()](/docs/7/api/form-api/forms-api-modify-forms-with-hook_form_alter)

Drupal 7 forms that modules create can be changed by other modules and even themes with the help of Drupal FAPI hooks system. See Drupal 7

## [\#tree and \#parents](/docs/7/api/form-api/tree-and-parents)

Explain the use of \#tree and \#parents properties in a form array.
