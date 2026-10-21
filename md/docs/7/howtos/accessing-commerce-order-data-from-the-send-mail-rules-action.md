---
title: "Accessing commerce order data from the send mail Rules action"
source_url: "https://www.drupal.org/docs/7/howtos/accessing-commerce-order-data-from-the-send-mail-rules-action"
page_type: page
last_updated: "Last updated on 8 December 2016"
published: "2015-01-22T20:38:20+00:00"
modified: "2016-12-08T07:51:17+00:00"
breadcrumb: ["Drupal 7", "Site building and development HowTos for Drupal 7"]
fetched: "2026-10-21T07:58:57Z"
raw: "raw/docs/7/howtos/accessing-commerce-order-data-from-the-send-mail-rules-action.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Accessing commerce order data from the send mail Rules action

It is common to send a confirmation email when a Commerce order has been completed. It is not obvious how to access data from the Rules action "Send mail". Here is an example of how to access information from the customer billing information and from the line items in the order.

You can use PHP evaluation in any of the fields of the send mail action, but it will be most useful in the email message body. It is possible to mix PHP and replacement patterns. The following example starts with plain text and replacement patterns. Under "Billing Information" is the address in the format:  
\[Street address\] \[Suite/unit\]  
\[City\], \[State\] \[Postal code\]  
\[Country\]

``` php
Thank you for your donation to the XYZ Foundation.

Order #[commerce-order:order-number]
Order total: [commerce-order:commerce-order-total:amount_decimal] [commerce-order:commerce-order-total:currency_code]

Name: [commerce-order:commerce-customer-billing:commerce-customer-address:name_line]
Email: [commerce-order:mail]
Billing Information: 
[commerce-order:commerce-customer-billing:commerce-customer-address:thoroughfare] [commerce-order:commerce-customer-billing:commerce-customer-address:premise]
[commerce-order:commerce-customer-billing:commerce-customer-address:locality], [commerce-order:commerce-customer-billing:commerce-customer-address:administrative_area] [commerce-order:commerce-customer-billing:commerce-customer-address:postal_code]
[commerce-order:commerce-customer-billing:commerce-customer-address:country]

<?php
$message = '';

// Get a custom field value -- phone number -- from the customer billing profile
$cust_billing_profile_id = $commerce_order->commerce_customer_billing[LANGUAGE_NONE][0]['profile_id'];
$customer_billing_profiles = entity_load('commerce_customer_profile', array($cust_billing_profile_id));
// entity_load returns an array even though we only requested one entity, so use reset to get the entity from the array
$customer_billing_profile = reset($customer_billing_profiles);
if ($items = field_get_items('commerce_customer_profile', $customer_billing_profile, 'field_phone_number')) {
  // My phone number field only allows one phone number, so it is safe to access it directly using its index, 0.
  $message .= 'Phone number: ' . $items[0]['safe_value'] . "\n";
}

// My line items have fields and I want to show their values in the email
$line_items = $commerce_order->commerce_line_items[LANGUAGE_NONE];
foreach ($line_items as $li) {
  $lis = entity_load('commerce_line_item', array($li['line_item_id']));
  $line_item = reset($lis);
  if ($items = field_get_items('commerce_line_item', $line_item, 'field_designation')) {
    // No sanitation used here, as this value was entered through a dropdown.
    $message .= 'Designate my gift to ' . $items[0]['value'] . "\n";
  }
  if ($items = field_get_items('commerce_line_item', $line_item, 'field_donation_name')) {
    // Using the safe value because this value was entered by the user in a text field.
    $message .= 'Please list name(s) as ' . $items[0]['safe_value'] . "\n";
  }
}

echo $message;
?>
```
