# -*- coding: utf-8 -*-

import unittest

from zope import interface
from zope.component import getAdapter

from collective.microdata.core.testing import MICRODATA_CORE_INTEGRATION_TESTING
from collective.microdata.core.interfaces import IMicrodataCoreLayer
from collective.microdata.core.interfaces import IMicrodataVocabulary

from collective.microdata.core.tests.base import ISchemaOrgMinimalBook

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
        microdata = IMicrodataVocabulary(self.news)
        self.assertTrue(ISchemaOrgMinimalBook.providedBy(microdata))

    def test_microdata(self):
        news = self.news
        microdata = IMicrodataVocabulary(news)
        self.assertEqual(microdata.microdata_vocabulary, u'http://schema.org/Book')
        self.assertEqual(microdata.genre, u'Fantasy')
        self.assertEqual(microdata.name, news.Title())
        self.assertEqual(microdata.description, news.Description())
        self.assertEqual(microdata.text, news.getText())
        self.assertEqual(microdata.creator, news.Creator())

    def test_catalog_implementation(self):
        portal = self.layer['portal']
        brain = portal.portal_catalog(portal_type='News Item')[0]
        self.assertEqual(brain.microdata_itemtype, 'http://schema.org/Book')
        microdata = getAdapter(brain, interface=IMicrodataVocabulary, name=u'http://schema.org/Book')
        self.assertEqual(microdata.microdata_vocabulary, u'http://schema.org/Book')
        self.assertEqual(microdata.genre, u'Fantasy')
        self.assertEqual(microdata.name, brain.Title)
        self.assertEqual(microdata.description, brain.Description)
        # Notw below: we will be forced to get the real object
        self.assertEqual(microdata.text, brain.getObject().getText())
        self.assertEqual(microdata.creator, brain.Creator)
        
