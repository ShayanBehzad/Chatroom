from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username']
    filter_horizontal = ('connections',)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)