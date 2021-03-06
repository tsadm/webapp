from . import TSAdmTestBase

class TSAdmTest(TSAdmTestBase):

    def test_DispatchException(self):
        from ..views import TSAdmView
        view = TSAdmView.as_view()
        resp = view(None)
        self.assertEqual(resp.status_code, 500)

    def test_HttpOptions(self):
        resp = self.client.options(self.getURL('home'))
        self.assertEqual(resp.get('Allow'), 'GET, HEAD, OPTIONS')

    def test_HttpCharset(self):
        resp = self.client.head(self.getURL('home'))
        self.assertEqual(resp.charset, 'utf-8')

    def test_InfoView(self):
        resp = self.client.get(self.getURL('info'))
        self.assertEqual(resp.status_code, 200)
