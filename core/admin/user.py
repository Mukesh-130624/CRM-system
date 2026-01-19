from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from core.models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ("username", "email", "role", "is_active", "is_staff")
    list_filter = ("role", "is_active")
    search_fields = ("username", "email")

    fieldsets = BaseUserAdmin.fieldsets + (("CRM Info", {"fields": ("role", "phone")}),)
