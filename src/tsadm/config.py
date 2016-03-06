_CFG = {
    'LOG_LEVEL': 'OFF',
    'LOG_FTIME': '%d/%b/%Y %H:%M:%S',
    'TEMPLATES_THEME': 'devel',
}

class TSAdmCfg:
    def get(self, name, default=None):
        return _CFG.get(name, default)
