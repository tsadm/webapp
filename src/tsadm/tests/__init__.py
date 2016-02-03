from django.core.urlresolvers import reverse
from django.test import TestCase
from django.contrib.auth.models import User

class TSAdmTestBase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='tester')
        self.client.force_login(self.user)

    def getURL(self, urlTag, kwargs=None):
        return reverse(urlTag, kwargs=kwargs)
