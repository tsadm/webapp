class TSAdmDB:
    pass

__DB = None

def getDB():
    global __DB
    if __DB is None:
        __DB = TSAdmDB()
    return __DB
