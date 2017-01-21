---
title: "TempoIQ Documentation Site"
excerpt: "Developer docs for a cloud-based data analytics service"
date_string: "2015"
header:
  teaser: projects/tempoiq-docs-th.png
---

TempoIQ was a sensor data analytics startup where I worked 2013-2016. In 2015 
I led the company's Developer Experience initiative, a large portion of which
involved reorganizing and rewriting the product's documentation.

As a technical product where our primary users were developers, the documentation
included guides explaining the product's major concepts and features, as well as 
reference material for the API and five client libraries.

{% include _image.html img="projects/tempoiq-docs.png" lightbox=false %}

We used the [Sphinx](http://www.sphinx-doc.org/) documentation generation tool.
I developed an extension for displaying code examples for the various
libraries and interfaces. Language-specific examples were maintained
with the libraries themselves, with example code being automatically tested
using our existing Continuous Integration tools. This prevented our example code
from falling out-of-date or being victim to copy-paste errors--common problems
when authoring example code snippets.

{% include _image.html img="projects/tempoiq-docs2.png" lightbox=false %}

