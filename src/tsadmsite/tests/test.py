from tsadm.tests import TSAdmTestBase
from ..models import SiteDB, SiteEnvDB, SiteEnvACL
from tsadmhost.models import HostDB


class TSAdmSiteTest(TSAdmTestBase):
    site = None

    def setUp(self):
        super(TSAdmSiteTest, self).setUp()
        self.site = SiteDB.objects.get(name='s0')


    def test_Site(self):
        self.assertEqual(self.site.id, 1)
        resp = self.client.get(
            self.getURL('site:home', kwargs={'name': 'INVALID'}),
        )
        self.assertEqual(resp.status_code, 400)


    def test_HomeView(self):
        resp = self.client.get(self.getURL('home'))
        self.assertContains(resp, 'TEST:site:s0', count=1, status_code=200)
        self.assertContains(resp, 'TEST:site:s1', count=1, status_code=200)
        self.assertNotContains(resp, 'TEST:site:s2', status_code=200)


    def test_SiteView(self):
        resp = self.client.get(self.getURL('site:home', kwargs={'name': 's0'}))
        self.assertContains(resp, 'TEST:site.env:dev', count=1, status_code=200)
        self.assertContains(resp, 'TEST:site.env:test', count=1, status_code=200)
        resp = self.client.get(self.getURL('site:home', kwargs={'name': 's1'}))
        self.assertContains(resp, 'TEST:site.env:test', count=1, status_code=200)
        self.assertNotContains(resp, 'TEST:site.env:prod', status_code=200)


    def test_SiteViewNoEnvs(self):
        resp = self.client.get(
            self.getURL('site:home', kwargs={'name': 's2'}),
        )
        self.assertEqual(resp.status_code, 400)


    def test_SiteEnvView(self):
        resp = self.client.get(self.getURL('site:env', kwargs={'site': 's0', 'env': 'dev'}))
        self.assertContains(resp, 'TEST:site.name:s0', count=1, status_code=200)
        self.assertContains(resp, 'TEST:site.env:dev', count=1, status_code=200)


    def test_SiteEnvViewNoAccess(self):
        resp = self.client.get(
            self.getURL('site:env', kwargs={'site': 's1', 'env': 'prod'}),
        )
        self.assertEqual(resp.status_code, 400)
