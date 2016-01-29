from tsadmcfg import getConfig

class TSAdm:
    cfg = None

    def __init__(self):
        self.cfg = getConfig()
