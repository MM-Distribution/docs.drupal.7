---
title: "Comparison of Invoice modules for Drupal Commerce"
source_url: "https://www.drupal.org/docs/7/extend/comparison-of-contributed-modules/comparison-of-invoice-modules-for-drupal-commerce"
page_type: page
last_updated: "Last updated on 30 April 2025"
published: "2012-04-16T14:00:19+00:00"
modified: "2025-04-30T20:53:04+00:00"
breadcrumb: ["Drupal 7", "Extending Drupal 7", "Comparison of contributed modules"]
fetched: "2026-10-21T08:59:45Z"
raw: "raw/docs/7/extend/comparison-of-contributed-modules/comparison-of-invoice-modules-for-drupal-commerce.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Comparison of Invoice modules for Drupal Commerce

By default, Drupal Commerce lets users view a list of their orders at `user/XX/orders` and a specific order overview can be found at `user/XX/orders/XX`. It contains order ID, billing information, order items (line items), subtotal, taxes and order total.

The following are modules that extend the functionality to invoices and/or packing slips.

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th>Module</th>
<th>Description</th>
<th>Core</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><a href="https://www.drupal.org/project/commerce_invoice_print">Commerce Invoice Print</a></td>
<td>This module fills a gap between Commerce Invoice and Print modules.<br />
It allows developers to create in their theme a template file to be used for and only for Drupal Commerce order invoice print pages.</td>
<td>D7</td>
</tr>
<tr class="even">
<td><a href="http://drupal.org/project/commerce_invoice">Commerce Invoice</a></td>
<td><ul>
<li>D7 - Obsolete. As of 22 May 2014, recommends <a href="https://drupal.org/project/commerce_billy">Commerce Billy</a></li>
<li>^8.8 || ^9 - This module provides flexible and heavy-weight invoicing capabilities to the Drupal Commerce ecosystem. It uses an Invoice entity type to store invoicing information</li>
</ul></td>
<td>^8.8 || ^9<br />
</td>
</tr>
<tr class="odd">
<td><a href="http://drupal.org/project/commerce_order_invoice">Commerce Order Invoice</a></td>
<td>This differs from Commerce Invoice in that it uses existing entity types rather than introducing a new "invoice" entity type</td>
<td>D7</td>
</tr>
<tr class="even">
<td><a href="http://drupal.org/project/commerce_invoice_receipt">Commerce Invoice Receipt</a></td>
<td>Provides an additional 'Invoice' display for Commerce orders, as well as a Rules action to email this invoice out to customers.</td>
<td>D7</td>
</tr>
<tr class="odd">
<td><a href="http://drupal.org/project/commerce_pdf_invoice">Commerce PDF Invoice</a></td>
<td>Provides a View for creating a PDF invoice from an order for Drupal Commerce.<br />
It's built with the <a href="http://drupal.org/project/views_pdf">Views PDF module</a>. The PDF invoice can easily be changed as it is a View</td>
<td>D7</td>
</tr>
<tr class="even">
<td><a href="http://drupal.org/project/commerce_invoices">Commerce Invoices</a></td>
<td>Creates the ability to send out invoices to clients and have them pay through a Drupal Commerce payment method.</td>
<td>D7</td>
</tr>
<tr class="odd">
<td><a href="http://drupal.org/project/commerce_email">Commerce Email</a></td>
<td>Allows admins to set up email templates that get sent out to customers when an order is completed. Note: per <a href="https://www.drupal.org/project/commerce_email/issues/3144958">this issue</a>, the Drupal 7 branches of this module are not supported.</td>
<td>8.x</td>
</tr>
<tr class="even">
<td><a href="http://drupal.org/project/commerce_billy">Commerce Billy</a></td>
<td>Lightweight billing approach supporting invoice number generation and PDF export. It uses the commerce order entity to hold invoice information, including a separate "invoiced" status. The order number property is used for the invoice number.</td>
<td>D7</td>
</tr>
<tr class="odd">
<td><a href="https://drupal.org/project/commerce_packing_slip">Commerce Packing Slip</a></td>
<td>Provides a customized order view to be used as a printable packing slip with a sub-tab on the administrative order view.</td>
<td>D7</td>
</tr>
</tbody>
</table>
