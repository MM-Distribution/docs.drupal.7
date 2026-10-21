---
title: "Comparison of Charting modules"
source_url: "https://www.drupal.org/docs/7/extend/comparison-of-contributed-modules/comparison-of-charting-modules"
page_type: guide
published: "2014-10-27T08:08:03+00:00"
modified: "2025-04-30T20:53:04+00:00"
breadcrumb: ["Drupal 7", "Extending Drupal 7", "Comparison of contributed modules"]
fetched: "2026-10-21T08:58:12Z"
raw: "raw/docs/7/extend/comparison-of-contributed-modules/comparison-of-charting-modules.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Comparison of Charting modules

------------------------------------------------------------------------

<img src="/files/ScatterGraph.png" data-align="right" alt="Comparison of Charting modules" />

- [About charting modules](#about)
- [Charting wrapper modules](#wrappermodules)
- [Native charting modules](#nativemodules)
- [Other charting modules](#othermodules)
- [Supported Drupal versions](#drupalversions)
- [Supported Charting Libraries](#supportedlibraries)
- [Available integrations](#integrations)
- [Features](#features)
- [Issue Queue Statistics](#stats)
- [Maintenance Scorecards](#scorecards)
- [Charting Modules Discussions](#discussions)
- [Contribute to this comparison](#contribute)

------------------------------------------------------------------------

Charts can help you visualize vast amounts of data in a way that is easily understood. Similar to the saying "A picture is worth more than 1000 words," one may say "A chart is worth more than 1.000 reports" ...

## About charting modules

There are a variety of modules that facilitate the creation of charts. When it comes to charting in Drupal, the saying "There's a module for it" doesn't really apply. In this case, it's more accurate to say, "There are plenty of modules for it" ...

These modules support for various charting libraries that may be desirable based on a site's desired appearance, feature-set, and licensing needs.

**Warning**: The names and/or namespaces of some of the modules, in combination with the various charting libraries they support, can be very confusing! Furthermore, it can be difficult to keep track of which charting module depends on another charting module, or which one is still supported. For anyone getting scared, help might be on the way in the form of [\#2368793: Chart 2.0](/project/chart/issues/2368793 "Status: Active") ...

## Charting wrapper modules

Charting wrapper modules are modules that support the creation of charts, but which depend on at least 1 **native charting module**, further explained below, to produce such charts.

Below is a list of charting wrapper modules:

- [Rate](/project/rate) provides flexible voting widgets for nodes and comments. Optionally it displays the vote results in a chart if the [Chart](/project/chart) module is available.
- [Google Analytics Reporting](/project/google_analytics_reports) provides graphical reporting of a site's tracking data. Graphical reports include a dashboard widget for administrators, a small path-based report in blocks, and a full path-based report. It currently uses the [Chart](/project/chart) module, though the next release will switch to using the [Charts](/project/charts) module.
- The Quiz Stats submodule of [Quiz](/project/quiz) (used to create graded assessments) provides charts using the [Charts](/project/charts) module.
- The Yandex.Metrics Reports submodule of [Yandex.Metrics](https://www.drupal.org/project/yandex_metrics) integrates a website with the Yandex.Metrica, which is an alternative to Google Analytics. It provides charts using the [Charts](/project/charts) module.
- The [Advertisement](/project/ad) module is a powerful advertising system with basic graphical reports created using the [Chart](/project/chart) module.
- [Commerce Reporting](/project/commerce_reports) provides a reporting system for [Drupal Commerce](/project/commerce) via an advanced reports dashboard using the [Charts](/project/charts) module.
- [Support Ticketing System](/project/support) provides a basic ticketing system and helpdesk that is native to Drupal. Optionally it generates basic charts from ticket statistics if the [Chart](/project/chart) module is available.
- [Search Log](/project/search_log) generates charts (some nice eye-candy ...) if the [Chart](/project/chart) module is available.
- [Quant](/project/quant) (**beta** version only for D7, and a D6 version) provides an engine for producing quantitative, time-based analytics for virtually any Drupal component. It takes raw data about normal Drupal actions, such as node creation, and plots the activity over time, with the selected time being configurable. It uses the [Chart](/project/chart) module.
- [Webform Chart](/project/webform_chart) displays [webform](http://drupal.org/project/webform) results in a graphical manner using either the [Chart](/project/chart) or [Charts](/project/charts) module.
- [Webform Charts](/project/webform_charts) (**beta** version only), not to be confused with [Webform Chart](/project/webform_chart), integrates the [Webform](/project/webform) module with the [Charts](/project/charts) module. It integrates with the "Analysis" tab of a Webform to provide charts for each individual component's analytical data.
- [Drupal Remote Dashboard](/project/drd) monitors and manages any number of Drupal installations at once. Optionally the monitoring data will be made visible in graphs if the [Chart](/project/chart) module is available.
- [Poll Chart Block](/project/poll_chart) displays poll's results in a block, with a selectable chart type, and using the [Chart](/project/chart) module.
- [Bugzilla Dashboard](/project/qmo_bugzilla) (D6 release only) sets up a Bugzilla query to run over a set period of time, at a given frequency, and pick up on specific data to display in a chart.
- [CSV Chart](/project/csvchart), which only has a D5 version for now, though recently [\#2368967: Upgrade to Drupal version 6](/project/csvchart/issues/2368967 "Status: Active, Assigned to: Pierre.Vriens") and [\#2368971: Upgrade to Drupal version 7](/project/csvchart/issues/2368971 "Status: Active, Assigned to: Pierre.Vriens") were announced.
- The [Views Chart Tools](/project/views_chart_tools) module (**dev** version only) integrates the advanced features of the interactive HTML5 charts of the [Google Chart Tools API](https://developers.google.com/chart/) with the query building abilities of [views](/project/views). It uses view results to render interactive visualizations containing multiple charts and controls and depends on the [Google Chart Tools for Drupal](/project/google_charts) module.
- The [Charts RGraph](/project/charts_rgraph) module (**alpha** version only) is a canvas and JavaScript based charts library built for web charts. It supports [views](/project/views) through the [Charts](/project/charts) module.
- The [Statistics Pro](/project/statspro) module, which creates statistics with aggregated data. The data is stored in a new table, which is updated with a cron run. It provides statistical results of nodes, comments and users. When specific modules are enabled, it enables specific features which depend one those modules, such as page visualization reports and graphs.
- [Views Charts](/project/views_charts) (**dev** version only for D7, and a D6 version, which requires [Views GroupBy](/project/views_groupby)), not to be confused with [Views Chart Tools](/project/views_chart_tools), provides a "charts" style output for [Views](/project/views) to render the result-set not just as text (list, tabular) but as a PieChart, BarChart, ScatterPlot etc. It has basic usage instructions available as Advanced Help pages. Install and enable it to see the available help. A great presentation about it was done during [DC DrupalCon '09](http://vimeo.com/5306364).
- The [Charts and Graphs Flot](/project/charts_graphs_flot) module, which adds [Flot](http://code.google.com/p/flot/) support for the [Charts and Graphs](http://drupal.org/project/charts_graphs) module using the [Flot module](http://drupal.org/project/flot).

The table below contains an overview of charting wrapper modules and their dependencies upon any of the native charting modules:

<table style="width:100%;">
<colgroup>
<col style="width: 14%" />
<col style="width: 14%" />
<col style="width: 14%" />
<col style="width: 14%" />
<col style="width: 14%" />
<col style="width: 14%" />
<col style="width: 14%" />
</colgroup>
<thead>
<tr class="header">
<th> </th>
<th><a href="/project/forena">Forena</a></th>
<th><a href="/project/google_chart_tools">Google<br />
Chart<br />
Tools</a></th>
<th><a href="/project/chart">Chart</a></th>
<th><a href="/project/charts">Charts</a></th>
<th><a href="/project/charts_graphs">Charts<br />
and<br />
Graphs</a></th>
<th><a href="/project/flot">Flot</a></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><a href="/project/rate">Rate</a></td>
<td>-</td>
<td>-</td>
<td><img src="/misc/watchdog-ok.png" alt="Yes" /></td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr class="even">
<td><a href="/project/google_analytics_reports">Google Analytics Reporting</a></td>
<td>-</td>
<td>-</td>
<td><img src="/misc/watchdog-ok.png" alt="Yes" /> (D6)</td>
<td><img src="/misc/watchdog-ok.png" alt="Yes" /> (D7)</td>
<td>-</td>
<td>-</td>
</tr>
<tr class="odd">
<td><a href="/project/quiz">Quiz</a></td>
<td>-</td>
<td>-</td>
<td>-</td>
<td><img src="/misc/watchdog-ok.png" alt="Yes" /></td>
<td>-</td>
<td>-</td>
</tr>
<tr class="even">
<td><a href="/project/yandex_metrics">Yandex.Metrics</a></td>
<td>-</td>
<td>-</td>
<td><img src="/misc/watchdog-ok.png" alt="Yes" /></td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr class="odd">
<td><a href="/project/ad">Advertisement</a></td>
<td>-</td>
<td>-</td>
<td><img src="/misc/watchdog-ok.png" alt="Yes" /></td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr class="even">
<td><a href="/project/commerce_reports">Commerce Reporting</a></td>
<td>-</td>
<td>-</td>
<td>-</td>
<td><img src="/misc/watchdog-ok.png" alt="Yes" /></td>
<td>-</td>
<td>-</td>
</tr>
<tr class="odd">
<td><a href="/project/support">Support Ticketing System</a></td>
<td>-</td>
<td>-</td>
<td><img src="/misc/watchdog-ok.png" alt="Yes" /></td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr class="even">
<td><a href="/project/search_log">Search Log</a></td>
<td>-</td>
<td>-</td>
<td><img src="/misc/watchdog-ok.png" alt="Yes" /></td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr class="odd">
<td><a href="/project/quant">Quant</a></td>
<td>-</td>
<td>-</td>
<td><img src="/misc/watchdog-ok.png" alt="Yes" /></td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr class="even">
<td><a href="/project/webform_chart">Webform Chart</a></td>
<td>-</td>
<td>-</td>
<td><img src="/misc/watchdog-ok.png" alt="Yes" /> (D6)</td>
<td><img src="/misc/watchdog-ok.png" alt="Yes" /> (D7)</td>
<td>-</td>
<td>-</td>
</tr>
<tr class="odd">
<td><a href="/project/webform_charts">Webform Charts</a></td>
<td>-</td>
<td>-</td>
<td>-</td>
<td><img src="/misc/watchdog-ok.png" alt="Yes" /></td>
<td>-</td>
<td>-</td>
</tr>
<tr class="even">
<td><a href="/project/drd">Drupal Remote Dashboard</a></td>
<td>-</td>
<td>-</td>
<td><img src="/misc/watchdog-ok.png" alt="Yes" /></td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr class="odd">
<td><a href="/project/poll_chart">Poll Chart Block</a></td>
<td>-</td>
<td>-</td>
<td><img src="/misc/watchdog-ok.png" alt="Yes" /></td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr class="even">
<td><a href="/project/qmo_bugzilla">Bugzilla Dashboard</a></td>
<td>-</td>
<td>-</td>
<td>-</td>
<td><img src="/misc/watchdog-ok.png" alt="Yes" /></td>
<td>-</td>
<td>-</td>
</tr>
<tr class="odd">
<td><a href="/project/csvchart">CSV Chart</a></td>
<td>-</td>
<td>-</td>
<td><img src="/misc/watchdog-ok.png" alt="Yes" /> (D5)</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr class="even">
<td><a href="/project/views_chart_tools">Views Chart Tools</a></td>
<td>-</td>
<td><img src="/misc/watchdog-ok.png" alt="Yes" /></td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr class="odd">
<td><a href="/project/charts_rgraph">Charts RGraph</a></td>
<td>-</td>
<td>-</td>
<td>-</td>
<td><img src="/misc/watchdog-ok.png" alt="Yes" /></td>
<td>-</td>
<td>-</td>
</tr>
<tr class="even">
<td><a href="/project/statspro">Statistics Pro</a></td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td><img src="/misc/watchdog-ok.png" alt="Yes" /></td>
<td>-</td>
</tr>
<tr class="odd">
<td><a href="/project/views_charts">Views<br />
Charts</a></td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td><img src="/misc/watchdog-ok.png" alt="Yes" /></td>
<td>-</td>
</tr>
<tr class="even">
<td><a href="/project/charts_graphs_flot">Charts and Graphs Flot</a></td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td><img src="/misc/watchdog-ok.png" alt="Yes" /></td>
<td><img src="/misc/watchdog-ok.png" alt="Yes" /></td>
</tr>
</tbody>
</table>

## Native charting modules

Native charting modules are modules that support the creation of charts, but which do not depend on other modules to produce such charts. These modules may depend on other Drupal modules (e.g. the libraries module), but these other modules are not related to the charting features they offer. Typically these native charting modules use one or more charting related libraries.

### An extensive comparison of modules that depend on the Highcharts javascript library can be found [here](https://www.drupal.org/node/2559993 "Comparison of native charting modules that depend on the Highcharts javascript library").

Below is a list of native charting modules, for which **at least 1 official release** exist:

- [Forena Reports](/project/forena) facilitates the creation of charts by using the [SVG Graph](http://www.goat1000.com/svggraph.php) library. Forena does not depend on [Views](/project/views) for creating charts, however it can be used as an extra views style plugin.
- [Google Chart Tools](/project/google_chart_tools) provides a simple API to build interactive SVG charts, using the [Google Chart Tools](http://code.google.com/apis/chart).
- [Google Chart Tools: Image Charts](/project/chart) currently only supports the deprecated [Google Chart Tools: Image Charts](https://developers.google.com/chart/image/), which is deprecated as of April 20, 2015. Though [\#2371567: Chart 6.x-2.x Release](/project/chart/issues/2371567 "Status: Closed (outdated)"), [\#2371075: Chart 7.x-2.x Release](/project/chart/issues/2371075 "Status: Active") and [\#2368793: Chart 2.0](/project/chart/issues/2368793 "Status: Active") are about addressing that. It is the most commonly used charting module today (over 25K reported installs, which is more then double of all other native charting modules together).
- [Charts](/project/charts) (not to be confused with the charting module with namespace [chart](/project/chart) !!!) provides an API that can be used as a stand-alone API, and the integration with [Views](/project/views) supports building charts with no coding.
- [Charts and Graphs](/project/charts_graphs), which is an API for developers. It can be extended by third-party modules that want to add their own charting implementations. It does nothing by itself. It should only be installed if some other module requires it. [Views Charts](/project/views_charts) is one of the modules using it, while [\#2364427: Renderer for Charts and Graphs APIs](/project/forena/issues/2364427 "Status: Active") is a forena feature request to also consider using it.
- [Flot](/project/flot) provides an API and views integration for using the flot graphing library.
- [Easychart](/project/easychart) is a graphical user interface, built on top of the [Highcharts](http://www.highcharts.com/products/highcharts) javascript library.

Some additional native charting modules, but for which **no official release** exists yet:

- [Views Gantt](/project/views_gantt) (**beta** version only), which provides a views display plugin to show tasks in a GANTT Chart using the (open source) [dhtmlx GANTT javascript library](http://www.dhtmlx.com/docs/products/dhtmlxGantt/).
- [Data Visualization API](/project/data_visualization) (**beta** version only), which allows site builders to create, import & store data visualizations as entities and their data as standardized JSON. A user can then choose which installed data visualization library to use when rendering each data visualization entity.
- [HighchartTable](/project/highcharttable) (**beta** version only) transforms any HTML table on a site into a Highchart by clicking on the cogwheel above it. It doesn't matter whether that table was created through [Views](http://drupal.org/project/views), [Webform](http://drupal.org/project/webform) or a WYSIWYG. *One click* and you have a chart on your page. Easy install of the JS libraries too through Drush with [Features](http://drupal.org/project/features) support via [Strongarm](http://drupal.org/project/strongarm).
- [D3](/project/d3) creates visualizations as [libraries](/project/libraries) (**alpha** version only) which allows one to add/remove visualizations, share them between modules, and integrate them with (for example: [views](/node/2257739)) through library .info files.
- [Highcharts](/project/highcharts) (**alpha** version only), to create charts using the [Highcharts](http://www.highcharts.com/products/highcharts) JS library.
- [Visualization API](/project/visualization) (**alpha** version only), which provides a theme hook that takes a data array and some options and will then render a chart in-place. It also provides a [Views](/project/views) display plugin to visualize data retrieved through Views.
- [Google Chart Tools for Drupal](/project/google_charts) (**dev** version only), not to be confused with [Google Chart Tools](/project/google_chart_tools) !!!). It is a tool for developers to facilitate the use of Google's [Chart Tools](https://developers.google.com/chart/) and its [Visualization API](https://developers.google.com/chart/interactive/docs/reference) within a Drupal site.

Below is an attempt to compare the charting capabilities of the native charting modules, limited to those modules for which at least 1 official release exists.

## Other charting modules

Since this comparison was created, new modules related to charting have been discovered. Consequently, they are still missing in this comparison. Here is an attempt to mention a few:

1.  [Views Dataviz with Google Charts API](/project/views_dataviz), which provides data visualisation for [views](/project/views).
2.  [Comment \#9](/node/2368793#comment-9330663) in [\#2368793: Chart 2.0](/project/chart/issues/2368793 "Status: Active") contains another list of (about 10) modules not included here. Anybody interested in getting the missing ones added here (in a similar format like being used here)?
3.  [Raphaël](/project/raphael) exposing some of the functionality of the [Raphaël](http://raphaeljs.com/) JavaScript vector graphics library.
4.  [JpGraph](/project/jpgraph) is a PHP library providing a simple loader for that library.
5.  [jqplot Charts Library](/project/jqPlot) provides a library interface for [jqPlot](http://www.jqplot.com/) javascript library and is used by (dependency) [Webform reports](https://drupal.org/project/webform_reports).
6.  [Forum Stats](/project/forum_stats) provides statistics on forum usage, using the [Highcharts](http://www.highcharts.com/products/highcharts) library.
7.  [Chartbeat](/project/Chartbeat) provides third party integration with [Chartbeat](http://chartbeat.com/), for real-time site monitoring statistics.
8.  ... (Which other ones should be mentioned here?).

Check out the links to those modules for more details. Better still, if you're familiar with any of these modules, get them added to the comparison here by editing this page. Adding an extra column to the right is probably the easiest approach.

Here are some other topics (not included in the comparisons below) that seem worth addressing:

- [Drush](http://drupal.org/project/drush) support (Yes or No).
- Supported [Views](http://drupal.org/project/views) versions (2, 3 or both).
- [Advanced help](http://drupal.org/project/advanced_help) support (Yes or No).
- [Features](http://drupal.org/project/features) support (Yes or No).

Anybody interested in investigating any of these topics, and adding them to the comparison here (by editing this page)? If not, George (the one Dries talked about at DrupalCon Amsterdam 2014) will hopefully do it ... someday.

## Supported Drupal versions

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 12%" />
<col style="width: 12%" />
<col style="width: 12%" />
<col style="width: 12%" />
<col style="width: 12%" />
<col style="width: 12%" />
<col style="width: 12%" />
</colgroup>
<thead>
<tr class="header">
<th> </th>
<th><a href="/project/forena">Forena</a></th>
<th><a href="/project/google_chart_tools">Google<br />
Chart<br />
Tools</a></th>
<th><a href="/project/chart">Chart</a></th>
<th><a href="/project/charts">Charts</a></th>
<th><a href="/project/charts_graphs">Charts<br />
and<br />
Graphs</a></th>
<th><a href="/project/flot">Flot</a></th>
<th><a href="https://www.drupal.org/project/easychart">Easychart</a></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Drupal 8 support</td>
<td>DEV</td>
<td>?</td>
<td><a href="/node/2139771">#2139771</a></td>
<td><a href="/node/2140651">#2140651</a></td>
<td>?</td>
<td>?</td>
<td><img src="/misc/watchdog-ok.png" alt="Yes" /></td>
</tr>
<tr class="even">
<td>Drupal 7 support</td>
<td><img src="/misc/watchdog-ok.png" alt="Yes" /></td>
<td><img src="/misc/watchdog-ok.png" alt="Yes" /></td>
<td><img src="/misc/watchdog-ok.png" alt="Yes" /></td>
<td><img src="/misc/watchdog-warning.png" alt="Warning" /><br />
(<strong>rc1</strong>)</td>
<td><img src="/misc/watchdog-ok.png" alt="Yes" /></td>
<td><img src="/misc/watchdog-ok.png" alt="Yes" /></td>
<td><img src="/misc/watchdog-ok.png" alt="Yes" /></td>
</tr>
<tr class="odd">
<td>Drupal 6 support</td>
<td><img src="/misc/watchdog-ok.png" alt="Yes" /></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td><img src="/misc/watchdog-ok.png" alt="Yes" /></td>
<td><img src="/misc/watchdog-ok.png" alt="Yes" /></td>
<td><img src="/misc/watchdog-ok.png" alt="Yes" /></td>
<td><img src="/misc/watchdog-ok.png" alt="Yes" /></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
</tr>
</tbody>
</table>

## Supported Charting Libraries

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 11%" />
<col style="width: 11%" />
<col style="width: 11%" />
<col style="width: 11%" />
<col style="width: 11%" />
<col style="width: 11%" />
<col style="width: 11%" />
<col style="width: 11%" />
</colgroup>
<thead>
<tr class="header">
<th> </th>
<th><a href="/project/forena">Forena</a></th>
<th><a href="/project/google_chart_tools">Google<br />
Chart<br />
Tools</a></th>
<th><a href="/project/chart">Chart</a></th>
<th><a href="/project/charts">Charts</a></th>
<th><a href="/project/charts_graphs">Charts<br />
and<br />
Graphs</a></th>
<th><a href="/project/flot">Flot</a></th>
<th><a href="https://www.drupal.org/project/easychart">Easychart</a></th>
<th><a href="/project/highcharttable">Highchart<br />
Table</a></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><a href="http://www.goat1000.com/svggraph.php">PHP SVG Graph</a></td>
<td><img src="/misc/watchdog-ok.png" alt="Yes" /></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
</tr>
<tr class="even">
<td><a href="https://developers.google.com/chart/image/">Google Chart Tools: Image API</a></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td><img src="/misc/watchdog-ok.png" alt="Yes" /></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
</tr>
<tr class="odd">
<td><a href="https://developers.google.com/chart/">Google Charts</a></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td><img src="/misc/watchdog-ok.png" alt="Yes" /></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td><img src="/misc/watchdog-ok.png" alt="Yes" /></td>
<td><img src="/misc/watchdog-ok.png" alt="Yes" /></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
</tr>
<tr class="even">
<td><a href="http://www.highcharts.com/">Highcharts</a></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td><img src="/misc/watchdog-ok.png" alt="Yes" /></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td><img src="/misc/watchdog-ok.png" alt="Yes" /></td>
<td><img src="/misc/watchdog-ok.png" alt="Yes" /></td>
</tr>
<tr class="odd">
<td><a href="http://teethgrinder.co.uk/open-flash-chart/">Open Flash Chart</a></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td><img src="/misc/watchdog-ok.png" alt="Yes" /></td>
<td>?</td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
</tr>
<tr class="even">
<td><a href="http://teethgrinder.co.uk/open-flash-chart-2/">Open Flash Chart 2</a></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td>?</td>
<td><img src="/misc/watchdog-ok.png" alt="Yes" /> (D6)</td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
</tr>
<tr class="odd">
<td><a href="http://www.amcharts.com/">amCharts</a></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td><img src="/misc/watchdog-ok.png" alt="Yes" /> (D6)</td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
</tr>
<tr class="even">
<td><a href="http://code.google.com/p/flot/">Flot</a></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td><img src="/misc/watchdog-ok.png" alt="Yes" /></td>
<td><img src="/misc/watchdog-ok.png" alt="Yes" /></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
</tr>
<tr class="odd">
<td><a href="http://d3js.org/">D3</a></td>
<td><img src="/misc/watchdog-ok.png" alt="Yes" /><br />
<a href="/node/2364427#comment-9363133">#2364427</a></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td><img src="/misc/watchdog-ok.png" alt="Yes" /></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
</tr>
<tr class="even">
<td><a href="http://bluff.jcoglan.com/">Bluff</a></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td><img src="/misc/watchdog-ok.png" alt="Yes" /></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
</tr>
<tr class="odd">
<td><a href="http://jpgraph.net/">JpGraph</a></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
</tr>
<tr class="even">
<td><a href="http://www.pchart.net/">pChart</a></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
</tr>
<tr class="odd">
<td><a href="http://www.dhtmlx.com/docs/products/dhtmlxGantt/">dhtmlx GANTT JS library</a></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
</tr>
</tbody>
</table>

***Note***: if the above list of libraries isn't enough yet, then checkout the list included in [Graph visualization library in JavaScript](http://stackoverflow.com/questions/7034/graph-visualization-library-in-javascript?rq=1).

## Available integrations

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 12%" />
<col style="width: 12%" />
<col style="width: 12%" />
<col style="width: 12%" />
<col style="width: 12%" />
<col style="width: 12%" />
<col style="width: 12%" />
</colgroup>
<thead>
<tr class="header">
<th> </th>
<th><a href="/project/forena">Forena</a></th>
<th><a href="/project/google_chart_tools">Google<br />
Chart<br />
Tools</a></th>
<th><a href="/project/chart">Chart</a></th>
<th><a href="/project/charts">Charts</a></th>
<th><a href="/project/charts_graphs">Charts<br />
and<br />
Graphs</a></th>
<th><a href="/project/flot">Flot</a></th>
<th><a href="https://www.drupal.org/project/easychart">Easychart</a></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><a href="/project/views">Views</a></td>
<td><img src="/misc/watchdog-ok.png" alt="Yes" /></td>
<td><img src="/misc/watchdog-ok.png" alt="Yes" /></td>
<td><img src="/misc/watchdog-ok.png" alt="Yes" /></td>
<td><img src="/misc/watchdog-ok.png" alt="Yes" /></td>
<td><img src="/misc/watchdog-ok.png" alt="Yes" /></td>
<td><img src="/misc/watchdog-ok.png" alt="Yes" /></td>
<td><img src="/misc/watchdog-ok.png" alt="Yes" /></td>
</tr>
<tr class="even">
<td><a href="/project/feeds">Feeds</a></td>
<td><img src="/misc/watchdog-ok.png" alt="Yes" /></td>
<td>?</td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td>?</td>
<td>?</td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
</tr>
<tr class="odd">
<td><a href="/project/bean">BEAN</a></td>
<td><img src="/misc/watchdog-ok.png" alt="Yes" /></td>
<td>?</td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td>?</td>
<td>?</td>
<td>?</td>
</tr>
<tr class="even">
<td><a href="https://www.drupal.org/project/wysiwyg">Wysiwig</a></td>
<td>?</td>
<td>?</td>
<td>?</td>
<td>?</td>
<td>?</td>
<td>?</td>
<td><img src="/misc/watchdog-ok.png" alt="Yes" /></td>
</tr>
</tbody>
</table>

## Features

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 12%" />
<col style="width: 12%" />
<col style="width: 12%" />
<col style="width: 12%" />
<col style="width: 12%" />
<col style="width: 12%" />
<col style="width: 12%" />
</colgroup>
<thead>
<tr class="header">
<th> </th>
<th><a href="/project/forena">Forena</a></th>
<th><a href="/project/google_chart_tools">Google<br />
Chart<br />
Tools</a></th>
<th><a href="/project/chart">Chart</a></th>
<th><a href="/project/charts">Charts</a></th>
<th><a href="/project/charts_graphs">Charts<br />
and<br />
Graphs</a></th>
<th><a href="/project/flot">Flot</a></th>
<th><a href="https://www.drupal.org/project/easychart">Easychart</a></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>JSON support</td>
<td><img src="/misc/watchdog-ok.png" alt="Yes" /><br />
<a href="/node/2362855#comment-9653785">#2362855</a></td>
<td>?</td>
<td>?</td>
<td><img src="/misc/watchdog-ok.png" alt="Yes" /><br />
<a href="/node/2429505">#2429505</a></td>
<td>?</td>
<td>?</td>
<td> </td>
</tr>
<tr class="even">
<td>XML support</td>
<td><img src="/misc/watchdog-ok.png" alt="Yes" /><br />
<a href="/node/2437701#comment-9663819">#2437701</a></td>
<td>?</td>
<td>?</td>
<td>?</td>
<td>?</td>
<td>?</td>
<td> </td>
</tr>
<tr class="odd">
<td>CSV support</td>
<td>?</td>
<td>?</td>
<td>?</td>
<td>?</td>
<td>?</td>
<td>?</td>
<td><img src="/misc/watchdog-ok.png" alt="Yes" /></td>
</tr>
<tr class="even">
<td>Multilanguage support</td>
<td><img src="/misc/watchdog-ok.png" alt="Yes" /></td>
<td>?</td>
<td><img src="/misc/watchdog-ok.png" alt="Yes" /></td>
<td><img src="/misc/watchdog-ok.png" alt="Yes" /></td>
<td>?</td>
<td>?</td>
<td><img src="/misc/watchdog-ok.png" alt="Yes" /></td>
</tr>
<tr class="odd">
<td>IE support</td>
<td><img src="/misc/watchdog-ok.png" alt="Yes" /></td>
<td><a href="/node/1987126">#1987126</a></td>
<td>?</td>
<td>?</td>
<td><img src="/misc/watchdog-ok.png" alt="Yes" /></td>
<td>?</td>
<td> </td>
</tr>
<tr class="even">
<td>export chart to PDF</td>
<td><img src="/misc/watchdog-ok.png" alt="Yes" /></td>
<td><a href="/node/1899032">#1899032</a></td>
<td>?</td>
<td>?</td>
<td>?</td>
<td>?</td>
<td><img src="/misc/watchdog-ok.png" alt="Yes" /></td>
</tr>
<tr class="odd">
<td>export chart to SVG</td>
<td>?</td>
<td>?</td>
<td>?</td>
<td>?</td>
<td>?</td>
<td>?</td>
<td><img src="/misc/watchdog-ok.png" alt="Yes" /></td>
</tr>
<tr class="even">
<td>export chart to jpg</td>
<td>?</td>
<td>?</td>
<td>?</td>
<td>?</td>
<td>?</td>
<td>?</td>
<td><img src="/misc/watchdog-ok.png" alt="Yes" /></td>
</tr>
<tr class="odd">
<td>export chart to png</td>
<td>?</td>
<td>?</td>
<td>?</td>
<td>?</td>
<td>?</td>
<td>?</td>
<td><img src="/misc/watchdog-ok.png" alt="Yes" /></td>
</tr>
<tr class="even">
<td>Privacy</td>
<td><img src="/misc/watchdog-ok.png" alt="Yes" /></td>
<td><a href="/node/1733940"><img src="/misc/watchdog-warning.png" alt="Attention" /></a></td>
<td><a href="/node/1733940"><img src="/misc/watchdog-warning.png" alt="Attention" /></a></td>
<td><a href="/node/1733940"><img src="/misc/watchdog-warning.png" alt="Attention" /></a></td>
<td>?</td>
<td>?</td>
<td>?</td>
</tr>
</tbody>
</table>

## Issue Queue Statistics

<table style="width:100%;">
<colgroup>
<col style="width: 14%" />
<col style="width: 14%" />
<col style="width: 14%" />
<col style="width: 14%" />
<col style="width: 14%" />
<col style="width: 14%" />
<col style="width: 14%" />
</colgroup>
<thead>
<tr class="header">
<th> </th>
<th><a href="/project/forena">Forena</a></th>
<th><a href="/project/google_chart_tools">Google<br />
Chart<br />
Tools</a></th>
<th><a href="/project/chart">Chart</a></th>
<th><a href="/project/charts">Charts</a></th>
<th><a href="/project/charts_graphs">Charts<br />
and<br />
Graphs</a></th>
<th><a href="/project/flot">Flot</a></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Open Issues,<br />
Fixed Issues,<br />
Total Issues</td>
<td><a href="/project/issues/forena?categories=All">33</a>,<br />
<a href="/project/issues/forena?status=2">0</a>,<br />
<a href="/project/issues/forena?status=All&amp;categories=All">318</a></td>
<td><a href="/project/issues/google_chart_tools?categories=All">49</a>,<br />
<a href="/project/issues/google_chart_tools?status=2">0</a>,<br />
<a href="/project/issues/google_chart_tools?status=All&amp;categories=All">79</a></td>
<td><a href="/project/issues/chart?categories=All">50</a>,<br />
<a href="/project/issues/chart?status=2">0</a>,<br />
<a href="/project/issues/chart?status=All&amp;categories=All">173</a></td>
<td><a href="/project/issues/charts?categories=All">82</a>,<br />
<a href="/project/issues/charts?status=2">9</a>,<br />
<a href="/project/issues/charts?status=All&amp;categories=All">287</a></td>
<td><span>27</span>,<br />
<a href="/project/issues/charts_graphs?status=2">0</a>,<br />
<a href="/project/issues/charts_graphs?status=All&amp;categories=All">129</a></td>
<td><a href="/project/issues/flot?categories=All">59</a>,<br />
<a href="/project/issues/flot?status=2">0</a>,<br />
<a href="/project/issues/flot?status=All&amp;categories=All">88</a></td>
</tr>
<tr class="even">
<td>Unresolved Issues /<br />
Total Issues</td>
<td>10%</td>
<td>62%</td>
<td>29%</td>
<td>25%</td>
<td>21%</td>
<td>67%</td>
</tr>
</tbody>
</table>

**Special Request**: Seems like transforming the tabular format above in a corresponding **CHART** can be done via [HighchartTable](https://drupal.org/project/highchartttable), but how to get this module enabled on drupal.org? As an alternative: add a row to the table with links to such chart for each of the modules, maybe with some details about the required steps to create these charts?

## Maintenance Scorecards

[\#2186377: Highlight projects that follow Best Practices](/project/drupalorg/issues/2186377 "Status: Needs work") contains a list of ***23 criteria*** (=28-5) that might help to evaluate the maintenance and support of contributed modules. Below is an attempt to apply those criteria to each of the native charting modules, however with some minor variations / interpretations to provide more accurate details.

**Tip**: some of the ![Yes](/misc/watchdog-ok.png) and ![Yes](/misc/watchdog-error.png) icons are hyperlinked, such as the ones for *(7)* .

<table style="width:100%;">
<colgroup>
<col style="width: 14%" />
<col style="width: 14%" />
<col style="width: 14%" />
<col style="width: 14%" />
<col style="width: 14%" />
<col style="width: 14%" />
<col style="width: 14%" />
</colgroup>
<thead>
<tr class="header">
<th> </th>
<th><a href="/project/forena">Forena</a></th>
<th><a href="/project/google_chart_tools">Google<br />
Chart<br />
Tools</a></th>
<th><a href="/project/chart">Chart</a></th>
<th><a href="/project/charts">Charts</a></th>
<th><a href="/project/charts_graphs">Charts<br />
and<br />
Graphs</a></th>
<th><a href="/project/flot">Flot</a></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><em>(1)</em> No open bugs +1 year</td>
<td>?</td>
<td>?</td>
<td>?</td>
<td>?</td>
<td>?</td>
<td>?</td>
</tr>
<tr class="even">
<td><em>(2)</em> No RTBC'd items +1 month</td>
<td>?</td>
<td>?</td>
<td>?</td>
<td>?</td>
<td>?</td>
<td>?</td>
</tr>
<tr class="odd">
<td><em>(3)</em> Stable release every year</td>
<td>?</td>
<td>?</td>
<td>?</td>
<td>?</td>
<td>?</td>
<td>?</td>
</tr>
<tr class="even">
<td><em>(4)</em> Last commits <strong>(*1*)</strong></td>
<td><a href="/node/728764/commits">Feb 11,<br />
2015</a></td>
<td><a href="/node/1508666/commits">Feb 27,<br />
2013</a></td>
<td><a href="/node/206038/commits">Nov 14,<br />
2014</a></td>
<td><a href="/node/232629/commits">Feb 13,<br />
2015</a></td>
<td><a href="/node/390684/commits">Mar 2,<br />
2015</a></td>
<td><a href="/node/314650/commits">Jul 16,<br />
2012</a></td>
</tr>
<tr class="odd">
<td><em>(7)</em> Community docu</td>
<td><a href="https://drupal.org/node/2041363"><img src="/misc/watchdog-ok.png" alt="Yes" /></a></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
<td><a href="/node/2370811"><img src="/misc/watchdog-ok.png" alt="Yes" /></a></td>
<td><a href="https://drupal.org/node/233753"><img src="/misc/watchdog-ok.png" alt="Yes" /></a></td>
<td><a href="https://drupal.org/node/681660"><img src="/misc/watchdog-ok.png" alt="Yes" /></a></td>
<td><img src="/misc/watchdog-error.png" alt="No" /></td>
</tr>
<tr class="even">
<td><em>(8)</em> Alpha / Beta duration</td>
<td>?</td>
<td>?</td>
<td>?</td>
<td>?</td>
<td>?</td>
<td>?</td>
</tr>
<tr class="odd">
<td><em>(9)</em> Recommended release present</td>
<td>?</td>
<td>?</td>
<td>?</td>
<td>?</td>
<td>?</td>
<td>?</td>
</tr>
<tr class="even">
<td><em>(11)</em> Support 2 core releases <strong>(*2*)</strong></td>
<td>?</td>
<td>?</td>
<td>?</td>
<td>?</td>
<td>?</td>
<td>?</td>
</tr>
<tr class="odd">
<td><em>(12)</em> DEV release for D8</td>
<td>?</td>
<td>?</td>
<td>?</td>
<td>?</td>
<td>?</td>
<td>?</td>
</tr>
<tr class="even">
<td><em>(13)</em> Committers</td>
<td><a href="/node/728764/committers">3</a></td>
<td><a href="/node/1508666/committers">6</a></td>
<td><a href="/node/206038/committers">12</a></td>
<td><a href="/node/232629/committers">3</a></td>
<td><a href="/node/390684/committers">5</a></td>
<td><a href="/node/314650/committers">4</a></td>
</tr>
<tr class="odd">
<td><em>(14)</em> Maint- and Dev-status</td>
<td>?</td>
<td>?</td>
<td>?</td>
<td>?</td>
<td>?</td>
<td>?</td>
</tr>
<tr class="even">
<td><em>(15)</em> Image on project page</td>
<td>?</td>
<td>?</td>
<td>?</td>
<td>?</td>
<td>?</td>
<td>?</td>
</tr>
<tr class="odd">
<td><em>(16)</em> SimpleTests or Unit Tests</td>
<td>?</td>
<td>?</td>
<td>?</td>
<td>?</td>
<td>?</td>
<td>?</td>
</tr>
<tr class="even">
<td><em>(17)</em> Meaningful release notes</td>
<td>?</td>
<td>?</td>
<td>?</td>
<td>?</td>
<td>?</td>
<td>?</td>
</tr>
<tr class="odd">
<td><em>(18)</em> Automated testing enabled</td>
<td>?</td>
<td>?</td>
<td>?</td>
<td>?</td>
<td>?</td>
<td>?</td>
</tr>
<tr class="even">
<td><em>(19)</em> README.txt &amp; INSTALL.txt</td>
<td>?</td>
<td>?</td>
<td>?</td>
<td>?</td>
<td>?</td>
<td>?</td>
</tr>
<tr class="odd">
<td><em>(20)</em> CHANGELOG.txt</td>
<td>?</td>
<td>?</td>
<td>?</td>
<td>?</td>
<td>?</td>
<td>?</td>
</tr>
<tr class="even">
<td><em>(23)</em> Project's purpose teaser</td>
<td>?</td>
<td>?</td>
<td>?</td>
<td>?</td>
<td>?</td>
<td>?</td>
</tr>
<tr class="odd">
<td><em>(24)</em> Project description +500 chars</td>
<td>?</td>
<td>?</td>
<td>?</td>
<td>?</td>
<td>?</td>
<td>?</td>
</tr>
<tr class="even">
<td><em>(25)</em> Headings &amp; docu links</td>
<td>?</td>
<td>?</td>
<td>?</td>
<td>?</td>
<td>?</td>
<td>?</td>
</tr>
<tr class="odd">
<td><em>(26)</em> Downloads<br />
/ installs ratio</td>
<td><a href="/project/usage/forena">8.700<br />
/650</a></td>
<td><a href="/project/usage/google_chart_tools">38.900<br />
/2.900</a></td>
<td><a href="/project/usage/chart">113.000<br />
/25.900</a></td>
<td><a href="/project/usage/charts">58.300<br />
/9.250</a></td>
<td><a href="/project/usage/charts_graphs">29.000<br />
/2.600</a></td>
<td><a href="/project/usage/flot">12.000<br />
/700</a></td>
</tr>
<tr class="even">
<td><em>(27)</em> Translations available</td>
<td>?</td>
<td>?</td>
<td>?</td>
<td>?</td>
<td>?</td>
<td>?</td>
</tr>
<tr class="odd">
<td><em>(28)</em> Contributing users in commits</td>
<td>?</td>
<td>?</td>
<td>?</td>
<td>?</td>
<td>?</td>
<td>?</td>
</tr>
</tbody>
</table>

**Notes**:

- **(\*1\*)**: Variation of '*If there are open bugs, see that there is activity in git every 6 months*'.
- **(\*2\*)**: Refer to [Supported Drupal versions](#drupalversions) for more detailed info.

------------------------------------------------------------------------

If you want to help completing or correcting the above criteria,  
it's fairly easy, just a lot of work to do all the research. So please ... [do so now](/node/2363985/edit)

## Charting Modules Discussions

- [Another comparison](https://groups.drupal.org/node/439438) about charting modules ... A group with related visualisation topics also.
- [History keeps repeating](https://groups.drupal.org/node/9946).
- [Charting and Graphing Modules](https://groups.drupal.org/node/93064).

## Contribute to this comparison

The comparison above reflects Drupal developments up until early 2015. It may become incomplete or outdated (e.g. because of recent evolutions in any of these modules), and it contains some "?" marks to indicate missing information. Hopefully there are no errors in it!

If you want to help to extend, enhance, complete or correct it, please ... [do so now](/node/2363985/edit)

## [Comparison of native charting modules that depend on the Highcharts javascript library](/docs/7/extend/comparison-of-contributed-modules/comparison-of-charting-modules/comparison-of-native-charting-modules-that-depend-on-the-highcharts-javascript-library)

Inspired by Pierre.Vriens and his extensive Comparison of Charting modules, I wrote this extension on native charting modules that depend on
