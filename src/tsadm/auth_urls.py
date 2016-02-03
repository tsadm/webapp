from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from .config import TSAdmCfg

cfg = TSAdmCfg()

def tmplPath(relPath):
    absPath = 'theme/{}/{}'.format(cfg.get('TEMPLATES_THEME', 'devel'), relPath)
    return absPath

urlpatterns = [
    # login/logout
    url(r'^login/$', auth_views.login,
        {'template_name': tmplPath('tsadm/login.html')}, name='login'),
    url(r'^logout/$', auth_views.logout_then_login, name='logout'),

    # password change
    url(r'^password_change/$', auth_views.password_change,
        {'template_name': 'tsadm/password_change_form.html'}, name='password_change'),
    url(r'^password_change/done/$', auth_views.password_change_done,
        {'template_name': 'tsadm/password_change_done.html'},
        name='password_change_done'),

    # password reset
    url(r'^password_reset/$', auth_views.password_reset,
        {'template_name': 'tsadm/password_reset_form.html',
        'email_template_name': 'tsadm/password_reset_email.html',
        'subject_template_name': 'tsadm/password_reset_subject.txt',},
        name='password_reset'),
    url(r'^password_reset/done/$', auth_views.password_reset_done,
        {'template_name': 'tsadm/password_reset_done.html'},
        name='password_reset_done'),

    # reset confirm
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', auth_views.password_reset_confirm,
        {'template_name': 'tsadm/password_reset_confirm.html'},
        name='password_reset_confirm'),
    url(r'^reset/done/$', auth_views.password_reset_complete,
        {'template_name': 'tsadm/password_reset_complete.html'}, name='password_reset_complete'),
]
