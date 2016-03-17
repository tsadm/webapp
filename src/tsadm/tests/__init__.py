from __future__ import print_function

import sys
from django.core.urlresolvers import reverse
from django.test import TestCase
from django.contrib.auth.models import User

import tsadmuser

print('Python', sys.version, file=sys.stderr)

class TSAdmTestBase(TestCase):

    def setUp(self):
        self.django_user = User.objects.create_user(username='tester')
        self.client.force_login(self.django_user)
        self.user = tsadmuser.load(self.django_user)

    def getURL(self, urlTag, kwargs=None):
        return reverse(urlTag, kwargs=kwargs)
