---
title: "How to Set up Google AdSense for Search without using a custom module"
source_url: "https://www.drupal.org/docs/7/howtos/how-to-set-up-google-adsense-for-search-without-using-a-custom-module"
page_type: page
last_updated: "Last updated on 26 January 2018"
published: "2008-06-24T19:29:46+00:00"
modified: "2018-01-26T00:02:16+00:00"
breadcrumb: ["Drupal 7", "Site building and development HowTos for Drupal 7"]
fetched: "2026-10-21T08:05:56Z"
raw: "raw/docs/7/howtos/how-to-set-up-google-adsense-for-search-without-using-a-custom-module.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# How to Set up Google AdSense for Search without using a custom module

**How to Set up Google AdSense for Search without using a custom module**

**Google AdSense for Search** offers your users site search or web search while earning revenue from ads relevant to their search terms. Incorporating **Google AdSense for Search** into a Drupal website without using a custom module can be accomplished if you utilize the following method.

**Prerequisites:**  
(1) Any Drupal CMS website (not version dependent).  
(2) You need to have a Google AdSense account.  
(3) You need to Set up an **AdSense for Search** Ad unit.

After you set up your **Google AdSense for Search** Ad unit, Google will present you with the following 2 code blocks for you to insert into your website. You will need to make a couple of changes to the **Original Google AdSense for Search Code** in order to get the site search to work properly. In the following example, the **node page 35** will be used as the Search Results page.

**Original Google AdSense for Search Code**  
*The Google Partner account number (partner-pub-xxxxxxxxxxxxxxxxxxx:g2l95q-v9ce) has been xxxx out in the example below. Remember to use your own assigned Google Partner account number and Search Form code.*

**Search Box Code**  
Paste this code into the page where you'd like your search box to appear.

``` php
<form action="http://yourwebsite.com/?q=node/35" id="cse-search-box">
  <div>
    <input type="hidden" name="cx" value="partner-pub-xxxxxxxxxxxxxxxxxxx:g2l95q-v9ce" />
    <input type="hidden" name="cof" value="FORID:11" />
    <input type="hidden" name="ie" value="ISO-8859-1" />
    <input type="text" name="q" size="15" />
    <input type="submit" name="sa" value="Search" />
  </div>
</form>
<script type="text/javascript" src="http://www.google.com/coop/cse/brand?form=cse-search-box&amp;lang=en"></script>
```

**Search Results Code**  
Paste this code on <http://yourwebsite.com/?q=node/35>, where you would like your search results to appear.

``` php
<div id="cse-search-results"></div>
<script type="text/javascript">
  var googleSearchIframeName = "cse-search-results";
  var googleSearchFormName = "cse-search-box";
  var googleSearchFrameWidth = 795;
  var googleSearchDomain = "www.google.com";
  var googleSearchPath = "/cse";
</script>
<script type="text/javascript" src="http://www.google.com/afsonline/show_afs_search.js"></script>
```

Below are the necessary changes to you will need to make to the **Search Box Code** in order to make the **Google AdSense for Search** function properly within a Drupal Website.

**Changes to the Search Box Code:**  
If your site is using the default Drupal **?q=node/23** page URL format, then the "**q**" in the site's URL will cause conflicts with Google's AdSense for Search **Search Box Form**. Google's search form input box statement also utilizes a "**q**" in the **name="q"** parameter. To eliminate this "**q**" conflict, one needs to replace **name="q"** with **name="as_q"** in the Search Box Code.

Making the following two changes will result in a properly functioning Google site search.

\(1\) Remove the **?q=** in the form action statement: from: <http://yourwebsite.com/?q=node/35> to: <http://yourwebsite.com/node/35>.  
(2) Replace **name="q"** with **name="as_q"** in the input statement.

**Modified Search Box Code**  
Paste this code into the page where you'd like your search box to appear.

``` php
<form action="http://yourwebsite.com/node/35" id="cse-search-box">
  <div>
    <input type="hidden" name="cx" value="partner-pub-xxxxxxxxxxxxxxxxxxx:g2l95q-v9ce" />
    <input type="hidden" name="cof" value="FORID:11" />
    <input type="hidden" name="ie" value="ISO-8859-1" />
    <input type="text" name="as_q" size="15" />
    <input type="submit" name="sa" value="Search" />
  </div>
</form>
<script type="text/javascript" src="http://www.google.com/coop/cse/brand?form=cse-search-box&amp;lang=en"></script>
```

**Adding Back the *"Google Custom Search"* Watermark Image**  
By making the **name="as_q"** replacement within the search form's input box statement, the Search form will function properly. However, this particular code change causes the *"Google Custom Search"* Watermark Image not to appear within the search form's input box upon page loading as it would if the original Search Box Code functioned properly in the first place.

To recreate the exact look of the original Google input box which includes the **"Google Custom Search"** Watermark Image, use the following code substitution for the input box statement:

Replace the following input box statement (still using the **name="as_q"** substitution for the **name="q"**):

``` php
<input type="text" name="as_q" size="15" />
```

with the following input box statement:

``` php
<input type="text" name="as_q" size="15" id="q" />
```

This input box statement will simulate the exact look of the original Google input box by placing a **"Google Custom Search"** image inside the text box. The image will disappear when the user places focus on the input box as it would in the original unaltered Google input box.

**Google AdSense program policies**  
*AdSense for search results pages may show only a single ad link unit in addition to the ads Google serves with the search results. No other ads may be displayed on your search results page.*
