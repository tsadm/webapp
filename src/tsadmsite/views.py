from tsadm.log import TSAdmLogger
from tsadm.views import TSAdmView
from . import TSAdmSite
from .models import TSAdmSiteDB, TSAdmSiteEnvDB

logger = TSAdmLogger(__name__)

class SiteView(TSAdmView):
    template_name = 'tsadmsite/home.html'

    def __init__(self):
        logger.debug('SiteView init')
        super(SiteView, self).__init__()

    def get_context_data(self, **kwargs):
        context = super(SiteView, self).get_context_data(**kwargs)
        dbobj = TSAdmSiteDB.objects.get(name=kwargs['name'])
        context['tsadm']['site'] = TSAdmSite(dbobj)
        context['tsadm']['siteEnvs'] = self.tsadm.user.siteEnvs(dbobj.id)
        return context


class SiteEnvView(TSAdmView):
    template_name = 'tsadmsite/env_home.html'

    def __init__(self):
        logger.debug('SiteEnvView init')
        super(SiteEnvView, self).__init__()

    def get_context_data(self, **kwargs):
        context = super(SiteEnvView, self).get_context_data(**kwargs)
        dbobj = TSAdmSiteDB.objects.get(name=kwargs['site'])
        context['tsadm']['site'] = TSAdmSite(dbobj)
        dbobj = TSAdmSiteEnvDB.objects.get(name=kwargs['env'], site__name=kwargs['site'])
        context['tsadm']['siteEnv'] = dbobj
        return context
