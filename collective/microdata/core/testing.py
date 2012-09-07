# -*- coding: utf-8 -*-

import zope.component
from zope.configuration import xmlconfig

from Products.ZCatalog.interfaces import ICatalogBrain

from plone.testing import z2

from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting
from plone.app.testing import applyProfile
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID

from Products.ATContentTypes.interfaces import IATNewsItem

from collective.microdata.core.tests.base import NewsItemTestingMicrodataAdapter
from collective.microdata.core.tests.base import NewsItemTestingMicrodataBrainAdapter
from collective.microdata.core.interfaces import IMicrodataVocabulary

class MicrodataCore(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE, )

    def setUpZope(self, app, configurationContext):
        # Load ZCML for this package
        import collective.microdata.core
        xmlconfig.file('configure.zcml',
                       collective.microdata.core,
                       context=configurationContext)
        z2.installProduct(app, 'collective.microdata.core')
        
        zope.component.provideAdapter(
            NewsItemTestingMicrodataAdapter,
            (IATNewsItem,),
            provides=IMicrodataVocabulary
        )

        zope.component.provideAdapter(
            NewsItemTestingMicrodataBrainAdapter,
            (ICatalogBrain,),
            provides=IMicrodataVocabulary,
            name=u'http://schema.org/Book'
        )


    def setUpPloneSite(self, portal):
        applyProfile(portal, 'collective.microdata.core:default')
        #quickInstallProduct(portal, 'collective.microdata.core')
        setRoles(portal, TEST_USER_ID, ['Member', 'Manager'])


MICRODATA_CORE_FIXTURE = MicrodataCore()
MICRODATA_CORE_INTEGRATION_TESTING = \
    IntegrationTesting(bases=(MICRODATA_CORE_FIXTURE, ),
                       name="MicrodataCore:Integration")
MICRODATA_CORE_FUNCTIONAL_TESTING = \
    FunctionalTesting(bases=(MICRODATA_CORE_FIXTURE, ),
                       name="MicrodataCore:Functional")

