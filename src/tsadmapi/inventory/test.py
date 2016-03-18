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

_HOSTINFO = '''{
    "fake0.tsadm.test": ["<SiteEnvDB: s0.dev>"]
}'''


class InventoryTest(TSAdmTestBase):

    def test_HostGroupsView(self):
        resp = self.client.get(self.getURL('api:inventory:hostgroups'))
        self.assertEqual(resp.status_code, 200)
        self.assertJSONEqual(resp.content.decode(), _HOSTGROUPS)

    def test_HostInfoView(self):
        resp = self.client.get(self.getURL(
            'api:inventory:hostinfo',
            kwargs={'fqdn': 'fake0.tsadm.test'},
        ))
        self.assertEqual(resp.status_code, 200)
        self.assertJSONEqual(resp.content.decode(), _HOSTINFO)
