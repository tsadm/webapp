from tsadmcfg import getConfig
from tsadmdb import getDB

class TSAdm:
    cfg = None
    db = None

    def __init__(self):
        self.cfg = getConfig()
        self.db = getDB()
