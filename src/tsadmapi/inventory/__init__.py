import tsadmuser


def hostInfo(user, host):
    henvs = tsadmuser.hostEnvsAll(user, host)
    return {host: [repr(e) for e in henvs]}


def hostGroups(user):
    hosts = tsadmuser.hostsAll(user)
    meta = {'hostvars': {}}
    for h in hosts:
        meta['hostvars'].update(hostInfo(user, h))
    return {
        "all": {
            "hosts": hosts,
            "vars": {},
        },
        "_meta": meta,
    }
