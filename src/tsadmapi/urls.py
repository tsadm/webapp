from django.conf.urls import url, include

urlpatterns = [
    url(r'^inventory/', include('tsadmapi.inventory.urls', namespace='inventory')),
]
