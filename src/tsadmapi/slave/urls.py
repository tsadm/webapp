from django.conf.urls import url
from .views import SetupScriptView

urlpatterns = [
    url(r'^setup\.sh$', SetupScriptView.as_view(), name='setupscript'),
]
