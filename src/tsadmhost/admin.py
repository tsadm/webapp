from django.contrib import admin
from .models import HostDB

class HostAdmin(admin.ModelAdmin):
    pass

admin.site.register(HostDB, HostAdmin)
