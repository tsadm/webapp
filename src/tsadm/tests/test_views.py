from . import TSAdmTestBase

class TSAdmViewsTest(TSAdmTestBase):

    def test_HomeView(self):
        resp = self.client.get(self.getURL('home'))
        self.assertEqual(resp.status_code, 200)
