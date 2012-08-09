from zope.interface import Interface
from zope import schema

class IMicrodataCoreLayer(Interface):
    """Marker interface for the collective.microdata.event layer"""


class IMicrodataVocabulary(Interface):
    
    microdata_vocabulary = schema.URI(title=u"Microdata type",
                                      description=u"An URI that identify "
                                                  u"univocally the microdata type",
                                      required=True)


class ISchemaOrgThing(IMicrodataVocabulary):
    """See http://schema.org/Thing"""
        
    additionalType = schema.URI(title=u"Additional type",
                                description=u"An additional type for the item, "
                                            u"typically used for adding more "
                                            u"specific types from external "
                                            u"vocabularies in microdata syntax.",
                                required=False)

    description = schema.Text(title=u"Description",
                              description=u"A short description of the item.",
                              required=False)

    image = schema.URI(title=u"Image",
                       description=u"URL of an image of the item.",
                       required=False)

    name = schema.TextLine(title=u"Name",
                           description=u"The name of the item.",
                           required=True)

    url = schema.URI(title=u"URL",
                     description=u"URL of the item.",
                     required=True)


