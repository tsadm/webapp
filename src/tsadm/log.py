import sys
import time

from .config import TSAdmCfg

class _Log:
    cfg = None
    ftime = None
    initDone = False

class TSAdmLogger:
    _caller = __name__

    def __init__(self, caller):
        if not _Log.initDone:
            _Log.cfg = TSAdmCfg()
            _Log.ftime = _Log.cfg.get('LOG_FTIME')
            _Log.initDone = True
            self._print('init done')
        self._caller = caller

    def _print(self, *msg):
        print('[{}] {}:'.format(time.strftime(_Log.ftime), self._caller), *msg, file=sys.stderr)

    def debug(self, *msg):
        self._print(*msg)
