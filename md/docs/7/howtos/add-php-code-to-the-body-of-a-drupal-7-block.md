---
title: "Add PHP code to the body of a Drupal 7 Block"
source_url: "https://www.drupal.org/docs/7/howtos/add-php-code-to-the-body-of-a-drupal-7-block"
page_type: page
last_updated: "Last updated on 25 January 2018"
published: "2011-01-31T20:29:46+00:00"
modified: "2018-01-25T23:26:04+00:00"
breadcrumb: ["Drupal 7", "Site building and development HowTos for Drupal 7"]
fetched: "2026-10-21T07:58:42Z"
raw: "raw/docs/7/howtos/add-php-code-to-the-body-of-a-drupal-7-block.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Add PHP code to the body of a Drupal 7 Block

**Enabling the PHP filter module is not a good idea**

The PHP input filter introduces the possibility for malicious users to attack your website with malicious scripts. Only grant permission to use the PHP filter for competent PHP coders you trust. It is a good idea to create a separate role distinct from “administrator” for this module (and other potentially dangerous ones) such as “developer.” The risks include:

- A typo causes a syntax error making your site inaccessible.
- A trusted user with a weak password, unlocked computer or insecure session sniffed allows an attacker to use their account.
- PHP code has full access to your site, including payment data submitted to the site, user passwords as they are submitted, and your site’s content.

This article is for Drupal 7 developers who have tried to put PHP code in the body of a Custom Block but can't get it to run. It assumes that you are logged in with administrative privileges and are not yet advanced enough to be aware of the **PHP filter Module** ( Like me, when I first ran into this problem). It also assumes you know how to create a block and place it on your page, although you should be able to get through this without that knowledge.

To begin, create a custom Block by navigating to the Add Block page found at \[your site\]/admin/structure/block/add or on the Drupal 7 menu: Administration \> Structure \> Blocks \> Add Block. After filling in the Block description and Block title, go ahead and put your PHP code in the Block body. You can mix text, HTML, and PHP code (sometimes called PHP snippets). Here is a simple example:

``` php
Hello
<p>Welcome!</p>
Today's date is: 
<?php
   echo date('m/d/Y');
?>
```

After placing your PHP code, you can select PHP code in Text Format drop-down. If this doesn't appear, check with your module **PHP filter Module** enabled or not. But realize that this is a problem we are going to have to fix. (If "PHP code" **is** an option on the Text Format drop-down, you should be all set and need not read any further. You have probably done what is necessary sometime in the past.)

Now, save your block, enable it by placing it on one of your theme's regions, and test it out. Most likely Drupal 7 will print out the PHP code instead of interpreting it, giving you an unexpected and ugly result.

**Here is the critical fix and the point of this article:**

Drupal 7 Core contains a module called **"PHP filter"**. A fresh install of Drupal 7 has this module disabled by default. We need to enable it.

To do this, make sure you've saved your block and navigate to the Module Administration page. This is found at \[your site\]/admin/modules or on the Drupal 7 menu system: Administration \> Modules. Scroll down to the **PHP filter** module and check the Enabled box. Press the Save Configuration button. At this point, you should be all set, but hold on for just a second. Scroll back down to the **PHP filter** module again and notice that two links have been added. The first is "help". It's not long and is worth reading, so check it out. The second new link is "permissions". Click on this to go to the Permissions page. Scroll down to the **Filter** section and notice that there is a new item called "Use the PHP code text format" and its checkbox for the Administrator is not checked. The permission box must be checked for the role that needs to use PHP code in order for the PHP filter to show on input boxes.

(Note: User 1 automatically has all permissions including the use of the PHP filter regardless whether permission is granted to any role.)

Make sure you save your changes on the Permissions page and navigate back to your Block's configuration page. (Administration \> Structure \> Blocks), then click on the "configure" link next to your block. Scroll down to the Text Format drop-down. You should now see a new option called **"PHP code"**. Select it.

Remember to save your change and go test your block. It should now work as expected.

Have fun PHPing in your Blocks!
