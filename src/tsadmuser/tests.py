from django.core.urlresolvers import reverse
from django.test import TestCase
from django.contrib.auth.models import User

class TSAdmTest(TestCase):
    def setUp(self):
        user = User.objects.create_user(username='tester')
        self.client.force_login(user)

    def test_UserView(self):
        resp = self.client.get(reverse('user:home'))
        self.assertEqual(resp.status_code, 200)
