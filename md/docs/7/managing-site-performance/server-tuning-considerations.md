---
title: "Server tuning considerations"
source_url: "https://www.drupal.org/docs/7/managing-site-performance/server-tuning-considerations"
page_type: page
last_updated: "Last updated on 18 June 2019"
published: "2003-08-24T20:19:00+00:00"
modified: "2019-06-18T05:51:46+00:00"
breadcrumb: ["Drupal 7", "Managing Drupal 7 site performance and scalability"]
fetched: "2026-10-21T07:01:16Z"
raw: "raw/docs/7/managing-site-performance/server-tuning-considerations.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Server tuning considerations

The performance of your Drupal site is dependent on three main factors: the goals of your site, the resource demands of your site traffic, and the system performance and configuration of underlying technologies.

### Identifying Drupal performance goals

If the goals of your site are to have a speedy user experience, such as Google, then you should focus on simplicity and ensure you have the resources to deliver pages in 1.5 seconds or less. If your goal is to have an aesthetically pleasing site, then a rich theme with things like lots of interactive JavaScript and longer load times might be acceptable. Either way you should begin with clear goals in mind before tuning your site for performance because there are many permutations of performance.

### Analyzing your site's traffic and resource consumption

You shouldn't use other system administrators' performance configurations. Each site is unique and must be tailored to address your sites traffic impact on four resources: bandwidth, CPU, memory, and disk input/output.

Profile your site's performance loading: bandwidth, anonymous page views (general reads), concurrent number of users (unique reads), concurrent number of user posts (writes) are all important in building your sites profile.

### Understanding and configuring your stack for performance

Configuring your server for performance falls outside the scope of the Drupal handbook and you should reference authoritative sources for each component of your server hardware and software stack. In many cases you will not have control of your hardware or the software components you rely on. We provide a list of configurable options that other Drupal administrators have found useful in tuning their sites for performance. **It is possible to destroy your site by configuring incorrectly. Be careful and back up configurations before making changes.**

1.  Understanding LAMP performance. This [LAMP performance study](http://web.archive.org/web/20061115173834/http://sourcelabs.com/pdfs/SourceLabsApacheMySQLPHPTestResults.pdf) revealed that **Apache is bandwidth limited**, **PHP is CPU limited**, and **MySQL is memory limited** and disk I/O bound. Be sure to compile your stack natively for maximum performance. Numerous performance enhancements related to process management and file systems in the 2.6.3x Linux kernel series (see e.g. <http://kernelnewbies.org/Linux26Changes> ) makes a recent Linux version or updated kernel highly advisable. You can also read [Optimize high traffic servers](http://www.crucialp.com/resources/tutorials/server-administration/optimize-tweak-high-traffic-servers-apache-load.php).

2.  Analyze your site's performance bottlenecks: CPU, memory, bandwidth, input/output. Once you have identified what is causing your system performance problems you can make configuration changes or resource upgrades. Use top and ps for analysing processes that are using up too much RAM or CPU. Netstat, [mrtg](http://oss.oetiker.ch/mrtg/)/[awstats](http://awstats.sourceforge.net/), who's online block will help for identifying network problems.  

    ``` php
    top
    ps -aux
    netstat -anp | sort -u
    ```

    If there are other applications running on your server, such as mail, ssh, anti-virus, spam checking, web services, custom applications, etc, that are consuming constrained resources, you might want to move them to a new server.

3.  Bad guests consuming too many resources: Crawlers, Aggregators, Spammers. Search engines may crawl your site and cause a performance degradation, although if they crawl as an anonymous user then they should received cached pages which consume less resources. Slow down the robots crawling your site by adding a robots.txt line like this:  

    ``` php
          User-Agent: *
          Crawl-Delay: 10
          Disallow: /archive
    ```

    Here 10 is the delay in seconds between page requests. Disallow robots from sections of your site that do not need indexing. See [Controlling what gets indexed -- the robots.txt file](/node/22265).

    Some RSS clients are set to check for aggregator feed updates too frequently. Check your logs for aggressive reads of feeds from a specific IP address. Spammers have many ways of consuming your sites resources, be sure your site has a spam blocking strategy. Since version 4.7, Drupal has had a mechanism that ensures forms originate from a given Drupal site installation and not from forms on remote servers. This prevents spammers from creating large amounts of comment and trackback spam remotely.

4.  [Apache performance](http://httpd.apache.org/docs/2.4/misc/perf-tuning.html) Apache is usually bandwidth limited so you should be aware how much bandwidth your server has access to. You can ask your hosting provider how much bandwidth you have or you can use a tool like [lperf](http://sourceforge.net/projects/iperf). The mod_rewrite module for Apache can consume resources if the directives are included in local directories through .htaccess files. If you have control of the Apache configuration then these directives should be moved to httpd.conf. You can also configure Apache to handle more connections with [MaxSpareServers](http://httpd.apache.org/docs/2.0/mod/prefork.html#maxspareservers), [ServerLimit](http://httpd.apache.org/docs/2.0/mod/mpm_common.html#serverlimit), [MaxClients](http://httpd.apache.org/docs/2.0/mod/mpm_common.html#maxclients). CGI is slow. mod_php is popular and fast, FastCGI is fast and secure. [PHP-FPM](http://php-fpm.org/about/) (PHP FastCGI Process Manager) has become increasingly popular and offers more features and greater stability than FastCGI. Read this tutorial on configuring Apache for [Configuring Apache for maximum performance.](http://linuxgazette.net/123/vishnu.html)

5.  [PHP tuning](/node/2602)

6.  [MySQL performance tuning](http://drupal.org/node/51263)

7.  Bandwidth: Images or media are likely to be the greatest source of bandwidth consumption which will limit Apache's performance. In order to ensure images are delivered quickly the theme should explictly call the images directly to reduce the PHP overhead of looking for image files. Details will be provided in the future.

8.  Drupal resource consumption: [Profiling memory usage](/node/659980), measure DB query times, and duplicate queries for modules or pages with [devel.module](/project/devel).

    The number of modules enabled on your site may affect performance but should be measured using the techniques outlined above. If the module has slow query times look at tuning the tables with schema changes and using the the MySQL optimization tools, such as ANALYSE and EXPLAIN. Other areas for analysis are theme resource consumption if your theme has a lot of PHP calls.

    There are several known performance issues in Drupal 4.6.5 including the URL alias table is loaded into memory frequently and the use of Path and PathAuto modules will lead to an increase in the number of aliases in the table (fixed in 4.7 and higher). Recent improvements to session handling for anonymous users and a proposed file cache that bypasses Drupal's page loading mechanisms offer significant performance improvements for anonymous users.

9.  Configuring Drupal for performance: Cron jobs such as aggregating lots of feeds can be resource intensive. If the cron jobs are set too frequently there can be a consistent drain on server performance. Drupal has a cache that is very effective for pages served to anonymous users. It can be found at **Administer \>\> SIte Configuration \>\> Performance** (admin/settings/performance)

10. Server architectures for scalability and performance: separate web server and database server, MySQL replication topologies, clustering servers.
