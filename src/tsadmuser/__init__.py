from tsadm.log import TSAdmLogger
from django.core.exceptions import ObjectDoesNotExist

logger = TSAdmLogger(__name__)

class TSAdmUser:
    def load(self, django_user):
        logger.debug('load django user:', django_user)
        try:
            return django_user.tsadmuser
        except ObjectDoesNotExist:
            from tsadmuser.models import TSAdmUserDB
            logger.warning('user not initialized')
            u = TSAdmUserDB(user=django_user)
            return u.save()
