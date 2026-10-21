---
title: "Multisite cron"
source_url: "https://www.drupal.org/docs/7/setting-up-cron/multisite-cron"
page_type: page
last_updated: "Last updated on 5 August 2016"
published: "2008-03-22T15:44:12+00:00"
modified: "2016-08-05T14:59:34+00:00"
breadcrumb: ["Drupal 7", "Setting up cron for Drupal 7"]
fetched: "2026-10-21T06:23:55Z"
raw: "raw/docs/7/setting-up-cron/multisite-cron.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Multisite cron

Sites that make use of Drupal's multisite feature need to take extra steps to ensure that each site gets its cron run, rather than just the default site. The following pages contain ways of how people have addressed this issue.

### Automatic multisite cron using php5

Create a new file preferably in the same directory as your drupal dir. Name it 'cronall.php' or something. Copy the following script into it. Then adjust the settings in the file, and visit the script with your webbrowser, to see if it is setup correctly.  
Then create a cronjob for the cronall.php script, and you're done.

``` php
<?php
/**
 * This script scans the sites directory, and uses a regular expression to extract the sitenames.
 * It then uses this sitename to execute the cronjob for these sites.
 * You then only have to create a cronjob for this script.
 * In this way, you can create and delete sites on the fly, but all their cronjobs will be executed.
 */

/***********
 * SETTINGS
 **********/
//the location of the 'sites' directory relative to this script.
$sitesDir = '../drupal/sites';
/**
 * A regular expression that matches the name of the directories in
 * the 'sites' dir that you want to execute cronjobs for, with a 
 * backreference around the actual site name. (so we can exclude the
 * domain part)
 * 
 * If you don't know regular expressions you might want to brush up
 * on them: http://www.regular-expressions.info/tutorial.html
 * 
 * Alternatively, you can just copy the name of one of the directories
 * in the site dir, put a backslash \ in front of all dots . and replace
 * the actual name of the site with ([a-zA-Z0-9_-])
 */
$siteNameRegExp = 'www\.example\.com\.([a-zA-Z0-9_-])';
//the url of the cron script, you should insert %s where the sitename should be inserted later.
$cronUrl = 'http://www.example.com/%s/cron.php';
//any other sites that you want to execute cronjobs for. Just comment this if you haven't got any.
$addedSites = array('drupal');
/***********
 * END SETTINGS
 **********/

error_reporting(E_ALL);
$sites = array();

$handle = opendir($sitesDir);
while ($file = readdir($handle)) {
    if(ereg($siteNameRegExp, $file)){
        $sites[] = ereg_replace($siteNameRegExp, '\\1', $file);
    }
}
//default site
if(isset($addedSites) && is_array($addedSites)){
    $sites = array_merge($sites, $addedSites);
}
foreach($sites as $site){
    $cmd = 'wget --spider '.sprintf($cronUrl, $site);
    echo 'Executing command: '.$cmd.'<br>';
    exec($cmd);
}

?>
```

### Cron script for multi source, multi site setup

I've just hacked up this little script as I have multiple installations of drupal each with multiple sites that get more each day. This should figure out which sites cron should run for.

``` php
#!/bin/bash

SITESROOT=/var/www/sites
MYIPRANGE=41.204.221

# get the base installs
cd $SITESROOT
for drupaldir in $(find . -maxdepth 2 -name INSTALL.mysql.txt |  awk -F/ '{print $2}')
do
  cd $SITESROOT/$drupaldir/sites
  for site in $(find  -L . -maxdepth 1 -type d  -iregex "./[a-z].*\.[a-z].*" | awk -F/ '{print $2}')
  do
    IP=$(dig $site  | sed '/AUTHORITY SECTION/,$d' | grep -v "^;" | grep  "IN[[:space:]]*A" | sed 's/.*A\W*//' )
    if echo $IP | grep -q $MYIPRANGE
    then
      #echo "Doing cron for $site"
      wget -O - -q http://$site/cron.php
    else
      a=1
      #echo "Skipping cron for $site"
    fi
  done
done
```

### Multi-site Cron Bash Script

A quick bash script to run cron for multiple sites:

