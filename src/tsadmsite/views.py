from tsadm.log import TSAdmLogger
from tsadm.views import TSAdmView
from .models import SiteDB, SiteEnvDB

import tsadmuser

logger = TSAdmLogger(__name__)

class SiteView(TSAdmView):
    template_name = 'tsadmsite/home.html'

    def __init__(self):
        logger.debug('SiteView init')
        super(SiteView, self).__init__()

    def get_context_data(self, **kwargs):
        context = super(SiteView, self).get_context_data(**kwargs)
        dbobj = SiteDB.objects.get(name=kwargs['name'])
        context['tsadm']['site'] = dbobj
        context['tsadm']['siteEnvs'] = tsadmuser.siteEnvs(self.tsadm.user, dbobj.id)
        if not context['tsadm']['siteEnvs']:
            raise self.tsadm.Error('invalid request', 400)
        return context


class SiteEnvView(TSAdmView):
    template_name = 'tsadmsite/env_home.html'

    def __init__(self):
        logger.debug('SiteEnvView init')
        super(SiteEnvView, self).__init__()

    def get_context_data(self, **kwargs):
        context = super(SiteEnvView, self).get_context_data(**kwargs)
        context['tsadm']['site'] = SiteDB.objects.get(name=kwargs['site'])
        context['tsadm']['siteEnv'] = SiteEnvDB.objects.get(name=kwargs['env'], site__name=kwargs['site'])
        return context
