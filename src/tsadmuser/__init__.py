from tsadm.log import TSAdmLogger
from django.core.exceptions import ObjectDoesNotExist

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

    def siteEnvs(self):
        return self._db.tsadmuser.siteenv.all()
