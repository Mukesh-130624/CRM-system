from django.contrib import admin
from core.models import Lead


@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "status", "assigned_to", "created_at")
    list_filter = ("status", "assigned_to")
    search_fields = ("name", "email")
    ordering = ("-created_at",)

    readonly_fields = ("created_at", "updated_at")
