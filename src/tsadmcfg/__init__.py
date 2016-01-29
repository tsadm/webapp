class TSAdmCfg:
    def get(self, name, default=None):
        return default

__CFG = None

def getConfig():
    global __CFG
    if __CFG is None:
        __CFG = TSAdmCfg()
    return __CFG
