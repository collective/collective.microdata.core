# -*- coding: utf8 -*-

from zope.interface import implements

from collective.microdata.core.interfaces import ISchemaOrgThing
from collective.microdata.core.adapter import ThingMicrodataProvider
from collective.microdata.core.adapter import ThingMicrodataBrainProvider

class ISchemaOrgMinimalBook(ISchemaOrgThing):
    """
    See http://schema.org/Book
    
    This is only used for testing, so we don't put there ALL the vocabulary elements
    """


class NewsItemTestingMicrodataAdapter(ThingMicrodataProvider):
    implements(ISchemaOrgMinimalBook)
    
    def __init__(self, content):
        super(NewsItemTestingMicrodataAdapter, self).__init__(content)
        self.microdata_vocabulary = 'http://schema.org/Book'
        self.genre = u'Fantasy'
        self.text = content.getText()
        self.creator = content.Creator()
        

class NewsItemTestingMicrodataBrainAdapter(ThingMicrodataBrainProvider):
    implements(ISchemaOrgMinimalBook)
    
    def __init__(self, brain):
        super(NewsItemTestingMicrodataBrainAdapter, self).__init__(brain)
        self.microdata_vocabulary = 'http://schema.org/Book'
        self.genre = u'Fantasy'
        self.text = brain.getObject().getText()
        self.creator = brain.Creator
