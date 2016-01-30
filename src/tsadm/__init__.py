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
