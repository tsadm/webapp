from django.db import models

class HostDB(models.Model):
    class Meta:
        verbose_name = "Host"
        verbose_name_plural = "Hosts"

    fqdn = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.fqdn
