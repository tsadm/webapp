from django.db import models

class TSAdmSiteDB(models.Model):
    class Meta:
        verbose_name = "Site"
        verbose_name_plural = "Sites"

    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return "Site:"+self.name

class TSAdmSiteEnvDB(models.Model):
    class Meta:
        verbose_name = "SiteEnv"
        verbose_name_plural = "SiteEnvs"

    name = models.CharField(max_length=64, unique=True)
    site = models.ForeignKey(
        TSAdmSiteDB,
        on_delete=models.PROTECT,
    )
    host = models.ForeignKey(
        'tsadmhost.TSAdmHostDB',
        on_delete=models.PROTECT,
    )

    def __str__(self):
        return "SiteEnv:"+self.name
