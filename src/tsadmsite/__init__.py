from tsadm.log import TSAdmLogger

logger = TSAdmLogger(__name__)

class TSAdmSite:
    _dbobj = None

    def __init__(self, dbobj):
        logger.debug('init site:', dbobj.name)
        self._dbobj = dbobj

    def ID(self):
        return self._dbobj.pk

    def name(self):
        return self._dbobj.name
