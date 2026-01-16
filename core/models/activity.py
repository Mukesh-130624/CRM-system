from django.db import models
from core.models.base import TimeStampedModel
from django.conf import settings
from core.models.customer import Customer


class Activity(TimeStampedModel):
    ACTIVITY_TYPE = (
        ("call", "Call"),
        ("email", "Email"),
        ("meeting", "Meeting"),
    )

    activity_type = models.CharField(max_length=20, choices=ACTIVITY_TYPE)

    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, related_name="activities"
    )

    notes = models.TextField()

    performed_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True
    )

    activity_date = models.DateTimeField()

    def __str__(self):
        return f"{self.activity_type} - {self.customer.name}"
