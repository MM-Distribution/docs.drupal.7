---
title: "Customize the User Edit page in Drupal 7 - an example"
source_url: "https://www.drupal.org/docs/7/theming/howto/customize-the-user-edit-page-in-drupal-7-an-example"
page_type: page
last_updated: "Last updated on 8 September 2016"
published: "2014-06-04T19:27:27+00:00"
modified: "2016-09-08T14:07:08+00:00"
breadcrumb: ["Drupal 7", "Theming Drupal 7", "Theming HowTos"]
fetched: "2026-10-21T08:49:41Z"
raw: "raw/docs/7/theming/howto/customize-the-user-edit-page-in-drupal-7-an-example.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Customize the User Edit page in Drupal 7 - an example

### Quick Intro

There is very little documentation on how to customize the user edit page in Drupal 7. Through trial and error (mostly error) I set out to customize the user edit page for a customer. This how-to will take you through how I did it. This was my first go-around, so the methods used may not be the best practices.

### The goal

The goal was to break up the user edit fields into groups, and to show the groups one at a time. I also wanted the ability to show only one group, hiding the buttons that allow the user to show other groups. The purpose of this option was to create a Change Password page. I accomplished this through the use of JavaScript. It was through limited documentation and trial-and-error that I learned how to display each of the user edit controls on the page.

### First things first

First, we must tell the theme to use the customized user edit page, which will be named user-profile-edit.tpl.php. You must locate the *THEMENAME_theme()* function (THEMENAME being the name of your theme), often found in template.php. In my case it was located in theme.inc. Open the file in a text-editor, locate the *THEMENAME_theme()* function and add the following code:

``` php
  return array(
    'user_profile_form' => array(
      // Forms always take the form argument.
      'arguments' => array('form' => NULL),
      'render element' => 'form',
      'template' => 'templates/user-profile-edit',
    ),
  );
```

There may already be a "return array..." in the function, so simply add the 'user_profile_form' piece to the return array, like this:

``` php
  return array(
    'custom_links' => array( 
      'variables' => array('links' => NULL, 'attributes' => NULL, 'heading' => NULL),
    ),
    'some_menu' => array(
      'variables' => array('menu' => NULL),
    ),
   'user_profile_form' => array(
      // Forms always take the form argument.
      'arguments' => array('form' => NULL),
      'render element' => 'form',
      'template' => 'templates/user-profile-edit',
    ),
  );
```