``` php
#!/bin/bash

## Define your websites in an array
sites=(example.com example2.com example3.com)

len=${#sites[*]}
for((i=0; i<$len; i++)); do
        wget -q http://${sites[${i}]}/cron.php
        # You may remove (or comment) the following line if you
        # wish to retain the downloaded file.
        rm cron.php
done
```

### Multisite cron without wget/curl

``` php
#!/usr/bin/php5
<?php
/**
* This script scans the sites directory, and uses a regular expression to extract the sitenames.
* It then uses this sitename to execute the cronjob for these sites.
* You then only have to create one cronjob for this script.
* In this way, you can create and delete sites on the fly, but all their cronjobs will be executed.
*/
/*
 * Carl van Denzen, june 2009:
 * Options for this script:
 * -h <hostname> (p.e. arjan.vandenzen.nl)
 * -r <regexp> (p.e. .+\.vandenzen\.nl) This will be used in most cases.
 * -a
 *
 * When this script is invoked  with parameter -r, then it will call
 * itself for every host in the sites directory that matches the -r regexp.
 * These calls will be with the -h <hostname> argument set to the site name.
 *
 * When invoked with -h option (only ONE is allowed), it will run cron
 * for the named hostname site.
 *
 * When this script is invoked without parameters, it will die. This is to avoid
 * runaway scripts.
 *
 * Purpose of this behaviour:
 *
 * You can add this script to your crontab with parameter -a: it will run
 * for every site found in the drupal sites directory. This is the regular
 * drupal/cron.php behaviour.
 * In a one-site set-up it will only run for the default directory.
 * In a multi-site set-up it will run for all sites (beware of the default directory?)
 *
 * You can add this script to your crontab with the -r parameter and it will only run cron
 * for the sites that match the <regexp>. This is primarily meant for a multi-site set-up
 * when the sites directory contains sites that you want to exclude from running cron
 * (p.e. the "default" site).
 *
 * You can add this script to your crontab with the -h option to run cron
 * for only the specified site (only one allowed).
 *
 * Without parameters it will do nothing.
 * I have seen some problems with argument parsing that made me
 * afraid of doing things like calling the same script. I would have preferred
 * that this script would cron all sites if it was invoked without parameters.
 *
 * This script calls itself for every site (in a new command shell).
 * It is impossible to do this in a
 * php function (i.e. without invoking a new process) because the drupal
 * bootstrap coding cannot (easily) be called multiple times.
 *
 * Disadvantages of this script:
 * pearl5 is needed for Console/Getopt.php
 * It is not efficient because for every host a new php process is
 * created.
 *
 * Advantage:
 * For me it works.
 * It is only one script (I saw other solutions that used two scripts
 * to accomplish this task).
 * It doesn't use wget or similar programs that try to start cron
 * by making a connection to the cron.php file. This strategy didn't
 * work for me, because my website hoster doesn't allow outgoing
 * connections.
*/

/***********
* SETTINGS
**********/
//the location of the 'sites' directory relative to this script.
$sitesDir = 'sites';
/**
* A regular expression that matches the name of the directories in
* the 'sites' dir that you want to execute cronjobs for, with a
* backreference around the actual site name. (so we can exclude the
* domain part)
*
*/
$siteNameRegExp = '(.*\.example\.com)';
$debug=0;
/***********
* END SETTINGS
**********/

/*
 * Do default action like old cron.php (i.e. before
 * the year 2008) script in Drupal 6.x
 */
function do_old_cron() {
    drupal_bootstrap(DRUPAL_BOOTSTRAP_FULL);
    drupal_cron_run();    
}
/*
 * some sanity checks
 */
if (!isset($_SERVER['argv'])) {
    // print('server argv not set<br/>');
    do_old_cron();
}

error_reporting(E_ALL);

include ("Console/Getopt.php");


// initialize object
$cg = new Console_Getopt();

/* define list of allowed options - p = a:all sites, h:one site, r:sites that match regular expression */
$allowedShortOptions = "ah:r:";

// read the command line
$args = $cg->readPHPArgv();

// get the options
$ret = $cg->getopt($args, $allowedShortOptions);

// check for errors and die with an error message if there was a problem
if (PEAR::isError($ret)) {
    die ("Error in command line: " . $ret->getMessage() . "\n");
}

ini_set('include_path',ini_get('include_path'). PATH_SEPARATOR . './scripts');

/* This doesn't work in every case: getopt function is not always available
$options = getopt("h:r:");
var_dump($options);
*/

include_once './includes/bootstrap.inc';

function cron_one_site($sitename) {
    $_SERVER['SCRIPT_NAME'] = '/cron.php';
    $_SERVER['SCRIPT_FILENAME'] = '/cron.php';
    $_SERVER['HTTP_HOST'] = $sitename;
    $_SERVER['REMOTE_ADDR'] = 'localhost';
    $_SERVER['REQUEST_METHOD'] = 'GET';

    drupal_bootstrap(DRUPAL_BOOTSTRAP_FULL);
    echo "Hostname is: $hostname<br/>\n";
    print 'conf_path is '.conf_path() . '<br/>';
    drupal_cron_run();
}
/*
 * Call this script for every site in regexp (call
 * it with -h option for every site).
 */
function cron_regexp($siteNameRegExp) {
    global $sitesDir;
    global $debug;
    $sites = array();
    // Get the name of this script, so we can call it recursively
    // doesn't work: argv is not defined: $thisScript=$argv[0];
    $argv=$_SERVER["argv"];
    $thisScript=$argv[0];

    $handle = opendir($sitesDir);
    while ($file = readdir($handle)) {
        if ($debug>0) {
          if (file_exists("$sitesDir/$file/settings.php")) {
            print('Yes: ');
          } else {
            print("No: ");
          }
          print("exists $sitesDir/$file/settings.php<br/>");
        }
        if (($file!='all') && (file_exists("$sitesDir/$file/settings.php"))) {
            // preg expects the pattern to be enclosed in a (freely chosen)
            // delimiter. I have chosen ^ because I think that will never
            // be used in a host name
            if(preg_match('^'.$siteNameRegExp.'^', $file)){
                if ($debug>0) {
                  print '$file is '.$file.', $siteNameRegExp is '.$siteNameRegExp.'<br/>\n';
                }
                $sites[] = $file;
            }
        }
    }
    foreach($sites as $site){

        if ($debug>0) {
          print 'Doing site '.$site.'<br/>\n';
        }
        $commandline='/usr/bin/php5 '.$thisScript.' -h '.$site;
        exec($commandline,$out1,$out2);
        if ($debug>0) {
          print 'Commandline is '.$commandline.'<br/>\n';
          print 'out1 is '.implode('\n',$out1).'<br/>\n';
          print 'out2 is '.implode('\n',$out2).'<br/>\n';
        }
    }
}
// display the options
//print_r($ret);
if ($debug>0) {
  print_r($_SERVER);
}
// parse the options array
$opts = $ret[0];
if (sizeof($opts) > 0) {
    // if at least one option is present
    foreach ($opts as $opt) {
        switch ($opt[0]) {
            // handle the all sites option
            case 'a':
                $re='.*';
                cron_regexp($re);
                break;
            // handle the hostname
            case 'h':
                $hostname = $opt[1];
                cron_one_site($hostname);
                break;
            /* handle the regexp option. */
            case 'r':
                $re = $opt[1]; // regular expression
                cron_regexp($re);
                break;
            default:
                print 'Usage: <br/>\n';
                print '- h hostname<br/>\n';
                print '- r regexp<br/>\n';
                print '- a (do all sites)<br/>\n';
                break;

        }
    }
}

/*
 * Some experienced I had with this script at your-webhost.nl in june 2009
 *         // $_SERVER["PHP_SELF"] is not set
*/
?>
```

