from django.contrib import admin
from .models import TSAdmSiteDB, TSAdmSiteEnvDB

class SiteEnvAdmin(admin.StackedInline):
    model = TSAdmSiteEnvDB
    extra = 0


class SiteAdmin(admin.ModelAdmin):
    inlines = [SiteEnvAdmin]

admin.site.register(TSAdmSiteDB, SiteAdmin)
