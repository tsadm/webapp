import tsadmuser


def hostInfo(user, host):
    henvs = user.siteenv.filter(host__fqdn=host).order_by('site__name', 'name')
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