### Multisite with cron-curl.sh

I have domain1.com hosted as the primary domain with domain2.com "parked" at domain1.com. My public_html/sites folder looks like this:

sites/all  
sites/default  
sites/domain2

My webhost (an Apache server running Cpanel 11) blocks user access to lynx or wget, so the normal recommendations for setting up a crontab were not working for me. However, I discovered a suggestion in <http://drupal.org/cron> to try the cron-curl.sh script that ships with Drupal in the "scripts" folder. I edited cron-curl.sh so that it includes the following line:

`curl --silent --compressed http://domain1.com/cron.php`

And then I set up a crontab that looks like this:

`*/2 * * * * /home/webhostaccountname/public_html/scripts/cron-curl.sh`

After remembering to set the file permissions on cron-curl.sh so that it could be executed, the cron job worked perfectly. The "\*/2" executes the crontab every other minute for testing purposes only.

So, then I went back into cron-curl.sh and added the following line:

`curl --silent --compressed http://domain2.com/cron.php`

Again, success! I'm watching the logs for both domain1.com and domain2.com. Cron jobs are being executed every 2 minutes for both domains.

### Run cron.php with python

I was unable to run cron.php from the cpanel cron on a multisite because I had no access to curl, lynx and wget. I knew I had python installed in the shared server so what I did was to create a python script in my home folder called *wget.py*

