from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from apps.usuario.models import Usuario

# Register your models here.

@admin.register(Usuario)
class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password', 'email','rol')}),
        

    )