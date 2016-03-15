from tsadm.tests import TSAdmTestBase
from ..models import TSAdmSiteDB

class TSAdmSiteTest(TSAdmTestBase):
    def setUp(self):
        super(TSAdmSiteTest, self).setUp()

    def test_SiteView(self):
        resp = self.client.get(self.getURL('site:home', kwargs={'name': 's0'}))
        self.assertContains(resp, 'TEST:site.env:dev', count=1, status_code=200)
        self.assertNotContains(resp, 'TEST:site.env:test', status_code=200)
        resp = self.client.get(self.getURL('site:home', kwargs={'name': 's1'}))
        self.assertContains(resp, 'TEST:site.env:test', count=1, status_code=200)
