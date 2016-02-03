from tsadm.log import TSAdmLogger

logger = TSAdmLogger(__name__)

class TSAdmSite:
    _dbobj = None

    def __init__(self, name):
        logger.debug('init site:', name)
        from .models import TSAdmSiteDB
        self._dbobj = TSAdmSiteDB.objects.get(name=name)

    def ID(self):
        return self._dbobj.pk

    def name(self):
        return self._dbobj.name
