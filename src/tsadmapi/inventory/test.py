from tsadm.tests import TSAdmTestBase


_HOSTGROUPS = '''{
    "_meta": {
        "hostvars": {
            "fake0.tsadm.test": ["<SiteEnvDB: s0.dev>"],
            "fake1.tsadm.test": ["<SiteEnvDB: s0.test>",
                "<SiteEnvDB: s1.test>"
            ]
        }
    },
    "all": {
        "hosts": ["fake0.tsadm.test", "fake1.tsadm.test"],
        "vars": {}
    }
}'''


class InventoryTest(TSAdmTestBase):

    def test_HostGroupsView(self):
        resp = self.client.get(self.getURL('api:inventory:hostgroups'))
        self.assertEqual(resp.status_code, 200)
        self.assertJSONEqual(resp.content.decode(), _HOSTGROUPS)
