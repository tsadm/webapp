from tsadm.tests import TSAdmTestBase
from ..models import TSAdmSiteDB

class TSAdmSiteTest(TSAdmTestBase):
    def setUp(self):
        super(TSAdmSiteTest, self).setUp()
        site = TSAdmSiteDB(name='fakesite')
        site.save()

    def test_SiteView(self):
        resp = self.client.get(self.getURL('site:home', kwargs={'name': 'fakesite'}))
        self.assertEqual(resp.status_code, 200)
