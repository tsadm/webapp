import os.path

_DEFAULT = {
    'CODE_DIR': os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
}

class TSAdmCfg:
    def get(self, name, default=None):
        return _DEFAULT.get(name, default)

__CFG = None

def getConfig():
    global __CFG
    if __CFG is None:
        __CFG = TSAdmCfg()
    return __CFG
