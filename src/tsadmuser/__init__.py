from tsadm.log import TSAdmLogger
from django.core.exceptions import ObjectDoesNotExist
from tsadmsite import TSAdmSite

logger = TSAdmLogger(__name__)

class TSAdmUser:
    _db = None

    def load(self, django_user):
        logger.debug('load django user:', django_user)
        self._db = django_user
        try:
            _ = django_user.tsadmuser
        except ObjectDoesNotExist:
            from tsadmuser.models import TSAdmUserDB
            logger.warning('user not initialized')
            u = TSAdmUserDB(user=django_user)
            return u.save()

    def sites(self):
        sites = list()
        prevId = None
        for env in self._db.tsadmuser.siteenv.order_by('site__name', 'name'):
            sid = env.site.id
            if sid != prevId:
                sites.append(TSAdmSite(env.site))
            prevId = sid
        return sites

    def siteEnvs(self, siteId):
        return self._db.tsadmuser.siteenv.filter(site__id=siteId).order_by('site__name', 'name').values()
