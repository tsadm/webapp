import sys
import time

from .config import TSAdmCfg

_LEVELS = {
    'OFF': 0,
    'DEBUG': 1,
    'WARNING': 2,
    'ERROR': 3,
}

class _Log:
    cfg = None
    ftime = None
    level = None
    initDone = False

class TSAdmLogger:
    _caller = __name__

    def __init__(self, caller):
        if not _Log.initDone:
            _Log.cfg = TSAdmCfg()
            _Log.ftime = _Log.cfg.get('LOG_FTIME')
            _Log.level = _Log.cfg.get('LOG_LEVEL', 'DEBUG')
            _Log.initDone = True
        self._caller = caller

    def _print(self, *msg, level=None):
        if _LEVELS.get(level) <= _LEVELS.get(_Log.level):
            print('[{}] {} - {}:'.format(time.strftime(_Log.ftime), level, self._caller), *msg, file=sys.stderr)

    def debug(self, *msg):
        self._print(*msg, level='DEBUG')

    def error(self, *msg):
        self._print(*msg, level='ERROR')
