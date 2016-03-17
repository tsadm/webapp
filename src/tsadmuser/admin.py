from django.contrib import admin
from .models import UserDB

class UserAdmin(admin.ModelAdmin):
    pass

admin.site.register(UserDB, UserAdmin)
