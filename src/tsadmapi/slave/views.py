import os.path
from tsadm.log import TSAdmLogger
from tsadm.views.files import TSAdmServeFileView

logger = TSAdmLogger(__name__)


class SetupScriptView(TSAdmServeFileView):

    def __init__(self):
        logger.debug('SetupScriptView init')
        super(SetupScriptView, self).__init__()

    def get_context_data(self, **kwargs):
        context = super(SetupScriptView, self).get_context_data()
        context['fileName'] = 'setup.sh'
        context['docRoot'] = os.path.join(
            self.tsadm.cfg.get('RUN_DIR'), 'ansible', 'libexec', 'slave'
        )
        return context
