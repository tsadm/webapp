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


def sites(user):
    sites = list()
    prevId = None
    for env in user.siteenv.order_by('site__name', 'name'):
        sid = env.site.id
        if sid != prevId:
            sites.append(env.site)
        prevId = sid
    return sites


def siteEnvs(user, siteId):
    return user.siteenv.filter(site__id=siteId).order_by('site__name', 'name')
