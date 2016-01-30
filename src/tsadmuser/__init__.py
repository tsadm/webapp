from tsadm.log import TSAdmLogger

logger = TSAdmLogger(__name__)

class TSAdmUser:
    def load(self, django_user):
        logger.debug('load django user:', django_user)
        # FIXME
        #~ return django_user.tsadmuser
        return False
