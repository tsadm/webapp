from tsadm.tests import TSAdmTestBase

class TSAdmUserTest(TSAdmTestBase):

    def test_UserView(self):
        resp = self.client.get(self.getURL('user:home'))
        self.assertContains(resp, 'TEST:user.name:tester', count=1, status_code=200)
