from tsadm.tests import TSAdmTestBase
from ..models import HostDB

class TSAdmHostTest(TSAdmTestBase):
    def setUp(self):
        super(TSAdmHostTest, self).setUp()
        host = HostDB(fqdn='fake.host.test')
        host.save()

    def test_HostView(self):
        resp = self.client.get(self.getURL('host:home', kwargs={'ID': 1}))
        self.assertEqual(resp.status_code, 200)
