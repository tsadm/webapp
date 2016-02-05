from tsadm.log import TSAdmLogger

logger = TSAdmLogger(__name__)

class TSAdmHost:
    _dbobj = None

    def __init__(self, dbobj):
        logger.debug('init host:', dbobj.fqdn)
        self._dbobj = dbobj

    def ID(self):
        return self._dbobj.pk

    def fqdn(self):
        return self._dbobj.fqdn
