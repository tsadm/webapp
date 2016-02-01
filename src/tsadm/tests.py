from django.core.urlresolvers import reverse
from django.test import TestCase
from django.contrib.auth.models import User

class TSAdmAnonTest(TestCase):
    def test_HomeView(self):
        resp = self.client.get(reverse('home'))
        self.assertRedirects(resp, '{}?next=/'.format(reverse('login')))

class TSAdmTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='tester')
        self.client.force_login(self.user)

    def test_HomeView(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)

    def test_HttpOptions(self):
        resp = self.client.options(reverse('home'))
        self.assertEqual(resp.get('Allow'), 'GET, HEAD, OPTIONS')

    def test_HttpCharset(self):
        resp = self.client.head(reverse('home'))
        self.assertEqual(resp.charset, 'utf-8')
