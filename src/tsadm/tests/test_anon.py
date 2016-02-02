from django.core.urlresolvers import reverse
from django.test import TestCase

class TSAdmAnonTest(TestCase):
    def test_LoginRedirect(self):
        resp = self.client.get(reverse('home'))
        self.assertRedirects(resp, '{}?next=/'.format(reverse('login')))
