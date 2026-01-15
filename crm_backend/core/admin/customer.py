from django.contrib import admin
from core.models import Customer


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone", "company", "owner", "created_at")
    list_filter = ("owner", "created_at")
    search_fields = ("name", "email", "company")
    ordering = ("-created_at",)

    readonly_fields = ("created_at", "updated_at")