Python 2 Version:

``` php
import sys, urllib
def reporthook(*a): print a
for url in sys.argv[1:]:
     i = url.rfind('/')
     file = url[i+1:]
     print url, "->", file
     urllib.urlopen(url)
```

Python 3 Version:

``` php
#!/path/to/python3
import sys, urllib.request
def reporthook(*a): 
    print (a)
    
for url in sys.argv[1:]:
     i = url.rfind('/')
     file = url[i+1:]
     print ("%s %s %s" % (url, "->", file))
     # urllib.urlretrieve(url, file, reporthook)
     urllib.request.urlopen(url)
```

Then, in the cron configuration, just add the command:

``` php
/path/to/python /path/to/wget.py url1/cron.php url2/cron.php url3/cron.php
```

### Simple wget multisite cron, lazy method

I just wrote this script for running the crons on all my drupal sites before I discovered this section in the documentation. This works well for me because I'm lazy and I don't have to maintain a list of my drupal sites somewhere for it to run all my crons. The script simply reads the domains from my sites folder. It works well for me, but I think it might not work for every situation, ymmv.

Create an executable called *drupalcron*:

``` php
#!/bin/bash

#change the following line to match your sites folder
cd /var/www/drupal/htdocs/sites

#the next line gets only directories, not symlinks (and not the 'all' nor 'default' directories)
for f in `ls -Fd *.*|grep '/$'`
#remove the 'echo' from the following line after making sure it looks right
do echo wget -O - -q -t 1 http://${f}cron.php
done
```

**Please note**, the script will only echo the command and not actually do anything. This is so that you can check to see if it looks right first. Please read the comments in the script. If the output is what you expect, then delete the word *echo* from the *do* line and then it will execute the wget commands next time.

Then simply add that to your crontab however you wish:

`10 * * * * /path/to/drupalcron > /dev/null 2>&1`

### Solution using Drush and crontab and without wget

The other solutions listed are still soft crons: a long task could be broken by an Apache timeout.

Use Drush for this. Create a crontab by logging in as the correct Linux user and typing in the shell 'crontab -e' and enter the following:

``` php
MAILTO="log@yourdomain.com"
0 * * * * cd ~/www/; drush @sites core-cron --yes
```

Notice that you may change the 'cd ~/www/' to your home folder. The current cron settings is 'once per start of an hour'. If you want to change this, look for a tutorial on crontab settings.

Notice that Drush executes via the CLI PHP so those php.ini settings apply. Imo, this is an advantage rather than a disadvantage as you can specify the cron to use more memory if necessary.

You can also use the --root option so you don't need to cd into the directory for each time.

``` php
0 * * * * drush --root=/home/user/www @sites core-cron --yes
```

### Multisite cron without wget/lynx or curl

I recently moved my sites to a new host, and they don't allow me to use either wget or curl from cron. Since I'm running multiple sites, I also can't just run cron.php directly. However, I can use the 'exec()' PHP call, so I came up with these two scripts:

runcron.php:  
\#!/usr/local/bin/php

``` php
$SITES = array( 'www.mainsite.com', 'www.subsite1.com', 'www.subsite2.com', ... );

$_SERVER['SCRIPT_NAME'] = '/cron.php';
$_SERVER['SCRIPT_FILENAME'] = '/cron.php';
foreach( $SITES as $site ) {
  exec( "./runsitecron.php ".$site );
}
```

runsitecron.php:  
\#!/usr/local/bin/php

``` php
$_SERVER['SCRIPT_NAME'] = '/cron.php';
$_SERVER['SCRIPT_FILENAME'] = '/cron.php';
$_SERVER['HTTP_HOST'] = $_SERVER["argv"][1];
include "cron.php";
```

Then I just call 'runcron.php' from my crontab and it runs Drupal's 'cron.php' for each of my sites.
