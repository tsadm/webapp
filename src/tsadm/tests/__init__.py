from __future__ import print_function

import sys
from django.core.urlresolvers import reverse
from django.test import TestCase
from django.contrib.auth.models import User

from tsadmuser import TSAdmUser
from tsadmuser.models import TSAdmUserDB
from tsadmsite.models import TSAdmSiteDB, TSAdmSiteEnvDB, TSAdmSiteEnvACL
from tsadmhost.models import TSAdmHostDB

print('Python', sys.version, file=sys.stderr)

class TSAdmTestBase(TestCase):

    def setUp(self):
        self.django_user = User.objects.create_user(username='tester')
        self.client.force_login(self.django_user)

        self.user = TSAdmUser()
        self.user.load(self.django_user)

        s0 = TSAdmSiteDB(name='s0')
        s0.save()
        s1 = TSAdmSiteDB(name='s1')
        s1.save()
        s2 = TSAdmSiteDB(name='s2')
        s2.save()

        h0 = TSAdmHostDB(fqdn='h0.fakehost')
        h0.save()
        h1 = TSAdmHostDB(fqdn='h1.fakehost')
        h1.save()

        s0dev = TSAdmSiteEnvDB(site=s0, name='dev', host=h0)
        s0dev.save()
        s0test = TSAdmSiteEnvDB(site=s0, name='test', host=h1)
        s0test.save()

        s1test = TSAdmSiteEnvDB(site=s1, name='test', host=h1)
        s1test.save()

        acl0 = TSAdmSiteEnvACL(siteenv=s0dev, user=self.user._db)
        acl0.save()
        acl1 = TSAdmSiteEnvACL(siteenv=s1test, user=self.user._db)
        acl1.save()

    def getURL(self, urlTag, kwargs=None):
        return reverse(urlTag, kwargs=kwargs)
