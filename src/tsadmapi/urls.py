from django.conf.urls import url, include

urlpatterns = [
    url(r'^inventory/', include('tsadmapi.inventory.urls', namespace='inventory')),
    url(r'^slave/', include('tsadmapi.slave.urls', namespace='slave')),
]
