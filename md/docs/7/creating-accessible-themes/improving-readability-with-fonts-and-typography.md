---
title: "Improving readability with fonts and typography"
source_url: "https://www.drupal.org/docs/7/creating-accessible-themes/improving-readability-with-fonts-and-typography"
page_type: page
last_updated: "Last updated on 8 September 2016"
published: "2009-05-16T14:56:55+00:00"
modified: "2016-09-08T13:24:09+00:00"
breadcrumb: ["Drupal 7", "Theming Drupal 7", "Creating accessible themes"]
fetched: "2026-10-21T08:24:48Z"
raw: "raw/docs/7/creating-accessible-themes/improving-readability-with-fonts-and-typography.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Improving readability with fonts and typography

Type on the web must have a high level of readability. Readability is a measure of how easily words, phrases and blocks of copy can be read.

Fonts should have a high level of legibility. Legibility refers to typeface design and is a measure of how easy it is to distinguish one letter from another in a particular typeface.

It's not just a matter of choosing the right font, but also what we do with it. We can set font size, color, italics, bold, line height and impart unlimited styles on fonts by way of image editing programs such as Photoshop. However, for accessibility we must maintain both the legibility of the typeface and the readability of text.

1.  [Use real text rather than text embedded within graphics](#real-text)
2.  [Select simple, readable fonts](#simple-fonts)
3.  [Ensure sufficient contrast between the text and the background](#contrast)
4.  [Avoid tiny font sizes](#small-fonts)
5.  [Use relative units for font size](#relative-units)
6.  [Avoid blinking or moving text](#blinking-text)
7.  [Avoid fully-justified text](#fully-justified)
8.  [Use appropriate case](#appropriate-case)

Use real text rather than text embedded within graphics  
A common technique is to use images instead of headings. This hides information from screen readers. Additionally, text in images does not scale well, so if the user zooms the page the text may become unreadable.

- If you must use images for headers or for other information consider using an [accessible image replacement technique](http://www.456bereastreet.com/archive/200712/choose_an_accessible_image_replacement_method/).
- If images of text or image replacement techniques are required, limit their use to only the main heading of a page. This helps users who require specific color schemes, preventing them from having to make further changes to their browser settings in order to read the page.
- Make images of text clear and easy to read. If images of text are unavoidable, ensure that the text size is reasonably large (above 18px) and has good contrast.

Select simple, readable fonts  
The best fonts for the web are sans-serif fonts such as Verdana, Tahoma, Trebuchet MS, Helvetica, Arial, DejaVu Sans and Bitstream Vera Sans. Verdana was developed by Microsoft for display on computer screens and has wide letter spacing, large x-height and good differentiation between similar characters such as lower case L and upper case i.

- Specify more than one font in your CSS, i.e.:  
  `font-family: Verdana, Geneva, "DejaVu Sans", sans-serif;`.
- For more information, see the [Complete Guide to Pre-Installed Fonts in Linux, Mac, and Windows](http://www.apaddedcell.com/web-fonts).

Ensure sufficient contrast between the text and the background  
For more information, see [Specifying Colors and Contrast for Readability](http://drupal.org/node/464500)  

Avoid tiny font sizes  
Many browsers will not display text smaller than 9px. This follows the W3C's recommendation: To preserve readability, a UA applying these guidelines should nevertheless avoid creating font-size resulting in less than 9 pixels per EM unit on a computer display. Fonts smaller than 9px present a significant problem to users with eyesight impairments.

- See [Font size: the font-size property (W3C)](http://www.w3.org/TR/CSS21/fonts.html#font-size-props).

Use relative units for font size  
Fonts should always be sized using relative units such as ems, keywords or percentages. Avoid font sizing based on absolute units such as points (pt), pixels (px), centimeters (cm), millimeters (mm) and inches (in). Font sizes expressed as percentages (%) and "ems" (em) are more accessible because all browsers can resize them, however Internet Explorer 6 and 7 cannot resize fonts set in pixels. Setting a base size font across the whole web site (for consistency) is recommended.

- See [Using Font Size](http://css-discuss.incutio.com/?page=UsingFontSize) at CSS-Discuss.

Base text sizes using a default of at least 100% or 1em. If absolute units must be used, provide a separate stylesheet for Internet Explorer that specifies sizes in percentages or ems to ensure those users can resize text if they need to.

Maintain readability when text size is decreased as well as increased. In general, avoid specifying text smaller than 75% or 0.75em, but if smaller text is required, ensure it remains readable at two steps smaller than default. This helps users with tunnel vision who may reduce the text size in order to reduce eye strain when reading on screen.

Consider making small text bold. This can improve contrast and readability.

Increase line-height to improve readability. [Using a line-height of slightly larger than normal](http://uxmag.com/articles/quickpanel-dyslexia) (e.g., 1.2 to 1.6) can prevent ascending and descending characters from “crashing together” making text easier to read for everyone, but those with dyslexia or other reading impairments in particular.

Avoid blinking or moving text  
According to [WebAIM](http://www.webaim.org):  

> Blinking text and moving text are annoying because they distract the reader's attention. This is especially relevant to people with attention deficits or cognitive disabilities. Neither is likely to cause a seizure, but they are likely to decrease the readability of the document as a whole and increase the time it takes for users to finish reading it.
>
> The situation is further complicated if users are required to click on moving text. Users with slower reaction times, tremors, or other motor difficulties may not be able to click on the links accurately.

Avoid fully justified text.,/dt\>  
Fully justified text can create “rivers” of whitespace and cause significant difficulty to dyslexic users.

Use appropriate case.  
Screen readers use different pronunciation rules for text in ALL-CAPS. For example, “CONTACT US” would be pronounced “contact U S” rather than “contact us”, which could cause confusion. Avoid this by using the appropriate case in the source and using text-transform in CSS to change the visual display if required.
