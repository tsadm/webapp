from django.db import models
from django.conf import settings

class TSAdmUserDB(models.Model):
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name = 'tsadmuser',
    )

    def __str__(self):
        return self.user.username
