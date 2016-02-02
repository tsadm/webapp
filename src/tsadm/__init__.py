from .config import TSAdmCfg
from .log import TSAdmLogger
from tsadmuser import TSAdmUser

logger = TSAdmLogger(__name__)

class TSAdm:
    cfg = None
    user = None

    def __init__(self):
        logger.debug('TSAdm init')
        self.cfg = TSAdmCfg()
        self.user = TSAdmUser()

    def start(self, django_user):
        if not django_user.is_anonymous():
            return self.user.load(django_user)
        return True
