from tsadm.log import TSAdmLogger
from tsadm.views import TSAdmView
from tsadm.errors import TSAdmError

import tsadmuser

logger = TSAdmLogger(__name__)

class SiteView(TSAdmView):
    template_name = 'tsadmsite/home.html'

    def __init__(self):
        logger.debug('SiteView init')
        super(SiteView, self).__init__()

    def get_context_data(self, **kwargs):
        context = super(SiteView, self).get_context_data(**kwargs)
        context['tsadm']['site'] = tsadmuser.site(self.tsadm.user, kwargs['name'])
        if not context['tsadm']['site']:
            logger.error(kwargs['name'], 'site not found')
            raise TSAdmError(400, 'invalid request')
        context['tsadm']['siteEnvs'] = tsadmuser.siteEnvsAll(
            self.tsadm.user,
            context['tsadm']['site'],
        )
        return context


class SiteEnvView(TSAdmView):
    template_name = 'tsadmsite/env_home.html'

    def __init__(self):
        logger.debug('SiteEnvView init')
        super(SiteEnvView, self).__init__()

    def get_context_data(self, **kwargs):
        context = super(SiteEnvView, self).get_context_data(**kwargs)
        context['tsadm']['site'] = tsadmuser.site(self.tsadm.user, kwargs['site'])
        context['tsadm']['siteEnv'] = tsadmuser.siteEnv(
            self.tsadm.user,
            context['tsadm']['site'],
            kwargs['env'],
        )
        return context
