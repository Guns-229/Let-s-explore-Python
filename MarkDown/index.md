
![](images/jupyter_logo.png)

![](images/cy3logoOrange.svg)
  

# Welcome to cyREST Examples for Python Users!

![](http://cl.ly/aPle/jupyter-sample1.png)


## What is Cytoscape?
[Cytoscape](http://www.cytoscape.org/) is an open source software platform for visualizing complex networks and integrating them with any type of attributes. A lot of [Apps](http://apps.cytoscape.org/) are available for various kinds of problem domains, including bioinformatics, social network analysis, and semantic web.

## Introduction to cyREST
[cyREST](http://apps.cytoscape.org/apps/cyrest) is a Cytoscape App providing access to Cytoscape core data objects including networks, tables, and Styles via RESTful API, which is totally platform/language independent.  This means you can write your own workflows using Cytoscape in programming language of your choice.

### Target Audience

* Computational Biologists
* Data Scientists
* And all people who use graph data!

We assume you have basic knowlege of Cytoscape and Python.  Some of the examples require third party libraries, and you need to know how to setup your own Python environment to satisfy the dependencies.

### Docker Containers for Python Examples
We have a Docker container with standard libraries for network analysis:

* [Docker Image for Basic Network Analysis](https://registry.hub.docker.com/u/idekerlab/vizbi-2015/)

And of course, you can use your own environment if you want.

# Table of Contents

## Warning: you need Cytoscape 3.2.1 and [cyREST 0.9.17](http://apps.cytoscape.org/apps/cyrest) and newer to run these examples

----

## New!  Examples Using py2cytoscape

Although cyREST provides a set of language-agnostic API, it requires some _boilarplate code_ to access raw REST API.  To avoid lots of duplicate code, we've released [py2cytoscape](https://github.com/idekerlab/py2cytoscape), a Python wrapper for cyREST.  If you use cyREST with py2cytoscape, you can signisicantly reduce lines of code in your workflow.  Please visit the link below to see how _natural_ the API is for Python users.

* [py2cytoscape project web site](https://github.com/idekerlab/py2cytoscape)
* [Sample Notebook using py2cytoscape](http://nbviewer.ipython.org/github/idekerlab/py2cytoscape/blob/develop/examples/New_wrapper_api_sample.ipynb)


----

## Examples Using Raw cyREST API

----

### Note: You need to run IPython Notebook server to view the actual results.  GitHub may not render notebooks linked from the following list.

 * [How to run these sample notebooks](https://github.com/idekerlab/cy-rest-python/blob/develop/README.md)

----

### Basic Exercises

* [Introduction to cyREST API](basic/CytoscapeREST_Basic1.ipynb)
* [NetworkX and Cytoscape](basic/CytoscapeREST_Basic2.ipynb)
* [Visual Style as a Python Object](basic/CytoscapeREST_Basic3.ipynb)
* [Import KEGG pathways from web service](basic/CytoscapeREST_Basic4_KEGG_API.ipynb)


* [Embed your networks as interactive Cytoscape.js widgets](basic/CytoscapeJS_visualization.ipynb)


* [RECOMB/Cytoscape 2014 Demo](basic/RECOMB2014_demo-final.ipynb)


### [cyREST Cookbook](basic/CyREST_Cookbook.ipynb)


### Advanced Exercises

* [Visualizing differentially expressed transcritome profile](advanced/CytoscapeREST_KEGG_f1000.ipynb)
* [Visualizing time series metabolome profile](advanced/CytoscapeREST_KEGG_time_series.ipynb)
* [Mapping DRUGBANK drug targets to KEGG pathway](advanced/integratingDrugbank.ipynb)
* [Mapping Path2Models whole genome metabolism model to KEGG pathway](advanced/path2models.ipynb)

# More Information


## Workshop Materials
* [VIZBI 2015 Tutorial: Cytoscape, IPython, Docker and Reproducible Data Visualization Workflow](https://github.com/idekerlab/vizbi-2015) - 3/24/2015
    * [Lecture slides](http://www.slideshare.net/keiono/vizbi-2015-tutorial-cytoscape-ipython-docker-and-reproducible-network-data-visualization-workflows)


* [SDCSB Cytoscape Advanced Tutorial](https://github.com/idekerlab/sdcsb-advanced-tutorial/wiki) - 4/17/2015
    * [Lecture slides](http://www.slideshare.net/keiono/sdcsb-cytoscape-advanced-tutorial)


## Links to cyREST Resources

* [User Guide for cyREST](https://github.com/idekerlab/cyREST/wiki)
* [cyREST Page at Cytoscape App Store](http://apps.cytoscape.org/apps/cyrest)
* [Source Code](https://github.com/idekerlab/cyREST)


## For R Users
[R example scripts are available here](https://github.com/idekerlab/cy-rest-R).


----

Be sure to follow us on Twitter [@cytoscape](https://twitter.com/cytoscape)! When you tweet about your Cytoscape workflows, please use _#cytoscape_ tag.

## Contact
For questions, please join the [cytoscape-discuss mailing list](https://groups.google.com/forum/#!forum/cytoscape-discuss)

Or directly to me (kono at ucsd dot edu)

<script>
  (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
  (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
  m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
  })(window,document,'script','//www.google-analytics.com/analytics.js','ga');

  ga('create', 'UA-27761864-9', 'auto');
  ga('send', 'pageview');
</script>
