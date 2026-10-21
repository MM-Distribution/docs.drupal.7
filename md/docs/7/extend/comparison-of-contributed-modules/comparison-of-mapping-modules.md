---
title: "Comparison of Mapping modules"
source_url: "https://www.drupal.org/docs/7/extend/comparison-of-contributed-modules/comparison-of-mapping-modules"
page_type: page
last_updated: "Last updated on 30 April 2025"
published: "2012-07-30T05:13:34+00:00"
modified: "2025-04-30T20:53:04+00:00"
breadcrumb: ["Drupal 7", "Extending Drupal 7", "Comparison of contributed modules"]
fetched: "2026-10-21T09:00:17Z"
raw: "raw/docs/7/extend/comparison-of-contributed-modules/comparison-of-mapping-modules.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# Comparison of Mapping modules

This page aims to provide developers and site builders some navigation on the sea of options for the mapping of location data sets in Drupal D7. This is by no means an extensive survey. The idea is that by listing a number of the most popular modules side by side with their features, it will make it easier for the reader to shortlist modules for their specific needs before examining details on the various project and documentation pages.

In general you'll need at least two modules to create maps from location data: one to provide a location data storage facility and one to render the locations as markers on a map.

Examples of location storage modules are: [Location](http://drupal.org/project/location), [Geofield](http://drupal.org/project/geofield) and [Geolocation field](http://drupal.org/project/geolocation) and [Get Locations](http://drupal.org/project/getlocations).

Additionally, while the table below indicates required location storage methods (such as "Geofield" for "Leaflets"), it is in fact possible to deploy a module such as [Geocoder](https://drupal.org/project/geocoder) to, for example, use Location as a storage method for Leaflet or OpenLayers.

Examples of map rendering modules are: [IP Geolocation Views and Maps](http://drupal.org/project/ip_geoloc), [GMap](http://drupal.org/project/gmap), [Get Locations](http://drupal.org/project/getlocations), [OpenLayers](http://drupal.org/project/openlayers) and [Leaflet](http://drupal.org/project/leaflet). We've used these map renderers as the main index into the comparison table below (first row).

Some of the location storage modules come with map renderers built in, although these are generally for a single location only, e.g. when viewing a node (example: [Geolocation field](http://drupal.org/project/geolocation)). [Geofield](http://drupal.org/project/geofield) and [Get Locations](http://drupal.org/project/getlocations) have their own Google Maps v3 interfaces to produce maps containing multiple location markers.

There is another related comparison page on geo module at [Geospatial Modules Assessment.](https://groups.drupal.org/node/89769 "Geospatial Modules Assessment.")

Please edit this page if you find inaccuracies or want to add mapping modules or features to the list.

Mapping module

[IP Geolocation Views & Maps](http://drupal.org/project/ip_geoloc)

[GMap](http://drupal.org/project/gmap)

[Get Locations](http://drupal.org/project/getlocations)

[OpenLayers](http://drupal.org/project/openlayers)

[Leaflet](http://drupal.org/project/leaflet)

Supported location storage modules

[Geofield](http://drupal.org/project/geofield)  
[Geolocation field](http://drupal.org/project/geolocation)  
[Get Locations](http://drupal.org/project/getlocations)  
[Location](http://drupal.org/project/location)  
any contrib module

[Location](http://drupal.org/project/location)

[Geofield](http://drupal.org/project/geofield)  
[Geolocation field](http://drupal.org/project/geolocation)  
  
[Get Locations](http://drupal.org/project/getlocations)

[Geofield](http://drupal.org/project/geofield), [PostGIS](http://drupal.org/project/postgis)

[Geofield](http://drupal.org/project/geofield)

Maps generated from

access log,  
views with any lat-long field

nodes & user accounts,  
views with Location module fields

nodes & user accounts,  
views with Getlocations_fields field, Geolocation Field or Geofield fields

views with Geofield fields

views with Geofield fields

Supported map providers

Google Maps v3, many others via its [OpenLayers](http://drupal.org/project/openlayers) and [Leaflet More Maps](http://drupal.org/project/leaflet_more_maps) interfaces

Google Maps v2, Google Maps v3 (development release)

Google Maps v3, Leaflet, Openlayers

many

defaults to OSM Mapnik, many more via [Leaflet More Maps](http://drupal.org/project/leaflet_more_maps)

Dependencies & libraries to download

[Views](http://drupal.org/project/views)

([Views](http://drupal.org/project/views))

[Libraries](http://drupal.org/project/libraries), marker image library, ([Views](http://drupal.org/project/views))

[Views](http://drupal.org/project/views), [Proj4js](https://www.drupal.org/project/proj4js), [(Libraries)](http://drupal.org/project/libraries)

[Libraries](http://drupal.org/project/libraries), [Leaflet library](http://leafletjs.com/), [Views](http://drupal.org/project/views)

Availability

D7

D6, D7

D6, D7

D6, D7

D7,D8

Display visitor marker amongst data locations

yes, with color configurable on all 3 map renderers

no

yes

no

no

Map centering options

- fixed point
- visitor's HTML5 location
- 1<sup>st</sup> location from view
- center of gravity

location of node arg.

configurable

- fixed point
- visitor's HTML5 location

yes, with the [IP Geolocation Views & Maps module](https://www.drupal.org/project/ip_geoloc)

Configurable marker balloon texts

yes, any fields from view

yes, any fields from view

yes, defaults to address or field from view

yes, any fields from view

yes, either one or all fields from view

Marker colors by taxonomy

yes, on all 3 map renderers

yes

yes

yes via [OpenLayers Taxonomy](http://drupal.org/project/openlayers_taxonomy)

no

Marker colors by any Views field

yes, on all 3 map renderers

yes

no

no

no

Other module integrations

[Commerce](http://drupal.org/project/commerce), [Leaflet MarkerCluster](http://drupal.org/project/leaflet_markercluster)

[Colorbox](http://drupal.org/project/colorbox), [jquery_colorpicker](https://www.drupal.org/project/jquery_colorpicker), [Smart IP](https://www.drupal.org/project/smart_ip), [Countries](https://www.drupal.org/project/countries)

many, see [project page](http://drupal.org/project/openlayers)

[Leaflet MarkerCluster](http://drupal.org/project/leaflet_markercluster)

Comments

easy to use, [OpenLayers](http://drupal.org/project/openlayers) interface much simplified compared to original.

“GMap is considered a legacy module” ([project page](http://drupal.org/project/gmap))

easy to use, many config options

many canvases to choose from; hard to use at first but very flexible, see this [tutorial for 7.x-2.x](http://drupal.org/node/1481374). Virtually no documentation for version 7.x-3.1+. Works well on mobile.

easy to use, few config options, colors etc. though Leaflet Moremaps adds to choices. Strong fit for mobile, very lightweight.
