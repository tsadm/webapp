_CFG = {
    'LOG_FTIME': '%d/%b/%Y %H:%M:%S',
}

class TSAdmCfg:
    def get(self, name, default=None):
        return _CFG.get(name, default)
