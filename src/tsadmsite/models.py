from django.db import models

class TSAdmSiteDB(models.Model):
    class Meta:
        verbose_name = "Site"
        verbose_name_plural = "Sites"

    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return "Site:"+self.name
