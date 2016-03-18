from django.http import JsonResponse
from .base import TSAdmView
from ..log import TSAdmLogger

logger = TSAdmLogger(__name__)

class TSAdmJsonView(TSAdmView):

    def render_to_response(self, context, **respargs):
        prettyPrint = None
        if self.tsadm.cfg.get('JSON_PRETTY_PRINT', False):
            prettyPrint = {'indent': 4, 'sort_keys': True}
        return JsonResponse(
            context,
            json_dumps_params=prettyPrint,
            **respargs
        )

    def get_context_data(self, **kwargs):
        return dict()

    def dispatchException(self, exc, status=500, message=None):
        logger.debug('dispatch JSON exception:', repr(exc))
        if message is None:
            message = str(exc)
        return JsonResponse(
            {"error": message},
            status=status,
        )
