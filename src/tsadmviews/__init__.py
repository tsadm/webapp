from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from tsadm import TSAdm
from tsadmlog import TSAdmLogger

logger = TSAdmLogger(__name__)

class TSAdmView(LoginRequiredMixin, TemplateView):
    tsadm = None

    def __init__(self):
        logger.debug('TSAdmView init')
        self.tsadm = TSAdm()
