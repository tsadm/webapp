import sys
from tsadmcfg import TSAdmCfg

class TSAdmLogger:
    __cfg = None
    caller = None

    def __init__(self, caller):
        self.__cfg = TSAdmCfg()
        self.caller = caller

    def __print(self, *msg):
        print('{}:'.format(self.caller), *msg, file=sys.stderr)

    def debug(self, *msg):
        self.__print(*msg)
