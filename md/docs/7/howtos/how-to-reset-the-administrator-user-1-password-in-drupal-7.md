---
title: "How to reset the administrator (user 1) password in Drupal 7"
source_url: "https://www.drupal.org/docs/7/howtos/how-to-reset-the-administrator-user-1-password-in-drupal-7"
page_type: page
last_updated: "Last updated on 12 May 2025"
published: "2018-02-01T12:13:24+00:00"
modified: "2025-05-12T09:19:23+00:00"
breadcrumb: ["Drupal 7", "Site building and development HowTos for Drupal 7"]
fetched: "2026-10-21T08:05:41Z"
raw: "raw/docs/7/howtos/how-to-reset-the-administrator-user-1-password-in-drupal-7.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# How to reset the administrator (user 1) password in Drupal 7

## Request new password via email

You can reset your password by requesting a new password at:  
`http://www.example.com/user/password`  
or  
`http://www.example.com?q=user/password`

You may need to find out the details with the following sql statement: `SELECT name, mail FROM users WHERE uid = 1;`

## Recover password with Drush

[Drush](http://drupal.org/project/drush) offers several ways of recovering the administrator's password.

### Generate login-link

Drush can generate a one-time login link.

``` php
drush uli
```

### Reset password

``` php
drush upwd --password="givememypasswordback" "admin"
```

drush 9:

``` php
drush upwd admin "admin123"
```

(where "admin" is the user name)

## When blocked because of maximum attempts

When you tried several times with wrong password, additional attempts will be temporarily be blocked. Drupal stores the attempts on the flood table.

To unblock the user you need to clear the data of flood table. To do so using drush run the following command:

``` php
drush sqlq "DELETE FROM flood"
```

This clears **all **flood data! So if someone else is making malicious login attempts, those will also be cleared. Make the query more-specific with a `WHERE` clause, if you can. Flood data is temporary, so resetting it is like setting a clock forward.

## When other methods don’t work 

Attempt to reset the password through the usual ways *first*. Use the password reset functionality if you can get the email with the password reset link. If another admin account has access to update user 1’s email address, do that so the email can be delivered. If you have ssh access, use `drush uli`

**Follow this documentation if other options have been exhausted.** 

Some hosting environments do not allow SSH access to the web server where a Drupal site is installed which makes it impossible to recover the administrator account password another way. The following method should be employed as a *"last resort"* when the command-line based password recovery techniques do not work.

The password reset method described below uses a PHP script that must be uploaded to the web server to reset the administrator password. The ability to upload a PHP file to the server where the site is hosted is required for successful execution of this method.

Under the hood, the PHP script executes a full Drupal bootstrap in order to obtain access to the necessary functions that generate the administrative password and then update the database with the new password that you specify via the URL when you execute the script through the web browser.

**Leaving this password reset script on your server after resetting the password is a security hole** that enables anyone to reset your administrator password. Use this script carefully, and always delete the script after you're finished using it.

1.  First, create a file with a random name, `gh34tu9.php` for example.

2.  Copy and paste the following contents into the file, and save the file.  

    ``` php
    define('DRUPAL_ROOT', getcwd());
    require_once DRUPAL_ROOT . '/includes/bootstrap.inc';
    drupal_bootstrap(DRUPAL_BOOTSTRAP_FULL);
    require_once DRUPAL_ROOT . '/includes/password.inc';
    $newhash = user_hash_password('[CHANGE THIS PASSWORD]');

    $updatepass = db_update('users') 
      ->fields(array(
        'pass' => $newhash,
    // Uncomment the following lines to reset the administrative username and/or email address, if necessary.
    //  'name' => 'admin',
    //  'mail' => 'yourmail@example.com'
      ))
      ->condition('uid', '1', '=')
      ->execute();
    print "Done. Please delete this file immediately!";
    drupal_exit();
    ```

3.  Upload the file to the root of the Drupal installation directory (i.e., where index.php, update.php, robots.txt and other files and directories exist).

4.  Execute the script, by requesting the file in a web browser using the following URL pattern:  
    `http://example.com/gh34tu9.php`
    - replace `example.com` with your actual domain name,
    - replace `gh34tu9.php` with the actual file name that you specified in step one above,

5.  If the script executes successfully, you will see the text "Done" in your web browser. The password of the administrative account created when installing Drupal (i.e., user/1) will be changed to the value you specified.

6.  Test that the password works, and change it through the Drupal UI to something else that has not been saved anywhere, except for a password manager.

7.  Finally, **delete the file from the Drupal installation root directory.**

### Reset administrator account username or email

If you can't remember (or simply do not know) the username of the administrator account, in the script above, change `// 'name' => 'admin',` to ` 'name' => 'admin',` and the username will also be changed to “admin”. You may also reset the administrator's email address in the same way, by “uncommenting” (remove the `//`) the line for the email address in the script above.

Finally, don't forget to **delete the file as soon as you have changed the password**.
