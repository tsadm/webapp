from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from tsadmlog import TSAdmLogger
from tsadm import TSAdm

logger = TSAdmLogger()

class TSAdmView(LoginRequiredMixin, TemplateView):
    tsadm = None

    def __init__(self):
        logger.debug('TSAdmView init')
        self.tsadm = TSAdm()
