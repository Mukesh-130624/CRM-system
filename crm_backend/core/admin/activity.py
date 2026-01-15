from django.contrib import admin
from core.models import Activity


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ("activity_type", "customer", "performed_by", "activity_date")

    list_filter = ("activity_type", "performed_by")
    search_fields = ("customer__name",)
    ordering = ("-activity_date",)
