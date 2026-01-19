from django.db import transaction
from core.models import Lead, Customer


@transaction.atomic
def convert_lead_to_customer(lead: Lead, user):
    if lead.is_converted:
        raise ValueError("Lead is already converted")

    # Permission check (extra safety)
    if user.role not in ["admin", "manager"] and lead.assigned_to != user:
        raise PermissionError("You cannot convert this lead")

    # Prevent duplicate customer
    if Customer.objects.filter(email=lead.email).exists():
        raise ValueError("Customer with this email already exists")

    customer = Customer.objects.create(
        name=lead.name, email=lead.email, phone=lead.phone, owner=lead.assigned_to
    )

    lead.is_converted = True
    lead.status = "qualified"
    lead.save()

    return customer
