---
title: "Getting started with accessibility"
source_url: "https://www.drupal.org/docs/7/creating-accessible-themes/getting-started-with-accessibility"
page_type: page
last_updated: "Last updated on 8 September 2016"
published: "2009-07-01T05:22:27+00:00"
modified: "2016-09-08T13:24:09+00:00"
breadcrumb: ["Drupal 7", "Theming Drupal 7", "Creating accessible themes"]
fetched: "2026-10-21T08:24:16Z"
raw: "raw/docs/7/creating-accessible-themes/getting-started-with-accessibility.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Getting started with accessibility

*Because she is amazing, [Ann McMeekin](http://www.pixeldiva.co.uk) has prepared for us a guide to designing accessibility into themes - it's useful far beyond this project so we've incorporated it into various pages in this section of the theming guide, please feel free to pass it on to others who may find it useful.*

This page provides some general information about theming. You can also download  
[Designing Accessibility Into Themes](http://www.d7ux.org/docs/DesigningAccessibilityIntoThemes.pdf) (PDF 77kB).

## Before you begin

- **Do some research.** If you don’t understand what accessibility is, or how people with disabilities use computers, take some time to do some research. [Understanding Web Accessibility](http://www.uiaccess.com/understanding.html) is a good place to start, and try viewing [videos of people with disabilities using the web](http://www.youtube.com/view_play_list?p=09C317E35FC6D005).
- **Ask an expert.** If you need help, ask an expert. If you don’t know any, you can find lots of helpful and knowledgeable people at [Accessify Forums](http://www.accessifyforum.com).
- **Accessibility isn’t just about sight loss.** Although we usually associate accessibility issues with people who have sight loss, many other people encounter difficulties when trying to use websites. The needs of those with hearing impairments, mobility difficulties, and cognitive impairments or any combination of the above are just as important.
- **Aim for a good experience regardless of ability or technology.** Listening to a site is a very different experience from seeing a site but, with careful implementation, both can be a good experience. Where a drag and drop interface might be great for those who can use a mouse, the equivalent experience for keyboard only users should be something equally easy to understand and use.
- **Include accessibility in the design.** Accessibility makes a site better for all users and is unlikely to have an adverse impact on the visual design if it is included in the design process rather than being implemented at the end.

## Testing

- **Validate your HTML and CSS.** Invalid code isn’t necessarily inaccessible, but may cause the page/site to behave unpredictably, which may in turn cause problems for assistive technology.
- **Check color combinations.** Use a tool which tests against the Luminosity algorithm and test for color-blindness issues using an appropriate tool or simulator. Learn more about [Specifying colors and contrast for accessibility](/node/464500).
- **Ensure fallbacks are in place.** Check that all important functionality works without JavaScript, CSS and images.
- **Unplug your mouse.** Before trying out a screen reader, unplug your mouse and try using the site/theme with keyboard only. If you can use the site comfortably without using your mouse, you’re doing very well.
- **Use an automated testing tool.** Tools like [WAVE](http://wave.webaim.org/) can help you identify coding errors and suggest areas which may require further manual assessment.
- **Get an expert review.** If you don’t feel that you have the experience or knowledge to fully test the site, get an expert to review the site. Do some user testing. If at all possible, ask some people with disabilities to test your site/theme and observe them while they’re using it.
