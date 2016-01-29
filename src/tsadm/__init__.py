from tsadmcfg import getConfig
from tsadmdb import getDB
from tsadmuser import TSAdmUser

class TSAdm:
    cfg = None
    db = None
    user = None

    def __init__(self):
        self.cfg = getConfig()
        self.db = getDB()
        self.user = TSAdmUser()
