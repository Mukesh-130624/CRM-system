from django.db import models
from core.models.base import TimeStampedModel
from django.conf import settings


class Lead(TimeStampedModel):
    STATUS_CHOICES = (
        ("new", "New"),
        ("contacted", "Contacted"),
        ("qualified", "Qualified"),
        ("lost", "Lost"),
    )

    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    is_converted = models.BooleanField(default=False)

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="new")

    assigned_to = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name="leads",
    )

    def __str__(self):
        return f"{self.name} - {self.status}"
