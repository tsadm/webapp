from tsadm.log import TSAdmLogger
from tsadm.views import TSAdmJsonView
from tsadmapi import inventory

logger = TSAdmLogger(__name__)


class HostGroupsView(TSAdmJsonView):

    def __init__(self):
        logger.debug('HostsGroupView init')
        super(HostGroupsView, self).__init__()

    def get_context_data(self, **kwargs):
        context = super(HostGroupsView, self).get_context_data(**kwargs)
        context['JsonData'] = inventory.hostGroups(self.tsadm.user)
        return context


class HostInfoView(TSAdmJsonView):

    def __init__(self):
        logger.debug('HostInfoView init')
        super(HostInfoView, self).__init__()
