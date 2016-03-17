from tsadm.log import TSAdmLogger
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
    e = user.siteenv.get(site__name=name)
    return e.site


def siteEnvsAll(user, site):
    return user.siteenv.filter(site=site).order_by('site__name', 'name')


def siteEnv(user, site, name):
    return user.siteenv.get(site=site, name=name)
