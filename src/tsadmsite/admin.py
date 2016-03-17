from django.contrib import admin
from .models import SiteDB, SiteEnvDB, SiteEnvACL

class SiteEnvAdmin(admin.StackedInline):
    model = SiteEnvDB
    extra = 0


class SiteAdmin(admin.ModelAdmin):
    inlines = [SiteEnvAdmin]

class SiteEnvACLAdmin(admin.ModelAdmin):
    pass

admin.site.register(SiteDB, SiteAdmin)
admin.site.register(SiteEnvACL, SiteEnvACLAdmin)
