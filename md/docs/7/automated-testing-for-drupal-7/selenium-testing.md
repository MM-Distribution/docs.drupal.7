---
title: "Selenium testing"
source_url: "https://www.drupal.org/docs/7/automated-testing-for-drupal-7/selenium-testing"
page_type: page
last_updated: "Last updated on 24 July 2023"
published: "2014-08-21T11:48:09+00:00"
modified: "2023-07-24T03:01:42+00:00"
breadcrumb: ["Drupal 7", "Automated testing for Drupal 7"]
fetched: "2026-10-21T08:09:33Z"
raw: "raw/docs/7/automated-testing-for-drupal-7/selenium-testing.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Selenium testing

[Selenium](http://www.seleniumhq.org/) is a tool which automates browser testing, and so can be used to test your Drupal website.

Selenium has two very different ways of creating and running tests:

- [Selenium WebDriver](https://www.selenium.dev/documentation/webdriver/) - a program-driven method of testing. Selenium WebDriver is used by a number of projects, including [CodeCeption](http://codeception.com/). 
- [Selenium IDE](http://www.seleniumhq.org/projects/ide/) (deprecated) - a Firefox add-on that will do simple record-and-playback of interactions with the browser. You cannot install it from the usual addons.mozilla.org web site, you must get it from the [Selenium downloads](http://docs.seleniumhq.org/download/) page. Release 2.9.0 can be installed from [here](http://release.seleniumhq.org/selenium-ide/2.9.0/selenium-ide-2.9.0.xpi). The record function saves the history of your clicks in an HTML file containing a table with three columns and a row for each click. The language of the recording is referred to as "selenese". You can edit the recording in the Selenium IDE or with your favorite text editor. If the page you are recording has AJAX functions, you may need to edit the file to insert waits for the data returned by the AJAX call. There is detailed [documentation](http://www.seleniumhq.org/docs/02_selenium_ide.jsp) available. NOTE: Selenium IDE will not run with recent versions of Firefox, starting with version 55.

## Selenium WebDriver

Drupal contains a number of contributed modules to enable you to use the Selenium WebDriver with Drupal. For example:

- [Selenium (Drupal contributed module)](https://www.drupal.org/project/selenium)

## Selenium WebDriver with Codeception

[CodeCeption](https://codeception.com) is an open source project that uses Selenium WebDriver to write acceptance tests. 

### Quickstart

Use [this QuickStart Guide](https://codeception.com/quickstart) to both install and execute your first test in 6 easy steps in less than 5 minutes

### Typing into CKEditor

\$I-\>executeJS("CKEDITOR.instances\['" . \$field . "'\].setData('" . \$text . "');");

### Selecting an option that uses Chosen

You can't use the selectOption method with a field that uses Chosen. Instead:

- Use pressKey to type the option into the Chosen field, preceded by a space.
- Use pressKey again to press Enter.

E.g., 

\$I-\>pressKey('//\*\[@id="edit_field_page_whatever_und_chosen"\]/ul/li/input', ' ' . \$label);  
\$I-\>pressKey('//\*\[@id="edit_field_page_whatever_und_chosen"\]/ul/li/input', WebDriverKeys::ENTER);

### Clicking a Paragraphs module button to add a paragraph

You can't use the click method to click the "Add" and "Remove" buttons that the Paragraphs module displays. Instead, use pressKey to press Enter on the button. 

\$I-\>pressKey('//\*\[@id="edit-field-bundle-bundlename-und-add-more-add-more"\]', WebDriverKeys::ENTER);

Then waitForElement for an element in the box that appears.

### Adding an Image to a Paragraph

This example needs fleshing out but it's a start:

\$I-\>amGoingTo('choose an image using the Media Browser');  
\$I-\>see('Browse');  
\$I-\>waitForElement('#edit-field-bundle-bundlename-und-0-field-image-und-0-upload');  
\$I-\>pressKey('//\*\[@id="edit-field-bundle-bundlename-und-0-field-image-und-0-browse-button"\]', WebDriverKeys::ENTER);  
\$I-\>waitForText('Media browser');  
\$I-\>switchToIFrame('mediaBrowser');

\$I-\>amGoingTo('choose the image from the Media Library');  
\$I-\>click('Library');  
\$I-\>waitForElement('//\*\[@id="edit-submit-media-browser"\]');

\$I-\>amGoingTo('choose an image from the library, searching for ' . \$image_search);  
\$I-\>waitForElement('#edit-filename');  
\$I-\>fillField('filename', \$image_search);  
\$I-\>click('#edit-submit-media-browser');  
\$I-\>waitForText(\$image_filename);  
\$I-\>waitForElement('//\*\[@id="' .  \$image_media_id . '"\]/div/div/img');  
\$I-\>click('//\*\[@id="' . \$image_media_id . '"\]');

\$I-\>amGoingTo('save the new title image');  
\$I-\>click('Submit');  
\$I-\>switchToIFrame();  
\$I-\>expect('the Media Browser to go away and to return to the edit page');  
\$I-\>waitForElement('//\*\[@id="edit-field-bundle-bundlename-und-0-field-image-und-0-remove-button"\]');

### Other Notes

Sometimes you can't click an item until you "see" it first.

## Selenium IDE (Runs only with Firefox 54 and earlier)

- [SeleniumHQ home page](http://www.seleniumhq.org/projects/ide/)
- [Installation](http://docs.seleniumhq.org/docs/02_selenium_ide.jsp)
- [Tutorial](https://blog.udemy.com/selenium-ide-tutorial/) and another [tutorial](http://www.guru99.com/introduction-selenuim-ide.html)

### Download and Install

Download and install the [Selenium IDE driver for Firefox](http://www.seleniumhq.org/download/). Once Selenium is installed, choose Options \> Options when the Selenium IDE window is open and set:

- Select Remember Base URL, so you don't have to enter the URL of the website each time.
- Deselect Start recording immediately on opening, because that's annoying.

### Creating and Saving a Test Case

- Launch Firefox.
- Browse to the site you want to test. If you have a dev or stage server, run the tests there so your tests can make a mess (edit or delete pages) without disturbing your live site.
- Click the Selenium IDE button near the right end of the Firefox toolbar to open the Selenium window.
- Press the red Record button.
- Do the actions you’d like automated.
- Press Record again to stop recording.
- Once you’ve completed your test, save it to the appropriate folder in your Git repository.

Tests are saved as XHTML files so you can view, edit, rename, and copy them in a text editor (or bulk edit them). Each step in the test appears as a row in a table.

### Playing a Test Case

- Launch Firefox.
- Click the Selenium IDE button to open the Selenium window.
- Load a test case by choosing File \> Add a Test Case.
- Select the test you want from the list on the left.
- Press the Play Test Button (or the Play All Tests button).
- You should see your test taking place in Firefox.

Note: You can also increase or decrease the speed of playback with the slider in the top left of Selenium IDE.

### Creating and Playing a Test Suite

You can save a group of test cases together as a test suite.

- Create and save all the test cases.
- Load them up in Selenium in the order you’d like them to run, by right-clicking in the listing area and choosing Add Test Case. (It's possible to load the same test case multiple times.)
- Choose File \> Save Test Suite from the menu and save the test suite file.

Play a test suite -- that is, play all the test cases in the order in which they are listed:

- Choose File \> Open Test Suite from the menu and chose the test suite. The test suite name and the listing of test cases appear in the Selenium window.
- Click the Play Entire Test Suite button on the toolbar to play them all in order.  
  Or, double-click a specific test case to select it (so it's boldface) and click the Play Test Case button on the toolbar.

The test suite stores the path of the test cases, so moving individual test cases will break the test suite. You can fix by editing the test suite file in a text editor.

### Adding Text to the CKEditor WYSIWYG

Selenium can't natively handle javascript elements like the WYSIWYG we're using. Fortunately it can pass Javascript through via the runScript command. If you wish to test adding text try the following command sequence, which replaces the current value of the text field with what you type:

Command: pause Target: 2000

Command: runScript Target: CKEDITOR.instances\["edit-body-und-0-value"\].setData('Some boring test text here.');

Command: pause Target: 2000

Pausing playback briefly before and after the JavaScript Command seems to be important; otherwise the editor may not finish loading or saving the text.

### Selecting an Option That Uses [Chosen](https://www.drupal.org/project/chosen)

Command: clickAt Target: id=edit_field_whatever_und_chosen

Command: clickAt Target: //li\[@data-option-array-index='1'\]

It doesn't always work. Replace the 1 with the index number of the option you want.

### More Information

There are a number of videos on using Selenium IDE with Drupal.

From NodeOne (now Wonderkraut Sweden): [Selenium tests and Drupal development](https://wunderkraut.se/blogg/selenium-tests-and-drupal-development)
