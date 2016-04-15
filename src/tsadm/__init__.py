import os.path

from .config import TSAdmCfg
from .log import TSAdmLogger

import tsadmuser

logger = TSAdmLogger(__name__)

class TSAdm:
    cfg = None
    user = None
    version = None

    def __init__(self):
        logger.debug('TSAdm init')
        self.cfg = TSAdmCfg()
        self.version = self._getVersion()

    def _getVersion(self):
        ver = None
        fn = os.path.join(self.cfg.get('BASE_DIR'), 'VERSION')
        with open(fn, 'r') as fh:
            ver = fh.read().strip()
            fh.close()
        logger.info('TSAdm version:', ver)
        return ver

    def start(self, django_user):
        if not django_user.is_anonymous():
            self.user = tsadmuser.load(django_user)
