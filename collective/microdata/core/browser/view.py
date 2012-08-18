# -*- coding: utf8 -*-

from zope.component import queryAdapter, getMultiAdapter
from zope.component.interfaces import ComponentLookupError

from Products.Five.browser import BrowserView
from plone.memoize import view

from collective.microdata.core.interfaces import ISchemaOrgThing

class ListingView(BrowserView):

    @view.memoize
    def get_microdata(self, brain):
        # look for a type-specific adapter, if any
        adapter = queryAdapter(brain, interface=ISchemaOrgThing,
                               name=brain.microdata_itemtype)
        if not adapter:
            # fallback to basic Thing adapter
            adapter = queryAdapter(brain, interface=ISchemaOrgThing,
                                   name=u'')            
        return adapter


    def render_item(self, item):
        microdata = self.get_microdata(item)
        try:
            view = getMultiAdapter ((self.context, self.request),
                                    name='%s folder_listing_item' % microdata.microdata_vocabulary)
        except ComponentLookupError:
            view = getMultiAdapter ((self.context, self.request),
                                    name='folder_listing_item')            
        return view(item, microdata)


class BaseItemListingView(BrowserView):
    """Base class for listing a single item"""
    
    def __init__(self, context, request):
        self.context = context
        self.request = request
        self.item = None
    
    def __call__(self, item, microdata, *args, **kwargs):
        self.item = item
        self.microdata = microdata
        return self.index()
