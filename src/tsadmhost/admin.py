from django.contrib import admin
from .models import TSAdmHostDB

class HostAdmin(admin.ModelAdmin):
    pass

admin.site.register(TSAdmHostDB, HostAdmin)
