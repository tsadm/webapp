from tsadm.log import TSAdmLogger
from tsadm.errors import TSAdmError
from django.core.exceptions import ObjectDoesNotExist

logger = TSAdmLogger(__name__)


def load(django_user):
    logger.debug('load django user:', django_user)
    try:
        user = django_user.tsadmuser
    except ObjectDoesNotExist:
        from tsadmuser.models import UserDB
        logger.warning('user not initialized')
        user = UserDB(user=django_user)
        user.save()
    return user


def sitesAll(user):
    sites = list()
    prevId = None
    for env in user.siteenv.order_by('site__name', 'name'):
        sid = env.site.id
        if sid != prevId:
            sites.append(env.site)
        prevId = sid
    return sites


def site(user, name):
    try:
        e = user.siteenv.filter(site__name=name)[0]
        return e.site
    except IndexError:
        raise TSAdmError(400, 'invalid request')


def siteEnvsAll(user, site):
    return user.siteenv.filter(site=site).order_by('site__name', 'name')


def siteEnv(user, site, name):
    return user.siteenv.get(site=site, name=name)


def hostsAll(user):
    hl = list()
    prev = None
    for e in user.siteenv.order_by('host__fqdn'):
        h = e.host.fqdn
        if h != prev:
            hl.append(h)
        prev = h
    return hl


def hostEnvsAll(user, host):
    return user.siteenv.filter(host__fqdn=host).order_by('site__name', 'name')


def host(user, ID):
    try:
        e = user.siteenv.filter(host__id=ID)[0]
        return e.host
    except IndexError:
        raise TSAdmError(400, 'invalid request')
