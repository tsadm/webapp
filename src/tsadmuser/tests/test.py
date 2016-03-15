from tsadm.tests import TSAdmTestBase

class TSAdmUserTest(TSAdmTestBase):
    def test_UserView(self):
        resp = self.client.get(self.getURL('user:home'))
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, 'TEST:user.name:tester')
