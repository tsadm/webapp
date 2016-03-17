from django.conf.urls import url
from .views import SiteView, SiteEnvView

urlpatterns = [
    url(r'(?P<name>[a-zA-Z0-9]+)/$', SiteView.as_view(), name='home'),
    url(r'(?P<site>[a-zA-Z0-9]+)/(?P<env>[a-zA-Z0-9]+)$', SiteEnvView.as_view(), name='env'),
]
