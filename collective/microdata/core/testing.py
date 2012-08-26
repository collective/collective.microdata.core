# -*- coding: utf-8 -*-

import zope.component

from zope.configuration import xmlconfig

from plone.testing import z2

from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting
from plone.app.testing import applyProfile
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID

from collective.microdata.core.tests.testingadapter import NewsItemTestingMicrodataAdapter

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
            testingadapter.NewsItemTestingMicrodataAdapter,
            (Products.ATContentTypes.interfaces.IATNewsItem),
            provides=collective.microdata.core.interfaces.IMicrodataVocabulary
        )

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'collective.microdata.core:default')
        #quickInstallProduct(portal, 'collective.analyticspanel')
        setRoles(portal, TEST_USER_ID, ['Member', 'Manager'])


MICRODATA_CORE_FIXTURE = MicrodataCore()
MICRODATA_CORE_INTEGRATION_TESTING = \
    IntegrationTesting(bases=(MICRODATA_CORE_FIXTURE, ),
                       name="MicrodataCore:Integration")
MICRODATA_CORE_FUNCTIONAL_TESTING = \
    FunctionalTesting(bases=(MICRODATA_CORE_FIXTURE, ),
                       name="MicrodataCore:Functional")

