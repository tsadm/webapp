"""tsadm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url, include
from django.contrib import admin

from .views import HomeView

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^auth/', include('tsadm.auth_urls')),
    url(r'^user/', include('tsadmuser.urls', namespace='user')),
    url(r'^site/', include('tsadmsite.urls', namespace='site')),
    url(r'^host/', include('tsadmhost.urls', namespace='host')),
    url(r'^api/', include('tsadmapi.urls', namespace='api')),
    url(r'^admin/', admin.site.urls),
]
