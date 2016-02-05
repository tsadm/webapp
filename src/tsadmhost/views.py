from tsadm.log import TSAdmLogger
from tsadm.views import TSAdmView
from . import TSAdmHost
from .models import TSAdmHostDB

logger = TSAdmLogger(__name__)

class HostView(TSAdmView):
    template_name = 'tsadmhost/home.html'

    def __init__(self):
        logger.debug('HostView init')
        super(HostView, self).__init__()

    def get_context_data(self, **kwargs):
        context = super(HostView, self).get_context_data(**kwargs)
        dbobj = TSAdmHostDB.objects.get(pk=kwargs['ID'])
        context['tsadm']['host'] = TSAdmHost(dbobj)
        return context
