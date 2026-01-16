from django.db import models
from django.conf import settings
from core.models.base import TimeStampedModel
from core.models.customer import Customer
from core.models.lead import Lead
from core.models.deal import Deal
from django.core.exceptions import ValidationError


class Task(TimeStampedModel):
    STATUS_CHOICES = (
        ("pending", "Pending"),
        ("completed", "Completed"),
        ("overdue", "Overdue"),
    )

    PRIORITY_CHOICES = (
        ("low", "Low"),
        ("medium", "Medium"),
        ("high", "High"),
    )

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")
    priority = models.CharField(
        max_length=20, choices=PRIORITY_CHOICES, default="medium"
    )

    due_date = models.DateTimeField()

    assigned_to = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name="tasks",
    )

    class Meta:
        constraints = [
            models.CheckConstraint(
                condition=models.Q(status__in=["pending", "completed", "overdue"]),
                name="task_status_valid",
            )
        ]
        indexes = [
            models.Index(fields=["assigned_to", "status"]),
            models.Index(fields=["due_date"]),
        ]

    # Task associations (only one should be used in practice)
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, null=True, blank=True, related_name="tasks"
    )

    lead = models.ForeignKey(
        Lead, on_delete=models.CASCADE, null=True, blank=True, related_name="tasks"
    )

    deal = models.ForeignKey(
        Deal, on_delete=models.CASCADE, null=True, blank=True, related_name="tasks"
    )

    def clean(self):
        links = [self.customer, self.lead, self.deal]
        if sum(link is not None for link in links) != 1:
            raise ValidationError(
                "Task must be linked to exactly one: Customer, Lead, or Deal."
            )

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} ({self.status})"
