import json
import os.path

_RUN_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

_CFG = {
    'LOG_LEVEL': 'OFF',
    'LOG_FTIME': '%d/%b/%Y %H:%M:%S',
    'TEMPLATES_THEME': 'devel',
    'JSON_PRETTY_PRINT': True,
    'RUN_DIR': _RUN_DIR,
}


class TSAdmCfg:
    def get(self, name, default=None):
        return _CFG.get(name, default)

    def dumps(self):
        return json.dumps(_CFG, sort_keys=True, indent=4)


if __name__ == '__main__':
    cfg = TSAdmCfg()
    print(cfg.dumps())
