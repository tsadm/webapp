from tsadm.log import TSAdmLogger
from tsadm.views import TSAdmView
from . import TSAdmSite
from .models import TSAdmSiteDB

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
        return context
