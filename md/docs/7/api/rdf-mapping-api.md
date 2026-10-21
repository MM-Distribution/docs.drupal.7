---
title: "RDF Mapping API"
source_url: "https://www.drupal.org/docs/7/api/rdf-mapping-api"
page_type: guide
published: "2016-10-13T19:50:53+00:00"
modified: "2016-10-13T19:50:53+00:00"
breadcrumb: ["Drupal 7", "Drupal 7 APIs"]
fetched: "2026-10-21T07:55:51Z"
raw: "raw/docs/7/api/rdf-mapping-api.html"
license: "CC BY-SA 2.0, (c) individual contributors; see LICENSE"
---

# RDF Mapping API

The RDF Mapping API allows you to expose your site's data for easy re-use by mapping bundles to RDF types and fields to RDF predicates. This abstract mapping can then be used to publish the content contained in these bundles, enabling you to serialize the RDF into a number of different formats, such as RDFa, RDF/XML, or populate a SPARQL endpoint.

## [Altering an existing RDF mapping](/docs/7/api/rdf-mapping-api/altering-an-existing-rdf-mapping)

Because RDF mappings are saved to the database on installation, hook_rdf_mapping should only be used in modules that create new bundles.

## [Creating mappings for taxonomies](/docs/7/api/rdf-mapping-api/creating-mappings-for-taxonomies)

There are two ways to map taxonomy to RDF

## [Defining a new RDF mapping](/docs/7/api/rdf-mapping-api/defining-a-new-rdf-mapping)

This document is a work in progress and is rapidly changing.

## [RDF namespaces registry](/docs/7/api/rdf-mapping-api/rdf-namespaces-registry)

At the core of the RDF mappings defined in the RDF mapping API are CURIEs such as 'sioc:Post' which refer to the particular class or
