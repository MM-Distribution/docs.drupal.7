---
title: "Specifying colors and contrast for accessibility"
source_url: "https://www.drupal.org/docs/7/creating-accessible-themes/specifying-colors-and-contrast-for-accessibility"
page_type: page
last_updated: "Last updated on 15 March 2017"
published: "2009-05-16T14:57:39+00:00"
modified: "2017-03-15T20:13:53+00:00"
breadcrumb: ["Drupal 7", "Theming Drupal 7", "Creating accessible themes"]
fetched: "2026-10-21T08:26:24Z"
raw: "raw/docs/7/creating-accessible-themes/specifying-colors-and-contrast-for-accessibility.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Specifying colors and contrast for accessibility

According to Vischeck, "Roughly 1 in 20 people have some sort of color vision deficiency." Having sufficient contrast between the text color and the background color can be critical for these users to read effectively. In fact, for most users, black text on a white background is the most readable. There are various forms of [color blindness](http://en.wikipedia.org/wiki/Color_blindness) that designers in particular need to be aware of.

The [accessibility gate](https://www.drupal.org/core/gates#accessibility) requires (Level AA) contrast on all visual presentations.

### What is sufficient color contrast?

As part of its Web Content Accessibility Guidelines (WCAG 2.0), the Worldwide Web Consortium (W3C) has established guidelines for sufficient color contrast. Briefly stated, they are:

- For large text, such as headings:
  - A color contrast ratio of at least 3:1 normally provides enough contrast. **(Level AA - this is our minimum target for the accessibility gate.)**
  - A color contrast ratio of at least 4.5:1 is necessary when you must have enhanced contrast. (Level AAA.)
- For regular text:
  - A color contrast ratio of at least 4.5:1 normally provides enough contrast. **(Level AA - this is our minimum target for the accessibility gate.)**
  - A color contrast ratio of at least 7:1 is necessary when you must have enhanced contrast. (Level AAA.)

To learn more about these issues, go to [WCAG 2.0 Guideline 1.4](http://www.w3.org/TR/WCAG/#visual-audio-contrast) - section [1.4.3 Contrast (Minimum)](https://www.w3.org/TR/WCAG/#visual-audio-contrast-contrast) and section [1.4.6 Contrast (Enhanced)](https://www.w3.org/TR/WCAG/#visual-audio-contrast7).

Here are some tools to help you evaluate your themes:

- [Contrast-A (online version)](http://contrast-a.dasplankton.com/)  (Requires Adobe Flash Player)— There is also a [downloadable version of Contrast-A](http://www.adobe.com/cfusion/marketplace/index.cfm?event=marketplace.offering&offeringid=10763&marketplaceid=1) as an Adobe AIR application. As described in detail in [this comment](http://drupal.org/node/874370#comment-3359712) on an issue involving color in Drupal 7, Contrast-A is probably the best tool for designers and their customers to select an accessible color palette. Its one disadvantage is that you must know either the hexadecimal codes or the RGB values of the colors you are assessing, but many of the rest of the tools mentioned here can give you those values if you can't find them some other way. Among its advantages are these:
  - With Contrast-A, you can quickly see the color pair as it would appear to people with normal vision and each of four extreme cases of colorblindness.
  - In addition to giving you the contrast value, Contrast-A gives you a quick visual representation of whether the color pair conforms with guidelines and, if so, at which level. In other words, Contrast-A shows you whether this color pair is unsuitable for meaningful information, suitable for only large text, or suitable for both small and large text.
  - If the color pair lacks enough contrast, you can make Contrast-A show you the ranges of colors within each chosen hue that would have enough contrast and the level at which those colors would conform with guidelines.
  - Using Contrast-A, you can easily adjust any one of the three aspects of color — hue, saturation, and darkness — independently of the other two and immediately observe the affect of this change on the contrast level of the color pair.
  - As you analyze the contrast of each color pair within a palette, Contrast-A lets you save the results for each pair as images that are like paint chips. Each image shows the two colors, their hexadecimal values, and whether they conform with contrast guidelines — and, if so, at what level.
  - You can save a collection of these chips as a PDF. With this PDF, you can easily share your observations and conclusions with your customers and co-workers, wherever they might be.
- [Vischeck.com](http://www.vischeck.com/) — This tool allows themers to visualize their design as it would appear to people with either of two types of color blindness (protanopia and tritanopia).
- [Juicy Studio's Contrast Checker](http://juicystudio.com/services/luminositycontrastratio.php) — This tool gives you a simple view of how much contrast there is between two colors.
- [Juicy Studio's Firefox Extension](http://juicystudio.com/article/colour-contrast-analyser-firefox-extension.php) — This tool reveals the color contrast of all elements in the DOM.
- [Paciello Group Colour Contrast Analyser](http://www.paciellogroup.com/resources/contrast-analyser.html) — The Windows version of this desktop application includes sliders that make it easy to adjust colors if they don't quite provide sufficient contrast. There is also a Mac version. When you use this tool, be sure to set it to measure the luminosity difference. (It also gives values for color difference, the algorithm that was used under WCAG 1.0.)
- [WhatColor](http://www.hikarun.com/e/) — Simple Windows application which will display the name and hexcode of the colour currently under the mouse cursor.

### When would I need enhanced contrast?

Use the guidelines for enhanced contrast when these or similar conditions exist:

- A heading needs extra emphasis — for example, because the information is urgent.
- Other text is finer or smaller than normal.
- The information is likely to be used with poor lighting or high glare.
- People with poor vision are a significant portion of your audience.

For more information on contrast guidelines for the Web, see:

- [WCAG 2.0: Do you have enough color contrast on your Web site?](http://drinkingoatmealstout.com/2007/06/02/wcag-20-do-you-have-enough-color-contrast-on-your-web-site/), an entry in Justin Thorp's blog;
- WebAIM's article on [color and contrast checking with images](http://www.webaim.org/techniques/images/color.php), which includes several examples of issues with color.
