from .config import TSAdmCfg
from .log import TSAdmLogger

import tsadmuser

logger = TSAdmLogger(__name__)

class TSAdm:
    cfg = None
    user = None

    class Error(Exception):
        status = None
        message = None

        def __init__(self, status, message):
            self.status = status
            self.message = message


    def __init__(self):
        logger.debug('TSAdm init')
        self.cfg = TSAdmCfg()


    def start(self, django_user):
        if not django_user.is_anonymous():
            self.user = tsadmuser.load(django_user)
