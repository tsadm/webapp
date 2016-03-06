from . import TSAdmTestBase

class TSAdmTest(TSAdmTestBase):

    def testLogger_SetLevel(self):
        from ..log import TSAdmLogger
        logger = TSAdmLogger(__name__)
        logger._setLevel('DEBUG')
        logger._setLevel('__INVALID__')
        logger._setLevel(None)

    def test_DispatchException(self):
        from ..views import TSAdmView
        view = TSAdmView.as_view()
        resp = view(None)
        self.assertEqual(resp.status_code, 500)

    def test_HomeView(self):
        resp = self.client.get(self.getURL('home'))
        self.assertEqual(resp.status_code, 200)

    def test_HttpOptions(self):
        resp = self.client.options(self.getURL('home'))
        self.assertEqual(resp.get('Allow'), 'GET, HEAD, OPTIONS')

    def test_HttpCharset(self):
        resp = self.client.head(self.getURL('home'))
        self.assertEqual(resp.charset, 'utf-8')
