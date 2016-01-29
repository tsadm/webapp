from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from tsadm import TSAdm

class TSAdmView(LoginRequiredMixin, TemplateView):
    tsadm = None

    def __init__(self):
        self.tsadm = TSAdm()
