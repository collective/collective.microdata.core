# -*- coding: utf-8 -*-

import unittest

from zope import interface
from zope.component import queryUtility

from collective.microdata.core.testing import MICRODATA_CORE_INTEGRATION_TESTING

class TestMicrodataSupport(unittest.TestCase):
    
    layer = MICRODATA_CORE_INTEGRATION_TESTING
    
    