---
title: "Configuring cron without wget, lynx, or curl commands"
source_url: "https://www.drupal.org/docs/7/setting-up-cron/configuring-cron-without-wget-lynx-or-curl-commands"
page_type: page
last_updated: "Last updated on 5 August 2016"
published: "2006-05-24T14:38:36+00:00"
modified: "2016-08-05T14:59:34+00:00"
breadcrumb: ["Drupal 7", "Setting up cron for Drupal 7"]
fetched: "2026-10-21T06:24:26Z"
raw: "raw/docs/7/setting-up-cron/configuring-cron-without-wget-lynx-or-curl-commands.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Configuring cron without wget, lynx, or curl commands

Some of you might have trouble getting lynx or wget to work. This may be the case if "localhost" is not permitted.  
Then wget, lynx or curl won't work on the local machine. If you are not willing to depend on others to perform cronjobs and you dislike poormans cron, try this script.

touch ~/scripts/cron-php.sh  
chmod 700 ~/scripts/cron-php.sh  
vi ~/scripts/cron-php.sh

``` php
#!/bin/bash
#
# Simple cron script for those who cannot
# use wget, lynx or curl because the host
# closed the localhost loop.
#
# Usage:
# - put this file in the ~/scripts dir
# - add a cronjob pointing to this script
#
# Copyright OCS - 2006
# Copyright hansfn@drupal.org - 2008
# This script is provided under the GPL.
#
# v 0.1 original release
# V 0.2 added PHP parser options and verbosity
#    setting to keep it quiet so real errors can
#    be reported by cron. 

#############################
# CONFIGURATION OPTIONS
#############################

# Complete local path
#
# Set the complete local path
# to where the cron.php file
# is (ie the root path)
# Default is /var/www/html/
root_path=/var/www/html/

# Complete php path
#
# Set the complete path
# to the php parser if
# different from standard
parse=/usr/bin/php

# PHP parser options
#
# Defaulting to not report notices.
parse_options="-d error_reporting=2037"

# Verbosity
#
# Default to only report errors.
verbose=false

##############################
# END OF CONFIGURATION OPTIONS
##############################

cd $root_path

if [ -e "cron.php" ]
then
    $parse $parse_options cron.php
    if [ "$?" -ne "0" ]
    then
         echo "cron.php not parsed."
    else
         if $verbose
         then
             echo "cron.php has successfully been parsed."
         fi
    fi
else
    echo "cron.php not found."
    exit
fi

exit
```

and then the crontab itself:  
crontab -e  
\* \* \* \* \* ~/scripts/cron-php.sh

where ~ is the directory where your drupal install is (the script defaults to /var/www/html/ but your professional hosting company will probably use /home/your.domain.tld/www

## Using Perl to run cron

If you're having problems with cron using curl and wget is not allowed on your server try out the curl call from the shell on another box - you may find you get HTML delivered saying "page not found."

If this is the case you can also use Perl to perform the call to the cron script.

You need command line access to Perl and the LWP::Simple module installed. Your crontab entry then becomes:

`45 * * * * perl -MLWP::Simple -e "getprint 'http://yourdomainhere/cron.php'"`
