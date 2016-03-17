def _hostsList(user):
    hl = list()
    prev = None
    for e in user.siteenv.order_by('host'):
        h = e.host.fqdn
        if h != prev:
            hl.append(h)
        prev = h
    return hl


def hostGroups(user):
    return {
        "all": {
            "hosts": _hostsList(user),
            "vars": {},
        },
    }
