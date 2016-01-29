from tsadmcfg import getConfig
from tsadmdb import getDB
from tsadmuser import TSAdmUser
from tsadmlog import TSAdmLogger

logger = TSAdmLogger()

class TSAdm:
    cfg = None
    db = None
    user = None

    def __init__(self):
        logger.debug('TSAdm init')
        self.cfg = getConfig()
        self.db = getDB()
        self.user = TSAdmUser()
