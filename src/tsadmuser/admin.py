from django.contrib import admin
from .models import TSAdmUserDB

class UserAdmin(admin.ModelAdmin):
    pass

admin.site.register(TSAdmUserDB, UserAdmin)