Now use a text editor to create your user-profile-edit.tpl.php. (Side note: I've seen comments that in Drupal 7 the file needs to be named user--profile--edit.tpl.php {two dashes instead of one}, but I could not get it to work that way. Perhaps it is how the theme I was using has been written.)

Here's the code I used to create my user-profile-edit.tpl.php file:

``` php
<div id="user-edit-<?php print $user->uid; ?>" class="user-edit-form">
    <div class="user-edit-container" id="user-edit-container">
        <?php print render($form['form_id']); ?>
        <?php print render($form['form_build_id']); ?>
        <?php print render($form['form_token']); ?>
        <input type="input" id="ViewMode" class="currentedittab" name="ViewMode" value="" style="display: none;">
        
        <div class="useredittabcontainer" id="useredittabcontainer">
            <ul class="usereditlist">
                <li id="accountinfo" class="useredittab accountinfo" onclick="clicktab('accountinfo');">Account Information</li>
                <li id="changeprofile" class="useredittab changeprofile" onclick="clicktab('changeprofile');">Profile Information</li>
                <li id="changeadditionalprofile" class="useredittab changeadditionalprofile" onclick="clicktab('changeadditionalprofile');">Additional Profile Information</li>
                <li id="changepassword" class="useredittab changepassword" onclick="clicktab('changepassword');">Change Password</li>
                <li id="showalledit" class="useredittab showalledit" onclick="clicktab('showalledit');">Show All</li>
            </ul>
        </div>
        
        <div class="usereditborder" id="usereditborder">
            <div class="showalledit toggleelement"><h3>Account Information</h3></div>
            <div class="showalledit accountinfo toggleelement"><?php print render($form['account']['name']); ?></div>
            <div class="showalledit accountinfo toggleelement"><?php print render($form['field_first_name']); ?></div>
            <div class="showalledit accountinfo toggleelement"><?php print render($form['field_middle_name']); ?></div>
            <div class="showalledit accountinfo toggleelement"><?php print render($form['field_last_name']); ?></div>
            <div class="showalledit accountinfo toggleelement"><?php print render($form['account']['mail']); ?></div>
            <div class="showalledit toggleelement"><hr></div>
            <div class="showalledit toggleelement"><h3>Change Password</h3></div>
            <div id="currpass" class="showalledit accountinfo changepassword toggleelement"><?php print render($form['account']['current_pass']); ?></div>
            <div class="showalledit changepassword toggleelement"><?php print render($form['account']['pass']); ?></div>
            <div class="showalledit toggleelement"><hr></div>
            <div class="showalledit toggleelement"><h3>Profile Information</h3></div>
            <div class="showalledit changeprofile toggleelement"><?php print render($form['field_address']); ?></div>
            <div class="showalledit changeprofile toggleelement"><?php print render($form['field_city']); ?></div>
            <div class="showalledit changeprofile toggleelement"><?php print render($form['field_state']); ?></div>
            <div class="showalledit changeprofile toggleelement"><?php print render($form['field_zip_code']); ?></div>
            <div class="showalledit changeprofile toggleelement"><?php print render($form['field_phone_number']); ?></div>
            <div class="showalledit changeprofile toggleelement"><?php print render($form['field_date_of_birth']); ?></div>
            <div class="showalledit changeprofile toggleelement"><?php print render($form['field_gender']); ?></div>
            <div class="showalledit toggleelement"><hr></div>
            <div class="showalledit toggleelement"><h3>Additional Profile Information</h3></div>
            <div class="showalledit changeadditionalprofile toggleelement"><?php print render($form['timezone']['timezone']); ?><hr></div>
            <div class="showalledit changeadditionalprofile toggleelement"><?php print render($form['signature_settings']['signature']); ?><hr></div>
            <div class="showalledit changeadditionalprofile toggleelement" style="min-height:135px;">
                <div class="showalledit changeadditionalprofile toggleelement"><?php print render($form['picture']['picture_current']); ?></div>
                <div class="showalledit changeadditionalprofile toggleelement"><?php print render($form['picture']['picture_upload']); ?></div>
                <div class="showalledit changeadditionalprofile toggleelement"><?php print render($form['picture']['picture_delete']); ?></div>
            </div>
            <div class="showalledit changeadditionalprofile toggleelement"><?php print render($form['account']['status']); ?></div>
            <div class="showalledit changeadditionalprofile toggleelement"><?php print render($form['account']['roles']); ?></div>
            <div class="showalledit changeadditionalprofile toggleelement"><?php print render($form['account']['notify']); ?></div>
            <div class="showalledit accountinfo toggleelement"><?php print render($form['field_terms_of_use']); ?></div>
        </div>
        
        <?php print render($form['actions']); ?>
    </div><!--end user-edit container-->
    
    <script type="text/javascript">
      afterpageload();
      function afterpageload() {
        var themode=getmode();
        <?php
          print('var prevMode =  \'');
          print($_REQUEST['ViewMode']); 
          print('\';');
        ?>
        
        switch (themode) {
          case "chpwd":
            prevMode = '';
            break;
          case "chpwdonly":
            prevMode = '';
            break;
        }
        
        
        switch (themode) {
          case "chpwd":
            break;
          case "chpwdonly":
            break;
          default:
            if (prevMode.length > 0) {
              themode = prevMode;
            }
            break;
        }
        
        
        switch (themode) {
          case "chpwd":
            //select the Change Password tab
            clicktab("changepassword");
            //Hide the selector tabs to clean up the interface
            document.getElementById("useredittabcontainer").style.display = 'none';
            break;
          case "chpwdonly":
            //select the Change Password tab
            clicktab("changepassword");
            //This is used for password reset, so hide the Current Password field.
            document.getElementById("currpass").style.display='none';
            //Hide the selector tabs to clean up the interface
            document.getElementById("useredittabcontainer").style.display = 'none';
            break;
          case "showchpwd":
            //Select the Change Password tab.
            clicktab("changepassword");
            break;
          case "showprofile":
            //Select the Profile tab
            clicktab("changeprofile");
            break;
          case "showaddlprofile":
            //Select the Additional Profile Information tab
            clicktab("changeadditionalprofile");
            break;
          case "showall":
            //Select the Show All tab
            clicktab("showalledit");
            break;
          case "showaccount":
          default:
            //Select the Account Information tab. This is the default behavior.
            clicktab("accountinfo");
            break;
        }
      }
      
      function getmode() {
        //Get the ?viewmode= argument, if any.
        <?php
          print('var returnmode = \'');
          print($_GET["viewmode"]);
          print('\';');
        ?>
        
        if (returnmode.length==0) {
          //If there is no ?viewmode= argument, check to see
          //if this is a password reset
          returnmode = ispasswordreset()
        }
        
        return returnmode;
      }
      
      function ispasswordreset() {
        //Get the ?pass-reset-token= argument, if any.
        <?php
          print('var passreset = \'');
          print($_GET["pass-reset-token"]);
          print('\';');
        ?>
        
        if (passreset.length==0) {
          //This is not a password reset, so start up in the default (normal) tab
          return "normal";
        }
        else
        {
          //This is a password reset. Start up with the password fields only.
          return "chpwdonly";
        }
      }
      
      function clicktab(showclass) {
        //Get all of the elements that have the 'toggleelement' class.
        var items = document.getElementsByClassName('toggleelement');
        
        //Loop through each element, looking for the 'donothide' class.
        //This will allow some elements to be displayed in all modes.
        for (var iCtr = 0; iCtr < items.length; iCtr++){
          if (!hasClass(items[iCtr], "donothide")) {
            //This does not have the 'donothide' class. Keep processing.
            if (hasClass(items[iCtr], showclass)) {
              //This is marked with the selected class (variable showclass).
              //Make sure it is visible.
              items[iCtr].style.display = '';
            }
            else
            {
              //This is not marked with the selected class. Hide it.
              items[iCtr].style.display = 'none';
            }
          }
        }
        //Now that the elements are shown or hidden,
        //Indicate the current tab.
        settabproperties(showclass);
        setParameter(showclass);
      }
    
    function settabproperties(activetab) {
      //Get all of the elements in the user edit menu/tab list.
      var tabs = document.getElementsByClassName('useredittab');
      
      //Loop through, looking for the active tab, indicated by the variable activetab.
      for (var iCtr = 0; iCtr < tabs.length; iCtr++) {
        if (hasClass(tabs[iCtr], activetab)) {
          //This is the active tab.
          tabs[iCtr].style.backgroundColor='red';
          tabs[iCtr].style.color='white';
          tabs[iCtr].style.borderColor='red';
        }
        else
        {
          //This is an inactive tab.
          tabs[iCtr].style.backgroundColor='#eeeeee';
          tabs[iCtr].style.color='black';
          tabs[iCtr].style.borderColor='#bbbbbb';
        }
      }
    }
    
    function hasClass(element, cls) {
      //Pad the className with spaces, and search for the class (cls).
      //cls is also padded to ensure that any results found are not substrings
      //of other classes.
      return (' ' + element.className + ' ').search(' ' + cls + ' ') > -1;
    }
    
    function setParameter(currTab) {
      var newViewmode = '';
      switch (currTab) {
        case "accountinfo":
          newViewmode = 'showaccount';
          break;
        case "changeprofile":
          newViewmode = 'showprofile';
          break;
        case "changeadditionalprofile":
          newViewmode = 'showaddlprofile';
          break;
        case "changepassword":
          newViewmode = 'showchpwd';
          break;
        case "showalledit":
          newViewmode = 'showall';
          break;
        default:
          newViewmode = "default";
          break;
      }
      document.getElementById('ViewMode').value=newViewmode;
    }
    </script>
</div><!--end user-edit-->
```

### Walk through the code

**The JavaScript**  
Note that the JavaScript is at the end. This allows the page to load before the JavaScript executes.  
The first function you'll see is the *afterpageload()* function. This first checks for one of two arguments: 'viewmode' or 'pass-reset-token'. The code also checks the \$\_REQUEST variable to see if this is a reloaded page. This would typically be the result of failed validation. Specifically, the value of the hidden 'ViewMode' imput element is checked for a previous value, set by the setParameter function. If there was a previous value, the 'viewmode' variable is set to match for cases in which the tabs are visible. The javascript does not do this if modes that do not show the tabs are used. This allows the form to remember the previous tab in cases of failed validation. If either of the previously mentioned arguments exist ('viewmode' or 'pass-reset-token'), the starting behavior of the user edit form is altered. You can see what the values for 'viewmode' are by examining the switch statement in the *afterpageload()* function. If no argument is passed for 'viewmode' the code checks for 'pass-token-reset'. This is a Drupal argument used when a password is being reset. In this case, the value itself is not examined, but merely the existence of the argument. If this argument exists, the 'chpwdonly' mode is used. Most of the view modes use one function to set up: *clicktab()*, which will be explained later. Two of the view modes also hide the buttons used to switch between 'tabs'.  
Each of the controls in the user edit form are wrapped inside *div* tags that have the classname *toggleelement* assigned. This tells the JavaScript function *clicktab()* that this control is to be shown or hidden based on the tab that was clicked. The *clicktab()* function takes one argument, 'showclass'. This is the name of the class assigned to every control that is to be visible. All other *toggleelement* divs are hidden. The same classnames are also used as ids to set the styling of the active and inactive tabs in the *settabproperties()* function. The setParameter function, mentioned earlier, sets the value of a hidden input control to the name of the current tab each time it changes. This allows the form to display the most current tab when the form is reloaded due to field validation errors.

**The Tabs / Buttons**  
The tabs are created with an unordered list (*ul* tag). CSS styling is used to display them inline. The classname 'useredittab' is used for CSS styling purposes.  
The *onclick=* parameter is what triggers the JavaScript code.

**The User Edit Controls**  
Most of the controls are output using a single line of code. Because the user profile picture was output using three lines of code, they were wrapped in an extra *div*.  
The \['field\_...'\] entries are used to display profile fields that were added to the system. The names will vary depending on how you have your user account set up. \['account'\]\['name'\] refers to the username. \['account'\]\['mail'\] refers to the e-mail address. \['account'\]\['timezone'\] allows the user to select his or her time zone. \['account'\]\['signature'\] allows the user to create/edit his or her signature for comments. \['account'\]\['status'\] allows an administrator to set the user as active or blocked. \['account'\]\['roles'\] allows an administrator to select/deselect roles for the user. \['account'\]\['notify'\] allows the administrator to choose whether or not the user will be notified of changes. These last three settings will only be shown to users that have appropriate permissions (administrators).

**A Note Concerning Administrators**  
Chances are you have a separate theme for administrative pages. If this is the case administrators will not see this, as this is an adjustment to the theme. I overcame this by copying the user-profile-edit.tpl.php file to my administrative theme folder and adjusting the *THEMENAME_theme()* function, as per the description above.
