from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.template.response import TemplateResponse

from . import TSAdm
from .log import TSAdmLogger

logger = TSAdmLogger(__name__)

class TSAdmView(LoginRequiredMixin, TemplateView):
    tsadm = None
    http_method_names = ['get', 'head', 'options']

    def __init__(self):
        logger.debug('TSAdmView init')
        super(TSAdmView, self).__init__()
        self.tsadm = TSAdm()

    def get_context_data(self, **kwargs):
        logger.debug('get_context_data')
        context = super(TSAdmView, self).get_context_data(**kwargs)
        context['tsadm'] = dict(
            user=self.tsadm.user,
        )
        return context

    def dispatch(self, request, *args, **kwargs):
        logger.debug('dispatch:', request)
        try:
            self.tsadm.user.load(self.request.user)
        except Exception as e:
            return self.dispatchException(e)
        else:
            response = super(TSAdmView, self).dispatch(request, *args, **kwargs)
            logger.debug('dispatch response:', response)
            try:
                logger.debug('response context data:', response.context_data)
            except AttributeError as e:
                logger.debug('no template response:', e)
            return response

    def dispatchException(self, exc):
        logger.error('dispatch exception:', repr(exc))
        return TemplateResponse(
            self.request,
            'tsadm/error.html',
            {'error': {'status': 500, 'message': str(exc)}},
            status=500,
        )

class HomeView(TSAdmView):
    template_name = 'tsadm/home.html'

    def __init__(self):
        logger.debug('HomeView init')
        super(HomeView, self).__init__()
