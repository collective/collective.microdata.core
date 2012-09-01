# -*- coding: utf-8 -*-

import unittest

from zope import interface
from zope.component import queryUtility

from collective.microdata.core.testing import MICRODATA_CORE_INTEGRATION_TESTING
from collective.microdata.core.interfaces import IMicrodataCoreLayer

class TestMicrodataSupport(unittest.TestCase):
    
    layer = MICRODATA_CORE_INTEGRATION_TESTING
    
    def markRequestWithLayer(self):
        # to be removed when p.a.testing will fix https://dev.plone.org/ticket/11673
        request = self.layer['request']
        interface.alsoProvides(request, IMicrodataCoreLayer)
    
    def setUp(self):
        self.markRequestWithLayer()
        portal = self.layer['portal']
        request = self.layer['request']
        portal.invokeFactory(type_name='News Item',
                             id='news',
                             title="The Lord of the Rings",
                             description="Boromir will die, sooner or later",
                             text="All begin in the Shrine...",
                             creator="J. R. R. Tolkien")
        request.set('ACTUAL_URL', 'http://nohost/plone/news')
        self.news = portal.news
    
    def test_basic_adapter_usage(self):
        self.assertFalse(False)