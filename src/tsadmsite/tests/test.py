from tsadm.tests import TSAdmTestBase
from ..models import SiteDB, SiteEnvDB, SiteEnvACL
from tsadmhost.models import HostDB


class TSAdmSiteTest(TSAdmTestBase):
    site = None

    def setUp(self):
        super(TSAdmSiteTest, self).setUp()
        s0 = SiteDB(name='s0')
        s0.save()
        s1 = SiteDB(name='s1')
        s1.save()
        s2 = SiteDB(name='s2')
        s2.save()

        h0 = HostDB(fqdn='h0.fakehost')
        h0.save()
        h1 = HostDB(fqdn='h1.fakehost')
        h1.save()

        s0dev = SiteEnvDB(site=s0, name='dev', host=h0)
        s0dev.save()
        s0test = SiteEnvDB(site=s0, name='test', host=h1)
        s0test.save()

        s1test = SiteEnvDB(site=s1, name='test', host=h1)
        s1test.save()

        acl0 = SiteEnvACL(siteenv=s0dev, user=self.user)
        acl0.save()
        acl1 = SiteEnvACL(siteenv=s1test, user=self.user)
        acl1.save()

        self.site = s0dev


    def test_Site(self):
        self.assertEqual(self.site.id, 1)


    def test_HomeView(self):
        resp = self.client.get(self.getURL('home'))
        self.assertContains(resp, 'TEST:site:s0', count=1, status_code=200)
        self.assertContains(resp, 'TEST:site:s1', count=1, status_code=200)
        self.assertNotContains(resp, 'TEST:site:s2', status_code=200)


    def test_SiteView(self):
        resp = self.client.get(self.getURL('site:home', kwargs={'name': 's0'}))
        self.assertContains(resp, 'TEST:site.env:dev', count=1, status_code=200)
        self.assertNotContains(resp, 'TEST:site.env:test', status_code=200)
        resp = self.client.get(self.getURL('site:home', kwargs={'name': 's1'}))
        self.assertContains(resp, 'TEST:site.env:test', count=1, status_code=200)


    def test_SiteEnvView(self):
        resp = self.client.get(self.getURL('site:env', kwargs={'site': 's0', 'env': 'dev'}))
        self.assertContains(resp, 'TEST:site.name:s0', count=1, status_code=200)
        self.assertContains(resp, 'TEST:site.env:dev', count=1, status_code=200)
