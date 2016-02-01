from django.core.urlresolvers import reverse
from django.test import TestCase

class TSAdmTest(TestCase):
    def test_HomeView(self):
        resp = self.client.get(reverse('home'))
        self.assertRedirects(resp, '{}?next=/'.format(reverse('login')))
