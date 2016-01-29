import sys
import time

from tsadmcfg import TSAdmCfg

class TSAdmLogger:
    _cfg = None
    _ftime = None
    _caller = None

    def __init__(self, caller):
        self._cfg = TSAdmCfg()
        self._ftime = self._cfg.get('LOG_FTIME')
        self._caller = caller

    def _print(self, *msg):
        print('[{}] {}:'.format(time.strftime(self._ftime), self._caller), *msg, file=sys.stderr)

    def debug(self, *msg):
        self._print(*msg)
