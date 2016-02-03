from django.conf.urls import url
from .views import SiteView

urlpatterns = [
    url(r'(?P<name>[a-zA-Z0-9]+)/$', SiteView.as_view(), name='home'),
]
