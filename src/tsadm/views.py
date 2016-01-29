from tsadmlog import TSAdmLogger
from tsadmviews import TSAdmView

logger = TSAdmLogger(__name__)

class HomeView(TSAdmView):
    template_name = 'tsadm/home.html'

    def __init__(self):
        logger.debug('HomeView init')
        super(HomeView, self).__init__()
