# -*- coding: utf8 -*-

from zope.interface import Interface, implements
from collective.microdata.core.interfaces import ISchemaOrgThing

class ThingMicrodataProvider(object):
    implements(ISchemaOrgThing)
    
    def __init__(self, content):
        self.microdata_vocabulary = 'http://schema.org/Thing'
        self.content = content
        self.additionalType = None
        self.description = content.Description()
        self.name = content.Title()
        self.url = content.absolute_url()
        if content.getField('image'):
            self.image = content.absolute_url() + '/image'