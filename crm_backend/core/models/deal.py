from django.db import models
from core.models.base import TimeStampedModel
from core.models.customer import Customer
from django.conf import settings


class Deal(TimeStampedModel):
    STAGE_CHOICES = (
        ("prospecting", "Prospecting"),
        ("proposal", "Proposal"),
        ("negotiation", "Negotiation"),
        ("won", "Won"),
        ("lost", "Lost"),
    )

    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, related_name="deals"
    )

    title = models.CharField(max_length=255)
    value = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        constraints = [
            models.CheckConstraint(
                condition=models.Q(value__gt=0), name="deal_value_positive"
            )
        ]

    stage = models.CharField(
        max_length=20, choices=STAGE_CHOICES, default="prospecting"
    )

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name="deals",
    )

    expected_close_date = models.DateField()

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["title", "owner"], name="unique_owner_deal_title"
            )
        ]
        indexes = [
            models.Index(fields=["stage"]),
            models.Index(fields=["expected_close_date"]),
        ]

    def __str__(self):
        return self.title
