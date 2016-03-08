from . import TSAdmTestBase

class TSAdmViewsTest(TSAdmTestBase):

    def test_HomeView(self):
        resp = self.client.get(self.getURL('home'))
        self.assertContains(resp, 'TEST:site:s0', count=1, status_code=200)
        self.assertContains(resp, 'TEST:site:s1', count=1, status_code=200)
        self.assertNotContains(resp, 'TEST:site:s2', status_code=200)
