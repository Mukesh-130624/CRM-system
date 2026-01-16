from django.contrib import admin
from core.models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "status",
        "priority",
        "assigned_to",
        "due_date",
        "created_at",
    )

    list_filter = ("status", "priority", "assigned_to")
    search_fields = ("title", "description")
    ordering = ("due_date",)

    readonly_fields = ("created_at", "updated_at")

    def save_model(self, request, obj, form, change):
        obj.full_clean()  # Enforce business rules in admin
        super().save_model(request, obj, form, change)
