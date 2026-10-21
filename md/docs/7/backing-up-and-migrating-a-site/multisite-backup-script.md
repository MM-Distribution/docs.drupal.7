---
title: "Multisite Backup Script"
source_url: "https://www.drupal.org/docs/7/backing-up-and-migrating-a-site/multisite-backup-script"
page_type: page
last_updated: "Last updated on 9 November 2016"
published: "2008-09-19T23:21:38+00:00"
modified: "2016-11-09T14:22:30+00:00"
breadcrumb: ["Drupal 7", "Backing up and migrating a Drupal 7 site"]
fetched: "2026-10-21T06:58:10Z"
raw: "raw/docs/7/backing-up-and-migrating-a-site/multisite-backup-script.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Multisite Backup Script

Here's a perl script that *should* properly backup a multisite Drupal installation. I've tested it on my site and it seems to work, but it needs further testing on different configurations.

This script handles each site stored in a separate database, and multiple sites stored in the same database, or any combination of the two.

Assumptions made by this script:

- you want your backup to sit side-by-side with your current top level Drupal directory
- any host/database combination represents a fully-retrievable database; ie - you don't have two sets of tables in the same host/database that require different username/password combinations to retrieve

As an example, if you have three sites, one.com,two.net, and three.org, and two.net and three.org use the same database (but with different table prefixes) and one.com has its own database, you will get two .sql files, one that contains a dump for one.com and one that contains a dump for two.net and three.org combined. It may use the username/password for two.net **or** for three.org when it dumps the combined database.

As always, use at your own risk. This is definitely a non-destructive script: the only thing it ever deletes is the temporary directory it creates when it starts, so it should have no side-effects on a site. However, don't assume it has created a full backup without checking on your own.

**For Drupal 7 and PostgreSQL see the [first comment](http://drupal.org/node/310948#comment-4381018)**.

Usage:  
`drupalbackup <top-level drupal directory, like ~/www/drupal>`

Save the following file as *drupalbackup* somewhere in your path.

``` php
#!/bin/sh --
#! -*- perl -*-
eval 'exec perl -x $0 ${1+"$@"} ;'
  if 0;

# fullsitebackup
# by jeff.jke.net
# cc 2008 jeffrey k eliasen

use strict;
use Cwd;

my $drupalroot = $ARGV[0];

my $logfilename = "drupalbackup.log";
my $sitetar = "drupalroot.tar";

my ($base, $backupname, $datestamp);
my ($site, @sites, @dbstrings);
my ($dbstring, %dbfinished);
my ($dbuser, $dbpw, $dbhost, $dbname, $dbid);

if ($drupalroot eq "") {
    usage();
    exit 1;
}

$datestamp = `date +'%m-%d-%Y'`;
chomp $datestamp;

$base = cwd();
open (LOG, ">$base/$logfilename"); # file path and name of log file to use

$backupname = "$drupalroot-$datestamp";

print LOG "Backing up drupal directory at $drupalroot to $base ...\n";

print LOG "\tcreating temp working dir $backupname ...\n";
if (-e $backupname) { die "$backupname already exists, exiting"; }
mkdir $backupname || die "couldn't make temp directory: $!";

print LOG "\tcopying website files from $drupalroot ...\n";
`tar cpvf $base/$backupname/$sitetar $drupalroot` || die "can't tar: $!";

print LOG "\tlooking for drupal databases ...\n";
@sites = `ls $drupalroot/sites/`;
foreach $site (@sites) {
    chomp $site;
    if ($site ne "all" && -d "$drupalroot/sites/$site") {
        open (SETTINGS, "<$drupalroot/sites/$site/settings.php");
        while (<SETTINGS>) {
            if ($_ =~ /^\s*\$db_url\s*=\s*'mysql:\/\/([^']+)'/) {
                push @dbstrings, $1;
                close SETTINGS;
            }
        }
        close SETTINGS;
        print LOG "\t\tfound settings for $site ...\n";
    }
}

print LOG "\tbacking up databases ...\n";
foreach $dbstring (@dbstrings) {
        ($dbuser, $dbpw, $dbhost, $dbname) = ($dbstring =~ /(.+):(.+)@(.+)\/(.+)/);
        $dbid = "$dbhost/$dbname";
        print LOG "\t\tdatabase $dbid: ";
        if (!$dbfinished{$dbid}) {
            $dbfinished{$dbid} = 1;
            `mysqldump --host=$dbhost --user=$dbuser --password=$dbpw --add-drop-table $dbname > $backupname/$dbhost--$dbname.sql`;
            print LOG "done!\n";
        } else {
            print LOG "I've already seen this, skipping ...\n";
        }
}

print LOG "\tcreating compressed file: $backupname.tgz ...\n";
`tar zcpvf $backupname.tgz $backupname`;

print LOG "\tremoving temp dir $backupname ...\n";
`rm -r $backupname`;

$datestamp = `date`;
chomp $datestamp;
print LOG "Backup completed $datestamp\n";

close(LOG);
exit 0;

sub usage() {
print <<'EOF'
usage: fullsitebackup <source> <dest>
       src     the path to the top of your drupal directory
       dest    the name of the compressed file to save the backup to
EOF
}
```
