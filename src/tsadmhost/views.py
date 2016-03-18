from tsadm.log import TSAdmLogger
from tsadm.views import TSAdmView
from tsadm.errors import TSAdmError
import tsadmuser

logger = TSAdmLogger(__name__)

class HostView(TSAdmView):
    template_name = 'tsadmhost/home.html'

    def __init__(self):
        logger.debug('HostView init')
        super(HostView, self).__init__()

    def get_context_data(self, **kwargs):
        context = super(HostView, self).get_context_data(**kwargs)
        context['tsadm']['host'] = tsadmuser.host(self.tsadm.user, kwargs['ID'])
        if not context['tsadm']['host']:
            logger.error('invalid host request')
            raise TSAdmError(400, 'invalid request')
        return context
