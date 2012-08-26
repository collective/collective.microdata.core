.. contents:: **Table of contents**

Introduction
============

This is the core product for adding `microdata`__ support to Plone.

__ http://en.wikipedia.org/wiki/Microdata_%28HTML%29

How to use
==========

This package simply provide raw support, not really useful on his own. It is intended to be
extender by 3rd part projects that want to microdata support for Plone.

One example: `collective.microdata.event`__.

__ http://pypi.python.org/pypi/collective.microdata.event

The microdata vocabulary
------------------------

Every content type that wanna provide microdata information needs to provide an adapter for the
``IMicrodataVocabulary`` interface. This interface is limited to a single information: n **URI
to a microdata vocabulary**.

The schema.org implementation
-----------------------------

The most promising implementation of microdata is the one defined at `schema.org`__. This package
is providing the most-generic type defined there: the `Thing`__ type.

__ http://schema.org/
__ http://schema.org/Thing

This is done providing an adapter for ``ISchemaOrgThing`` interface (that extends ``IMicrodataVocabulary``).

How to extend
=============

Your product must provide his own implementation for the ``IMicrodataVocabulary``::

    <adapter for="your.products.content.IType"
             provides="collective.microdata.core.interfaces.IMicrodataVocabulary"
             factory=".adapter.YourTypeMicrodataProvider" />

Then you need to provide the adapter::

    class YourTypeMicrodataProvider(object):
    implements(IYourMicrodataVocabulary)
    
    def __init__(self, content):
        self.microdata_vocabulary = 'http://your.microdata.uri'
        self.microdata_data1 = ... 

The your content type view must obtain the microdata adapter you defined, and put the right HTML
code in the view.

Support for folder content listing views
========================================

If you want to provide microdata information also in folder content views (so displaying multiple
microdata objects in a single page), you could like to install `collective.microdata.contentlisting`__.

__ http://pypi.python.org/pypi/collective.microdata.contentlisting

See it's documentation for further information on how to use this in you product.

Testing your microdata
======================

This product also include a JavaScript tester microdata tool called `Microdata Tool`__
(a modified ones, just to fix some stupid Sunburst CSS styles).

__ http://krofdrakula.github.com/microdata-tool/

To enable it while testing your site, just run the *testing* Generic Setup profile from
your *site_setup* tool. 

This will enable the JavaScript tester in every page.

**Hint**: duration checker seems not working properly.

Final notes
===========

Providing microdata doesn't ensure that search engines will use it.
