import sys

class TSAdmLogger:
    def __print(self, tag, *msg):
        print(tag, *msg, file=sys.stderr)

    def debug(self, *msg):
        self.__print('D:', *msg)

__LOGGER = None

def getLogger():
    if __LOGGER is None:
        __LOGGER = TSAdmLogger()
    return __LOGGER
