from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from apps.usuario.models import Usuario

@admin.register(Usuario)
class UserAdmin(BaseUserAdmin):
       fieldsets = (
        (None, {'fields':('username', 'password')}),
        ('Personal info', {'fields':('firts_name', 'last_name', 'email')}),
        ('Permissions', {'fields': ('is_activate', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )