.. contents:: **Table of contents**

Introduction
============

This is the core product for adding `microdata`__ support to Plone.

__ http://en.wikipedia.org/wiki/Microdata_%28HTML%29

How to use
==========

This package simply provide raw support, not really useful on his own. It is intended to be
extender by 3rd part projects that want to microdata support for Plone.

One complete implementation: `collective.microdata.event`__.

__ http://pypi.python.org/pypi/collective.microdata.event

The microdata vocabulary
------------------------

Every content type that wanna provide microdata information needs to provide an adapter for the
``IMicrodataVocabulary`` interface. This interface is limited to a single information: an **URI
to a microdata vocabulary**.

The schema.org implementation
-----------------------------

As the most promising implementation of microdata is the one defined at `schema.org`__, this package
is supporting it. This is done providing the most-generic type defined: the `Thing`__ type.

This is done for all Plone content types and catalog objects (for catalog: a new catalog metadata
``microdata_itemtype`` will be added to your catalog, saving there the most specific vocabulary
URL found).

__ http://schema.org/
__ http://schema.org/Thing

This is done providing adapters for ``ISchemaOrgThing`` interface (that extends ``IMicrodataVocabulary``).

How to extend
=============

From contents
-------------

To get microdata information from a content types, your product must provide his own implementation for
the ``IMicrodataVocabulary``::

    <adapter for="your.products.content.IType"
             provides="collective.microdata.core.interfaces.IMicrodataVocabulary"
             factory=".adapter.YourTypeMicrodataProvider" />

Then you need to provide the adapter::

    class YourTypeMicrodataProvider(object):
    implements(IYourMicrodataVocabulary)
    
    def __init__(self, content):
        self.microdata_vocabulary = 'http://your.microdata.uri'
        # now get data from the content
        self.microdata_data1 = ... 

Then your content's view must obtain the microdata adapter you defined, and put the right HTML
code in the view.

From catalog
------------


XXXX catalog brain


There's an adapter for getting raw ``Thing`` microdata from a catalog brain from all Plone content
types, but your 3rd party content type must also provide a more specific ones::

    <adapter for="Products.ZCatalog.interfaces.ICatalogBrain"
             provides="collective.microdata.core.interfaces.IMicrodataVocabulary"
             factory=".adapter.YourTypeMicrodataBrainProvider"
             name="http://your.microdata.uri" />

Then you need to provide the adapter::

    class YourTypeMicrodataBrainProvider(object):
    implements(IYourMicrodataVocabulary)
    
    def __init__(self, brain):
        self.microdata_vocabulary = 'http://your.microdata.uri'
        # now get data from the catalog
        self.microdata_data1 = ... 

If your adapter is more specific than the default "Thing" ones, it will replace that one in the catalog.

Support for folder content listing views
========================================

If you want to provide microdata information also in folder content views (so displaying multiple
microdata objects in a single page), you could like to install `collective.microdata.contentlisting`__.

__ http://pypi.python.org/pypi/collective.microdata.contentlisting

See it's documentation for further information on how to use this in you product.

Testing your microdata
======================

This product also include a JavaScript tester microdata tool called `Microdata Tool`__
(a modified ones, just to fix some crappy Sunburst CSS rules).

__ http://krofdrakula.github.com/microdata-tool/

To enable it while testing your site, just run the *testing* Generic Setup profile from
your *site_setup* tool. 

This will enable the JavaScript tester in every page.

**Hint**: duration checker seems not working properly.

Final notes
===========

Providing microdata doesn't ensure that search engines will use it.
