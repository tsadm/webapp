import os
import sys
import time

from .config import TSAdmCfg

_LEVELS = {
    'OFF': 0,
    'ERROR': 1,
    'WARNING': 2,
    'INFO': 3,
    'DEBUG': 4,
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
            _Log.level = os.environ.get('TSADM_LOG', None)
            if _Log.level is None:
                _Log.level = _Log.cfg.get('LOG_LEVEL', 'DEBUG')
            _Log.initDone = True
        self._caller = caller

    def _print(self, *msg, level=None):
        if _LEVELS.get(level) <= _LEVELS.get(_Log.level):
            print('[{}] {} - {}:'.format(time.strftime(_Log.ftime), level, self._caller), *msg, file=sys.stderr)

    def error(self, *msg):
        self._print(*msg, level='ERROR')

    def warning(self, *msg):
        self._print(*msg, level='WARNING')

    def info(self, *msg):
        self._print(*msg, level='INFO')

    def debug(self, *msg):
        self._print(*msg, level='DEBUG')
