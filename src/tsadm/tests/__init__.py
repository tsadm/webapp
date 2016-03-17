from django.core.urlresolvers import reverse
from django.test import TestCase
from django.contrib.auth.models import User

import tsadmuser

class TSAdmTestBase(TestCase):
    fixtures = ['testdata']

    def setUp(self):
        self.django_user = User.objects.get(username='tester')
        self.client.force_login(self.django_user)
        self.user = tsadmuser.load(self.django_user)

    def getURL(self, urlTag, kwargs=None):
        return reverse(urlTag, kwargs=kwargs)
