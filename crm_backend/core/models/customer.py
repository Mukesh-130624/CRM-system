from django.db import models
from core.models.base import TimeStampedModel
from django.conf import settings


class Customer(TimeStampedModel):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    company = models.CharField(max_length=255, blank=True)

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name="customers",
    )

    def __str__(self):
        return self.name
