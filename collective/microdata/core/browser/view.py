# -*- coding: utf8 -*-

from zope.component import queryAdapter

from Products.Five.browser import BrowserView
from collective.microdata.core.interfaces import ISchemaOrgThing

class ListingView(BrowserView):

    def get_microdata(self, brain):
        portal_type = brain.portal_type
        # look for a type specific adapter, if any
        adapter = queryAdapter(brain, interface=ISchemaOrgThing,
                               name=portal_type)
        if not adapter:
            # fallback to basic Thing adapter
            adapter = queryAdapter(brain, interface=ISchemaOrgThing,
                                   name=u'')            
        return adapter
