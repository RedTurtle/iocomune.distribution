# -*- coding: utf-8 -*-
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import iocomune.distribution


class IocomuneDistributionLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.app.dexterity

        self.loadZCML(package=plone.app.dexterity)
        import plone.restapi

        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=iocomune.distribution)

    def setUpPloneSite(self, portal):
        applyProfile(portal, "iocomune.distribution:default")


IOCOMUNE_DISTRIBUTION_FIXTURE = IocomuneDistributionLayer()


IOCOMUNE_DISTRIBUTION_INTEGRATION_TESTING = IntegrationTesting(
    bases=(IOCOMUNE_DISTRIBUTION_FIXTURE,),
    name="IocomuneDistributionLayer:IntegrationTesting",
)


IOCOMUNE_DISTRIBUTION_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(IOCOMUNE_DISTRIBUTION_FIXTURE,),
    name="IocomuneDistributionLayer:FunctionalTesting",
)


IOCOMUNE_DISTRIBUTION_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        IOCOMUNE_DISTRIBUTION_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name="IocomuneDistributionLayer:AcceptanceTesting",
)
