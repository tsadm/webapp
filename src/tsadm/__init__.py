from tsadmcfg import TSAdmCfg
from tsadmdb import getDB
from tsadmuser import TSAdmUser
from tsadmlog import TSAdmLogger

logger = TSAdmLogger(__name__)

class TSAdm:
    cfg = None
    db = None
    user = None

    def __init__(self):
        logger.debug('TSAdm init')
        self.cfg = TSAdmCfg()
        self.db = getDB()
        self.user = TSAdmUser()
