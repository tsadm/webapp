import tsadmuser
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
