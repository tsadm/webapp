from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.template.response import TemplateResponse
from django.core.exceptions import ObjectDoesNotExist

from .. import TSAdm
from ..log import TSAdmLogger
from ..errors import TSAdmError

logger = TSAdmLogger(__name__)


class TSAdmBaseView(TemplateView):
    tsadm = None
    http_method_names = ['get', 'head', 'options']

    def __init__(self):
        logger.debug('TSAdmBaseView init')
        super(TSAdmBaseView, self).__init__()
        self.tsadm = TSAdm()


    def get_context_data(self, **kwargs):
        logger.debug('get_context_data')
        context = super(TSAdmBaseView, self).get_context_data(**kwargs)
        context['tsadm'] = dict(
            version=self.tsadm.version,
        )
        return context


    def dispatch(self, request, *args, **kwargs):
        logger.debug('dispatch:', request)
        self.template_name = 'theme/{}/{}'.format(
            self.tsadm.cfg.get('TEMPLATES_THEME', 'devel'),
            self.template_name,
        )
        logger.debug('dispatch template:', self.template_name)
        try:
            response = super(TSAdmBaseView, self).dispatch(request, *args, **kwargs)
        except ObjectDoesNotExist as e:
            logger.error('object does not exists!')
            return self.dispatchException(e, status=400, message='invalid request')
        except TSAdmError as e:
            logger.error('tsadm exception:', e)
            return self.dispatchException(e, status=e.status, message=e.message)
        except Exception as dispatchExc:
            logger.error('exception:', dispatchExc)
            return self.dispatchException(dispatchExc)
        else:
            try:
                logger.debug('response context data:', response.context_data)
            except AttributeError as e:
                logger.debug('no template response:', e)
            logger.debug('dispatch response:', repr(response))
            return response


    def dispatchException(self, exc, status=500, message=None):
        logger.debug('dispatch exception:', repr(exc))
        if message is None:
            message = str(exc)
        return TemplateResponse(
            self.request,
            'theme/{}/tsadm/error.html'.format(self.tsadm.cfg.get('TEMPLATES_THEME', 'devel')),
            {'error': {'status': status, 'message': message}},
            status=status,
        )


class TSAdmAnonView(TSAdmBaseView):

    def __init__(self):
        logger.debug('TSAdmAnonView init')
        super(TSAdmAnonView, self).__init__()


    def get_context_data(self, **kwargs):
        logger.debug('get_context_data')
        context = super(TSAdmAnonView, self).get_context_data(**kwargs)
        context['tsadm']['user'] = None
        return context


    def dispatch(self, request, *args, **kwargs):
        logger.debug('dispatch:', request)
        try:
            response = super(TSAdmAnonView, self).dispatch(request, *args, **kwargs)
        except Exception as dispatchExc:
            logger.error('exception:', dispatchExc)
            return self.dispatchException(dispatchExc)
        else:
            logger.debug('dispatch response:', repr(response))
            return response


class TSAdmView(LoginRequiredMixin, TSAdmBaseView):

    def __init__(self):
        logger.debug('TSAdmView init')
        super(TSAdmView, self).__init__()


    def get_context_data(self, **kwargs):
        logger.debug('get_context_data')
        context = super(TSAdmView, self).get_context_data(**kwargs)
        context['tsadm']['user'] = self.tsadm.user
        return context


    def dispatch(self, request, *args, **kwargs):
        logger.debug('dispatch:', request)
        try:
            self.tsadm.start(self.request.user)
        except Exception as e:
            return self.dispatchException(e)
        else:
            try:
                response = super(TSAdmView, self).dispatch(request, *args, **kwargs)
            except Exception as dispatchExc:
                logger.error('exception:', dispatchExc)
                return self.dispatchException(dispatchExc)
            else:
                logger.debug('dispatch response:', repr(response))
                return response
