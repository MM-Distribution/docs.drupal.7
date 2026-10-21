---
title: "Writing secure code"
source_url: "https://www.drupal.org/docs/7/security/writing-secure-code"
page_type: guide
published: "2016-09-20T13:27:42+00:00"
modified: "2017-08-31T03:57:26+00:00"
breadcrumb: ["Drupal 7", "Security in Drupal 7"]
fetched: "2026-10-21T06:56:37Z"
raw: "raw/docs/7/security/writing-secure-code.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Writing secure code

Writing secure code in Drupal 7.

## [Overview](/docs/7/security/writing-secure-code/overview)

Whether you are writing a PHP snippet or an entire module, it is important to keep your code secure.

## [Avoid using data from \$form_state\['input'\]](/docs/7/security/writing-secure-code-0/avoid-using-data-from-form_stateinput)

In the Form API, using data from \$form_state\['input'\], \$\_POST, and/or \Drupal::request()-\>request (Drupal 8) are a security risk.

## [Create forms in a safe way to avoid cross-site request forgeries (CSRF)](/docs/7/security/writing-secure-code/create-forms-in-a-safe-way-to-avoid-cross-site-request-forgeries)

Cross-site request forgery (CSRF or XSRF) is a process where a request is made to a site which takes an action when the user did not intend

## [Database access](/docs/7/security/writing-secure-code/database-access)

Drupal provides several functions to send queries to the database. The canonical form is db_query. Always use functions provided by Drupal

## [Do not use /e in preg_replace() - use preg_replace_callback() instead](/docs/7/security/writing-secure-code/do-not-use-e-in-preg_replace-use-preg_replace_callback-instead)

Security advisories have pointed out the risk of passing user input through regular expressions that use the /e flag.

## [File uploads, downloads and management](/docs/7/security/writing-secure-code-0/file-uploads-downloads-and-management)

\[This section is a work in progress\]

## [Directories](/docs/7/security/writing-secure-code-0/directories)

For starters, always make sure that actions on uploaded files (upload, view, download, delete) are taking place in the 'files' directory or

## [Handle text in a secure fashion](/docs/7/security/writing-secure-code/handle-text-in-a-secure-fashion)

When handling and outputting text in HTML, you need to be careful that proper filtering or escaping is done. Otherwise, there might be bugs

## [Handling Private/Personally Identifiable Information](/docs/7/security/writing-secure-code/handling-privatepersonally-identifiable-information)

When working with certain kinds of sensitive data, it is important to carefully evaluate Drupal's handling of that information and determine

## [Session IDs](/docs/7/security/writing-secure-code-0/session-ids)

Session support in PHP allows one to preserve data across subsequent accesses. A visitor accessing your website is assigned a unique ID,

## [Use of hash functions](/docs/7/security/writing-secure-code-0/use-of-hash-functions)

For Drupal 7 and later core and contributed modules, the md5() and sha1() hash functions should never be used in any code, since they are

## [Using PHP with eval() or drupal_eval()](/docs/7/security/writing-secure-code-0/using-php-with-eval-or-drupal_eval)

Using eval() or drupal_eval() in your module's code could have a security risk if the PHP input provided to the function contains malicious

## [When to use db_rewrite_sql or -\>addTag()](/docs/7/security/writing-secure-code-0/when-to-use-db_rewrite_sql-or-addtag)

db_rewrite_sql() in Drupal 6 and db_select() tagged with (for example) 'node_access' in Drupal 7 provide a method for modules to extend your

## [Use Drupal Unicode functions for strings](/docs/develop/coding-standards/use-drupal-unicode-functions-for-strings)

How and why to use Unicode functions for strings

## [Safely Impersonating Another User](/docs/7/security/safely-impersonating-another-user)

Impersonating Possibilities
