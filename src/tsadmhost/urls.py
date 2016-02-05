from django.conf.urls import url
from .views import HostView

urlpatterns = [
    url(r'(?P<ID>\d+)/$', HostView.as_view(), name='home'),
]
