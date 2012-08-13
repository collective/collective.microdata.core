# -*- coding: utf8 -*-

from plone.indexer.decorator import indexer
from Products.Archetypes.interfaces.base import IBaseContent
from collective.microdata.core.interfaces import IMicrodataVocabulary

@indexer(IBaseContent)
def microdata_itemtype(object, **kw):
    adapter = IMicrodataVocabulary(object)
    return adapter.microdata_vocabulary
