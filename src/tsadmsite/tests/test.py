from tsadm.tests import TSAdmTestBase

class TSAdmTest(TSAdmTestBase):
    def test_SiteView(self):
        resp = self.client.get(self.getURL('site:home', kwargs={'name': 'fakesite'}))
        self.assertEqual(resp.status_code, 200)
