---
title: "Managing images and media for accessibility"
source_url: "https://www.drupal.org/docs/7/creating-accessible-themes/managing-images-and-media-for-accessibility"
page_type: page
last_updated: "Last updated on 3 January 2018"
published: "2009-05-16T14:56:03+00:00"
modified: "2018-01-03T12:03:17+00:00"
breadcrumb: ["Drupal 7", "Theming Drupal 7", "Creating accessible themes"]
fetched: "2026-10-21T08:25:37Z"
raw: "raw/docs/7/creating-accessible-themes/managing-images-and-media-for-accessibility.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Managing images and media for accessibility

For most of us it would be hard to understand the web without images, audio, video and new interactive media. However, much of that information needs to be conveyed in an alternate format.

1.  [Images](#images)
2.  [Audio, Video, and Interactive Media](#more-media)

## Images

This tutorial demonstrates how to provide appropriate text alternatives based on the purpose of the image:

- **[Informative images](https://www.w3.org/WAI/tutorials/images/informative/)**: Images that graphically represent concepts and information, typically pictures, photos, and illustrations. The text alternative should be at least a short description conveying the essential information presented by the image.

- **[Decorative images](https://www.w3.org/WAI/tutorials/images/decorative/)**: Provide a null text alternative (`alt=""`) when the only purpose of an image is to add visual decoration to the page, rather than to convey information that is important to understanding the page.

- **[Functional images](https://www.w3.org/WAI/tutorials/images/functional/)**: The text alternative of an image used as a link or as a button should describe the functionality of the link or button rather than the visual image. Examples of such images are a printer icon to represent the print function or a button to submit a form.

- **[Images of text](https://www.w3.org/WAI/tutorials/images/textual/)**: Readable text is sometimes presented within an image. If the image is not a logo, avoid text in images. However, if images of text are used, the text alternative should contain the same words as in the image.

- **[Complex images](https://www.w3.org/WAI/tutorials/images/complex/)** such as graphs and diagrams: To convey data or detailed information, provide a full-text equivalent of the data or information provided in the image as the text alternative.

- **[Groups of images](https://www.w3.org/WAI/tutorials/images/groups/)**: If multiple images convey a single piece of information, the text alternative for one image should convey the information for the entire group.

- **[Image maps](https://www.w3.org/WAI/tutorials/images/imagemap/)**: The text alternative for an image that contains multiple clickable areas should provide an overall context for the set of links. Also, each individually clickable area should have alternative text that describes the purpose or destination of the link.

The following points will improve the accessibility of your images:

Provide alt attributes for every image.  
Every image placed in HTML must have an `alt` attribute which contains a concise, appropriate alternative. [WebAIM's Appropriate Use of Alternative Text](http://www.webaim.org/techniques/alttext/) explains how to use the `alt` attribute in a variety of contexts. [Wikipedia](https://en.wikipedia.org/wiki/Wikipedia:Alternative_text_for_images) also does a good job explaining how to manage images effectively.

- For linked images, the `alt` text should describe the destination of the link. For example, if you are using an image of an arrow to provide page navigation, an `alt` text of "right arrow" may not give the user the information they need to understand that what you REALLY mean is "next page." Images that do not provide additional information do not have to be revealed when inside a link element.
- For decorative images, the `alt` text should be null (alt=””) or empty (alt=” “), which lets assistive technology know that the image can safely be ignored. Alternatively, these images can be presented as CSS background images.
- To determine whether the image is important enough to contain a description, imagine reading the page to someone over the telephone. If the image is important enough to include in the telephone conversation, it needs a description. To create a useful description, imagine what you would need to say during the telephone conversation. Use the `alt` text to convey the same information as was intended by the image. Ultimately, it comes down to [knowing the purpose of the image](http://simplyaccessible.com/bpow/descriptive-alt-attributes/).
- If the image is a graph or diagram, the `alt` text should be a concise description of the content (e.g., “Sales figures for June 2009”), accompanied by a longer description or alternative displayed adjacent to the image or provided on a separate but clearly linked page.
- For images of text, the `alt` text should duplicate the text within the image.

Include links to longer descriptions  
Descriptions that are more than 125 characters should include a link, rather than the `longdesc` attribute. `longdesc` is poorly interpreted in many browsers and is deprecated in HTML5. Learn more about longer description techniques on [WebAIM's Longdesc article](http://www.webaim.org/techniques/images/longdesc).

Avoid using CSS to display images that contain content information  
Instead, include an appropriate description as part of the content, and set `background-image` to display that data to sighted users. If you cannot include an appropriate description as part of the content, use the `img` element with appropriate `alt` attribute.

Ensure text contrast is maintained if a background image is not displayed  
Specify a background colour in addition to the background image to avoid text becoming unreadable if the background image is not displayed for any reason.

Use images to enhance understanding  
Helpful for those who may have difficulty understanding text by itself, including users whose main language is not the same as the site language. A question mark icon, for example, could be added next to the word “Help”.

Combine adjacent image and text links  
Reduce the link repetition for for screen reader users.

Ensure the image alt and link text make sense when read together  
A good test is reading them out loud. Leave the image `alt` null if the alt text would otherwise duplicate the adjacent link text. A link to a downloadable document could be written as `<a href="url">Annual Report 2009 (<img src="pdf.jpg" alt="PDF" /> 400kB)</a>` or an e-mail link could be written as `<a href="mailto:address"><img src="email.jpg" alt="" />email us</a>`.

## Audio, Video, and Interactive Media

Keep in mind that your media will be accessed by keyboard-only users, mouse-only users, screenreading users, and many others. The following points will improve the accessibility of your media:

Don't set media to `autoplay`  
Content that automatically plays will likely interfere with screenreading users hearing the rest of the site. Additionally, impaired users may be performing another task on your site -- don't assume they're always ready to experience your audio, video, and interactive media

Include content-specific controls  
Accessible methods to adjust volume, pause/stop, and start content are helpful for everyone. While HTML5 does have included audio and video controls, many assistive technologies don't currently interpret these controls, so when possible, include controls outside of the actual media content.

Provide a textual transcript or description near the media  
As with images, imagine describing this media to someone on the telephone. A transcript is best, and a description is helpful. Display a textual description and/or other media alternative of live content, and provide a full description once the event is complete.

Clearly identify media and alternatives  
When displaying a textual or other media alternative, make sure the alternative is clearly associated with the media.

Display captions on video content  
Captions may be open (always-on) or closed.

Include relevant links and descriptions to required software  
Ensure that visitors can experience your media by saying, for example, "You need to install Adobe Flash to experience this audio slideshow."

Special Considerations for Flash  
For Flash accessibility issues, assistive support, and screen reading techniques, read [WebAIM's Flash article](http://www.webaim.org/techniques/flash/).
