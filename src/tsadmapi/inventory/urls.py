from django.conf.urls import url
from .views import HostGroupsView, HostInfoView

urlpatterns = [
    url(r'^hostgroups/$', HostGroupsView.as_view(), name='hostgroups'),
    url(r'^hostinfo/(?P<fqdn>[\w\.]+)/$', HostInfoView.as_view(), name='hostinfo'),
]
