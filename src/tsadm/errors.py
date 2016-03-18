class TSAdmError(Exception):
    status = None
    message = None

    def __init__(self, status, message):
        self.status = status
        self.message = message
