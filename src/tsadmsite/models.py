from django.db import models


class SiteDB(models.Model):
    class Meta:
        verbose_name = "Site"
        verbose_name_plural = "Sites"

    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.name


class SiteEnvDB(models.Model):
    class Meta:
        verbose_name = "SiteEnv"
        verbose_name_plural = "SiteEnvs"

    name = models.CharField(max_length=64, unique=False)
    site = models.ForeignKey(
        SiteDB,
        on_delete=models.PROTECT,
    )
    host = models.ForeignKey(
        'tsadmhost.HostDB',
        on_delete=models.PROTECT,
    )
    users = models.ManyToManyField(
        'tsadmuser.UserDB',
        through='SiteEnvACL',
        related_name='siteenv',
    )

    def __str__(self):
        return '{}.{}'.format(self.site.name, self.name)


class SiteEnvACL(models.Model):
    class Meta:
        verbose_name = "SiteEnvACL"
        verbose_name_plural = "SiteEnvsACL"

    user = models.ForeignKey('tsadmuser.UserDB', on_delete=models.PROTECT)
    siteenv = models.ForeignKey(SiteEnvDB, on_delete=models.PROTECT)

    def __str__(self):
        return '{} {}.{}'.format(self.user.user.username, self.siteenv.site.name, self.siteenv.name)
