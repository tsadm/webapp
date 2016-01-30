from django.db import models
from django.conf import settings

class TSAdmUserDB(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name = 'tsadmuser',
    )
