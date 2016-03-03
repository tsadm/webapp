from django.contrib import admin
from .models import TSAdmSiteDB, TSAdmSiteEnvDB, TSAdmSiteEnvACL

class SiteEnvAdmin(admin.StackedInline):
    model = TSAdmSiteEnvDB
    extra = 0


class SiteAdmin(admin.ModelAdmin):
    inlines = [SiteEnvAdmin]

class SiteEnvACLAdmin(admin.ModelAdmin):
    pass

admin.site.register(TSAdmSiteDB, SiteAdmin)
admin.site.register(TSAdmSiteEnvACL, SiteEnvACLAdmin)
