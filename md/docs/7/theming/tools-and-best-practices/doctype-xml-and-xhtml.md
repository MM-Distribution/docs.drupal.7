---
title: "Doctype, XML, and XHTML"
source_url: "https://www.drupal.org/docs/7/theming/tools-and-best-practices/doctype-xml-and-xhtml"
page_type: page
last_updated: "Last updated on 22 December 2016"
published: "2008-11-28T07:43:06+00:00"
modified: "2016-12-22T12:54:52+00:00"
breadcrumb: ["Drupal 7", "Theming Drupal 7", "Tools and best practices"]
fetched: "2026-10-21T08:55:06Z"
raw: "raw/docs/7/theming/tools-and-best-practices/doctype-xml-and-xhtml.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Doctype, XML, and XHTML

Doctype is the first line of any HTML page and tells the browser how to interpret the HTML.

## HTML or XML

Your basic HTML 4 doctype looks like:  
`<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">`

HTML 5: `<!DOCTYPE html>`1

Your web page starts with:

``` php
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
```

You can use old HTML or badly formed HTML, but browsers will still muddle through a strange set of rules for decoding HTML tries to display your pages right. XHTML is a great leap forward from HTML, because it is more strict and therefore helps the developer to choose the correct doctype. The basic XHTML doctype is:  
`<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">`

Because XHTML has to fit XML standards, your web page starts with :

``` php
<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html>
```

The XML format makes life easier for browsers when they interpret the page. Browsers use only a tiny bit of standard code to read the XML formatted information. The DTD tells the browser what is legal and what is not. You can read the finished page using standard PHP XML and extract information, which is exactly how XMLRPC gets information out of a HTTP response.

The XML format makes significant changes to your page.  
`<option selected>Sydney</option>` becomes `<option selected="selected">Sydney</option>`. The XML schema for XHTML does not allow `selected` as some strange data hanging around. You have to use the format name="value" which means you have to type `selected="selected"`. The advantage is clarity, the browser knows exactly what you mean without complicated decoding rules.

`<img src="example.png">` becomes `<img src="example.png" />`. `<br>` becomes `<br />`. You have to have the ending `/` even in single elements.

## Strict or Transitional

Compare the following two HTML doctypes:  
`<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">`  
`<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">`

Now compare the following two XHTML doctypes:  
`<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">`  
`<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">`

The change from Transitional to Strict tells the browser to reject some old ideas in HTML. It is the browser equivalent of turning warnings on in PHP. Strict is the equivalent of driving your sports car when there is a police patrol car cruising behind you. You obey more rules.

Strict will reject formatting elements including center, font, iframe, strike, and u. Use CSS for formatting when you use Strict in your doctype.

## Drupal.org as an example

The Drupal.org home page starts with the following doctype and XHTML. There is an explanation somewhere about their non-compliance and it has to do with some browsers not working the way they should. There are also things caused by the use of so many modules and special bits of code that the result takes a while to clean up.

``` php
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en">
 <head>
  <!-- Note: does not validate. We would like it to, but that would mean reduced user experience for the majority of our visitors. -->
```

One of the validation errors is `id="edit-submit"` in the following input element. The forms code, the search code, and other modules used to render forms with the same ID because they were rarely used on the same page. Now that there are more people working on Drupal development, the code is being modified to avoid these errors.  
`<input type="submit" name="op" id="edit-submit" value="Search" class="form-submit" />`

Try telling a browser the rules to decode the following heading start element, as found on Drupal.org. It is easier to change the HTML to a standard format and the XML format used in XHTML is the simplest standard but it has to be applied everywhere; the Drupal base code, your theme, and everything produced by all your plug-in modules.

## Modules

You know you have to validate your output when you change a theme. Do you validate your output when you add a new module? That new module might add a class around existing information or produce a new data element. Modules can create blocks, provide extra form input elements, pass new data through a template, and add CSS. When you add a new module, you have to make sure the module produces output that fits the doctype you specify for your page.

## Testing

There are testing and validation tools listed [elsewhere](/node/37156). Some let you change doctypes for testing. A quick test of the Drupal.org home page using the default transitional doctype produced 25 errors and a switch to strict produced 50 errors. The general idea is to eliminate the default errors, rather than experiment with a higher level, strict instead of transitional, or XHTML 1.1 instead of XHTML 1.0. Fix the strict errors before changing your doctype from transitional to strict.

## Language support

In XHTML, `<html>` changes to `<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en">`, where `en` is the language used on the web page. Drupal 6 has multiple language support built into the base code. You go to *Administer \> Site Building \> Modules*, then switch on the modules Locale and Content translation. Your output has to be XHTML to specify the language. While some browsers will guess what you want, the doctype has to be XHTML to make every browser read the extra information in the `<html>` element.

## Case

HTML is very lenient when it comes to using lower case and UPPER CASE, with many browsers trying to read both. XML requires that all element names, attribute names, and reserved works have to be a single case, and in XHTML this is lower case.

The main recommendation is to use XHTML Strict when you start a new site or page.

## References

1<http://www.w3.org/TR/html5-diff/#doctype>
