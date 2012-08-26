# -*- coding: utf8 -*-

from zope.interface import Interface

class ISchemaOrgMinimalBook(Interface):
    """
    See http://schema.org/Book
    
    This is only used for testing, so we don't put there ALL the vocabulary elements
    """

class NewsItemTestingMicrodataAdapter(object):
    implements(ISchemaOrgMinimalBook)
    
    def __init__(self, content):
        self.microdata_vocabulary = 'http://schema.org/Book'


