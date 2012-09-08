# -*- coding: utf8 -*-

from zope.interface import implements
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


class ThingMicrodataBrainProvider(object):
    implements(ISchemaOrgThing)
    
    def __init__(self, brain):
        self.brain = brain
        self.microdata_vocabulary = 'http://schema.org/Thing'
        self.additionalType = None
        self.description = brain.Description
        self.name = brain.Title
        self.url = brain.getURL()
        