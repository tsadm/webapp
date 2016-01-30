from tsadm.log import TSAdmLogger
from tsadm.views import TSAdmView

logger = TSAdmLogger(__name__)

class UserView(TSAdmView):
    template_name = 'tsadmuser/home.html'

    def __init__(self):
        logger.debug('UserView init')
        super(UserView, self).__init__()
