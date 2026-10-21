---
title: "Change the favicon"
source_url: "https://www.drupal.org/docs/7/theming/howto/change-the-favicon"
page_type: page
last_updated: "Last updated on 8 September 2016"
published: "2009-01-21T21:44:21+00:00"
modified: "2016-09-08T14:07:11+00:00"
breadcrumb: ["Drupal 7", "Theming Drupal 7", "Theming HowTos"]
fetched: "2026-10-21T08:27:11Z"
raw: "raw/docs/7/theming/howto/change-the-favicon.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Change the favicon

In web development, you can provide a small logo for your site that appears near the address bar and in the bookmarks folder in a visitor's browser. This logo is called the favicon. Drupal provides a default one, which is the recognizable water drop logo. Using the Drupal logo as the favicon is fine but if you really want to make your site stand out, you should provide your own. Favicon files are in the .ico format and are extremely small in dimensions. The default Drupal favicon is 32 pixels high by 32 pixels wide, many browsers use a 16 x 16 pixel version that can be included in the same file. This is because the favicon is only an icon that shows up in the address bar and favorites (bookmarks) list and typically there is not a lot of room there. Any favicon that you create should be just as small.

### Changing the favicon

1.  Create a favicon.ico file using a graphics application. If your own favicon file is not named favicon.ico, rename it to that now. Make sure your favicon is also in the ICO format.
2.  Navigate to the admin/build/themes/settings/THEME or for Drupal 7 admin/appearance/settings/THEME page in the admin area of the site (replace THEME with the name of your default theme).
3.  Choose the favicon.ico file in the 'Shortcut icon settings' section of the theme configuration page and upload the file. (It's possible to specify a path to store the favicon in the theme folder).

The changes may not appear immediately in your browser, so completely clear your browser's cache and reload the page. Also, if you've bookmarked your site, you may need to delete the bookmark and then create it again so that the new favicon is used instead.

### Tips for creating a favicon

- When creating a favicon from scratch, make the file square in dimensions and make it large. Using dimensions that are a multiple of 16 is a good idea, e.g. 64 x 64 or 128 x 128. This makes it far easier to create a favicon (unless you are excellent at pixel art).
- You may find sharpening or scaling the favicon using 'bicubic sampling' produces best results when converting the file to an ICO.
- Favicons should follow the color palette of the site.
- Include a notable symbol in your favicon (i.e., the Drupal drop, the Wikipedia "W", the Google "G").
- There are plugins for many graphics applications to allow easy exporting of the ICO file.
- Simple is best at the tiny scale of the favicon.

### Further reading

For more information about favicons, see the [Wikipedia article for favicons](http://en.wikipedia.org/wiki/Favicon) and also [the W3C page on favicons](http://www.w3.org/2005/10/howto-favicon). There are several sites you can visit that help you create favicons, for instance [www.favicon.cc](http://www.favicon.cc/). For a fully fledged solution, look at [RealFaviconGenerator](http://realfavicongenerator.net) which lets you create all icons required by different devices (desktop, iOS, android) at once; icons can further be integrated in your website with the [responsive_favicons](https://www.drupal.org/project/responsive_favicons) module.
