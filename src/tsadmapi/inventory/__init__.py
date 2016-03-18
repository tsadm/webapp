import tsadmuser
from tsadm.errors import TSAdmError


def hostInfo(user, host):
    henvs = tsadmuser.hostEnvsAll(user, host)
    if henvs:
        return {host: [repr(e) for e in henvs]}
    else:
        raise TSAdmError(400, 'invalid request')


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
