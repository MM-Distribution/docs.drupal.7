---
title: "Creating HTML formatted emails in Drupal 7"
source_url: "https://www.drupal.org/docs/7/converting-drupal-6-modules-to-drupal-7/creating-html-formatted-emails-in-drupal-7"
page_type: page
last_updated: "Last updated on 15 November 2021"
published: "2010-09-02T17:56:27+00:00"
modified: "2021-11-15T05:25:42+00:00"
breadcrumb: ["Drupal 7", "Converting Drupal 6 modules to Drupal 7"]
fetched: "2026-10-21T07:50:57Z"
raw: "raw/docs/7/converting-drupal-6-modules-to-drupal-7/creating-html-formatted-emails-in-drupal-7.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Creating HTML formatted emails in Drupal 7

Since Drupal 7 automatically converts all HTML emails to plain text before sending them (<http://drupal.org/node/224333#email-html>), you must now write your own implementation of MailSystemInterface and set a variable telling Drupal to use it in order to send HTML emails. Here is the class which needs to go in your module:

``` php
/**
 * Modify the drupal mail system to send HTML emails.
 */
class ExampleMailSystem implements MailSystemInterface {
  /**
   * Concatenate and wrap the e-mail body for plain-text mails.
   *
   * @param array $message
   *   A message array, as described in hook_mail_alter().
   *
   * @return array
   *   The formatted $message.
   */
  public function format(array $message) {
    $message['body'] = implode("\n\n", $message['body']);
    return $message;
  }

  /**
   * Send an e-mail message, using Drupal variables and default settings.
   *
   * @see http://php.net/manual/en/function.mail.php
   * @see drupal_mail()
   *
   * @param array $message
   *   A message array, as described in hook_mail_alter().
   *
   * @return bool
   *   TRUE if the mail was successfully accepted, otherwise FALSE.
   */
  public function mail(array $message) {
    $mimeheaders = array();
    foreach ($message['headers'] as $name => $value) {
      $mimeheaders[] = $name . ': ' . mime_header_encode($value);
    }
    $line_endings = variable_get('mail_line_endings', MAIL_LINE_ENDINGS);
    return mail(
      $message['to'],
      mime_header_encode($message['subject']),
      // Note: e-mail uses CRLF for line-endings. PHP's API requires LF
      // on Unix and CRLF on Windows. Drupal automatically guesses the
      // line-ending format appropriate for your system. If you need to
      // override this, adjust $conf['mail_line_endings'] in settings.php.
      preg_replace('@\r?\n@', $line_endings, $message['body']),
      // For headers, PHP's API suggests that we use CRLF normally,
      // but some MTAs incorrectly replace LF with CRLF. See #234403.
      implode("\n", $mimeheaders)
    );
  }
}
```

Rename the class for your module (e.g. ForwardMailSystem). Then, you need to set the mail_system variable:

``` php
variable_set('mail_system', array('default-system' => 'ExampleMailSystem'));
```

If you wish to have only emails from your module be sent in HTML but leave all others untouched, use this code:

``` php
variable_set('mail_system', array('default-system' => 'DefaultMailSystem', 'example' => 'ExampleMailSystem'));
```

That code can go in your module's install file in hook_install to set that variable as soon as your module is enabled. Make sure to also set the variable back to the default in hook_uninstall.
