from django.db import models



class TSAdmSiteDB(models.Model):
    class Meta:
        verbose_name = "Site"
        verbose_name_plural = "Sites"

    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.name



class TSAdmSiteEnvDB(models.Model):
    class Meta:
        verbose_name = "SiteEnv"
        verbose_name_plural = "SiteEnvs"

    name = models.CharField(max_length=64, unique=False)
    site = models.ForeignKey(
        TSAdmSiteDB,
        on_delete=models.PROTECT,
    )
    host = models.ForeignKey(
        'tsadmhost.TSAdmHostDB',
        on_delete=models.PROTECT,
    )
    users = models.ManyToManyField(
        'tsadmuser.TSAdmUserDB',
        through='TSAdmSiteEnvACL',
        related_name='siteenv',
    )

    def __str__(self):
        return '{}.{}'.format(self.site.name, self.name)



class TSAdmSiteEnvACL(models.Model):
    class Meta:
        verbose_name = "SiteEnvACL"
        verbose_name_plural = "SiteEnvsACL"

    user = models.ForeignKey('tsadmuser.TSAdmUserDB', on_delete=models.PROTECT)
    siteenv = models.ForeignKey(TSAdmSiteEnvDB, on_delete=models.PROTECT)

    def __str__(self):
        return '{} {}.{}'.format(self.user.user.username, self.siteenv.site.name, self.siteenv.name)
