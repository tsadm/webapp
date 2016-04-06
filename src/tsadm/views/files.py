from .base import TSAdmView
from ..log import TSAdmLogger
from django.views.static import serve

logger = TSAdmLogger(__name__)

class TSAdmServeFileView(TSAdmView):

    def render_to_response(self, context, **respargs):
        fileName = context.get('fileName', None)
        docRoot = context.get('docRoot', None)
        return serve(self.request, fileName, docRoot)

    def get_context_data(self, **kwargs):
        return dict()
