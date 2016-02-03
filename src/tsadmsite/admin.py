from django.contrib import admin
from .models import TSAdmSiteDB

class SiteAdmin(admin.ModelAdmin):
    pass

admin.site.register(TSAdmSiteDB, SiteAdmin)
