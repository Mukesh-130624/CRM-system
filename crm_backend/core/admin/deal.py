from django.contrib import admin
from core.models import Deal


@admin.register(Deal)
class DealAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "customer",
        "value",
        "stage",
        "owner",
        "expected_close_date",
        "created_at",
    )

    list_filter = ("stage", "owner")
    search_fields = ("title", "customer__name")
    ordering = ("-created_at",)

    readonly_fields = ("created_at", "updated_at")
