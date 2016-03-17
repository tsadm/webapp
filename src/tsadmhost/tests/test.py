from tsadm.tests import TSAdmTestBase
from ..models import HostDB

class TSAdmHostTest(TSAdmTestBase):

    def setUp(self):
        super(TSAdmHostTest, self).setUp()

    def test_HostView(self):
        resp = self.client.get(self.getURL('host:home', kwargs={'ID': 1}))
        self.assertContains(resp, 'TEST:host.fqdn:fake0.tsadm.test', status_code=200)
