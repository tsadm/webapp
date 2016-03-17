from django.core.urlresolvers import reverse
from django.test import TestCase
from django.contrib.auth.models import User

class TSAdmAnonTest(TestCase):

    def test_Logger(self):
        from ..log import TSAdmLogger
        logger = TSAdmLogger(__name__)
        logger._setLevel('DEBUG')
        logger._setLevel('__INVALID__')
        logger._setLevel(None)

    def test_LoginRedirect(self):
        resp = self.client.get(reverse('home'))
        self.assertRedirects(resp, '{}?next=/'.format(reverse('login')))

    def test_LoginLogout(self):
        credentials = dict(username='tester', password='izkK9aAfuppnmrMi')
        user = User.objects.create_user(**credentials)
        # login
        resp = self.client.post(reverse('login'), credentials)
        self.assertRedirects(resp, reverse('home'))
        # logout
        resp = self.client.get(reverse('logout'))
        self.assertRedirects(resp, reverse('login'))
