from django.contrib import admin
from .models import TSAdmSiteDB, TSAdmSiteEnvDB

class SiteAdmin(admin.ModelAdmin):
    pass

class SiteEnvAdmin(admin.ModelAdmin):
    pass

admin.site.register(TSAdmSiteDB, SiteAdmin)
admin.site.register(TSAdmSiteEnvDB, SiteEnvAdmin)
