import tsadmuser
import django.db
from .base import TSAdmView
from ..log import TSAdmLogger

logger = TSAdmLogger(__name__)

class HomeView(TSAdmView):
    template_name = 'tsadm/home.html'

    def __init__(self):
        logger.debug('HomeView init')
        super(HomeView, self).__init__()

    def get_context_data(self, **kwargs):
        logger.debug('get_context_data')
        context = super(HomeView, self).get_context_data(**kwargs)
        context['tsadm'] = dict(
            userSites=tsadmuser.sitesAll(self.tsadm.user),
        )
        return context


class InfoView(TSAdmView):
    template_name = 'tsadm/info.html'

    def __init__(self):
        logger.debug('InfoView init')
        super(InfoView, self).__init__()

    def _dbconns(self):
        dbConnections = list()
        for dbconn in django.db.connections.all():
            dbinfo = {
                'alias': dbconn.alias,
                'version': dbconn.Database.version,
                'name': dbconn.settings_dict['NAME'],
                'vendor': dbconn.vendor,
                'vendorVersion': None,
            }
            if dbconn.vendor == 'sqlite':
                dbinfo['vendorVersion'] = dbconn.Database.sqlite_version
            dbConnections.append(dbinfo)
        return dbConnections

    def get_context_data(self, **kwargs):
        logger.debug('get_context_data')
        context = super(InfoView, self).get_context_data(**kwargs)
        context['tsadm'] = {
            'config': self.tsadm.cfg.dumps(),
            'dbConnections': self._dbconns(),
        }
        return context
