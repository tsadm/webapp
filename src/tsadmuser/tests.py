from tsadm.tests import TSAdmTestBase

class TSAdmTest(TSAdmTestBase):
    def test_UserView(self):
        resp = self.client.get(self.getURL('user:home'))
        self.assertEqual(resp.status_code, 200)
