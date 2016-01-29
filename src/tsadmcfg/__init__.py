import os.path

_DEFAULT = {
    'CODE_DIR': os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    'LOG_FTIME': '%d/%b/%Y %H:%M:%S',
}

class TSAdmCfg:
    def get(self, name, default=None):
        return _DEFAULT.get(name, default)
