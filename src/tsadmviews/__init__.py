from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from tsadm import TSAdm
from tsadmlog import TSAdmLogger

logger = TSAdmLogger(__name__)

class TSAdmView(LoginRequiredMixin, TemplateView):
    tsadm = None
    http_method_names = ['get', 'head', 'options']

    def __init__(self):
        logger.debug('TSAdmView init')
        self.tsadm = TSAdm()

    def get_context_data(self, **kwargs):
        logger.debug('get_context_data')
        context = super(TSAdmView, self).get_context_data(**kwargs)
        context['tsadm'] = dict()
        return context

    def dispatch(self, request, *args, **kwargs):
        logger.debug('dispatch', request)
        response = super(TSAdmView, self).dispatch(request, *args, **kwargs)
        logger.debug('dispatch response:', response)
        return response
